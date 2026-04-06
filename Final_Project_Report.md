# Final Project Report — Foundations of AI (H9FAI)

Project title: Comparative Ethical Policy Auditor (CEPA)
Team: <Team Member Names — add full names & student numbers here>
Date: 27-March-2026

---

## Abstract (100–150 words)

CEPA is an AI-assisted platform that helps people compare the policy documents published by major AI providers (terms of use, privacy policies, acceptable-use policies, and model/system cards). Instead of expecting users to read long legal text, CEPA extracts relevant clauses, groups them into clear categories (privacy, commercial use, liability, and safety/content restrictions), and produces an explainable “user‑friendliness” score with direct quotes as evidence. Our approach is intentionally hybrid: we combine simple, deterministic heuristics (as a reliable baseline) with LLM-based semantic analysis (to capture meaning beyond keywords). This report outlines the problem we’re tackling, the system design, how we will collect and preprocess data, how we plan to evaluate accuracy and trustworthiness, and the main ethical considerations. The full literature review will be added in a later revision once the 25+ papers are finalised.

## Keywords

policy analysis, legal-NLP, explainable AI, model auditing, clause classification

## 1. Introduction

Public-facing policy documents are important, but they’re also hard to work with. They are long, written in legal language, and spread across multiple pages. In practice, most users never read them end-to-end, and even motivated users struggle to compare providers fairly. This makes it easy to miss meaningful differences in privacy protections, data sharing, licensing, liability, and content restrictions.

CEPA (Comparative Ethical Policy Auditor) is our attempt to make these documents more understandable and comparable. The goal is not to provide legal advice, but to give users a transparent, evidence-backed summary and a consistent way to compare providers side-by-side.

Research questions:
- RQ1: Can a hybrid pipeline (LLM + deterministic heuristics) detect "concerning" clauses with sufficient precision to support automated triage?
- RQ2: Does anchoring LLM outputs to source snippets reduce hallucination and increase user trust compared with LLM summaries alone?
- RQ3: How well do automated rankings of "user-friendliness" align with expert human judgments?

In practical terms, CEPA will ship as a simple web interface where a user selects two companies and receives a scorecard, short plain‑English explanations, and highlighted evidence snippets. Alongside the UI, our deliverables include a reproducible dataset of collected documents, a small annotated ground-truth set (clause-level labels), and an evaluation suite that measures detection quality (precision/recall/F1), ranking agreement (e.g., Spearman’s rho), and explanation quality via a small user study.

## 2. Related Work (placeholder)

This section will be completed in the final submission and will include **a minimum of 15 state-of-the-art research papers** (as required in the CA brief). We also plan to expand it to **25+ papers** to support the broader project report.

At a minimum, the review will cover legal-NLP datasets/benchmarks (e.g., CUAD for contract clause understanding, LexGLUE for legal NLP tasks, and OPP‑115 for privacy policy annotations), plus recent research on contract clause extraction, legal summarisation, and evaluation of LLM-based systems.

The goal here is critical evaluation, not just a summary: we will compare methods, highlight what works well and what doesn’t for our setting (policy documents from AI providers), and justify why a hybrid, evidence-anchored approach is a good fit.

## 3. Project Overview & Objectives

Primary objective: Build an automated system that takes policy/legal documents for two or more AI providers, summarises them along clear axes, and produces a measurable “user‑friendliness” score. The system should also flag potentially concerning clauses and show the exact source text behind each claim.

Secondary objectives:
- Evaluate LLM-based outputs against rule-based baselines and human annotations.
- Produce a UI that presents explainable verdicts tailored to non-expert users.
- Release an annotated dataset and reproducible evaluation scripts.

Success criteria:
- Clause-level detection: target F1 ≥ 0.7 for the "concerning" class on the annotation test set.
- Ranking agreement: Spearman's rho ≥ 0.6 against an expert ranking of providers.
- User study: mean perceived trust/usefulness ≥ 4/5 for the interface with anchored citations.

