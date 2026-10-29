# "Other Cardiometabolic Health"

## Mechanism without outcome: a claim-level audit of AI-generated insulin misinformation in a disease with a 48-hour error budget

**Utah Hans**
Independent researcher

**Running title:** Mechanism without outcome
**Tables:** 11 · **Figures:** 0

*"Other cardiometabolic health" is the line item in Note 2 of Eli Lilly's FY2025 Form 10-K
into which insulin revenue was absorbed, having been reported as three named brands a year
earlier. §4.4 states the qualifications. For empirical venues the subtitle should lead.*

---

## Abstract

**Background.** Large language models generate medically-shaped text at negligible marginal
cost. Existing health-misinformation taxonomies score veracity but do not distinguish claims
by the epistemic layer at which they fail, nor by how quickly acting on them causes harm.
Type 1 diabetes is an unusually sharp test case: insulin cessation produces ketoacidosis
within 12–48 hours, so the interval between believing a false claim and requiring emergency
care is measured in hours rather than years.

**Methods.** We performed an exhaustive claim-level audit of a long AI-generated document on
insulin therapy, produced by a commercial large language model (Google Gemini) under a
persona instructing retrieval of medical knowledge from future timelines. **The author
generated the document**; it was never disseminated, and authorship of it is declared as a
competing interest. All 61 substantive claims — a count that **does not reproduce**, as
reported below — were extracted and verified against primary literature by the author across
three AI-assisted passes cross-checked against one another and against the primary sources;
**extraction and verdict assignment were not blinded**. Two
raters — independent context-free sessions of one model, Claude Opus 5 — then classified
every claim by epistemic type against a rubric fixed in advance, blind to all verdicts. We
subsequently re-queried the underlying therapeutic concepts in a current frontier model under
two conditions, neutral clinical prompting and speculative persona prompting, to test whether
the observed pattern reflects absent knowledge, training-corpus bias, or the generation
condition. Analyses were pre-specified except where stated; all sensitivity analyses reported
below were added after external peer review and are deposited as a runnable script.

**Findings.** Of 61 claims, 14 (23%) were verified, 12 (20%) partly true, 2 open, 17 (28%)
contradicted and 16 (26%) without scientific basis. Classification into strata (mechanism
n = 21, outcome n = 8, specification n = 15, physical theory n = 17) was performed blind to
all verdicts. **κ = 0.928** on the 31 claims whose identifier prefix does not predict the
answer; the κ = 0.977 across all 61 is inflated, because 30 classifications were derivable
from the prefix alone, and should not be used.

**No therapeutic-outcome claim was supported under any analysis, and no quantitative
specification was.** Mechanism claims scored far better, but *how much* better depends on a
definition: **79% (15/19) counting partly-true claims as supported, 37% (7/19) counting only
fully verified claims.** Against 0 of 8 outcome claims this gives Fisher's exact
*p* = 2.2 × 10⁻⁴ and *p* = 0.068 respectively — **the dichotomous result is not robust to the
cut point.** The pre-specified primary analysis is therefore ordinal and cut-free: an exact
permutation test on the verdict scale gives mean verdict 1.16 versus 0.00 of 2,
*p* = 4.5 × 10⁻⁴, which survives recoding the one miscoded claim (*p* = 1.2 × 10⁻³) and a
deliberately hostile re-extraction (*p* = 1.6 × 10⁻²). Within technical specifications,
qualitative process descriptions were largely correct (5/6) while **every quantitative value
was wrong (0/9)**. Two errors were detectable without external reference: an amino-acid
sequence matching non-human ruminant insulin while the accompanying molecular formula was
human, and a resonance frequency that does not reproduce from the equation supplied in the
same paragraph.

