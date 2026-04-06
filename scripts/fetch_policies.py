"""
Policy Fetcher
==============
Fetches public AI policies from major providers (OpenAI, Anthropic, Google, Meta, Apple, Samsung).
Stores raw HTML + extracted text in documents/<company>/ for later analysis.

Usage:
    python scripts/fetch_policies.py
"""

import os
import json
import time
from pathlib import Path
from datetime import datetime
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# ─────────────────────────────────────────────
#  Company Policy URLs
# ─────────────────────────────────────────────
POLICY_SOURCES = {
    "openai": {
        "name": "OpenAI",
        "ticker": "PRIVATE",
        "urls": {
            "terms_of_service": "https://openai.com/policies/terms-of-use",
            "privacy_policy": "https://openai.com/policies/privacy-policy",
            "usage_policies": "https://openai.com/policies/usage-policies",
            "api_terms": "https://openai.com/policies/api-terms",
        }
    },
    "anthropic": {
        "name": "Anthropic",
        "ticker": "PRIVATE",
        "urls": {
            "terms_of_service": "https://www.anthropic.com/terms",
            "privacy_policy": "https://www.anthropic.com/privacy",
            "acceptable_use": "https://www.anthropic.com/acceptable-use-policy",
            "claude_docs": "https://docs.anthropic.com/",
        }
    },
    "google": {
        "name": "Google / Alphabet",
        "ticker": "GOOGL",
        "urls": {
            "terms_of_service": "https://policies.google.com/terms",
            "privacy_policy": "https://policies.google.com/privacy",
            "ai_principles": "https://ai.google/principles/",
            "gemini_terms": "https://support.google.com/generativeai/answer/13392725",
        }
    },
    "meta": {
        "name": "Meta Platforms",
        "ticker": "META",
        "urls": {
            "terms_of_service": "https://www.meta.com/legal/terms/",
            "data_policy": "https://www.meta.com/en/privacy/your-privacy/",
            "ai_principles": "https://www.meta.com/ai/research/",
            "llama_license": "https://github.com/facebookresearch/llama/blob/main/LICENSE",
        }
    },
    "apple": {
        "name": "Apple",
        "ticker": "AAPL",
        "urls": {
            "terms_of_service": "https://www.apple.com/legal/internet-services/terms/site.html",
            "privacy_policy": "https://www.apple.com/privacy/",
            "ai_principles": "https://www.apple.com/privacy/",
            "siri_privacy": "https://support.apple.com/en-us/HT209084",
        }
    },
    "samsung": {
        "name": "Samsung Electronics",
        "ticker": "005930.KS",
        "urls": {
            "terms_of_service": "https://www.samsung.com/common/terms-of-use/",
            "privacy_policy": "https://www.samsung.com/us/privacy/",
            "ai_ethics": "https://www.samsung.com/us/about-samsung/corporate-responsibility/",
            "galaxy_ai": "https://www.samsung.com/us/galaxy-ai/",
        }
    }
}

# ─────────────────────────────────────────────
#  Fetch & Store
# ─────────────────────────────────────────────

def create_docs_structure():
    """Create documents/ folder if it doesn't exist."""
    docs_dir = Path("documents")
    docs_dir.mkdir(exist_ok=True)
    return docs_dir

def fetch_url_safe(url: str, timeout=10) -> str:
    """Safely fetch a URL with error handling."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urlopen(url, timeout=timeout)
        content = req.read().decode('utf-8', errors='ignore')
        return content
    except HTTPError as e:
        print(f"  ⚠️  HTTP Error {e.code}: {url}")
        return ""
    except URLError as e:
        print(f"  ⚠️  URL Error: {url}")
        return ""
    except Exception as e:
        print(f"  ⚠️  Error fetching {url}: {str(e)[:80]}")
        return ""

def extract_text_from_html(html: str) -> str:
    """Simple text extraction from HTML (removes tags)."""
    import re
    # Remove script and style elements
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '\n', html)
    # Clean up whitespace
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def fetch_and_store_policies(docs_dir: Path):
    """Fetch policies for all companies and store them."""
    print("\n" + "="*60)
    print("  AI Policy Fetcher — Collecting Public Policies")
    print("="*60 + "\n")

    for company_id, company_info in POLICY_SOURCES.items():
        print(f"📥 Fetching policies for {company_info['name']}...")
        
        company_dir = docs_dir / company_id
        company_dir.mkdir(exist_ok=True)
        
        metadata = {
            "company": company_info['name'],
            "ticker": company_info['ticker'],
            "fetched_at": datetime.now().isoformat(),
            "policies": {}
        }
        
        for policy_name, url in company_info['urls'].items():
            print(f"  → {policy_name}: {url[:60]}...")
            
            html_content = fetch_url_safe(url)
            
            if html_content:
                # Save HTML
                html_file = company_dir / f"{policy_name}.html"
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                # Extract and save text
                text_content = extract_text_from_html(html_content)
                text_file = company_dir / f"{policy_name}.txt"
                with open(text_file, 'w', encoding='utf-8') as f:
                    f.write(text_content)
                
                # Store metadata
                metadata['policies'][policy_name] = {
                    "url": url,
                    "status": "fetched",
                    "size_bytes": len(html_content),
                    "text_length": len(text_content)
                }
                
                print(f"    ✓ Saved ({len(html_content)} bytes)")
            else:
                metadata['policies'][policy_name] = {
                    "url": url,
                    "status": "failed_to_fetch"
                }
            
            # Rate limiting
            time.sleep(1)
        
        # Save metadata
        metadata_file = company_dir / "metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"  ✓ {company_info['name']} complete.\n")

if __name__ == "__main__":
    docs_dir = create_docs_structure()
    fetch_and_store_policies(docs_dir)
    print("\n✓ Policy collection complete!")
    print(f"  Documents stored in: {docs_dir.absolute()}")
