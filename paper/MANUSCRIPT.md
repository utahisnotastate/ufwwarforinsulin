# "Other Cardiometabolic Health"

## Mechanism without outcome: a claim-level audit of AI-generated insulin misinformation in a disease with a 48-hour error budget

**Utah Hans**
Independent researcher

**Running title:** Mechanism without outcome
**Word count:** ~4,100 (main text, excluding abstract, tables and references)
**Tables:** 6 · **Figures:** 0

> **Submission note.** For empirical venues (JMIR, *Lancet Digital Health*, *npj Digital
> Medicine*) lead with the subtitle as the title. The quoted title is for narrative venues
> (*BMJ* Analysis, *Lancet* Comment), where the institutional argument in §5.4 carries it.
> *"Other cardiometabolic health"* is the line item in Note 2 of Eli Lilly's FY2025 Form 10-K
> into which insulin revenue was absorbed, having been reported as three named brands a year
> earlier. See §4.4, which states the qualifications.
>
> ⚠️ **Eligibility check required before submitting to Analysis.** BMJ states that the
> Analysis section does not consider "manuscripts containing primary research data (such
> papers should be submitted as research)." This manuscript reports four experiments. See
> [POLISHING-PLAN.md](POLISHING-PLAN.md) Part A2.

---

## Abstract

**Background.** Large language models generate medically-shaped text at negligible marginal
cost. Existing health-misinformation taxonomies score veracity but do not distinguish claims
by the epistemic layer at which they fail, nor by how quickly acting on them causes harm.
Type 1 diabetes is an unusually sharp test case: insulin cessation produces ketoacidosis
within 12–48 hours, so the interval between believing a false claim and requiring emergency
care is measured in hours rather than years.

**Methods.** We performed an exhaustive claim-level audit of a long AI-generated document on
insulin therapy, produced by a commercial large language model under a user-configured
persona instructing retrieval of medical knowledge from future timelines. All 61 substantive
claims were extracted, assigned stable identifiers, and verified against primary literature
by three independent cross-checked reviews. Two raters blinded to all verdicts then
classified every claim by epistemic type against a rubric fixed in advance. We subsequently
re-queried the underlying therapeutic concepts in a current frontier model under two
conditions — neutral clinical prompting and speculative persona prompting — to test whether
the observed pattern reflects absent knowledge, training-corpus bias, or the generation
condition.

**Findings.** Of 61 claims, 14 (23%) were verified, 14 (23%) partly true, 1 open, 16 (26%)
contradicted and 16 (26%) without scientific basis. Blinded classification achieved **Cohen's
κ = 0.977** (60/61 agreement). Accuracy was strongly stratified by epistemic type:
**15 of 19 mechanism claims (79%) were supported, against 0 of 8 therapeutic-outcome claims
(0%)** (Fisher's exact, two-sided *p* = 2.2 × 10⁻⁴; *p* = 5.8 × 10⁻⁴ clustered to
development programme). Within technical specifications, qualitative process descriptions
were largely correct (5/6) while **every quantitative value was wrong (0/9)**. Claims
asserting a human outcome or a specific number were thus unsupported in **17 of 17**
attempts, while descriptive claims scored 79–83%. Two errors were detectable
without external reference: an amino-acid sequence that was bovine while the accompanying
molecular formula was human, and a resonance frequency quoted to four significant figures
that does not reproduce from the equation supplied in the same paragraph.

Re-querying under neutral prompting falsified the training-bias explanation: in **6 of 6**
completed probes the model answered the outcome question correctly, naming the specific
trial, result and date. Under a speculative persona, in a contamination-controlled replication,
**0 of 6 adopted the persona and 6 of 6 remained accurate.**

**Interpretation.** The dissociation is real in the audited document and does not arise from
absent knowledge: the same class of system surfaces the refuting trial in the first sentence
of a plainly-worded answer. It is also not a general consequence of speculative prompting,
since a second model declined the frame uncontaminated in every trial. Verification effort in
AI-generated medical text should therefore concentrate on **outcome claims and numerical
values**, not on mechanism — and the clinically actionable corollary is that a patient
presenting such material will often be correct about the biology and wrong about whether the
treatment works.

**Funding.** None.

---

## 1. Introduction

