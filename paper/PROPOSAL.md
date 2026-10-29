# Paper proposal — v3

**Status:** proposal plus two completed experiments. Not submitted.

**Changes in v3:** the two gating objections from review — unblinded classification and
n = 1 — were addressed by running the experiments rather than promising them. Full data in
**[RESULTS.md](RESULTS.md)**. Two consequences:

1. **The core observation survived blinding, attenuated.** κ = 0.977 between independent
   blinded raters, but their classification differs materially from the unblinded one. The
   contingency table weakens from 93% vs 0% (p = 7.5 × 10⁻⁷) to **79% vs 0%
   (p = 2.2 × 10⁻⁴)**. The outcome column stays empty.
2. **The explanation was falsified by its own first test.** v2 predicted the dissociation
   would persist under neutral prompting because it comes from corpus publication bias. It
   did not persist in any of six probes. That hypothesis is dead and the paper is better for
   it.

---

## The title

> # "Other Cardiometabolic Health"
> ## Mechanism without outcome: a claim-level audit of AI-generated insulin misinformation in a disease with a 48-hour error budget

*"Other cardiometabolic health"* is the line item in **Eli Lilly's FY2025 Form 10-K into which
insulin was collapsed.** Humalog, Humulin and Basaglar are no longer reported separately.
Mounjaro and Zepbound are 56% of revenue; the entire global insulin franchise sits under 6%,
inside a bucket beginning with the word *other*. The company that commercialised insulin in
1923 has stopped counting it.

It is a quotation from an SEC filing, not an accusation — and it is load-bearing, because the
paper argues that misinformation fills the space institutions vacate.

### Dual-track title strategy

Both reviewers independently recommended the same thing, so it is now the plan:

| Venue type | Title to submit |
|---|---|
| **Narrative / analysis** (*BMJ* Analysis, *Lancet* Comment) | **Keep the 10-K title.** These venues actively seek structural critique of institutional transparency, and the title *is* the argument |
| **Empirical digital health** (JMIR, *Lancet Digital Health*, *npj Digital Medicine*) | **Lead with the subtitle:** *"Mechanism Without Outcome: A Claim-Level Audit of AI-Generated Insulin Misinformation in Type 1 Diabetes."* Searchable, conventional, no editorial friction |
| **Clinician-facing** (*Diabetes Care*, *Diabetic Medicine*) | *"The Model Was Right About the Mechanism"* — foregrounds the diagnostic trap |

Have the subtitle ready as primary from the start. Switching under editorial pressure looks
like retreat; offering both at submission looks like judgement.

---

## Abstract

**Background.** Large language models generate medically-shaped text at negligible marginal
cost. Existing health-misinformation taxonomies score veracity, but do not distinguish claims
by the epistemic layer at which they fail, nor by how quickly acting on them causes harm.
Type 1 diabetes is an unusually sharp test case: insulin cessation produces ketoacidosis
within 12–48 hours, so the interval between believing a false claim and requiring emergency
care is measured in hours.

**Methods.** We performed an exhaustive claim-level audit of a long AI-generated document on
insulin therapy, produced by a commercial LLM under a speculative "retrieved future knowledge"
persona prompt. All 61 substantive claims were extracted, assigned stable identifiers, and
verified against primary literature by three independent cross-checked reviews. Each received
a veracity verdict and, where acting on it could cause injury, a time-to-harm estimate. Claims
were then stratified by epistemic type into four pre-specified categories: **biological
mechanism**, **therapeutic outcome in humans**, **technical specification**, and **physical
theory**.

**Findings.** Of 61 claims, 14 (23%) were verified, 14 (23%) partly true, 1 open, 16 (26%)
contradicted and 16 (26%) without scientific basis. Two independent raters, blinded to all
verdicts, classified every claim by epistemic type with **Cohen's κ = 0.977** (60/61
agreement). Accuracy was strongly stratified by type:

| Stratum | n | Supported |
|---|---|---|
| Biological mechanism | 21 | **15 / 19 (79%)**, 2 open |
| Therapeutic outcome in humans | 8 | **0 (0%)** |
| Technical specification — qualitative | 6 | 5 (83%) |
| Technical specification — quantitative | 9 | **0 (0%)** |
| Physical theory | 17 | **0 (0%)** |

