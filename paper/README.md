# paper/ — data and analysis

| File | What it is |
|---|---|
| [PROPOSAL.md](PROPOSAL.md) | Title, abstract, structure, journal targets, submission checklist |
| [RESULTS.md](RESULTS.md) | Both experiments, written up — including the one that falsified the hypothesis |
| `data-claims-unlabelled.txt` | The 61 claims as given to the blinded raters. No verdicts |
| `data-rater-A.txt`, `data-rater-B.txt` | Independent blinded classifications |
| `analysis-kappa.py` | Cohen's kappa. Reproduces 0.977 |
| `analysis-contingency.py` | Blinded contingency table and Fisher's exact. Reproduces p = 2.2e-04 |

Reproduce:

```
python analysis-kappa.py data-rater-A.txt data-rater-B.txt out.json
python analysis-contingency.py
```

Everything here is open so the analysis can be checked or attacked. The blinded
classification **weakened** the headline result and the replication **falsified** the
proposed explanation; both are reported rather than buried.
