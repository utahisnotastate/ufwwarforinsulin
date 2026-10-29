# What a real small-scale insulin program needs

← [Manufacturing index](README.md) · [The purity gap](the-purity-gap.md)

The rest of this doc set is about why the source's protocol doesn't work. This page is the
constructive inverse: **if you wanted to actually do this, what would it take?**

The goal is legitimate. Local, community-governed insulin supply would be genuinely valuable,
especially outside high-income countries where the $35 caps don't reach and where cold chain is
the binding constraint. Organizations are pursuing it. This is the honest scope.

---

## The decision that comes first

**You are not building a way for individuals to make their own insulin.** That is not a
regulatory opinion, it is an engineering one: the release testing is irreducible, and it is
irreducible because each test corresponds to a way people have actually died. No amount of
decentralization removes the need to know the potency of a vial.

What you can build is a **small manufacturing entity** — a cooperative, a nonprofit, a
hospital pharmacy compounding operation, a national or regional producer — that serves a
population and carries the quality burden on their behalf. That is the Open Insulin model and
it is the right one.

Everything below assumes that frame.

---

## Stage 0 — Decide what molecule

| Option | Pros | Cons |
|---|---|---|
| **Regular human insulin (RHI)** | off-patent, simplest, USP monograph exists, reference standard available, WHO essential medicine | less convenient dosing profile than analogues |
| NPH | same, plus basal coverage | suspension — adds uniformity and resuspension QC |
| Analogues (glargine, lispro, aspart) | what patients actually use | patent landscape, harder characterization, higher API cost |

**Start with RHI.** The monograph exists, the reference standard is purchasable, the sequence
is unencumbered, and if your output can't pass the RHI monograph you have no business
attempting an analogue. Open Insulin went for analogues first and this is arguably why they
are still in R&D a decade in.

---

## Stage 1 — Strain and construct

