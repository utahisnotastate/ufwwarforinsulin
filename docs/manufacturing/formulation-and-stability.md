# Formulation and stability

← [Manufacturing index](README.md) · [The purity gap](the-purity-gap.md)

**Claims addressed:** C12, and the cold-chain argument generally.

This is the part of the source material where a genuinely interesting and under-exploited truth
sits right next to a number that would injure someone. Both deserve attention.

---

## 1. What is actually in a vial

| Component | Typical concentration | Why |
|---|---|---|
| Insulin | 3.47 mg/mL (U-100) | the drug |
| **Zinc** | **15–30 µg/mL** | hexamer coordination — 2 Zn²⁺ per hexamer plus modest excess |
| **m-cresol / phenol** | **1.5–3.2 mg/mL** | preservative **and** conformational stabilizer |
| Glycerol | ~16–20 mg/mL | tonicity |
| Buffer | phosphate or Tris | pH ~7.0–7.8 (glargine is acidic, pH ~4) |

Representative products: Humulin R U-100 — zinc 0.015 mg/mL, metacresol 2.5 mg/mL. Lantus —
zinc 30 µg/mL, m-cresol 2.7 mg/mL, glycerol 85% 20 mg/mL, polysorbate 20 at 20 µg/mL.

### The stoichiometry check

U-100 = 100 IU/mL × 0.0347 mg/IU = 3.47 mg/mL ÷ 5,808 g/mol ≈ **0.6 mM insulin monomer**.

Zinc at 15–30 µg/mL (MW 65.38) = **0.23–0.46 mM** — i.e. **0.4–0.8 Zn per monomer, or roughly
2–4 Zn²⁺ per hexamer.**

That is exactly the classical two zincs per hexamer plus a working excess. The formulation
chemistry is internally consistent at the microgram scale, which is how you know the microgram
figure is the right one.

---

## 2. The source's 0.1 M zinc acetate ☠️

0.1 M Zn²⁺ = 0.1 mol/L × 65.38 g/mol = **6,538 µg/mL**.

| Comparison | Factor |
|---|---|
| vs Lantus (30 µg/mL) | **218×** |
| vs Humulin R (15 µg/mL) | **436×** |

As zinc acetate dihydrate (MW 219.5), 0.1 M is **21.95 g/L**, so a 1 mL subcutaneous injection
delivers **6.5 mg of elemental zinc**.

**What this would actually do:**

1. **Precipitate the insulin.** Zinc-insulin crystallization occurs at far lower zinc; a large
   molar excess drives amorphous precipitation. The result is a suspension with unpredictable,
   markedly delayed absorption — functionally an uncontrolled protamine-zinc-like depot, not a
   soluble insulin. You could not dose it.
2. **Injure tissue.** Concentrated zinc salts are astringent and are used therapeutically as
   sclerosants and chemical ablatants. Expect pain, inflammation, induration, and necrosis at
   injection sites — and accelerated injection-site amyloid formation as a consequence.
3. **Risk systemic zinc toxicity** with chronic multi-daily dosing, plus secondary copper
   deficiency.

---

## 3. "Trace m-cresol" is also wrong, in the other direction

Phenolic preservative is not an optional additive. It does two separate jobs, both load-bearing.

**Antimicrobial preservation.** Insulin is a multi-dose product, punctured 10–60 times over its
in-use life. The preservative must be at a concentration validated to pass **USP ⟨51⟩
Antimicrobial Effectiveness Testing** (USP and EP criteria differ; EP criterion "A" is
stricter). "Trace" m-cresol fails ⟨51⟩, and an unpreserved multi-dose vial punctured dozens of
times is a dependable route to injection-site abscess and bacteremia.

**Conformational stabilization.** Phenolic ligands bind the insulin hexamer and drive the
**T6 → R6 transition**, which is what suppresses fibrillation and aggregation. The literature
puts the minimum at roughly **three phenolic molecules per hexamer**, with ~23–35 mM preferred
when preservation sets the level.

