# Molecular architecture of insulin

**Audience:** scientists, engineers, advanced students.
**Claims addressed:** C1, C2, F1.

---

## 1. Primary structure

Mature human insulin is a 51-residue two-chain polypeptide, 5807.6 Da, formula
**C₂₅₇H₃₈₃N₆₅O₇₇S₆**.

```
A-chain (21 aa)   G I V E Q C C T S I C S L Y Q L E N Y C N
                  1         6 7 8 9 10 11                20 21
                            │ │     │                    │
                            │ └─────┼────────────────────┼──── A7–B7   (interchain)
                            └───────┘                    │
                              A6–A11 (intrachain)        └──── A20–B19 (interchain)

B-chain (30 aa)   F V N Q H L C G S H L V E A L Y L V C G E R G F F Y T P K T
                  1         7                19                            30
```

Three disulfides, exactly as the source states:

| bond | type | role |
|---|---|---|
| **A6–A11** | intrachain | staples the A-chain's internal loop |
| **A7–B7** | interchain | joins the chains |
| **A20–B19** | interchain | joins the chains |

Six cysteines, three bonds, and only one of the 15 possible pairings is correct. This is the
entire engineering problem of insulin production — see
[the manufacturing docs](../manufacturing/README.md).

### The source's sequence is not human insulin

The source gives the A-chain as:

```
G-I-V-E-Q-C-C-A-S-V-C-S-L-Y-Q-L-E-N-Y-C-N
                  ↑     ↑
                 A8    A10
```

Position **A8 = Ala** and position **A10 = Val**. Human insulin has **A8 = Thr** and
**A10 = Ile**.

Those two substitutions are not random. A8 Thr→Ala and A10 Ile→Val are precisely two of the
three differences that define **bovine insulin**:

| position | human | porcine | bovine | source |
|---|---|---|---|---|
| A8 | Thr | Thr | **Ala** | **Ala** |
| A9 | Ser | Ser | Ser | Ser |
| A10 | Ile | Ile | **Val** | **Val** |
| B30 | Thr | **Ala** | **Ala** | **Thr** |

The source's A-chain is bovine. Its B-chain terminates in Thr, which is human. The molecule it
specifies is a **bovine-A / human-B chimera that does not occur in nature**, presented under a
molecular formula (C₂₅₇H₃₈₃N₆₅O₇₇S₆) that belongs to human insulin, in a protocol that
repeatedly promises "human-identical" and "clinical-grade" product.

This matters beyond pedantry:

- **It is the immunogenic difference.** Bovine insulin's greater sequence divergence from human
  is exactly why bovine-sourced insulin provoked more anti-insulin antibody formation and more
  injection-site reactions than porcine or human insulin, and why the industry moved off it.
- **It would propagate into the construct.** A synthetic ORF built from the sequence as written
  would express the wrong protein. No amount of correct downstream processing fixes a wrong
  gene.
- **It is diagnostic of provenance.** The error is the signature of text assembled from mixed
  sources rather than from a sequence database. Anyone treating the document as an engineering
  specification should treat this as a hard stop and verify every other number in it
  independently — which is what [`INTEGRITY_AUDIT.md`](../../INTEGRITY_AUDIT.md) does.

Canonical reference: UniProt **P01308** (*INS_HUMAN*), residues 90–110 (A-chain) and 25–54
(B-chain) of preproinsulin.

---

## 2. Proinsulin and the C-peptide

Insulin is not translated as two chains. The gene encodes **preproinsulin** (110 aa):

```
[signal peptide 24] – [B-chain 30] – [C-peptide 31] – [A-chain 21]
                       └──── RR ────┘           └──── KR ────┘
```

The signal peptide is removed co-translationally on entry to the ER. The remaining single chain
— **proinsulin** — folds there, and the C-peptide is what makes that folding reliable: it
tethers the A- and B-chain segments in proximity so protein disulfide isomerase can resolve the
correct disulfide pairing rather than one of the 14 wrong ones.

Then, in the secretory granule, two prohormone convertases cut it out:

- **PC1/3** cleaves at the B-chain/C-peptide junction (Arg31-Arg32)
- **PC2** cleaves at the C-peptide/A-chain junction (Lys64-Arg65)
- **Carboxypeptidase E** trims the exposed basic residues

Insulin and C-peptide are therefore secreted in **strict 1:1 molar ratio**. This is why serum
C-peptide is the standard clinical assay for endogenous insulin production — it is unaffected
by injected insulin and escapes hepatic first-pass extraction, so it reports beta-cell function
directly.

The source's instinct that the industrial process "discards" a functional molecule is correct
as a matter of fact. What C-peptide *does*, and what happened when it was given back to
patients, is covered in [the C-peptide file](../endocrinology/c-peptide-the-full-story.md) —
and the ending is not the one the source gives.

---

## 3. Quaternary structure and zinc

Insulin self-associates. At the concentrations inside a secretory granule or a pharmaceutical
vial, monomers dimerize through an antiparallel β-sheet at the B-chain C-terminus, and three
dimers assemble around **two Zn²⁺ ions** — each coordinated by the His B10 imidazoles of three
monomers — into a **hexamer**.

