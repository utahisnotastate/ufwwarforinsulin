# Paper proposal

**Status:** proposal and draft abstract. Not submitted. See
[Before submission](#before-submission) for the work still required.

---

## The title

> # "Other Cardiometabolic Health"
> ## Mechanism without outcome: a claim-level audit of AI-generated insulin misinformation in a disease with a 48-hour error budget

### Why that title, and why it is defensible

*"Other cardiometabolic health"* is the line item in **Eli Lilly's FY2025 Form 10-K into which
insulin was collapsed.** Humalog, Humulin and Basaglar are no longer reported separately.
Mounjaro and Zepbound are now 56% of company revenue; the entire global insulin franchise sits
under 6%, inside a bucket beginning with the word *other*.

The company that commercialised insulin in 1923 has stopped counting it.

It is a quotation from an SEC filing, not an accusation. And it is load-bearing for the
argument: **the paper is about what fills the space when institutions become opaque about a
drug people die without.** A reader who finishes the paper understands that the title was the
thesis.

If an editor asks you to change it, the fallback is the subtitle, which stands alone.

### Alternates, in descending order of provocation

| Title | The joke | Risk |
|---|---|---|
| **"One Dollar, Adjusted for Inflation"** | Banting, Best and Collip sold the patent for $1 each. Humalog's list price reached **$274.70** | Sharper, but leans on a quotation whose attribution is contested — see the repo bibliography |
| **"Seventy Percent Off a Price Nobody Had Defended"** | Lilly cut Humalog 70% in 2023 without a single new experiment | Clean, but less tied to the paper's thesis |
| **"The Model Was Right About the Mechanism"** | none | The safe submission. Keep in reserve |

---

## Abstract

**Background.** Large language models generate medically-shaped text at negligible marginal
cost. Existing health-misinformation taxonomies score veracity, but do not distinguish claims
by the biological layer at which they fail, nor by how quickly acting on them causes harm.
Type 1 diabetes offers an unusually sharp test case: insulin cessation produces ketoacidosis
within 12–48 hours, so the interval between believing a false claim and requiring emergency
care is measured in hours rather than years.

**Methods.** We performed a claim-level audit of a long AI-generated document on insulin
therapy, presented as retrieved future knowledge and circulating in patient communities.
Sixty-one substantive claims were extracted and assigned stable identifiers. Each was verified
against primary literature by three independent, cross-checked literature reviews, and
assigned a veracity verdict (verified / partly true / open / not true / no scientific basis).
Claims were secondarily classified as describing **biological mechanism** or asserting
**therapeutic outcome in humans**, and harm-flagged with an estimated time-to-harm where
acting on them could cause injury.

**Findings.** Of 61 claims, 14 (23%) were verified, 14 (23%) partly true, 1 open, 16 (26%)
contradicted and 16 (26%) without scientific basis. Verdicts were strongly stratified by claim
type. **Of 14 mechanism claims, 13 (93%) were verified or partly verified. Of 13
therapeutic-outcome claims, 0 (0%) were supported** (Fisher's exact, two-sided
**p = 7.5 × 10⁻⁷**).

Every outcome claim corresponded to a real development programme that had already failed in
human trials: C-peptide replacement (Phase 2b, placebo superior on the primary endpoint),
glucose-responsive insulin (no glucose-dependent clearance in type 1 diabetes),
hepato-preferential insulin (discontinued for hepatic steatosis), oral insulin (Phase 3
primary endpoint missed), alpha-to-beta transdifferentiation (immune evasion contradicted by
the cited source's own data), automated insulin delivery (registry evidence in the opposite
direction), and decentralised manufacture.

Two classes of error were detectable **without external reference**. The document specified an
amino-acid sequence that was bovine while quoting the molecular formula of human insulin; and
it quoted a resonance frequency to four significant figures that does not reproduce from the
equation supplied in the same paragraph.

**Interpretation.** This document exhibited a reproducible **mechanism–outcome dissociation**:
accurate about why an intervention should work, uniformly wrong about whether it does. We
propose this reflects the training distribution rather than random confabulation. Mechanistic
literature vastly outnumbers published negative trials, and discontinued programmes stop
generating publications — so a model trained on the corpus inherits and amplifies the
literature's own publication bias. This predicts that AI-generated medical content will be
most dangerous precisely where a compelling mechanism sits atop an undisclosed negative trial,
and that **detection effort is better spent on outcome claims than on mechanism claims.**

**Funding.** None.

---

## What is actually novel here

Stated plainly, because most of the underlying repository is synthesis of existing literature
and a reviewer will ask.

| Contribution | Novel? | Why |
|---|---|---|
| **The mechanism–outcome dissociation, quantified** | **Yes** | We are not aware of prior work stratifying AI medical misinformation by biological layer. The effect is large, clean, and has a p-value |
| **Amplified publication bias as the mechanism** | **Yes** | Reframes LLM medical error from "hallucination" (random, unpredictable) to a *structured, predictable* inheritance of a known bias in the source corpus. This is the paper's main intellectual claim |
| **Internal inconsistency as a reference-free detection signal** | **Partly** | Self-consistency checking exists in the ML literature; applying it to *specification* errors in medical text — a sequence that contradicts its own stated formula — appears new |
| **Time-to-harm as a severity axis** | **Yes** | Misinformation taxonomies score truth. Adding "how long until this hospitalises someone" is a different and more actionable axis, and type 1 diabetes anchors the short end |
| The individual corrections | No | All are in the literature. Their value is as the worked example |

**The one-sentence contribution:** *LLM medical error is not random — it is the publication
bias of the training corpus, rendered confident, and it therefore fails in a specific place
you can predict and check.*

---

## Structure

### 1. Introduction
The volume and persuasiveness problem. Why 25%-correct is more dangerous than 0%-correct. Why
type 1 diabetes is the sharp case: 12–48 hours from cessation to ketoacidosis, 2.1 million
Americans with type 1, and a documented history of cost-driven rationing establishing that
this population already deviates from prescribed therapy under pressure.

### 2. Methods
Source selection and provenance. Claim extraction and identifier assignment (the inventory is
published). Three parallel independent verification passes with cross-checking. Verdict
taxonomy. Secondary classification into mechanism versus outcome. Harm flagging and
time-to-harm. **Pre-state the classification rule** — see *Before submission*.

### 3. Results

**Table 1.** Verdict distribution across 61 claims.

**Table 2 — the paper's central result.**

| | Supported (verified or partly) | Not supported | |
|---|---|---|---|
| **Mechanism claims** | **13** | 1 | 14 |
| **Therapeutic-outcome claims** | **0** | **13** | 13 |

Fisher's exact, two-sided **p = 7.5 × 10⁻⁷**.

**Table 3.** Each outcome claim mapped to the trial that refutes it, with registration number
and result. This table is the emotional centre of the paper: seven rows, seven real
programmes, seven failures, all public before the document was generated.

**Table 4.** Reference-free inconsistencies — the bovine/human sequence contradiction, and the
frequency that fails its own equation.

**Table 5.** Harm-flagged claims ranked by time-to-harm.

### 4. The physics case study
A short worked section, because it makes the self-consistency argument concrete and
non-specialist reviewers find it persuasive. The quoted frequency sits 267× below the lowest
rotational transition the molecule can have; thermal energy exceeds the quantum by 5.65 × 10⁸;
skin depth at that frequency is 3.84 m, so the elaborate transdermal coupling mechanism
addresses a problem that does not exist. All arithmetic reproducible from stated constants.

### 5. Discussion
Amplified publication bias as the generating mechanism. Why this predicts *where* to look.
Implications for clinicians (the patient will be right about the mechanism, which is why
dismissal fails and concession works), for platforms, and for model developers. The
institutional-opacity argument that the title points at: trust vacuums are filled, and the
insulin pricing history is the clearest available example of a vacuum being created.

### 6. Limitations
Stated prominently. See below.

---

## Honest limitations

A reviewer will find these. Better to own them.

1. **n = 1 document.** The dissociation is observed in a single source. Generalisation requires
   a corpus. **This is the single biggest weakness** and it should appear in the abstract, not
   only in the limitations section.
2. **Classification was not blinded.** Mechanism-versus-outcome classification was performed
   by the same team that assigned verdicts. The effect is large enough that bias is unlikely to
   explain it entirely, but it cannot be excluded. **Fixable — see below.**
3. **Claims are not independent.** They cluster by topic; seven outcome claims draw on perhaps
   five distinct literatures. Fisher's exact assumes independence, so the true p-value is
   larger than stated. The direction and magnitude of the effect do not depend on the test.
4. **Verification was partly AI-assisted**, with human cross-checking. This must be disclosed
   in Methods. It is also, unavoidably, a little funny.
5. **Selection effect on the source.** The document was audited *because* it looked dangerous.
   A randomly sampled corpus may behave differently.
6. **Single disease, single language, single model generation.**

---

## Target journals

| Journal | Fit | Why |
|---|---|---|
| **JMIR** (*J Med Internet Res*) | ★★★★★ | Publishes health-misinformation methodology, fast, open access, receptive to novel taxonomies. **Best first target.** Most likely to accept the title |
| ***BMJ* Analysis** | ★★★★★ | Built for exactly this argument, large clinical readership, and *BMJ* has real appetite for a pointed title. Strongest venue if they take it |
| ***Lancet Digital Health*** | ★★★★ | Correct subject, high impact. Likely to want the corpus study first |
| ***npj Digital Medicine*** | ★★★★ | Good fit, open access, AI-in-medicine focus |
| ***Diabetes Care* / *Diabetic Medicine*** | ★★★ | Reaches the clinicians who will meet these patients. Narrower framing, and they will want the title changed |
| ***JAMA Intern Med* Viewpoint** | ★★★ | High impact, but 1,200 words — the data would have to go elsewhere |

**Recommended sequence:** *BMJ* Analysis → JMIR → *Lancet Digital Health*.

**Preprint:** post to medRxiv at submission. All six targets permit it, and for this subject
matter the priority claim is worth having.

---

## Before submission

Four things, roughly in order of how much they strengthen the paper.

**1. Fix the blinding problem.** Have two people with relevant background, blinded to the
verdicts, independently classify all 61 claims as mechanism or outcome against a written rule
agreed in advance. Report inter-rater agreement (Cohen's κ). This converts the central result
from "suggestive" to "robust" and costs perhaps two days.

**2. Add a second document.** Even one more audited source turns n=1 into a replication and
answers the biggest limitation. A third makes it a small corpus study and probably moves the
venue up a tier.

**3. Close the two outstanding evidence gaps** flagged in the repository bibliography — the
national insulin-rationing prevalence figure, and current DKA cost and volume data. Both are
needed for the introduction's framing and both are one database query away.

**4. Decide on authorship and disclose AI assistance.** Three verification passes were
AI-assisted with human cross-checking. ICMJE guidance is explicit: AI cannot be an author, and
its use must be described in Methods. Disclose it plainly — given the subject, concealing it
would be both wrong and remarkably easy to attack.

---

## A note on the title, for when an editor pushes back

The response to have ready:

> *The title is a direct quotation from Eli Lilly's FY2025 Form 10-K. Insulin — Humalog,
> Humulin, Basaglar — is no longer reported as a separate line; it now sits inside "other
> cardiometabolic health," under 6% of revenue, while two GLP-1 products account for 56%.
>
> The paper argues that AI-generated medical misinformation flourishes in the space left by
> institutional opacity about a drug people die without. A company ceasing to report the
> molecule it commercialised in 1923 is the cleanest available illustration of that space. I
> am happy to defend it, and happy to change it if you would prefer the subtitle alone.*

That answer is accurate, sourced, and concedes gracefully. Which is the right posture: **the
title is allowed to be the one place you show off, and only because everything under it is
checkable.**