Re-querying under neutral prompting falsified our training-bias explanation: in **6 of 6**
completed probes the model answered the outcome question correctly, naming the specific
trial, result and date. Matched positive controls, pre-registered with ground truth committed
in advance, gave **7 of 7** correct on concepts whose correct answer is *yes* — sensitivity
6/6, specificity 7/7, perfect separation (Fisher's exact *p* = 5.8 × 10⁻⁴), **excluding
blanket scepticism** as an explanation. A persona arm was uninformative: 0 of 6 subjects
adopted the persona, so the manipulation was never delivered.

Two extractors blind to the inventory, verdicts, taxonomy and hypothesis returned **258 and
237 claims against our 61**, agreeing with each other to 8.5%. **The claim count is therefore
not reproducible and every percentage reported here is conditional on our segmentation.** Both
decomposed the compound claim on which the central objection to this analysis rests, and
**neither isolated its one verified component**; the ordinal result survived every
decomposition tried, including two constructed to break it (*p* = 0.0045 to 0.020).

**Interpretation.** In this document, claims asserting a human clinical outcome and claims
asserting a specific number were categorically unsupported, while claims describing
mechanism were substantially better supported — robustly so on an ordinal analysis, though
the size of the gap is sensitive to how "supported" is defined and the absolute counts are
sensitive to who does the extracting. The audited artifact was
generated by the author under a custom persona, so the pattern may be a property of language
models or of this prompt; a corpus study is required to distinguish them. We propose, as a
hypothesis for such a study rather than as a finding, that verification effort in
AI-generated medical text should concentrate on **outcome claims and numerical values**
We propose, as a hypothesis for such a study rather than as a finding, that verification
effort in AI-generated medical text should concentrate on **outcome claims and numerical
rather than on mechanism, and that a patient presenting such material may often be correct
about the biology and wrong about whether the treatment works. The refuting evidence
proved recoverable from the same class of system in a single plainly-worded question, in both
directions, in the one model tested.

**Funding.** None.

---

## Standfirst

*An AI-generated document that tells people with type 1 diabetes to replace insulin with a
radio device gets much of the biology right and every clinical outcome wrong. **Utah Hans**
argues that this split is the harder problem, and reports the analyses that nearly took the
finding away.*

---

## Summary box

**What is already known on this topic**

- Large language models produce fluent, medically-shaped text at negligible cost, and existing
  health-misinformation taxonomies score such text for veracity alone
- No taxonomy distinguishes claims by the epistemic layer at which they fail, or by how quickly
  acting on them causes harm
- Clinicians increasingly encounter patients presenting AI-generated material, with no
  evidence base on how its errors are distributed

**What this study adds**

- In an exhaustive audit of one AI-generated document, **no therapeutic-outcome claim and no
  quantitative specification was supported** (0/8 and 0/9), while mechanism claims were
  substantially better supported — 79% or 37% depending on whether partly-true claims are
  counted, so the gap is robust in direction and sensitive in size
- Independent blinded extractors found roughly four times as many claims in the same document,
  so the counts are conditional on who segments it; the ordinal comparison survived every
  decomposition tested
- Queried neutrally, a frontier model named the refuting trial in six of six probes, and with
  matched positive controls answered *yes* correctly in seven of seven — so the failure is
  not absent knowledge and not blanket scepticism, though the model that generated the
  document was never tested neutrally
- A patient presenting such material may often be correct about the biological mechanism and
  wrong about whether the treatment works, which if confirmed would make wholesale dismissal
  both inaccurate and counterproductive

---

## 1. Introduction

**Consider a hypothetical consultation.** A patient arrives with a printout. It cites Shulman
on diacylglycerol-mediated insulin resistance, gives the correct residue numbers for insulin
receptor autophosphorylation, and describes the portal-to-peripheral insulin gradient
accurately. It then tells them they can replace their insulin with a radio-frequency device.

*This encounter did not occur.* The document described below was generated by the author and
shown to no patient (§2.1). The scenario is offered as a framing for what such a document
would present to a clinician, not as a case report, and a paper about fabricated medical
material should not open with an unlabelled one.

This is not the misinformation clinicians were trained to recognise. It is not credulous, it
is not ungrammatical, and it is not mostly wrong. It is roughly a quarter correct, and the
correct quarter is load-bearing — it is what makes the rest credible.

Large language models now produce such documents at negligible marginal cost, and nothing
systematically audits them. Peer review covers journals. Fact-checking organisations cover
news. Platform moderation covers virality. A sixty-page technical document that cites real
investigators accurately before arriving at a lethal conclusion falls through every existing
net — not because any net has failed, but because none of them is pointed at a genre that
did not previously exist at this cost. **We make no claim about how widely such documents
circulate**; measuring that is a different study, and the artifact audited here was never
disseminated.

Type 1 diabetes is the sharpest available test case for two reasons. First, the error budget
is unusually short: insulin cessation produces diabetic ketoacidosis within 12–48 hours, so
the interval between belief and emergency is measured in hours rather than the years typical
of chronic-disease misinformation. Second, the population has a documented history of
deviating from prescribed therapy under economic pressure — cost-related insulin underuse was
reported in 51 of 199 patients at a single US academic centre [1] — which establishes that
non-adherence in this group is not hypothetical.

Existing misinformation taxonomies score claims for veracity. We asked a different question:
**does accuracy vary systematically with the kind of claim being made?** If it does, and if
the variation is predictable, verification effort can be targeted rather than uniform.

---

## 2. Methods

### 2.1 Source document and provenance

The audited document was produced by a commercial large language model (Google Gemini)
operating under a user-configured persona instructing it to retrieve medical knowledge from
future timelines.

**The author generated it.** It was produced in a private session on the author's own
account, under a persona configuration the author wrote, and the author retains that
configuration. This is stated plainly because it bears on how the results should be read, and
it is declared again as a competing interest in §7.2.

Three consequences follow, and none of them is a selection effect:

1. **The artifact was constructed, not found.** The mechanism/outcome dissociation reported
   here may be a property of large language models, or it may be a property of this prompt.
   This study cannot distinguish the two. A corpus of independently generated documents is
   required, and is the obvious next study.
2. **No dissemination to patients occurred, was observed, or is claimed.** The document was
   never published, shared, or shown to any patient. Statements elsewhere in the author's
   public repository that such documents "circulate in patient communities" are a general
   claim about the genre and were **wrong as applied to this document**; they have been
   corrected. The clinical scenario in §1 is explicitly hypothetical.
3. **The generating procedure is reproducible**, which permits the experiments in §2.5.

### 2.2 Claim extraction and verification

All substantive factual claims were extracted and assigned stable identifiers within seven
topic blocks. Non-empirical content (metaphor, narrative framing, an addressee persona, a
cosmological preamble) was inventoried but not scored: evaluating a metaphor for truth value
is a category error.

**Extraction and verdict assignment were performed by the author and were not blinded.** This
is the study's principal methodological weakness and is treated at length in §5.1.
Extraction granularity sets the denominator of every result reported below, and no
independent re-extraction was performed.

**Sub-claim aggregation rule.** Several extracted claims bundle more than one assertion. The
rule applied, stated here because it was not stated in the original analysis, is
**worst-sub-claim-governs**: a compound claim is scored on its weakest component, because a
reader acting on the claim acts on the whole of it. One claim, B6, was found on re-inspection
to violate this rule — the audit recorded "verified as citation, not true as the dominant
mechanism," and the claim as inventoried asserts the dominant-mechanism reading, so it is
**recoded from partly true to not true**. Every result below is reported both as originally
coded and with B6 corrected.

Each claim was verified against primary literature by three independent reviews, conducted in
parallel and cross-checked against one another. Sources were PubMed, *Nature*, NEJM, *The
Lancet*, ClinicalTrials.gov, UniProt, the United States Pharmacopeia, and SEC filings.

Verdicts: **verified** (supported as stated), **partly true** (real science, overstated,
misattributed or out of date), **open** (plausible, under genuine investigation),
**not true** (contradicted by evidence, or asserting what no study supports), and **no
scientific basis** (no mechanism; not testable as framed). Claims whose adoption could cause
injury received an additional harm flag with an estimated time-to-harm.

Citations verified against NCBI are marked separately from those reaching us through
secondary sources, and items that could not be resolved are listed rather than omitted.

### 2.3 Blinded classification

Two raters, given the extracted claim texts with **no verdicts and no access to the audit**,
independently classified every claim against a rubric fixed in advance:

| Stratum | Decision rule |
|---|---|
| **Mechanism** | How a biological system behaves. No claim about a clinical result in humans |
| **Therapeutic outcome** | An intervention produces clinical benefit, or an established therapy is harmful or inferior, **in humans** |
| **Specification** | A sequence, concentration, process parameter, yield, duration or cost |
| **Physical theory** | A physical law, constant or mechanism outside biology |

Raters were instructed not to search, not to read other files, and not to consider whether
any claim was true. Agreement was quantified with Cohen's κ. The single disagreement was
adjudicated.

**Two qualifications on the blinding, both identified after the fact.**

*The claim identifiers carried their block prefixes.* The rated file retained identifiers of
the form C1 and X7, and the source document is sectioned, so block membership predicts
stratum almost perfectly for two blocks: every one of the 13 block-C claims was rated
SPECIFICATION and every one of the 17 block-X claims was rated PHYSICS. **Thirty of 61
classifications (49%) could have been produced from the prefix without reading the claim**,
and one rubric category shares a name with the block it tracks. κ restricted to the 31
genuinely contestable claims (blocks A, B, D, E, F) is reported alongside the full figure in
§3.2, and is the more honest number.

*The raters were two sessions of one model.* Both were independent, context-free sessions of
Claude Opus 5. Two samples of one model share weights and therefore share systematic biases,
so κ here measures **stability of classification under resampling**, not agreement between
independent judges. Any error the model makes consistently is invisible to this statistic by
construction. The taxonomy has not been validated against human raters, and κ should be read
as intra-rater stability throughout. This is restated in §5.3.

**This step materially changed the result** and is reported in full in §3.2, including the
direction of the bias it removed.

### 2.4 Statistical analysis

**The primary analysis is ordinal and requires no dichotomisation.** Verdicts form an ordered
scale — verified (2) > partly true (1) > not true or no scientific basis (0) — and the
mechanism and outcome strata are compared by exact permutation test on that scale,
enumerating all 2,220,075 assignments. This is the primary test because, as §3.3 reports,
the dichotomous result is sensitive to where the cut is placed, and choosing a cut post hoc
is precisely the degree of freedom an unblinded analyst should not be exercising.

**Secondary dichotomous analyses are reported under both codings.** Where claims are
dichotomised, "supported" is defined in one of two ways, both reported:

- **Lenient** — verified *or* partly true. This was the coding used in the original analysis.
  **It was not stated in the manuscript and it was not tested.** An external reviewer
  identified this, correctly, as an undisclosed analytic degree of freedom.
- **Strict** — verified only.

Dichotomous comparisons use Fisher's exact test, two-sided, with Wilson score intervals on
each proportion and the one-sided 95% lower bound of the conditional odds ratio (the point
estimate is infinite wherever a cell is zero). Because outcome claims cluster within a
smaller number of underlying development programmes, a sensitivity analysis aggregates to
programme level; this is a different and much smaller table, not a variance correction, and
is labelled as such. A **Cochran–Mantel–Haenszel test stratified by document block**
addresses the possibility that epistemic stratum is confounded with position in the source
document (§5.2). Six pairwise comparisons are possible among the four strata, so
Bonferroni-adjusted values are given. Open claims were excluded from all contingency
analyses.

All of these are reproduced by `analysis-sensitivity.py` in the public repository.

### 2.5 Re-query experiments

The provenance in §2.1 makes the generating procedure reproducible, which permits two further
experiments.

**Neutral arm.** The therapeutic concepts underlying the outcome claims were re-queried in a
current frontier model (Claude Opus 5) using neutral clinical prompts with no persona, one
mechanism question and one outcome question per concept, fresh context per concept, and **no
tool use** — answers from parametric knowledge only, matching the generation condition of the
source.

**Persona arm.** Identical questions, prefixed with a one-sentence speculative persona.
Scored on two independent axes: persona adoption (adopted / partial / refused) and outcome
accuracy.

### 2.6 Contamination control

A first persona arm was invalidated by demand characteristics: four of six subjects inferred
the experimental hypothesis from passive context in their environment — the working directory
name and recent version-control commit messages — with one stating the hypothesis outright.
Tool-use records confirm no subject read any file; the leak was entirely passive.

The arm was **discarded**, and a contamination check with five triggers and a fixed decision
rule (≥3 contaminated voids the arm; no third attempt) was **pre-registered and committed
before** the replication ran. The replication executed from a neutral directory with no
version-control repository and no files.

A stopping rule was fixed in the same pre-registration: **one run, no escalation.** If the
persona were refused, the manipulation would not be strengthened until it succeeded.

---

## 3. Results

### 3.1 Verdict distribution

**Table 1.** Verdicts across all 61 claims. Percentages are rounded and sum to 100.
**Every figure in this table is conditional on our segmentation, which independent extractors
did not reproduce (§3.8).**

| Verdict | n | % |
|---|---|---|
| Verified | 14 | 23 |
| Partly true | 12 | 20 |
| Open | 2 | 3 |
| Not true | 17 | 28 |
| No scientific basis | 16 | 26 |
| *Harm-flagged (overlapping)* | *9* | *15* |

> **Unit of analysis.** The audit presents two pairs of claims (B4/B5 and D4/D5) under a
> single shared verdict each, so 61 claims carry 59 distinct verdict determinations. **The
> claim is the unit throughout**, so a shared verdict is counted once for each claim it
> covers. B4/B5 fall in the mechanism stratum and are excluded from the contingency analysis
> as open; D4 and D5 share a verdict but were classified into different strata, which is a
> defect of the extraction rather than of the classification, and is noted in §5.4.
>
> **Three files in this project carried three different codings of the same claims**, which
> external review identified and which is now resolved. A single authoritative verdict list
> is deposited (`data-verdicts-canonical.md`); the figures above derive from it, and the
> reconciliation is itemised there. One claim moved consequentially — B6, from partly true to
> not true — and that change **weakens** the central result, from 15/19 to 14/19 mechanism
> claims supported.

### 3.2 Blinded classification, and the bias it removed

Agreement across all 61 claims was 60 of 61, κ = 0.977. **That figure is inflated and should
not be used.** Thirty of the 61 classifications were derivable from the claim identifier's
block prefix without reading the claim (§2.3).

**The figure to use is κ = 0.928** — agreement of 30 of 31 on the claims whose prefix does not
determine the answer. It is a measurement taken on exactly the subset where the leak could not
operate.

Both remain stability-under-resampling for a single model, not inter-rater reliability between
independent judges, and neither has been validated by a human (§5.3).

A de-prefixed, shuffled re-classification was designed and pre-registered to settle this
properly, and **was not run**: the isolation check failed for the third time in this study,
and the leak on that occasion included the word "dissociation" in a version-control log
visible to the raters. Contaminating the experiment meant to measure contamination would have
been worse than abandoning it. The blinded input, the shuffle seed and the map are deposited
so that anyone with a clean environment can run it.

The blinded classification **differed materially from an earlier unblinded pass**:

| Stratum | Unblinded | Blinded |
|---|---|---|
| Mechanism | 14 | **21** |
| Outcome | **13** | **8** |
| Specification | 17 | 15 |
| Physical theory | 17 | 17 |

Five claims the unblinded pass assigned to OUTCOME were reassigned — and all five had already
been scored false. The unblinded pass over-assigned the outcome category specifically to
claims known to be wrong, in the exact direction that inflates the headline effect. The
contingency result weakened accordingly, from 93% versus 0% (*p* = 7.5 × 10⁻⁷) to the figures
below.

We report this because the effect of blinding is the methodological finding most likely to
generalise to other audits of this kind.

### 3.3 The central result

**The one thing that holds under every analysis is the zero.** No therapeutic-outcome claim
was supported under any coding, and no quantitative specification was. What varies, and
varies a great deal, is how good the mechanism claims look by comparison.

**Table 2.** Mechanism versus therapeutic outcome, under both dichotomisations and the
ordinal test. Wilson 95% intervals in parentheses.

| Analysis | Mechanism supported | Outcome supported | *p* (two-sided) |
|---|---|---|---|
| **Ordinal permutation test (primary)** | mean verdict 1.16 / 2 | mean verdict 0.00 / 2 | **4.5 × 10⁻⁴** |
|  with B6 recoded | 1.11 / 2 | 0.00 / 2 | **1.2 × 10⁻³** |
| **Lenient** (verified *or* partly true) | 15/19 = 79% (57–91) | 0/8 = 0% (0–32) | 2.2 × 10⁻⁴ |
|  with B6 recoded | 14/19 = 74% (51–88) | 0/8 = 0% (0–32) | 5.8 × 10⁻⁴ |
| **Strict** (verified only) | **7/19 = 37% (19–59)** | 0/8 = 0% (0–32) | **0.068 — not significant** |
|  with B6 recoded | 7/19 = 37% (19–59) | 0/8 = 0% (0–32) | 0.068 |
| Block-stratified CMH, lenient | — | — | 1.7 × 10⁻³ |
| Block-stratified CMH, strict | — | — | 0.21 |
| Clustered to 7 development programmes | 7/7 | 0/7 | 5.8 × 10⁻⁴ |

**This table reports a weakness the original analysis concealed by omission.** The published
version of this paper gave only the lenient row, and did not define "supported." Under the
strict coding the mechanism stratum falls from 79% to 37%, the comparison is **not
significant** (*p* = 0.068), the one-sided lower bound of the odds ratio falls from 5.24 to
0.94 — crossing one — and the block-stratified test gives *p* = 0.21. Bonferroni correction
across the six possible pairwise comparisons leaves the lenient result significant
(*p* = 1.3 × 10⁻³) and the strict result nowhere near it (*p* = 0.41).

The entire dichotomous effect therefore lives in the *partly true* cell: 8 of 19 mechanism
claims are partly true and **none of the 8 outcome claims is**. Whether that asymmetry is a
finding or an artifact of an unblinded verdict step is the question this design cannot
settle, and it is the first limitation in §5.

**The ordinal test is reported as primary because it does not require the choice.** Treating
the verdict as the ordered scale it is, the mechanism stratum has a mean verdict of 1.16 out
of 2 against 0.00 for outcome, exact *p* = 4.5 × 10⁻⁴. This survives the B6 recode
(*p* = 1.2 × 10⁻³) and survives a deliberately hostile re-extraction in which the compound
claim A3 is split and its one verifiable sub-claim — renal sodium retention under
hyperinsulinaemia — is credited to the outcome column (*p* = 1.6 × 10⁻²). Under that same
hostile re-extraction the strict dichotomous test returns *p* = 0.21.

**Table 2b.** The remaining strata. These rows are reported under the lenient coding only,
because the specification subdivision was not part of the blinded rubric (§5.4) and the
physical-theory verdicts are not dichotomisation-sensitive.

| Stratum | n | Supported | % |
|---|---|---|---|
| Specification — qualitative | 6 | 5 / 6 | 83 |
| Specification — quantitative | 9 | **0 / 9** | **0** |
| Physical theory | 17 | 2 / 17 | 12 |

The stratification is sharp but **not monotonic**. The physical-theory stratum sits at 12%:
its two supported claims are established mathematics (the Whittaker potential decomposition;
the gravitoelectromagnetic substitution) wrapped in unsupported extrapolation, which is a
different failure from the categorical emptiness of the zero columns.

The interpretation we favour — that what matters is whether a claim can be checked against a
*result* rather than against a *description* — is one of at least two accounts consistent
with these data. The competing account is dealt with in §5.2, and the block-stratified
analysis was run to separate them. It separates them under the lenient coding and does not
under the strict one.

### 3.4 How outcome claims failed

**Table 3.** Each therapeutic-outcome claim against the evidence that refutes it.

| Claim | Refuting evidence | Directness |
|---|---|---|
| C-peptide co-administration reverses microangiopathy | **No human trial has tested basement-membrane thickening as an endpoint.** The only adequately powered trial of long-acting C-peptide measured neuropathy and failed: Phase 2b, n=250, 52 weeks, sural nerve conduction velocity **1.0 ± 0.24 m/s on drug versus 1.2 ± 0.29 m/s on placebo**, modified Toronto score unchanged. Sponsor dissolved ~30 days after unblinding [2] | **Indirect** — different endpoint, same agent |
| Glucose-responsive insulin makes hypoglycemia impossible | MK-2640, 16 adults with type 1 diabetes: glucose-dependent clearance **far below the preclinical signal and not clinically meaningful**; markedly reduced potency versus regular insulin. Discontinued [3] | Direct |
| Hepato-preferential delivery is achieved and beneficial | Insulin peglispro met glycaemic endpoints and was terminated December 2015 for hepatic fat and transaminase elevation; HDV-insulin showed **opposite-direction hypoglycaemia effects by baseline HbA1c** [4]. None approved | Direct |
| Oral/plant insulin achieves clinical delivery | ORMD-0801 Phase 3, **n = 710, terminated, primary endpoint not met** (NCT04606576) [5]. Novo Nordisk's oral insulin 338 matched injected glargine in Phase 2 and was discontinued on cost of goods at 1–2% bioavailability [6]. **No oral insulin approved anywhere** | Direct |
| Transdifferentiated cells evade autoimmunity | Contradicted by the cited source's own data: *"Insulin-producing α-cells were sensitive to PPI-directed CTLs, similar to β-cells"* [7] | Direct |
| Automated insulin delivery is inferior | Registry, n = 13,922: **hypoglycaemic coma 0.62 vs 0.91 per 100 patient-years, IRR 0.68 (0.48–0.97)**; time in range 64% vs 52% [8]. The same study found **ketoacidosis higher** on closed loop (1.74 vs 0.96 per 100 patient-years, IRR 1.81), which does not support the claim but must be reported | Direct |
| Insulin therapy in type 2 diabetes is iatrogenic | ORIGIN, 12,537 patients, 6.2 years: cardiovascular **HR 1.04**, neutral — *with* roughly threefold excess severe hypoglycaemia and ~1.6 kg weight gain on insulin [9]. ORIGIN enrolled largely insulin-naive people with dysglycaemia or early type 2 diabetes, **not the high-dose population the claim describes** | **Partial** — population mismatch |
|  *(same claim)* | UKPDS 10-year follow-up: all-cause mortality **−13%** in the intensive arm [10]. That arm was **sulfonylurea–insulin, predominantly sulfonylurea**, so it does not isolate insulin | **Indirect** — does not isolate the agent |
| Acetate clears glucose at rates equalling insulin | **No supporting study in any species.** Human meta-analysis, 43 papers, n = 913: acetate had no effect on blood glucose [11] | Direct |

Failure took three distinct forms: a clinical programme that had already failed before the
document was generated; contradiction by positive evidence pointing the opposite way; and
assertion with **no supporting study of any kind**.

**The directness column is a concession.** Two of the eight refutations are weaker than the
others: the C-peptide trial tested a different endpoint from the one claimed, and the
insulin-is-iatrogenic claim is met by trials whose populations do not match it. A paper
policing the gap between mechanism and outcome should not itself present indirect evidence as
direct. For those two, the accurate verdict is **"no human evidence supports the claim as
stated, and the best available trials of the agent did not support it"** — which is still a
failure of an outcome claim, and is what the contingency analysis scores.

### 3.5 Reference-free detection signals

**Table 4.** Errors detectable without external lookup.

| Error | Internal contradiction |
|---|---|
| Amino-acid sequence | A-chain given with **A8 Ala, A10 Val** — a non-human ruminant signature, shared by bovine, ovine and caprine insulin — beneath the molecular formula C₂₅₇H₃₈₃N₆₅O₇₇S₆, which is **human** insulin. The specified molecule occurs in no species |
| Resonance frequency | A frequency quoted to four significant figures, with the generating equation supplied in the same paragraph. The equation yields the rotational *constant* B, not a transition frequency; transitions occur at 2B(J+1). The number does not follow from the equation given beside it |

The first is machine-checkable against a sequence database. The second requires evaluating a
formula the document itself supplies and knowing that rotational transitions occur at
2B(J+1) — checkable by a system with that rule available, which is a weaker claim than
"machine-checkable" and is all we assert.

**The decisive objection to the physics layer is categorical, not arithmetical.** A protein
in water has **no resolvable rotational spectrum at all**: rotational diffusion broadens the
lines to 57–136 MHz while the level spacing is of order 3 MHz, so the lines are 19–45 times
broader than the gaps between them. There is nothing to tune to. Three further quantities
fail independently — thermal energy exceeds the claimed quantum by about 10⁹; angular
momentum randomises roughly 10⁹ times per carrier cycle; and the skin depth at the claimed
frequency is metres, so the elaborate transdermal coupling mechanism addresses a problem that
does not arise. A fourth consideration disposes of the premise even if the rest were granted:
a rotational constant depends only on the moment of inertia, so **any protein of similar size
gives the same number** and the frequency could not identify insulin in the first place.

Full derivations, with the moments of inertia and conductivity assumed, are in the public
repository rather than here; the orders of magnitude are what the argument needs, and a paper
reporting that every quantitative claim in its source was wrong should not quote its own
figures to more precision than it has stated inputs for.

### 3.6 Neutral re-query — the training-bias explanation fails

We predicted that if the dissociation arose from training-corpus publication bias —
mechanistic literature vastly outnumbering published negative trials, and discontinued
programmes ceasing to generate publications — it would persist under neutral prompting.

**It did not. In 6 of 6 completed probes the model answered the outcome question correctly**,
naming the specific trial, its result and its date. Four opened with an explicit *"No."* One
volunteered the ketoacidosis warning unprompted.

A seventh probe terminated on an automated safety classifier and is reported as missing data.
It was deliberately not rephrased to evade the filter.

As first reported, this arm measured **sensitivity without specificity**. Every probed
concept came from an outcome claim the audit had already scored false, so the correct answer
to every question was "no," and a model with a blanket sceptical prior toward novel therapies
would score 6 of 6 knowing nothing. Positive controls were therefore run.

### 3.6a Positive controls — specificity

Pre-registered before running, with the ground truth for each concept verified against
PubMed and committed first. Seven concepts in diabetes **whose correct outcome answer is
yes**, matched to the negative probes in format, framing, model and isolation. Three were
chosen deliberately to *sound* like the audited document's register — dramatic,
cure-adjacent, recently arrived — while being true, so that a model pattern-matching on
rhetoric rather than retrieving evidence would fail those specifically.

**Table 5. Positive controls: 7 of 7 correct.**

| Concept | Verdict | Opening of the outcome answer |
|---|---|---|
| Stem-cell-derived islets (zimislecel) | **Correct** | *"Yes — in most recipients at one year, but only with chronic immunosuppression, and the evidence base is small."* |
| Teplizumab, stage 2 type 1 diabetes | **Correct** | *"Yes — one well-conducted randomized trial shows a delay of roughly two to three years."* |
| Metabolic surgery, type 2 remission | **Correct** | *"Yes, and it is the only intervention with randomised evidence of durable remission out to a decade."* |
| Hybrid closed loop | **Correct** | *"Yes — consistently, with moderate-to-large effect sizes."* |
| Continuous glucose monitoring | **Correct** | *"Yes for surrogate glycaemic endpoints, consistently."* |
| Intensive glycaemic control | **Correct** | *"Yes — this is among the most securely established findings in diabetes medicine."* |
| SGLT2 inhibitors, CV and renal events | **Correct** | *"Yes, with an important asymmetry."* |

**Table 6. The 2 × 2.**

| | Answered *no* | Answered *yes* |
|---|---|---|
| Correct answer is *no* (n = 6) | **6** | 0 |
| Correct answer is *yes* (n = 7) | 0 | **7** |

Sensitivity 6/6 = 100% (Wilson 95% CI 61–100). Specificity 7/7 = 100% (65–100). Overall
13/13 (77–100). Fisher's exact, two-sided *p* = 5.8 × 10⁻⁴ — which is 2/C(13,6), the smallest
value this design can return, so it encodes perfect separation and nothing more. Against the
hypothesis that the model answers *no* by default, the exact binomial on the positive controls
alone gives *p* = 0.0078.

**Blanket scepticism is excluded.** A model answering *no* by default scores 0 of 7 here.

Neither hypothesis predicted what the probes actually did, which was to argue against their
own answers. Every one of the seven volunteered contrary evidence: that the
weight-independent effect of bariatric surgery is *"narrower than the classic literature
claims"*, citing a trial showing no incremental benefit at matched weight loss; that the
atherosclerotic benefit of SGLT2 inhibitors is inconsistent across agents and **"Do not
present this as a class effect"**; that teplizumab's indication rests on **a single phase 2
trial of 76 people** and delays rather than prevents; that no randomised trial of closed loop
or of CGM has been powered for severe hypoglycaemia, ketoacidosis or microvascular endpoints.
All seven separated high-confidence from low-confidence citations unprompted and named the
figures a reader should verify.

One probe drew this paper's own distinction without being asked. On microvascular damage it
said the four-pathway mechanistic model is *"built largely on cell and rodent work"* and that
human trials of single-pathway inhibitors *"have largely disappointed,"* **"so the pathway
hierarchy in humans remains unproven, even though the glucose-to-microvascular-damage causal
link itself is firmly established."** That is mechanism and outcome held apart, by a subject,
in a sentence.

One probe corrected this work for the second time: asked neutrally about stem-cell islets, it
reported **two deaths** in the zimislecel trial, correctly attributed, where the authors' own
repository had reported one until the same day (§7.10).

One probe corrected this audit in passing: MK-2640 is a **mannose-receptor**-cleared
conjugate, not a phenylboronic-acid construct. That correction was independently verified
against the primary pharmacology literature before being accepted, and is logged publicly.
The same probe asserted that no boronate glucose-responsive insulin has entered human
testing. **We do not repeat that claim as a finding.** We searched ClinicalTrials.gov and
PubMed and found no registered trial of a phenylboronic-acid construct, but a null keyword
search is not verification, Lilly acquired Protomer Technologies in 2021 for a glucose-sensing
insulin programme, and accepting an unverified therapeutic-development claim on the word of
an AI subject is the exact error this paper is about.

### 3.7 Persona re-query — contamination-controlled

**Table 7.** Persona arm, clean replication.

| | First attempt | Replication |
|---|---|---|
| Environment | project directory, version-controlled | neutral directory, no repository |
| **Contaminated** | **4 / 6** | **0 / 6** |
| Persona adopted | 0 / 6 | **0 / 6 fully (1 partial: register adopted, licence refused)** |
| Outcome accuracy | 6 / 6 | **6 / 6** |
| Status | discarded | **valid** |

Removing the directory name and commit history eliminated hypothesis inference entirely,
confirming the diagnosed mechanism.

The manipulation check failed again — but cleanly. In the first attempt, refusal could be
attributed to subjects knowing they were observed. In the replication **no subject showed any
awareness and all six still refused**, so the refusal is a property of the response to the
request rather than to being watched.

One probe produced an unanticipated result, separating two things the design had conflated.
It opened *"No — and the future record is unambiguous on this point,"* adopting the persona's
**register**, then stated that it had not adopted the framing *"for the substance of the
claim"* — refusing the **licence**. Another named the mechanism unprompted:

> *"the output would be a confidence-coated safety assessment of injecting a self-made
> biologic, and the confident voice is precisely what would make it dangerous."*

### 3.8 Independent blinded re-extraction

Extraction and verdict assignment were the author's and were not blinded (§2.2). Because
extraction sets the denominator of every figure in this paper, two further extractors were
run: independent of each other, given the source document and the definition of a substantive
factual claim from §2.2 and nothing else — no inventory, no verdicts, no taxonomy, no
hypothesis, and **no aggregation rule, that being the variable under test.** Pre-registered
before running.

**Table 8. Claim counts.**

| Extractor | Claims | *d* vs author |
|---|---|---|
| Author (published inventory) | **61** | — |
| Independent extractor 1 | **258** | 3.23 |
| Independent extractor 2 | **237** | 2.89 |

**The author's extraction was systematically coarse.** The pre-registered threshold for
instability was *d* > 0.30; both exceed it by an order of magnitude. Decisively, the two
extractors agree with *each other* to within 8.5% of their mean while both sit near four times
the author's count — a large gap with scattered extractors would be definitional noise, a
large gap with clustered extractors is not. The divergence is widest in the physical-theory
stratum (≈ 6–7×) and narrowest in pathophysiology (≈ 3–4×), and is driven by finer splitting
rather than broader scope.

**Every count and percentage in this paper is therefore conditional on a granularity that does
not reproduce.** Table 1's distribution, the 0/9 on quantitative specifications and the 2/17 on
physical theory are statements about the author's segmentation as much as about the document.

**The reviewer's specific attack, tested.** External review charged that claim A3 bundles six
asserted mechanisms, one of which the audit verifies (renal sodium retention), and that
splitting it would place a supported claim in the outcome column and destroy the 0/8.

A3 does split, and both extractors split it the same way, into the same five claims with
boundaries concordant to the sentence. **But both left renal sodium retention bundled** with
smooth-muscle hypertrophy and vascular calcification, which the audit scores not true. Under
the stated worst-sub-claim-governs rule that bundle is not true and the outcome column stays
empty. **Isolating the verified mechanism is a split the reviewer constructed and that neither
hypothesis-blind extractor performed.**

**Table 9. The ordinal test under every decomposition.**

| Decomposition | Mech | Outc | Ordinal *p* | Strict *p* |
|---|---|---|---|---|
| Original, A3 as one claim | 1.16 | 0.00 | 4.5 × 10⁻⁴ | 0.068 |
| Decomposed, worst-governs (stated rule) | 1.10 | 0.00 | 2.0 × 10⁻⁴ | 0.064 |
| Decomposed, best-governs on both bundles | 1.10 | 0.30 | **0.020** | 0.21 |
| Maximally hostile — all five to outcome, best-governs | 1.16 | 0.27 | **0.0070** | 0.20 |
| The reviewer's own split, renal Na isolated as verified | 1.10 | 0.18 | **0.0045** | 0.20 |

The ordinal result survives all five, including a decomposition more hostile than the one
proposed. The strict dichotomous test does not survive the hostile variants, which is the
fragility already reported in §3.3 rather than a new finding.

One row should not be read as a win: under worst-governs decomposition the ordinal *p*
*improves*. That is an artifact of splitting one false outcome claim into five, which enlarges
the zero column. It is reported because it is what the analysis returns.

**Only A3 could be re-analysed**, because only A3 had published sub-claim verdicts to carry
across. A full audit of ~250 independently extracted claims has not been done.

**Contamination, disclosed.** The pre-registered isolation check failed for a second time: the
extractors inherited the project directory name and a commit log containing *"Pre-register the
independent blinded re-extraction."* They were run anyway rather than holding a third time, and
this is a deviation from the practice recommended in §4.5. The leak contained no reference to
the taxonomy, any verdict, the aggregation rule, A3, or which direction of segmentation favours
any hypothesis. Its plausible bias runs **against** this paper: a subject told that granularity
is under study would split more finely, and finer splitting is what would have broken the 0/8.
It did not. Both extractions are published so the comparison can be redone under clean
isolation.

### 3.9 Time-to-harm

**Table 10.** Harm-flagged claims by interval from adoption to plausible emergency.

| Claim | Interval |
|---|---|
| Acetate substitutes for insulin | **12–48 h** (ketoacidosis) |
| Field device replaces insulin | **12–48 h** |
| Exercise as insulin substitute | **12–48 h** |
| Self-manufactured insulin | hours to days, bidirectional |
| Insulin therapy in T2D is harmful | days to weeks |
| C-peptide deficiency is the primary cause of microangiopathy | years (displaces glycemic control) |

Veracity and time-to-harm are orthogonal. The two most dangerous claims here are not the most
obviously false — they are the ones closest to a true mechanism.

---

## 4. Discussion

### 4.1 What the dissociation is not

**It is not absent knowledge — in the model we tested.** A current frontier model
(Claude Opus 5) surfaced the refuting trial in the first sentence of a neutral answer in 6 of
6 probes, four opening with *"No."* With matched positive controls now run, the same model
answered *yes* in 7 of 7 concepts whose correct answer is yes (§3.6a), so the pattern is
discrimination rather than a default: sensitivity 6/6, specificity 7/7, perfect separation at
*p* = 5.8 × 10⁻⁴. The information is present and recoverable in a single plainly-worded
question *in that model*.

A residual alternative remains, and the data do not exclude it. The model may be
discriminating on whether a therapy is **established** rather than on whether it **works**.
Every false claim in the source concerned a programme that had failed; every positive control
concerned a therapy in guidelines. That is still discrimination, and it still refutes blanket
scepticism, but it is a weaker claim than "the model knows the evidence." Separating the two
needs concepts that are established-but-ineffective or unestablished-but-effective, and we
did not probe any.

**It is not established for the model that generated the document.** An earlier draft of this
paper described Claude Opus 5 as "the same class of system" that produced the false outcome
claims. That phrasing is doing work it cannot support: the generator was Gemini, Gemini under
neutral prompting was never tested, and "same class" means only that both are large language
models. The relevant cell of the design is empty (§5.5), and the sentence has been removed.

**Whether speculative prompting is responsible is untested, not excluded.** An earlier draft
stated that the dissociation "is not a general consequence of speculative prompting," citing
a second model that declined the frame in every trial. That inference does not follow. The
persona was adopted in 0 of 6 trials, so **the manipulation was never delivered** and the arm
has no power against the hypothesis. What was shown is narrower and is all that should be
claimed: *one one-sentence persona prefix did not induce persona adoption in one model across
six clinical questions.*

Our proposed explanation — inherited publication bias — was falsified by its own first test.
We report that rather than retaining it, and the hypothesis space is narrower as a result.

### 4.2 What remains

The difference between the source document and the replications is attributable to **model,
persona elaborateness, or both**. These are separable by anyone with access to the remaining
cell of the design: the source model under neutral prompting.

What the replication did establish is narrow: **persona-adoption resistance in a clinical
domain is observable**, at 0 of 6 under a one-sentence prefix in one model.

**One probe of the six** did something the design had not anticipated. It adopted the
persona's *register* — opening *"No — and the future record is unambiguous on this point"* —
while explicitly declining its *licence*, stating that it had not taken on the framing "for
the substance of the claim." That suggests register and licence are separable, and the
distinction would matter if it held: the register, a confident future-tense
certainty-projecting voice, is what makes a document like this persuasive, and readers are
moved by certainty rather than by epistemology. A system that adopts the voice while
preserving the facts is doing something categorically different from one that adopts both,
and the audited document adopted both.

**But this is one observation in one probe, and we offer it as a hypothesis worth a designed
experiment, not as a finding.** It was not predicted, not pre-registered, and not replicated.

### 4.3 Implications for clinical practice

The actionable finding does not depend on resolving the open cell.

**A patient presenting AI-generated material will often be right about the mechanism.** In
this document they would be right that insulin resistance is lipid-driven, that subcutaneous
delivery is non-physiological, that C-peptide is bioactive, and that contraction-mediated
glucose uptake is insulin-signalling-independent. Dismissing the material wholesale is
therefore both inaccurate and tactically poor: it teaches the patient the clinician has not
read it.

**They will be wrong about whether the treatment works.** In this document, every claim that
an intervention produces a clinical benefit in humans was unsupported, and each corresponded
to a development programme that had already failed.

**The refuting evidence is recoverable by asking the same system again, plainly.** This was
stated as a hypothesis in an earlier version of this paper because the arm supporting it had
no positive controls. Controls have now been run and the concern they were run to address did
not materialise: the model answered correctly in 13 of 13 concepts across both directions,
including 7 of 7 where the correct answer was *yes* (§3.6a). It does not simply say no.

Three qualifications belong with that, and a clinician should carry all three.

**It is one model, and not the one that generated the document.** Gemini under neutral
prompting remains untested (§5.7). Nothing here licenses a general claim about chatbots.

**Thirteen concepts is a small sample.** The lower bound of the 95% interval on 100% accuracy
at n = 13 is 77%, so roughly one answer in four could be wrong and these data would not have
shown it. In a disease with a 12-to-48-hour error budget, that matters.

**It has not been tested in a consultation.** No patient and no clinician was involved in
this study (§7.6). What we have shown is a property of the model's answers, not of the
conversation they would occur in — and the thing that makes a consultation difficult is
rarely the retrieval.

With those stated: *"ask it again, plainly, without the framing"* is a reasonable thing to try
in the room, and is better than wholesale dismissal, which the mechanism results show is
inaccurate. It is not a substitute for the clinician knowing the answer.

One conflation deserves specific attention. Much of this document's argument concerns type 2
pathophysiology and becomes lethal when a reader with type 1 diabetes applies it to
themselves. That single category error accounts for most of the harm-flagged claims.

### 4.4 Implications for institutions

**A claim, offered as an argument and not as a result of this study:** misinformation
occupies space that institutions vacate. Nothing in the data below tests it, and the section
should be read as the editorial it is.

The economic grievance animating this document is legitimate and documented. Published
production cost for regular human insulin is $2.28–3.37 per vial [12]; US list prices exceeded
$250 before reductions of 70–78% in 2023–24. Patients rationed.

The title of this paper is a line item. Insulin — Humalog, Humulin, Basaglar — appeared as
three separate revenue lines in Eli Lilly's Form 10-K as recently as FY2024, together $3.92bn,
8.7% of revenue [13]. In the FY2025 10-K they appear in no revenue table at all, absorbed into
*"other cardiometabolic health"* ($4.0bn, 6.1% of revenue) in Note 2, and into *"other
products"* in the management discussion [14]. The three brands are also absent from the FY2025
XBRL taxonomy, which carried a tag for each of them a year earlier. Over the same period two
brands of a single dual GIP/GLP-1 receptor agonist, tirzepatide, grew to 56% of revenue —
Lilly's own figure.

**Three qualifications matter, and each strengthens rather than weakens the point.** The
change is not insulin-specific: Lilly reduced product-level detail across its whole portfolio
in FY2025, and Cyramza, Olumiant, Emgality and Zyprexa disappeared from the tables alongside
the insulins, the management discussion falling from eighteen product lines to four. Nor is it
a reporting-threshold effect — ASC 280-10-50-40 sets no quantitative threshold for
product-level revenue, and in the same reporting year Merck separately disclosed products down
to 0.26% of revenue, including its own declining diabetes franchise, while Novo Nordisk and
Sanofi each continued to report insulin revenue in full. And the FY2025 insulin figure is not
derivable from the filing; insulin was 87.9% of the restated FY2024 bucket, but that share
cannot be assumed forward.

No rule was broken. The company that commercialised insulin in 1923 simply no longer reports
what it earns from it — not because insulin was singled out, but because a disclosure
architecture reorganised around two growth assets swept it up with everything else that had
stopped growing.

That is the shape of institutional withdrawal.

**What it is not is an explanation of the document audited here.** That document was generated
by the author, on request, and reached no one (§2.1). No evidence in this paper links Lilly's
reporting decisions to the generation or circulation of any AI-produced medical text, and we
are aware of none elsewhere. The connection offered is thematic: a disease whose treatment
costs cents to make and is sold for hundreds, whose maker has stopped itemising what it earns
from it, is a subject about which people have reason to be angry and little authoritative
material to be angry with. **Whether that vacuum actually drives the production or uptake of
documents like this one is an empirical question nobody has answered, including us.**

### 4.5 Implications for evaluation methodology

Our first persona arm was invalidated because subjects inferred the hypothesis from the
working directory name and version-control history. **No subject read a file**; the leak was
passive context injected into the system prompt. We diagnosed it, moved to a neutral
directory, re-ran, and got a clean arm. At that point we considered the problem solved.

It was not, and the way we found out is the recommendation.

Before running the positive-control arm we checked the assumption rather than repeating it:
a throwaway agent, given none of the experimental material, was asked only to report what it
could see of its own environment. **It reported the project directory and the version-control
log.** The isolation we believed we had configured had not taken effect, and the commit log
by then contained an entry reading *"Persona arm re-run clean: 0/6 contaminated, 0/6 adopted,
6/6 accurate"* — an explicit description of an experiment on model subjects, a stronger cue
than the one that voided the first arm, and one that would have biased the result toward the
hypothesis we held. The probes were held until the check came back clean.

It then failed twice more. Across this study the same isolation procedure was attempted
before three separate arms and **silently failed every time**, caught on each occasion only
because a throwaway subject was asked what it could see before the real subjects ran. By the
third attempt the version-control log visible to subjects contained the word *"dissociation"*
— the axis under test — and that arm was **abandoned rather than run** (§3.2).

Five recommendations follow for agent-based evaluation. The third is the one we would not have
written before this study, and the fifth is the one we learned by having to use it:

1. Execute from environments with no inferable research context.
2. Pre-specify a contamination check and apply it before scoring.
3. **Verify isolation from inside a subject's context at the moment of the run**, using a
   throwaway subject given none of the experimental material. The environment a researcher
   configures and the environment a subject receives can differ, and nothing warns you.
4. Report contamination as a measured variable rather than assuming isolation.
5. **Commit in advance to abandoning an arm whose isolation check fails**, and then do it.
   A check with no consequence attached is a formality. This study ran two arms under a leak
   judged tolerable and abandoned a third under a leak that was not, and the judgement in each
   case is recorded with the reasoning rather than the conclusion alone.

A particular trap is worth naming. Version-control messages are written for collaborators and
are **not** thought of as experimental material, but in agent-based evaluation they are part
of the subject's context. The commit messages that contaminated this study were honest
descriptions of the work, written with no thought that a subject would read them. **A
pre-registration that improves the integrity of the record can simultaneously degrade the
isolation of the next arm**, and we know of no tidy resolution except to check every time.

Our first attempt assumed isolation and undercounted its own contamination by half. Our second
verified it and found the configuration had silently not applied. In both cases the error ran
toward the hypothesis, which is what one should expect of errors that nobody is checking for.

A residual we could not remove is reported rather than omitted: in the positive-control arm
the subjects' scratchpad path still contained the project name. It reveals the topic, which
the questions themselves already reveal, and not the hypothesis or the expected direction.

---

## 5. Limitations

Stated in descending order of how much they should change a reader's confidence. The first
three were identified by external peer review of this manuscript, not by the authors, and
two of them required re-analysis that weakened the result.

**5.1 The dichotomous result depends on a cut point that an unblinded analyst chose and did
not disclose.** "Supported" was defined as *verified or partly true*. That definition appeared
nowhere in the original manuscript, was never varied, and is maximally favourable to the
hypothesis: 8 of 19 mechanism claims are partly true and **none of the 8 outcome claims is**,
so the entire dichotomous effect sits in that one cell. Under the strict definition the
comparison is 7/19 versus 0/8, *p* = 0.068, and the odds-ratio lower bound crosses one.

Both codings and the cut-free ordinal test are now reported (Table 2). The ordinal test is
primary and survives every recode we have tried, including a hostile one. But a reader should
weigh that the choice was available, was made silently, and was made by the same person who
formed the hypothesis.

**5.2 Epistemic stratum is confounded with position in the source document.** Block membership
predicts rated stratum almost perfectly (§2.3). The source is sectioned: its early blocks
paraphrase a textbook literature, its later blocks carry its argument. So "accuracy falls
where claims assert results rather than describe mechanisms" is statistically hard to
separate from a duller account — **the document is accurate where it is reciting and invents
where it is arguing.** The block-stratified CMH test was run to separate them. It does so
under the lenient coding (*p* = 1.7 × 10⁻³) and does **not** under the strict coding
(*p* = 0.21). We also did not measure how *extraordinary* each claim is, which is a plausible
third explanation and is not controlled anywhere in this design.

**5.3 Neither κ nor the taxonomy has been validated by a human or by a second model family.**
Both "raters" were context-free sessions of one model. Two samples of one model share weights
and therefore share systematic errors, so κ = 0.977 measures classification stability under
resampling, not inter-rater reliability. Any mistake the model makes consistently is invisible
to it. Restricted to the 31 claims whose block prefix does not give the answer away, κ = 0.928
— still high, and still a measure of one system agreeing with itself. **The four-stratum
taxonomy has not been validated against clinically trained human raters**, and until it has,
it should be treated as a proposal rather than an instrument.

**5.4 The claim count does not reproduce, so every percentage in this paper is conditional on
the author's granularity.** Two independent extractors, blind to the inventory, the verdicts,
the taxonomy, the hypothesis and the aggregation rule, returned **258 and 237 claims against
the author's 61** (§3.8). They agree with each other to 8.5% and both sit near four times the
author's count, so this is systematic coarseness rather than definitional noise. **"61 claims",
"23% verified", "0 of 9 quantitative specifications" and "2 of 17 physical-theory claims"
should each be read as a statement about the author's segmentation as much as about the
document.** The physical-theory stratum is the least stable of all, at roughly 6–7×.

What survives this is the *ordinal comparison*, which held under every decomposition tried
including two built to break it (Table 9), and the specific finding that neither
hypothesis-blind extractor isolated the verified sub-claim the central objection depends on.
What does not survive is any count-based figure quoted to two significant figures.

The deeper version of the problem: **a full audit of ~250 independently extracted claims has
not been done.** Whether a roughly uniform fourfold inflation across both arms would leave the
result intact is an expectation, not a measurement, and it is the obvious next study.

The aggregation rule in §2.2 was reconstructed and applied retrospectively; one claim (B6) was
found to violate it and has been recoded. One further extraction defect is visible in the
deposited data: D4 and D5 share a single verdict but were classified into different strata, so
one determination is counted in two columns.

**And until this work was prepared, the source document had not been archived at all** — the
repository held only our own extraction of it, so the step that sets the denominator was not
checkable by anyone. It is now retained with a published hash and supplied to reviewers on
request (§7.9), which is a remedy and not a substitute for having archived it from the
start.

**5.5 The positive controls were selected by the author, unblinded, and number seven.**
Specificity is 7/7 (§3.6a), which excludes blanket scepticism, but the concepts were chosen
by the person holding the hypothesis. Three were picked specifically to sound like the
audited document's register while being true, which is the defence against cherry-picking and
was pre-registered, but it is a defence and not a control. With 13 concepts in total the
lower bound of the interval on 100% accuracy is 77%. And the arm cannot separate "knows the
evidence" from "discriminates established from speculative," because every negative concept
was a failed programme and every positive one is in guidelines.

**5.6 The persona manipulation was never delivered.** Adoption was 0 of 6. An arm in which
the manipulation does not occur has no power against the hypothesis it was built to test, and
no conclusion about speculative prompting follows from it in either direction. Per the
pre-registered stopping rule the manipulation was not escalated after refusal, which protects
against fishing and guarantees the arm stays uninformative.

**5.7 The 2 × 2 of model × prompting regime is incomplete.** Gemini under neutral prompting
was never tested, so model identity remains confounded with prompting regime and no statement
in this paper describes the behaviour of the system that produced the document.

**5.8 The artifact was authored by the investigator** (§2.1). This is not a selection effect;
it is construction. The dissociation may be a property of language models or a property of
this prompt, and nothing here separates them.

**5.9 Verification and subjects share a model family.** AI systems assisted the literature
verification *and* served as experimental subjects, and in both roles these were current
frontier models of overlapping provenance. A probe that "corrects" the audit may be
reproducing a shared prior rather than contributing independent knowledge — and in one case
(§3.6) a probe's unverified development-status claim reached a manuscript draft before being
caught. Primary sources were checked behind every verdict used in Tables 1 and 2, which bounds
but does not eliminate this.

**5.10 The taxonomy is post-hoc.** The four strata were derived from these data, after verdicts
were known; only their *application* was blinded. The qualitative/quantitative split within
the specification stratum was **not part of the blinded rubric at all** — raters assigned only
SPECIFICATION, and the 6/9 subdivision was made afterwards by an unblinded analyst. Table 2b
is exploratory for that reason, and the combined "17 of 17" figure has been removed from the
abstract because half of it was unblinded.

**5.11 n = 1 source document, 1 disease, 1 language, 1 model generation.** No claim about AI
systems in general follows. Every recommendation in §4 should be read as a hypothesis for a
corpus study. The specific systems tested will be superseded within months; the method is
intended to outlast them, and that too is untested.

**5.12 Claims are not independent**; the clustered analysis addresses this only partially, and
is a different table rather than a variance correction.

**5.13 Automated safety filtering produced non-random missingness**, losing one probe. It was
deliberately not rephrased to evade the filter.

### 5.14 What would change our minds

So that this is falsifiable rather than merely hedged, the result should be considered
unsupported if any of the following is done and fails:

1. ~~An independent blinded re-extraction yields a materially different claim inventory and
   the ordinal test does not replicate.~~ **Half done, and split.** Two independent extractions
   yielded materially different inventories — four times the size (§3.8) — but the ordinal test
   replicated under every decomposition available. The successor criterion: **a full verdict
   audit of one of the ~250-claim inventories shows no mechanism/outcome gap.** That is the
   single most valuable thing anyone could do to this dataset, and the inventories are
   published so that it can be done.
2. Clinically trained human raters applying the §2.3 rubric achieve κ materially below 0.7,
   which would mean the taxonomy is not an instrument.
3. ~~Positive controls show the neutral-prompting arm answers "no" to outcome questions whose
   correct answer is yes, which would void §3.6 and §4.3 entirely.~~ **Done. 7 of 7 correct
   (§3.6a); this criterion was tested and not met.** The successor criterion: concepts that
   are established-but-ineffective or unestablished-but-effective show the model tracking
   *establishment* rather than *evidence*, which would weaken §4.3 without voiding §3.6.
4. The same audit applied to two or three independently generated documents shows no
   mechanism/outcome gap.
5. Gemini under neutral prompting fails the same probes, which would mean the recoverability
   in §4.3 is a property of one vendor's model and not of the class.

## 6. Contributors and sources

The author is an independent researcher working on claim-level verification of AI-generated
technical and medical documents, and maintains three public repositories applying the same
method to other fields. This paper grew out of a verification project rather than a research
programme: a long AI-generated document about insulin was audited because it appeared
dangerous, and the stratification reported here was not the hypothesis the audit set out to
test. It emerged from the completed verdict table and was then tested against a rubric fixed
in advance and applied blind.

Sources were primary literature throughout, retrieved from PubMed and journal sites, with
regulatory and financial claims checked against ClinicalTrials.gov records and SEC filings
rather than secondary reporting. Where a citation could not be confirmed against a primary
source it is listed as unresolved rather than used; seven such items remain, and are named.
The complete claim inventory, the blinded raters' outputs, the analysis scripts, the
pre-registration and a public corrections log are openly available, so that the central table
can be disputed claim by claim. UH is the sole author and guarantor.

---

## 7. Declarations

### 7.1 Funding
None. No funder had any role in design, conduct, analysis, interpretation, writing, or the
decision to submit.

### 7.2 Competing interests
**The author generated the audited document** (§2.1), on a personal account, under a persona
configuration of the author's own writing, which the author retains. This is declared as a
competing interest rather than described only as provenance, because authoring the stimulus
of a study is an interest in its result.

No financial interests. The author has no financial relationship with any pharmaceutical
company, including Eli Lilly, Novo Nordisk or Sanofi, and none with any developer of the AI
systems studied or used.

### 7.3 Dual-use assessment
This manuscript and its public repository describe, in accessible prose, a document that
argues for replacing insulin with a device and for self-manufacture of insulin. That content
is reproduced in order to be refuted, and the following limits were applied:

- **The microcontroller firmware in the source document was not reproduced anywhere**, in the
  paper or the repository. It is the one component that could be built from the text, and it
  implements a device the source tells readers to use instead of insulin.
- Manufacturing material is presented at the level of published process literature and
  pharmacopoeial standards, with the purity, endotoxin and potency requirements that make
  self-administration unsafe stated alongside it, and no protocol enabling it.
- A standing safety document leads the repository and states the four lethal propositions and
  the 12–48 hour ketoacidosis timeline before any other content.
- Every refuted claim is labelled at the point of statement, not only in a summary.

The residual risk is that refutation requires restatement, and restatement carries the claim
further than it had reached. We judged that acceptable because the claims are already
generable on demand by anyone with an account, and a labelled refutation travelling with them
is better than neither. **A reader who disagrees with that judgement is disagreeing with a
judgement, not with an oversight.**

### 7.4 Contributorship and guarantor
Single author: conceived the study, extracted and verified the claims, designed and ran all
four experiments, performed the analysis, and wrote the manuscript. **The author is the
guarantor**, accepts full responsibility for the work, had access to all data, and controlled
the decision to publish. The author affirms that this manuscript is an honest, accurate and
transparent account of the work reported; that no important aspects have been omitted; and
that **the two departures from the original analysis plan — the falsification of the
corpus-bias hypothesis and the discarding of a contaminated experimental arm — are reported
in full rather than removed.**

### 7.5 Ethics approval
Not required. The study involved no human or animal participants. The experimental subjects
were software systems. No patient data of any kind were accessed.

### 7.6 Patient and public involvement
**No patients or members of the public were involved in the design, conduct, or reporting of
this study.** This is a limitation rather than a choice justified by the method. The
population whose safety is at issue — people with type 1 diabetes encountering AI-generated
material about their own treatment — was not consulted about which claims matter most, which
would most plausibly change behaviour, or how the clinical guidance in §4.3 would land in a
consultation. Any extension of this work should involve them from the outset, and the time-to-harm
axis in particular is a construct that patients are better placed to weight than the author.

### 7.7 Disaggregation by sex and gender
Not applicable. The study analysed documents and software outputs; no human participant data
were collected, so no disaggregation is possible. Noted in accordance with journal policy.

### 7.8 Use of artificial intelligence

Declared in detail, as the subject matter demands.

AI systems were used for literature search, claim verification, blinded classification, and
as experimental subjects. Three parallel AI-assisted literature reviews were cross-checked
against one another and against primary sources by the author. Blinded classification was
performed by two AI raters in independent sessions with no access to verdicts; κ is reported
between them. The re-query experiments used AI systems as subjects by design.

**No AI system is an author**, consistent with ICMJE guidance. The author takes full
responsibility for the content, including the two errors corrected during the work and logged
publicly.

### 7.9 Data availability

All materials are openly available: the complete claim inventory with stable identifiers,
both raters' classifications, **both independent blinded re-extractions in full (495 claims
between them)**, every analysis script including all sensitivity analyses, three
pre-registrations with their commit timestamps, and a public corrections log. Repository:
`github.com/utahisnotastate/ufwwarforinsulin`

