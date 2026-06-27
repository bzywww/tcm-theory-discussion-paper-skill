---
name: tcm-theory-discussion-paper
description: Plan, draft, revise, and audit Chinese TCM theory discussion manuscripts for journals such as 中医学报. Use when selecting a precise TCM theory topic, building a classic-source to pathogenesis to treatment/formula argument, integrating modern mechanisms without losing Chinese medicine logic, or reviewing DOCX/text drafts for theory-discussion style.
---

# TCM Theory Discussion Paper

Use this skill to help write Chinese 中医理论探讨 papers. Keep the article anchored in a real clinical problem, orthodox Chinese medicine theory, a precise disease/stage/symptom-state cut, and a complete 理-法-方-药 argument.

## Core Workflow

1. **Clarify the clinical problem before choosing the theory.** Identify the disease carrier, disease stage, symptom-state, unresolved clinical contradiction, and target journal style.
2. **Choose a precise topic.** For topic selection or title revision, read `references/topic_selection.md`.
3. **Build the article architecture.** For outlines, section titles, or full drafting, read `references/article_structure.md`.
4. **Assign evidence functions.** For classical quotations, modern mechanisms, and literature role assignment, read `references/evidence_rules.md`.
5. **Write in theory-discussion style.** For headings, phrasing, paragraph discipline, and common failure modes, read `references/style_rules.md`.
6. **Audit before delivery.** For manuscript review, read `references/review_checklist.md`. If a `.docx` or `.txt` draft is available and Python can run, execute `scripts/audit_manuscript.py` and use its output as a first-pass risk screen.

## Non-Negotiable Principles

- Do not start from a fashionable theory. Start from a real clinical problem that existing explanations do not fully clarify.
- Do not write a literature review disguised as theory discussion. Literature must serve a pathogenesis argument.
- Do not use task-like section titles such as “理论基础”, “病机分析”, “现代机制”, or “治疗思路” unless the target journal explicitly requires them. Prefer titles that state academic claims.
- Do not let modern mechanisms become the main building. Use them as a bridge to clarify one difficult TCM pathogenesis link.
- Do not pile up classical quotations. Each original text must support one specific function: concept, physiology, etiology, pathogenesis, transmission, treatment principle, or formula logic.
- Do not end with generic treatment lists. Treatment and formulas must be derived from the core pathogenesis.

## Capability Fallbacks

- If DOCX tools are available, extract title, abstract, headings, body, and references directly. If not, ask the user for pasted text or a `.txt` export.
- If Zotero, CNKI, Wanfang, Google Scholar, or web access is available, use it only for legal metadata/full-text discovery and verification. If not, ask the user for exported citation lists or downloaded papers.
- Never ask for database passwords. Ask the user to log in locally and export/download files when needed.
- If scripts cannot run, apply `references/review_checklist.md` manually.

## Output Expectations

For topic planning, output candidate titles, rationale, innovation, repetition risks, and required evidence.  
For outlines, output a section chain where each title is an academic claim.  
For drafting, write Chinese academic prose, not explanatory chat.  
For review, lead with structural and argument risks, then language and reference issues.
