# 📖 User Guide: How to Use the Evidence System

## Getting Started

1. **Open the app:** http://localhost:8000
2. **See the default comparison:** Perplexity vs OpenAI
3. **Explore the features:** Click "View Evidence" on any metric

---

## Understanding the Interface

### Main Comparison Table

```
┌─────────────────────────────────────────────────────────────────┐
│ METRIC                    PERPLEXITY      OPENAI    DIFFERENCE  │
├─────────────────────────────────────────────────────────────────┤
│ Privacy Protection        7.2/10          7.6/10    -0.4 (-5.3%)│
│ Score                     [📄 View Evidence]                     │
│                                                                   │
│ Transparency &            7.8/10          8.2/10    -0.4 (-4.9%)│
│ Explainability            [📄 View Evidence]                     │
│                                                                   │
│ Liability & Safety        7.4/10          7.9/10    -0.5 (-6.3%)│
│                           [📄 View Evidence]                     │
│                                                                   │
│ User Rights & Control     7.6/10          7.8/10    -0.2 (-2.6%)│
│                           [📄 View Evidence]                     │
│                                                                   │
│ ... and so on ...                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Reading an Evidence Card

### Step 1: Click "View Evidence"
Button appears under each metric name in the table.

### Step 2: Card Expands
Animation reveals full methodology and reasoning.

### Step 3: Read Both Companies

**Left side: Company A**
```
╔─────────────────────┐
║  PERPLEXITY AI      ║
║                     ║
║ 7.2/10 ± 1.5        ║
║ [Confidence badge]  ║
║                     ║
║ 📋 REASONING:       ║
║                     ║
║ Data minimization   ║
║ practices and       ║
║ privacy-first       ║
║ design. Lower       ║
║ confidence (±1.5)   ║
║ due to limited      ║
║ historical track    ║
║ record and no       ║
║ government          ║
║ transparency        ║
║ reports.            ║
└─────────────────────┘
```

**Right side: Company B**
```
╔─────────────────────┐
║  OPENAI             ║
║                     ║
║ 7.6/10 ± 1.3        ║
║ [Confidence badge]  ║
║                     ║
║ 📋 REASONING:       ║
║                     ║
║ Good GDPR           ║
║ compliance and      ║
║ data retention      ║
║ policies, but       ║
║ training data       ║
║ sourced from        ║
║ internet scraping   ║
║ raises consent      ║
║ concerns. Moderate  ║
║ confidence (±1.3)   ║
║ due to tension      ║
║ between stated      ║
║ policies and        ║
║ practice.           ║
└─────────────────────┘
```

### Step 4: Interpret Confidence

**±1.5 (Perplexity)**
- Wider range
- "We're less confident"
- Why? Young company, limited track record
- Interpretation: "Could be higher or lower as they mature"

**±1.3 (OpenAI)**
- Narrower than Perplexity
- "We're more confident"
- Why? More data available, but some tension
- Interpretation: "This assessment is solid but acknowledges complexity"

### Step 5: Close
Click **X** button or click outside to close the card.

---

## Comparing Confidence Levels

### Same Metric, Different Confidence

| Company | Score | Confidence | Why | Trust Level |
|---------|-------|-----------|-----|------------|
| Anthropic | 8.3 | ±0.9 | Published research | ✅ Very High |
| OpenAI | 7.6 | ±1.3 | Good docs, some tension | ✅ High |
| Google | 6.8 | ±1.3 | Complex ad model | 🤔 Moderate |
| Perplexity | 7.2 | ±1.5 | Young company | 🤔 Moderate |
| DeepSeek | 6.2 | ±2.2 | Opacity barriers | ⚠️ Low |

**Narrower ± = "We're more confident in this assessment"**
**Wider ± = "We're admitting significant uncertainty"**

---

## Real-World Scenarios

### Scenario 1: Employee Challenge
**Employee from Perplexity:**
> "I think our privacy score should be 8.0, not 7.2. You're being too harsh about our age."

**You respond:**
> "Look at the evidence card. We gave you ±1.5 range (5.7-8.8) exactly because of your startup age. If you show us new privacy commitments, we can adjust. The ±1.5 acknowledges that your score could reasonably be 8.0 as you mature."

### Scenario 2: Investor Question
**Investor:**
> "Why is Meta's privacy 5.9 but Anthropic's is 8.3? Seems like you're biased."

**You show:**
- Anthropic confidence: ±0.9 (published research)
- Meta confidence: ±1.5 (conflicting signals)
- Side-by-side reasoning shows different issues

> "Not bias—different data. Anthropic has published research backing their claims. Meta has internal policies but ad-driven business model creates inherent tensions. The confidence intervals show which is more certain."

### Scenario 3: Media Question
**Journalist:**
> "How do you prove these ratings aren't arbitrary?"

**You say:**
> "Click 'View Evidence' on any metric. You'll see:
> - Exact data basis (what we analyzed)
> - Per-metric reasoning (why this score)
> - Confidence ranges (how certain we are)
> - Both companies' methodologies (side-by-side comparison)
>
> The ±ranges show we're not claiming false precision. This is honest assessment with admitted uncertainty."

---

## Understanding Confidence Ranges

### Example: Privacy Score

**Anthropic: 8.3/10 ± 0.9**
- Score: 8.3
- Confidence interval: 0.9
- Range: [7.4, 9.2]
- Interpretation: Most likely 8.3, could reasonably be 7.4-9.2

**What ±0.9 means:**
- We're quite sure (narrow range)
- Based on published research
- High confidence this is accurate

**What if someone disagrees?**
- They might think Anthropic deserves 7.8
- That's within the confidence range!
- Reasonable disagreement, not bad methodology

---

**Meta: 5.9/10 ± 1.5**
- Score: 5.9
- Confidence interval: 1.5
- Range: [4.4, 7.4]
- Interpretation: Most likely 5.9, could reasonably be 4.4-7.4

**What ±1.5 means:**
- We're less sure (wider range)
- Ad model creates conflicting signals
- Reasonable people might score 5.0-7.0

**What if someone disagrees?**
- They might think Meta deserves 6.5
- That's within the confidence range!
- We're admitting this range of disagreement exists

---

## Tips for Understanding

### 1. Wider ≠ Bad
A wide ±1.5 range doesn't mean the company is bad. It means:
- We admit uncertainty
- Multiple reasonable interpretations exist
- We're being intellectually honest

### 2. Narrow ≠ Certain
A narrow ±0.8 range means:
- We have strong evidence
- Most auditors would reach similar conclusion
- Still acknowledges small uncertainty

### 3. Read Both Sides
Always compare the methodologies:
- What did they look at?
- Is it the same data?
- Why different confidence?

### 4. Look for Specifics
Good methodology says:
- ✅ "Published 5 research papers"
- ✅ "Privacy policy explicitly states no scraping"
- ❌ "Privacy is important"
- ❌ "We looked at stuff"

---

## Keyboard Navigation

| Action | How |
|--------|-----|
| Compare companies | Select from dropdowns, click "Run Comparison" |
| View evidence | Click "[📄 View Evidence]" button |
| Close evidence | Click [✕] or click elsewhere |
| Scroll to card | Opens with auto-scroll to view |

---

## Mobile Usage

### On Your Phone

1. **Rotate to landscape** for better table view
2. **Tap "View Evidence"** to expand card
3. **Scroll down** to read both companies
4. **Tap ✕** to close and return to table
5. **Select new companies** at top with dropdown

### Mobile Design
- Full-width cards on small screens
- Stacked company sections
- Easy-to-tap buttons
- Readable font sizes

---

## What If...?

### "The evidence card won't open?"
1. Try refreshing the page (Cmd+R or Ctrl+R)
2. Make sure JavaScript is enabled
3. Check browser console for errors

### "The numbers seem wrong?"
1. Check the confidence range - maybe you're within it
2. Read the methodology - maybe you misunderstood the data basis
3. Contact us with specific concerns

### "I disagree with the reasoning?"
1. That's okay! Check if your disagreement fits in the ±range
2. If you think the methodology is wrong, propose corrections
3. Show us data they might have missed

### "Can I download this?"
Yes! Look for download buttons at bottom:
- CSV export
- JSON export
- SQL schema

---

## Summary

**This system lets you:**
✅ See exactly why companies scored as they did
✅ Understand confidence levels
✅ Compare methodologies side-by-side
✅ Verify claims are backed by evidence
✅ Disagree intelligently (within ranges)
✅ Trust the assessment is honest about uncertainty

**That's the whole point:** 
Transparent, honest assessment with admitted uncertainty.

Not arbitrary numbers. Not false precision.
**Real methodology you can verify.**

---

**Happy exploring!** 🚀
