# Integrity Audit

Every substantive claim in the source transmission, scored against the peer-reviewed
literature. Claim IDs refer to [`archive/source-claim-inventory.md`](archive/source-claim-inventory.md).

Verification was done in October 2026 against PubMed, PMC, *Nature*, *Science*, NEJM, *Lancet*,
ClinicalTrials.gov, UniProt, USP, and SEC filings. PMIDs are given where confirmed.

---

## Status key

| | Meaning |
|---|---|
| ✅ **VERIFIED** | Supported by peer-reviewed evidence, as stated |
| 🟡 **PARTLY TRUE** | Real underlying science; the claim overstates, misattributes, or is out of date |
| 🔵 **OPEN** | Plausible and under genuine investigation; not established |
| ❌ **NOT TRUE** | Contradicted by the evidence, or asserts something no study supports |
| ⛔ **NO BASIS** | No mechanism, no evidence; not a testable scientific claim as framed |
| ☠️ | **Harm flag** — acting on this claim could injure or kill someone |

## Scoreboard

| Block | Subject | ✅ | 🟡 | 🔵 | ❌ | ⛔ | ☠️ |
|---|---|---|---|---|---|---|---|
| A | Pathophysiology, portal delivery, C-peptide | 2 | 3 | 0 | 3 | 0 | 2 |
| B | Lipid lesion, non-insulin glucose disposal | 3 | 4 | 1 | 3 | 0 | 2 |
| C | Decentralized manufacturing | 5 | 3 | 0 | 5 | 0 | 1 |
| D | Delivery and next-generation molecules | 2 | 2 | 0 | 2 | 1 | 2 |
| E | Regeneration and cure | 1 | 0 | 0 | 3 | 0 | 1 |
| F | Insulin receptor | 1 | 0 | 0 | 0 | 0 | 0 |
| X | The physics layer | 0 | 2 | 0 | 0 | 15 | 1 |
| | **Total (61 claims)** | **14** | **14** | **1** | **16** | **16** | **9** |

**Roughly a quarter of the source's claims survive contact with the literature. Another fifth
are real science overstated. The remainder are wrong, and nine of them are wrong in ways that
can kill an insulin-dependent reader.**

---

## Block A — Pathophysiology, portal delivery, C-peptide

### A1 — Insulin resistance is a protective adaptation, not a breakdown
**🟡 PARTLY TRUE (genuinely contested)**

This is a real, published, non-fringe position. Hoehn KL et al., *"Insulin resistance is a
cellular antioxidant defense mechanism,"* **PNAS 2009;106(42):17787–92 (PMID 19805130)** is the
canonical mechanistic paper. Nolan CJ, Ruderman NB, Kahn SE, Pedersen O, Prentki M., *"Insulin
Resistance as a Physiological Defense Against Metabolic Stress,"* **Diabetes
2015;64(3):673–86 (PMID 25713189)** is the clinical-implications paper the source is effectively
echoing, and it does explicitly warn that overriding resistance with high-dose insulin may
provoke metabolic cardiomyopathy.

Three problems with the phrasing:

1. **"is *not* a biochemical breakdown"** is a false dichotomy. Even Nolan et al. treat
   resistance as adaptive at the cell level *and* pathological at the organism level over time.
2. **"protects mitochondria"** inverts the mechanism. In Hoehn 2009 mitochondrial superoxide is
   the upstream *signal*; the protected entity is the cell, not the mitochondrion.
3. The adaptive framing holds for an individual myocyte under acute nutrient excess. It is not
   an account of established Type 2 diabetes with beta-cell failure, where hyperglycemia
   damages end organs regardless of why it started.

The field's own current framing — see *"The insulin resistance mosaic: defect, defence or
both?"*, *Diabetologia* 2026 — is that the real question is *when* adaptation becomes
maladaptive.

### A2 — High glucose is an overflow metric, not the primary disease
**🟡 PARTLY TRUE.** Accurate as mechanism, dangerous as therapeutic inference. DCCT/EDIC and
UKPDS both show that lowering glucose reduces complications, whatever the upstream cause. A
reading that licenses leaving glucose high is not supported by anything.

### A3 — Exogenous insulin in T2D is an iatrogenic disaster ☠️
**❌ NOT TRUE — contradicted by randomized evidence**

| Trial | Result for insulin |
|---|---|
| **ORIGIN** (NEJM 2012;367:319–28, **PMID 22686416**) — 12,537 patients, glargine vs standard care, 6.2 y | **Neutral.** HR 1.04 (0.97–1.12). No excess cancer. Modest ↑ severe hypoglycemia, ~1.6 kg weight gain |
| **UKPDS 33** (Lancet 1998;352:837–53, **PMID 9742976**) | MI RR −16% (p=0.052); significant microvascular benefit |
| **UKPDS 10-year follow-up** (NEJM 2008;359:1577–89, **PMID 18784090**) | **Benefit:** MI ↓15%, diabetes-related death ↓17%, all-cause death ↓13% |
| **ACCORD** (NEJM 2008;358:2545–59, **PMID 18539917**) | ↑ mortality with intensive HbA1c target <6.0% |

ACCORD is the trial this argument usually leans on, and it is being misread. The ADA's own
epidemiological analysis found hypoglycemia did **not** explain the excess mortality, and that
the excess occurred among patients who *failed to reach* the target — tracking difficulty of
control, a marker of disease severity, rather than insulin exposure. ACCORD argues against an
aggressive HbA1c target in long-duration high-CV-risk T2D. It does not show insulin is
cardiotoxic.

The observational literature (notably Currie CJ et al., *JCEM* 2013;98:668–77, reporting
HR ~2.2 for all-cause mortality) is the source of the "insulin kills" narrative and is
explained by **confounding by indication** — insulin goes to patients with longer duration,
worse renal function, more comorbidity, and failed oral therapy. Randomized meta-analyses do
not reproduce it (20-RCT meta-analysis, *BMC Endocr Disord* 2016;16:39: all-cause mortality
RR 0.99).

