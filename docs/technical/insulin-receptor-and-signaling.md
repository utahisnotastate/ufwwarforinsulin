# The receptor, the cascade, and where the lipid lesion actually sits

**Audience:** scientists, graduate students, anyone who wants the signaling detail.
**Claims addressed:** F1, B1–B6.

The source document's signaling section is a mix of correct current biology, correct biology
from 2008, and one claim whose functional direction was reversed by a knock-in mouse. Sorting
those apart is more instructive than either accepting or rejecting the whole thing.

---

## 1. Receptor activation requires mechanical work

The insulin receptor is a **constitutive (αβ)₂ heterotetramer** — a disulfide-linked dimer
even without ligand, which distinguishes it from the ligand-dimerized receptor tyrosine
kinases. Both subunits come from one *INSR* gene product cleaved at a furin site. UniProt
P06213: signal peptide 1–27, α-chain 28–758, β-chain 763–1382.

**Unliganded:** the ectodomain sits in an autoinhibited **inverted-V**, with the activation
loop obstructing the nucleotide site so that Tyr1162 cannot be phosphorylated in *cis*.

**Liganded:** insulin engages site 1 and site 2 asymmetrically, collapsing the ectodomain into
a **T-shape**. This juxtaposes the transmembrane helices, which juxtaposes the intracellular
kinase domains, which permits **trans-autophosphorylation** of the activation loop at
**Tyr1158, Tyr1162, Tyr1163**.

Structural anchors: Hubbard SR, *EMBO J* 1997;16(18):5572–81 (PMID 9312016); Hubbard SR, Wei L,
Ellis L, Hendrickson WA, *Nature* 1994;372:746–754; cryo-EM by Uchikawa E, Choi E, Shang G,
Yu H, Bai XC, *eLife* 2019;8:e48630.

### Numbering conventions — check which one a paper is using

| convention | activation-loop tyrosines |
|---|---|
| **Mature IR-B** (signal peptide removed; structural literature) | **Y1158, Y1162, Y1163** |
| Mature IR-A (exon 11 skipped, 12 residues shorter) | Y1146, Y1150, Y1151 |
| UniProt P06213 precursor (+27 aa signal peptide) | Y1185, Y1189, Y1190 |

The offsets are exact: 1158 + 27 = 1185; IR-B − 12 = IR-A. Older literature also uses
pre-signal-peptide numbering for other residues ("Tyr-960" = Tyr-999). The source's figures are
correct under the mature IR-B convention; it just doesn't say so.

Note also the juxtamembrane Tyr960 (IR-B mature) and the C-terminal Tyr1328/1334 — functionally
distinct from the activation loop and not interchangeable with it.

### Why this section matters for the physics claims

Activation is a **large-amplitude, asymmetric conformational rearrangement of a ~320 kDa
ectodomain**, driven by multivalent site-specific binding at ~10⁻¹⁰ M affinity — on the order of
55 kJ/mol of binding free energy, applied as shaped contacts.

Claim X9 asserts a spatially uniform oscillating field can produce the same rearrangement with
no ligand. It cannot, and the reason is structural rather than merely energetic: a uniform
field deposits energy isotropically and has no way to apply an *asymmetric* force along a
specific internal coordinate. See
[why the physics layer fails](why-the-physics-layer-fails.md).

For completeness: genuinely ligand-independent IR/IGF1R signaling *does* exist — but it
requires molecular engineering (membrane-anchored intracellular domains), not fields, and those
papers argue precisely that the ligand's role is to establish *geometry*. That is the thing a
field cannot supply.

---

## 2. The canonical cascade

```
insulin → IR (αβ)₂ → trans-autophosphorylation Y1158/1162/1163
   → IRS-1 / IRS-2 tyrosine phosphorylation (pYXXM motifs)
      → p85/p110 PI3K recruitment → PIP₃
         → PDK1 + mTORC2 → Akt
            → TBC1D4 (AS160) phosphorylation → Rab-GAP activity relieved
               → GLUT4 storage vesicle exocytosis → glucose uptake
            → GSK3 inhibition → glycogen synthesis
            → FoxO1 nuclear exclusion → ↓ hepatic gluconeogenic transcription
```