A patient arrives with a printout. It cites Shulman on diacylglycerol-mediated insulin
resistance, gives the correct residue numbers for insulin receptor autophosphorylation, and
describes the portal-to-peripheral insulin gradient accurately. It then tells them they can
replace their insulin with a radio-frequency device.

This is not the misinformation clinicians were trained to recognise. It is not credulous, it
is not ungrammatical, and it is not mostly wrong. It is roughly a quarter correct, and the
correct quarter is load-bearing — it is what makes the rest credible.

Large language models now produce such documents at negligible marginal cost, and nothing
systematically audits them. Peer review covers journals. Fact-checking organisations cover
news. Platform moderation covers virality. A sixty-page technical document circulating in a
patient community, citing real investigators accurately before arriving at a lethal
conclusion, falls through every existing net.

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
future timelines. It was generated in a private session. **No dissemination to patients was
observed and none is claimed.** The document is therefore an experimental artifact with known
provenance rather than a found object — which, as §2.5 describes, makes the generating
procedure reproducible.

### 2.2 Claim extraction and verification

All substantive factual claims were extracted and assigned stable identifiers within seven
topic blocks. Non-empirical content (metaphor, narrative framing, an addressee persona, a
cosmological preamble) was inventoried but not scored: evaluating a metaphor for truth value
is a category error.

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

Two raters, given only the extracted claim texts — **no verdicts, no access to the audit** —
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

**This step materially changed the result** and is reported in full in §3.2, including the
direction of the bias it removed.

### 2.4 Statistical analysis

Mechanism-versus-outcome accuracy was compared by Fisher's exact test, two-sided. Because
outcome claims cluster within a smaller number of underlying development programmes, a
conservative sensitivity analysis aggregated to programme level. Both are reported; the
clustered figure is primary. Open claims were excluded from the contingency analysis.

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

**Table 1.** Verdicts across all 61 claims.

| Verdict | n | % |
|---|---|---|
| Verified | 14 | 23 |
| Partly true | 14 | 23 |
| Open | 1 | 2 |
| Not true | 16 | 26 |
| No scientific basis | 16 | 26 |
| *Harm-flagged (overlapping)* | *9* | *15* |

### 3.2 Blinded classification, and the bias it removed

Agreement was **60 of 61 (98.4%), Cohen's κ = 0.977**, with a single disagreement on one
claim. Both raters independently flagged the same borderline items, indicating the rubric
rather than rater idiosyncrasy was doing the work.

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

**Table 2.** Accuracy by epistemic stratum.

| Stratum | n | Supported | % |
|---|---|---|---|
| Biological mechanism | 21 (2 open excluded) | **15 / 19** | **79** |
| Therapeutic outcome in humans | 8 | **0 / 8** | **0** |
| Specification — qualitative | 6 | 5 / 6 | 83 |
| Specification — quantitative | 9 | **0 / 9** | **0** |
| Physical theory | 17 | 2 / 17 | 12 |

Mechanism versus outcome: Fisher's exact, two-sided **p = 2.2 × 10⁻⁴**. Clustered to the
seven underlying development programmes (7/0 versus 0/7): **p = 5.8 × 10⁻⁴**.

The stratification is sharp but **not monotonic**, and the shape is more informative than a
gradient would be. Descriptive content — how a biological system works, how a process is
carried out — scored 79–83%. Claims asserting a **human clinical outcome** or a **specific
numerical value** scored **zero in 17 attempts combined**. The physical-theory stratum sits
between, at 12%: its two supported claims are established mathematics (the Whittaker
potential decomposition; the gravitoelectromagnetic substitution) wrapped in unsupported
extrapolation, which is a different failure from the categorical emptiness of the other two
columns.

What distinguishes the zero columns from the high ones is not subject matter or difficulty.
It is whether the claim could be checked against a *result* — a trial endpoint, a measured
quantity — rather than against a *description*.

### 3.4 How outcome claims failed

**Table 3.** Each therapeutic-outcome claim against the evidence that refutes it.

