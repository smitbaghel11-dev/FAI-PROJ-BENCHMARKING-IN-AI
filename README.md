# BenchmarkIQ — Company Benchmark Comparison System
### Apple Inc. vs Samsung Electronics · Technology Industry · FY 2023

---

## Overview

BenchmarkIQ is a full-stack Python web application that lets you compare two companies
across **13 benchmark metrics in 5 categories** using real, verified FY 2023 data.

**System flow:**
```
User Input → Flask API → Comparison Engine → Score Normalisation → Insights Engine → Dashboard
```

---

## Project Structure

```
benchmarkiq/
├── app.py                      ← Flask backend (API + comparison engine + insights)
├── requirements.txt
├── templates/
│   └── index.html              ← Single-page dashboard
├── static/
│   ├── css/style.css           ← Stylesheet (dark editorial theme)
│   └── js/main.js              ← Chart.js rendering + API calls
└── data/
    ├── companies.json          ← Primary data store (13 metrics × 2 companies)
    ├── benchmark_dataset.csv   ← Downloadable flat dataset
    └── schema.sql              ← MySQL schema + seed data
```

---

## Quick Start (3 commands)

```bash
# 1. Install dependency
pip install flask

# 2. Run the server
python app.py

# 3. Open in browser
#    http://localhost:5000
```

The dashboard auto-loads an Apple vs Samsung comparison on startup.

---

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/companies` | List available companies |
| GET | `/api/company/<id>` | Full data for one company |
| GET | `/api/categories` | Available benchmark categories |
| GET | `/api/compare` | **Main comparison endpoint** |
| GET | `/api/download/csv` | Download CSV dataset |
| GET | `/api/download/json` | Download JSON dataset |
| GET | `/api/download/sql` | Download SQL schema |

### Compare endpoint parameters

```
GET /api/compare?company_a=apple&company_b=samsung&category=all
```

| Parameter | Values | Default |
|-----------|--------|---------|
| `company_a` | `apple` \| `samsung` | `apple` |
| `company_b` | `apple` \| `samsung` | `samsung` |
| `category` | `all` \| `financial` \| `performance` \| `internal` \| `customer` \| `innovation` | `all` |

---

## Benchmark Metrics (13 total)

### 💰 Financial (3)
| Metric | Unit | Source |
|--------|------|--------|
| Revenue | USD Billions | Apple 10-K / Samsung Annual Report 2023 |
| Profit Margin | % | Apple 10-K / Samsung Annual Report 2023 |
| Smartphone Market Share | % | IDC Q4 2023 |

### 📈 Performance (3)
| Metric | Unit | Source |
|--------|------|--------|
| Revenue Growth YoY | % | Apple 10-K / Samsung Annual Report 2023 |
| Revenue per Employee | USD Millions | Apple 10-K / Samsung Annual Report 2023 |
| Operating Efficiency (margin) | % | Apple 10-K / Samsung Annual Report 2023 |

### 👥 Internal / HR (2)
| Metric | Unit | Source |
|--------|------|--------|
| Employee Satisfaction (Glassdoor) | / 5 | Glassdoor 2023 |
| Employee Growth YoY | % | Apple 10-K / Samsung Annual Report 2023 |

### ⭐ Customer (2)
| Metric | Unit | Source |
|--------|------|--------|
| Customer Satisfaction (ACSI) | / 10 | ACSI 2023 |
| Net Promoter Score | pts | Bain & Company 2023 |

### 🔬 Innovation (3)
| Metric | Unit | Source |
|--------|------|--------|
| New Products Launched | units | Company press releases |
| R&D Spending | USD Billions | Apple 10-K / Samsung Annual Report 2023 |
| Tech Adoption Index | / 10 | Composite analyst estimate |

---

## Scoring Logic

1. **Per-metric winner**: `if val_A > val_B → A wins` (for higher-is-better metrics)
2. **Normalisation**: each value mapped to 0–10 using min-max scaling
   ```
   score = (value − min) / (max − min) × 10
   ```
3. **Overall score**: average of all metric scores × 10 → range 0–100
4. **Scores always sum to 100** across both companies

---

## Insight Engine

The AI insight system is deterministic-rule-based and produces:
- **Strengths** per company (based on which metrics each wins and by how much)
- **Weaknesses** explaining the root cause
- **Strategic recommendations** for both companies

---

## Database Setup (optional MySQL)

```bash
# Requires MySQL running locally
mysql -u root -p < data/schema.sql

# Then update app.py to use mysql-connector-python instead of JSON
pip install mysql-connector-python
```

The JSON file (`data/companies.json`) is used by default — no database required.

---

## Data Sources

| Source | Used for |
|--------|----------|
| Apple Inc. Form 10-K (Oct 2023) | Revenue, Profit, R&D, Employees, Growth |
| Samsung Electronics Annual Report 2023 | Revenue, Profit, R&D, Employees, Growth |
| IDC Worldwide Mobile Phone Tracker Q4 2023 | Smartphone market share |
| Glassdoor Company Reviews 2023 | Employee satisfaction (1–5) |
| American Customer Satisfaction Index 2023 | CSAT score |
| Bain & Company NPS Benchmarks 2023 | Net Promoter Score |
| USPTO Patent Activity 2023 | Patents filed |
| Interbrand Best Global Brands 2023 | Brand value |

> Samsung financial figures converted from KRW to USD at average 2023 rate ≈ 1,305 KRW/USD.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3 + Flask |
| Frontend | HTML5 + CSS3 + Vanilla JS |
| Charts | Chart.js 4 (Radar + Horizontal Bar) |
| Data store | JSON (+ MySQL schema provided) |
| Fonts | Syne + DM Sans (Google Fonts) |
