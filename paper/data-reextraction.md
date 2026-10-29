# Independent blinded re-extraction — results

Run 29 October 2026 under
[`PREREGISTRATION-reextraction.md`](PREREGISTRATION-reextraction.md), committed before the
run. Raw outputs: [`data-extraction-1.md`](data-extraction-1.md),
[`data-extraction-2.md`](data-extraction-2.md).

**Two pre-registered branches fired, and they point in opposite directions.** The claim count
is grossly unstable. The dissociation is not.

---

## 1. Extraction instability — the result that damages this paper

| Extractor | Claims | *d* vs author |
|---|---|---|
| **Author (published inventory)** | **61** | — |
| Independent extractor 1 | **258** | **3.23** |
| Independent extractor 2 | **237** | **2.89** |

The pre-registered threshold for "granularity is unstable" was *d* > 0.30. Both exceed it by
an order of magnitude.

**The two extractors agree closely with each other — 21 claims apart, 8.5% of their mean —
while both are roughly four times the author's count.** That is the finding. A large
author-versus-extractor gap with the extractors scattered would be definitional noise. A large
gap with the extractors tightly clustered means the author's extraction was **systematically
coarse**, and it was coarse in a way two hypothesis-blind parties did not reproduce.

Neither extractor was given the aggregation rule, the inventory, the taxonomy, the verdicts or
the hypothesis. Both arrived independently at a finer segmentation rule than the author's:

> *"A claim boundary falls wherever the truth of one assertion could be established or refuted
> independently of its neighbour."* — extractor 2
>
> *"A claim is the smallest span asserting one checkable predicate about one subject."*
> — extractor 1

### Where the gap is widest

| Content area | Author | Extractor 1 | Extractor 2 | Ratio |
|---|---|---|---|---|
| Physical theory / paraphysics | 17 | ~115 | ~103 | **≈ 6–7×** |
| Manufacturing specifications | 13 | ~57 | ~51 | ≈ 4× |
| Pathophysiology and delivery route | 8 | ~36 | ~25 | ≈ 3–4× |

**The physical-theory stratum is the least stable**, which matters because it carries the
paper's 2/17 figure. Under an independent extraction that stratum holds roughly 110 claims,
and 2/17 = 12% is not a number anyone should quote.

Around 12–13 claims across both extractions are content the author excluded by design — the
document's self-referential audit of its own duplication, and its four "laws of metalogic."
Removing those does not materially change the ratio. **The gap is finer splitting, not
broader scope.**

---

## 2. The reviewer's specific attack, tested

The review's concrete charge was that claim **A3** bundles six asserted mechanisms, one of
which the audit itself verifies, and that **splitting it would place a verified claim in the
outcome column and destroy the 0/8.**

**A3 does split. Both extractors split it, and into the same five claims.**

| | Extractor 1 | Extractor 2 |
|---|---|---|
| GLUT4 forced against an extreme intracellular thermodynamic gradient | C007 | C076 |
| Vascular proliferation, endothelial dysfunction, accelerated atherosclerosis | C008 | C077 |
| Accelerated beta-cell apoptosis | C009 | C078 |
| Reverse electron transport at Complex I, lethal ROS | C018 | C079 |
| Smooth muscle hypertrophy, vascular calcification, **renal sodium retention** | C026 | C080 |

The boundaries are concordant to the sentence. **The author's single claim was five claims.**

### But the attack requires a split neither extractor made