**Sub-claims, scored separately:**

| Mechanism alleged | Verdict |
|---|---|
| Renal sodium retention | ✅ **VERIFIED** — DeFronzo's clamp work; ~35% fall in fractional sodium excretion. Genuinely real |
| Endothelial dysfunction | 🟡 Arcaro et al., *Circulation* 2002;105:576–82 shows hyperinsulinemia impairs endothelium-dependent vasodilation — but insulin is *also* an NO-mediated vasodilator via PI3K/Akt/eNOS. Presenting one half is selective |
| Receptor downregulation | 🟡 Real in cultured cells; not demonstrated as progressive loss of responsiveness in treated patients |
| Accelerated atherosclerosis | ❌ ORIGIN is the direct test, and it is negative |
| Vascular smooth muscle hypertrophy | ❌ In vitro at supraphysiological concentrations only |
| Beta-cell apoptosis | ❌ **Backwards.** "Beta-cell rest" with exogenous insulin *preserves* function — Weng J et al., *Lancet* 2008;371:1753–60, short-term intensive insulin in new-onset T2D produced ~45–51% one-year remission vs ~27% on oral agents |

**The defensible version:** escalating insulin to force normoglycemia in long-duration,
high-CV-risk Type 2 diabetes produces hypoglycemia and weight gain without cardiovascular
benefit. That is why current ADA/EASD guidance sequences metformin, GLP-1 receptor agonists,
and SGLT2 inhibitors ahead of insulin. It is an argument about **sequencing and targets**, not
about insulin being poison.

### A4 — 50–80% hepatic first-pass extraction
**✅ VERIFIED**, with a caveat: this is the high end of a published range running 40–80%, and
extraction **falls with obesity, hepatic steatosis, and T2D**. Write it as a range, not a
constant.

### A5 — Subcutaneous delivery abolishes the portal gradient
**✅ VERIFIED.** Native secretion gives roughly a 3:1 portal:peripheral gradient; subcutaneous
injection produces relative peripheral hyperinsulinemia with relative hepatic
hypoinsulinemia. This is a genuine, long-recognized limitation.

