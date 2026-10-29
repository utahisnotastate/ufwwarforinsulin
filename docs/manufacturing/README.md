# Making insulin — the insulin-maker doc set

**Audience:** bioprocess engineers, synthetic biologists, community-lab organizers, students of
pharmaceutical manufacturing, and anyone evaluating a decentralized insulin proposal.

| Document | What it covers |
|---|---|
| **This page** | How insulin is actually manufactured, and what the source gets right |
| [The purity gap](the-purity-gap.md) | Quantified: why a filtered supernatant is not injectable |
| [What a real program needs](what-a-real-program-needs.md) | The constructive version — a build plan |
| [Formulation and stability](formulation-and-stability.md) | Zinc, phenolics, cold chain, the 2021–2023 thermostability evidence |

**Read [`the-purity-gap.md`](the-purity-gap.md) before you read anything else as a protocol.**

---

## 1. What the source gets right

It is worth being precise about this, because the document's core technical instinct is
**correct** and it is the reason the rest of it is seductive.

**Yeast secretion of a single-chain precursor is the better route, and it is already
industrial.** The source frames this as suppressed future knowledge. It is neither suppressed
nor future:

| Manufacturer | Host |
|---|---|
| Eli Lilly | *E. coli* |
| Sanofi | *E. coli* |
| **Novo Nordisk** | ***Saccharomyces cerevisiae*** |
| **Biocon, Wockhardt** | ***Pichia pastoris / K. phaffii*** |
| Tonghua Dongbao | *Hansenula polymorpha* |

Global pharmaceutical demand now exceeds **40 tonnes/year, roughly half of it produced by
secretory expression in *S. cerevisiae***. *Pichia*-derived insulin has been on the market for
years.

So the claim "the industry is trapped in the E. coli inclusion-body paradigm" is simply false,
and the claim "yeast secretion eliminates the refolding problem" is true and has been
commercially exploited for decades. The source is describing the present and calling it the
future.

**The specific mechanism is right too.** Constraining the B- and A-chain segments with a short
linker does place the six cysteines in productive proximity, and the yeast ER's protein
disulfide isomerase does resolve the correct pairing (A6–A11, A7–B7, A20–B19) co-translationally.
The α-mating-factor pre-pro leader does direct secretion. These are real and well-published.

Key references: Kjeldsen T. *Appl Microbiol Biotechnol* 2000;54(3):277–286 · Gurramkonda C et al.
*Microb Cell Fact* 2010;9:31 (PMID 20465840) · Baeshen NA et al. *Microb Cell Fact* 2014;13:141.

---

## 2. The two routes, honestly compared

### *E. coli* inclusion-body route (Lilly, Sanofi)

```
transform → ferment → harvest → high-pressure lysis → isolate inclusion bodies
   → solubilize (6–8 M urea or GdnHCl, alkaline, + BME/DTT)
   → sulfitolysis (sulfite + tetrathionate)
   → dilution refolding (glycine-NaOH pH 10.5–10.8)
   → capture (IEX/IMAC) → trypsin + CpB conversion
   → polish (RP-C8, IEX, SEC) → Zn crystallization → formulate → fill
```

Refolding yield is strongly concentration-dependent and reported anywhere from 43% to 99%,
typically ~50% at 0.5 mg/mL and 30–40% at 1–2 mg/mL. This step is why the route is capital- and
volume-intensive.

### Yeast secretion route (Novo, Biocon, Wockhardt)

```
transform → fed-batch ferment → clarify (centrifuge/depth filter)
   → capture → trypsin transpeptidation or trypsin + CpB conversion
   → polish (RP, IEX) → crystallize → formulate → fill
```

Steps eliminated: lysis, chaotropic solubilization, sulfitolysis, in-vitro refolding. That is
a genuinely large simplification and it is the source's real insight.

Steps **not** eliminated: capture chromatography, enzymatic conversion, orthogonal polishing,
and every single release test. The source deletes all of these, and they are where the safety
lives.

---

