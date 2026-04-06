# Official AI Policy Sources by Company

## 1. **Apple Inc.** (AAPL)

### Official AI Policy Documents:
- **Apple Machine Learning & AI Ethics**: https://www.apple.com/privacy/
  - Focus: Privacy protection, AI model transparency, user data protection
  - Document: Apple Privacy Policy and Machine Learning Privacy
  
- **Apple AI Privacy in On-Device Intelligence**: https://www.apple.com/privacy/features/
  - Focus: On-device ML privacy (no data transmission to servers)
  - Key docs: Private Cloud Compute, On-Device Processing

- **Apple Responsible AI**: https://www.apple.com/newsroom/
  - Search for: "Machine Learning" + "Privacy" + "AI Ethics"
  - Focus: AI responsibility, user control, transparency

- **Apple Patent Database on AI Safety**: https://patents.apple.com/
  - Search: "machine learning privacy" OR "AI safety"
  - Focus: AI safety mechanisms, privacy-preserving ML

---

## 2. **OpenAI**

### Official AI Policy Documents:
- **OpenAI Usage Policies**: https://openai.com/policies/usage-policies
  - Focus: Acceptable use of AI models, safety guidelines
  - Coverage: Misuse prevention, bias prevention, content policy

- **OpenAI Privacy Policy**: https://openai.com/privacy
  - Focus: User data handling, API data retention
  - Coverage: GDPR compliance, data minimization

- **OpenAI Safety & Security**: https://openai.com/safety
  - Focus: AI safety research, model safety, risk mitigation
  - Coverage: Deployment safety, red-teaming, safety measures

- **OpenAI Terms of Service**: https://openai.com/terms
  - Focus: Legal liability, warranty disclaimers
  - Coverage: Responsibility allocation

- **OpenAI Responsible Disclosure**: https://openai.com/security/
  - Focus: Security policies, vulnerability disclosure
  - Coverage: Bug bounty, security best practices

---

## 3. **Google (Alphabet Inc.)**

### Official AI Policy Documents:
- **Google AI Principles**: https://ai.google/principles/
  - Focus: Responsible AI development, ethical framework
  - Coverage: Fairness, accountability, transparency, privacy

- **Google Privacy Policy**: https://policies.google.com/privacy
  - Focus: Data collection from AI services, user privacy
  - Coverage: Targeted ads, ML training data, user control

- **Google Responsible AI Practices**: https://developers.google.com/machine-learning/responsible-ai
  - Focus: Developer guidelines for responsible AI
  - Coverage: Bias detection, fairness testing, interpretability

- **Google AI Explanations & Transparency**: https://research.google/pubs/?area=machine-intelligence
  - Focus: Explainable AI, transparency research
  - Coverage: Model interpretability, decision explanation

- **Google Trust & Safety**: https://blog.google/around-the-globe/google-asia/our-approach-to-trust-and-safety/
  - Focus: Content moderation, safety in AI systems
  - Coverage: Harmful content prevention, user safety

- **Bard/Gemini AI Safety**: https://support.google.com/bard/answer/13594961
  - Focus: LLM safety features, usage guidelines
  - Coverage: Model limitations, safety filters

---

## 4. **Anthropic**

### Official AI Policy Documents:
- **Anthropic Constitution AI**: https://www.anthropic.com/research/articles/constitutional-ai-harmlessness-from-ai-feedback
  - Focus: AI safety training methodology (RLHF with safety constitution)
  - Coverage: Reducing harmful outputs, AI alignment

- **Anthropic Privacy Policy**: https://www.anthropic.com/privacy
  - Focus: User data handling in Claude API and web interface
  - Coverage: Data retention, GDPR compliance

- **Anthropic Policy on Responsible Use**: https://www.anthropic.com/claude/responsible-use-policy
  - Focus: Acceptable use of Claude, prohibited uses
  - Coverage: Bias prevention, misuse prevention

- **Anthropic Safety & Policy Blog**: https://www.anthropic.com/research
  - Focus: AI safety research, model evaluation
  - Coverage: Red-teaming, adversarial testing, safety benchmarks

- **Anthropic Terms of Service**: https://www.anthropic.com/terms
  - Focus: Liability, AI model limitations
  - Coverage: Warranty disclaimers, responsibility allocation