**But the translation record is the opposite of what the source implies.** See
[D-block](#block-d--delivery-and-next-generation-molecules) and
[the endocrinology set](docs/endocrinology/README.md): Lilly's **insulin peglispro** did exactly
what the theory predicted glycemically — better HbA1c than glargine, less nocturnal
hypoglycemia, weight *loss* — and was **discontinued in December 2015** because it raised
hepatic fat and ALT. Diasome's **HDV-insulin** met non-inferiority in a 2019 Phase 2b
(**PMID 31551249**) but showed *opposite-direction* hypoglycemia effects depending on baseline
HbA1c, and has still not started Phase 3 seven years later. **Zero hepato-preferential insulins
are approved.**

### A6 — C-peptide is bioactive, binds a GPCR, activates Na⁺/K⁺-ATPase and eNOS
**🟡 PARTLY TRUE**

- **Bioactivity in cells:** ✅ C-peptide raises Na,K-ATPase expression in human renal tubular
  cells and increases eNOS and NO release in aortic endothelial cells.
- **The GPCR:** ❌ The proposed receptor GPR146 **failed independent replication**. Lindfors L
  et al., *"Is GPR146 really the receptor for proinsulin C-peptide?"*, *Bioorg Med Chem Lett*
  2020;30(13):127208 (**PMID 32354568**) found no response up to 33 µM, no β-arrestin
  recruitment, no internalization. Even the pro-GPR146 camp concedes direct binding has never
  been demonstrated.
- Note the **bell-shaped dose-response** (effect at 1 nM but not 10 nM), which is itself a red
  flag for a conventional receptor mechanism.

### A7 — C-peptide deprivation is the primary etiology of diabetic microangiopathy ☠️
**❌ NOT TRUE**

DCCT/EDIC refutes this directly. In Type 1 diabetes, C-peptide is absent in *both* arms — yet
complication rates diverged by 60–76% on glycemic control alone. If C-peptide deficiency were
the primary cause, glycemic control should not have worked. It did.

**This is the most causally displacing claim in the document.** Believed, it would justify
relaxing glycemic control in Type 1 diabetes, which is the most direct route to harm in the
entire source.

### A8 — 1:1 C-peptide co-administration reverses basement membrane thickening ☠️
**❌ NOT TRUE — the definitive trial failed**

> Wahren J, Foyt H, Daniels M, Arezzo JC. *"Long-Acting C-Peptide and Neuropathy in Type 1
> Diabetes: A 12-Month Clinical Trial."* **Diabetes Care 2016;39(4):596–602 (PMID 26884473)**

This is the Cebix "Ersatta" (pegylated C-peptide) Phase 2b: 250 patients, 32 sites, 52 weeks.

- Sural nerve conduction velocity rose **1.0 ± 0.24 m/s on drug** vs **1.2 ± 0.29 m/s on
  placebo**. *The placebo group did better.*
- Modified Toronto Clinical Neuropathy Score: unchanged.
- Only vibration perception threshold improved — one secondary endpoint in a trial that missed
  its primary.

**Cebix shut down in February 2015, about 30 days after unblinding**, having raised ~$50M. The
CEO described drug and placebo as "indistinguishable." The senior author is John Wahren, the
field's principal advocate — this is not a hostile result.

Human efficacy data otherwise consists of four small studies totalling **n = 74**, graded weak
by meta-analysis (*PLoS One* 2015;10(5):e0127439). "Reverses" is unsupported in any human
study; the animal data show *prevention* of progression in young STZ rats, not reversal of
established lesions.

**Practical harm:** C-peptide is available from grey-market peptide suppliers. A document
asserting it reverses microangiopathy invites self-administration of unregulated injectables
for an indication where the one adequately powered trial failed.

---

## Block B — The lipid lesion and non-insulin glucose disposal

### B1 — DAG activates PKC-θ in muscle, PKC-ε in liver
**✅ VERIFIED.** The tissue–isoform pairing is correct and uncontroversial.

### B2 — IRS-1 inhibitory serine phosphorylation at Ser307, Ser612, Ser1101
**🟡 PARTLY TRUE — one site holds, one is weak, one is actively wrong**

- **Ser1101: ✅ VERIFIED, including in humans.** Szendroedi J et al. (Shulman senior author),
  *PNAS* 2014;111(26):9597–602 (**PMID 24979806**) — human lipid infusion → cytosolic DAG rise
  → PKC-θ activation → ↑ IRS-1 Ser1101 → ↓ IRS-1 tyrosine phosphorylation. (Notably: **no**
  relationship with any ceramide species in this dataset.)
- **Ser612: 🟡** Associated with insulin resistance in human muscle, but attributed to
  ERK/MAPK and mTORC1-S6K, not validated as a PKC-θ site.
- **Ser307: ❌ NOT TRUE, and the problem is worse than numbering.**
  - The numbering issue is real: **mouse IRS-1 Ser307 ≡ human Ser312.**
  - But the functional direction was *reversed in vivo*. Copps KD, … White MF, *"Irs1 serine
    307 promotes insulin sensitivity in mice,"* **Cell Metab 2010;11(1):84–92 (PMID 20074531)**
    — Ser307→Ala knock-in mice on a high-fat diet developed **more severe** insulin resistance.
    Mouse Ser307 is a *positive* regulatory site. The inhibitory story survives only in
    cell-free and overexpression systems.

### B2b — The liver arm runs through IRS-1
**❌ NOT TRUE — a decade out of date, and it misattributes a mechanism its own author replaced**

Shulman's group relocated the hepatic lesion from IRS-1 to the **insulin receptor kinase
itself**: Petersen MC et al., *"Insulin receptor Thr1160 phosphorylation mediates lipid-induced
hepatic insulin resistance,"* **J Clin Invest 2016;126(11):4361–71 (PMID 27760050)**. PKC-ε
phosphorylates **INSR Thr1160** in the activation loop.

This is itself contested — Brandon AE et al., *Cell Metab* 2019;29(1):183–191 found that
liver-specific PKC-ε deletion does *not* protect mice and detected no PKC-ε-dependent change
in receptor phosphorylation. Treat the hepatic arm as **🔵 OPEN**.

### B3 — Blocked PI3K-Akt, GLUT4 stranded in cytoplasm
**✅ VERIFIED.** Shulman's group specifically locates the rate-limiting defect at GLUT4
translocation / glucose transport.

### B4, B5 — The cell locks its gates to protect the respiratory chain; forcing glucose drives reverse electron transport and lethal ROS
**🔵 OPEN.** Mechanistically plausible and partly supported in vitro; the teleological framing
is not established. See A1.

### B6 — The Randle substrate conflict is the governing frame
**✅ VERIFIED as citation / ❌ NOT TRUE as the dominant mechanism**

Original: Randle PJ, Garland PB, Hales CN, Newsholme EA, *"The glucose fatty-acid cycle,"*
**Lancet 1963;1(7285):785–9 (PMID 13990765)**.

Randle remains correct as fuel-selection biochemistry and is still operative in heart and
acute fatty-acid loading. It is **not** the dominant account of human skeletal-muscle insulin
resistance, and the discriminator is clean: Randle predicts intracellular glucose-6-phosphate
should **rise** (hexokinase inhibition). ³¹P-MRS in lipid-infused humans shows G6P **falls**,
placing the lesion upstream at glucose transport. Randle and DAG-nPKC are not rival
explanations of the same measurement — they predict opposite signs, and the human data favor
the signaling model.

### B7 — Contraction activates AMPK/CaMKK → TBC1D1/TBC1D4, bypassing the insulin receptor
**🟡 PARTLY TRUE — correct in outline, three specific errors**

Contraction-stimulated glucose uptake is genuinely distinct from and additive to insulin
signaling, converges on the Rab-GAPs TBC1D1 and TBC1D4, and is **preserved in insulin-resistant
muscle**. That much is solid and is the physiological basis of exercise therapy.

Corrections:
- **CaMKK → CaMKII.** The Ca²⁺-arm effector for TBC1D1 Ser231 and TBC1D4 Thr642 during
  contraction is CaMKII. CaMKK2's role is comparatively weak; LKB1 is the dominant upstream
  AMPK kinase in muscle.
- **TBC1D1 ≠ TBC1D4.** TBC1D1 is the contraction-relevant isoform in fast muscle; TBC1D4/AS160
  is more insulin-relevant. The source treats them as interchangeable.
- **Rac1 is omitted** and is a required third limb (Kjøbsted R et al., *Diabetes*
  2021;70(12):2796).

### B8 — Acetate raises the AMP:ATP ratio and triggers AMPK
**🟡 PARTLY TRUE.** The mechanism is real — ACSS2 consumes ATP → AMP + PPi, a two-ATP-equivalent
hit, making acetate unusually effective at raising AMP per mole. Sakakibara S et al., *BBRC*
2006;344(2):597–604 (**PMID 16630552**) is the foundational rodent paper.

**But the entire chain is bovine hepatocyte plus diabetic mouse.** No human study shows dietary
or supplemental acetate raises muscle or hepatic AMP:ATP enough to activate AMPK in vivo.

### B9 — Acetate clears glucose at rates equal to or exceeding pharmacological insulin ☠️☠️
**❌ NOT TRUE — no supporting study of any kind exists, and the human evidence is null**

> Cherta-Murillo A, Pugh JE, Alaraj-Alshehhi S, Hajjar D, Chambers ES, Frost GS. *"The effects
> of SCFAs on glycemic control in humans: a systematic review and meta-analysis."* **Am J Clin
> Nutr 2022;116(2):335–361 (PMID 35388874)**

43 papers, 46 studies, n = 913. **Acetate: no significant effect on blood glucose.** Propionate:
none. The authors' conclusion is that SCFAs "had no effect on blood glucose and insulin in
humans."

The one exception is **vinegar**, which modestly reduces the acute postprandial glucose
response in IGT/T2D (SMD −0.53), graded *very uncertain*. And the mechanism is almost certainly
**delayed gastric emptying**, not AMPK-mediated disposal — vinegar *tablets* do not reproduce
the liquid effect, which is hard to explain any other way.

No clamp study has ever compared acetate-driven to insulin-driven glucose disposal. Pharmacological
insulin in a euglycemic clamp drives whole-body disposal to 10 mg/kg/min and above; no SCFA
intervention has approached any fraction of this.

**This is the single most dangerous sentence in the source document.** It should be deleted,
not qualified.

*(One thing the source could legitimately have argued: acetate is **antilipolytic** via
FFAR2/GPR43, lowering FFA delivery, which by the DAG model should improve insulin sensitivity.
That is the defensible pro-acetate case. Note it is typically followed by rebound hyperlipolysis
once acetate clears — the known failure mode of niacin and acipimox.)*

### B10 — Cold-induced non-shivering thermogenesis via UCP-1 oxidizes submembrane DAG
**❌ NOT TRUE as mechanism**

The anchor study is Hanssen MJW et al., *"Short-term cold acclimation improves insulin
sensitivity in patients with type 2 diabetes mellitus,"* **Nat Med 2015;21(8):863–865
(PMID 26147760)** — and it contradicts the claim's causal chain. Peripheral insulin sensitivity
rose ~43%, but the mechanism was **increased basal skeletal-muscle GLUT4 translocation**, with
**no change in insulin signaling, no change in AMPK activation, and only a minor increase in
BAT glucose uptake.**

It is a muscle effect, most likely from low-grade shivering — not UCP-1-mediated non-shivering
thermogenesis.

Replication is poor: *Nat Commun* 2021;12:1516 found **no effect** in the same population, and
a meta-analysis of cold-induced BAT activation in healthy humans (7 studies, n=85) found no
significant change in glucose, insulin, or triglycerides.

**On intramyocellular lipid specifically: no human trial has ever measured IMCL before and
after repeated cold exposure.** The claim has no supporting measurement.

### B11 — Restores glycemic sensitivity in 72–120 hours
**❌ NOT TRUE.** The one positive trial was **n = 8** over **10 days (240 hours)**, and failed
replication.

☠️ **Additional harm note:** prolonged self-administered cold exposure in diabetes carries
specific risks the general-population literature does not address — non-freezing cold injury
in peripheral neuropathy with impaired sensation, blunted thermoregulation in autonomic
neuropathy, and the fact that **cold-induced shivering, pallor, and confusion are
indistinguishable from hypoglycemia.**

---

## Block C — Decentralized manufacturing

Full technical treatment: [`docs/manufacturing/`](docs/manufacturing/README.md).

| ID | Claim | Verdict |
|---|---|---|
| **C1** | 51 aa, C₂₅₇H₃₈₃N₆₅O₇₇S₆, disulfides A6–A11, A7–B7, A20–B19 | ✅ **VERIFIED** |
| **C2** | A-chain sequence | ❌ **NOT TRUE — the sequence given is bovine** |
| **C3** | *E. coli* inclusion bodies, guanidine/urea, sulfitolysis, HPLC | ✅ chemistry / ❌ "all industrial insulin" |
| **C4** | The barrier is patents, not chemistry | 🟡 **PARTLY TRUE** |
| **C5** | Pichia SCIP folds correctly co-translationally | ✅ **VERIFIED** |
| **C6** | Secretion eliminates lysis and chaotropic denaturation | ✅ **VERIFIED** |
| **C7** | >92% pure after 0.22 µm gravity filtration | ❌ **NOT TRUE** |
| **C8/C9** | Single gravity pass, >95% yield, >200 cycles | 🟡 / ❌ kinetics 6–200× too fast |
| **C10** | 1.5 g/L from a desktop 5 L reactor | 🟡 conflates two different published figures |
| **C11** | <$0.008 per 1,000 IU vial | ❌ **NOT TRUE** |
| **C12** | 0.1 M zinc acetate, >180 days at room temperature | ❌ **NOT TRUE** ☠️ |
| **C13** | Feedstock <$0.005/L | ✅ trivially true, and misleading |

### C2 — The sequence is bovine ❌

| position | human | bovine | **source** |
|---|---|---|---|
| A8 | Thr | **Ala** | **Ala** |
| A10 | Ile | **Val** | **Val** |
| B30 | Thr | Ala | Thr |

A8-Ala and A10-Val are two of the three substitutions that define **bovine insulin**. Paired
with the source's human B-chain, the specified molecule is a **chimera occurring in no species**
(computed C₂₅₅H₃₇₉N₆₅O₇₆S₆, MW ≈ 5763.5) — while the document quotes the molecular formula and
mass of *human* insulin, an internal contradiction it never notices.

Anyone ordering a synthetic gene from that residue table gets the wrong molecule, and
animal-type A-chain epitopes are the classic driver of anti-insulin antibody formation and
immune insulin resistance. Correct: `GIVEQCCTSICSLYQLENYCN`.

### C3 — "The industry is trapped in the E. coli paradigm" ❌

The inclusion-body chemistry is accurately described. The framing is false: **roughly half of
the world's >40 tonnes/year of insulin is already made by secretory expression in
*S. cerevisiae*** (Novo Nordisk), and *Pichia*-derived insulin is commercial (Biocon,
Wockhardt). The source is describing current industrial practice and calling it suppressed
future knowledge.

### C7 — "92% purity after a filter" ❌
A 0.22 µm filter is a **cell-removal** step. It removes no soluble host cell protein, no host
DNA, no endotoxin, no β-glucans, no media components, no secreted proteases. The 96% figure in
the cited literature was achieved **after IMAC capture**. And 8% impurity = 80,000 ppm host
cell protein against a ≤100 ppm expectation.

**The deeper problem:** the secreted species is the single-chain *precursor*, which has
drastically reduced insulin receptor affinity because the short linker prevents the B-chain
C-terminal detachment that receptor binding requires. A filtered supernatant is not weak
insulin — it is mostly **inactive protein**.

### C11 — Cost ❌
Raw API alone, at published export prices, is **$0.86 per 1,000 IU vial**. Full production cost
for regular human insulin is **$2.28–3.37** (Gotham D, Barber MJ, Hill A, *BMJ Glob Health*
2018;3(5):e000850). The claim is **86× below the drug substance by itself** and **228–337×
below** a credible all-in cost. The Open Insulin Foundation's own planning figure is **$7.00**.

### C12 — 0.1 M zinc acetate ☠️
Commercial insulin carries **15–30 µg Zn/mL** (Humulin R 15, Lantus 30). 0.1 M is **6,538
µg/mL — 218 to 436× higher.** A 1 mL injection would deliver 6.5 mg of elemental zinc. Expected
effects: precipitation of the insulin into an uncontrolled depot, local tissue injury
(concentrated zinc salts are used as sclerosants), and chronic zinc toxicity.

Meanwhile "trace m-cresol" is far *too little* — commercial levels are 1.5–3.2 mg/mL, which are
functional minimums required both to pass USP ⟨51⟩ preservative efficacy and to maintain the
R6 hexamer state that suppresses fibrillation.

The 180-day room-temperature figure is roughly defensible — Cochrane 2023
(doi:10.1002/14651858.CD015385.pub2) found unopened human insulin stable up to 6 months at
25 °C — but that is a property of **properly formulated commercial insulin**, not a consequence
of adding zinc acetate, and it says nothing about microbiological integrity.

---

## Block D — Delivery and next-generation molecules

### D1 — Chloroplast CTB-proinsulin at up to 40% of total soluble protein
**✅ VERIFIED.** Boyhan D, Daniell H, *Plant Biotechnol J* 2011;9(5):585–598 reports proinsulin
at 47% of total leaf protein in tobacco and 53% in lettuce, with ~40% retained in dried
senescent leaves. The expression numbers are real and impressive.

### D2 — Oral delivery via CTB/GM1 binding into the hepatic portal vein
**🟡 PARTLY TRUE — and the source misdescribes what the experiment showed**

Ruhlman T, Ahangari R, Devine A, Samsam M, Daniell H, *Plant Biotechnol J* 2007;5(4):495–510 fed
powdered transgenic leaf to NOD mice and showed **prevention of pancreatic insulitis and
preservation of beta cells**, attributed to **Th2-mediated oral tolerance**.

That is immune tolerance induction to *prevent autoimmune diabetes onset*. It is **not**
glycemic control by orally absorbed insulin. These are different drugs with different
endpoints, and the source blurs them.

### D3 — Achieves oral, liver-targeted delivery for pennies, no refrigeration
**❌ NOT TRUE.** No registered human efficacy trial of chloroplast-derived insulin exists. The
platform has advanced to early clinical work for other indications; the insulin program did
not.

Oral insulin generally has failed repeatedly. **Oramed's ORMD-0801 Phase 3 (ORA-D-013-1,
n = 710) missed its primary endpoint in January 2023** and the program was discontinued — after
a positive Phase 2b (0.54% placebo-adjusted HbA1c reduction, p = 0.036) that did not replicate.
Novo's oral insulin 338 showed non-inferior HbA1c to glargine in Phase 2 (Halberg IB et al.,
*Lancet Diabetes Endocrinol* 2019;7(3):179–188) and was **discontinued on cost-of-goods
grounds** — ~1–2% oral bioavailability made the API requirement prohibitive. **No oral insulin
is approved anywhere.**