- Host: *K. phaffii* (or *S. cerevisiae*) — secretory, no LPS, eukaryotic disulfide machinery
- Construct: α-factor pre-pro leader → Kex2 site → B-chain → linker → A-chain
- **Verify the sequence against UniProt P01308 before ordering the gene.** `GIVEQCCTSICSLYQLENYCN`
  for the A-chain. See [§4 of the manufacturing index](README.md#4-the-sequence-error) for why
  this warning is here.
- Linker choice is an empirical optimization, not a solved question. AAK is Novo's
  *S. cerevisiae* construct. Published *Pichia* work uses DGK, direct B29→A1 fusion, and
  charged N-terminal spacers to improve Kex2 processing. Screen several.
- Expect to spend real time on clone screening. Expression varies by orders of magnitude
  between integrants.

**Deliverable:** a sequenced, banked, characterized master cell bank with documented copy
number and stability over the intended number of generations.

---

## Stage 2 — Fermentation

Non-negotiable instrumentation:

- dissolved oxygen control with cascade, probably O₂ enrichment
- pH control
- temperature control
- methanol feed control (DO-spike or methanol sensor) if using AOX1; GAP avoids this
- antifoam addition
- the ability to hold >100 g DCW/L

A 5–20 L instrumented glass bioreactor is the realistic entry point. This is buyable used in
the low tens of thousands of dollars. It is not a countertop device and the published titers
are not achievable without this control.

**Target:** 1–3 g/L secreted precursor. **Deliverable:** a reproducible batch record.

---

## Stage 3 — Downstream (this is the actual product)

The source's protocol stops after a filter. Here is what has to be between the fermenter and
the vial:

1. **Clarification** — centrifugation or depth filtration, not gravity settling
2. **Capture** — IMAC or ion exchange. This is where your 4–6 logs of impurity clearance begin
3. **Conversion** — trypsin + carboxypeptidase B, or tryptic transpeptidation with a Thr-ester
   to install B30 directly. Residence time **30 min – 16 h** depending on conditions, not five
   minutes. Needs a defined quench
4. **Polishing** — orthogonal. Reverse-phase C8 **and** ion exchange. This is what separates
   des-Thr(B30) (4–6% of your material), Arg(B31)/di-Arg species, and A21-desamido from
   product. Published RP step yields are 54–82%, so plan your mass balance accordingly
5. **Crystallization** — zinc, at the right stoichiometry
6. **Formulation and sterile fill** — see [formulation](formulation-and-stability.md)

**Steps 2 and 4 are the ones that make it a drug.** Everything upstream makes it a protein.

---

## Stage 4 — Analytics, which you need before you need them

Buy or get access to these *before* your first batch, not after. A batch you cannot
characterize is a batch you have to discard, and discovering that at the end is how programs
die.

| Test | Instrument | Answers |
|---|---|---|
| **Potency / assay** | RP-HPLC vs USP Insulin Human RS | How many IU/mL — the single most important number |
| **Identity** | peptide mapping; intact-mass LC-MS | Is it the right molecule |
| **Disulfide mapping** | LC-MS/MS of non-reduced digest | Is it folded right — isomers have identical mass and no potency |
| **HMWP / aggregates** | SEC | ≤1.7% |
| **Related substances** | RP-HPLC | des-B30, A21-desamido, Arg species |
| **HCP** | process-specific ELISA | ≤100 ppm |
| **Residual DNA** | qPCR | ≤10 ng/dose, ≤200 bp |
| **Endotoxin** | LAL **with glucan-blocking buffer**, or recombinant Factor C | ≤80 EU/mL — and see below |
| **Sterility** | USP ⟨71⟩ | plus a validated aseptic process, because the test is weak |
| **Preservative efficacy** | USP ⟨51⟩ | multi-dose vials require this |
| **Residual trypsin** | ELISA or activity assay | immobilized enzyme leaches |

### The endotoxin trap, stated once more

If you use yeast, **a standard LAL assay will give you false positives** from β-1,3-glucans
activating Factor G. Use glucan-blocking reagent or recombinant Factor C from the beginning.
Otherwise you will get a number, it will be wrong, and nothing about it will look wrong.

An HPLC with a decent detector is the single highest-value purchase. Used systems are
affordable. **If you have one instrument, make it this one.**

---

## Stage 5 — Quality system

Not glamorous, genuinely load-bearing:

- master and working cell banks, with stability data
- batch records and change control
- validated aseptic process: ISO 5 / Grade A fill zone, environmental monitoring, operator
  qualification, **routine media fills**
- filter integrity testing (pre- and post-use)
- stability program — real-time and accelerated, to justify your expiry and storage claims
- deviation handling, and a defined recall path

The quality system is what converts "we made insulin once" into "this vial is what the label
says." That conversion is the entire product.

---

## Stage 6 — Regulatory

You will need a regulator. Which one depends on where you are and who you serve. Routes that
exist:

- **Biosimilar / follow-on** pathway in a jurisdiction with one
- **Hospital pharmacy compounding** under national rules, for a defined patient population
- **WHO prequalification**, if the target is LMIC supply
- **National producer** status, which several countries have pursued for insulin specifically

Di Franco's own framing is worth repeating: FDA approval is "another order of magnitude from
what we are trying to accomplish right now." He is right, and that is the honest statement of
where community biology currently sits relative to a licensed product.

**The most promising near-term route is probably not a new producer at all** — it is
technology transfer to an existing licensed manufacturer in a country that wants domestic
supply. Less romantic, far more likely to put insulin in someone's hand.

---

## Realistic budget and timeline

Open Insulin's own 2020 figures: **$200,000 used equipment** (≈$7–20 per patient served,
one-time) to **$1,000,000 new** (≈$73/patient), assuming $7/vial and 2 vials/patient/month.

They have been at it since 2015 and their current public position is that they remain
"primarily on technology research and development," with manufacturing "some way off."

That is not a failure. It is the actual difficulty of the problem, measured by people who are
seriously trying. Any plan that is dramatically cheaper or faster than this has left something
out, and the thing it left out is almost always analytics.

---

## The honest strategic assessment

Three things are true at once:

1. **The molecule is cheap.** $0.86 of API per vial. Full production cost $2.28–3.37. This is
   not in dispute.
2. **The quality burden is irreducible and is most of the cost.** Not because of bureaucracy,
   but because unknown-potency insulin kills people in both directions.
3. **In the US, the access gap has narrowed a lot since 2023** — list prices down 70–78%,
   $35/month caps. The remaining US gap is ~1 order of magnitude at the margin, concentrated
   among the uninsured and underinsured.

Which means the strongest case for decentralized production is **not** the US retail price. It
is:

- **LMIC supply**, where price and availability are both still binding
- **Cold chain independence** — and here the [thermostability
  evidence](formulation-and-stability.md) is genuinely encouraging and underexploited
- **Supply resilience** — a three-company global market is fragile, as several shortages have
  demonstrated
- **Governance** — communities owning their own supply is a real good independent of price

Lead with those. They are true, they are durable, and they don't collapse the moment a reader
checks the current price of a vial of Humulin.

---

← [Manufacturing index](README.md) · [Formulation and stability →](formulation-and-stability.md)
