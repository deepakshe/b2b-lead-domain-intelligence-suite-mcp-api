#!/usr/bin/env python3
"""client.py
Zero-dependency Python client for b2b-lead-domain-intelligence-suite.
Calls Apify Cloud synchronously to enrich domains with executive contacts, MX validation, DMARC/SPF, and tech stack.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional

ACTOR_SLUG = "b2b-lead-domain-intelligence-suite"
DEFAULT_BASE_URL = f"https://api.apify.com/v2/acts/deepaksheoran172~{ACTOR_SLUG}/run-sync-get-dataset-items"

def run_b2b_lead_domain_intelligence(
    domains: List[str],
    extract_contacts: bool = True,
    verify_emails: bool = True,
    audit_security: bool = True,
    detect_tech: bool = True,
    apify_token: Optional[str] = None,
    timeout_sec: int = 180
) -> List[Dict[str, Any]]:
    """Enriches domains via Apify Cloud.
    
    Args:
        domains: List of company domains or URLs (e.g. ['stripe.com', 'mejuri.com'])
        extract_contacts: Crawl contact/about pages for executive emails and phones.
        verify_emails: Perform DNS MX and RFC validation on discovered emails.
        audit_security: Audit DNS SPF, DMARC enforcement, and SSL validity.
        detect_tech: Identify CMS, e-commerce engines, CDNs, and frameworks.
        apify_token: Apify API token. Defaults to os.environ.get('APIFY_TOKEN').
        timeout_sec: Timeout in seconds.
        
    Returns:
        List of enriched corporate intelligence records.
    """
    token = apify_token or os.environ.get("APIFY_TOKEN")
    if not token:
        raise ValueError("Apify token required. Set APIFY_TOKEN or pass apify_token parameter.")

    payload = {
        "domains": domains,
        "extractContacts": extract_contacts,
        "verifyEmails": verify_emails,
        "auditDomainSecurity": audit_security,
        "detectTechSignals": detect_tech
    }

    url = f"{DEFAULT_BASE_URL}?token={token}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as response:
            if response.status not in (200, 201):
                raise RuntimeError(f"Actor run returned HTTP {response.status}: {response.read().decode('utf-8')}")
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8") if e.fp else str(e)
        raise RuntimeError(f"HTTPError {e.code}: {err_msg}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"URLError connecting to Apify: {e.reason}") from e


if __name__ == "__main__":
    sample_domains = ["stripe.com", "mejuri.com", "linear.app"]
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        print("[!] APIFY_TOKEN not set in environment.")
        print("To run against live Apify cloud:")
        print("  export APIFY_TOKEN='your_token'")
        print("  python client.py")
        print("
Constructed payload:")
        print(json.dumps({"domains": sample_domains}, indent=2))
        sys.exit(0)

    print(f"[*] Running b2b-lead-domain-intelligence-suite for {sample_domains}...")
    try:
        results = run_b2b_lead_domain_intelligence(sample_domains, apify_token=token)
        print(f"[+] Success! Received {len(results)} enriched lead profiles:")
        print(json.dumps(results[:2], indent=2))
    except Exception as e:
        print(f"[-] Execution failed: {e}")
        sys.exit(1)
