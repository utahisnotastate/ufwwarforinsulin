# The purity gap

**Audience:** bioprocess engineers, molecular biologists, community-lab organizers, and anyone
who has read a protocol for yeast-secreted insulin and thought *this doesn't look that hard.*

**Thesis:** the biology is the easy part and it really is nearly as easy as it looks. The gap
between "there is insulin-like protein in this liquid" and "this liquid can be injected into a
human" is **three to six orders of magnitude on every axis that matters**, and this document
quantifies each one.

This is not a legal disclaimer. It is a spec sheet. If you are building toward legitimate
small-scale insulin production — which is a worthwhile goal and real organizations are pursuing
it — this is the list you are actually building toward.

---

## 0. The finding that reframes everything

Before the contamination numbers, the molecule itself.

The species *Komagataella phaffii* secretes under the single-chain insulin precursor (SCIP)
design is **not insulin**. It is a single-chain precursor in which the B-chain C-terminus is
tethered to the A-chain N-terminus by a short linker.

Single-chain insulins with very short B29→A1 linkers have **drastically reduced insulin
receptor affinity.** The reason is structural: receptor engagement requires the B-chain
C-terminal segment (B24–B30) to detach from the hydrophobic core and swing away, exposing the
site-1 binding surface. A three-residue tether physically prevents that detachment.

This is why Novo Nordisk's industrial process contains a tryptic transpeptidation step at all.
The conversion is not a purification nicety. **The precursor is not therapeutically active, and
converting it is the point of the entire downstream process.**

Consequence: a gravity-filtered supernatant is not dilute insulin. It is a solution of mostly
*inactive* protein with an unknown minority of active species. Someone injecting it would
most likely be **under-dosing**, and the clinical endpoint of under-dosing in Type 1 diabetes
is diabetic ketoacidosis — which develops in hours, not days.

The intuitive fear is overdose. The likely failure mode is the opposite, and it is just as
lethal.

---

## 1. Endotoxin

### The limit

| | |
|---|---|
| General parenteral threshold | **K = 5.0 EU/kg/hr** (USP ⟨85⟩) |
| Systemic ceiling, 70 kg adult | **350 EU/hr** |
| USP insulin monograph | **NMT 80 EU per 100 insulin units** → ≤80 EU/mL at U-100 |

*(Verify monograph figures against current USP–NF; limits are revised.)*

### What a culture carries

*E. coli* fermentation broth routinely runs **10⁶–10⁸ EU/mL**. Meeting the limit requires
**4–6 logs of endotoxin clearance**, and that clearance is delivered by multi-step
chromatography — the exact steps the "desktop" protocol deletes.

A 0.1 mL injection (10 IU at U-100) drawn from a supernatant at a *conservative* 10⁴ EU/mL
delivers **1,000 EU** — roughly **3× the hourly pyrogenic threshold for a 70 kg adult**. At
10⁶ EU/mL it is 300×. Clinically: rigors, fever, tachycardia, hypotension, and at the top of
that range a septic-shock-like presentation.

**Endotoxin is not removed by 0.22 µm filtration, by autoclaving, or by boiling.** It is stable
to 250 °C. The filter removes the cells that made it and leaves the molecule behind.

### The yeast caveat, which cuts both ways

*Pichia* produces no LPS. This is a genuine and underappreciated advantage of the yeast route,
and it is a real argument for it.

But three things undercut it:

1. Any Gram-negative bioburden in a non-GMP fermentation contributes LPS directly. A
   non-sterile bench process is not a closed system.
2. **β-1,3-glucans and mannans shed from the yeast cell wall are pyrogenic and
   immunostimulatory in their own right.** They pass a 0.22 µm filter freely.
3. β-glucans activate the *Limulus* amebocyte lysate cascade through **Factor G**, producing
   **false-positive endotoxin readings.**

Point 3 is the cruel one. The single test a well-equipped community lab might actually run —
an LAL assay — returns an uninterpretable number on exactly this sample type unless you use
glucan-blocking buffer or recombinant Factor C. So the operator gets a reading, and the reading
is wrong, and nothing about the reading announces that it is wrong.

---

## 2. Host cell protein and host DNA

| Attribute | Expectation | Filtered supernatant | Gap |
|---|---|---|---|
| HCP | **≤100 ppm** (ICH Q6B practice; often ≤10 ppm) | 8% impurity at the claimed "92% pure" = **80,000 ppm** | **800–8,000×** |
| HCP, realistic | same | 1.5 g/L product vs 0.3–1 g/L HCP = **2–6 × 10⁵ ppm** | **10³–10⁴×** |
| Residual DNA | **≤10 ng/dose, ≤200 bp** | µg–mg/mL, full-length | **10³–10⁶×** |

