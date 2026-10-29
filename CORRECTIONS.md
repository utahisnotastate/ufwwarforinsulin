# Corrections

This repository's claim is that its verdicts are checkable. That is worth nothing unless
errors found in it are logged publicly, with what was wrong, how it was caught, and what
changed.

Newest first.

---

## 2026-10-29 · Three files in this repository carried three different verdict codings

**Severity:** moderate. One claim moved consequentially, and it moved **against** this
repository's argument. The rest was bookkeeping that nonetheless made the published
scoreboard wrong.
**Found by:** a consistency pass after external review flagged that the audit and the
deposited analysis script disagreed about at least one verdict. They disagreed about more
than one, and the audit disagreed with itself.

| Source | Block B | Block D | Totals |
|---|---|---|---|
| The audit's scoreboard | S3 P4 O1 N3 | S2 P2 N2 X1 | 14 / 14 / 1 / 16 / 16 |
| The audit's own per-claim sections | S3 P3 O2 N3 | S3 P1 N2 X1 | 15 / 12 / 2 / 16 / 16 |
| `paper/analysis-contingency.py` | S2 P4 O2 N3 | S2 P1 N3 | — |
| **Canonical, after correction** | **S2 P3 O2 N4** | **S3 P1 N2 X1** | **14 / 12 / 2 / 17 / 16** |

### The one that matters: B6

The audit's section for B6 opens **"✅ VERIFIED as citation / ❌ NOT TRUE as the dominant
mechanism."** The claim as inventoried asserts the dominant-mechanism reading. Under the
worst-sub-claim-governs rule it is **not true**.

The scoreboard read the first symbol and scored it **verified**. The analysis script scored it
**partly true**. Three readings of one claim, none of them agreeing.

Canonical is **not true**, which is the reading that **weakens** this repository's central
result: mechanism claims supported falls from 15/19 to 14/19.

### The others

**Block D, one claim.** The scoreboard recorded D1 as partly true where its own section scores
it verified. Canonical follows the section.

**D6, no effect.** The section marks ⛔ no scientific basis, the script marks ❌ not true. Both
are unsupported and both rank zero, so no reported figure changes.

**Block B's missing open.** The scoreboard counted the shared B4/B5 verdict once and balanced
the block with an extra partly-true. That is how 61 claims came to show a single open verdict,
and it is the arithmetic behind the "Table 1 says 1 open, Table 2 says 2 open" contradiction
an external reviewer spotted.

### What changed on the page

| | Was | Now |
|---|---|---|
| Verified | 14 | 14 |
| Partly true | **14** | **12** |
| Open | **1** | **2** |
| Not true | **16** | **17** |
| No scientific basis | 16 | 16 |

Corrected in [`INTEGRITY_AUDIT.md`](INTEGRITY_AUDIT.md), [`README.md`](README.md),
[`paper/MANUSCRIPT.md`](paper/MANUSCRIPT.md) and [`paper/PROPOSAL.md`](paper/PROPOSAL.md).

**A single authoritative verdict list now exists**, which is what the reviewer asked for:
[`paper/data-verdicts-canonical.md`](paper/data-verdicts-canonical.md). Where any other file
disagrees with it, that file is wrong.

### The uncomfortable part

This repository's claim is that its verdicts are checkable. Three of its own files disagreed
about what those verdicts were, and the disagreement survived every previous pass, including
the one that produced the paper. It was found only because someone outside the project read
the deposited script instead of the prose describing it.

---

## 2026-10-29 · The claim count is not reproducible. Two blind extractors found ~250, not 61.

**Severity:** high. It does not overturn the paper's central comparison, but it invalidates
every count and percentage quoted from the inventory.
**Found by:** running the independent blinded re-extraction that external review ranked first.

Two extractors, independent of each other and blind to the inventory, the verdicts, the
taxonomy, the hypothesis and the aggregation rule, were given the source document and the
definition of a substantive factual claim from the manuscript's Methods.

| Extractor | Claims | vs 61 |
|---|---|---|
| **This repository** | **61** | — |
| Independent extractor 1 | **258** | 4.2× |
| Independent extractor 2 | **237** | 3.9× |