Advantages and disadvantages (at a glance):
- **Advantages:** transparent evidence snippets, explainable baselines, and better semantic coverage when LLMs are used.
- **Disadvantages / risks:** LLM cost and rate limits, potential hallucinations (mitigated via anchoring), and subjective judgement in what counts as “concerning” (mitigated via annotation guidelines and inter-annotator agreement).

## 4. Methodology

### 4.1 Data collection

We will collect a corpus of public policy documents from selected AI providers (e.g., OpenAI, Microsoft, Google, Anthropic, Meta). For each provider, we will archive the raw HTML and also store a cleaned, extracted plain‑text version under `documents/<company>/`. We will timestamp snapshots so that results are reproducible even if providers update their pages later. Data collection will follow fair scraping practices (respect robots.txt, rate limiting, and minimal load).

### 4.2 Annotation / Ground truth

To evaluate the system properly, we need some ground truth. We will create a clause-level annotation schema where each clause is:
- tagged with one or more categories (privacy, data retention, commercial use, liability/indemnity, content restrictions, IP/license, termination, etc.)
- given a severity score (1–5)
- labelled overall as *user‑friendly*, *neutral*, or *concerning*

Annotations will be exported as CSV/JSON into `documents/annotations/`. We are aiming for ~200–500 annotated clauses (more if time allows). Where possible, multiple annotators will label overlapping subsets so we can measure agreement (e.g., Cohen’s kappa) and refine the guidance.

### 4.3 Preprocessing

