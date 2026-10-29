# Corrections

This repository's claim is that its verdicts are checkable. That is worth nothing unless
errors found in it are logged publicly, with what was wrong, how it was caught, and what
changed.

Newest first.

---

## 2026-10-29 · Three errors in the manuscript's Eli Lilly paragraph

**Severity:** high — one factual, one a pharmacology error in a medical manuscript, one an
inference the record contradicts.
**Found by:** verifying the claim against primary SEC filings before submission, after an
external reviewer questioned it on accounting grounds.

| Error | Correction |
|---|---|
| *"under 6% of revenue"* | **Wrong.** $4,006M / $65,179M = **6.15%** — over six. And read as describing insulin rather than the line item, the FY2025 insulin figure **is not disclosed in the filing** and cannot be asserted at all |
| *"two GLP-1 products"* | Mounjaro and Zepbound are two brands of **one molecule, tirzepatide**, a **dual GIP/GLP-1 receptor agonist**. Lilly's own 10-K describes it that way. A pharmacology error in a medical manuscript |
| *"has stopped counting it"* | An inference the filing contradicts. Lilly reduced product-level detail **across the whole portfolio** in FY2025 — Cyramza, Olumiant, Emgality, Zyprexa and Baqsimi went too, and the management discussion fell from 18 product lines to 4. Insulin was not singled out |

**The reviewer's own accounting argument was also wrong**, in the opposite direction. ASC
280-10-50-40 requires product-level revenue disclosure with **no quantitative threshold**; the
10% figures govern reportable segments and major customers, not products; Regulation S-K
carries no numeric threshold since 2020; and ASU 2023-07 *increased* the obligation. In the
same year **Merck disclosed 30 products, the smallest at 0.26% of revenue.** The aggregation
is not routine.

**Net effect on the argument: stronger.** Insulin's disappearance is a by-product of a
disclosure architecture reorganised around two growth assets, which is more defensible than
concealment and makes the same point.

## 2026-10-29 · The polishing plan misstated the BMJ Analysis word limit

**Severity:** moderate — it would have produced an unnecessarily severe compression.

An earlier version of [`paper/POLISHING-PLAN.md`](paper/POLISHING-PLAN.md) stated the limit as
**1,500–1,800 words** and asserted this was "worse than the review says." The live BMJ page
specifies **2,000 words**.

The error came from relying on 2007-dated guidance retrieved via PMC after BMJ's current
author page refused automated retrieval twice. **The reviewer's figure was closer than mine,
and the plan contradicted them on the basis of stale data.**

Also missed in that version, and more consequential than the word count: BMJ states the
Analysis section does not consider *"manuscripts containing primary research data."* This
manuscript reports four experiments. See POLISHING-PLAN Part A2.

---

## 2026-10-29 · Understated the contamination in the persona arm: "at least two," actually four

**Severity:** minor factually, notable in kind — it is an error in the direction that
flattered the work.
**Found by:** re-auditing the probe transcripts before acting on the result.

[`paper/RESULTS.md`](paper/RESULTS.md) reported that "at least two of the six" persona-arm
subjects inferred the experimental hypothesis. **Four did.** The original count caught the two
that quoted the working-directory path and missed two that referenced the paper proposal and
`CORRECTIONS.md` without naming the path.

"At least two" was technically true and substantively misleading. The corrected figure makes
the arm less salvageable, not more: the uncontaminated subset is **n = 2**, which cannot
support a claim about model behaviour.

Corrected in place in `paper/RESULTS.md` and `paper/PROPOSAL.md`, with the original figure
quoted rather than overwritten.

---

## 2026-10-29 · MK-2640 was described as a phenylboronic-acid insulin. It is not.

**Severity:** moderate — a mechanism misattribution, not a safety error.
**Found by:** a replication probe run for [`paper/RESULTS.md`](paper/RESULTS.md), which
answered a neutral question about glucose-responsive insulins more precisely than this
repository had.

### What was wrong

[`INTEGRITY_AUDIT.md`](INTEGRITY_AUDIT.md) discussed Merck's MK-2640 under the heading for
claims D4/D5, which concern **phenylboronic acid (PBA)** conjugation at the B29 lysine. That
placement implied MK-2640 was the clinical test of PBA chemistry.

It was not. **MK-2640 is a mannose-functionalised insulin** cleared via the **mannose receptor
(MRC1 / CD206)**. Rising glucose was intended to compete it off that receptor, slowing
clearance and raising exposure. Entirely different sensing chemistry.

### Why it mattered

The conflation made the audit's conclusion *weaker* than the evidence supports. The corrected
position:

> **No phenylboronic-acid-based glucose-responsive insulin has entered human testing at all.**
> Ins-PBA-F, boronate hydrogels and boronate micelles are all preclinical. The chemistry the
> source document specifies has never been given to a person — and the one GRI that did reach
> humans used different chemistry and still failed.

### Also added

**Eli Lilly acquired Protomer Technologies in 2021**, a deal worth up to approximately
$1 billion, to enter the glucose-sensing insulin field behind Novo Nordisk. Protomer was
preclinical at acquisition; no human glucose-responsiveness data have been published. Absent
from earlier versions of the bibliography.

### Files changed

`INTEGRITY_AUDIT.md` · `README.md` · `disclosure2.md` · `docs/endocrinology/README.md` ·
`references/bibliography.md`

### How it was caught, which is the interesting part

The error surfaced during an experiment designed to test something else. Six fresh model
instances were asked neutral clinical questions about the therapeutic concepts in the source
document, to see whether they would reproduce its errors. They did not — and one of them
**corrected this repository in passing**, noting both the MRC1 mechanism and that no PBA
construct has reached humans.

A verification project was corrected by the thing it was verifying. That is the system
working, and it is logged here rather than quietly patched.

---

## Corrections policy

Labels move with evidence, in either direction, including from ❌ back to ✅.

- Every correction is logged here with its date, what was wrong, and what changed.
- Corrections are **annotated in place**, not silently overwritten. The audit carries an
  inline note at the point of the error.
- **Safety-relevant corrections are logged even if they make the repository look worse.**
  Especially then.
- Found something? Open an issue or a pull request. A peer-reviewed source that moves a
  verdict is the most useful contribution anyone can make here.

### Known open items

Not errors, but gaps stated rather than hidden:

- **Eight unresolved citations** listed at the end of
  [`references/bibliography.md`](references/bibliography.md)
- **Two evidence gaps:** a national US insulin-rationing prevalence figure (Fang & Selvin,
  *JAMA* 2023, PMC10061307) and current HCUP DKA cost and volume data. The repository
  currently relies on a single-centre rationing study (n=199) and 2014 DKA charge data, and
  labels both as such
- **The paper's central confound:** model identity is confounded with prompting regime in
  [`paper/RESULTS.md`](paper/RESULTS.md). Stated in the abstract, not resolved