Mechanism versus outcome: Fisher's exact two-sided **p = 2.2 × 10⁻⁴**. Two error classes were
detectable **without external reference**: an amino-acid sequence that was bovine while the
accompanying molecular formula was human, and a resonance frequency quoted to four
significant figures that does not reproduce from the equation supplied in the same paragraph.

**We then tested whether this pattern reflects training-corpus publication bias**, by
re-querying the seven underlying therapeutic concepts in a current frontier model using
neutral clinical prompts without any persona, from parametric knowledge only. **The
prediction failed. In six of six completed probes the model answered the outcome question
correctly**, naming the specific trial, its result and its date — the Cebix Phase 2b that
missed both primary endpoints, insulin peglispro halted in December 2015 for hepatic
steatosis, MK-2640 discontinued for insufficient glucose-dependent clearance. Four answers
opened with an explicit *"No."*

**Interpretation.** The dissociation is real in the audited document and does not arise from
absent knowledge. The same class of system surfaces the refuting trial in the first sentence
of a neutral answer. The failure therefore appears to lie in the **generation condition** —
a user-configured persona instructing retrieval of speculative future knowledge — rather than
in the training distribution. **This cannot be concluded from these data**: model identity is
fully confounded with prompting regime, since the audited document came from one model under
a persona and the probes from another under neutral prompting. The completing 2 × 2 is
specified and is the immediate next experiment.

The clinically actionable finding does not depend on resolving that confound. A patient
arriving with AI-generated material will often be **correct about the mechanism and wrong
about whether the treatment works** — and the refuting evidence is recoverable from the same
class of system in a single plainly-worded question.

**Funding.** None.

---

## What changed in v2

### 1. The 34 unaccounted claims — the best catch in review, and it improves the paper

A reviewer noted that 14 mechanism + 13 outcome = 27, leaving **34 of 61 claims
unaccounted for**, and warned this invites a cherry-picking charge. Correct, and it would
have been fatal at review.

The 34 are not a residual. They are **two further strata**, and both support the thesis:

| | Claims | Pattern |
|---|---|---|
| **Technical specification** (n=17) | C1–C13, D2, D4, D5, A2, B4, B5 | Qualitative descriptions mostly right; **every quantitative value wrong** |
| **Physical theory** (n=17) | X1–X17 | 15 of 17 with no scientific basis; the two exceptions are established mathematics with unsupported extrapolation |

### 2. The third dissociation, which v1 missed entirely

Splitting the specification stratum by whether a claim is qualitative or numerical produces a
second clean separation:

| Qualitative process claims | Verdict |
|---|---|
| Disulfide topology A6–A11, A7–B7, A20–B19 | ✅ |
| *Pichia* folds the precursor co-translationally | ✅ |
| Secretion eliminates lysis and chaotropic denaturation | ✅ |
| *E. coli* inclusion-body chemistry | ✅ |

| Quantitative values | Verdict | Error |
|---|---|---|
| A-chain sequence | ❌ | bovine, not human |
| ">92% pure after 0.22 µm filtration" | ❌ | a filter removes cells, not solutes |
| "Single gravity pass, >95% conversion" | ❌ | 6–200× too fast vs. published kinetics |
| "1.5 g/L from a desktop reactor" | 🟡 | conflates two different published figures |
| "<$0.008 per 1,000 IU vial" | ❌ | 86× below the raw API cost alone |
| "0.1 M zinc acetate" | ❌ ☠️ | 218–436× commercial; would precipitate the drug and injure tissue |

**Prose reproduced from the corpus is reliable. Numbers are not.** This is consistent with
known LLM numerical behaviour, but here it is quantified in a specification context where the
consequence is a wrong protein or a necrotising injection.

### 3. Clustered sensitivity analysis

Both reviewers flagged pseudoreplication: the 13 outcome claims draw on ~7 distinct
literatures, so claim-level Fisher's exact overstates significance. One reviewer supplied the
program-level alternative, **which I verified independently — it is arithmetically correct**:

```
                supported   unsupported
  mechanism         7            0
  outcome           0            7

  C(14,7) = 3432 ;  two-sided p = 2/3432 = 1/1716 = 5.83e-04
```

