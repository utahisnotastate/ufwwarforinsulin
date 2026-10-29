# Submission readiness

Last checked 29 October 2026, against the current `MANUSCRIPT.md`.

## Mechanically verified

| Check | State |
|---|---|
| Cross-references (`§n.n`) all resolve to a real section | ✅ 0 broken |
| Tables numbered sequentially, none missing or duplicated | ✅ 1–10 plus 2b |
| In-text citations all appear in the reference list | ✅ 14/14 |
| Reference list entries all cited in text | ✅ 14/14, in order of appearance |
| Author lists complete per Vancouver (all ≤6, else first 6 + *et al*) | ✅ verified against PubMed |
| Every PMID confirmed against PubMed | ✅ |
| Every statistic reproduced by a deposited script | ✅ 4 scripts |
| Main-text word count (BMJ convention: excl. abstract, references, tables, boxes) | **9,282** |
| Word (.docx) for submission | [manuscript.docx](manuscript.docx) — 49pp, double-spaced, continuous line numbers; schema-validated |
| PDF for reading / preprint | [manuscript.pdf](manuscript.pdf) — 27pp, typeset |

## Mandatory declarations present

Funding · competing interests (including authorship of the stimulus) · **dual-use
assessment** · contributorship and guarantor · ethics · patient and public involvement ·
sex/gender disaggregation · use of AI · data availability · corrections during preparation ·
transparency declaration · provenance and peer review · licence.

## Deposited materials

| | |
|---|---|
| Claim inventory, 61 claims with stable IDs | `archive/source-claim-inventory.md` |
| **Canonical verdict file** — the authoritative list | `data-verdicts-canonical.md` |
| Both blinded raters' classifications | `data-rater-A.txt`, `data-rater-B.txt` |
| **Two independent re-extractions, 495 claims** | `data-extraction-1.md`, `data-extraction-2.md` |
| De-prefixed shuffled input + published shuffle seed and map | `data-claims-deprefixed-map.txt` |
| Positive-control ground truth, fixed before the run | `data-positive-controls-groundtruth.md` |
| Analysis scripts | `analysis-kappa.py`, `analysis-contingency.py`, `analysis-sensitivity.py`, `analysis-positive-controls.py`, `analysis-reextraction.py` |
| Pre-registrations, with commit timestamps | persona re-run · positive controls · re-extraction · re-classification |
| Public corrections log, 11 entries | `../CORRECTIONS.md` |
| Source document | **retained, not published**; SHA-256 given, supplied to editors and reviewers on request |

## Venue

**BMJ Analysis is ruled out** — 9,282 words of main text against a 2,000 limit, and BMJ states Analysis
does not consider manuscripts containing primary research data. This reports five experiments.

Target **BMJ Research** or **JMIR / npj Digital Medicine**. Letters for all three are drafted
in `SUBMISSION-LETTERS.md`; send letter A first if you want a steer, otherwise B or C.

## Known open items, all stated in the paper

These are not blockers. They are disclosed, and a reviewer will see them because the paper
points at them.

1. **No human has validated the taxonomy.** Every rater in every arm was a language model. The
   de-prefixed re-classification was pre-registered and **abandoned** when its isolation check
   failed; the input is deposited for anyone with a clean environment.
2. **The claim count does not reproduce** — 258 and 237 against our 61. Every percentage is
   conditional on our segmentation. The ordinal result survived every decomposition tried.
3. **Gemini under neutral prompting is untested**, so model identity stays confounded with
   prompting regime.
4. **The strict dichotomous coding is not significant** (*p* = 0.068). Reported in the
   abstract and led in Limitations; the ordinal test is primary and robust.
5. **n = 1 source document, authored by the investigator.** Declared as a competing interest.
6. No patient or clinician was involved, which §7.6 states as a limitation rather than a
   justification.

## Before you hit send

- [ ] Decide the title. `"Other Cardiometabolic Health"` suits a narrative venue; for an
      empirical one the subtitle should lead.
- [ ] Confirm you are content with authorship of the source document being declared as a
      competing interest in the abstract, §2.1 and §7.2. It is the right call and it is
      prominent.
- [ ] Post to medRxiv at submission, as the cover letters state.
- [ ] Have the unredacted source document to hand; editors may ask.
