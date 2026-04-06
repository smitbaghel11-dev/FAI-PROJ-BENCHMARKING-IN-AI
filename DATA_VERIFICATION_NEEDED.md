# ⚠️ DATA VERIFICATION REQUIRED

## Current Status
The benchmark data in `data/companies.json` contains **unverified ratings and explanations** that may not accurately reflect actual company policies.

## Issues Identified

### 1. **Made-up Policy Explanations**
- Descriptions claim specific policy details without access to verified sources
- Example: Claims about Perplexity's "optional account creation" and privacy-first model need verification
- Example: Claims about OpenAI's training data practices are based on general knowledge, not current verified policies

### 2. **Questionable Score Assignments**
Current scores show minimal differences between companies, which may not reflect real policy differences:
- **Perplexity (7.5 overall)** vs **OpenAI (7.875 overall)** - only 0.375 points difference
- If the user reports OpenAI has "far more gray areas" but scores higher, the ratings are inverted

### 3. **Unverified Government Relationship Claims**
- Claims about OpenAI's "DoD contracts" and "Microsoft partnerships" influencing scores
- No clear source documentation for these claims

## What Needs to Happen

### Option 1: Manual Research & Curation (Recommended)
1. Manually visit each company's actual policy pages:
   - Perplexity: https://www.perplexity.ai/privacy
   - OpenAI: https://openai.com/policies
   - Google: https://ai.google/principles/
   - Anthropic: https://www.anthropic.com/safety
   - Meta: https://www.meta.com/ai/
   - DeepSeek: https://www.deepseek.com/

2. Document specific, verifiable facts from each policy
3. Assign ratings based on this verified information
4. Keep direct quotes/links as evidence

### Option 2: Transparency Through Uncertainty
1. Lower confidence intervals dramatically (show that ratings are speculative)
2. Mark sections as "UNVERIFIED - User Input Needed"
3. Add user interface prompts for human review

### Option 3: Data Minimalism
1. Remove all explanations except direct policy quotes
2. Score only based on publicly verifiable factors
3. Show that most ratings cannot be definitively assigned without human review

## Recommended Action

**Add a clear disclaimer to the UI:**

```
🔍 IMPORTANT: This benchmark is based on our analysis of publicly available policies 
as of April 2026. 

⚠️ Ratings are subject to:
- Human interpretation of policy documents
- Availability of public information
- Rapid policy changes
- Incomplete policy transparency by companies

📋 VERIFICATION: Each rating should link to the specific policy document 
and direct quote that justifies it.
```

## For Employee Buy-In

**Instead of claiming certainty, emphasize honesty:**
- "We've reviewed X company's published policy and found Y"
- "We don't have access to Z, so we marked it as uncertain"
- "Here's the actual quote from their policy: [link]"
- "If you find information that changes this, please report it"

This builds trust through transparency, not through false certainty.
