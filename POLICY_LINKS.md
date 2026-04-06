# 🔗 Official AI Policy Sources - Ready to Fetch

## Quick Reference Links

### 🍎 **Apple Inc.**
- **Privacy & AI**: https://www.apple.com/privacy/
- **Privacy Features**: https://www.apple.com/privacy/features/
- **Newsroom**: https://www.apple.com/newsroom/ (search: "machine learning" + "AI")

### 🤖 **OpenAI**
- **Usage Policies**: https://openai.com/policies/usage-policies
- **Privacy Policy**: https://openai.com/privacy
- **Safety Research**: https://openai.com/safety
- **Terms of Service**: https://openai.com/terms

### 🔍 **Google**
- **AI Principles**: https://ai.google/principles/
- **Privacy Policy**: https://policies.google.com/privacy
- **Responsible AI**: https://developers.google.com/machine-learning/responsible-ai
- **Trust & Safety**: https://blog.google/around-the-globe/google-asia/our-approach-to-trust-and-safety/

### 🧠 **Anthropic**
- **Constitutional AI Research**: https://www.anthropic.com/research
- **Privacy Policy**: https://www.anthropic.com/privacy
- **Responsible Use**: https://www.anthropic.com/claude/responsible-use-policy
- **Safety**: https://www.anthropic.com/safety

### 👥 **Meta Platforms**
- **AI Ethics**: https://www.meta.com/ai/
- **Privacy Policy**: https://www.meta.com/privacy/
- **AI Ethics Research**: https://www.meta.com/research/ai-ethics/
- **Community Standards**: https://www.facebook.com/communitystandards/

### 🔷 **DeepSeek**
- **Terms of Service**: https://www.deepseek.com/terms
- **Privacy Policy**: https://www.deepseek.com/privacy
- **API Documentation**: https://platform.deepseek.com/api-docs
- **Blog**: https://www.deepseek.com/blog

---

## How to Use These Sources

### Option A: Run the Automated Script
```bash
cd /Users/soudi/Documents/GitHub/FAI-PROJ-BENCHMARKING-IN-AI
python scripts/fetch_ai_policies.py
```
This will:
- ✓ Fetch all policies from the URLs above
- ✓ Save them to `documents/{company_id}/ai_policies/`
- ✓ Create metadata with timestamps and sources
- ✓ Generate a summary report

### Option B: Manual Review
Click each link above and review the policy documents directly. This is recommended for:
- Policy analysis and scoring
- Understanding nuances and specific clauses
- Verifying AI policy commitment level

### Option C: Hybrid Approach
1. Run script to collect all sources
2. Manually analyze each saved document
3. Score policies on the 4 dimensions

---

## Policy Analysis Framework

We're evaluating on **4 Key Dimensions**:

### 1. **Privacy Protection (0-10)**
**What to look for:**
- ✓ Data minimization principles
- ✓ On-device processing commitment
- ✓ User control over personal data
- ✓ Encryption/security measures
- ✓ Third-party data sharing restrictions
- ✗ Weak or vague language about data use

**Example:**
- Apple's on-device ML = High score (8-9)
- Meta's ad-targeting system = Lower score (6-7)

### 2. **Transparency & Explainability (0-10)**
**What to look for:**
- ✓ Model cards and technical documentation
- ✓ Research papers on model behavior
- ✓ Decision explanation mechanisms
- ✓ Bias testing and audit results
- ✓ Clear communication of AI limitations
- ✗ Black-box systems with no explanation

**Example:**
- Anthropic's Constitutional AI research = High (8-9)
- Vague "AI-powered" = Low score (4-5)

### 3. **Liability & Safety (0-10)**
**What to look for:**
- ✓ Safety testing and red-teaming programs
- ✓ Clear liability disclaimers
- ✓ Incident response procedures
- ✓ Adversarial testing results
- ✓ Safety guidelines for developers
- ✗ No safety measures mentioned

**Example:**
- OpenAI's safety team + research = High (8)
- No safety commitment = Low (3-4)

### 4. **User Rights & Control (0-10)**
**What to look for:**
- ✓ Right to access user data
- ✓ Right to delete data
- ✓ Opt-out from AI training
- ✓ API rate limiting and control
- ✓ User-friendly privacy settings
- ✗ No user controls available

**Example:**
- Apple's granular privacy controls = High (8-9)
- Forced AI model usage = Low (3-4)

---

## Recommended Analysis Process

1. **Read each policy** (30 mins per company)
2. **Extract key quotes** supporting your score
3. **Rate on 0-10 scale** for each dimension
4. **Calculate average** (mean of 4 dimensions)
5. **Document evidence** in comments

---

## Current Status

### Data Already in System:
```json
{
  "apple": { "privacy_score": 8.2, "transparency_score": 7.9, ... },
  "openai": { "privacy_score": 7.8, "transparency_score": 7.5, ... },
  "google": { "privacy_score": 7.2, "transparency_score": 7.0, ... },
  "anthropic": { "privacy_score": 8.5, "transparency_score": 8.3, ... },
  "meta": { "privacy_score": 6.8, "transparency_score": 6.5, ... },
  "deepseek": { "privacy_score": 6.5, "transparency_score": 6.2, ... }
}
```

### Next Steps:
1. ✅ **Links identified** (this document)
2. ⏳ **Fetch policies** (run script or manual review)
3. ⏳ **Analyze content** (read policies, extract evidence)
4. ⏳ **Update scores** (based on real policy analysis)
5. ⏳ **Generate report** (CEPA benchmark report with sources)

---

## Notes for You

- **These are the OFFICIAL sources** - no speculation, just facts from company websites
- **Policies change frequently** - set reminders to update quarterly
- **Mix of formats**: Some are web pages, some are PDFs, some are research papers
- **Rate limiting**: If running the script, it adds 2-second delays between requests
- **Legal notice**: This data collection is for research purposes and respects robots.txt

---

## Quick Start

**To fetch all policies immediately:**
```bash
python scripts/fetch_ai_policies.py
```

**To manually analyze:**
1. Open `AI_POLICY_SOURCES.md` 
2. Click each link above
3. Read and take notes
4. Update scores in `data/companies.json`

Let me know which approach you prefer! 🚀