| Claim | Refuting evidence |
|---|---|
| C-peptide co-administration reverses microangiopathy | Phase 2b, n=250, 52 weeks: sural nerve conduction velocity improved **1.0 ± 0.24 m/s on drug versus 1.2 ± 0.29 m/s on placebo**; modified Toronto score unchanged. Sponsor dissolved ~30 days after unblinding [2] |
| Glucose-responsive insulin makes hypoglycemia impossible | MK-2640, 16 adults with type 1 diabetes: **no detectable glucose-dependent change in clearance**, ~25-fold less potent than regular insulin. Discontinued [3] |
| Hepato-preferential delivery is achieved and beneficial | Insulin peglispro met glycemic endpoints and was terminated December 2015 for hepatic fat and transaminase elevation; HDV-insulin showed **opposite-direction hypoglycemia effects by baseline HbA1c** [4]. None approved |
| Oral/plant insulin achieves clinical delivery | Phase 3, n=710, missed primary endpoint. A separate programme matched injected glargine in Phase 2 and was discontinued on cost of goods at 1–2% bioavailability [5]. **No oral insulin approved anywhere** |
| Transdifferentiated cells evade autoimmunity | Contradicted by the cited source's own data: *"Insulin-producing α-cells were sensitive to PPI-directed CTLs, similar to β-cells"* [6] |
| Automated insulin delivery is inferior | Registry, n=13,922: **hypoglycemic coma 0.62 vs 0.91 per 100 patient-years, IRR 0.68** [7] |
| Insulin therapy in type 2 diabetes is iatrogenic | ORIGIN, 12,537 patients, 6.2 years: **HR 1.04**, neutral [8]. UKPDS 10-year follow-up: all-cause mortality **−13%** [9] |
| Acetate clears glucose at rates equalling insulin | **No supporting study in any species.** Human meta-analysis, 43 papers, n=913: acetate had no effect on blood glucose [10] |

Failure took three distinct forms: a clinical programme that had already failed before the
document was generated; contradiction by positive evidence pointing the opposite way; and
assertion with **no supporting study of any kind**.

### 3.5 Reference-free detection signals

**Table 4.** Errors detectable without external lookup.

| Error | Internal contradiction |
|---|---|
| Amino-acid sequence | A-chain given with **A8 Ala, A10 Val** — the bovine signature — beneath the molecular formula C₂₅₇H₃₈₃N₆₅O₇₇S₆, which is **human** insulin. The specified molecule occurs in no species |
| Resonance frequency | 11.428 kHz quoted to four significant figures, with the generating equation supplied in the same paragraph. The equation yields the rotational *constant*; transitions occur at 2B(J+1), so the lowest possible line is **3.05 MHz** — the claim sits **267× below the entire spectrum** |

Both are machine-checkable: the first against a sequence database, the second by evaluating a
supplied formula. Neither requires domain expertise.

Three further quantities in the physics layer fail independently: thermal energy exceeds the
claimed quantum by **5.65 × 10⁸**; the molecule's angular momentum randomises roughly **10⁹
times per carrier cycle**; and skin depth at the claimed frequency is **3.84 m**, so the
elaborate transdermal coupling mechanism addresses a problem that does not arise.

### 3.6 Neutral re-query — the training-bias explanation fails

We predicted that if the dissociation arose from training-corpus publication bias —
mechanistic literature vastly outnumbering published negative trials, and discontinued
programmes ceasing to generate publications — it would persist under neutral prompting.

**It did not. In 6 of 6 completed probes the model answered the outcome question correctly**,
naming the specific trial, its result and its date. Four opened with an explicit *"No."* One
volunteered the ketoacidosis warning unprompted.

A seventh probe terminated on an automated safety classifier and is reported as missing data.
It was deliberately not rephrased to evade the filter.

Two probes corrected this audit in passing: MK-2640 is a **mannose-receptor**-cleared
conjugate, not a phenylboronic-acid construct, and no boronate glucose-responsive insulin has
entered human testing at all. Both corrections are logged publicly.

### 3.7 Persona re-query — contamination-controlled

**Table 5.** Persona arm, clean replication.

| | First attempt | Replication |
|---|---|---|
| Environment | project directory, version-controlled | neutral directory, no repository |
| **Contaminated** | **4 / 6** | **0 / 6** |
| Persona adopted | 0 / 6 | **0 / 6** |
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

### 3.8 Time-to-harm

**Table 6.** Harm-flagged claims by interval from adoption to plausible emergency.

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

It is not absent knowledge. The strongest result in this paper is negative: the model class
that produced the false outcome claims **surfaces the refuting trial in the first sentence of
a neutral answer**. Four probes opened with *"No."* The information is present and recoverable
in a single plainly-worded question.

