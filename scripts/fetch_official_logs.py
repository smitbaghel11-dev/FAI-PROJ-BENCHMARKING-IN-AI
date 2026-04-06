#!/usr/bin/env python3
"""
Fetch Official Company Logs, Press Releases & Public Statements
================================================================

This script collects official communications from each company:
- Press releases and announcements
- Official blog posts about AI policies
- SEC/regulatory filings (where applicable)
- Public statements on AI safety and ethics

Target Companies:
  • Apple Inc.
  • Samsung Electronics
  • OpenAI
  • Anthropic
  • Google / Alphabet
  • Meta Platforms

Output: Stores raw text in documents/<company>/official_logs/ folder
"""

import os
import json
import time
import socket
import ssl
import urllib.request
import urllib.error
from urllib.parse import urljoin
from pathlib import Path
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "documents")

# Official company log sources
COMPANY_LOGS = {
    "apple": {
        "name": "Apple Inc.",
        "sources": [
            {
                "name": "Apple Newsroom - AI & Privacy",
                "url": "https://www.apple.com/newsroom/",
                "description": "Official press releases on AI, privacy, and technology"
            },
            {
                "name": "Apple Privacy Documentation",
                "url": "https://www.apple.com/privacy/",
                "description": "Official privacy policies and AI transparency docs"
            },
            {
                "name": "Apple Terms of Service",
                "url": "https://www.apple.com/legal/terms/",
                "description": "Legal terms covering AI service usage and liability"
            }
        ]
    },
    "samsung": {
        "name": "Samsung Electronics",
        "sources": [
            {
                "name": "Samsung Newsroom",
                "url": "https://news.samsung.com/",
                "description": "Official press releases and announcements"
            },
            {
                "name": "Samsung AI & Research",
                "url": "https://www.samsung.com/semiconductor/about/ai-research/",
                "description": "AI research initiatives and policy statements"
            },
            {
                "name": "Samsung Privacy Policy",
                "url": "https://www.samsung.com/common/privacy/",
                "description": "Data privacy and AI usage terms"
            }
        ]
    },
    "openai": {
        "name": "OpenAI",
        "sources": [
            {
                "name": "OpenAI Blog - Safety & Policy",
                "url": "https://openai.com/blog/",
                "description": "Official blog posts on AI safety, ethics, and policy"
            },
            {
                "name": "OpenAI Terms of Use",
                "url": "https://openai.com/terms/",
                "description": "Official terms covering API usage, liability, and responsibilities"
            },
            {
                "name": "OpenAI Safety & Alignment",
                "url": "https://openai.com/safety/",
                "description": "Public documentation on safety practices and alignment research"
            },
            {
                "name": "OpenAI Press Releases",
                "url": "https://openai.com/press/",
                "description": "Official press releases and announcements"
            }
        ]
    },
    "anthropic": {
        "name": "Anthropic",
        "sources": [
            {
                "name": "Anthropic Research & Policy",
                "url": "https://www.anthropic.com/research",
                "description": "Research publications on AI safety and policy"
            },
            {
                "name": "Anthropic Blog",
                "url": "https://www.anthropic.com/blog",
                "description": "Official blog on responsible AI development"
            },
            {
                "name": "Anthropic Terms of Service",
                "url": "https://www.anthropic.com/legal/terms",
                "description": "API terms, usage policies, and liability clauses"
            },
            {
                "name": "Anthropic Press",
                "url": "https://www.anthropic.com/press",
                "description": "Official press releases and media updates"
            }
        ]
    },
    "google": {
        "name": "Google / Alphabet",
        "sources": [
            {
                "name": "Google AI Safety & Ethics",
                "url": "https://ai.google/safety/",
                "description": "Official AI safety and ethics framework"
            },
            {
                "name": "Google Privacy Policy",
                "url": "https://policies.google.com/privacy",
                "description": "Data privacy and AI usage policies"
            },
            {
                "name": "Google Terms of Service",
                "url": "https://policies.google.com/terms",
                "description": "Terms covering API usage and liability"
            },
            {
                "name": "Google Blog - AI",
                "url": "https://blog.google/technology/ai/",
                "description": "Official announcements on AI initiatives"
            },
            {
                "name": "Alphabet Investor Relations",
                "url": "https://abc.xyz/investor/",
                "description": "SEC filings and regulatory statements"
            }
        ]
    },
    "meta": {
        "name": "Meta Platforms",
        "sources": [
            {
                "name": "Meta Newsroom - AI",
                "url": "https://www.meta.com/newsroom/",
                "description": "Official press releases and announcements"
            },
            {
                "name": "Meta Privacy & Safety",
                "url": "https://www.meta.com/privacy-center/",
                "description": "Privacy policies and AI safety documentation"
            },
            {
                "name": "Meta Data Use Policy",
                "url": "https://www.meta.com/legal/data-policy/",
                "description": "Data usage and AI terms of service"
            },
            {
                "name": "Meta Research - AI",
                "url": "https://research.facebook.com/",
                "description": "Research publications and AI safety initiatives"
            }
        ]
    }
}