**They agree with each other to 8.5% while both sit near four times this repository's count.**
A large gap with scattered extractors would be definitional noise. A large gap with clustered
extractors means the extraction here was **systematically coarse**. The divergence is widest
in the physics block (≈ 6–7×) and narrowest in pathophysiology (≈ 3–4×), and is driven by
finer splitting, not broader scope.

**What this invalidates.** "61 claims." "14 verified, 13 partly true, 16 not true, 16 no
basis." "0 of 9 quantitative specifications." "2 of 17 physical-theory claims." Each is a
statement about this repository's segmentation as much as about the document, and none should
be quoted to two significant figures. The scoreboard on the front page is in that category.

**What survives.** The mechanism/outcome dissociation, tested ordinally, held under every
decomposition available — including the reviewer's own construction and a version more
hostile than it (*p* = 0.0045 to 0.020). And the specific objection it was run to test did not
succeed: the reviewer argued that splitting claim A3 would put a verified sub-claim (renal
sodium retention) into the outcome column. **A3 does split — both extractors split it into the
same five claims — but neither isolated the verified component.** Both left it bundled with
two false ones. The split the objection requires is one no hypothesis-blind party made.

**What is untested.** Only A3 could be re-analysed, because only A3 had published sub-claim
verdicts. **Nobody has audited the ~250-claim inventories.** Both are published so that
someone can.

**A deviation, reported rather than buried.** The isolation check failed for the second time —
the extractors inherited the project directory and a commit log naming this very experiment.
They were run anyway rather than holding a third time. The leak revealed no taxonomy, no
verdict, no aggregation rule and nothing identifying A3, and its plausible bias runs against
this repository: a subject told granularity is under study splits more finely, and finer
splitting is what would have broken the result. It did not.

---

## 2026-10-29 · The source document was never archived

**Severity:** high, and structural rather than factual.
**Found by:** preparing the re-extraction above, which needed the source and could not find it.

Until today this repository contained only **its own extraction** of the audited document
([archive/source-claim-inventory.md](archive/source-claim-inventory.md)), not the document.
The extraction step — the one that sets the denominator of every figure here — was therefore
**not checkable by anyone.** That is a stronger version of the reviewer's objection than the
reviewer made; they assumed the source was available.

A repository whose entire argument is that claims should be checkable had made its own first
step uncheckable, and nobody noticed for the whole of its existence.

The document has been recovered in full from the session record (20,089 words, unaltered).

**Resolved: it is retained, not published.** A redacted copy was prepared — eleven regions
removed, about 500 lines — and the redaction verified. It was withheld anyway. A redaction is
a judgement and a single miss is irreversible, and what a miss would distribute is device-build
instructions to insulin-dependent readers. The cost of withholding is a gap that can be stated;
the cost of a miss cannot be undone.

The document's **SHA-256 is published** so any copy supplied can be verified as the one
audited, and it goes to journal editors and peer reviewers on request, in full. See
[archive/SOURCE-DOCUMENT.md](archive/SOURCE-DOCUMENT.md).

Most of the auditability is restored without it: the two independent extractions, published in
full, state **495 claims** in their own words, written by parties who had never seen this
repository's inventory.

---

## 2026-10-29 · The paper's headline statistic depended on an undisclosed analytic choice, and does not survive removing it

**Severity:** the most serious error logged here. It is not a factual slip; it is the kind of
analytic degree of freedom this project exists to object to, exercised by this project.
**Found by:** an external hostile peer review commissioned before submission, which read the
deposited analysis script rather than the manuscript's description of it.

### What was wrong

`paper/analysis-contingency.py` contains the line:

```python
sup = sum(1 for i in ids if V[i] in ("S","P"))
```

**"Supported" was defined as VERIFIED *or* PARTLY TRUE.** That definition appeared nowhere in
the manuscript — not in the methods, not in the table legend, not in the abstract — and was
never varied. Every reader of *"15 of 19 mechanism claims (79%) were supported"* would take
"supported" to mean "true." It meant "true, or real-science-overstated-misattributed-or-out-of-date."

The choice is maximally favourable to the hypothesis. Eight of the 19 mechanism claims are
partly true; **none of the 8 outcome claims is.** The entire dichotomous effect lives in that
one cell.