So under-dosing the phenolic removes the anti-aggregation mechanism — which connects directly
to the immunogenicity problem in [the purity gap](the-purity-gap.md#6-immunogenicity-the-irreversible-one).
Aggregates are the best-established driver of protein-drug immunogenicity, and
insulin-derived amyloidosis at injection sites is documented in >75 published cases, reducing
absorption at affected sites to ≤40% of normal.

One manufacturing detail worth knowing: m-cresol **adsorbs onto silicone during filling**, so
as-filled concentration drops below formulated concentration. Commercial formulations carry
margin for this. It is a reason to be careful, not a reason to under-dose.

**Net: the source's formulation is wrong in both directions at once — roughly 400× too much of
the component that precipitates the drug, and far too little of the component that keeps it
sterile and monomeric.**

---

## 4. Thermostability: the part the source is right about, and it matters

The claim of "over 180 days at 20–25 °C" is **roughly defensible** — but not for the reason
given, and with conditions that matter.

### What the labels say

| | |
|---|---|
| **Unopened** | Refrigerate 2–8 °C until expiry |
| **In-use (opened)** | **28 days** at ≤30 °C for most vials. Levemir vials 42 days; Tresiba pens 56 days — product-specific |

Lantus, verbatim: *"Vials must be discarded 28 days after being opened... as long as the
temperature is not greater than 86°F (30°C)."*

### What the evidence actually shows

> **Kaufmann B, Boulle P, Berthou F, et al.** *"Heat-stability study of various insulin types
> in tropical temperature conditions."* **PLoS ONE 2021;16(2):e0245372**

MSF/Geneva. Logged real temperatures at **Dagahaley refugee camp, northern Kenya** — oscillating
**25–37 °C** — reproduced them in the lab, and tested the three human insulins MSF uses. Weekly
HPLC over four weeks: **full conformity to pharmacopoeia limits, <1% loss of activity in
cell-based assay, no significant conformational change by circular dichroism.** Opened vials
can be stored at least four weeks at tropical room temperature.

> **Richter B, et al.** *"Thermal stability and storage of human insulin."* **Cochrane Database
> Syst Rev 2023. doi:10.1002/14651858.CD015385.pub2**

17 studies, including previously unreleased manufacturer data from BIOTON, Eli Lilly, and Novo
Nordisk. Findings: **unopened vials and cartridges of specific human insulins can be stored up
to 25 °C for up to 6 months, and up to 37 °C for up to 2 months**, without clinically relevant
loss of activity. Opened containers at up to 37 °C for up to 12 weeks likewise showed no
clinically relevant reduction.

The review's own caveat: two studies reported up to **18% activity loss after 1 week to 28 days
at 37 °C**.

### What this means, stated precisely

1. The ~180-day figure applies to **≤25 °C, unopened, specific human insulin products** — not
   to anything at any temperature, and the evidence is weaker for analogues.
2. It is a property of **properly formulated, properly preserved commercial insulin**,
   including its normal 15–30 µg/mL zinc and 1.5–3.2 mg/mL phenolic. It is **not** a result of
   adding zinc acetate, and no evidence supports that intervention.
3. It is a **chemical potency** finding. It says nothing about **microbiological integrity**,
   which is what actually sets in-use dating for a multi-dose vial and which is governed by
   preservative efficacy.
4. Manufacturer labeling remains 28 days in use. Cochrane is an argument for **relaxing
   cold-chain requirements in low-resource settings**, not a license to re-label.

### Why this is the strongest real argument in the source's vicinity

The cold chain is a genuine, binding constraint on insulin access — in refugee settings, in
rural LMIC distribution, during power outages, in conflict zones. The MSF and Cochrane work
says the constraint is **substantially less tight than current labeling implies**, and that is
actionable right now with existing, properly made insulin.

That is a real finding with real humanitarian weight, and it requires no desktop bioreactor, no
novel formulation, and no regulatory revolution — just a change in guidance. The source gestures
at cold-chain liberation and then attaches it to a formulation that would precipitate the drug.
The genuine version is better and it is already published.

---

← [Manufacturing index](README.md) · [What a real program needs](what-a-real-program-needs.md)