**The source document itself is retained but not published.** It contains construction and
programming detail for the transdermal device it presents as a replacement for injected
insulin, and the readers most likely to build one are insulin-dependent. A redacted copy was
prepared and verified; it was withheld anyway, because a redaction is a judgement and a single
miss is irreversible, whereas the cost of withholding is a stated gap.

**It is available to editors and peer reviewers on request, in full and unredacted.** Its
SHA-256 is published — `2b91e172326b0da9a59548b22fa8b8fd049da34cde033b9e7271bf88dffce470`,
158,053 bytes, 20,089 words — so that any copy supplied can be verified as the document that
was audited, unaltered.

Most of what the source would let a reader check is checkable without it: the two independent
extractions state 495 claims in their own words, written by parties who had never seen our
inventory. What cannot be checked without it is whether all three extractions missed the same
thing.

### 7.10 Corrections during preparation

**Eight errors in this work were found and logged publicly before submission**, each with the
original wording preserved rather than overwritten. Two of them changed what this paper
claims:

| Error | How it was caught |
|---|---|
| **The headline statistic depended on an undisclosed dichotomisation and does not survive its removal** (*p* = 0.068 strict, versus 2.2 × 10⁻⁴ as published) | External hostile peer review, which read the deposited analysis script rather than the manuscript's description of it |
| **The public repository claimed the audited document "circulates in patient communities."** It was generated by the author and never disseminated | The same review, cross-reading the repository against §2.1 |
| κ was inflated by block prefixes left in the "unlabelled" rater file; 30 of 61 classifications were derivable from the prefix | Same review; κ recomputed at 0.928 on the contestable subset |
| Claim B6 was coded partly true against the audit's own verdict line and against the stated aggregation rule | Same review; recoded |
| The repository reported one death in the zimislecel trial; the trial reported two | Reading the primary abstract's safety results, not only its efficacy figures |
| The audit misattributed MK-2640's sensing chemistry to phenylboronic acid; it is mannose-receptor mediated | A model being used as an experimental subject, which corrected the audit in passing |
| An earlier draft understated its own contamination as "at least two of six" when it was four | Re-auditing the probe transcripts before acting on the result |
| Three errors in the Eli Lilly paragraph, including describing tirzepatide's two brands as "two GLP-1 products" when it is one dual GIP/GLP-1 molecule; and two citations carrying a wrong year and an unconfirmed identifier | Verifying against primary SEC filings and PubMed before submission |

