# Cover letter

Utah Hans · Independent researcher

---

Dear Editors,

I am submitting **"Other Cardiometabolic Health" — Mechanism without outcome: a claim-level
audit of AI-generated insulin misinformation in a disease with a 48-hour error budget** for
consideration as Original research.

**What it reports.** An exhaustive audit of 61 claims in an AI-generated document on insulin
therapy, with classification into epistemic strata performed blind to all verdicts, plus five
experiments. **No therapeutic-outcome claim was supported (0/8) and no quantitative
specification was (0/9), under any analysis.** Mechanism claims scored substantially better;
an exact ordinal permutation test on the verdict scale gives *p* = 4.5 × 10⁻⁴. Every false
outcome claim corresponded to a development programme that had already failed — C-peptide
replacement, glucose-responsive insulin, hepato-preferential insulin, oral insulin,
alpha-to-beta transdifferentiation.

**Why it matters clinically.** Type 1 diabetes gives this an unusually short error budget:
ketoacidosis follows insulin cessation within 12 to 48 hours, so the interval between
believing a false claim and requiring emergency care is measured in hours rather than years.
The practical observation is that a patient presenting such material will typically be right
about the mechanism and wrong about the outcome, which makes wholesale dismissal both
inaccurate and, I argue, counterproductive in a consultation.

**What I would ask you to weigh most, because it is why the paper looks as it does.** Five
separate analyses in this work damaged its own claims, and all five are reported:

1. **Blinded classification** revealed that an earlier unblinded pass had over-assigned the
   outcome category specifically to claims already scored false, cutting the effect from
   93%/0% to 79%/0%.
2. **A replication falsified the explanatory hypothesis I had proposed.** I predicted the
   dissociation would persist under neutral prompting because it arose from corpus
   publication bias. It did not persist in any of six probes.
3. **One experimental arm was discarded** for demand characteristics after four of six
   subjects inferred the hypothesis from passive context in their environment.
4. **Pre-submission peer review showed the headline statistic was not robust.** The
   dichotomisation had been chosen silently; under the strict coding *p* = 0.068, which is
   not significant. The paper now reports both codings, makes the cut-free ordinal test
   primary, and leads its Limitations with the problem rather than closing with it.
5. **Two independent blinded extractors found 258 and 237 claims where I found 61**, agreeing
   with each other to 8.5%. My counts therefore do not reproduce, and the abstract says so.

A sixth arm was pre-registered and then **abandoned** when its isolation check failed; the
abandonment is published rather than omitted.

I would rather submit a paper with a smaller claim and a visible audit trail than a larger
claim and a fragile one.

**Disclosure.** I generated the audited document myself, under a persona prompt I wrote. It
was never disseminated. This is declared as a competing interest, not merely as provenance,
because authoring the stimulus of a study is an interest in its result — and because it
bounds the conclusion: the pattern may be a property of language models or of this prompt,
and this design cannot separate them.

**Dual use.** The source document contains construction and programming detail for the
transdermal device it presents as a replacement for injected insulin. That material is
reproduced nowhere. **The source document is retained but not published, and is available to
you and to reviewers on request, in full and unredacted.** Its SHA-256 is published so any
copy supplied can be verified as the one audited.

**Use of AI.** AI systems were used for literature search, verification, blinded
classification, and as experimental subjects. No AI system is an author. The circularity this
creates is treated as a limitation, including that both raters were sessions of one model, so
κ measures stability under resampling and not inter-rater reliability.

**Open materials.** The complete claim inventory, the canonical verdict file, both raters'
classifications, both independent re-extractions, all five analysis scripts, four
pre-registrations with commit timestamps, and a public corrections log with eleven entries
are at `github.com/utahisnotastate/ufwwarforinsulin`. The complete analysis output is also
reproduced verbatim in the supplementary material.

**Reporting guideline.** No EQUATOR-registered guideline covers this design. The submitted
checklist uses STROBE as the closest available frame and states plainly where it does not
fit, rather than stretching items to appear compliant.

**Prior publication, stated in full.** The manuscript, its data, its analysis scripts and
its corrections log are **already publicly available** in an open repository at
`github.com/utahisnotastate/ufwwarforinsulin`, and have been since the work was done. The
repository is the mechanism by which this work is auditable, and taking it down would defeat
the paper's central claim, so I have not done so.

I take this to fall under BMJ's preprint policy rather than to constitute prior publication,
since it is an author-posted version that has not been peer reviewed or published by any
journal. **I am flagging it explicitly rather than letting you discover it**, because the
required declaration asks whether the manuscript duplicates already-published material and I
would rather you rule on that than have me assume the answer. A version will also be posted
to medRxiv at submission.

**It has not been submitted to, accepted by, or is under consideration at any other journal**,
and The BMJ is the only journal considering it.

This work received no funding and I have no financial competing interests.

Yours faithfully,

**Utah Hans**
Independent researcher