The MAPK/ERK branch runs in parallel off Grb2/SOS and carries the mitogenic rather than
metabolic output. The **balance between the PI3K and MAPK arms** is what determines whether
hyperinsulinemia is net vasodilatory (eNOS) or net harmful (endothelin-1, proliferation) — which
is why the source's selective presentation of only the harmful half is misleading.

---

## 3. The lipid lesion: where it is, and where the source puts it

### Muscle — the source is right

**DAG → PKC-θ → IRS-1 Ser1101** is supported *in humans*:

> Szendroedi J et al. (Shulman GI senior author). *"Role of diacylglycerol activation of PKCθ
> in lipid-induced muscle insulin resistance in humans."* **PNAS 2014;111(26):9597–602
> (PMID 24979806)**

Human lipid infusion → rise in cytosolic DAG → PKC-θ activation → ↑ IRS-1 Ser1101
phosphorylation → ↓ IRS-1 tyrosine phosphorylation. Same associations in insulin-resistant
obese and obese T2D subjects.

Worth noting: **no relationship with any muscle ceramide species** in this dataset. The source
lists "diacylglycerols and ceramides" together throughout; in human muscle the DAG evidence is
much stronger than the ceramide evidence.

### Liver — the source is a decade out of date

The source says PKC-ε serine-phosphorylates IRS-1 in hepatocytes. Shulman's own group moved the
hepatic lesion **off IRS-1 and onto the insulin receptor kinase itself**:

> Petersen MC et al. *"Insulin receptor Thr1160 phosphorylation mediates lipid-induced hepatic
> insulin resistance."* **J Clin Invest 2016;126(11):4361–71 (PMID 27760050)**

PKC-ε phosphorylates **INSR Thr1160** in the kinase activation loop; a phosphomimetic mutation
severely impairs kinase activity.

And this is itself unsettled. Brandon AE et al., *Cell Metab* 2019;29(1):183–191 found that
*global* but not *liver-specific* PKC-ε deletion protects mice, with no PKC-ε-dependent change
in receptor phosphorylation. A 2020 *Trends Endocrinol Metab* review describes the genetic and
phosphoproteomic data as in open conflict. **Treat the hepatic arm as open.**

### Ser307 — the cautionary tale

The source lists Ser307 among the inhibitory sites. Two separate problems:

**The numbering.** Mouse IRS-1 Ser307 ≡ **human Ser312**. (Human Ser307 corresponds to mouse
Ser302.) Secondary literature conflates these routinely.

**The function, which is worse.** The direction was reversed in vivo:

> Copps KD, … White MF. *"Irs1 serine 307 promotes insulin sensitivity in mice."*
> **Cell Metab 2010;11(1):84–92 (PMID 20074531)**

Ser307→Ala knock-in mice on a high-fat diet developed **more severe** insulin resistance than
controls. Mouse Ser307 is a *positive* regulatory site that limits the severity of insulin
resistance. Replicated in a liver-specific TSC1-depletion model (Herrema H et al., *BBRC* 2014).

The inhibitory story survives only in cell-free and overexpression systems.

**Ser612** (human; mouse Ser616) is most often attributed to ERK/MAPK and mTORC1-S6K. It
appears as a correlate of insulin resistance in human muscle but is not a validated PKC-θ
target and cannot carry the causal weight the source assigns it.

### Summary of corrections

| Source says | Current state |
|---|---|
| muscle: DAG → PKC-θ → IRS-1 Ser1101 | ✅ correct, human data |
| liver: DAG → PKC-ε → IRS-1 | ❌ → **INSR Thr1160**, and contested |
| IRS-1 Ser307 is inhibitory | ❌ knock-in mice say the opposite |
| IRS-1 Ser612 is a PKC-θ site | 🟡 associated; kinase attribution unclear |
| DAG *and ceramides* | 🟡 DAG evidence is much stronger in human muscle |