### On the "92% purity after a 0.22 µm filter" claim

A 0.22 µm filter is a **cell-removal step**. It is not a purification step. It removes
essentially none of:

- soluble host cell protein
- host DNA
- endotoxin and β-glucans
- residual methanol and its oxidation products (formaldehyde, formate)
- antifoam, biotin, and PTM1 trace-metal salts (Cu, Co, Mo, Mn, Zn, Fe, iodide, boric acid)
- **secreted yeast proteases**, which keep clipping your product in the vial after you fill it
- hyperglycosylated precursor from incomplete Kex2 processing

The 96% purity figure in the source literature (Gurramkonda et al. 2010) was achieved **after
IMAC capture**, not after a filter.

And "purity" read off a Coomassie gel is ±10–20% and **blind to disulfide isomers, deamidated
species, and clipped forms that co-migrate.** A280 is useless for quantitation here. You can
have a beautiful single band that is 100% wrong molecule.

---

## 3. Sterility

USP ⟨71⟩ requires 14-day incubation in two media with defined container counts. But the
important point is that **⟨71⟩ is a statistically weak destructive test that cannot detect
low-level contamination.** Sterility is assured by the *process*, not the test: terminal
sterilization to SAL 10⁻⁶, or validated aseptic processing with ISO 5 / Grade A fill,
environmental monitoring, operator qualification, and routine media fills.

A 0.22 µm filter is a sterilizing-grade filter only when it is an **integrity-tested, validated
filter** (challenged with *Brevundimonas diminuta* at ≥10⁷ CFU/cm²) **discharging into a
pre-sterilized container inside a Grade A zone.** A syringe filter into a clean-looking vial on
an open bench is a bioburden-reduction step with a comforting appearance. It also does not
remove mycoplasma.

And insulin is a **multi-dose** product, punctured 10–60 times over its in-use life. That
requires a preservative at a validated concentration passing **USP ⟨51⟩ Antimicrobial
Effectiveness Testing** — see §5.

---

## 4. Potency: the thing you cannot determine

**1 IU = 0.0347 mg of pure insulin** (28.8 IU/mg), per the 2nd WHO International Standard,
NIBSC 11/212.

*(The older 83/500 standard is labelled 0.03846 mg/IU ≈ 26 IU/mg because that material contains
water and salts. Confusing the two is a real and documented source of error.)*

USP requires potency at **95.0–105.0% of label claim**, determined by RP-HPLC against USP
Insulin Human RS, with high-molecular-weight proteins **NMT 1.7%**.

You cannot obtain IU/mL from mass, A280, Bradford, or a gel. You need quantitative RP-HPLC
against a reference standard, plus identity by peptide mapping, intact-mass LC-MS, and
disulfide-bond mapping. The historical alternative is a rabbit or mouse bioassay.

**Why identity testing is not optional here:** disulfide isomers of correctly-sequenced insulin
have identical mass and near-identical gel mobility, and **near-zero potency**. Nothing short
of disulfide mapping or a bioassay distinguishes a correctly folded molecule from a scrambled
one. The one failure mode the yeast route is supposed to eliminate is precisely the one you
cannot detect without the instruments you were trying to avoid buying.

### What unknown potency does clinically

Set the scale first. The "1800 rule": one unit of rapid-acting insulin lowers blood glucose by
approximately 1800/TDD mg/dL. For an adult with a total daily dose of 40 U, **1 unit ≈ 45
mg/dL (2.5 mmol/L).** Normal fasting glucose is 80–100 mg/dL.

**The entire safe operating window is about two to three units wide.**

**If the vial is stronger than labeled.** ADA hypoglycemia levels: Level 1 <70 mg/dL, Level 2
<54 mg/dL (clinically significant), Level 3 severe (altered status, requires assistance). A
2× potency error on a routine 10 U meal dose delivers 10 extra units ≈ **450 mg/dL of
unopposed glucose-lowering.** From 150 mg/dL that is profound neuroglycopenia: confusion,
seizure, coma, arrhythmia, death. Published overdose series show hypoglycemia **refractory for
days** — one case required sustained dextrose infusion and stress-dose corticosteroids after
900 U of glargine. Dose correlates with *duration* of risk more than peak severity. A home
glucagon kit is designed for a one- or two-unit miscalculation, not a formulation error.

**If the vial is weaker than labeled, or is mostly inactive precursor.** Hyperglycemia → DKA,
beginning within hours of absent basal insulin in Type 1. As established in §0, **this is the
likely case.**

**If potency varies between batches — the realistic case — it is the worst of the three.** No
titration is possible. The patient cannot learn their correction factor because it changes
under them. They oscillate between DKA and severe hypoglycemia with no stable reference. This
is precisely why potency *uniformity*, not average potency, is the regulated attribute.

