# Pre-registration — de-prefixed re-classification

**Written and committed before any rater was run.** Commit timestamp is the registration.

---

## Why this experiment exists

Two defects in the original blinded classification, both identified by external review.

**M3 — the blinding leaked.** The file named `data-claims-unlabelled.txt` retained
block-prefixed identifiers (`A1`, `C1`, `X7`). The source document is sectioned, so block
membership predicts stratum almost perfectly: **every one of the 13 block-C claims was rated
SPECIFICATION and every one of the 17 block-X claims was rated PHYSICS.** Thirty of 61
classifications — 49% — were derivable from the prefix without reading the claim, and one
rubric category shares a name with the block it tracks. The reported κ = 0.977 is inflated by
an unknown amount.

**M4 — κ was not inter-rater reliability.** Both "raters" were context-free sessions of one
model. Two samples of one model share weights and therefore share systematic errors, so the
statistic measured stability under resampling. Any mistake the model makes consistently was
invisible to it by construction.

## What this experiment can and cannot fix

**Can fix M3 entirely.** Identifiers are stripped, claims shuffled with a published seed, and
renumbered `01`–`61`. The shuffle map is deposited
([`data-claims-deprefixed-map.txt`](data-claims-deprefixed-map.txt)) so the whole thing is
reproducible.

**Cannot fix M4 properly.** The reviewer asked for clinically trained human raters. None is
available to this project, and no amount of model-switching substitutes for one. What is
available is a **second model** of different size and training, which gives agreement that is
not pure resampling. That is a partial answer and will be reported as a partial answer. **The
taxonomy remains unvalidated by any human.**

## Design

Three raters, independent, each in a fresh context with no shared history:

| Rater | Model | Purpose |
|---|---|---|
| **C** | Claude Opus 5 | Clean replication of the original condition |
| **D** | Claude Opus 5, separate session | κ(C,D) = resampling stability **without the label leak** |
| **E** | Claude Sonnet 5 | κ(C,E), κ(D,E) = agreement across a different model |

Each receives `claims.txt` — the de-prefixed shuffled claims — and the rubric from §2.3 of
the manuscript, verbatim and unchanged:

| Stratum | Decision rule |
|---|---|
| **Mechanism** | How a biological system behaves. No claim about a clinical result in humans |
| **Therapeutic outcome** | An intervention produces clinical benefit, or an established therapy is harmful or inferior, **in humans** |
| **Specification** | A sequence, concentration, process parameter, yield, duration or cost |
| **Physical theory** | A physical law, constant or mechanism outside biology |

Raters are instructed not to search, not to read any other file, and not to consider whether
any claim is true. They receive **no verdicts, no inventory, no block structure, no claim
counts per stratum, and no statement of the hypothesis.**

**Isolation.** Executed from `C:\code\tmp-rt-eval`: neutral directory, no version-control
repository, nothing but `claims.txt`. Isolation will be verified from inside a rater's context
immediately before the run. **This check has failed twice in this project** — on both previous
arms the requested directory change had not taken effect — so it is treated as a real gate and
not a formality.

## Pre-specified measures

1. **κ(C,D)** — the headline. Same model, two sessions, no label leak. Compared against the
   originally reported 0.977 and against the 0.928 computed by excluding the block-determined
   claims.
2. **κ(C,E) and κ(D,E)** — cross-model agreement.
3. **Stratum migration** — how many of the 61 claims land in a different stratum than in the
   original classification, and whether the migration is concentrated in blocks C and X, which
   is where the leak did its work.
4. **Re-run of the central comparison** on the new consensus assignments, if any claim moves
   between the mechanism and outcome strata.

## Decision rule, fixed in advance