### What happens when it is removed

| Coding | Mechanism | Outcome | Fisher 2-sided |
|---|---|---|---|
| Lenient — as published | 15/19 (79%) | 0/8 | 2.2 × 10⁻⁴ |
| **Strict — verified only** | **7/19 (37%)** | **0/8** | **0.068 — not significant** |
| Strict, block-stratified (CMH) | — | — | 0.21 |
| Strict, Bonferroni × 6 | — | — | 0.41 |

The one-sided 95% lower bound on the odds ratio falls from 5.24 to **0.94**, crossing one.

### What survives

The zero does. **No therapeutic-outcome claim was supported under any coding, and no
quantitative specification was.** And the comparison does not actually require a cut point:
an exact ordinal permutation test on the verdict scale (verified 2 > partly true 1 > not true
0) gives *p* = 4.5 × 10⁻⁴, surviving a miscoding correction (*p* = 1.2 × 10⁻³) and a
deliberately hostile re-extraction (*p* = 1.6 × 10⁻²). That test is now the paper's primary
analysis, and both dichotomisations are reported side by side.

### Why it is logged this way

The sensitivity analysis that found this is **one line of code.** It was not run, because the
first coding produced a publishable number. That is textbook, and it happened here, in a paper
whose argument is that unchecked claims should not be believed.

The reviewer's recommendation was **reject**. The re-analysis, the cut-free primary test, the
new sensitivity script (`paper/analysis-sensitivity.py`), and a rewritten Limitations section
that leads with this problem are the response. A reader who thinks the response is inadequate
has the data to check.

### Four further findings from the same review, all verified and all acted on

| Finding | Status |
|---|---|
| **κ is inflated by a label leak.** The file named `data-claims-unlabelled.txt` carried block-prefixed claim IDs. All 13 block-C claims were rated SPECIFICATION and all 17 block-X claims PHYSICS — **30 of 61 (49%) derivable from the prefix alone.** κ on the 31 contestable claims is **0.928**, not 0.977 | Confirmed; both now reported, restricted figure named as the honest one |
| **κ is not inter-rater reliability.** Both raters were sessions of one model, so it measures stability under resampling; systematic errors are invisible to it by construction | Confirmed; relabelled throughout |
| **B6 was miscoded.** The audit recorded "verified as citation / not true as the dominant mechanism," and the inventoried claim asserts the dominant-mechanism reading. It was scored PARTLY TRUE | Confirmed; recoded to NOT TRUE, and a sub-claim aggregation rule now stated |
| **The denominator was unstable.** Table 1 reported 1 open claim; the analysis script expands B4/B5 into two. 61 claims carry 59 verdicts | Confirmed; unit of analysis now stated, Table 1 corrected to 2 open / 13 partly true |

### Overclaims removed from the manuscript in the same pass

- *"The same class of system surfaces the refuting trial"* — **false as written.** The
  generator was Gemini; Gemini under neutral prompting was never tested. "Same class" meant
  only "both are large language models."
- *"It is also not a general consequence of speculative prompting"* — the persona was adopted
  in **0 of 6** trials, so the manipulation was never delivered and the arm has no power in
  either direction.
- *"'Ask it again, plainly' is advice a clinician can give in the room"* — demoted to a
  hypothesis. The re-query arm has **no positive controls**: every probed question had "no" as
  its correct answer, so a model with a blanket sceptical prior scores 6/6 knowing nothing.
- *"No boronate glucose-responsive insulin has entered human testing at all"* — accepted from
  an AI experimental subject and never verified, **in a paper arguing that AI
  therapeutic-outcome claims are categorically unreliable.** Now stated as "we searched and
  found none," which is what is actually known.
- The manuscript's opening clinical vignette was written in the simple present with no marker
  of hypotheticality. It is now labelled.

---

## 2026-10-29 · "It circulates in patient communities." It does not; it was generated here.

**Severity:** high — an unsupported empirical claim, about the premise of the whole project,
on the first screen of the front page.
**Found by:** the same external review, cross-reading the manuscript's methods against this
repository's README.

The README said of the audited document that **"it circulates in patient communities where
nobody checks it."** The manuscript's methods section said, of the same document,
**"no dissemination to patients was observed and none is claimed."** Both could not be true.

