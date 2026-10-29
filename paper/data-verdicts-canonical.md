# Canonical verdict file

**One authoritative verdict per claim.** External review (M8) asked for this:

> The published audit and the published analysis script disagree about at least one verdict.
> … Reconcile, state the unit of analysis, and republish a single machine-readable verdict
> file that the audit and the scripts both derive from.

This is that file. Where it disagrees with any other file in the repository, **this one is
correct** and the other is being corrected.

## Unit of analysis

**The claim.** Two audit sections each cover two claim IDs under one shared verdict
(B4/B5 and D4/D5); the shared verdict is counted once for each claim it covers. So 61 claims
carry 59 distinct verdict determinations.

Codes: `S` verified · `P` partly true · `O` open · `N` not true · `X` no scientific basis.

## Per-claim verdicts

| Block | Claims | Verdicts |
|---|---|---|
| **A** | A1 P · A2 P · A3 N · A4 S · A5 S · A6 P · A7 N · A8 N | S2 P3 N3 |
| **B** | B1 S · B2 P · B3 S · B4 O · B5 O · **B6 N** · B7 P · B8 P · B9 N · B10 N · B11 N | S2 P3 O2 N4 |
| **C** | C1 S · C2 S · C3 S · C4 P · C5 N · C6 N · C7 S · C8 P · C9 N · C10 N · C11 S · C12 P · C13 N | S5 P3 N5 |
| **D** | D1 S · D2 P · D3 N · D4 S · D5 S · D6 X · D7 N | S3 P1 N2 X1 |
| **E** | E1 S · E2 N · E3 N · E4 N | S1 N3 |
| **F** | F1 S | S1 |
| **X** | X1–X17: two carry an established mathematical kernel (Whittaker decomposition; GEM substitution), fifteen have no scientific basis | P2 X15 |

## Totals

| Verdict | n | % |
|---|---|---|
| Verified | **14** | 23 |
| Partly true | **12** | 20 |
| Open | **2** | 3 |
| Not true | **17** | 28 |
| No scientific basis | **16** | 26 |
| **Total** | **61** | 100 |
| *Harm-flagged (overlapping)* | *9* | *15* |

## What this corrects

Three files carried three different codings of the same claims.

| Source | Block B | Block D | Totals |
|---|---|---|---|
| `INTEGRITY_AUDIT.md` scoreboard | S3 P4 O1 N3 | S2 P2 N2 X1 | 14/14/1/16/16 |
| The audit's own per-claim sections | S3 P3 O2 N3 | S3 P1 N2 X1 | 15/12/2/16/16 |
| `analysis-contingency.py` | S2 P4 O2 N3 | S2 P1 N3 | — |
| **This file (canonical)** | **S2 P3 O2 N4** | **S3 P1 N2 X1** | **14/12/2/17/16** |

Two substantive differences, and one that does not matter:

1. **B6 — the only consequential one.** The audit's section opens *"✅ VERIFIED as citation /
   ❌ NOT TRUE as the dominant mechanism."* The claim as inventoried asserts the
   dominant-mechanism reading, so under the worst-sub-claim-governs rule it is **N**. The
   scoreboard read the first symbol and scored it verified; the script scored it partly true.
   Canonical: **N**.
2. **Block D, one claim.** The scoreboard recorded one claim as partly true that its own
   section scores verified (D1, chloroplast CTB-proinsulin expression level). Canonical
   follows the section: **S**.
3. **D6 — no effect.** The audit section marks ⛔ no scientific basis; the script marks ❌ not
   true. Both are unsupported and both rank zero on the ordinal scale, so no reported figure
   changes. Canonical follows the section: **X**.

**Block B's open count was the double-counting artifact.** The scoreboard counted B4/B5 as one
open claim and balanced the block with an extra partly-true, which is how 61 claims came to
show only one open verdict.

## Effect on reported results

**On the central comparison: none.** The mechanism-versus-outcome analysis uses blocks
A, B, D, E and F, and the canonical file differs from the analysis script on exactly one claim
in that set — B6, which is in the mechanism stratum and moves from partly true to not true.
That change is already carried through every table in the manuscript as the "B6 recoded" row,
and it **weakens** the lenient result from 15/19 to 14/19.

**On Table 1 and the repository scoreboard: yes.** Partly true falls from 14 to 12, not true
rises from 16 to 17, and open rises from 1 to 2. Those are corrected wherever they appear.

**A standing caveat applies to all of it.** These counts are conditional on this repository's
segmentation, which two independent extractors did not reproduce — they found 258 and 237
claims where this file has 61. See [`data-reextraction.md`](data-reextraction.md). The
canonical file settles which verdict attaches to which claim; it does not settle what counts
as a claim.
