/* ================================================
   BenchmarkIQ — Frontend JavaScript
   Handles API calls, DOM rendering, Chart.js
   ================================================ */

"use strict";

// ── Module-level chart references ──
let _radar = null;
let _bar   = null;

// ════════════════════════════════════════════
//  ENTRY POINT
// ════════════════════════════════════════════
async function runComparison() {
  const idA  = document.getElementById("sel-a").value;
  const idB  = document.getElementById("sel-b").value;
  const cat  = document.getElementById("sel-cat").value;

  if (idA === idB) {
    alert("Please choose two different companies.");
    return;
  }

  setLoading(true);

  try {
    const url  = `/api/compare?company_a=${idA}&company_b=${idB}&category=${cat}`;
    const resp = await fetch(url);
    if (!resp.ok) {
      const err = await resp.json().catch(() => ({}));
      throw new Error(err.error || `HTTP ${resp.status}`);
    }
    const data = await resp.json();
    renderAll(data);

    const results = document.getElementById("results");
    results.style.display = "block";
    results.classList.add("fade-in");

    setTimeout(() => {
      document.getElementById("section-scores")
        .scrollIntoView({ behavior: "smooth", block: "start" });
    }, 80);

  } catch (e) {
    alert("Error: " + e.message);
    console.error(e);
  } finally {
    setLoading(false);
  }
}

// ════════════════════════════════════════════
//  LOADING STATE
// ════════════════════════════════════════════
function setLoading(on) {
  document.getElementById("loader").style.display = on ? "flex" : "none";
  document.getElementById("btn-compare").disabled = on;
}

// ════════════════════════════════════════════
//  MASTER RENDER
// ════════════════════════════════════════════
function renderAll(data) {
  renderScores(data);
  renderCharts(data);
  renderMetricTables(data);
  renderInsights(data);
  renderSources(data);
}

// ════════════════════════════════════════════
//  SCORE HEADER
// ════════════════════════════════════════════
function renderScores(data) {
  const { company_a, company_b, total_score_a, total_score_b, overall_winner } = data;

  // Company names
  setText("sc-name-a", company_a.name);
  setText("sc-name-b", company_b.name);

  // Numeric scores
  setText("sc-val-a", total_score_a.toFixed(1));
  setText("sc-val-b", total_score_b.toFixed(1));

  // Animated bars
  setTimeout(() => {
    setStyle("sc-bar-a", "width", total_score_a + "%");
    setStyle("sc-bar-b", "width", total_score_b + "%");
  }, 100);

  // Winner badge
  hide("winner-tag-a"); hide("winner-tag-b");
  if (overall_winner === "A") { show("winner-tag-a"); }
  if (overall_winner === "B") { show("winner-tag-b"); }

  // Center
  const winName = overall_winner === "A" ? company_a.name
                : overall_winner === "B" ? company_b.name
                : "— Tie —";
  setText("overall-winner-name", winName);
  const delta = Math.abs(total_score_a - total_score_b).toFixed(1);
  setText("overall-delta", `Score gap: ${delta} pts`);
}

// ════════════════════════════════════════════
//  CHARTS
// ════════════════════════════════════════════
function renderCharts(data) {
  buildRadar(data);
  buildBar(data);
}