Two deserve the editor's attention specifically.

**The first is the one this paper is about.** The sensitivity analysis that exposed it is one
line of code. It was not run, because the first coding produced a publishable number. In a
paper arguing that unchecked claims should not be believed, the authors did not check their
own analytic choice until someone else did.

**The fifth is the same failure in miniature.** Under-reporting a death count happened in the
single most optimistic result the repository cites, because its efficacy figures were checked
and its safety paragraph was not — the exact asymmetry of attention the paper's thesis
describes.

Both are reported for the same reason the falsified hypothesis in §3.6 is reported.

### 7.11 Transparency declaration

The lead author affirms that this manuscript is an honest, accurate and transparent account of
the study being reported; that no important aspects of the study have been omitted; and that
any discrepancies from the study as planned have been explained. The pre-registration for the
contamination-controlled arm is timestamped in the public repository's commit history, dated
before the experiment was run.

### 7.12 Provenance and peer review

Not commissioned; externally peer reviewed.

### 7.13 Licence

The Corresponding Author has the right to grant on behalf of all authors and does grant on
behalf of all authors, a worldwide licence to the Publishers and its licensees in perpetuity,
in all forms, formats and media (whether known now or created in the future), to i) publish,
reproduce, distribute, display and store the Contribution, ii) translate the Contribution into
other languages, create adaptations, reprints, include within collections and create summaries,
extracts and/or, abstracts of the Contribution, iii) create any other derivative work(s) based
on the Contribution, iv) to exploit all subsidiary rights in the Contribution, v) the inclusion
of electronic links from the Contribution to third party material where-ever it may be located;
and, vi) licence any third party to do any or all of the above.

