# Which CV To Use — Mahmoud Alyosify

All files use the same LaTeX template as `CV July 2026.tex` (XeLaTeX, Arial with TeX Gyre Heros fallback, ATS-safe: no columns in body text, no graphics, standard headings, ligatures disabled, PDF keyword metadata set per role).

**Rule of thumb:** never send the General CV to an actual job posting. Pick the persona that matches the job title, then tweak 2–3 bullets to echo the job description's exact wording.

---

## The general one (root folder)

| File | Send it when |
|---|---|
| `../Mahmoud Alyosify - General CV.tex` | A friend, professor, or contact asks "send me your CV" with no role attached. Referrals, networking, LinkedIn DMs, conference intros. |

This is the only deliberately broad CV. It stays coherent (AI/ML Engineer — LLM systems + applied ML + deployment) rather than listing every domain.

---

## The 13 role-specific CVs

| # | File | Target job titles |
|---|---|---|
| 01 | LLM and Generative AI Engineer | LLM Engineer, GenAI Engineer, Applied LLM, Foundation Model Engineer, Prompt/Inference Engineer |
| 02 | Machine Learning Engineer | ML Engineer, Applied ML Engineer, AI Engineer (generalist ML), Junior/Associate MLE |
| 03 | Computer Vision Engineer | CV Engineer, Perception Engineer, Visual Search / Image Retrieval, Medical Imaging (entry) |
| 04 | Reinforcement Learning Engineer | RL Engineer, Decision Intelligence, Control/Optimisation, Simulation Engineer |
| 05 | AI Research Engineer | Research Engineer, Applied Scientist, AI Resident, Research Assistant, Lab roles |
| 06 | Edge and Efficient AI Engineer | Edge AI, On-Device AI, Embedded AI, Inference Optimisation, Model Optimisation, AI Performance Engineer |
| 07 | AI Agent Systems Engineer | Agentic AI Engineer, AI Automation Engineer, Multi-Agent Systems, AI Product Engineer |
| 08 | NLP Engineer | NLP Engineer, Conversational AI, Text Analytics, Information Extraction |
| 09 | Data Scientist | Data Scientist, Data Analyst, Analytics Engineer, Decision Scientist |
| 10 | AI Security and Threat Intelligence Engineer | AI Security Engineer, CTI Analyst, OSINT Engineer, ML for Security, Fraud/Anomaly Detection |
| 11 | MLOps and Cloud AI Engineer | MLOps Engineer, ML Platform, Cloud AI Engineer, AI Infrastructure, ML Systems |
| 12 | Software Engineer | Software Engineer, Backend (.NET or Python), Full-Stack, Data Systems Engineer |
| 13 | AI Instructor and Technical Trainer | Instructor, Technical Trainer, TA, Curriculum Developer, Developer Advocate, EdTech |

---

## The two special-purpose CVs

| # | File | Use for |
|---|---|---|
| 14 | Academic CV - PhD Scholarship | PhD applications, supervisor cold emails, research scholarships (Vanier, CSC, DAAD, Marie Curie, university funding), RA positions. Leads with Research Interests, frames each project as question → method → design → scope → reproducibility, and ends with References available on request. |
| 15 | Volunteering Fellowships and Exchange Programmes | Volunteering, youth programmes, exchange/mobility schemes, travel grants, leadership fellowships, "AI for Good" programmes. Leads with community leadership and open education, then international recognition, then socially-relevant projects. |

---

## Before you send any of them

1. **Read the job description twice** and mirror its exact vocabulary in the summary and 2–3 bullets. If they say "GenAI", don't only write "LLM". If they say "PyTorch", make sure PyTorch appears early.
2. **Reorder projects** so the most relevant one sits first — the template makes this a copy-paste of one `\cvproject` block.
3. **Cut, don't add.** If a section pushes past two pages, drop the least relevant project rather than shrinking the font.
4. **Rename the exported PDF** to `Mahmoud Alyosify - <Role> - <Company>.pdf`. Recruiters see the filename before they see the CV.
5. **Never send the .tex** — export to PDF.

## Things worth adding as soon as they exist

- Master's completion (Nov 2026) → change `Expected Nov 2026` to `Completed Nov 2026` in every file (one `\cventry` line each).
- Any publication or preprint from CISC 898 → add a `Publications` section to CV 14 first; it is the single biggest upgrade to the PhD application.
- Concrete numbers from the research project (e.g. "% token reduction", "% latency saved") → add them to CVs 01, 05, 06, 11. Right now those CVs describe the method rigorously but carry no headline result number.
- English test score (IELTS/TOEFL) → CVs 14 and 15.
