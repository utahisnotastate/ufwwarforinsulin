# Pre-registration — independent blinded re-extraction

**Written and committed before any extraction was run.** Commit timestamp is the registration.

---

## Why this experiment exists

External peer review ranked this **first** among the things that would have to be done before
the paper could be accepted:

> Claim extraction was unblinded, by the author, with no stated granularity rule — and it sets
> the denominator. … **Extraction granularity is a free parameter that directly controls the
> headline, and it was set unblinded by the person who formed the hypothesis.** §3.2 proves
> this kind of bias was operating in this project, in this direction, at the adjacent step.

The reviewer's concrete attack: claim **A3** bundles six asserted mechanisms, one of which the
audit itself verifies (renal sodium retention under hyperinsulinaemia). A3 is scored as a
single NOT TRUE outcome claim. **Splitting it would put a verified claim into the outcome
column and destroy the 0/8.** Meanwhile **B2** bundles three residues and is scored PARTLY
TRUE on its best component. Opposite rules, applied by the same unblinded analyst.

A hostile re-extraction of A3 alone has already been run as a sensitivity analysis (§3.3): it
moves the ordinal *p* to 1.6 × 10⁻² and the strict dichotomous *p* to 0.21. **That is the
author constructing the attack on the author.** This experiment asks parties who do not know
the hypothesis to extract the claims from scratch.

## A problem found while preparing this, which is worse than the reviewer knew

**The source document was not archived.** Until today this repository contained only the
author's extraction of it (`archive/source-claim-inventory.md`), not the artifact itself. The
extraction step was therefore **not independently auditable by anyone**, which is a stronger
version of the reviewer's objection than the reviewer made — they assumed the source was
available.

The document has been recovered in full from the session record: 20,089 words, structure
matching the inventory's seven blocks. Whether it is published, and in what form, is a
separate dual-use decision (see the end of this document). It is used here regardless, because
without it this experiment is impossible.

## Design

**Two extractors, independent of each other and blind to everything downstream.**

Each receives the source document as a plain file in a neutral directory, and this
instruction, which is the definition of "substantive factual claim" copied verbatim from §2.2
of the manuscript and nothing more:

> Extract every substantive factual claim from this document. State each neutrally, in the
> document's own terms, without correcting it. Assign each a sequential identifier. Group them
> under topic headings of your choosing. Non-empirical content — metaphor, narrative framing,
> an addressee persona, a cosmological preamble — should be noted as present but not extracted
> as claims, because evaluating a metaphor for truth value is a category error.

**What the extractors will NOT be given, and must not infer:**

- the existing inventory, or its claim count, or its block letters
- any verdict, or the existence of an audit
- the mechanism / outcome / specification / physical-theory taxonomy
- any statement of the hypothesis
- the sub-claim aggregation rule — **this is the variable under test and supplying it would
  void the experiment**

**Isolation.** Executed from `C:\code\tmp-ex-eval`: neutral directory name, no version-control
repository, nothing but `document.txt`. Isolation will be verified from inside a subject's
context immediately before the run, per the recommendation this project added to §4.5 after
the last arm nearly ran contaminated.

## Pre-specified measures

1. **Claim count.** Each extractor's total, against the original's 61.
2. **Inter-extractor agreement on count**, which bounds how much of any author-versus-extractor
   difference is definitional noise rather than bias.
3. **Boundary agreement.** Each original claim is classified as `1:1` (one extractor claim
   covers it), `SPLIT` (two or more), `MERGED` (shares an extractor claim with another original
   claim), or `ABSENT`.
4. **The decisive measure — treatment of the compound claims.** Specifically A3, and also B2,
   B4/B5 and D4/D5. For A3: **did an independent extractor split it, and if so did any
   resulting sub-claim correspond to the verified renal-sodium-retention mechanism?**
5. **Re-run of the ordinal test** on the independent inventory, carrying verdicts across the
   1:1 mappings and treating splits per the rule below.

## Decision rule, fixed in advance

Let *d* = |independent claim count − 61| / 61, and let *S* = the set of original claims that at
least one independent extractor split.

| Condition | Conclusion |
|---|---|
| Both extractors split **A3** into components including the verified renal mechanism, **and** the ordinal test on the re-extracted inventory loses significance | **The headline does not survive independent extraction.** Report as the primary result and withdraw the stratification claim |
| A3 is split but the ordinal test survives | The dissociation is robust to the specific attack the reviewer identified. Report both inventories |
| Neither extractor splits A3 | The author's granularity was not idiosyncratic on the claim that matters. Report, and note that this does not vindicate the granularity generally |
| *d* > 0.30 | **Extraction granularity is unstable**, and every count-based figure in the paper must be reported with that instability attached, whatever the ordinal test does |

**Mapping is the weak point and is declared as such.** Mapping independent claims onto the
original 61 will be done by the author, who knows the hypothesis. The mapping will be published
as a file so that a reader can redo it. Where a mapping is genuinely ambiguous it will be
resolved **against** the paper's thesis, and those cases will be listed.

## Anti-gaming commitments

1. **Two extractors, one run each. No re-running an extractor whose output is inconvenient.**
2. **No concept, instruction or definition will be changed after seeing any output.**
3. **The result is reported whichever way it falls**, including the branch that requires
   withdrawing the central claim.
4. If an extractor's output is unusable for a reason unrelated to the hypothesis — truncation,
   a safety termination — that is reported as missing data and not silently replaced.

## What this experiment still cannot do

The extractors are language models, and the verification behind every verdict was also
AI-assisted (§5.9). This is a test of whether *the author's* granularity was idiosyncratic,
not a human-validated extraction. It narrows the objection; it does not close it. A human
domain expert extracting independently remains the thing that would close it, and has not been
done.

## Dual-use note on the recovered source

The document contains microcontroller firmware parameters for a transdermal device presented
as a replacement for injected insulin. The existing dual-use position (§7.3) is that this
firmware is **reproduced nowhere**. Recovering the document for analysis does not change that
position. Whether to archive the document publicly — redacted of the firmware, which would make
the extraction step auditable for the first time — is a decision for the repository owner and
is **not** taken by running this experiment.