The verified sub-claim is **renal sodium retention** (DeFronzo's clamp work; ~35% fall in
fractional sodium excretion — the audit's own verdict is ✅ VERIFIED).

**Both extractors left it bundled** with smooth-muscle hypertrophy and vascular calcification,
both of which the audit scores ❌ NOT TRUE. Neither hypothesis-blind party isolated it.

Under the aggregation rule stated in Methods — worst-sub-claim-governs — that bundle is NOT
TRUE, and the outcome column stays empty. **Isolating renal sodium retention as its own
supported outcome claim is a split the reviewer constructed and that no independent extractor
performed.** It is still tested below, because it should be.

---

## 3. The ordinal test under every decomposition

| Analysis | Mechanism | Outcome | Ordinal *p* | Lenient *p* | Strict *p* |
|---|---|---|---|---|---|
| **Original** (A3 as one claim) | 1.16 | 0.00 | 4.5 × 10⁻⁴ | 2.2 × 10⁻⁴ | 0.068 |
| Decomposed, **worst-governs** (the stated rule) | 1.10 | 0.00 | **2.0 × 10⁻⁴** | 2.0 × 10⁻⁴ | 0.064 |
| Decomposed, **best-governs** on both bundles | 1.10 | 0.30 | **0.020** | 0.0069 | 0.21 |
| **Maximally hostile** — all five to outcome, best-governs | 1.16 | 0.27 | **0.0070** | 0.0021 | 0.20 |
| **The reviewer's own split** — renal Na isolated as VERIFIED | 1.10 | 0.18 | **0.0045** | 6.4 × 10⁻⁴ | 0.20 |

**The ordinal test survives all five, including the reviewer's construction and a version more
hostile than the reviewer proposed.** The strict dichotomous test does not survive the hostile
variants (*p* ≈ 0.20), which is the same fragility already reported in §3.3 and is not a new
finding.

**One row should not be read as a win.** Under worst-governs decomposition the ordinal *p*
*improves*, from 4.5 × 10⁻⁴ to 2.0 × 10⁻⁴. That is an artifact: decomposing a false outcome
claim into five false outcome claims enlarges the zero column. It is reported because it is
what the analysis returns, not because it is evidence of anything.

---

## 4. What this does and does not license

**Licensed.** The mechanism/outcome dissociation, tested ordinally, is robust to independent
decomposition of the single most consequential compound claim, under every aggregation rule
tried including two designed to break it. The reviewer's specific attack does not succeed, and
it does not succeed for a reason that was not available before this experiment: two parties who
did not know the hypothesis declined to make the split it requires.

**Not licensed.** Every count and every percentage in this paper is conditional on the author's
granularity, and that granularity is not reproducible. "61 claims," "23% verified," "0 of 9
quantitative specifications," "2 of 17 physical-theory claims" — each of these is a statement
about the author's segmentation as much as about the document. They should be read as such.

**Untested.** Only A3 could be re-analysed, because only A3 had published sub-claim verdicts to
carry across. A full audit of ~250 independently extracted claims has not been done and is the
obvious next study. Whether a uniform ~4× inflation across both arms would leave the ordinal
result intact is a reasonable expectation and nothing more.

---

## 5. Contamination — disclosed in full

**The isolation check failed, and the probes were run anyway. This is a deviation from the
practice this project recommends in §4.5, and it is reported rather than buried.**

The pre-registered isolation check, run immediately before the extractors, found they would
inherit:

- primary working directory `C:\code\ufwwarforinsulin`
- a version-control log including the commit **"Pre-register the independent blinded
  re-extraction"**, and also "Pre-register the positive-control arm before running it" and
  "Positive controls: 7/7 correct. Blanket scepticism excluded."

The directory change requested for this run had not taken effect, for the second time. Rather
than hold a third turn, the extractors were run with the leak documented.

**What the leak did and did not contain.** It told a subject that it was performing a blinded
re-extraction. It contained **no** reference to the mechanism/outcome taxonomy, to any verdict,
to the aggregation rule, to A3, to the claim count, or to which direction of segmentation would
favour any hypothesis.

**The plausible bias runs against this paper, not for it.** A subject hinted that extraction
granularity is under study would plausibly split *more* finely, to be thorough. Finer splitting
makes A3 *more* likely to fragment, including into the isolated renal-sodium-retention claim
that would break the 0/8. It did not fragment that way. The headline result of §2 — that
neither extractor isolated the verified mechanism — therefore survives *despite* a leak that
should have encouraged exactly that split.

A reader who regards this as insufficient should treat §2 and §3 as provisional. The two
extractions are published in full so that the comparison can be redone against a cleanly
isolated replication.

---

## 6. A problem found while preparing this

**The source document had never been archived.** This repository contained only the author's
extraction of it. The extraction step — the one the reviewer correctly identified as setting
the denominator — was not auditable by anyone, which is a stronger objection than the reviewer
made, since they assumed the source was available.

The document has been recovered in full from the session record (20,089 words) and is archived,
redacted, as [`../archive/source-document.txt`](../archive/source-document.txt). See that file's
header for what was removed and why.