That last one is the most instructive data point in the whole field, and it inverts the
source's thesis: the science worked and the economics killed it.

### D4, D5 — PBA conjugation at B29; glucose displaces the boronate
**✅ VERIFIED as chemistry.** Hoeg-Jensen T et al., *J Pept Sci* 2005;11(6):339–46; Chou DH-C
et al., *PNAS* 2015;112(8):2401–2406 (**PMID 25675515**) — DCC/NHS coupling preferentially
acylates the ε-amine of LysB29.

Three constraints the narrative usually omits: PBA binds **fructose and lactate more tightly
than glucose** (so exercise, sepsis, or metformin perturb the sensor); unmodified PBAs have
pKa > 8.5 and bind diols poorly at physiological pH; and most published responsiveness is
measured at non-physiological glucose (~167 mM vs the real 4–20 mM range).

### D6 — Hypoglycemia is chemically impossible; a single depot lasts weeks ☠️
**⛔ NO BASIS as stated**

**No glucose-responsive insulin has ever worked in a human.** The one that was tested:

> Krug AW et al., *"Clinical Evaluation of MK-2640: An Insulin Analog With Glucose-Responsive
> Properties."* **Clin Pharmacol Ther 2019;105(2):417–425 (PMID 30125349)**

Merck acquired SmartCells for >$500M in potential milestones. In 16 adults with Type 1 diabetes,
MK-2640 showed **no detectable glucose-dependent change in clearance**, and was **~25-fold less
potent** than regular human insulin. Discontinued on efficacy grounds.

