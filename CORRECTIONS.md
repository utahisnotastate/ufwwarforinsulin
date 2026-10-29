# Corrections

This repository's claim is that its verdicts are checkable. That is worth nothing unless
errors found in it are logged publicly, with what was wrong, how it was caught, and what
changed.

Newest first.

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

- **Eight unresolved citations** listed at the end of
  [`references/bibliography.md`](references/bibliography.md)
- **Two evidence gaps:** a national US insulin-rationing prevalence figure (Fang & Selvin,
  *JAMA* 2023, PMC10061307) and current HCUP DKA cost and volume data. The repository
  currently relies on a single-centre rationing study (n=199) and 2014 DKA charge data, and
  labels both as such
- **The paper's central confound:** model identity is confounded with prompting regime in
  [`paper/RESULTS.md`](paper/RESULTS.md). Stated in the abstract, not resolved
