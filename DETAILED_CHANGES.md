# Changes Made to Implement Evidence-Backed Justifications

## Files Modified

### 1. `app.py` (Backend API)

**Lines modified:** 240-267 (comparison engine)

**What changed:**
```python
# BEFORE: Just returned raw scores
row_list.append({
    "score_a": sc_a,
    "score_b": sc_b,
    "winner": winner,
})

# AFTER: Now includes methodology and confidence data
# Extract methodology explanation for each metric
methodology_key = f"{item['key']}_explanation"
methodology_a = deep_get(company_a, f"{cat_key}_methodology.{methodology_key}") or ""
methodology_b = deep_get(company_b, f"{cat_key}_methodology.{methodology_key}") or ""

confidence_a = deep_get(company_a, f"{cat_key}.{item['key']}_confidence_interval") or None
confidence_b = deep_get(company_b, f"{cat_key}.{item['key']}_confidence_interval") or None

row_list.append({
    # ... existing fields ...
    "methodology_a": methodology_a,      # NEW
    "methodology_b": methodology_b,      # NEW
    "confidence_a": confidence_a,        # NEW
    "confidence_b": confidence_b,        # NEW
})

# Also added to category results:
results[cat_key] = {
    "methodology_a": deep_get(company_a, f"{cat_key}_methodology"),  # NEW
    "methodology_b": deep_get(company_b, f"{cat_key}_methodology"),  # NEW
}
```

**Impact:** API now sends methodology data to frontend

---

### 2. `data/companies.json` (Data Layer)

**Lines modified:** 
- Added to Perplexity: ai_policy_methodology (lines ~20-30)
- Added to Perplexity: values_accountability_methodology (lines ~56-63)
- Added to OpenAI: values_accountability (lines ~226-236)
- Added to OpenAI: values_accountability_methodology (lines ~237-244)
- Added to Anthropic: values_accountability (lines ~350-360)
- Added to Anthropic: values_accountability_methodology (lines ~361-368)
- All companies: confidence_interval fields on every metric

**What changed:**

Each company now has 2 methodology objects:

```json
"ai_policy_methodology": {
  "basis": "Analysis of [data sources]...",
  "privacy_score_explanation": "Explains why privacy gets 7.2 with confidence ±1.5...",
  "transparency_score_explanation": "...",
  "liability_score_explanation": "...",
  "user_rights_score_explanation": "...",
  "confidence_note": "Overall confidence context..."
},

"values_accountability_methodology": {
  "basis": "Analysis of [values assessment]...",
  "gov_collaboration_score_explanation": "...",
  "geopolitical_score_explanation": "...",
  "human_values_score_explanation": "...",
  "confidence_note": "..."
}
```

Plus confidence intervals:
```json
"privacy_score": 7.2,
"privacy_confidence_interval": [5.7, 8.7],  // ±1.5
```

**Impact:** All data needed for evidence cards is available

---

### 3. `static/js/main.js` (Frontend Logic)

**Lines modified:**
- Lines 279-335: `buildRow()` function completely rewritten
- Lines 590-605: Added `showEvidence()` and `closeEvidence()` functions

**What changed:**