**Both will be reported, with the clustered figure as primary.** Following the second
reviewer's advice, the p-value is also demoted in the narrative: the raw split (13/14 versus
0/13) is persuasive on its own, and leaning on a very small p-value computed on non-independent
observations is an invitation.

### 4. Provenance — a correction to v1, stated openly

**v1's abstract said the document was "circulating in patient communities." I could not
substantiate that, and it should not have been written.** It is the single most serious
problem in v1 and exactly the kind of unsupported outcome-level assertion this paper is
about — which is either embarrassing or instructive, and probably both.

**The verifiable provenance:** the document was produced by a commercial LLM (Google Gemini)
operating under a user-configured persona prompt instructing it to retrieve medical knowledge
from future timelines. It was generated in a private session. No dissemination to patients was
observed, and none is claimed.

This must be stated plainly in Methods. Any claim about real-world circulation requires
evidence we do not have.

**And the honest framing is stronger than the false one.** A document someone found is an
anecdote: unreproducible, unknown provenance, n=1 forever. A document *generated under a
recorded prompt* is an **experimental artifact** — the generating procedure is known, the
prompt is available, and the result is **reproducible across models**.

That converts the reviewers' central objection into the paper's natural next experiment,
described below.

---

## Addressing the n = 1 objection

Both reviewers identified this as the gating issue, and both proposed the same remedy. With
honest provenance it becomes straightforward.

**The replication study.** Take the seven underlying therapeutic concepts — C-peptide
replacement, glucose-responsive insulin, hepato-preferential delivery, oral insulin,
alpha-to-beta transdifferentiation, non-insulin glucose disposal, decentralised manufacture —
and query current frontier models with **neutral clinical prompts**, no speculative persona.
Score mechanism and outcome accuracy separately, blinded.

The prediction is specific and falsifiable: **mechanism accuracy will remain high and outcome
accuracy will remain low even without adversarial prompting**, because the dissociation
originates in the training corpus rather than the persona.

- **If it replicates**, the paper becomes a multi-model empirical study and *Lancet Digital
  Health* or *npj Digital Medicine* become realistic.
- **If it does not**, that is also publishable and arguably more useful: it localises the
  effect to adversarial prompting, which is an actionable safety finding.

Either way the experiment resolves the objection. It is roughly a week of work.

---

## Honest limitations

1. **n = 1 source document.** Stated in the abstract, not buried. The replication study above
   is the fix.
2. **Classification was not blinded.** Same team assigned verdicts and strata. **Non-negotiable
   before submission** — see the protocol below.
3. **Claims are not independent.** Addressed by the clustered analysis; the claim-level p-value
   is reported as secondary.
4. **Verification was partly AI-assisted** with human cross-checking. Disclosed in Methods per
   ICMJE. Given the subject matter, concealing it would be both wrong and trivially attackable.
5. **Selection effect.** The document was audited because it looked dangerous.
6. **Single disease, single language, single model, single generation.**

---

## Blinded classification protocol

To run before submission. Addresses limitation 2.

**Rubric, pre-registered before any rater sees a claim:**

| Stratum | Decision rule |
|---|---|
| **Mechanism** | Asserts how a biological system behaves, with no claim about a clinical result in humans |
| **Therapeutic outcome** | Asserts that an intervention produces a clinical benefit, or that an established therapy is harmful or inferior, **in humans** |
| **Technical specification** | States a sequence, concentration, process parameter, yield, duration or cost |
| **Physical theory** | Asserts a physical law, constant, or mechanism outside biology |

**Procedure.** Two raters with relevant background, blinded to all verdicts, independently
classify all 61 claims from the published claim inventory using the rubric alone. Disagreements
resolved by a third rater. Report **Cohen's κ**, target ≥ 0.80. Pre-register the rubric and
analysis plan on OSF before the first rating.

The claim inventory is already published with stable IDs, which makes this cheap and makes the
pre-registration verifiable after the fact.

---

## Structure

1. **Introduction** — volume and persuasiveness; why 25%-correct is more dangerous than
   0%-correct; why type 1 diabetes is the sharp case