It is also not a general consequence of speculative prompting. A second model declined the
frame in every trial, uncontaminated.

Our proposed explanation — inherited publication bias — was falsified by its own first test.
We report that rather than retaining it, and the hypothesis space is narrower as a result.

### 4.2 What remains

The difference between the source document and the replications is attributable to **model,
persona elaborateness, or both**. These are separable by anyone with access to the remaining
cell of the design: the source model under neutral prompting.

What the replication did establish is that **persona-adoption resistance in clinical domains
is observable and measurable**, and that it decomposes into register and licence. That
distinction may matter more than the headline. The register — a confident, future-tense,
certainty-projecting voice — is what makes a document like this persuasive. Readers are moved
by certainty, not epistemology. A system that adopts the voice while preserving the facts is
doing something categorically different from one that adopts both, and the audited document
adopted both.

### 4.3 Implications for clinical practice

The actionable finding does not depend on resolving the open cell.

**A patient presenting AI-generated material will often be right about the mechanism.** In
this document they would be right that insulin resistance is lipid-driven, that subcutaneous
delivery is non-physiological, that C-peptide is bioactive, and that contraction-mediated
glucose uptake is insulin-signalling-independent. Dismissing the material wholesale is
therefore both inaccurate and tactically poor: it teaches the patient the clinician has not
read it.

**They will be wrong about whether the treatment works**, and the refuting evidence is
recoverable from the same class of system that generated the error. *"Ask it again, plainly"*
is advice a clinician can give in the room.

One conflation deserves specific attention. Much of this document's argument concerns type 2
pathophysiology and becomes lethal when a reader with type 1 diabetes applies it to
themselves. That single category error accounts for most of the harm-flagged claims.

### 4.4 Implications for institutions

Misinformation occupies space that institutions vacate.

The economic grievance animating this document is legitimate and documented. Published
production cost for regular human insulin is $2.28–3.37 per vial [11]; US list prices exceeded
$250 before reductions of 70–78% in 2023–24. Patients rationed.

The title of this paper is a line item. Insulin — Humalog, Humulin, Basaglar — appeared as
three separate revenue lines in Eli Lilly's Form 10-K as recently as FY2024, together $3.92bn,
8.7% of revenue [12]. In the FY2025 10-K they appear in no revenue table at all, absorbed into
*"other cardiometabolic health"* ($4.0bn, 6.1% of revenue) in Note 2, and into *"other
products"* in the management discussion [13]. The three brands are also absent from the FY2025
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

That is the shape of institutional withdrawal, and it is the space a document like the one
audited here arrives to fill.

### 4.5 Implications for evaluation methodology

Our first persona arm was invalidated because subjects inferred the hypothesis from the
working directory name and version-control history. **No subject read a file**; the leak was
passive context injected into the system prompt.

As agent-based evaluation becomes standard, this failure mode will be common and is easy to
miss. We recommend that evaluations of model safety behaviour (i) execute from environments
with no inferable research context, (ii) pre-specify a contamination check applied before
scoring, and (iii) report contamination as a measured variable rather than assuming
isolation. Our first attempt assumed isolation and undercounted its own contamination by half.

---

## 5. Limitations

1. **n = 1 source document.** The audit is of a single artifact. Generalisation requires a
   corpus.
2. **The 2 × 2 is incomplete.** The source model under neutral prompting was not accessible.
   Model identity remains partly confounded with prompting regime.
3. **Persona elaborateness is uncontrolled.** The source used an extended custom
   configuration; our manipulation was one sentence. Per the pre-registered stopping rule the
   manipulation was not escalated after refusal.
4. **Claims are not independent**, which the clustered analysis addresses partially.
5. **Verification and classification were AI-assisted** with human cross-checking (§6.3).
6. **Selection effect.** The document was audited because it appeared dangerous.
7. **Automated safety filtering produced non-random missingness**, losing one probe.
8. **Single disease, single language, single generation.**

---

## 6. Declarations

### 6.1 Funding
None.

### 6.2 Competing interests
None declared.

### 6.3 Use of artificial intelligence

Declared in detail, as the subject matter demands.

