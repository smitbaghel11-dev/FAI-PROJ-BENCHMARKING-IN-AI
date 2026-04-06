# CEPA Enhanced Features - Concerning Policies & Source Links

## Overview

CEPA now includes two new critical sections for each company comparison:

### 1. **⚠️ Concerning Policies & Red Flags**
Highlights 1-2 key policy concerns for each company with severity levels.

### 2. **📄 Policy Documents & Source Links**
Provides direct links to official policy documents for independent verification.

---

## What's Included

### Apple Inc.
**Concerning Policies:**
- ⚠️ MEDIUM: Limited Model Transparency - On-device ML models operate as black boxes
- 🔴 HIGH: Siri Audio Recording Practices - Past contractor hearing controversies

**Policy Sources (3):**
- ⚖️ Apple Privacy Policy - https://www.apple.com/privacy/
- 🔒 Apple Machine Learning Privacy - https://www.apple.com/privacy/features/
- 📢 Apple Newsroom (AI & Privacy) - https://www.apple.com/newsroom/

---

### OpenAI
**Concerning Policies:**
- 🔴 HIGH: Data Training Without Explicit Consent - Internet-scraped data used without individual consent
- 🟡 MEDIUM: Limited Liability - Terms limit OpenAI's responsibility for generated content

**Policy Sources (4):**
- ⚖️ OpenAI Usage Policies - https://openai.com/policies/usage-policies
- 🔒 OpenAI Privacy Policy - https://openai.com/privacy
- 🛡️ OpenAI Safety & Research - https://openai.com/safety
- 📜 OpenAI Terms of Service - https://openai.com/terms

---

### Anthropic
**Concerning Policies:**
- 🟢 LOW: Limited Public Transparency on Training Data - Constitutional AI published but data sources unclear
- 🟢 LOW: Rapid Evolution of Safety Measures - As young company, long-term policy sustainability unproven

**Policy Sources (4):**
- 🛡️ Anthropic Safety Documentation - https://www.anthropic.com/safety
- 📊 Constitutional AI Research - https://www.anthropic.com/research
- 🔒 Anthropic Privacy Policy - https://www.anthropic.com/privacy
- 📋 Claude Responsible Use Policy - https://www.anthropic.com/claude/responsible-use-policy

---

### Google
**Concerning Policies:**
- 🔴 HIGH: Ad-Targeting AI Lacks Transparency - Most powerful AI used for ads with minimal transparency
- 🟡 MEDIUM: Dual-Use AI Research - AI published for surveillance and other dual-use applications

**Policy Sources (4):**
- ⚖️ Google AI Principles - https://ai.google/principles/
- 🔒 Google Privacy Policy - https://policies.google.com/privacy
- 📋 Google Responsible AI Practices - https://developers.google.com/machine-learning/responsible-ai
- 🎯 Bard AI Safety - https://support.google.com/bard/

---

### Meta Platforms
**Concerning Policies:**
- 🔴 HIGH: History of Privacy Violations - Cambridge Analytica, data breaches eroded user trust
- 🔴 HIGH: Weak User Control Over ML Data - Limited opt-out from ML training, especially ad targeting

**Policy Sources (5):**
- ⚖️ Meta AI Ethics - https://www.meta.com/ai/
- 🔒 Meta Privacy Policy - https://www.meta.com/privacy/
- 📊 Meta AI Ethics Research - https://www.meta.com/research/ai-ethics/
- 🚫 Community Standards (Moderation) - https://www.facebook.com/communitystandards/
- 📦 Llama Model Community License - https://github.com/facebookresearch/llama

---

### DeepSeek
**Concerning Policies:**
- 🔴 HIGH: Regulatory Uncertainty - China-based company operating under different regulatory frameworks (CAC)
- 🔴 HIGH: Limited Public Policy Documentation - Minimal transparency; less rigorous than Western competitors

**Policy Sources (3):**
- 📜 DeepSeek Terms of Service - https://www.deepseek.com/terms
- 🔒 DeepSeek Privacy Policy - https://www.deepseek.com/privacy
- 📋 DeepSeek API Documentation - https://platform.deepseek.com/api-docs

---

## Severity Levels

| Icon | Level | Meaning |
|------|-------|---------|
| 🔴 | **HIGH** | Critical concern affecting user rights or data safety |
| 🟡 | **MEDIUM** | Significant concern but with workarounds or context |
| 🟢 | **LOW** | Minor concern or limitation; doesn't affect core policies |

---

## How to Use

### For Users:
1. **Run a comparison** between any two companies
2. **Scroll to "Concerning Policies"** section to see red flags
3. **Scroll to "Policy Documents"** section to access official sources
4. **Click on policy links** to verify claims independently
5. **Use severity badges** to understand concern levels

### For Researchers:
1. All policy links point to **official company sources**
2. No secondary/interpreted sources - direct from companies
3. Perfect for academic papers and policy analysis
4. Links are maintained and updated quarterly

### For Auditors:
1. **Verify each claim** by visiting official policy documents
2. **Track policy changes** by revisiting links periodically
3. **Compare policies** across companies using side-by-side view
4. **Export data** for compliance audits (CSV/JSON download)

---

## Data Integrity

✅ **Verified sources**: All URLs point to official company websites  
✅ **Manual curation**: Each concern is based on published policies  
✅ **Severity assigned**: Based on impact on user rights/data protection  
✅ **Searchable**: All text is indexed and searchable  
✅ **Linkable**: Each policy document has a direct URL  

---

## Technical Implementation

### Frontend (JavaScript)
- `renderConcerningPolicies()` - Displays concern cards with severity badges
- `renderPolicyDocuments()` - Creates clickable policy source links
- Dynamic emoji assignment based on policy type
- Responsive grid layout (1-2 columns)

### Backend (Flask)
- New field in API response: `companies_data`
- Returns both companies' concerning policies & sources
- Includes metadata for display

### Data Structure (JSON)
```json
{
  "concerning_policies": [
    {
      "concern": "Title of concern",
      "description": "Detailed explanation",
      "severity": "high|medium|low"
    }
  ],
  "policy_sources": [
    {
      "title": "Document name",
      "url": "https://...",
      "type": "Category"
    }
  ]
}
```

### Styling (CSS)
- Gradient backgrounds reflecting concern type
- Hover animations for policy document links
- Severity color coding (red/orange/green)
- Type-based emoji assignment

---

## Future Enhancements

- [ ] Policy change tracking (compare old vs new versions)
- [ ] Timeline view showing policy evolution
- [ ] Community flag/comment system on concerns
- [ ] AI-powered concern detection from policy text
- [ ] Integration with GDPR/regulatory compliance APIs
- [ ] PDF download of policy comparison reports

---

## Contact & Updates

- **Last Updated**: April 5, 2026
- **Next Review**: July 5, 2026 (quarterly)
- **Data Source**: Official company policy documents
- **Verification**: Manual review by policy experts

---

*CEPA - Comparative Ethical Policy Auditor*  
*Transparent AI policy analysis for educational & research purposes*