def fetch_url_safe(url: str, timeout: int = 10) -> str:
    """
    Safely fetch URL content with error handling.
    Returns raw HTML/text or error message.
    """
    try:
        # Create SSL context that bypasses certificate verification (dev only)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        )
        with urllib.request.urlopen(req, timeout=timeout, context=ssl_context) as response:
            content = response.read().decode("utf-8", errors="ignore")
            return content
    except urllib.error.URLError as e:
        return f"URLError: {str(e)}"
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}: {e.reason}"
    except socket.timeout:
        return "Timeout: Connection timed out"
    except Exception as e:
        return f"Error: {str(e)}"


def extract_text_from_html(html: str) -> str:
    """
    Basic HTML text extraction (removes tags, scripts).
    """
    import re
    # Remove script and style
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    html = re.sub(r"<[^>]+>", " ", html)
    # Clean whitespace
    html = re.sub(r"\s+", " ", html).strip()
    return html


def fetch_and_store_logs():
    """
    Main function: Fetch official logs for each company and store locally.
    """
    for company_id, company_data in COMPANY_LOGS.items():
        print(f"\n{'='*70}")
        print(f"Fetching logs for: {company_data['name']}")
        print(f"{'='*70}")

        # Create company-specific log directory
        company_log_dir = os.path.join(DOCS_DIR, company_id, "official_logs")
        os.makedirs(company_log_dir, exist_ok=True)

        # Metadata file
        metadata = {
            "company": company_data["name"],
            "company_id": company_id,
            "fetch_date": datetime.now().isoformat(),
            "sources": []
        }

        for source_idx, source in enumerate(company_data["sources"], 1):
            print(f"\n  [{source_idx}/{len(company_data['sources'])}] Fetching: {source['name']}")
            print(f"  URL: {source['url']}")

            content = fetch_url_safe(source["url"])

            if content.startswith("URLError") or content.startswith("HTTP") or content.startswith("Error"):
                status = "❌ FAILED"
                print(f"  {status}: {content}")
                metadata["sources"].append({
                    "name": source["name"],
                    "url": source["url"],
                    "description": source["description"],
                    "status": "failed",
                    "error": content,
                    "file": None
                })
            else:
                status = "✅ SUCCESS"
                print(f"  {status}: Fetched {len(content)} characters")

                # Extract text
                text_content = extract_text_from_html(content)

                # Save raw HTML
                html_filename = f"{source_idx:02d}_{source['name'].lower().replace(' ', '_')}.html"
                html_filepath = os.path.join(company_log_dir, html_filename)
                with open(html_filepath, "w", encoding="utf-8") as f:
                    f.write(content)

                # Save extracted text
                text_filename = f"{source_idx:02d}_{source['name'].lower().replace(' ', '_')}.txt"
                text_filepath = os.path.join(company_log_dir, text_filename)
                with open(text_filepath, "w", encoding="utf-8") as f:
                    f.write(text_content)

                metadata["sources"].append({
                    "name": source["name"],
                    "url": source["url"],
                    "description": source["description"],
                    "status": "success",
                    "html_file": html_filename,
                    "text_file": text_filename,
                    "size_bytes": len(content)
                })

            # Rate limiting
            time.sleep(1)

        # Save metadata
        metadata_filepath = os.path.join(company_log_dir, "metadata.json")
        with open(metadata_filepath, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        print(f"\n  📁 Saved to: {company_log_dir}")
        print(f"  📋 Metadata: {metadata_filepath}")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("CEPA — Official Company Logs & Policy Fetcher")
    print("="*70)
    print("\nThis script fetches official company communications and policies.")
    print("Target: Press releases, blog posts, terms of service, and policy docs.")
    print(f"\nDocuments will be stored in: {DOCS_DIR}")
    print("\n")

    try:
        fetch_and_store_logs()
        print("\n" + "="*70)
        print("✅ Official logs fetch complete!")
        print("="*70 + "\n")
    except KeyboardInterrupt:
        print("\n\n⚠️  Fetch interrupted by user.")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {str(e)}")
