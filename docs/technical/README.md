# Technical doc set

**Audience:** scientists, engineers, graduate students — anyone who wants mechanism, numbers,
and citations rather than summary.

| Document | Covers |
|---|---|
| [Molecular architecture](molecular-architecture.md) | Sequence, disulfides, proinsulin and C-peptide, hexamer and zinc, analogue engineering, and the bovine A-chain error |
| [The receptor and the cascade](insulin-receptor-and-signaling.md) | IR structure and activation, PI3K-Akt-GLUT4, where the lipid lesion actually sits, Randle vs. signaling, contraction-mediated uptake |
| [Why the physics layer fails](why-the-physics-layer-fails.md) | Quantitative teardown of the 11.428 kHz claim, scalar waves, keratin transduction, and the Benveniste lineage |

The claim-by-claim scoring with verdicts and PMIDs is in
[`INTEGRITY_AUDIT.md`](../../INTEGRITY_AUDIT.md).

---

## The short version, for someone deciding whether to read further

**What the source gets right technically:**

- The disulfide topology (A6–A11, A7–B7, A20–B19) and why it is the central engineering problem
- Yeast secretion of a self-folding single-chain precursor as superior to *E. coli* inclusion
  bodies — correct, though already standard industrial practice rather than suppressed
  knowledge
- The DAG → PKC-θ → IRS-1 Ser1101 lesion in human skeletal muscle
- Contraction-mediated GLUT4 translocation as a genuinely separate pathway
- Insulin receptor structure and the activation-loop tyrosines
- Portal vs. peripheral insulin delivery as a real limitation of subcutaneous therapy
- C-peptide being bioactive rather than inert

**What it gets wrong, in descending order of how much it matters:**

1. **The entire physics layer.** 11.428 kHz is 267× below the lowest rotational transition
   insulin can have, the quantum is 5.65 × 10⁸ times smaller than kT, and the molecule's
   angular momentum randomizes ~10⁹ times per carrier cycle. The claim that this activates
   receptors without insulin is lethal to anyone who believes it.
2. **The A-chain sequence is bovine.** A8-Ala, A10-Val, paired with a human B-chain — a chimera
   that exists in no species, presented under human insulin's molecular formula.
3. **The liver arm of the lipid lesion** runs through INSR Thr1160, not IRS-1 — a correction
   Shulman's own lab published in 2016.
4. **IRS-1 Ser307 is not inhibitory in vivo.** Knock-in mice got *worse*, not better.
5. **Every clinical endpoint it cites as a success actually failed:** C-peptide (Cebix Phase
   2b, placebo won), glucose-responsive insulin (MK-2640, no glucose-dependent clearance in
   humans), hepato-preferential insulin (peglispro, discontinued for hepatic steatosis), oral
   insulin (Oramed Phase 3, missed primary endpoint).
6. **Transdifferentiated alpha cells are not immune-invisible.** Furuyama 2019's own Figure 5
   shows they are killed by preproinsulin-directed CTLs "similar to β-cells."

**The pattern worth noticing:** the source is strongest on *mechanism* and weakest on
*outcome*. Nearly every claim that fails does so at the point where a mechanism met a clinical
trial. That gap — between a physiologically correct idea and a drug that works in people — is
the real subject of this repository.