Novo's **NNC2215** (*Nature* 2024;634:944–951, PMID 39415004) is a genuine advance and is
frequently misreported. From the paper itself: receptor affinity rose 12.5-fold from 0→20 mM
glucose, but only **3.2-fold across the physiologically relevant 3→20 mM range** — a ~3×
modulator, not a switch. Absolute affinity is 0.75–9.2% of human insulin. **Rats and pigs only;
no human trial is registered.** The paper's own title claims "attenuation of hypoglycaemia," not
abolition.

Why "chemically impossible" cannot be true even in principle: every published GRI retains
baseline activity at euglycemia; a subcutaneous depot has no control over hepatic glucose
output, exercise, alcohol, or renal clearance; counterregulation is blunted in long-standing
T1D regardless of insulin kinetics; and **insulin already absorbed cannot be recalled.**

**On "a single depot lasting weeks" — the safety logic runs backwards.** The longest-acting
approved insulins are *once-weekly*, and in Type 1 diabetes they **increase** severe
hypoglycemia: in QWINT-5 (efsitora vs degludec, 52 weeks), severe hypoglycemia occurred in
**35/343 (10%) on weekly vs 11/349 (3%) on daily** (*Lancet* 2024). A long, non-retrievable
depot is a hypoglycemia risk factor, not a safety feature.