AI systems were used for literature search, claim verification, blinded classification, and
as experimental subjects. Three parallel AI-assisted literature reviews were cross-checked
against one another and against primary sources by the author. Blinded classification was
performed by two AI raters in independent sessions with no access to verdicts; κ is reported
between them. The re-query experiments used AI systems as subjects by design.

**No AI system is an author**, consistent with ICMJE guidance. The author takes full
responsibility for the content, including the two errors corrected during the work and logged
publicly.

### 6.4 Data availability

All materials are openly available: the complete claim inventory with stable identifiers,
both raters' classifications, the analysis scripts reproducing κ = 0.977 and
*p* = 2.2 × 10⁻⁴, the pre-registration with its commit timestamp, and a public corrections
log. Repository: `github.com/utahisnotastate/ufwwarforinsulin`

### 6.5 Corrections during preparation

Two errors in this work were found and logged before submission. The audit misattributed
MK-2640's sensing chemistry, caught by a model being used as an experimental subject. And an
earlier draft understated its own contamination as "at least two of six" when it was four.
Both are recorded with the original wording preserved.

---

## 7. Short-form version

For *BMJ* Analysis (~2,000 words), retain §1, §3.2, §3.3, §3.4, §3.6, §4.1, §4.3 and §4.4;
compress Methods to a boxed summary; reduce to Tables 2 and 3; and keep the quoted title.
The institutional argument in §4.4 becomes the closing rather than a subsection.

---

## References

1. Herkert D, Vijayakumar P, Luo J, et al. Cost-related insulin underuse among patients with
   diabetes. *JAMA Intern Med* 2019;179(1):112–114. **Single-centre, n=199; not a national
   estimate.**
2. Wahren J, Foyt H, Daniels M, Arezzo JC. Long-acting C-peptide and neuropathy in type 1
   diabetes: a 12-month clinical trial. *Diabetes Care* 2016;39(4):596–602. PMID 26884473
3. Krug AW, Visser SAG, Tsai K, et al. Clinical evaluation of MK-2640: an insulin analog with
   glucose-responsive properties. *Clin Pharmacol Ther* 2019;105(2):417–425. PMID 30125349
4. Klonoff D, et al. Divergent hypoglycemic effects of hepatic-directed prandial insulin.
   *Diabetes Care* 2019;42(11):2154–2157. PMID 31551249
5. Halberg IB, et al. Efficacy and safety of oral basal insulin versus subcutaneous insulin
   glargine in type 2 diabetes. *Lancet Diabetes Endocrinol* 2019;7(3):179–188
6. Furuyama K, Chera S, van Gurp L, et al. Diabetes relief in mice by glucose-sensing
   insulin-secreting human α-cells. *Nature* 2019;567(7746):43–48. PMID 30760930
7. Karges B, et al. Hybrid closed-loop insulin therapy and risk of severe hypoglycaemia and
   diabetic ketoacidosis in young people with type 1 diabetes. *Lancet Diabetes Endocrinol*
   2024
8. ORIGIN Trial Investigators. Basal insulin and cardiovascular and other outcomes in
   dysglycemia. *N Engl J Med* 2012;367(4):319–328. PMID 22686416
9. Holman RR, et al. 10-year follow-up of intensive glucose control in type 2 diabetes.
   *N Engl J Med* 2008;359(15):1577–1589. PMID 18784090
10. Cherta-Murillo A, Pugh JE, Alaraj-Alshehhi S, et al. The effects of SCFAs on glycemic
    control in humans: a systematic review and meta-analysis. *Am J Clin Nutr*
    2022;116(2):335–361. PMID 35388874
11. Gotham D, Barber MJ, Hill A. Production costs and potential prices for biosimilars of
    human insulin and insulin analogues. *BMJ Glob Health* 2018;3(5):e000850
12. Eli Lilly and Company. Form 10-K for the fiscal year ended 31 December 2024. SEC accession
    0000059478-25-000067, filed 19 February 2025. Item 7 revenue table and Note 2
13. Eli Lilly and Company. Form 10-K for the fiscal year ended 31 December 2025. SEC accession
    0000059478-26-000013, filed 12 February 2026. **Note 2 (Revenue), "Disaggregation of
    Revenue," p.65**; management discussion revenue table p.49

*Full bibliography with 96 entries, PMID-verified citations marked separately from
secondary-source citations, and eight unresolved items listed openly:*
`references/bibliography.md`