| Condition | Conclusion |
|---|---|
| κ(C,D) ≥ 0.90 **and** stratum migration < 10% of claims | The original classification was sound and the leak inflated κ without changing assignments. Report the de-prefixed κ as primary |
| κ(C,D) ≥ 0.90 **but** migration ≥ 10% | Agreement is fine, the assignments were not. **Re-run the contingency analysis on the new assignments and report it as primary** |
| κ(C,D) < 0.90 | The original 0.977 was substantially an artifact of the prefix. Report the lower figure as primary wherever κ appears |
| **Any pairwise κ < 0.70** | **The four-stratum taxonomy is not a reliable instrument.** This is the reviewer's own threshold (§5.14 criterion 2), and meeting it requires the stratification to be reported as a proposal rather than a measurement |
| Mechanism/outcome membership changes | Re-run the ordinal test; report whatever it returns |

## Anti-gaming commitments

1. **One run per rater. No re-running a rater whose output is inconvenient.**
2. **The rubric will not be edited after seeing any output.** It is copied verbatim from the
   published Methods.
3. **The shuffle seed is published in advance** (`random.Random(20261029)`), so the ordering
   cannot be selected after the fact.
4. **The result is reported whichever way it falls**, including the branch that demotes the
   taxonomy to a proposal and the branch that forces the central table to be recomputed.
5. If a rater's output is unusable for a reason unrelated to the hypothesis, that is reported
   as missing data rather than silently replaced.

## What remains open regardless of the outcome

No human has validated this taxonomy. Every rater in this study, in every arm, has been a
language model, and the verification behind every verdict was AI-assisted. A good result here
narrows the objection to the *blinding*; it does not touch the objection to the *species of
rater*. That limitation stands in §5.3 whatever this experiment returns.


---

## Addendum, 2026-10-29 — not executed. Isolation could not be achieved.

**This arm was not run.** Recorded here rather than quietly dropped, because a pre-registration
that only ever reports completed arms is not a pre-registration.

The isolation check specified above was run and **failed for the third consecutive time in
this project.** The requested working-directory change had not taken effect, and the raters
would have inherited:

- primary working directory `C:\code\ufwwarforinsulin`
- a version-control log whose most recent entries include
  **"Independent re-extraction: counts do not reproduce, dissociation does."** and
  **"Pre-register the de-prefixed re-classification before running it"**

### Why this leak is disqualifying for *this* arm specifically

Earlier arms were run despite a comparable leak, on the reasoning that its plausible bias ran
against the hypothesis. That reasoning does not hold here.

The word **"dissociation"** appears in the log alongside a rubric, supplied to the rater, that
contains MECHANISM and OUTCOME as adjacent categories. A rater could infer the axis under
test. It would not need the verdicts to bias the result: assigning grandiose, cure-shaped
claims to OUTCOME correlates with assigning false claims to OUTCOME, and that is precisely the
bias §3.2 documents in this project's own unblinded pass.

**Contaminating the one experiment designed to measure contamination would be worse than not
running it.** The arm is therefore not run, and no result from it is reported.

### What stands in its place

The leak-free estimate already computed and reported in the manuscript: **κ = 0.928 on the 31
claims whose block prefix does not determine the answer** (30 of 61 were prefix-determined and
are excluded). This is a measurement of agreement on exactly the claims where the leak could
not have operated, and it is the figure the manuscript treats as honest. It is not equivalent
to a full de-prefixed re-run, because it cannot detect whether claims would *migrate* between
strata once the prefix is removed — that question remains open.

The blinded input is built and deposited regardless, so that anyone with a clean environment
can run this arm as specified: the de-prefixed shuffled claims, the published seed
`random.Random(20261029)`, and the shuffle map in
[`data-claims-deprefixed-map.txt`](data-claims-deprefixed-map.txt).

### The methodological point, which is the part worth keeping

Three arms of this study attempted the same isolation procedure. **It silently failed every
time**, and was caught every time only because a throwaway subject was asked what it could see
before the real subjects ran. On the first two occasions the leak was judged tolerable; on this
one it was not, and the arm was abandoned.

This strengthens the recommendation in §4.5 past where it stood. It is not enough to execute
from a clean environment, and not enough to verify isolation once. **In an agent-based
evaluation the researcher's configuration and the subject's actual context can diverge
repeatedly and without warning, and the only reliable guard is an instrumented check
immediately before every single run, with a pre-committed willingness to abandon the arm.**
This project abandoned one.
