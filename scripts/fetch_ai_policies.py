#!/usr/bin/env python3
"""
Fetch official AI policies from company sources.
This script fetches real AI policy documents and extracts key information.
"""

import os
import json
import requests
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Official AI policy URLs for each company
AI_POLICY_SOURCES = {
    "apple": {
        "name": "Apple Inc.",
        "urls": [
            ("Privacy Policy", "https://www.apple.com/privacy/"),
            ("Privacy Features", "https://www.apple.com/privacy/features/"),
            ("Newsroom - ML/AI", "https://www.apple.com/newsroom/"),
        ]
    },
    "openai": {
        "name": "OpenAI",
        "urls": [
            ("Usage Policies", "https://openai.com/policies/usage-policies"),
            ("Privacy Policy", "https://openai.com/privacy"),
            ("Safety", "https://openai.com/safety"),
            ("Terms of Service", "https://openai.com/terms"),
        ]
    },
    "google": {
        "name": "Google",
        "urls": [
            ("AI Principles", "https://ai.google/principles/"),
            ("Privacy Policy", "https://policies.google.com/privacy"),
            ("Responsible AI", "https://developers.google.com/machine-learning/responsible-ai"),
            ("Trust & Safety", "https://blog.google/around-the-globe/google-asia/our-approach-to-trust-and-safety/"),
        ]
    },
    "anthropic": {
        "name": "Anthropic",
        "urls": [
            ("Constitutional AI", "https://www.anthropic.com/research"),
            ("Privacy Policy", "https://www.anthropic.com/privacy"),
            ("Responsible Use", "https://www.anthropic.com/claude/responsible-use-policy"),
            ("Safety", "https://www.anthropic.com/safety"),
        ]
    },
    "meta": {
        "name": "Meta Platforms",
        "urls": [
            ("AI Ethics", "https://www.meta.com/ai/"),
            ("Privacy Policy", "https://www.meta.com/privacy/"),
            ("AI Ethics Research", "https://www.meta.com/research/ai-ethics/"),
            ("Community Standards", "https://www.facebook.com/communitystandards/"),
        ]
    },
    "deepseek": {
        "name": "DeepSeek",
        "urls": [
            ("Terms of Service", "https://www.deepseek.com/terms"),
            ("Privacy Policy", "https://www.deepseek.com/privacy"),
            ("API Docs", "https://platform.deepseek.com/api-docs"),
            ("Blog", "https://www.deepseek.com/blog"),
        ]
    }
}

class PolicyFetcher:
    def __init__(self, output_dir="documents"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.timeout = 10
        
    def fetch_url(self, url):
        """Fetch content from URL with error handling."""
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.warning(f"Failed to fetch {url}: {e}")
            return None
    
    def save_policy(self, company_id, policy_name, content):
        """Save fetched policy to file."""
        company_dir = self.output_dir / company_id / "ai_policies"
        company_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filename from policy name
        filename = policy_name.lower().replace(" ", "_").replace("/", "_") + ".html"
        filepath = company_dir / filename
        
        # Save content
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Saved: {filepath}")
            return str(filepath)
        except Exception as e:
            logger.error(f"Failed to save {filepath}: {e}")
            return None
    
    def fetch_company_policies(self, company_id, company_data):
        """Fetch all policies for a company."""
        logger.info(f"\n{'='*60}")
        logger.info(f"Fetching policies for: {company_data['name']}")
        logger.info(f"{'='*60}")
        
        policies_fetched = []
        
        for policy_name, url in company_data['urls']:
            content = self.fetch_url(url)
            if content:
                saved_path = self.save_policy(company_id, policy_name, content)
                policies_fetched.append({
                    "name": policy_name,
                    "url": url,
                    "saved_at": datetime.now().isoformat(),
                    "file": saved_path
                })
            
            # Rate limiting
            time.sleep(2)
        
        # Save metadata
        metadata_file = self.output_dir / company_id / "ai_policies_metadata.json"
        metadata_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(metadata_file, 'w') as f:
            json.dump({
                "company": company_data['name'],
                "fetched_at": datetime.now().isoformat(),
                "policies": policies_fetched,
                "total_fetched": len(policies_fetched)
            }, f, indent=2)
        
        logger.info(f"✓ Fetched {len(policies_fetched)} policies")
        
        return policies_fetched
    
    def fetch_all(self):
        """Fetch policies for all companies."""
        results = {}
        
        for company_id, company_data in AI_POLICY_SOURCES.items():
            results[company_id] = self.fetch_company_policies(company_id, company_data)
        
        # Save summary
        summary_file = self.output_dir / "fetch_summary.json"
        with open(summary_file, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "companies": {
                    company_id: {
                        "name": AI_POLICY_SOURCES[company_id]['name'],
                        "policies_fetched": len(results[company_id]),
                        "policies": results[company_id]
                    }
                    for company_id, results_list in results.items()
                }
            }, f, indent=2)
        
        logger.info(f"\n{'='*60}")
        logger.info(f"Summary saved to: {summary_file}")
        logger.info(f"{'='*60}")
        
        return results

def main():
    """Main entry point."""
    fetcher = PolicyFetcher()
    
    logger.info("Starting AI Policy Fetcher")
    logger.info(f"Fetching {len(AI_POLICY_SOURCES)} companies")
    
    results = fetcher.fetch_all()
    
    logger.info("\n" + "="*60)
    logger.info("FETCH COMPLETE")
    logger.info("="*60)
    logger.info(f"✓ Total companies processed: {len(results)}")
    total_policies = sum(len(v) for v in results.values())
    logger.info(f"✓ Total policies fetched: {total_policies}")
    logger.info(f"✓ Documents saved to: ./documents/")
    
    # Print source mapping for reference
    logger.info("\n" + "="*60)
    logger.info("POLICY SOURCES SUMMARY")
    logger.info("="*60)
    for company_id, company_data in AI_POLICY_SOURCES.items():
        logger.info(f"\n{company_data['name']}:")
        for policy_name, url in company_data['urls']:
            logger.info(f"  - {policy_name}: {url}")

if __name__ == "__main__":
    main()