### D7 — Closed-loop pumps are a transitional technology with moderate hypoglycemia risk ☠️
**❌ NOT TRUE — and this is the most clinically consequential error in the document**

Automated insulin delivery is the best-evidenced therapy in Type 1 diabetes short of
transplantation.

- **Meta-analysis, 22 studies / 2,376 participants:** AID vs usual care gives **+10.9 percentage
  points time in range** and **HbA1c −0.37%**.
- **Karges B et al., *Lancet Diabetes Endocrinol* 2024** — DPV registry, 250 centres,
  **n = 13,922** young people: **hypoglycemic coma 0.62 vs 0.91 per 100 patient-years,
  IRR 0.68 (0.48–0.97) — significantly LOWER with closed loop.** TIR 64% vs 52%.
- Real-world: MiniMed 780G TIR ≈ 73% (4,120 users); Omnipod 5 TIR ≈ 64% with <1% time
  hypoglycemic (~70,000 users); NHS England pediatric rollout 49% → 63% at six months.

**On "sensor lag":** it is real, small, and explicitly modeled by the control algorithms. A
Dexcom G7 characterization found a 2-minute lag assumption minimized mean ARD; the widely
quoted "5–15 minutes" comes from consumer material.

**The one genuine caveat the source could have raised and didn't:** the same registry found
**DKA higher with closed loop — 1.74 vs 0.96 per 100 patient-years, IRR 1.81** — concentrated
in users with HbA1c ≥8.5%. That argues for ketone monitoring and training, not for abandoning
the technology.

Steering a person with Type 1 diabetes away from AID toward an unapproved modality is the
single most harmful piece of practical advice in the source.

---

## Block E — Regeneration and cure

### E1 — Alpha cells share a lineage with beta cells and are a renewable reservoir
**✅ VERIFIED**

### E2 — FoxO1 maintains alpha-cell identity by repressing Pdx1
**❌ NOT TRUE — wrong cell type, and the published direction is the opposite**

The Accili lab's FoxO1 work is in **gut/enteroendocrine progenitors**, not alpha cells:
Talchai C, Xuan S, Kitamura T, DePinho RA, Accili D, *"Generation of functional insulin-producing
cells in the gut by Foxo1 ablation,"* **Nat Genet 2012;44(4):406–412 (PMID 22406641)**.

The companion paper runs the *opposite* way from the claim: Talchai et al., *Cell*
2012;150(6):1223–1234 — beta-cell FoxO1 knockout causes **dedifferentiation**, with ~30% loss
of beta-cell mass and ~50% *increase* in alpha-cell mass. That is β→α, not α→β.

### E3 — Transient FoxO1 ablation plus Pdx1/Ngn3/MafA converts adult alpha cells in vivo
**❌ NOT TRUE as a combination.** No published study performed this experiment. It is a synthesis
of three separate literatures:

- **Thorel F, … Herrera PL,** *Nature* 2010;464:1149–1154 — α→β conversion after ablation of
  >99% of beta cells, **explicitly in the absence of inflammation or autoimmunity**. Only a
  small minority of alpha cells converted, recovering ~4–17% of beta-cell mass over months,
  with insulin support still required.
- **Furuyama K, … Herrera PL,** *Nature* 2019;567:43–48 (**PMID 30760930**) — human donor alpha
  cells reprogrammed with **PDX1 + MAFA** (not FoxO1, not Ngn3) secrete insulin
  glucose-responsively and reversed diabetes in mice for ≥6 months.
- **Zhou Q, Brown J, Kanarek A, Rajagopal J, Melton DA,** *Nature* 2008;455:627–632 — the
  Ngn3/Pdx1/MafA triad converts **acinar** cells, not alpha cells, in mouse.

### E4 — Converted cells are invisible to CD8⁺ T cells; permanent cure without immunosuppression ☠️
**❌ NOT TRUE — directly contradicted by the primary literature**

From **Furuyama 2019**, Figure 5, in a section the authors titled *"Insulin-secreting α-cells
are hypoimmunogenic"*: tested against HLA-A2-restricted beta-cell-specific CD8⁺ CTL clones from
patients with recent-onset Type 1 diabetes —

> **"Insulin-producing α-cells were sensitive to PPI-directed CTLs, similar to β-cells."**

Preproinsulin-reactive killing was essentially preserved. The authors' own word is "reduced
immunogenicity," not invisibility, and their experiments were in vitro with immunodeficient
NSG host mice, never autoimmune NOD.

And the logic is self-defeating: the entire point of the converted cell is that it makes
preproinsulin, and **preproinsulin is the dominant CD8 autoantigen in Type 1 diabetes.**