function buildRadar(data) {
  const ctx = document.getElementById("radarChart").getContext("2d");

  const labels = [], scA = [], scB = [];

  for (const [, cat] of Object.entries(data.comparison)) {
    const arr = cat.metrics;
    if (!arr.length) continue;
    labels.push(cat.label.replace(" Metrics", ""));
    const avgA = arr.reduce((s, m) => s + m.score_a, 0) / arr.length;
    const avgB = arr.reduce((s, m) => s + m.score_b, 0) / arr.length;
    scA.push(+avgA.toFixed(2));
    scB.push(+avgB.toFixed(2));
  }

  if (_radar) _radar.destroy();

  _radar = new Chart(ctx, {
    type: "radar",
    data: {
      labels,
      datasets: [
        { label: data.company_a.name, data: scA,
          backgroundColor: "rgba(96,165,250,.14)",
          borderColor:      "rgba(96,165,250,.9)",
          borderWidth: 2, pointBackgroundColor: "rgba(96,165,250,.9)", pointRadius: 4 },
        { label: data.company_b.name, data: scB,
          backgroundColor: "rgba(244,114,182,.14)",
          borderColor:      "rgba(244,114,182,.9)",
          borderWidth: 2, pointBackgroundColor: "rgba(244,114,182,.9)", pointRadius: 4 },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { labels: { color: "#9CA3AF", font: { size: 12, family: "DM Sans" } } }
      },
      scales: {
        r: {
          min: 0, max: 10,
          ticks: { color: "#6B7280", backdropColor: "transparent", stepSize: 2 },
          grid:  { color: "rgba(255,255,255,.07)" },
          angleLines: { color: "rgba(255,255,255,.07)" },
          pointLabels: { color: "#9CA3AF", font: { size: 12, family: "DM Sans" } },
        }
      }
    }
  });
}

function buildBar(data) {
  const ctx = document.getElementById("barChart").getContext("2d");

  const labels = [], scA = [], scB = [];

  for (const [, cat] of Object.entries(data.comparison)) {
    for (const m of cat.metrics) {
      labels.push(m.label);
      scA.push(m.score_a);
      scB.push(m.score_b);
    }
  }

  if (_bar) _bar.destroy();

  _bar = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [
        { label: data.company_a.name, data: scA,
          backgroundColor: "rgba(96,165,250,.75)", borderColor: "rgba(96,165,250,1)",
          borderWidth: 1, borderRadius: 4 },
        { label: data.company_b.name, data: scB,
          backgroundColor: "rgba(244,114,182,.75)", borderColor: "rgba(244,114,182,1)",
          borderWidth: 1, borderRadius: 4 },
      ],
    },
    options: {
      indexAxis: "y",
      responsive: true,
      plugins: {
        legend: { labels: { color: "#9CA3AF", font: { size: 12, family: "DM Sans" } } },
        tooltip: { callbacks: { label: ctx => ` Score: ${ctx.parsed.x.toFixed(1)} / 10` } }
      },
      scales: {
        x: { min: 0, max: 10,
             ticks: { color: "#6B7280", font: { size: 11 } },
             grid:  { color: "rgba(255,255,255,.07)" } },
        y: { ticks: { color: "#9CA3AF", font: { size: 11 } },
             grid:  { color: "rgba(255,255,255,.04)" } },
      }
    }
  });
}

// ════════════════════════════════════════════
//  METRIC TABLES
// ════════════════════════════════════════════
function renderMetricTables(data) {
  const container = document.getElementById("metric-tables");
  container.innerHTML = "";

  const nameA = data.company_a.name;
  const nameB = data.company_b.name;

  for (const [, cat] of Object.entries(data.comparison)) {
    if (!cat.metrics.length) continue;

    const block = document.createElement("div");
    block.className = "cat-block";

    block.innerHTML = `
      <div class="cat-header">
        <span class="cat-header__icon">${cat.icon}</span>
        <span class="cat-header__name">${cat.label}</span>
      </div>
      <table class="metric-tbl">
        <thead>
          <tr>
            <th>Metric</th>
            <th class="th-a">${nameA}</th>
            <th class="th-b">${nameB}</th>
            <th>Difference</th>
            <th>Score (0–10)</th>
            <th class="th-c">Winner</th>
          </tr>
        </thead>
        <tbody>
          ${cat.metrics.map(m => buildRow(m, nameA, nameB)).join("")}
        </tbody>
      </table>
    `;
    container.appendChild(block);
  }
}