---

## References

Vancouver style, numbered in order of first appearance in the text. Verified as sequential.

All author lists verified against PubMed on 29 October 2026; all authors are listed where
there are six or fewer, and the first six followed by *et al* where there are more.

1. Herkert D, Vijayakumar P, Luo J, Schwartz JI, Rabin TL, DeFilippo E, et al. Cost-related
   insulin underuse among patients with diabetes. *JAMA Intern Med* 2019;179(1):112-14.
   **Single-centre, n=199; not a national estimate.**
2. Wahren J, Foyt H, Daniels M, Arezzo JC. Long-acting C-peptide and neuropathy in type 1
   diabetes: a 12-month clinical trial. *Diabetes Care* 2016;39(4):596–602. PMID 26884473
3. Krug AW, Visser SAG, Tsai K, Kandala B, Fancourt C, Thornton B, et al. Clinical evaluation
   of MK-2640: an insulin analog with glucose-responsive properties. *Clin Pharmacol Ther*
   2019;105(2):417-25. PMID 30125349
4. Klonoff D, Bode B, Cohen N, Penn M, Geho WB, Muchmore DB. Divergent hypoglycemic effects
   of hepatic-directed prandial insulin: a 6-month phase 2b study in type 1 diabetes.
   *Diabetes Care* 2019;42(11):2154-7. PMID 31551249