The methods section is the accurate one. The document was generated in a private session, by
the owner of this repository, under a persona prompt written for the purpose, and **was never
published, shared, or shown to any patient.** The README sentence was a claim about the genre
written as a claim about this artifact.

Corrected on [`README.md`](README.md) and in `private/funding-case.md`. The manuscript now
discloses authorship of the source document as a **competing interest** rather than as
provenance, because authoring the stimulus of a study is an interest in its result — and
because it changes what the result can mean. The dissociation reported may be a property of
language models or a property of this prompt, and the study cannot distinguish them.

How widely such documents circulate is a real and unanswered question. This repository does
not answer it, and no longer implies that it does.

---

## 2026-10-29 · The zimislecel trial reported two deaths. This repository reported one.

**Severity:** high — a safety understatement, in the direction that flattered the most
optimistic finding in the repository.
**Found by:** pulling the primary abstract from PubMed to confirm a PMID that had been flagged
as unverified, and reading the results section rather than only the efficacy numbers.

Four files — [`README.md`](README.md), [`disclosure4.md`](disclosure4.md),
[`INTEGRITY_AUDIT.md`](INTEGRITY_AUDIT.md) and
[`docs/endocrinology/README.md`](docs/endocrinology/README.md) — described the VX-880-101
(FORWARD) trial as having **"one participant died of cryptococcal meningitis attributed to the
regimen."**

Reichman et al., *NEJM* 2025;393(9):858–868 reports **two deaths**:

| Death | Attribution |
|---|---|
| Cryptococcal meningitis | Attributed to the immunosuppressive regimen |
| Severe dementia with agitation, from progression of preexisting neurocognitive impairment | **Not** attributed to the therapy |

The second death is not a therapy-attributed death, and omitting it is defensible as a
judgement about causality. **It was not a judgement.** It was not noticed, because the
efficacy numbers were checked and the safety paragraph was not. In a repository whose entire
argument is that therapeutic-outcome claims need checking more carefully than mechanism
claims, under-reporting a death count in the one unambiguously good result is the specific
error this project exists to catch.

Also added from the same abstract: **neutropenia was the most common serious adverse event,
in 3 participants** — absent from every previous version.

Efficacy figures were re-checked at the same time and are correct: 10 of 12 (83%)
insulin-independent at day 365; all 12 free of severe hypoglycemic events with HbA1c <7% and
time-in-range >70%.

---

## 2026-10-29 · Two citations carried wrong or unverified identifiers

**Severity:** low — neither changed a verdict. Logged because the repository's claim is that
its citations are checkable, and two of them were not checked.

| Citation | Was | Is |
|---|---|---|
| Karges B et al., closed-loop DKA study | *Lancet Diabetes Endocrinol* **2024**, DOI only, flagged ⚠️ unverified | ***2025;13(2):88–96*, PMID 39701114** — epub ahead of print Dec 2024, which is where the wrong year came from |
| Reichman TW et al., zimislecel | PMID 40544428 "from an aggregator, not confirmed" | **Confirmed** against PubMed: title, journal, volume, issue and pages all match |

Every numeric claim drawn from Karges was re-verified against the abstract and is correct:
n = 13,922, 250 centres, hypoglycaemic coma 0.62 vs 0.91 per 100 patient-years (IRR 0.68,
0.48–0.97), DKA 1.74 vs 0.96 (IRR 1.81), TIR 64% vs 52%.

The unresolved-item list in [`references/bibliography.md`](references/bibliography.md) is
**seven items, down from eight.**

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

- **Seven unresolved citations** listed at the end of
  [`references/bibliography.md`](references/bibliography.md)
- **Two evidence gaps:** a national US insulin-rationing prevalence figure (Fang & Selvin,
  *JAMA* 2023, PMC10061307) and current HCUP DKA cost and volume data. The repository
  currently relies on a single-centre rationing study (n=199) and 2014 DKA charge data, and
  labels both as such
- **The paper's central confound:** model identity is confounded with prompting regime in
  [`paper/RESULTS.md`](paper/RESULTS.md). Stated in the abstract, not resolved