- **Anthropic AI Safety**: https://www.anthropic.com/safety
  - Focus: Long-term AI safety, alignment research
  - Coverage: Technical safety approaches, safety evaluation

---

## 5. **Meta Platforms**

### Official AI Policy Documents:
- **Meta AI Ethics & Responsible Innovation**: https://www.meta.com/ai/
  - Focus: AI ethics framework, responsible development
  - Coverage: Fairness, transparency, accountability

- **Meta Privacy Policy**: https://www.meta.com/privacy/
  - Focus: How AI uses personal data from Meta services
  - Coverage: Ad targeting, ML model training, user control

- **Meta Responsible AI Team**: https://www.meta.com/research/ai-ethics/
  - Focus: AI ethics research, bias mitigation
  - Coverage: Algorithmic fairness, transparency, interpretability

- **Meta Community Standards & AI Moderation**: https://www.facebook.com/communitystandards/
  - Focus: AI-powered content moderation policies
  - Coverage: Harmful content removal, user safety

- **Meta Data Policy (AI Training)**: https://www.meta.com/policies/
  - Focus: Data collection for AI model training
  - Coverage: Opt-out options, data minimization

- **Meta Llama 2 Community License**: https://github.com/facebookresearch/llama
  - Focus: Open-source AI model usage restrictions
  - Coverage: Acceptable use, safety requirements

---

## 6. **DeepSeek**

### Official AI Policy Documents:
- **DeepSeek Terms of Service**: https://www.deepseek.com/terms
  - Focus: Model usage policies, acceptable use
  - Coverage: Prohibited uses, safety guidelines

- **DeepSeek Privacy Policy**: https://www.deepseek.com/privacy
  - Focus: User data handling, privacy practices
  - Coverage: Data retention, user rights

- **DeepSeek API Documentation**: https://platform.deepseek.com/api-docs
  - Focus: API usage restrictions, safety guidelines
  - Coverage: Rate limiting, content policy

- **DeepSeek Safety & Responsibility**: https://www.deepseek.com/safety
  - Focus: AI safety measures, responsible deployment
  - Coverage: Content filtering, harmful use prevention

- **DeepSeek Research Blog**: https://www.deepseek.com/blog
  - Focus: AI safety research, model evaluation
  - Coverage: Safety benchmarks, alignment research

---

## Key AI Policy Dimensions Being Evaluated:

### 1. **Privacy Protection Score** (0-10)
- Measures: Data minimization, on-device processing, user control over data
- **Sources**: Privacy policies, data handling practices, GDPR compliance

### 2. **Transparency & Explainability** (0-10)
- Measures: Model card publication, research disclosure, decision explainability
- **Sources**: Technical reports, research papers, policy transparency

### 3. **Liability & Safety** (0-10)
- Measures: Warranty disclaimers, safety testing, incident response procedures
- **Sources**: Terms of service, safety research, incident disclosure

### 4. **User Rights & Control** (0-10)
- Measures: Data deletion rights, opt-out options, API rate control
- **Sources**: Privacy policies, API documentation, user control features

---

## How to Fetch These Policies:

### Option 1: Automated Fetching (Python Script)
We can create a Python script using:
- `requests` library for HTTP requests
- `BeautifulSoup` for HTML parsing
- Retry logic for rate limiting
- Output to JSON with timestamps

### Option 2: Manual Collection
Download PDFs/HTML from each link above and store in `/documents/{company_id}/ai_policies/`

### Option 3: Hybrid Approach
- Automated for accessible web content
- Manual for PDFs and legally-binding documents
- Version control with timestamps

---

## Important Notes:

1. **Rate Limiting**: Add delays between requests (1-3 seconds)
2. **User-Agent**: Use proper User-Agent header to avoid 403 errors
3. **Legal Compliance**: Check Terms of Service for web scraping permissions
4. **Freshness**: Update policies monthly as they change frequently
5. **Attribution**: Always credit original sources in citations

---

## Next Steps:

1. **Decide on fetching method**: Automated, manual, or hybrid
2. **Update companies.json**: Replace dummy scores with analysis of real policies
3. **Create policy documents**: Store actual policy texts for reference
4. **Version control**: Track policy changes over time
5. **Benchmark update**: Re-run benchmarks with real policy analysis