---

## 5. Formulation: the source's numbers are harmful as written

| Component | Commercial | Source claim | Error |
|---|---|---|---|
| Zinc | **15–30 µg/mL** (Humulin R 15; Lantus 30) | **0.1 M = 6,538 µg/mL** | **218–436× too high** |
| m-cresol | **1.5–3.2 mg/mL** | "trace" | far too low |

### Why the microgram figure is the right one

U-100 insulin = 100 IU/mL × 0.0347 mg/IU = 3.47 mg/mL ÷ 5,808 g/mol ≈ **0.6 mM monomer**.
Commercial zinc at 15–30 µg/mL = **0.23–0.46 mM** = roughly **2–4 Zn²⁺ per hexamer** — the
classical two zincs plus modest excess. The chemistry is internally consistent at the microgram
scale and nonsensical at 0.1 M.

### What 0.1 M zinc acetate would actually do

1. **Precipitate the insulin.** A large molar excess drives amorphous precipitation. You get a
   suspension with unpredictable, markedly delayed absorption — an uncontrolled depot, not a
   soluble insulin.
2. **Injure tissue.** 1 mL delivers **6.5 mg elemental zinc**. Concentrated zinc salts are
   astringent and are used therapeutically as sclerosants and chemical ablatants. Expect pain,
   inflammation, induration, necrosis — and accelerated injection-site amyloid formation.
3. **Risk systemic zinc toxicity** with chronic multi-daily dosing, plus secondary copper
   deficiency.

### Why m-cresol is not "trace"

Commercial phenolic concentrations are **functional minimums** serving two separate purposes:

1. **Antimicrobial preservation** of a multi-dose vial — required, demonstrated by USP ⟨51⟩.
   "Trace" m-cresol fails ⟨51⟩, and an unpreserved vial punctured dozens of times is a reliable
   route to injection-site abscess and bacteremia.
2. **Conformational stabilization** — phenolic ligands bind the hexamer and drive the
   **T6 → R6 transition**, which is what suppresses fibrillation. Roughly three phenolic
   molecules per hexamer minimum.

So removing the preservative removes the anti-aggregation mechanism, which feeds directly into
the next section.

The source's formulation is therefore wrong in both directions at once: ~400× too much of the
component that precipitates the drug, far too little of the component that keeps it both
sterile and monomeric.

---

## 6. Immunogenicity: the irreversible one

Every other failure mode on this page is an acute event you can in principle survive and learn
from. This one is permanent.

**Aggregates are the best-established driver of protein-drug immunogenicity.** Aggregated
protein presents repetitive epitope arrays that cross-link B-cell receptors and can break
tolerance **even to a self-protein**.

**Insulin-derived amyloidosis** ("insulin ball") is documented, increasing, and specific: a
subcutaneous amyloid mass at injection sites, first reported in 1983, now **>75 published
cases**. Exogenous insulin misfolds into insoluble fibrils in the tissue. Clinically,
**insulin absorption at an affected site falls to ≤40% of normal**, producing erratic control
and apparent insulin resistance. Lesions can be impalpable and are routinely mistaken for
lipohypertrophy.

Now add the sequence error. The source specifies a **bovine A-chain** (A8 Ala, A10 Val) paired
with a human B-chain — see
[molecular architecture](../technical/molecular-architecture.md). Non-human A-chain epitopes are
the classic historical driver of anti-insulin antibody formation and immune insulin resistance.
This is the exact problem recombinant human insulin was invented to solve.

**The consequence of getting this wrong is not a bad week.** Anti-insulin antibodies can make a
person refractory to *all* insulin, including the pharmaceutical product that would otherwise
keep them alive. You cannot un-sensitize someone. There is no rescue.

---

## 7. Conversion kinetics: the protocol is 6–200× too fast

Published trypsin/carboxypeptidase B conversion conditions:

| Conditions | Time | Yield |
|---|---|---|
| 30 °C, trypsin 1 mg/L + CpB 4 mg/L | 4 h | 95% |
| pH 7.5, 25 °C, 10 mM H₂O₂ | 1 h | 90% |
| pH 8.5, 15 °C | 16 h | 77.7% |
| pH 9.0, 37 °C, 1:600 w/w | 5 h | >90% |
| pH 7.5, 37 °C, trypsin 1:100, CpB 1:400 | 30 min | — |

Range: **30 minutes to 16 hours.**

A single gravity pass at 1.0 mL/min over, say, a 5 mL bed gives **~5 minutes contact** — six to
two hundred times short of any published condition. Gravity flow also cannot be held at a
controlled rate as the bed compresses.

And even at correct residence time, the reaction generates characterized side products:

