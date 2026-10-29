# paper/ — manuscript, data and analysis

| File | What it is |
|---|---|
| **[MANUSCRIPT.md](MANUSCRIPT.md)** | **The full draft.** ~4,100 words, 6 tables, 11 references. §7 says what to cut for a 2,000-word *BMJ* Analysis version |
| [PROPOSAL.md](PROPOSAL.md) | Title strategy, journal targets, submission checklist |
| [RESULTS.md](RESULTS.md) | All four experiments written up, including the two that damaged the paper |
| [PREREGISTRATION-persona-rerun.md](PREREGISTRATION-persona-rerun.md) | Contamination check and stopping rules, **committed before the experiment ran** — the commit timestamp is the evidence |
| `data-claims-unlabelled.txt` | The 61 claims as given to the blinded raters. No verdicts |
| `data-rater-A.txt`, `data-rater-B.txt` | Independent blinded classifications |
| `data-persona-rerun-scoring.md` | Per-probe contamination and accuracy scoring, clean re-run |
| `analysis-kappa.py` | Cohen's κ. Reproduces **0.977** |
| `analysis-contingency.py` | Blinded contingency table and Fisher's exact. Reproduces **p = 2.2 × 10⁻⁴** |

```bash
python analysis-kappa.py data-rater-A.txt data-rater-B.txt out.json
python analysis-contingency.py
```

---

## The finding

A long AI-generated document on insulin was accurate about **mechanism** and categorically
wrong about **clinical outcome**:

| | Supported |
|---|---|
| Biological mechanism | **15 / 19 (79%)** |
| Specification — qualitative | 5 / 6 (83%) |
| Physical theory | 2 / 17 (12%) |
| **Therapeutic outcome in humans** | **0 / 8** |
| **Specification — quantitative** | **0 / 9** |

Blinded, κ = 0.977. Fisher's exact *p* = 2.2 × 10⁻⁴.

**Claims asserting a human outcome or a specific number were unsupported in 17 of 17
attempts.** Descriptive claims scored 79–83%.

## The four experiments, and what each did to the paper

| | Result | Effect |
|---|---|---|
| 1. Claim-level audit | 61 claims scored | the observation |
| 2. Blinded classification | κ = 0.977 | **weakened it** — 93%/0% → 79%/0%, and revealed the unblinded pass had over-assigned OUTCOME to claims already scored false |
| 3. Neutral re-query | 6/6 accurate | **falsified the explanation** — the corpus-bias hypothesis predicted the dissociation would persist. It did not |
| 4. Persona re-query | 0/6 adopted, 6/6 accurate | first attempt discarded (4/6 contaminated); clean replication valid (0/6) |

Two of four damaged the paper's original claims. Both are reported.

## Two errors found and logged during the work

1. **MK-2640's chemistry was misattributed** — it is mannose-receptor-cleared, not a
   phenylboronic-acid construct. Caught by a model being used as an experimental subject.
2. **An earlier draft understated its own contamination** as "at least two of six" when it
   was four.

Both in [`../CORRECTIONS.md`](../CORRECTIONS.md), with the original wording preserved rather
than overwritten.