This is functionally important in two directions:

- **Storage.** The hexamer is compact, chemically stable, and resistant to fibrillation. It is
  how beta cells store insulin and how vials keep.
- **Activity.** Only the **monomer** binds the receptor. A subcutaneous depot of hexamers must
  dissociate before it works, and that dissociation is the rate-limiting step in the absorption
  kinetics of regular human insulin — the reason it has a 30–60 minute onset.

Essentially all rapid-acting analogues are engineered to destabilize this assembly:

| analogue | modification | effect |
|---|---|---|
| **lispro** | B28-B29 Pro/Lys inversion | disrupts the dimer interface |
| **aspart** | B28 Pro→Asp | charge repulsion at the dimer interface |
| **glulisine** | B3 Asn→Lys, B29 Lys→Glu | destabilizes self-association |

And the long-acting analogues run the other way, engineering *more* association or
albumin-binding to slow release:

| analogue | modification | effect |
|---|---|---|
| **glargine** | A21 Asn→Gly, +2 Arg at B-chain C-terminus | shifts pI to ~6.7; precipitates at subcutaneous pH |
| **detemir** | B30 removed, C14 myristic acid on B29 | reversible albumin binding |
| **degludec** | B30 removed, C16 diacid via γ-Glu on B29 | forms soluble multi-hexamer chains in the depot |

This table is the practical answer to a question the source never asks: insulin pharmacology is
not about the molecule's *activity*, which is fixed, but about controlling its **association
state** and therefore its absorption profile. That is where essentially all the real
engineering of the last thirty years has gone.

### On the source's formulation numbers

The source specifies **0.1 M zinc acetate** plus trace m-cresol for room-temperature stability.
0.1 M zinc is off by orders of magnitude from any pharmaceutical insulin formulation — real
products carry zinc in the range of tens of micrograms per 100 units, roughly stoichiometric
with the two Zn²⁺ per hexamer plus a modest excess. At 0.1 M you are far outside the
coordination regime and into territory where zinc precipitates protein non-specifically.
Scored in the [audit](../../INTEGRITY_AUDIT.md) and detailed in
[the formulation note](../manufacturing/formulation-and-stability.md).

---

## 4. The receptor (claim F1)

The source's description of the receptor is **correct**, which is worth stating plainly in a
document that spends a lot of time on what isn't.

The insulin receptor is a disulfide-linked **(αβ)₂ heterotetramer** — a constitutive dimer, not
a ligand-induced one. Both subunits derive from a single *INSR* gene product cleaved at a
furin site. The α-subunits are entirely extracellular and carry the binding sites; the
β-subunits span the membrane and carry a cytoplasmic tyrosine kinase domain.

In the unliganded state the ectodomain sits in an autoinhibited **inverted-V**. Insulin binding
— at the high-affinity "site 1" and the lower-affinity "site 2," engaged asymmetrically —
collapses this into a **T-shaped** active conformation. That collapse brings the transmembrane
helices together, which brings the intracellular kinase domains into contact, which permits
**trans-autophosphorylation** of the activation loop at **Tyr1158, Tyr1162, Tyr1163**.

Those residue numbers are correct under the mature-IR-B numbering convention. Be aware that the
literature also uses Tyr1146/1150/1151 (numbering from the mature receptor without the signal
peptide, or for IR-A which lacks exon 11's 12 residues) — the same three tyrosines, different
offset. If you are comparing papers, check which convention is in use.

Downstream, activated kinase phosphorylates IRS-1/IRS-2 on tyrosines, creating pYXXM motifs
that recruit the p85 regulatory subunit of PI3K → PIP₃ → PDK1 and mTORC2 → Akt → phosphorylation
of TBC1D4/AS160, relieving its Rab-GAP activity and releasing GLUT4 storage vesicles to the
plasma membrane.

**Why this matters for the physics claim.** Receptor activation is a mechanical event driven by
binding free energy — a ligand making specific contacts and paying roughly 55 kJ/mol to force a
large conformational rearrangement. Claim X9 asserts this can be produced by a far-field
oscillating potential with no ligand present. The conformational change has no coupling to such
a field; there is no mechanism by which an 11.428 kHz carrier applies a shaped force to the
ectodomain. Fully worked in
[why the physics layer fails](why-the-physics-layer-fails.md).

---

## References

- UniProt P01308 — INS_HUMAN
- Weiss MA, Lawrence MC. *A thing of beauty: Structure and function of insulin's "aromatic
  triplet."* Diabetes Obes Metab. 2018;20(S2):51–63.
- Uchikawa E, Choi E, Shang G, Yu H, Bai X. *Activation mechanism of the insulin receptor
  revealed by cryo-EM structure of the fully liganded receptor–ligand complex.* eLife.
  2019;8:e48630.
- Hua QX et al. — proinsulin folding and disulfide pairing.
- Full bibliography: [`../../references/bibliography.md`](../../references/bibliography.md)
