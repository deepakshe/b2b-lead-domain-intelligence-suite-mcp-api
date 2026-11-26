# All-in-One B2B Lead & Domain Intelligence Suite (Contacts, MX & Security)

[![Apify Store](https://img.shields.io/badge/Apify_Store-Run_on_Apify-blue?style=for-the-badge&logo=apify)](https://apify.com/deepaksheoran172/b2b-lead-domain-intelligence-suite)
[![deepakshe/b2b-lead-domain-intelligence-suite-mcp-api MCP server](https://glama.ai/mcp/servers/deepakshe/b2b-lead-domain-intelligence-suite-mcp-api/badges/score.svg)](https://glama.ai/mcp/servers/deepakshe/b2b-lead-domain-intelligence-suite-mcp-api)
[![MCP Server](https://img.shields.io/badge/MCP-Model_Context_Protocol-purple?style=for-the-badge)](https://modelcontextprotocol.io)
[![Pricing](https://img.shields.io/badge/Pricing-%240.008_per_Lead-green?style=for-the-badge)](https://apify.com/deepaksheoran172/b2b-lead-domain-intelligence-suite)
[![Maintenance](https://img.shields.io/badge/Status-100%25_Operational-emerald?style=for-the-badge)](https://apify.com/deepaksheoran172/b2b-lead-domain-intelligence-suite)

> **The ultimate B2B data enrichment engine. Extract executive emails, validate MX deliverability, audit DNS DMARC/SPF/SSL security posture, and detect e-commerce tech stacks in a single unified run.**

---

## ⚡ The Pain vs. The Relief

### 🛑 The Brutal B2B Prospecting Reality
Building a high-converting outbound lead list currently requires subscribing to 4 separate tools:
1. A website contact scraper ($50/month)
2. An email verifier to prevent domain blacklists ($0.03/check)
3. A DNS/DMARC security auditor to find corporate vulnerability angles ($150/seat)
4. A technology stack detection plugin ($99/month)

You waste 4 hours stitching together CSVs in Excel, only to discover invalid emails that burn your domain reputation and bounce back.

### ✅ The 1-Click Automated Relief
**B2B Lead & Domain Intelligence Suite** consolidates this entire pipeline into **1 single cloud execution**:
- Input: Just a list of corporate domain names (`stripe.com`, `mejuri.com`, `linear.app`).
- Output: 100% enriched, RFC-compliant master profiles featuring **verified emails, direct phone/WhatsApp numbers, DMARC/SPF security scores, and underlying CMS/e-commerce technologies**.
- Cost: **$0.008 per enriched lead** (vs $0.25+ on Apollo or ZoomInfo). **Zero proxy fees**.

---

## 📊 Side-by-Side Visual Proof

### What You Give (Input JSON):
```json
{
  "domains": [
    "stripe.com",
    "mejuri.com"
  ],
  "extractContacts": true,
  "verifyEmails": true,
  "auditDomainSecurity": true,
  "detectTechSignals": true
}
```

### What You Get (Clean Normalized Output):
```json
{
  "domain": "mejuri.com",
  "company_name": "Mejuri",
  "website_status": "ONLINE",
  "lead_quality_score": 95,
  "contacts": [
    {
      "email": "hello@mejuri.com",
      "status": "DELIVERABLE",
      "is_valid": true,
      "mx_host": "aspmx.l.google.com",
      "provider": "Google Workspace"
    }
  ],
  "phone_numbers": [
    "+1 (800) 555-0199"
  ],
  "social_links": {
    "linkedin": "https://linkedin.com/company/mejuri",
    "instagram": "https://instagram.com/mejuri"
  },
  "technology_signals": {
    "platform": "Shopify",
    "cdn": "Cloudflare",
    "server": "cloudflare",
    "frontend_frameworks": ["React", "Next.js"]
  },
  "security_posture": {
    "security_score": 90,
    "ssl_valid": true,
    "ssl_issuer": "Cloudflare Inc ECC CA-3",
    "spf_configured": true,
    "dmarc_configured": true,
    "dmarc_policy": "reject"
  },
  "enriched_at": "2026-10-30T23:20:00Z"
}
```

---

## 🚀 Quickstart: 1-Line cURL (Test in 2 Seconds)

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~b2b-lead-domain-intelligence-suite/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"domains": ["stripe.com", "mejuri.com"], "extractContacts": true, "verifyEmails": true, "auditDomainSecurity": true, "detectTechSignals": true}'
```

---

## 🤖 Claude Desktop & Cursor MCP Server Setup

Turn your AI agent into an autonomous B2B researcher. Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "b2b-lead-domain-intelligence": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN",
        "ACTOR_NAME": "deepaksheoran172/b2b-lead-domain-intelligence-suite"
      }
    }
  }
}
```

---

## 🔄 Daily Automation via n8n / Make.com / Zapier

Convert this actor into a perpetual weekly outbound prospecting pipeline:

```
[Google Sheets / CRM: New Domains]
         │
         ▼
[HTTP Request Node: Apify b2b-lead-domain-intelligence-suite]
         │
         ▼
[Filter: Lead Score >= 80 & DMARC Policy == 'reject']
         │
         ▼
[Instantly / Smartlead: Trigger Guarded Cold Email Sequence]
```

---

## 💰 Anchored Pricing & 60% Launch Discount

| Provider | Contacts | MX Verification | DMARC/Security Audit | Tech Stack | Price per 1k Leads |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Apollo / ZoomInfo** | ✅ | Paid Add-on | ❌ | Partial | $250.00 |
| **Clearbit** | ✅ | ❌ | ❌ | ✅ | $180.00 |
| **BuiltWith + MillionVerifier** | ❌ | ✅ | ❌ | ✅ | $120.00 |
| **Our Master Suite (Apify)** | **✅** | **✅** | **✅** | **✅** | **$8.00** |

👉 **You save 96% while getting 4x the data depth in a single run.**

---

## 🛡️ 100% Automated Self-Service & Zero-DM Guarantee

- **Pure Self-Service:** Runs autonomously via Apify Cloud API. No sales calls, manual configuration, or onboarding tickets needed.
- **Pay-Per-Result:** Only successful output items are billed ($0.008 per enriched lead). Zero-charge on failed executions.
- **API Documentation:** For key creation, webhooks, and concurrency settings, see [Apify Docs](https://docs.apify.com/platform/actors/running/api).

---

## 📄 License & Compliance

- **Zero-Proxy Architecture:** Runs asynchronously with zero IP rotation overhead.
- **B2B Legitimate Interest:** Crawls only public corporate contact pages and DNS records.
- **RFC 4180 / ISO 8601 Compliant:** All timestamps UTC, CSV formatted with zero spreadsheet formula injection risks.
