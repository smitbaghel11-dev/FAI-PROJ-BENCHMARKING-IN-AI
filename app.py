"""
BenchmarkIQ — Flask Backend
============================
Full benchmark comparison engine for Apple Inc. vs Samsung Electronics.

Data Sources (FY 2023):
  • Apple Inc. Form 10-K (Oct 2023)
  • Samsung Electronics Annual Report 2023
  • IDC Worldwide Mobile Phone Tracker Q4 2023
  • Glassdoor Company Reviews 2023
  • American Customer Satisfaction Index (ACSI) 2023
  • Net Promoter Score Benchmarks – Bain & Company 2023
  • USPTO Patent Activity 2023
  • Interbrand Best Global Brands 2023

Run:
  python app.py
  → http://localhost:5000
"""

import json
import os
import csv
import io
from flask import (
    Flask, jsonify, request,
    send_from_directory, render_template,
    send_file, make_response
)

# ─────────────────────────────────────────────
#  App Setup
# ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


@app.after_request
def cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


# ─────────────────────────────────────────────
#  Load Data from JSON (acts as our DB layer)
# ─────────────────────────────────────────────
DATA_FILE = os.path.join(BASE_DIR, "data", "companies.json")

with open(DATA_FILE, "r", encoding="utf-8") as _f:
    _raw = json.load(_f)

COMPANIES  = {c["id"]: c for c in _raw["companies"]}
META       = _raw["metadata"]