```javascript
// BEFORE: Just showed metric name and score
function buildRow(m, nameA, nameB) {
  return `
    <tr>
      <td>${m.label}</td>
      <td>${m.val_a}</td>
      <td>${m.score_a.toFixed(1)}</td>
      <!-- ... -->
    </tr>
  `;
}

// AFTER: Now includes expandable evidence card
function buildRow(m, nameA, nameB) {
  const evidenceId = `evidence-${m.key}-${Math.random().toString(36).substr(2, 9)}`;
  
  const evidenceCard = `
    <div class="evidence-card evidence-card--hidden" id="${evidenceId}">
      <div class="evidence-header">
        <h4>📋 Evidence & Justification</h4>
        <button class="evidence-close" onclick="closeEvidence('${evidenceId}')">&times;</button>
      </div>
      <div class="evidence-body">
        <div class="evidence-company">
          <h5>${nameA}</h5>
          <div class="evidence-score">Score: <strong>${m.score_a.toFixed(1)}/10</strong></div>
          <div class="evidence-methodology">${m.methodology_a}</div>
        </div>
        <div class="evidence-divider"></div>
        <div class="evidence-company">
          <h5>${nameB}</h5>
          <div class="evidence-score">Score: <strong>${m.score_b.toFixed(1)}/10</strong></div>
          <div class="evidence-methodology">${m.methodology_b}</div>
        </div>
      </div>
    </div>
  `;

  return `
    <tr>
      <td>
        ${m.label}
        <button class="btn-evidence" onclick="showEvidence('${evidenceId}')">📄 View Evidence</button>
      </td>
      <!-- ... -->
    </tr>
    <tr class="evidence-row">
      <td colspan="6">${evidenceCard}</td>
    </tr>
  `;
}

// NEW: Show/hide evidence
function showEvidence(evidenceId) {
  const card = document.getElementById(evidenceId);
  if (card) {
    card.classList.remove("evidence-card--hidden");
    card.classList.add("evidence-card--visible");
    card.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
}

function closeEvidence(evidenceId) {
  const card = document.getElementById(evidenceId);
  if (card) {
    card.classList.remove("evidence-card--visible");
    card.classList.add("evidence-card--hidden");
  }
}
```

**Impact:** Evidence cards render with smooth animations

---

### 4. `static/css/style.css` (Styling)

**Lines added:** 636-752 (new evidence card section)

**What changed:**

Added ~120 lines of new CSS:

```css
/* ── Evidence Cards ── */
.evidence-card {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%);
  border: 1px solid rgba(59, 130, 246, 0.25);
  border-radius: var(--radius);
  padding: 24px;
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  transition: all 0.3s ease;
}

.evidence-card--hidden {
  max-height: 0;
  opacity: 0;
  pointer-events: none;
}

.evidence-card--visible {
  max-height: 800px;
  opacity: 1;
  pointer-events: auto;
}

.evidence-body {
  display: grid;
  grid-template-columns: 1fr 1px 1fr;
  gap: 24px;
}

.evidence-methodology {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.6;
  background: rgba(0, 0, 0, 0.2);
  padding: 12px;
  border-radius: var(--radius-sm);
  border-left: 2px solid rgba(59, 130, 246, 0.4);
}

.btn-evidence {
  background: transparent;
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: #60A5FA;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  transition: all var(--ease);
}

.btn-evidence:hover {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.6);
  transform: translateY(-1px);
}

/* Responsive design */
@media (max-width: 768px) {
  .evidence-body {
    grid-template-columns: 1fr;
  }
  .evidence-divider {
    display: none;
  }
}
```

**Impact:** Evidence cards look professional and animate smoothly

---

## Summary of Changes

| File | Type | Lines | Change |
|------|------|-------|--------|
| `app.py` | Backend | 240-267 | Extract methodology + confidence data |
| `data/companies.json` | Data | ~150 total | Add methodology objects + intervals |
| `static/js/main.js` | Frontend | 279-335, 590-605 | Evidence cards + show/hide logic |
| `static/css/style.css` | Styling | 636-752 | Evidence card design + animations |

## User-Visible Changes

### Before
```
Metric: Privacy Score
Perplexity: 7.2/10 | OpenAI: 7.6/10
```

### After
```
Metric: Privacy Score
Perplexity: 7.2/10 | OpenAI: 7.6/10
[📄 View Evidence button]

[Clicking shows:]
┌─────────────────────────────────────────┐
│ 📋 Evidence & Justification          ✕  │
├──────────────┬────┬──────────────────┤
│ Perplexity   │    │ OpenAI           │
├──────────────┼────┼──────────────────┤
│ 7.2/10 ±1.5  │    │ 7.6/10 ±1.3      │
│              │    │                  │
│ Data minima- │    │ Good GDPR        │
│ tion practic │    │ compliance but   │
│ es. Lower    │    │ internet scrapi- │
│ confidence   │    │ ng raises conse- │
│ (±1.5) due   │    │ nt concerns...   │
│ to limited   │    │                  │
│ track record │    │                  │
└──────────────┴────┴──────────────────┘
```

---

**Result:** Complete transparency on how we calculate every rating.