## 3. Realistic numbers

| Parameter | Source claim | Published reality |
|---|---|---|
| Secreted precursor titer | 1.5 g/L from a desktop 5 L vessel | ~3 g/L precursor in broth under **instrumented fed-batch**; 1.5 g/L is the *finished purified insulin* figure after IMAC + conversion + polishing |
| Purity after 0.22 µm | >92% | filter removes cells only; 96% purity in the cited source came **after IMAC** |
| Conversion | single gravity pass, 1 mL/min | published residence times **30 min – 16 h** |
| Column reuse | >200 cycles | plausible for immobilized enzyme, but leaching must be assayed every cycle |
| Linker | Ala-Ala-Lys, presented as the *Pichia* standard | AAK is Novo's **MI3 construct in *S. cerevisiae***. *Pichia* work uses DGK, direct fusion, and charged spacers. No published head-to-head titer comparison found |
| Cost | <$0.008/1,000 IU | API alone **$0.86**; full production **$2.28–3.37** |

### On "desktop"

The published titers require dissolved-oxygen cascade control (>20–30% saturation, often with
O₂ enrichment), pH control, antifoam, cell densities above 100 g DCW/L, and methanol feed
control by DO-spike or methanol sensor. A shake flask or an uninstrumented carboy will not
approach them. This should be stated plainly rather than implied away — a 5 L instrumented
bioreactor is a real and buyable piece of equipment, but it is not a countertop appliance and
pretending otherwise sets up a failure that looks like a biology problem when it is an
engineering problem.

---

## 4. The sequence error

The source's A-chain is **bovine**:

| position | human | bovine | source |
|---|---|---|---|
| A8 | Thr | **Ala** | **Ala** |
| A10 | Ile | **Val** | **Val** |
| B30 | Thr | Ala | Thr |

Paired with the human B-chain it specifies a **chimera that occurs in no species** (computed
C₂₅₅H₃₇₉N₆₅O₇₆S₆, MW ≈ 5763.5), while quoting the molecular formula and mass of *human* insulin
— an internal contradiction the document never notices.

**Anyone ordering a synthetic gene from that residue table receives the wrong molecule**, and
animal-type A-chain epitopes are the classic driver of anti-insulin antibody formation and
immune insulin resistance. Correct sequence: `GIVEQCCTSICSLYQLENYCN`.

Full treatment: [molecular architecture](../technical/molecular-architecture.md).

---

## 5. Open Insulin

The Open Insulin Foundation is real: founded 2015 by Anthony Di Franco at Counter Culture Labs
in Oakland, now with participating labs in Oakland, Baltimore, and Paris. Stated goal is *"a
small-scale, community-centered model for insulin production, so that communities in need have
local, affordable, high-quality insulin that they own and govern."* They have engineered
microorganisms to produce glargine and lispro analogues.

Two things worth getting right about them:

**Their own cost model assumes $7.00 per vial** — 700× the source document's figure. Their 2020
estimate for a production facility was $200,000 in used equipment or up to $1,000,000 new.
These are the numbers of people who have actually costed the problem.

**Their model is cooperative, community-owned production — not individual home manufacture.**
We could not locate any public statement from them endorsing or addressing DIY
self-administration, and we are not attributing one to them. Conflating a cooperative
manufacturing program with kitchen chemistry misrepresents the project and is the most likely
way a document like this gets read as an instruction manual.

Contemporaneous expert commentary is on record and worth quoting: Stanford's Hank Greely warned
that dosing errors and contaminants could be fatal, and reporting at the time noted that
published plans without brewing facilities or purity verification remain "a long way from
usable product."

---

## 6. Where to go next

- If you are evaluating whether a decentralized program is feasible →
  [what a real program needs](what-a-real-program-needs.md)
- If you want the quantified safety case → [the purity gap](the-purity-gap.md)
- If you want the formulation chemistry → [formulation and stability](formulation-and-stability.md)
- If someone has told you they are making their own → [`../../SAFETY.md`](../../SAFETY.md)