# ─────────────────────────────────────────────
#  Metric Catalogue
#  Each entry defines: path into company dict,
#  display info, and scoring direction.
# ─────────────────────────────────────────────
METRIC_CATALOGUE = {
    "financial": {
        "label": "Financial Metrics",
        "icon":  "💰",
        "items": [
            {
                "key":              "revenue",
                "label":            "Revenue",
                "path":             "financial.revenue",
                "unit":             "B USD",
                "higher_is_better": True,
                "description":      "Total annual revenue (USD Billions)",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
            {
                "key":              "profit_margin",
                "label":            "Profit Margin",
                "path":             "financial.profit_margin",
                "unit":             "%",
                "higher_is_better": True,
                "description":      "Net income as % of revenue",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
            {
                "key":              "market_share",
                "label":            "Smartphone Market Share",
                "path":             "financial.market_share_smartphones",
                "unit":             "%",
                "higher_is_better": True,
                "description":      "Global smartphone shipment share Q4 2023",
                "source":           "IDC Worldwide Mobile Phone Tracker Q4 2023"
            },
        ]
    },
    "performance": {
        "label": "Performance Metrics",
        "icon":  "📈",
        "items": [
            {
                "key":              "revenue_growth",
                "label":            "Revenue Growth (YoY)",
                "path":             "performance.revenue_growth_yoy",
                "unit":             "%",
                "higher_is_better": True,
                "description":      "Year-over-year revenue change",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
            {
                "key":              "revenue_per_employee",
                "label":            "Revenue per Employee",
                "path":             "performance.revenue_per_employee",
                "unit":             "M USD",
                "higher_is_better": True,
                "description":      "Productivity proxy: revenue ÷ headcount",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
            {
                "key":              "operating_margin",
                "label":            "Operating Efficiency",
                "path":             "financial.operating_margin",
                "unit":             "%",
                "higher_is_better": True,
                "description":      "Operating income as % of revenue",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
        ]
    },
    "internal": {
        "label": "Internal / HR Metrics",
        "icon":  "👥",
        "items": [
            {
                "key":              "glassdoor_rating",
                "label":            "Employee Satisfaction",
                "path":             "internal.glassdoor_rating",
                "unit":             "/ 5",
                "higher_is_better": True,
                "description":      "Average Glassdoor rating (2023 average)",
                "source":           "Glassdoor Company Reviews 2023"
            },
            {
                "key":              "employee_growth",
                "label":            "Employee Growth (YoY)",
                "path":             "internal.employee_growth_yoy",
                "unit":             "%",
                "higher_is_better": True,
                "description":      "Year-over-year headcount change",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
        ]
    },
    "customer": {
        "label": "Customer Metrics",
        "icon":  "⭐",
        "items": [
            {
                "key":              "csat_score",
                "label":            "Customer Satisfaction",
                "path":             "customer.csat_score",
                "unit":             "/ 10",
                "higher_is_better": True,
                "description":      "ACSI score normalised to 10-point scale (2023)",
                "source":           "American Customer Satisfaction Index 2023"
            },
            {
                "key":              "nps_score",
                "label":            "Net Promoter Score",
                "path":             "customer.nps_score",
                "unit":             "pts",
                "higher_is_better": True,
                "description":      "NPS – how likely customers are to recommend",
                "source":           "Bain & Company NPS Benchmarks 2023"
            },
        ]
    },
    "innovation": {
        "label": "Innovation Metrics",
        "icon":  "🔬",
        "items": [
            {
                "key":              "new_products",
                "label":            "New Products Launched",
                "path":             "innovation.new_products_launched",
                "unit":             "units",
                "higher_is_better": True,
                "description":      "Major new product / SKU launches in 2023",
                "source":           "Company press releases / annual reports"
            },
            {
                "key":              "rd_spending",
                "label":            "R&D Spending",
                "path":             "innovation.rd_spending",
                "unit":             "B USD",
                "higher_is_better": True,
                "description":      "Research & development expenditure (USD Billions)",
                "source":           "Apple 10-K / Samsung Annual Report 2023"
            },
            {
                "key":              "tech_adoption",
                "label":            "Tech Adoption Index",
                "path":             "innovation.tech_adoption_index",
                "unit":             "/ 10",
                "higher_is_better": True,
                "description":      "Composite index: AI, 5G, chip integration, platform ecosystem",
                "source":           "Composite – analyst estimates 2023"
            },
        ]
    }
}


# ─────────────────────────────────────────────
#  Utility helpers
# ─────────────────────────────────────────────

def deep_get(obj: dict, dotted_path: str):
    """Traverse 'section.key' notation into nested dict."""
    keys = dotted_path.split(".")
    val = obj
    for k in keys:
        if not isinstance(val, dict):
            return None
        val = val.get(k)
    return val


def normalise(value: float, lo: float, hi: float) -> float:
    """Map value to [0, 10] given the two extremes."""
    if hi == lo:
        return 5.0
    return round(max(0.0, min(10.0, (value - lo) / (hi - lo) * 10)), 3)


def winner_tag(val_a, val_b, higher_is_better: bool) -> str:
    if val_a is None or val_b is None:
        return "tie"
    if higher_is_better:
        if val_a > val_b:   return "A"
        if val_b > val_a:   return "B"
    else:
        if val_a < val_b:   return "A"
        if val_b < val_a:   return "B"
    return "tie"


def pct_diff(val_a, val_b) -> float:
    """Signed % difference: (A − B) / |B| × 100"""
    if not val_b:
        return 0.0
    return round((val_a - val_b) / abs(val_b) * 100, 1)


def safe_gt(a, b):
    return a is not None and b is not None and a > b


def safe_lt(a, b):
    return a is not None and b is not None and a < b


# ─────────────────────────────────────────────
#  Comparison Engine
# ─────────────────────────────────────────────

def run_comparison(company_a: dict, company_b: dict, categories: list) -> dict:
    """
    Core engine: iterate all requested metric categories,
    compute per-metric winners, normalised scores, diffs.
    Returns structured result dict.
    """
    results      = {}
    total_score_a = 0.0
    total_score_b = 0.0
    metric_count  = 0

    for cat_key in categories:
        if cat_key not in METRIC_CATALOGUE:
            continue
        cat = METRIC_CATALOGUE[cat_key]
        row_list = []

        for item in cat["items"]:
            val_a = deep_get(company_a, item["path"])
            val_b = deep_get(company_b, item["path"])

            if val_a is None or val_b is None:
                continue

            winner  = winner_tag(val_a, val_b, item["higher_is_better"])
            diff    = round(val_a - val_b, 3)
            diff_p  = pct_diff(val_a, val_b)

            lo, hi  = min(val_a, val_b), max(val_a, val_b)
            if item["higher_is_better"]:
                sc_a = normalise(val_a, lo, hi)
                sc_b = normalise(val_b, lo, hi)
            else:
                sc_a = normalise(-val_a, -hi, -lo)
                sc_b = normalise(-val_b, -hi, -lo)

            total_score_a += sc_a
            total_score_b += sc_b
            metric_count  += 1

            row_list.append({
                "key":              item["key"],
                "label":            item["label"],
                "unit":             item["unit"],
                "description":      item["description"],
                "source":           item["source"],
                "higher_is_better": item["higher_is_better"],
                "val_a":            val_a,
                "val_b":            val_b,
                "diff":             diff,
                "diff_pct":         diff_p,
                "score_a":          sc_a,
                "score_b":          sc_b,
                "winner":           winner,
            })

        results[cat_key] = {
            "label":   cat["label"],
            "icon":    cat["icon"],
            "metrics": row_list,
        }

    if metric_count == 0:
        return {"error": "No valid metrics found for selected categories."}

    # Overall scores – scale to 100
    overall_a = round(total_score_a / metric_count * 10, 1)
    overall_b = round(total_score_b / metric_count * 10, 1)
    overall_winner = "A" if overall_a > overall_b else "B" if overall_b > overall_a else "tie"

    return {
        "categories":     results,
        "total_score_a":  overall_a,
        "total_score_b":  overall_b,
        "overall_winner": overall_winner,
        "metric_count":   metric_count,
    }


# ─────────────────────────────────────────────
#  AI Insight Engine  (rule-based)
# ─────────────────────────────────────────────

def generate_insights(company_a: dict, company_b: dict, comparison: dict) -> dict:
    """
    Produce human-readable strengths, weaknesses, and
    strategic recommendations via deterministic rules.
    """
    na = company_a["name"]
    nb = company_b["name"]

    strengths_a      = []
    strengths_b      = []
    weaknesses_a     = []
    weaknesses_b     = []
    recommendations  = []

    # — Financial —
    pm_a = deep_get(company_a, "financial.profit_margin")
    pm_b = deep_get(company_b, "financial.profit_margin")
    if safe_gt(pm_a, pm_b):
        strengths_a.append(
            f"{na} achieves a {pm_a}% net profit margin vs {nb}'s {pm_b}%, "
            f"reflecting Apple's premium pricing power and high-margin services business (App Store, Apple Music, iCloud)."
        )
        weaknesses_b.append(
            f"{nb}'s {pm_b}% profit margin is constrained by heavy semiconductor manufacturing costs and intense competition in mid-range segments."
        )

    rev_a = deep_get(company_a, "financial.revenue")
    rev_b = deep_get(company_b, "financial.revenue")
    if safe_gt(rev_a, rev_b):
        strengths_a.append(
            f"{na} generated ${rev_a}B in revenue — {round(rev_a/rev_b, 1)}× more than {nb}'s ${rev_b}B — "
            f"driven by a tightly integrated hardware–software–services ecosystem."
        )

    # — Performance —
    rpe_a = deep_get(company_a, "performance.revenue_per_employee")
    rpe_b = deep_get(company_b, "performance.revenue_per_employee")
    if safe_gt(rpe_a, rpe_b):
        strengths_a.append(
            f"{na} earns ${rpe_a}M revenue per employee vs ${rpe_b}M for {nb}, "
            f"indicating far superior workforce productivity through outsourced manufacturing and a high-margin software layer."
        )
        weaknesses_b.append(
            f"{nb}'s lower revenue-per-employee ratio reflects the overhead of operating its own semiconductor fabs and diversified hardware lines."
        )
        recommendations.append(
            f"{nb} should consider accelerating its software and services revenue streams to improve per-employee productivity."
        )

    oe_a = deep_get(company_a, "financial.operating_margin")
    oe_b = deep_get(company_b, "financial.operating_margin")
    if safe_gt(oe_a, oe_b):
        strengths_a.append(
            f"{na}'s operating margin of {oe_a}% dwarfs {nb}'s {oe_b}%, "
            f"underlining Apple's unmatched ability to convert revenue to operating profit."
        )

    # — Customer —
    nps_a = deep_get(company_a, "customer.nps_score")
    nps_b = deep_get(company_b, "customer.nps_score")
    if safe_gt(nps_a, nps_b):
        strengths_a.append(
            f"{na}'s NPS of {nps_a} vs {nb}'s {nps_b} indicates significantly higher customer loyalty and willingness to recommend — "
            f"a key driver of Apple's 92% retention rate."
        )
        weaknesses_b.append(
            f"{nb}'s NPS of {nps_b} suggests that a meaningful share of customers remain passive or detractors, "
            f"partly due to fragmented Android software updates and slower premium brand positioning."
        )
        recommendations.append(
            f"{nb} should invest in a more unified post-purchase experience — faster OS updates, "
            f"premium support tiers, and loyalty programmes — to close the NPS gap."
        )

    ret_a = deep_get(company_a, "customer.retention_rate_pct")
    ret_b = deep_get(company_b, "customer.retention_rate_pct")
    if safe_gt(ret_a, ret_b):
        strengths_a.append(
            f"{na} retains {ret_a}% of customers year-on-year vs {ret_b}% for {nb}, "
            f"demonstrating the lock-in effect of the Apple ecosystem (iMessage, AirDrop, FaceTime, iCloud)."
        )

    # — Innovation —
    pat_a = deep_get(company_a, "innovation.patents_filed")
    pat_b = deep_get(company_b, "innovation.patents_filed")
    if safe_gt(pat_b, pat_a):
        strengths_b.append(
            f"{nb} filed {pat_b:,} patents in 2023 vs {na}'s {pat_a:,}, "
            f"demonstrating broader raw R&D output — particularly in semiconductor, display, and memory technologies."
        )
        recommendations.append(
            f"{na} should expand patent filings in emerging categories such as AR/VR, health sensors, and automotive to protect future product lines."
        )

    rd_pct_a = deep_get(company_a, "innovation.rd_pct_of_revenue")
    rd_pct_b = deep_get(company_b, "innovation.rd_pct_of_revenue")
    if safe_gt(rd_pct_b, rd_pct_a):
        strengths_b.append(
            f"{nb} allocates {rd_pct_b}% of revenue to R&D vs {na}'s {rd_pct_a}%, "
            f"reflecting the capital intensity of leading-edge chip (3nm/5nm) and OLED display manufacturing."
        )

    np_a = deep_get(company_a, "innovation.new_products_launched")
    np_b = deep_get(company_b, "innovation.new_products_launched")
    if safe_gt(np_b, np_a):
        strengths_b.append(
            f"{nb} launched {np_b} new products in 2023 vs {na}'s {np_a}, "
            f"covering a wider range of segments from entry-level A-series phones to foldables and home appliances."
        )
        recommendations.append(
            f"{na} should consider accelerating launch cadence in emerging form factors (foldables, mixed-reality headsets) to maintain category leadership."
        )

    # — Internal —
    gl_a = deep_get(company_a, "internal.glassdoor_rating")
    gl_b = deep_get(company_b, "internal.glassdoor_rating")
    if safe_gt(gl_a, gl_b):
        strengths_a.append(
            f"{na} scores {gl_a}/5 on Glassdoor vs {nb}'s {gl_b}/5, "
            f"reflecting stronger employer branding, higher compensation, and a more mission-driven culture."
        )
        weaknesses_b.append(
            f"{nb}'s {gl_b}/5 Glassdoor rating points to cultural challenges in its global workforce, "
            f"with common concerns around work-life balance and hierarchical management styles."
        )
        recommendations.append(
            f"{nb} should invest in global talent programmes, remote-work flexibility, and compensation parity "
            f"to attract world-class engineers in AI, software, and chip design."
        )

    # — Overall recommendation —
    overall_winner = comparison.get("overall_winner")
    sc_a           = comparison.get("total_score_a", 0)
    sc_b           = comparison.get("total_score_b", 0)

    if overall_winner == "A":
        recommendations.append(
            f"Overall, {na} leads with a benchmark score of {sc_a}/100 vs {nb}'s {sc_b}/100. "
            f"{nb} should prioritise margin improvement and customer-experience investment to close the gap."
        )
    elif overall_winner == "B":
        recommendations.append(
            f"Overall, {nb} leads with a benchmark score of {sc_b}/100 vs {na}'s {sc_a}/100. "
            f"{na} should accelerate product launch velocity and patent output to maintain its innovation edge."
        )
    else:
        recommendations.append(
            f"The two companies are closely matched overall ({sc_a}/100 vs {sc_b}/100). "
            f"Both should monitor the other's moves in AI integration and emerging markets."
        )

    return {
        "strengths_a":     strengths_a,
        "strengths_b":     strengths_b,
        "weaknesses_a":    weaknesses_a,
        "weaknesses_b":    weaknesses_b,
        "recommendations": recommendations,
    }


# ─────────────────────────────────────────────
#  Routes — Pages
# ─────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


# ─────────────────────────────────────────────
#  Routes — API
# ─────────────────────────────────────────────

@app.route("/api/companies", methods=["GET"])
def api_companies():
    """List all available companies (id, name, ticker, industry)."""
    listing = [
        {
            "id":          cid,
            "name":        c["name"],
            "ticker":      c["ticker"],
            "industry":    c["industry"],
            "hq":          c["hq"],
            "logo_color":  c["logo_color"],
        }
        for cid, c in COMPANIES.items()
    ]
    return jsonify({"companies": listing, "metadata": META})


@app.route("/api/company/<company_id>", methods=["GET"])
def api_company(company_id):
    """Full data snapshot for a single company."""
    company = COMPANIES.get(company_id)
    if not company:
        return jsonify({"error": f"Company '{company_id}' not found."}), 404
    return jsonify(company)


@app.route("/api/categories", methods=["GET"])
def api_categories():
    """Return list of available benchmark categories."""
    cats = [
        {"key": k, "label": v["label"], "icon": v["icon"], "metric_count": len(v["items"])}
        for k, v in METRIC_CATALOGUE.items()
    ]
    return jsonify({"categories": cats})


@app.route("/api/compare", methods=["GET"])
def api_compare():
    """
    Main comparison endpoint.

    Query parameters:
      company_a  – id of Company A   (default: apple)
      company_b  – id of Company B   (default: samsung)
      category   – one of: all | financial | performance | internal | customer | innovation
    """
    id_a     = request.args.get("company_a", "apple").strip().lower()
    id_b     = request.args.get("company_b", "samsung").strip().lower()
    cat_arg  = request.args.get("category", "all").strip().lower()

    company_a = COMPANIES.get(id_a)
    company_b = COMPANIES.get(id_b)

    if not company_a:
        return jsonify({"error": f"Company '{id_a}' not found."}), 404
    if not company_b:
        return jsonify({"error": f"Company '{id_b}' not found."}), 404
    if id_a == id_b:
        return jsonify({"error": "Please select two different companies."}), 400

    # Resolve which categories to compare
    if cat_arg == "all":
        cats = list(METRIC_CATALOGUE.keys())
    elif cat_arg in METRIC_CATALOGUE:
        cats = [cat_arg]
    else:
        return jsonify({"error": f"Unknown category '{cat_arg}'."}), 400

    # Run comparison engine
    comparison = run_comparison(company_a, company_b, cats)
    if "error" in comparison:
        return jsonify(comparison), 500

    # Generate insights
    insights = generate_insights(company_a, company_b, comparison)

    return jsonify({
        "company_a":     {"id": id_a, "name": company_a["name"], "ticker": company_a["ticker"], "color": company_a["logo_color"]},
        "company_b":     {"id": id_b, "name": company_b["name"], "ticker": company_b["ticker"], "color": company_b["logo_color"]},
        "category_filter": cat_arg,
        "comparison":    comparison["categories"],
        "total_score_a": comparison["total_score_a"],
        "total_score_b": comparison["total_score_b"],
        "overall_winner": comparison["overall_winner"],
        "metric_count":  comparison["metric_count"],
        "insights":      insights,
        "metadata":      META,
    })


# ─────────────────────────────────────────────
#  Routes — Downloads
# ─────────────────────────────────────────────

@app.route("/api/download/json")
def download_json():
    path = os.path.join(BASE_DIR, "data", "companies.json")
    return send_file(path, as_attachment=True, download_name="benchmark_dataset_2023.json")


@app.route("/api/download/csv")
def download_csv():
    path = os.path.join(BASE_DIR, "data", "benchmark_dataset.csv")
    return send_file(path, as_attachment=True, download_name="benchmark_dataset_2023.csv")


@app.route("/api/download/sql")
def download_sql():
    path = os.path.join(BASE_DIR, "data", "schema.sql")
    return send_file(path, as_attachment=True, download_name="benchmarkiq_schema.sql")


# ─────────────────────────────────────────────
#  Entry Point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "="*55)
    print("  BenchmarkIQ — Company Benchmark Comparison System")
    print("="*55)
    print(f"  Data: FY 2023 | Companies: Apple vs Samsung")
    print(f"  Open → http://localhost:5000")
    print("="*55 + "\n")
    app.run(debug=True, port=5000)