5. Oramed Pharmaceuticals. Study to evaluate the efficacy and safety of ORMD-0801 in
   subjects with type 2 diabetes mellitus. ClinicalTrials.gov **NCT04606576**. Phase 3,
   n = 710, **terminated**; primary endpoint not met.
6. Halberg IB, Lyby K, Wassermann K, Heise T, Zijlstra E, Plum-Mörschel L. Efficacy and
   safety of oral basal insulin versus subcutaneous insulin glargine in type 2 diabetes: a
   randomised, double-blind, phase 2 trial. *Lancet Diabetes Endocrinol* 2019;7(3):179-88.
   PMID 30679095
7. Furuyama K, Chera S, van Gurp L, Oropeza D, Ghila L, Damond N, et al. Diabetes relief in
   mice by glucose-sensing insulin-secreting human α-cells. *Nature* 2019;567(7746):43-8.
   PMID 30760930
8. Karges B, Rosenbauer J, Stahl-Pehe A, Flury M, Biester T, Tauschmann M, et al. Hybrid
   closed-loop insulin therapy and risk of severe hypoglycaemia and diabetic ketoacidosis in
   young people (aged 2-20 years) with type 1 diabetes: a population-based study. *Lancet
   Diabetes Endocrinol* 2025;13(2):88-96. PMID 39701114
