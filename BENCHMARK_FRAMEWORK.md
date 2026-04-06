# 🎯 AI Policy Benchmark Framework

## Evaluation Dimensions (All Required)

### 1. **PRIVACY & DATA PROTECTION**
**Question:** How does the company handle user data?

**Evaluation Criteria:**
- Data minimization practices (do they collect only what's needed?)
- User consent requirements (do they ask for permission?)
- Data retention policies (how long do they keep data?)
- Opt-out capabilities (can users control data use?)
- Training data practices (do they use user data to train models without consent?)

**Evidence Requirements:**
- Direct quotes from official privacy policy
- Link to policy document
- Severity if issues found (high/medium/low)
- Confidence rating (how certain are we about this assessment?)

---

### 2. **TRANSPARENCY & DISCLOSURE**
**Question:** How openly does the company communicate about their AI systems?

**Evaluation Criteria:**
- Policy accessibility (is there an official policy document?)
- Technical transparency (do they explain how models work?)
- Limitation disclosure (do they admit what models can't do?)
- Research publication (do they publish safety/ethics research?)
- Government contract disclosure (do they report government requests?)

**Evidence Requirements:**
- Links to published research, reports, or disclosures
- Quotes showing transparency commitments
- Gaps in transparency (what they don't disclose)

---

### 3. **LIABILITY & SAFETY**
**Question:** How does the company handle responsibility for AI harms?

**Evaluation Criteria:**
- Clear terms of service with liability limits
- Content policy clarity (what's not allowed?)
- Safety guidelines for users
- Incident response procedures
- Indemnification clauses (who bears risk?)

**Evidence Requirements:**
- Terms of service quotes
- Safety policy documents
- Known incidents and how they were handled

---

### 4. **USER RIGHTS & CONTROL**
**Question:** What rights do users have over their data and interactions?

**Evaluation Criteria:**
- Data deletion rights (can users delete their data?)
- Data export (can users get their data out?)
- Account control (can they manage settings?)
- Appeal/recourse mechanisms (can they challenge decisions?)
- Bias/discrimination protections

**Evidence Requirements:**
- Policy quotes on user rights
- Links to account settings or data download tools
- Documentation of appeal processes

---

### 5. **GOVERNMENT COLLABORATION & ACCOUNTABILITY**
**Question:** How transparent is the company about government relationships?

**Evaluation Criteria:**
- Government contract disclosure (are contracts public?)
- Data sharing with authorities (what's their policy?)
- Transparency reports (do they publish government request data?)
- Regulatory compliance (do they follow EU/US laws?)
- Geopolitical alignment (any evidence of state influence?)

**Evidence Requirements:**
- Transparency reports (if published)
- Government contract documentation
- Public statements on government cooperation
- Regulatory filings

---

### 6. **VALUES & ETHICAL ACCOUNTABILITY**
**Question:** Does the company demonstrate commitment to ethical AI?

**Evaluation Criteria:**
- Ethical AI research (do they publish ethics research?)
- Labor practices (how do they treat employees?)
- Diversity & inclusion commitments
- Environmental impact
- Long-term accountability mechanisms

**Evidence Requirements:**
- Published ethics papers or commitments
- DEI reports
- Employee reviews or public statements
- Sustainability reports

---

## Scoring Rubric

### Scale: 1-10

- **8-10:** Strong public commitment with detailed policies and transparency
- **6-7:** Adequate policies, some transparency gaps
- **4-5:** Minimal commitment, significant gaps
- **1-3:** Concerning policies or refusal to disclose
- **0:** No public policy available

### Confidence Intervals

Every rating should include uncertainty range:
- **±0.5:** Very confident (strong evidence, recent, detailed)
- **±1.0:** Moderately confident (good evidence, some ambiguity)
- **±1.5:** Low confidence (limited info, rapid changes expected)
- **±2.0:** Very low confidence (minimal public info, unreliable)

---

## Evidence Format (Required for Each Rating)

```json
{
  "metric": "Privacy Score",
  "company": "OpenAI",
  "rating": 6.5,
  "confidence_interval": [5.5, 7.5],
  "evidence": [
    {
      "claim": "User API conversations are not used to train models by default",
      "source": "OpenAI API Terms of Service",
      "url": "https://openai.com/policies/api-terms-of-service",
      "quote": "Content and files uploaded to the API are deleted after 30 days unless you tell us to keep them longer...",
      "verified": true,
      "date_accessed": "2026-04-05"
    },
    {
      "claim": "BUT training models use internet-scraped data without explicit consent",
      "source": "OpenAI Privacy Policy",
      "url": "https://openai.com/privacy",
      "quote": "We collect information through various means, including when you provide it directly...",
      "concern": "Scraping raises consent issues for content creators",
      "verified": true,
      "severity": "medium",
      "date_accessed": "2026-04-05"
    }
  ],
  "reasoning": "OpenAI has good API privacy practices but concerning training data practices reduce score",
  "gaps": "No transparency on exact training data sources or percentages"
}
```

---

## What NOT To Do

❌ **Don't make assumptions** - If you don't have evidence, say "unknown"  
❌ **Don't exaggerate** - Use exact quotes, not paraphrasing  
❌ **Don't hide concerns** - List both positive and negative  
❌ **Don't avoid ambiguity** - Show wide confidence intervals when uncertain  
❌ **Don't forget to link** - Every claim needs a URL to source  

---

## Workflow

1. **Research** - Visit each company's official policy pages
2. **Extract** - Find specific quotes that relate to each dimension
3. **Rate** - Assign a score (1-10) with confidence interval
4. **Evidence** - Document the quote + URL + reasoning
5. **Review** - Have someone check your work
6. **Update** - Keep dates current and track when policies change

---

## Company Policy URLs to Check

| Company | Privacy | Terms | Safety | Research |
|---------|---------|-------|--------|----------|
| **OpenAI** | https://openai.com/privacy | https://openai.com/terms | https://openai.com/safety | https://openai.com/research |
| **Anthropic** | https://www.anthropic.com/privacy | https://www.anthropic.com/terms | https://www.anthropic.com/safety | https://www.anthropic.com/research |
| **Google** | https://policies.google.com/privacy | https://policies.google.com/terms | https://ai.google/principles | https://research.google/ |
| **Meta** | https://www.facebook.com/privacy | https://www.facebook.com/terms | https://www.meta.com/ai | https://research.facebook.com |
| **Perplexity** | https://www.perplexity.ai/privacy | https://www.perplexity.ai/terms | https://www.perplexity.ai/help | https://blog.perplexity.ai |
| **DeepSeek** | https://www.deepseek.com/privacy | https://www.deepseek.com/terms | https://www.deepseek.com/ | - |

---

## Next Steps

1. **For each company**: Visit the URLs above
2. **For each dimension**: Find evidence from policies
3. **Document everything**: Copy exact quotes with URLs
4. **Assign scores**: Based on clear criteria above
5. **Mark unknowns**: Use 0 or "unknown" if no public info
6. **Request review**: Have team verify accuracy
