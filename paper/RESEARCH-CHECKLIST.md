# Reporting checklist

**"Other Cardiometabolic Health" — Mechanism without outcome: a claim-level audit of
AI-generated insulin misinformation in a disease with a 48-hour error budget**

Utah Hans · Independent researcher

---

## Which checklist, and why this one is an imperfect fit

**No EQUATOR-registered reporting guideline covers this design.** It is not a trial
(CONSORT), not an epidemiological study of human participants (STROBE as intended), not a
systematic review (PRISMA), not a diagnostic accuracy study (STARD), not a case report
(CARE), and not a quality-improvement report (SQUIRE).

It is an exhaustive content audit of a single document, with blinded classification and four
experiments in which the subjects were software systems.

**STROBE is used below as the closest available frame**, because its items — setting,
variables, bias, study size, statistical methods, limitations — map onto this design more
cleanly than any alternative, and because an imperfect declared mapping is more useful to an
editor than no checklist. Items that genuinely do not apply are marked **n/a** with the
reason, rather than silently skipped or stretched.

Line numbers refer to the submitted Word manuscript, which carries continuous line numbering.
Where a line reference would be fragile, the section number is given instead.

---

## STROBE items

| # | Item | Addressed? | Where |
|---|---|---|---|
| **1a** | Study design in the title or abstract | Yes | Title and Abstract — "a claim-level audit" |
| **1b** | Informative, balanced abstract | Yes | Abstract states the null result (0/8, 0/9), both dichotomisations, the non-significant strict coding, and the failure of the counts to reproduce |
| **2** | Background and rationale | Yes | §1 |
| **3** | Objectives and pre-specified hypotheses | Yes, with a caveat | §1; and SAP §1 states plainly that the core hypothesis emerged from the data and was **not** pre-registered |
| **4** | Study design, early in the paper | Yes | §2.1–§2.4 |
| **5** | Setting, locations, relevant dates | Yes | §2.1; all work 28–29 October 2026 |
| **6a** | Eligibility criteria, sources, selection methods | Yes | §2.2 — all substantive factual claims; non-empirical content inventoried but not scored, with the reason |
| **6b** | Matching criteria | n/a | No matched design |
| **7** | Variables: outcomes, exposures, predictors, confounders, effect modifiers | Yes | §2.2 (verdict), §2.3 (stratum); SAP §2 |
| **8** | Data sources and measurement, for each variable | Yes | §2.2; sources were PubMed, *Nature*, NEJM, *The Lancet*, ClinicalTrials.gov, UniProt, USP, SEC filings |
| **9** | Efforts to address sources of bias | **Yes, and the failures are reported** | §2.3 blinding; §3.2 blinding weakened the result; §2.6 contamination control; §5.1–§5.4 the biases that remain |
| **10** | Study size, and how arrived at | Yes | §2.2; SAP §1 — the denominator is the claim count of one document, and §3.8 reports that it does not reproduce |
| **11** | Quantitative variables: handling, groupings, why | Yes | §2.4 and SAP §2.3 — both dichotomisations reported; ordinal primary analysis chosen to avoid the cut |
| **12a** | Statistical methods, including confounding control | Yes | §2.4; SAP §3 |
| **12b** | Methods for subgroups and interactions | Yes | §3.3 Table 2b; §3.8 decomposition variants |
| **12c** | How missing data were addressed | Yes | §5.13; SAP §7 — one probe lost to an automated safety classifier, reported and deliberately not retried |
| **12d** | Loss to follow-up / sampling strategy | n/a | No follow-up; audit is exhaustive, not sampled |
| **12e** | Sensitivity analyses | **Yes, extensively** | §3.3 Table 2, §3.8 Table 9; SAP §3.2–§3.6. Nine sensitivity analyses, four of which damage the result |
| **13a** | Numbers at each stage | Yes | §3.1 Table 1; §3.3; §3.8 Table 8 |
| **13b** | Reasons for non-participation | n/a | No participants |
| **13c** | Flow diagram | Not included | The pipeline is four steps and fully described in §2; a diagram would add nothing. Available on request |
| **14a** | Descriptive data | Yes | §3.1 Table 1 |
| **14b** | Missing data per variable | Yes | §3.6, one probe |
| **14c** | Follow-up time | n/a | — |
| **15** | Outcome events / summary measures | Yes | §3.3 Tables 2 and 2b |
| **16a** | Unadjusted and adjusted estimates, with confounders | Yes | §3.3 — unadjusted Fisher's exact and block-stratified CMH, both codings |
| **16b** | Category boundaries for continuous variables | Yes | §2.4 and SAP §2.3 — the dichotomisation is the category boundary, and both are reported |
| **16c** | Absolute risk translation | n/a | Not a risk-estimation study |
| **17** | Other analyses: subgroups, interactions, sensitivity | Yes | §3.8; SAP §3.6 |
| **18** | Key results with reference to objectives | Yes | §3.3; §4.1 |
| **19** | Limitations, direction and magnitude of bias | **Yes, at length** | §5.1–§5.14, fourteen items, ordered by how much each should change a reader's confidence, plus explicit falsification criteria |
| **20** | Cautious overall interpretation | Yes | §4.1–§4.3; the clinical recommendation carries three stated qualifications |
| **21** | Generalisability | Yes | §5.11 — n = 1 document, one disease, one language, one model generation |
| **22** | Funding and role of funders | Yes | §7.1 — none |

---

## Items this design needs that STROBE does not cover

Declared here because no checklist asks for them and they matter more than several that
checklists do ask for.

| Item | Where |
|---|---|
| **The investigator authored the study stimulus** | §2.1 and §7.2, declared as a competing interest, not merely as provenance |
| **Dual-use assessment** | §7.3 — what was withheld, and the residual risk accepted |
| **Use of AI, including as experimental subjects** | §7.8 |
| **Circularity: verification and subjects share a model family** | §5.9 |
| **Contamination in agent-based evaluation** | §2.6, §4.5 — a discarded arm, an abandoned arm, and the recommendation that follows |
| **Pre-registrations with verifiable timestamps** | §7.6; supplementary S3 |
| **Corrections made during preparation** | §7.10 — eleven, logged publicly with the original wording preserved |
| **Source-document availability** | §7.9 — retained not published, SHA-256 given, supplied to editors and reviewers on request |

---

## Data and code availability

Complete. The claim inventory, the canonical verdict file, both blinded raters' output, both
independent re-extractions (495 claims), all five analysis scripts, four pre-registrations
with commit timestamps, and the public corrections log are all deposited. The full analysis
output is reproduced verbatim in supplementary material S4.

The one item not public is the source document itself, for the dual-use reason in §7.3. It
is available to editors and reviewers on request, and its SHA-256 is published so any copy
supplied can be verified as the one audited.