function buildRow(m, nameA, nameB) {
  // Format value with smart precision
  const fmtV = v => {
    if (v === null || v === undefined) return "—";
    const abs = Math.abs(v);
    if (abs >= 1000) return v.toLocaleString("en-US", { maximumFractionDigits: 0 });
    if (abs >= 10)   return v.toLocaleString("en-US", { maximumFractionDigits: 1 });
    return v.toLocaleString("en-US", { maximumFractionDigits: 2 });
  };

  const diffCls = m.diff >= 0 ? "pos" : "neg";
  const sign    = m.diff >= 0 ? "+" : "";

  // Winner pill
  let pill;
  if      (m.winner === "A") pill = `<span class="pill pill--a">🏆 ${nameA}</span>`;
  else if (m.winner === "B") pill = `<span class="pill pill--b">🏆 ${nameB}</span>`;
  else                        pill = `<span class="pill pill--tie">— Tie</span>`;

  // Score bars — each side gets up to 50% of the bar container width
  const wA = (m.score_a / 10 * 100).toFixed(1);
  const wB = (m.score_b / 10 * 100).toFixed(1);

  return `
    <tr>
      <td>
        <div class="td-label">${m.label}</div>
        <div class="td-unit">${m.unit} · ${m.source}</div>
      </td>
      <td class="td-val-a">${fmtV(m.val_a)}</td>
      <td class="td-val-b">${fmtV(m.val_b)}</td>
      <td class="td-diff">
        <span class="${diffCls}">${sign}${fmtV(m.diff)} (${sign}${m.diff_pct}%)</span>
      </td>
      <td>
        <div class="score-bars">
          <div class="score-bar score-bar--a" style="width:${wA}%;max-width:46%"></div>
          <div class="score-bar score-bar--b" style="width:${wB}%;max-width:46%"></div>
          <span class="score-num">${m.score_a.toFixed(1)} | ${m.score_b.toFixed(1)}</span>
        </div>
      </td>
      <td class="td-winner">${pill}</td>
    </tr>
  `;
}

// ════════════════════════════════════════════
//  INSIGHTS
// ════════════════════════════════════════════
function renderInsights(data) {
  const { insights, company_a, company_b } = data;
  const grid = document.getElementById("insights-grid");
  grid.innerHTML = "";

  const cards = [
    { cls: "ins-card--a",    icon: "💪", title: `${company_a.name} — Strengths`,     items: insights.strengths_a },
    { cls: "ins-card--b",    icon: "💪", title: `${company_b.name} — Strengths`,     items: insights.strengths_b },
    { cls: "ins-card--weak", icon: "⚠️", title: "Identified Weaknesses",              items: [...(insights.weaknesses_a||[]), ...(insights.weaknesses_b||[])] },
    { cls: "ins-card--rec",  icon: "🎯", title: "Strategic Recommendations",          items: insights.recommendations },
  ];

  for (const card of cards) {
    if (!card.items || !card.items.length) continue;
    const el = document.createElement("div");
    el.className = `ins-card ${card.cls}`;
    el.innerHTML = `
      <div class="ins-card__head">
        <span class="ins-card__icon">${card.icon}</span>
        <span class="ins-card__title">${card.title}</span>
      </div>
      <ul class="ins-list">
        ${card.items.map(i => `<li>${i}</li>`).join("")}
      </ul>
    `;
    grid.appendChild(el);
  }
}

// ════════════════════════════════════════════
//  DATA SOURCES
// ════════════════════════════════════════════
function renderSources(data) {
  const list = document.getElementById("sources-list");
  list.innerHTML = (data.metadata.sources || [])
    .map(s => `<div class="source-tag">${s}</div>`)
    .join("");
}

// ════════════════════════════════════════════
//  TINY DOM HELPERS
// ════════════════════════════════════════════
function setText(id, text)         { const el = document.getElementById(id); if (el) el.textContent = text; }
function setStyle(id, prop, val)   { const el = document.getElementById(id); if (el) el.style[prop] = val; }
function show(id)                  { const el = document.getElementById(id); if (el) el.style.display = ""; }
function hide(id)                  { const el = document.getElementById(id); if (el) el.style.display = "none"; }

// ════════════════════════════════════════════
//  AUTO-RUN on first load
// ════════════════════════════════════════════
window.addEventListener("DOMContentLoaded", () => runComparison());