In vivo confirmation of relapse: Xiao X et al., *Cell Stem Cell* 2018;22(1):78–90 — intraductal
AAV-Pdx1/MafA normalized glucose in autoimmune NOD mice, but the effect and the new
insulin-producing cells **persisted only ~4 months before autoimmune diabetes returned.** The
senior author's own later review concedes the cells were likely recognized and destroyed, and
that immunogenicity "needs to be addressed before clinical use."

### What is actually working in humans

The source's cure narrative is wrong, but the real one is arguably more exciting — and the
difference is that it comes with a cost the source refuses to acknowledge.

| Therapy | Status | The catch |
|---|---|---|
| **Zimislecel (VX-880)**, stem-cell-derived islets — Reichman TW et al., *NEJM* 2025;393(9):858–868 | **10 of 12 insulin-independent at 1 year**; all 12 free of severe hypoglycemia, HbA1c <7%, TIR >70% | **Requires standard immunosuppression.** One death from cryptococcal meningitis attributed to the regimen. **Still investigational — not FDA-approved** |
| **VX-264**, same cells in an immunosuppression-free device | **Failed** — insufficient insulin production | The field has *not* solved immune protection |
| **Lantidra (donislecel)** | **FDA-approved 28 June 2023**, first allogeneic islet cell therapy | Lifelong immunosuppression; available at essentially one center |
| **Teplizumab (Tzield)** — Herold KC et al., *NEJM* 2019;381:603–613 (**PMID 31180194**) | Delays stage 3 onset: **48.4 vs 24.4 months**. Label expanded to age 1 (April 2026) and to newly diagnosed stage 3 in children (June 2026) | Delays; does not cure or reverse |
| **Harmine / DYRK1A inhibitors** | Strong preclinical beta-cell proliferation data (Stewart lab) | Phase 1 (NCT05526430, n=27) was **safety only, with no glycemic endpoint at all**. MTD 2.7 mg/kg, limited by vomiting and CNS effects — harmine is an MAOI and the active β-carboline in ayahuasca |

**The honest summary:** functional cures exist and work. Every one of them currently costs
immunosuppression, and the one program that tried to avoid it failed.

---

## Block F — The insulin receptor

### F1 — (αβ)₂ heterotetramer; trans-autophosphorylation at Tyr1158/1162/1163
**✅ VERIFIED.** Correct, including the residue numbers under the mature IR-B convention.

Worth noting for anyone comparing papers — the same three tyrosines appear under three
conventions:

| convention | residues |
|---|---|
| Mature IR-B (structural literature) | **Y1158, Y1162, Y1163** |
| Mature IR-A (exon 11 skipped, 12 shorter) | Y1146, Y1150, Y1151 |
| UniProt P06213 precursor (+27 aa signal peptide) | Y1185, Y1189, Y1190 |

A document asserting specific numbers should say which convention it means. The source does
not, but it is right.

---

## Block X — The physics layer

**⛔ NO BASIS — 15 of 17 claims.** **🟡 PARTLY TRUE — X8 and X13**, which have a genuine
established kernel wrapped in an unsupported extrapolation. ☠️ for X9 specifically.

Full quantitative treatment, with reproducible arithmetic:
[`docs/technical/why-the-physics-layer-fails.md`](docs/technical/why-the-physics-layer-fails.md).

### The two with a real kernel

- **X8 (scalar/longitudinal waves).** The **Whittaker decomposition is established mathematics**
  (1903–04) — a scalar potential in a source-free region can be written as paired
  counter-propagating wave sets. A bifilar coil really does cancel the far-field magnetic
  dipole. What is unsupported is that the remainder constitutes a channel carrying power or
  information; that is **testable with an expected null**, and a protocol exists (E005 below).
- **X13 (Q = G^(1/2)M).** Substituting √G·M for charge in Coulomb's law **does** reproduce
  Newton's law — legitimate algebra, and the basis of gravitoelectromagnetism, a real weak-field
  approximation of GR. What fails is the triple equality E = mc² = (c²/√G)Q, which is
  dimensionally inconsistent unless Q is given ad hoc units, and the reading of Q as
  "consciousness" in an interconversion law.

### Real physics adjacent to four other claims

Noted because a debunk that erases the real neighbors is less useful and less credible:

| Claim | The real thing nearby |
|---|---|
| **X4** super-radiant gain | **Dicke superradiance (1954) is real** — coherent sources add in amplitude, power scales as N². It's how phased arrays and lasers work. It does not apply to protein rotational states, which don't exist in water |
| **X5** keratin demodulation | **Electrophonic hearing is real** — perception from electrical and ultrasonic stimulation outside the ear canal; ultrasonic bone conduction (Lenhardt et al., *Science*, 1991). Puharich's patents are real history. Keratin acting as a demodulating diode is not demonstrated |
| **X7** meridians / cellulomas | **Skin impedance genuinely varies by location.** Whether acupuncture points specifically show lower impedance is **contested, not refuted** (Ahn et al., 2008 systematic review: inconsistent) |
| **X14** hyperchannel gain | **Inter-brain synchrony is real** — hyperscanning reliably shows neural synchronization during conversation, music, cooperation. Ordinary shared attention and timing, not an exponential channel |

### The 8.1 × 10²⁰ Hz claim, in one line

$$E = h\nu = 6.626\times10^{-34}\times 8.1\times10^{20} = 5.37\times10^{-13}\ \text{J} = \mathbf{3.35\ MeV}$$

Hard gamma radiation, above the pair-production threshold. Not a brain signal.

### Independently audited twice already

This physics layer is the same framework, from the same oracle persona, that was audited
claim-by-claim in two sibling repositories — both reaching the same verdicts:

- **[FallOfPhysics](https://github.com/utahisnotastate/FallOfPhysics)** — 11 experiment
  protocols (E001–E011), including null tests E005, E008, E009, E010, E011 that cover X6, X8,
  X10 and X14 directly.
- **[RiseOfGeometry](https://github.com/utahisnotastate/RiseOfGeometry)** — 31 disclosures,
  ~105 claims. D12 refutes the Eerkens maser with the same argument used here; D04 traces the
  "Fourth Law of Logic" to **T. E. Bearden's self-published work**; D27 covers keratin; D28
  covers Q = G^(1/2)M; D09/D21 cover the hyperchannel.

Full cross-mapping table and the runnable protocols:
[`docs/technical/why-the-physics-layer-fails.md#7-this-has-already-been-audited-twice`](docs/technical/why-the-physics-layer-fails.md#7-this-has-already-been-audited-twice).

**Provenance matters here.** The transmission is not retrieving future knowledge; it is
recombining an identifiable mid-century psychotronics corpus — Bearden, Dubrov, Inomata,
Eerkens, Puharich, Lisitsyn — almost all self-published or in non-indexed venues. Recognizing
the corpus is what makes it checkable.

The compressed version, on the central claim (X3, X9) that insulin has a characteristic
resonance at 11.428 kHz which can be broadcast into the body to activate receptors without
insulin:

| Test | Result |
|---|---|
| Is 11.428 kHz a rotational transition of insulin? | **No.** The lowest possible transition is 2B = 3.05 MHz. The claim is **267× below the entire spectrum** |
| Does the source's own formula give its own number? | **No.** It gives the rotational *constant*, and even then 62.9 kHz for the hexamer, not 11.428 kHz |
| Can the quantum compete with thermal noise? | **No.** kT/hν = **5.65 × 10⁸** |
| Is there a resonance to tune to in water? | **No.** Linewidth 57–136 MHz vs level spacing 3.05 MHz — lines are 19–45× broader than the gaps |
| Does phase coherence survive? | **No.** Angular momentum randomizes every 77–183 fs, ~10⁹ times per carrier cycle |
| Can the field couple selectively? | **No.** λ = 26 km vs a 2.4 nm molecule; uniform to 1 part in 10¹³ |
| Could a rotational frequency identify insulin anyway? | **No.** It depends only on the moment of inertia. Any similar-sized protein gives the same number |
| Does skin need a special transduction mechanism? | **No** — and this refutes the keratin story. Skin depth at 11.428 kHz is **3.84 m**; VLF passes through a body unattenuated |
| Can keratin rectify? | **No.** Piezoelectricity is linear (S = dE). Rectification requires a nonlinear asymmetric characteristic. This is a category error |

The "44-digit Lisitsyn code" `0x2A9C4F1B3E7` carries **42 bits — 5.25 bytes** of information,
against an *INS* promoter region spanning thousands of base pairs, read by transcription
factors through protein–DNA contacts. There is no demodulator in the nucleus.

The complex-thermodynamics and vacuum-energy material (X11–X13) relabels the second law and
then ignores it; the Dirac sea is not an energy reservoir; and Q = G^(1/2)M is dimensionally
inconsistent as written.

**Provenance:** this approach descends from Jacques Benveniste's "water memory" (failed
replication, *Nature* 1993) and Luc Montagnier's "DNA electromagnetic signals" (2009, never
independently replicated). The objection has been the same in every generation: **information
about a molecule is not a substitute for the molecule.**

---

## The nine sentences that could kill someone

Ranked by immediacy.

1. **B9** — acetate clears glucose at rates equal to or exceeding insulin. *No study supports
   this. The human meta-analysis is null.*
2. **X9** — the transducer activates receptors without insulin. *No mechanism. DKA in 12–48 h.*
3. **D7** — closed-loop systems are inferior transitional technology. *Steers people off the
   single best-evidenced therapy in Type 1 diabetes.*
4. **A3** — insulin therapy in Type 2 diabetes is an iatrogenic disaster. *Could prompt
   discontinuation → hyperosmolar state or DKA.*
5. **B7 framing** — "non-insulin-dependent glucose disposal." *True of the signaling pathway,
   catastrophically false as a clinical option: contraction-mediated uptake still requires
   permissive basal insulin to suppress ketogenesis. Exercising without insulin raises glucose
   and ketones.*
6. **A7** — C-peptide deficiency is the primary cause of microvascular disease. *Displaces
   glycemic control as the therapeutic target; refuted by DCCT/EDIC.*
7. **D6** — hypoglycemia is chemically impossible with glucose-responsive insulin. *False
   security about a drug class that has never worked in a human.*
8. **C12** — 0.1 M zinc acetate. *218–436× commercial levels; would precipitate the drug and
   injure tissue.*
9. **C11 + C7 together** — clinical-grade insulin from a filtered supernatant for under a cent.
   *Unknown potency, uncontrolled endotoxin, and a precursor that is mostly inactive.*

## The five best things in the source

Fairness matters here, because the document is not worthless and treating it as worthless is
both inaccurate and rhetorically self-defeating.

1. **The over-stuffed freight car.** The best explanation of lipid-overload insulin resistance
   in any register. Reused, with credit, in the [kids'](docs/kids/README.md) and
   [all-ages](docs/all-ages/README.md) documents.
2. **Yeast secretion over *E. coli* inclusion bodies.** Correct, important, and
   under-appreciated outside the industry — though already standard *inside* it.
3. **The C-peptide question.** Genuinely was dismissed as inert waste, genuinely is bioactive.
   The source just doesn't know how the story ends.
4. **Portal vs. peripheral insulin delivery.** A real, under-taught limitation of subcutaneous
   therapy.
5. **The price of insulin is indefensible.** True, consequential, and the legitimate grievance
   driving the whole document.

---

**See also:** [`SAFETY.md`](SAFETY.md) · [`README.md`](README.md) ·
[`references/bibliography.md`](references/bibliography.md)