- **des-Thr(B30) insulin: 4–6%** from over-trypsinization — patent literature calls it
  "difficult and cumbersome" to remove
- **Arg(B31)-insulin and Arg(B31),Arg(B32)-insulin** from incomplete CpB trimming
- **A21-desamido insulin** from Asn-A21 deamidation
- miscleavage fragments, excised linker, unconverted precursor, aggregates, disulfide isomers
- **leached trypsin** — immobilized enzyme does leach; it is both an immunogenic impurity and
  an ongoing degradant source in the finished vial

Separating des-B30 and A21-desamido from product is the genuinely hard part of insulin
manufacturing, and the published reverse-phase step yields are only **54–82%**. The source's
protocol omits both the quench and the orthogonal polishing that accomplish it.

---

## 8. Cost: the real number, and why the real number is the better argument

| Basis | Cost per 1,000 IU vial |
|---|---|
| Source claim | <$0.008 |
| **Raw API alone**, at published export price ($24,750/kg × 34.7 mg) | **$0.86** |
| **Full production cost**, regular human insulin (Gotham et al. 2018) | **$2.28–3.37** |
| Open Insulin Foundation's own planning assumption | **$7.00** |

The claimed figure is **~86× below the cost of the drug substance by itself**, before vial,
stopper, label, fill-finish, sterile filtration, QC release testing, stability program, or cold
chain — and **228–337× below** a credible all-in production cost.

A charitable reading is that <$0.01 refers to marginal fermentation media per vial-equivalent
at bench scale. That number is approximately right and approximately meaningless, because media
is a negligible fraction of the cost of a *releasable* vial.

### Why overstating this is self-defeating

Post-2023 US list prices are roughly **$64–72/vial**, with **$35/month out-of-pocket caps** for
Medicare beneficiaries and, voluntarily, for many commercially insured and uninsured patients.

So the honest gap between production cost and patient cost is now roughly **one order of
magnitude at the margin**, substantially narrowed since 2023 — not the three or four orders the
source implies.

That is still a real grievance and the global picture is worse. But a document that claims a
1000× arbitrage loses exactly the readers who could check it, and those are the readers who
could actually build something. **The real number is damning enough and it has the advantage of
being true.**

---

## Summary: filtered supernatant vs. release criteria

| Attribute | Requirement | Gravity-filtered supernatant | Gap |
|---|---|---|---|
| **Active species** | mature two-chain insulin | single-chain precursor, largely inactive | **wrong molecule** |
| Endotoxin | ≤80 EU/mL | 10⁴–10⁸ EU/mL; glucans also break the assay | 10²–10⁶× |
| HCP | ≤100 ppm | 10⁵–10⁶ ppm | 10³–10⁴× |
| Host DNA | ≤10 ng/dose, ≤200 bp | µg–mg/mL, full-length | 10³–10⁶× |
| HMWP/aggregate | ≤1.7% | unmeasured, unbounded | ∞ |
| Sterility | SAL 10⁻⁶ / validated aseptic | non-validated filter, open bench | unassured |
| Preservative | validated, passes ⟨51⟩ | "trace" | fails |
| Potency | 95–105% of label | unknown and unknowable without HPLC | — |
| Identity | peptide map / intact MS | not performed | not established |
| Sequence | human | **bovine A-chain** | wrong protein |

---

## What this document is not saying

It is not saying small-scale insulin production is impossible or illegitimate. The Open Insulin
Foundation and similar groups are pursuing it seriously, and the strategic case — local,
community-governed supply — is sound.

It is saying that **the hard part is not the fermentation, and a protocol that skips
purification, conversion kinetics, potency assay, and formulation has not made insulin cheap.
It has made something else, and called it insulin.**

If you want the version of this that is a build plan rather than a warning, see
[what a real small-scale program needs](what-a-real-program-needs.md).

---

**Sources:** Gotham D, Barber MJ, Hill A. *BMJ Glob Health* 2018;3(5):e000850 · Siew YY, Zhang W.
*Bioresour Bioprocess* 2021;8:65 · Gurramkonda C et al. *Microb Cell Fact* 2010;9:31 (PMID
20465840) · Kjeldsen T. *Appl Microbiol Biotechnol* 2000;54(3):277–286 · Rosenberg AS. *AAPS J*
2006;8(3):E501–507 · Ratanji KD et al. *J Immunotoxicol* 2014;11(2):99–109 · NIBSC 11/212 ·
USP ⟨51⟩, ⟨71⟩, ⟨85⟩ and the USP Insulin Human monograph · FDA, *Clinical Immunogenicity
Considerations for Biosimilar and Interchangeable Insulin Products*. Full list:
[`../../references/bibliography.md`](../../references/bibliography.md)
