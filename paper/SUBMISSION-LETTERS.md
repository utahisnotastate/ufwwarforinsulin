# Submission letters

Rewritten 2026-10-29 after external peer review forced a re-analysis. **The earlier drafts of
these letters led with "15 of 19 versus 0 of 8, *p* = 2.2 × 10⁻⁴" as the headline. That figure
depends on a definition of "supported" the manuscript did not state and had not tested, and it
does not survive the strict definition (*p* = 0.068).** The letters below lead with what
survives.

**The Analysis route is closed.** The body is now ~8,000 words against a 2,000-word limit, and
BMJ states Analysis does not consider manuscripts containing primary research data. Send **A**
only if you want a steer; otherwise go straight to **B** or **C**.

---

## A. Pre-submission enquiry to *The BMJ*

> **Subject: Pre-submission enquiry — AI-generated medical misinformation, insulin**
>
> Dear Editors,
>
> I have a manuscript I believe belongs in Research rather than Analysis, and I would value a
> steer before formatting it.
>
> **The work.** A long AI-generated document on insulin therapy tells readers they can replace
> insulin with a radio-frequency device. I extracted all 61 substantive claims and verified
> each against primary literature. I generated the document myself, under a persona prompt;
> that is declared as a competing interest rather than buried as provenance.
>
> **The finding that holds.** No therapeutic-outcome claim was supported — 0 of 8 — and no
> quantitative specification was — 0 of 9. Every false outcome claim corresponded to a
> development programme that had already failed. Mechanism claims scored substantially better,
> and an exact ordinal permutation test puts the difference at *p* = 4.5 × 10⁻⁴, surviving both
> a miscoding correction and a deliberately hostile re-extraction.
>
> **The finding that did not hold, which is why I am writing.** The paper originally reported
> 79% versus 0%, *p* = 2.2 × 10⁻⁴. An external reviewer identified that "supported" had been
> silently defined to include partly-true claims, and that the definition was never stated or
> varied. Under the strict definition the figure is 37% versus 0%, *p* = 0.068 — **not
> significant** — and a block-stratified test gives *p* = 0.21. The manuscript now reports both
> codings in its central table, makes the cut-free ordinal test primary, and states in its
> first limitation that the choice was available, was made silently, and was made by the person
> who formed the hypothesis.
>
> I mention this because it is the sort of thing an editor would rather learn from the author
> than from a referee, and because the paper's whole argument is about the discipline of
> checking claims.
>
> **My question.** The piece makes an argument and could be written at Analysis length, but it
> reports four experiments and your guidance states that Analysis does not consider manuscripts
> containing primary research data. I take that as directing me to Research. Is that right, or
> is this not for The BMJ?
>
> The title is *"Other Cardiometabolic Health"* — the line item in Note 2 of Eli Lilly's FY2025
> Form 10-K into which insulin revenue was absorbed, having been three named brands a year
> earlier. The text states the qualifications: the change was portfolio-wide, not
> insulin-specific, and it is not a reporting-threshold effect. I am attached to the title but
> not immovable on it.
>
> One further thing in the paper's favour, added after the same review. The review noted that
> the re-query experiment had no positive controls and therefore measured sensitivity without
> specificity. I pre-registered and ran them, with ground truth verified against PubMed and
> committed before the run: the model answered correctly in **7 of 7** concepts whose correct
> answer is *yes*, giving perfect separation across both directions. The criterion that would
> have voided the arm was tested and not met.
>
> All data, rater outputs, analysis scripts including the sensitivity analyses and the
> specificity arm, two pre-registrations with their commit timestamps, and a public
> corrections log are openly available.
>
> Yours faithfully,
> Utah Hans

---

## B. Cover letter — *BMJ Research* submission