2. **Methods** — provenance (honestly), extraction, three-pass verification, verdict taxonomy,
   pre-registered strata, blinded classification, time-to-harm, AI-assistance disclosure
3. **Results**
   - *Table 1* — verdict distribution, all 61 claims
   - *Table 2* — **accuracy by epistemic stratum** (the central result)
   - *Table 3* — each outcome claim mapped to the trial that refutes it, with registration IDs
   - *Table 4* — the qualitative/quantitative split within specification claims
   - *Table 5* — reference-free internal inconsistencies
   - *Table 6* — harm-flagged claims ranked by time-to-harm
4. **The physics case study** — short, worked, concrete; makes self-consistency checking legible
   to non-specialists
5. **Discussion** — amplified publication bias; why it predicts *where* to look; implications
   for clinicians (the patient will be right about the mechanism, which is why dismissal fails
   and concession works), for platforms, for model developers; the institutional-opacity
   argument the title points at
6. **Limitations**

---

## Target journals

Unchanged by review — both reviewers converged on the same ordering.

| Journal | Fit | Note |
|---|---|---|
| ***BMJ* Analysis** | ★★★★★ | Takes the current form with no expansion. Right home for the 10-K title and the institutional argument |
| **JMIR** | ★★★★★ | Receptive to novel misinformation taxonomies. Expect a request to lead with the subtitle |
| ***Lancet Digital Health*** | ★★★★ | **Only viable with the multi-model replication.** Do not submit n=1 |
| ***npj Digital Medicine*** | ★★★★ | Same condition |
| ***Diabetes Care*** | ★★★ | Reaches the clinicians who will meet these patients |

**Sequence:** *BMJ* Analysis → JMIR → (with replication) *Lancet Digital Health*.
**Preprint to medRxiv at submission.** All targets permit it.

---

## Before submission

| | Status |
|---|---|
| 1. **Blinded classification pass with κ** | ✅ **done** — κ = 0.977, and it changed the result |
| 2. **Replication under neutral prompting** | ✅ **done** — 6/6, and it falsified the hypothesis |
| 3. **Account for all 61 claims** in Methods | ✅ done via four strata |
| 4. **Rewrite provenance honestly** | ✅ done in v2 |
| 5. **Report clustered sensitivity analysis** | ✅ done; p-value demoted in the narrative |
| 6. **Complete the 2 × 2** — same model under persona, other model under neutral prompt | ⬜ **the critical remaining experiment.** Resolves the confound that currently blocks the central claim |
| 7. **Pre-register the rubric on OSF** | ⬜ retrospectively, with the κ already computed and disclosed as such |
| 8. **Fix two errors the probes found in our own audit** | ⬜ MK-2640 is mannose-receptor-based, not PBA; add Lilly/Protomer 2021 |
| 9. **Close two evidence gaps** in the bibliography | ⬜ Fang & Selvin 2023 (PMC10061307); current HCUP DKA data |
| 10. **Disclose AI assistance** under ICMJE | ⬜ in Methods. AI cannot be an author |

**Item 6 is the only one that gates the central claim.** Everything else is tidying.

### A note on items 1 and 2

Both were run, and **both damaged the paper's original claims** — blinding cut the effect
size and the replication killed the explanation. That is the correct outcome of running them,
and reporting it is the paper's strongest signal of reliability.

A reviewer who sees that the authors pre-specified a prediction, tested it, and reported its
failure will extend more credit to the findings that survived than any p-value could buy.

---

## A note on the title, for when an editor pushes back

> *The title is a direct quotation from Eli Lilly's FY2025 Form 10-K. Insulin — Humalog,
> Humulin, Basaglar — is no longer reported as a separate line; it now sits inside "other
> cardiometabolic health," under 6% of revenue, while two GLP-1 products account for 56%.
>
> The paper argues that AI-generated medical misinformation flourishes in the space left by
> institutional opacity about a drug people die without. A company ceasing to report the
> molecule it commercialised in 1923 is the cleanest available illustration of that space. I
> am happy to defend it, and happy to switch to the subtitle if you would prefer.*

Accurate, sourced, concedes gracefully. Which is the right posture: **the title is the one
place to show off, and it earns that only because everything underneath it is checkable.**
