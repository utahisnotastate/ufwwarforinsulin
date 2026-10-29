# Statistical analysis plan

**"Other Cardiometabolic Health" — Mechanism without outcome: a claim-level audit of
AI-generated insulin misinformation in a disease with a 48-hour error budget**

Utah Hans · Independent researcher

---

## An honest preamble about what was pre-specified

This study did not begin as a study. It began as a verification exercise on a single
AI-generated document, and the hypothesis emerged from the completed verdict table rather
than preceding it. **The core analysis is therefore not pre-registered, and this plan does
not claim otherwise.**

What *was* pre-registered, each committed to a public repository before the corresponding
work ran, is set out in §4. Every analysis in the manuscript is labelled below as
**pre-specified**, **post-hoc**, or **added after peer review**, and the manuscript carries
the same labels.

A reader who treats only the pre-registered items as confirmatory, and everything else as
exploratory, will be reading this paper correctly.

---

## 1. Design and unit of analysis

**Design.** Exhaustive claim-level audit of one AI-generated document, with blinded
classification into epistemic strata, followed by four experiments using language models as
subjects.

**Unit of analysis.** The claim. Two audit entries each cover two claim identifiers under one
shared verdict (B4/B5, D4/D5); a shared verdict is counted once for each claim it covers, so
61 claims carry 59 distinct verdict determinations.

**No sample size calculation was performed, and none was possible.** The denominator is the
number of substantive claims in one document. The study is powered by whatever that number
turned out to be.

---

## 2. Outcome definitions

### 2.1 Verdict (the dependent variable)

Each claim was assigned exactly one of five verdicts against primary literature:

| Verdict | Definition |
|---|---|
| Verified | Supported as stated |
| Partly true | Real science, overstated, misattributed or out of date |
| Open | Plausible, under genuine investigation |
| Not true | Contradicted by evidence, or asserting what no study supports |
| No scientific basis | No mechanism; not testable as framed |

**Verdict assignment was not blinded**, and was performed by the author. This is the study's
principal methodological weakness and is stated as such in the manuscript.

### 2.2 Stratum (the independent variable)

Four strata, applied by two raters blinded to all verdicts against a rubric fixed before they
saw the claims: **mechanism**, **therapeutic outcome**, **specification**, **physical
theory**. The rubric is reproduced in the supplementary material, S2.1.

### 2.3 "Supported" — the definition that was not stated, and should have been

Where claims are dichotomised, "supported" admits two readings:

- **Lenient** — verified *or* partly true.
- **Strict** — verified only.

**The original analysis used the lenient coding, did not state it, and did not test it.** An
external reviewer identified this before submission. It is an undisclosed analytic degree of
freedom and it mattered: under the strict coding the central comparison is not statistically
significant. Both codings are now reported everywhere, and the primary analysis avoids the
choice entirely.

---

## 3. Analyses

### 3.1 Primary analysis — ordinal, cut-free · *added after peer review*

Verdicts form an ordered scale: verified (2) > partly true (1) > not true or no scientific
basis (0). The mechanism and outcome strata are compared by **exact permutation test** on
that scale, enumerating all 2,220,075 assignments.

**Rationale.** The dichotomous result is sensitive to where the cut is placed, and choosing a
cut post hoc is precisely the degree of freedom an unblinded analyst should not exercise. An
ordinal test uses all the information and chooses no cut.

Open claims are excluded from all contingency analyses.

### 3.2 Secondary — dichotomous contingency · *post-hoc, reported under both codings*

Fisher's exact test, two-sided, on the mechanism-versus-outcome 2 × 2, reported separately
under the lenient and strict definitions, with:

- **Wilson score intervals** on each proportion
- the **one-sided 95% lower bound of the conditional odds ratio**, because the point estimate
  is infinite wherever a cell is zero
- **Bonferroni adjustment** across the six pairwise comparisons possible among four strata

### 3.3 Clustering sensitivity · *post-hoc*

Outcome claims cluster within a smaller number of underlying development programmes, so a
sensitivity analysis aggregates to programme level (7 versus 7). **This is a different and
much smaller table, not a variance correction**, and is labelled as such. At that dimension
the smallest achievable *p* is 2/C(14,7), so the figure encodes perfect separation and
nothing more.

### 3.4 Confounding by position in the source document · *added after peer review*

Block membership predicts stratum almost perfectly, so "accuracy falls where claims assert
results" is hard to separate from "the document is accurate where it recites and invents
where it argues." A **Cochran–Mantel–Haenszel test stratified by document block** addresses
this, reported under both codings.

### 3.5 Sub-claim aggregation · *rule reconstructed retrospectively*

Several extracted claims bundle more than one assertion. The rule applied is
**worst-sub-claim-governs**: a compound claim is scored on its weakest component, because a
reader acting on the claim acts on all of it.