> Dear Editors,
>
> I am submitting **"Other Cardiometabolic Health" — Mechanism without outcome: a claim-level
> audit of AI-generated insulin misinformation in a disease with a 48-hour error budget** for
> consideration as a Research article.
>
> **What it reports.** An exhaustive audit of 61 claims in an AI-generated document on insulin
> therapy, with classification into epistemic strata performed blind to all verdicts, plus two
> re-query experiments. **No therapeutic-outcome claim was supported (0/8) and no quantitative
> specification was (0/9), under any analysis.** Mechanism claims scored substantially better;
> an exact ordinal permutation test on the verdict scale gives *p* = 4.5 × 10⁻⁴.
>
> **Why it matters clinically.** Type 1 diabetes gives this an unusually short error budget —
> ketoacidosis follows insulin cessation within 12 to 48 hours. The practical observation is
> that such a patient will typically be right about the mechanism and wrong about the outcome,
> which makes wholesale dismissal both inaccurate and, I argue, counterproductive in a
> consultation.
>
> **What I would ask you to weigh most, because it is why the paper looks as it does.** Four
> separate analyses in this paper damaged its own claims, and all four are reported:
>
> 1. **Blinded classification** revealed that an earlier unblinded pass had over-assigned the
>    outcome category specifically to claims already scored false, cutting the effect from
>    93%/0% to 79%/0%.
> 2. **A replication falsified the explanatory hypothesis I had proposed.** I predicted the
>    dissociation would persist under neutral prompting because it arose from corpus
>    publication bias. It did not persist in any of six probes.
> 3. **A third arm was discarded** for demand characteristics after four of six subjects
>    inferred the hypothesis from their environment.
> 4. **Peer review before submission showed the headline statistic was not robust.** The
>    dichotomisation had been chosen silently; under the strict coding *p* = 0.068. The paper
>    now reports both codings, makes the cut-free ordinal test primary, and leads its
>    Limitations with the problem rather than closing with it.
>
> The same review identified that the re-query arm had no positive controls. I pre-registered
> and ran them — seven concepts whose correct answer is *yes*, ground truth verified against
> PubMed and committed before the run, three chosen deliberately to sound like the audited
> document's register while being true. The model answered **7 of 7** correctly: sensitivity
> 6/6, specificity 7/7, perfect separation. That one went the paper's way, and I report it in
> the same place and the same voice as the three that did not.
>
> I would rather submit a paper with a smaller claim and a visible audit trail than a larger
> claim and a fragile one.
>
> **Disclosure.** I generated the audited document myself under a persona prompt I wrote. This
> is declared as a competing interest in §7.2, not only as provenance, because authoring the
> stimulus of a study is an interest in its result. It also bounds the conclusion: the pattern
> may be a property of language models or of this prompt, and this design cannot separate them.
> §7.3 carries a dual-use assessment; the one component of the source document that could be
> built from its text — microcontroller firmware for the device it recommends instead of
> insulin — is reproduced nowhere.
>
> **Use of AI.** AI systems were used for literature search, verification, blinded
> classification, and as experimental subjects. No AI system is an author. §7.8 states this in
> detail, and §5.3 and §5.9 treat the circularity it creates as limitations rather than
> footnotes — including that both "raters" were sessions of one model, so κ measures stability
> under resampling and not inter-rater reliability.
>
> **Open materials.** The complete claim inventory, both raters' classifications, the analysis
> scripts reproducing every statistic including all sensitivity analyses, the pre-registration
> with its commit timestamp, and the corrections log are at
> github.com/utahisnotastate/ufwwarforinsulin.
>
> **Prior publication.** A full-length version will be posted to medRxiv at submission. No part
> has been published elsewhere.
>
> This work received no funding and I have no financial competing interests.
>
> Yours faithfully,
> Utah Hans

---

## C. Cover letter — JMIR / *npj Digital Medicine*

> Dear Editors,
>
> I am submitting **"Mechanism Without Outcome: A Claim-Level Audit of AI-Generated Insulin
> Misinformation in Type 1 Diabetes."**
>
> Existing health-misinformation taxonomies score veracity. This paper proposes that accuracy
> in AI-generated medical text is **stratified by epistemic layer**, and tests it. In an
> exhaustive audit of 61 claims, no therapeutic-outcome claim and no quantitative specification
> was supported (0/8 and 0/9); mechanism claims scored substantially better, with an exact
> ordinal permutation test giving *p* = 4.5 × 10⁻⁴. The dichotomous version of that comparison
> is **not robust to the cut point** — 79% versus 37% supported depending on whether
> partly-true claims count — and the paper reports both codings rather than the favourable one.
>
> Three contributions may interest your readership specifically.
>
> **Two reference-free detection signals**, requiring no external lookup: an amino-acid
> sequence contradicting its own stated molecular formula, and a frequency that does not
> reproduce from the equation supplied in the same paragraph.
>
> **A time-to-harm axis** orthogonal to veracity, anchored by a disease where the interval from
> belief to emergency is 12 to 48 hours.
>
> **A contamination mechanism in agent-based evaluation** that we expect will affect others
> working in this area: subjects inferred our experimental hypothesis from passive
> system-prompt context — a working directory name and version-control history — with no
> subject reading any file. Four of six were contaminated. The arm was discarded and a
> contamination check with a fixed decision rule was pre-registered before the replication,
> which came back clean.
>
> The sequel is the part we would most like other groups to take. Before a later arm we
> **instrumented the subject environment instead of assuming it** — a throwaway agent, given
> none of the experimental material, asked only what it could see. It reported the project
> directory and the version-control log: the isolation we believed we had configured had not
> taken effect. The probes were held. **Executing from a clean environment is not sufficient;
> isolation has to be verified from inside the subject's context at the moment of the run**,
> because what the researcher configures and what the subject receives can differ.
>
> The paper reports four analyses that damaged its own claims, including one found in
> pre-submission peer review that showed the original headline statistic depended on an
> undisclosed analytic choice. All are in the manuscript rather than in a file drawer.
>
> I generated the audited document myself; this is declared as a competing interest and bounds
> what the result can mean. All materials, including pre-registration with commit timestamp and
> a public corrections log, are at github.com/utahisnotastate/ufwwarforinsulin.
>
> Yours faithfully,
> Utah Hans
