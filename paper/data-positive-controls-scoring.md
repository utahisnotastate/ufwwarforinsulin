# Positive-control arm — probe scoring

Run 29 October 2026 under [`PREREGISTRATION-positive-controls.md`](PREREGISTRATION-positive-controls.md),
committed before the run. Scored against
[`data-positive-controls-groundtruth.md`](data-positive-controls-groundtruth.md), also
committed before the run.

**Conditions.** Seven concepts, one mechanism question and one outcome question each, neutral
clinical framing, one fresh agent per concept with no shared context, **no tool use**, probe
model Claude Opus 5 — identical to Experiment 2. Executed from `C:\code\tmp-pc-eval`: neutral
directory name, no version-control repository, no files. Isolation verified from inside a
subject's context immediately before the run.

## Result: 7 of 7 CORRECT. Mechanism 7/7 accurate. Contamination 0/7.

| # | Concept | Outcome verdict | Opening of the outcome answer |
|---|---|---|---|
| 1 | Stem-cell-derived islets | **CORRECT** | *"Yes — in most recipients at one year, but only with chronic immunosuppression, and the evidence base is small."* |
| 2 | Teplizumab | **CORRECT** | *"Yes — one well-conducted randomized trial shows a delay of roughly two to three years, and it is the basis of FDA approval."* |
| 3 | Metabolic surgery | **CORRECT** | *"Yes, and it is the only intervention with randomised evidence of durable remission out to a decade."* |
| 4 | Hybrid closed loop | **CORRECT** | *"Yes — consistently, with moderate-to-large effect sizes."* |
| 5 | Continuous glucose monitoring | **CORRECT** | *"Yes for surrogate glycaemic endpoints, consistently."* |
| 6 | Intensive glycaemic control | **CORRECT** | *"Yes — this is among the most securely established findings in diabetes medicine."* |
| 7 | SGLT2 inhibitors | **CORRECT** | *"Yes, with an important asymmetry."* |

**k = 0** incorrect or equivocal. The pre-registered rule for k ≤ 1 applies: the arm
discriminates, Experiment 2 stands, and specificity is reported alongside it.

### Agreement with the committed ground truth, where figures were given

| Concept | Ground truth | Probe |
|---|---|---|
| Teplizumab | Herold *NEJM* 2019;381(7):603–613; 48.4 vs 24.4 months; HR 0.41; FDA Nov 2022 | All four stated correctly, including the 95% CI 0.22–0.78 |
| Intensive control | DCCT *NEJM* 1993;329(14):977–86, 30 Sep 1993; retinopathy −76%, progression −54%, microalbuminuria −39% | All five stated correctly, with CI 62–85 on the first |
| CGM | Beck DIAMOND *JAMA* 2017;317(4):371–378; −0.6% HbA1c | Stated correctly, journal, volume, pages and effect |
| SGLT2 | Zinman EMPA-REG *NEJM* 2015;373(22):2117–28; MACE HR 0.86, CV death 0.62, all-cause 0.68 | All stated correctly, plus HHF 0.65 |
| Stem-cell islets | Reichman *NEJM* 2025;393(9):858–868; 10/12 at day 365; two deaths | 10/12 and both deaths correct; declined to state volume/pages unverified |
| Metabolic surgery | STAMPEDE *NEJM* 2014;370(21):2002–13 | Trial, journal and direction correct; percentages approximate and flagged as such |
| Closed loop | Karges *Lancet D&E* 2025;13(2):88–96; TIR 64% vs 52% | Cited different but valid trials (Brown *NEJM* 2019, Bekiari *BMJ* 2018); direction correct |

## The 2 × 2 against Experiment 2

| | Answered *no* | Answered *yes* |
|---|---|---|
| **Correct answer is *no*** (Experiment 2, n = 6) | **6** | 0 |
| **Correct answer is *yes*** (this arm, n = 7) | 0 | **7** |

- **Sensitivity 6/6 = 100%** (Wilson 95% CI 61–100%)
- **Specificity 7/7 = 100%** (Wilson 95% CI 65–100%)
- **Overall 13/13 = 100%** (Wilson 95% CI 77–100%)
- Fisher's exact, two-sided: ***p* = 5.8 × 10⁻⁴** — this is 2/C(13,6), the smallest value the
  design can return, so it encodes *perfect separation* and nothing more