**This rule was not stated in the original analysis and was reconstructed afterwards.** One
claim (B6) was found to violate it and is recoded from partly true to not true; that change
weakens the result, from 15/19 to 14/19 mechanism claims supported. Every figure is reported
both as originally coded and with B6 corrected.

### 3.6 Decomposition sensitivity · *added after peer review*

The compound claim A3 is decomposed as two independent blinded extractors decomposed it, and
the ordinal test re-run under four variants including two built to break the result: a
maximally hostile assignment of all five components to the outcome stratum, and the
reviewer's own proposed split.

### 3.7 Agreement

Cohen's κ between the two blinded raters, reported twice:

- across all 61 claims, and
- **restricted to the 31 claims whose identifier prefix does not predict the answer** —
  30 of 61 classifications were derivable from the block prefix without reading the claim, so
  **the restricted figure is the one to use.**

Both measure stability of one model under resampling, not inter-rater reliability between
independent judges. Neither has been validated by a human rater.

### 3.8 Experimental arms

| Arm | Measure | Status |
|---|---|---|
| Neutral re-query | Proportion of outcome questions answered correctly | Exploratory; hypothesis falsified |
| Persona re-query | Persona adoption; outcome accuracy | **Pre-registered**; manipulation never delivered (0/6), so uninformative |
| Positive controls | Specificity, with Fisher's exact against the negative probes | **Pre-registered** including the decision rule |
| Re-extraction | Claim count, boundary concordance, ordinal test on the decomposition | **Pre-registered** including the decision rule |
| De-prefixed re-classification | κ without the label leak | **Pre-registered and NOT RUN** — isolation could not be achieved |

---

## 4. What was pre-registered, and when

Each was committed to the public repository before the corresponding work ran, so the
timestamp is in version control and cannot be revised afterwards. Full texts are in
supplementary material S3.

| Arm | Pre-registration | Committed |
|---|---|---|
| Persona re-run | `PREREGISTRATION-persona-rerun.md` | 2026-10-28T23:53:27−04:00 |
| Positive controls | `PREREGISTRATION-positive-controls.md` | 2026-10-29T01:10:39−04:00 |
| Re-extraction | `PREREGISTRATION-reextraction.md` | 2026-10-29T01:38:38−04:00 |
| Re-classification | `PREREGISTRATION-reclassification.md` | 2026-10-29T07:25:20−04:00 |

Each carries a decision rule fixed in advance, including the branch that would have required
withdrawing a central claim, and anti-gaming commitments: one run per arm, no re-running an
arm whose output is inconvenient, no changing a definition after seeing output, and the
result reported whichever way it fell.

**One arm was abandoned** after its pre-registered isolation check failed for the third time
in this study. The abandonment is published rather than omitted.

---

## 5. Deviations from plan

Reported in full because they are the parts a reader should weigh most.

1. **The corpus-bias hypothesis was falsified by its own first test.** It was the authors'
   proposed explanation for the dissociation. It is reported as falsified, not retained.
2. **Blinding the classification weakened the result**, from 93%/0% to 79%/0%. The unblinded
   pass had over-assigned the outcome category specifically to claims already scored false.
3. **One experimental arm was discarded for contamination** after four of six subjects
   inferred the hypothesis from passive environment context.
4. **One arm was pre-registered and never run** (§4).
5. **All sensitivity analyses in §3.1, §3.4 and §3.6 were added after external peer review**,
   not pre-specified. The reviewer's central objection — that the headline depended on an
   undisclosed dichotomisation — was correct, and the re-analysis is in the paper.

---

## 6. Software and reproducibility

All analyses are in Python 3.11 using only the standard library; no statistical package is
required and there is nothing to install.

| Script | Produces |
|---|---|
| `analysis-kappa.py` | Agreement between raters |
| `analysis-contingency.py` | The central 2 × 2 and Fisher's exact test |
| `analysis-sensitivity.py` | Dichotomisation sensitivity, Wilson intervals, odds-ratio bounds, CMH, Bonferroni, the ordinal permutation test |
| `analysis-positive-controls.py` | Sensitivity, specificity, exact binomial |
| `analysis-reextraction.py` | Ordinal test under every decomposition, and the extraction-instability measure |

Every statistic in the manuscript is produced by one of these five, and their complete
console output is reproduced verbatim in supplementary material S4.

---

## 7. Missing data

**One probe of seven** in the neutral re-query arm terminated on an automated safety
classifier and is reported as missing data. It was deliberately **not rephrased to evade the
filter**: working around a safety classifier to complete a dataset would be indefensible in a
paper about AI safety, and n = 6 honestly obtained is worth more than n = 7 obtained that way.

Automated safety filtering is itself a non-random source of missingness in this kind of
research, and is noted as a limitation.