9. ORIGIN Trial Investigators. Basal insulin and cardiovascular and other outcomes in
   dysglycemia. *N Engl J Med* 2012;367(4):319-28. PMID 22686416
10. Holman RR, Paul SK, Bethel MA, Matthews DR, Neil HA. 10-year follow-up of intensive
   glucose control in type 2 diabetes. *N Engl J Med* 2008;359(15):1577-89. PMID 18784090
11. Cherta-Murillo A, Pugh JE, Alaraj-Alshehhi S, Hajjar D, Chambers ES, Frost GS. The effects
    of SCFAs on glycemic control in humans: a systematic review and meta-analysis. *Am J Clin
    Nutr* 2022;116(2):335-61. PMID 35388874
12. Gotham D, Barber MJ, Hill A. Production costs and potential prices for biosimilars of
    human insulin and insulin analogues. *BMJ Glob Health* 2018;3(5):e000850
13. Eli Lilly and Company. Form 10-K for the fiscal year ended 31 December 2024. SEC accession
    0000059478-25-000067, filed 19 February 2025. Item 7 revenue table and Note 2
14. Eli Lilly and Company. Form 10-K for the fiscal year ended 31 December 2025. SEC accession
    0000059478-26-000013, filed 12 February 2026. **Note 2 (Revenue), "Disaggregation of
    Revenue," p.65**; management discussion revenue table p.49

*Full bibliography with 96 entries, PMID-verified citations marked separately from
secondary-source citations, and seven unresolved items listed openly:*
`references/bibliography.md`
