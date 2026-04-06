# 🎯 Evidence & Justification System

## What's New?

Every metric now has a **"📄 View Evidence"** button showing:
- The exact score with confidence range (±)
- Why we gave that score  
- What data we analyzed
- How certain we are

---

## Click Flow

```
User clicks "View Evidence" on Privacy Score
         ↓
Evidence card expands smoothly
         ↓
Shows side-by-side:
  • Company A: Score + reasoning + confidence
  • Company B: Score + reasoning + confidence
         ↓
User reads actual methodology
  (not just arbitrary numbers)
         ↓
User thinks: "I understand their reasoning.
  They're honest about uncertainty.
  This is fair."
```

---

## Example Evidence Card

```
╔════════════════════════════════════════════════════╗
║ 📋 Evidence & Justification                     ✕ ║
╟─────────────────────┬───────┬──────────────────╢
║ ANTHROPIC           │       │ META             ║
╟─────────────────────┼───────┼──────────────────╢
║                     │       │                  ║
║ Score: 8.3/10 ± 1.0 │       │ Score: 5.9 ±1.5║
║ (range: 7.3-9.3)    │       │ (range: 4.4-7.4)║
║                     │       │                  ║
║ ✅ WHY HIGH:        │       │ ⚠️ WHY MODERATE:║
║ • Explicit no-      │       │ • Good policies │
║   retraining        │       │ • BUT business  │
║   guarantees        │       │   model creates │
║ • No contractor     │       │   inherent      │
║   access            │       │   conflicts     │
║ • Published         │       │                 ║
║   research backing  │       │ 🎯 CONFIDENCE:  │
║                     │       │ MODERATE (±1.5) │
║ 🎯 CONFIDENCE:      │       │ Conflicting     │
║ HIGH (±1.0)         │       │ signals create  │
║ Well-documented     │       │ uncertainty     │
║ policies            │       │                 │
║                     │       │                 ║
╚═════════════════════╧═══════╧══════════════════╝
```

---

## What the ± Means

| Range | Meaning | Example |
|-------|---------|---------|
| ±0.8 | Very sure (published research) | Anthropic: 8.3 ± 0.8 |
| ±1.0 | Quite sure (documented policy) | OpenAI: 7.6 ± 1.0 |
| ±1.3 | Moderately sure (some tension) | Google: 6.8 ± 1.3 |
| ±1.5 | Less sure (young/conflicting) | Perplexity: 7.2 ± 1.5 |
| ±1.8 | Uncertain (geopolitical) | DeepSeek: 4.7 ± 1.8 |

**Narrow range = "We're confident"**
**Wide range = "We're honest about uncertainty"**

---

## Key Principles

### 1. Transparency Over False Precision
❌ DON'T: "Privacy: 7.5" (sounds certain)
✅ DO: "Privacy: 7.5 ± 1.3 [6.2-8.8]" (honest)

### 2. Show Your Work
❌ DON'T: "We gave 7.5 because it matters"
✅ DO: "7.5 because: good GDPR BUT scraping raises consent concerns. ±1.3 due to policy/practice tension"

### 3. Admit Uncertainty
❌ DON'T: "Anthropic 8.5 (this is right)"
✅ DO: "Anthropic 8.5 ± 0.9 (high confidence but acknowledges ±0.9 range)"

---

## What Each Card Shows

| Element | Example |
|---------|---------|
| **Score** | 8.3/10 |
| **Confidence** | ± 1.0 |
| **Range** | [7.3-9.3] |
| **Basis** | "Constitutional AI research, privacy policies" |
| **Why this score** | "Explicit guarantees + no contractor access" |
| **Confidence note** | "High confidence due to published research" |

---

## Confidence Levels Explained

### HIGH (±0.8-1.0)
- Published research papers
- Transparency reports
- Official policies
- Years of track record
- **Example:** Anthropic

### MODERATE (±1.2-1.4)
- Good documentation
- Some conflicting signals
- Mixed government relations
- Established company
- **Example:** OpenAI, Google

### LOWER (±1.5-1.8)
- Young company
- Limited documentation
- Geopolitical complexity
- Rapid changes expected
- **Example:** Perplexity, DeepSeek

---

## How This Works

### For Users
✅ See exactly why companies got their scores
✅ Understand confidence levels  
✅ Make informed comparisons

### For Company Employees
✅ See the reasoning (not arbitrary)
✅ Understand data basis
✅ Know where to improve

### For Credibility
✅ Shows we admit uncertainty
✅ Shows we did research
✅ Shows we're not arbitrary

---

## How to Use

1. **Visit:** http://localhost:8000
2. **Compare:** Two companies
3. **See:** Metric comparison table
4. **Click:** "📄 View Evidence" on any metric
5. **Read:** Full reasoning with confidence levels

---

## Files Changed

| File | What Changed |
|------|--------------|
| `app.py` | Backend extracts methodology data |
| `data/companies.json` | All methodologies + confidence intervals |
| `static/js/main.js` | Evidence card rendering |
| `static/css/style.css` | Professional card styling |

---

## Responsive Design

| Device | Layout |
|--------|--------|
| Desktop | Side-by-side companies |
| Tablet | Stacked with divider |
| Mobile | Stacked, no divider |

---

**Status:** ✅ Live at http://localhost:8000

**Achievement:** Every score is now transparent, honest, and defensible.
4. `.jpg` ← Final fallback

This ensures all logos display regardless of file format! 🎨

---

## Technical Details

**Modified Files:**
- `templates/index.html` (2 lines changed)
- `data/companies.json` (1 line changed)
- `static/js/main.js` (15 lines changed)
- `static/css/style.css` (12 lines changed)

**Total Changes:** 30 lines of code

**Testing:** ✅ All endpoints verified and working

---

## What's Next?

Platform is ready for:
- ✅ AI policy comparisons
- ✅ Visual logo display
- ✅ Multi-format image support
- ✅ Full 6-company benchmark suite

Enjoy using CEPA! 🚀