The raw documents will be cleaned and normalised before analysis. We will remove boilerplate and navigation text, segment content into clause-sized chunks, and keep headings when they provide context. On top of that, we will run basic NLP preprocessing (sentence segmentation, tokenisation), optional NER for privacy-related entities, and a set of simple features that are useful in legal text (modal verbs like *may*/*must*, negation patterns, and licensing/transfer keywords).

### 4.4 Baseline systems (rule-based)

We’ll start with interpretable baselines:
- keyword dictionaries + heuristic scoring (e.g., spotting patterns such as “we may share”, “indemnify”, “without notice”, “perpetual license”)
- a simple feature-based classifier (logistic regression or SVM) trained on handcrafted features for a stronger non-LLM baseline

These baselines matter because they give us a stable reference point and help us understand the incremental benefit of LLMs.

### 4.5 Advanced systems (LLM-based pipeline)

On top of the baselines, we’ll build an LLM-assisted pipeline for higher-level understanding. Prompted tasks will include clause classification, short rationales, and category-level summaries.

The key design choice is *anchoring*. For every claim the model makes, CEPA will return the exact supporting snippet (plus offsets where possible) and a confidence estimate. We will also combine LLM outputs with rule-based scores (e.g., a weighted ensemble or a small meta-classifier) to improve precision and reduce hallucinations.

Any LLM usage will be handled server-side. API keys will be stored in environment variables and never committed to the repository.

## 5. System Design & Implementation

### 5.1 Architecture

CEPA will use a straightforward web architecture:

- **Backend (Python + Flask / REST API):** document ingestion + storage (filesystem + metadata), a local analyser (heuristics + features), an LLM wrapper (prompts, retries, rate limiting), a scoring and comparison engine, and an insights/recommendation module.
- **Frontend (single page UI):** HTML/CSS/vanilla JS (and Chart.js where visualisations help) to render comparisons and highlight evidence snippets.

### 5.2 Current repo mapping (implemented)

This repository already contains a Flask backend plus a comparison-style UI (built originally for a benchmarking demo). We plan to reuse that structure:

- `app.py` currently hosts a comparison engine and REST endpoints. For CEPA, we will reuse the Flask scaffold and adapt endpoints for policy comparison.
- `templates/` and `static/` already support a dashboard-like UI and can be repurposed to show evidence snippets and scorecards.
- We will add new folders: `documents/` for collected policy documents, and `documents/annotations/` for labelled evaluation data.

### 5.3 Implementation plan (near-term)

We are planning to build CEPA in three short phases:
1. **Phase 1 (2–3 weeks):** scaffolding, ingestion pipeline, and rule-based analyser.
2. **Phase 2 (2–3 weeks):** prompt design + LLM integration, plus an initial annotation set and baseline evaluation.
3. **Phase 3 (1–2 weeks):** UI polishing, user study, and packaging the final reproducible artefacts + report.

## 6. Evaluation Plan

### 6.1 Detection metrics

We’ll evaluate clause detection the normal way: Precision, Recall, and F1 for the “concerning” class. We’ll also include confusion matrices and breakdowns per category (privacy vs liability vs commercial use, etc.), because a single headline score can hide important failure modes.

### 6.2 Ranking metrics

Since the product ultimately outputs a ranking/score, we’ll measure how well our rankings match expert human rankings using Spearman’s rho and Kendall’s tau. We’ll also report mean absolute rank error for a more intuitive “how far off were we?” view.

### 6.3 Explanation & summarisation

Automatic metrics (e.g., ROUGE/ROUGE‑L) can help sanity-check summary consistency, but we’ll rely more on human judgement for faithfulness and usefulness. We plan a small user study (6–8 raters, ~30 comparisons) with Likert-scale questions around trust, clarity, and usefulness. A key experimental condition will be “LLM summary with citations” vs “LLM summary without citations”.

### 6.4 Statistical significance

Where we compare methods, we will use bootstrap or permutation tests to check whether observed improvements are likely to be real rather than noise.

## 7. Ethical, Legal & Practical Considerations

This project touches legal text, so we need to be careful about how results are presented and used:

- **Not legal advice:** CEPA is an informational tool. The UI and report will include clear disclaimers.
- **Data governance:** we will store only public documents; we won’t collect user personal data; and we will keep all API keys and credentials out of the repo (environment variables).
- **Responsible collection:** follow robots.txt and site terms where applicable, and rate-limit crawling.
- **Bias and context:** policies vary by region and regulator. We will avoid treating differences as purely “better/worse” without context.
- **Human annotation ethics:** use a clear annotation guide, avoid overclaiming certainty, and credit contributors appropriately.

## 8. Expected Outcomes & Deliverables

- Working web prototype for pairwise policy comparison with anchored citations.
- Annotated evaluation dataset (clauses + labels) and evaluation scripts.
- Final project report (PDF) with literature review, experiments, and user study results.
- Code release and instructions for reproducibility.

## 9. Timeline & Milestones

- Week 1–2: finalize dataset list & scaffolding; implement ingestion and rule-based analyzer.
- Week 3–4: annotation (200 clauses) and baseline experiments.
- Week 5–7: LLM integration, prompt tuning; run main experiments and collect metrics.
- Week 8: user study and UI polish.
- Week 9–10: write final report and prepare final submission (PDF + code + dataset).

## 10. Conclusion

CEPA is meant to make policy comparison more accessible, transparent, and reproducible. Our core idea is to combine the reliability of deterministic heuristics with the flexibility of LLM-based understanding, while keeping the system grounded in direct evidence snippets. The immediate next steps are to finalise the paper list for the literature review (25+ papers), produce the first annotation batch, and run the baseline vs hybrid evaluations described above.

## References (placeholder)

- [To be populated with 25+ research papers: CUAD, LexGLUE, OPP-115, contract clause extraction, legal summarization, model auditing literature.]

## Appendix

- Current repository snapshot: `app.py`, `templates/`, `static/`, and `data/companies.json` (used by the benchmark demo). For CEPA, we will create `documents/` and `documents/annotations/` directories and add scripts for scraping and extraction (`scripts/ingest.py`).


---

Notes:
- I focused this draft on the deliverables requested by the H9FAI assignment and content specific to the CEPA project described in the draft `EthiCAL INTIGRITY - FAI REPORT.docx`.
- Related work and the detailed literature review will be added after you provide or confirm the 25+ papers to cite.
- I can convert this Markdown into PDF/DOCX, or produce a formatted LaTeX/PDF if you want a submission-ready file next. Please tell me your preferred final format and any student names/student numbers to include on the title page.