---

## 4. Randle vs. the signaling model

These are often presented as the same idea. They are not, and they make opposite predictions.

| | Randle (1963) | DAG–nPKC (current) |
|---|---|---|
| Mechanism | substrate competition — FA oxidation ↑ acetyl-CoA/citrate → inhibits PDH, PFK | signal transduction failure at IRS-1 / INSR |
| Rate-limiting step | glycolysis / hexokinase | **glucose transport (GLUT4)** |
| **Predicted intracellular G6P on lipid loading** | **rises** (hexokinase inhibited) | **falls** (transport limited upstream) |

³¹P-MRS in lipid-infused humans shows **G6P falls**. That single measurement is the decisive
discriminator, and it favors the signaling model in skeletal muscle.

Randle remains correct and operative in heart and in acute fatty-acid loading. Original:
Randle PJ, Garland PB, Hales CN, Newsholme EA, *Lancet* 1963;1(7285):785–9 (**PMID 13990765**).

A further irony the source would enjoy: several groups now argue that *reduced* capacity to
oxidize fat — mitochondrial dysfunction — rather than Randle's *elevated* FA oxidation is what
permits DAG to accumulate. That inverts Randle's own logic.

---

## 5. The second door: contraction-mediated uptake

Genuinely insulin-signaling-independent, and the source is right that it is under-taught.

```
muscle contraction
   → energy stress (↑AMP:ATP) → LKB1 → AMPK
   → Ca²⁺ release → CaMKII
   → Rac1 (cytoskeletal remodeling)
        ↓
   TBC1D1 (Ser231) and TBC1D4 (Thr642) phosphorylation
        ↓
   GLUT4 translocation — no IR, no IRS-1, no PI3K, no Akt required
```

Three corrections to the source's version:

1. **CaMKII, not CaMKK.** CaMKK2 is an upstream AMPK kinase; the better-supported Ca²⁺-arm
   effector for TBC1D1/TBC1D4 during contraction is CaMKII. LKB1 is the dominant upstream AMPK
   kinase in muscle.
2. **TBC1D1 ≠ TBC1D4.** In glycolytic muscle, TBC1D1 is the contraction-relevant isoform;
   TBC1D4/AS160 is more insulin-relevant. They are not interchangeable.
3. **Rac1 is a required third limb** and is omitted entirely (Kjøbsted R et al., *Diabetes*
   2021;70(12):2796).

Also: AMPK is modulatory rather than obligatory. TBC1D1/AS160 phosphorylation is *transient*
despite *sustained* AMPK activation, so "contraction clears glucose via AMPK" as a simple
causal chain overstates the evidence.

### ☠️ The clinical inversion that matters

Contraction-mediated uptake is insulin-**signaling**-independent. It is **not**
insulin-independent.

It requires a permissive amount of circulating insulin. In frank insulin deficiency, exercise
**raises** blood glucose and ketones: counter-regulatory hormones drive hepatic glucose output
and lipolysis, and absent insulin cannot restrain ketogenesis. The ADA position statement
(Colberg SR et al., *Diabetes Care* 2016;39(11):2065–79) advises checking ketones for
unexplained hyperglycemia ≥250 mg/dL and warns explicitly that omitting insulin before exercise
drives glucose up.

A reader who takes "non-insulin-dependent glucose disposal" as a clinical option in Type 1
diabetes will get ketoacidosis, not euglycemia. The phrase is accurate about a pathway and
catastrophically misleading about a therapy.

---

**See also:** [molecular architecture](molecular-architecture.md) ·
[why the physics layer fails](why-the-physics-layer-fails.md) ·
[`../../INTEGRITY_AUDIT.md`](../../INTEGRITY_AUDIT.md)
