# 🎨 New Benchmark UI/UX Design

## How It Will Look When You Click "View Evidence"

```
╔════════════════════════════════════════════════════════════════╗
║          🔗 OFFICIAL POLICY EVIDENCE                          ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  OPENAI - Privacy & Data Protection                           ║
║  ────────────────────────────────────                         ║
║  Rating: 6.5/10  (±1.0)                                       ║
║                                                                ║
║  📌 Official Quote:                                           ║
║  ┌──────────────────────────────────────────────────────────┐ ║
║  │ "We don't use data from your API requests to train    │ ║
║  │ or improve our models. However, we may use data for  │ ║
║  │ other purposes in accordance with the API Terms."    │ ║
║  └──────────────────────────────────────────────────────────┘ ║
║                                                                ║
║  ⚠️  Concern:                                                 ║
║  ┌──────────────────────────────────────────────────────────┐ ║
║  │ Training models on internet-scraped data without    │ ║
║  │ explicit consent from content creators.              │ ║
║  │ Severity: MEDIUM                                      │ ║
║  └──────────────────────────────────────────────────────────┘ ║
║                                                                ║
║  📄 Official Documents:                                       ║
║  • Privacy Policy https://openai.com/privacy ↗              ║
║  • API Terms https://openai.com/policies/api-terms ↗        ║
║                                                                ║
║  💭 Reasoning:                                               ║
║  OpenAI has clear API data minimization commitments but    ║
║  lacks transparency on training data sources. The gap      ║
║  between API privacy and training data practices lowered    ║
║  the score.                                                  ║
║                                                                ║
║  ❓ Unknowns:                                                ║
║  • Exact percentage of scraped vs. licensed training data   ║
║  • Specific opt-out mechanisms for training data use        ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║  [Close Evidence] [Flag as Inaccurate] [Report Update]       ║
╚════════════════════════════════════════════════════════════════╝
```

---

## Comparison View

```
PRIVACY SCORE COMPARISON
════════════════════════════════════════════════════════════════

OpenAI          6.5/10 ±1.0  [████████░░░░░░]
  └─ Quote: "We don't use data from your API requests..."
     Policy: https://openai.com/privacy ↗

Anthropic       8.2/10 ±0.8  [██████████████░]
  └─ Quote: "We never train Claude on your conversations..."
     Policy: https://www.anthropic.com/privacy ↗

────────────────────────────────────────────────────────────────
Difference: 1.7 points in Anthropic's favor
  
Why? Anthropic has explicit training data opt-out guarantees.
     OpenAI uses internet-scraped data without explicit consent.

View both full policies ↗
```

---

## Data Structure Behind the UI

```json
{
  "comparison": {
    "privacy": {
      "metrics": [
        {
          "id": "openai-privacy",
          "company": "OpenAI",
          "dimension": "Privacy & Data Protection",
          "score": 6.5,
          "confidence_interval": [5.5, 7.5],
          "evidence": [
            {
              "type": "positive",
              "claim": "API conversations not used for training by default",
              "quote": "We don't use data from your API requests to train or improve our models...",
              "source": "OpenAI API Terms of Service",
              "url": "https://openai.com/policies/api-terms-of-service",
              "section": "Data and Training",
              "verified_date": "2026-04-05"
            },
            {
              "type": "concern",
              "claim": "Training data sourced from internet scraping without explicit consent",
              "quote": "We collect information from publicly available sources...",
              "source": "OpenAI Privacy Policy",
              "url": "https://openai.com/privacy",
              "severity": "medium",
              "verified_date": "2026-04-05"
            }
          ],
          "reasoning": "OpenAI has good API privacy practices but training data practices raise concerns about consent and transparency.",
          "gaps": [
            "No disclosure of exact training data sources",
            "Limited opt-out options for training data use",
            "No public transparency report on government requests"
          ]
        }
      ]
    }
  }
}
```

---

## UI Features

### 1. **Evidence Panel** (On rating click)
- Shows official quote in highlighted box
- Links to source documents
- Lists concerns separately
- Reasoning clearly explained
- Known gaps/unknowns listed

### 2. **Confidence Indicator**
```
Score: 6.5 ±1.0 means:
- We're fairly confident (±1.0 is moderate)
- Real score likely between 5.5 and 7.5
- Click the ⓘ icon to see why we're uncertain
```

### 3. **Comparison Highlights**
```
❕ Key Differences:
┌─────────────────────────────────────────┐
│ OpenAI: No training data guarantees     │
│ Anthropic: Explicit no-training pledge  │
│ Gap: 1.7 points justifiable              │
└─────────────────────────────────────────┘
```

### 4. **Verification Status**
Each policy shows:
- ✅ Last verified: April 5, 2026
- ⚠️ Policy may have changed
- [Report Update] button for users

### 5. **Transparency Row**
```
DATA INTEGRITY NOTICE
⚠️  This benchmark is built from verified official policies.
Each rating is linked to source documents. If you find
inaccuracies, click [Report] and we'll investigate.
```

---

## How Users Interact

### Reading a Rating
1. User sees: "OpenAI Privacy Score: 6.5/10 ±1.0"
2. User clicks: "View Evidence"
3. Panel opens showing:
   - Official quote from privacy policy
   - Link to full policy document
   - Why this score was assigned
   - What concerns remain

### Challenging a Rating
1. User reads the quote
2. User clicks: "Flag as Inaccurate"
3. They can:
   - Provide newer policy link
   - Share quote from updated policy
   - Explain why reasoning is wrong
4. System flags for review

### Finding Differences
1. User compares two companies
2. Click "Why the difference?"
3. See side-by-side quotes
4. Understand the actual policy gap

---

## Success Metrics

✅ **Employee trust:** "I can verify this myself"  
✅ **Internal defensibility:** "Here's the source, judge for yourself"  
✅ **Accuracy:** Built on real policies, updated when they change  
✅ **Transparency:** Unknowns are clearly marked  
✅ **Participation:** Users can report inaccuracies  

---

## What Happens Next

1. **You provide research** (scores + quotes + URLs)
2. **I update companies_clean.json** with your verified data
3. **Backend processes the data** to support new UI
4. **Frontend renders:** Score + Quote + Link + Reasoning
5. **Deploy** with data integrity notice

The system is designed. Now we need the honest data to fill it.