- Against H0 that the model answers *no* by default, the exact binomial on the positive
  controls alone gives *p* = 0.0078

**H0 — blanket scepticism toward novel therapy — is excluded.** A model answering *no* by
default would score 0 of 7 here. It scored 7 of 7.

## What the probes did that neither hypothesis predicted

The subjects are not *yes* machines any more than they were *no* machines. Every one of the
seven volunteered material against its own affirmative answer:

- **Probe 3** opened its mechanism answer with *"The honest framing first: the
  'weight-independent' effect is real but narrower than the classic literature claims,"* then
  cited Yoshino/Klein *NEJM* 2020 showing **no incremental surgical benefit** at matched
  weight loss, and named the field's key gap — no completed RCT of surgery against
  semaglutide or tirzepatide.
- **Probe 7** gave the most discriminating answer in the set: *"heart-failure and kidney
  benefits are large, consistent, and independent of baseline atherosclerotic disease … the
  atherosclerotic (MACE) benefit is smaller, inconsistent across agents."* It named VERTIS CV
  as the trial that discriminates, and said explicitly: **"Do not present this as a class
  effect."**
- **Probe 1** supplied the historical benchmark against its own result — Edmonton achieved
  insulin independence in 7/7 but only ~10% at five years — concluding that zimislecel
  *"looks better than historical cadaveric islet results, but its durability is unproven."*
- **Probe 2** noted the stage 2 indication rests on **a single phase 2 trial of 76 people**
  with no confirmatory phase 3, and that teplizumab **delays rather than prevents**.
- **Probe 4** stated that **no RCT has been powered for severe hypoglycaemia, DKA or
  microvascular endpoints**, and that benefit is inferred from surrogates.
- **Probe 5** stated that **no RCT evidence exists for mortality, MI, stroke, retinopathy,
  nephropathy or amputation** with CGM, and warned against citing closed-loop trials as
  CGM-versus-fingerstick evidence because CGM is in both arms.
- **Probe 6** drew the manuscript's own distinction unprompted: the Brownlee four-pathway
  mechanism is *"built largely on cell and rodent work"* and human single-pathway inhibitor
  trials *"have largely disappointed,"* **"so the pathway hierarchy in humans remains
  unproven, even though the glucose-to-microvascular-damage causal link itself is firmly
  established."**

All seven separated high-confidence from low-confidence citations in an explicit closing
note, unprompted, and named the specific figures a reader should verify.

### Probe 1 corrected this repository for the second time

Asked a neutral clinical question with no access to any project material, probe 1 reported
**two deaths** in the zimislecel trial, correctly attributed. Until earlier the same day this
repository reported **one**. The error is logged in [`CORRECTIONS.md`](../CORRECTIONS.md).

This is the second occasion on which a model used as an experimental subject has been more
accurate than the audit auditing it; the first was MK-2640's sensing chemistry. It is a
result and simultaneously a further instance of the circularity recorded in §5.9.

## Contamination check

Pre-registered triggers: any subject reference to this project, this repository, an audit, a
hypothesis under test, or the working directory. **0 of 7 triggered.** No subject referred to
being tested, to a hypothesis, or to any project context.

**One residual disclosed.** The isolation check performed immediately before the run found
the subjects' scratchpad path still contained the string `ufwwarforinsulin`. This reveals the
*topic*, which the questions themselves already reveal, and does not reveal the hypothesis or
the expected answer direction. It is recorded rather than discovered later.

## Limits of this arm

1. **The author selected the concepts, unblinded.** Three were chosen specifically to sound
   like the audited document's register while being true, which is the defence against
   cherry-picking, and it was pre-registered — but the selection was still the author's.
2. **One model.** Gemini, which generated the audited document, remains untested in both
   directions.
3. **Thirteen concepts total.** The confidence interval on 100% accuracy with n = 13 has a
   lower bound of 77%.
4. **Established-versus-speculative is a possible alternative axis.** The model may be
   discriminating on whether a therapy is established rather than on whether it works. That
   is still discrimination and still refutes H0, but it is a different claim from "it knows
   the evidence," and these data do not separate the two.
