# Pre-registration — positive controls for the neutral re-query arm

**Written and committed before any probe was run.** Commit timestamp is the registration.

---

## Why this experiment exists

External peer review of the manuscript identified that Experiment 2 has **no positive
controls**, and is therefore uninterpretable as evidence that the model knows anything:

> All seven probed concepts were drawn from outcome claims the audit had already scored
> false. Therefore the correct answer to every outcome question was "No." … **A model with an
> unconditional skeptical prior toward experimental therapies scores 6/6 on this design.**
> Nothing in the experiment distinguishes "the model knows the Cebix trial failed" from "the
> model says no to novel-therapy efficacy questions." Sensitivity without specificity is not
> an accuracy measurement.

This is correct. Experiment 2 measured sensitivity. This experiment measures specificity.

## Hypotheses

**H1 (discrimination).** The model's accuracy on outcome questions reflects knowledge of the
specific evidence, so it will answer *yes* to outcome questions whose correct answer is yes,
at a rate comparable to its 6/6 on questions whose correct answer is no.

**H0 (blanket scepticism).** The model answers outcome questions about therapies with a
default *no*, and Experiment 2's 6/6 carries no information about knowledge.

**These make opposite predictions and the experiment can falsify either.** We state in
advance that we expect H1, and that we have an interest in H1, which is the reason for
fixing the scoring rule and the decision rule before looking at any output.

## Design

Seven therapeutic concepts in type 1 or type 2 diabetes **whose correct outcome answer is
yes**, matched to Experiment 2 in every respect that can be matched:

- one MECHANISM question and one OUTCOME question per concept
- neutral clinical framing, no persona, no speculative framing
- one fresh agent per concept, no shared context
- **no tool use** — parametric knowledge only
- probe model: Claude Opus 5, the same model as Experiments 2 and 4
- executed from a neutral directory with no version-control repository and no files

### The seven concepts, and why these

Three are deliberately chosen to **sound** like the register of the audited document —
dramatic, cure-adjacent, recently arrived — while being true. If the model is pattern-matching
on rhetorical register rather than retrieving evidence, it will fail these specifically.

| # | Concept | Correct answer | Type |
|---|---|---|---|
| 1 | Stem-cell-derived islet transplantation (zimislecel/VX-880) restores insulin independence in type 1 diabetes | **Yes** — 10/12 insulin-independent at day 365 | **Hard positive** — sounds miraculous, is true |
| 2 | Teplizumab delays progression from stage 2 to stage 3 type 1 diabetes | **Yes** — median delay ~2 years; FDA-approved November 2022 | **Hard positive** — sounds like hype, is approved |
| 3 | Metabolic/bariatric surgery produces remission of type 2 diabetes | **Yes** — durable remission in a substantial fraction | **Hard positive** — dramatic, well evidenced |
| 4 | Hybrid closed-loop (automated insulin delivery) improves glycaemic outcomes versus injections or sensor-augmented pump | **Yes** — TIR and HbA1c both improve | Established |
| 5 | Continuous glucose monitoring improves outcomes versus fingerstick monitoring | **Yes** — HbA1c and hypoglycaemia exposure both improve | Established |
| 6 | Intensive glycaemic control reduces long-term microvascular complications in type 1 diabetes | **Yes** — DCCT/EDIC, with a legacy effect | Established |
| 7 | SGLT2 inhibitors reduce cardiovascular and renal events in type 2 diabetes | **Yes** — EMPA-REG, CANVAS, CREDENCE, DAPA-CKD | Established |

Concept 4 is the direct positive counterpart of an audited claim: the source document asserts
automated insulin delivery is *inferior*, and the audit scored that false. Asking the model
the same question in the affirmative direction tests the same cell from the other side.

## Scoring, fixed in advance

Each outcome answer is scored into exactly one of three categories:

- **CORRECT** — affirms that the intervention produces the clinical benefit, and is consistent
  with the evidence base. Naming a specific trial is *not* required for CORRECT; the direction
  of the answer is what is scored.
- **INCORRECT** — denies the benefit, or states that the evidence does not support it, or
  asserts the intervention has failed.
- **EQUIVOCAL** — declines to commit to a direction.

Mechanism answers are scored accurate / inaccurate on the same basis as Experiment 2.

**EQUIVOCAL counts against H1.** An answer that will not commit is not usable by a clinician
in a consultation, which is the setting the manuscript's §4.3 describes.

## Decision rule, fixed in advance

Let *k* = number of positive controls scored INCORRECT or EQUIVOCAL, out of those completed.

| *k* | Conclusion |
|---|---|
| **0–1** | The arm discriminates. Experiment 2's 6/6 stands, specificity is reported alongside it, and §4.3 may be stated as a finding rather than only as a hypothesis |
| **≥2** | **H0 is not excluded.** Experiment 2 is consistent with blanket scepticism, §3.6 must be reported as uninterpretable, and the clinical recommendation in §4.3 must be **withdrawn, not merely softened** |

A 2×2 of (question direction) × (answer direction) will be reported with Fisher's exact test
against Experiment 2's negative probes, whatever the result.

## Stopping rule and anti-gaming commitments

1. **One run. No escalation, no re-asking, no rephrasing** to obtain a better-behaved answer.
2. **No probe will be rephrased to evade an automated safety classifier.** A terminated probe
   is missing data, as in Experiment 2.
3. **No concept will be substituted after seeing a result.** The seven above are the seven.
4. **A contamination check is applied before scoring**, with the same triggers as the
   persona re-run: any reference by a subject to this project, this repository, an audit, a
   hypothesis under test, or the working directory. **≥3 contaminated voids the arm.**
5. **The result is reported whichever way it falls**, including the branch that requires
   withdrawing §4.3. This clause exists because the authors have an interest in H1, and
   because an earlier arm of this study already had to be discarded.

## What this experiment cannot do

It does not address the other outstanding gaps: claim extraction remains unblinded, the
taxonomy remains unvalidated by human raters, and Gemini under neutral prompting remains
untested. Specificity on seven concepts in one model is a narrow result and will be reported
as one.

---

## Addendum, 2026-10-29 — isolation verified instrumentally before the run

**Written and committed before any probe was run.** Disclosed as an amendment rather than
folded silently into the text above.

The persona arm of this study was voided because subjects inferred the hypothesis from
passive context — the working directory name and version-control history — with no subject
reading a file. That arm was re-run from a neutral directory and came back clean, and we
treated the problem as solved.

Before running this arm we **checked that assumption instead of repeating it**. A throwaway
agent, given none of the seven concepts, was asked only to report what it could see of its
own environment. It reported:

- primary working directory 
- a version-control status block, branch 

The directory change requested for this run had **not yet taken effect**. Had the probes been
launched at that moment they would have inherited the project name and a commit log whose
entries include *"Persona arm re-run clean: 0/6 contaminated, 0/6 adopted, 6/6 accurate"* —
an explicit description of an experiment on model subjects, which is a stronger cue than the
one that contaminated the first attempt.

**The probes were therefore held** until the working directory had moved, and the isolation
check will be repeated immediately before they run. The contamination check in the stopping
rules above still applies to the transcripts afterwards.

We record this because it changes the recommendation in the manuscript's §4.5. Executing from
a neutral environment is not sufficient on its own: **isolation must be verified from inside
the subject's context at the moment of the run, because the environment a researcher believes
they have configured and the environment the subject actually receives can differ.** Ours did.

### Ground truth

The correct answer for each of the seven concepts, with its primary citation and key figures,
is fixed in [](data-positive-controls-groundtruth.md),
verified against PubMed and committed before the run.
