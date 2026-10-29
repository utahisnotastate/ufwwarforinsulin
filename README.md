# UFW: War For Insulin

**Claims about insulin, checked one at a time against the published literature.**
This repository extracted **61**. Of those, 14 held up, 17 were contradicted by trials that
already ran, and 9 would kill an insulin-dependent reader who acted on them.

> **Read 61 as "how this repository cut it up," not as a property of the document.** Two
> independent extractors, blind to this inventory and to everything downstream, cut the same
> document into **258** and **237** claims — agreeing with each other to within 8.5% while both
> landing near four times our count. Our segmentation was systematically coarse. Every count
> and percentage below inherits that, and
> [the measurement is published](paper/data-reextraction.md) along with
> [both](paper/data-extraction-1.md) [extractions](paper/data-extraction-2.md) in full.
>
> What survived the re-extraction is the *pattern*, not the arithmetic: claims about what a
> treatment does to a person were wrong at every granularity tried.

---

> ## ⚠️ If you take insulin, read this paragraph before anything else
>
> **Nothing in this repository replaces insulin.** There is no device, diet, frequency,
> supplement, or protocol here that substitutes for the hormone. A person with Type 1
> diabetes who stops taking insulin develops **diabetic ketoacidosis within 12 to 48 hours**.
>
> The source material audited here tells readers they can replace insulin with a
> radio-frequency device. **That claim is false and it is the reason this repository exists.**
>
> **→ [SAFETY.md](SAFETY.md)** · DKA and hypoglycemia warning signs, and what to do.

---

## What this is

A long, confident, technical-looking medical document about insulin — a "future disclosure"
claiming to retrieve knowledge from the future. It cites real researchers. It uses real
residue numbers. It is roughly a quarter correct, which makes it far more persuasive than
ordinary quackery.

**Two things about where it came from, stated up front.** It was generated here, in a private
session with Google Gemini under a persona prompt written for the purpose — it is not a found
object. And **it was never shown to a patient or published anywhere.** An earlier version of
this page said it "circulates in patient communities." That was a claim about the genre
applied carelessly to this document, it was not true of this document, and it is
[logged as a correction](CORRECTIONS.md).

Documents of this kind can be produced by anyone with an account, in an afternoon, for
nothing. That is the reason to check one carefully. How widely they actually circulate is a
real question and this repository does not answer it.

So every claim in it was checked. Not summarised — **checked**, against PubMed, *Nature*,
NEJM, *The Lancet*, ClinicalTrials.gov, UniProt, USP, and SEC filings.

What came back is more interesting than the original. Several claims are **true, important,
and barely known** — the kind where you think *how is this not common knowledge?* Several are
real findings stretched past breaking. And a few are the specific kind of false that puts
people in intensive care.

| | Count |
|---|---|
| ✅ **VERIFIED** — holds up as stated | **14** |
| 🟡 **PARTLY TRUE** — real science, overstated or out of date | **14** |
| 🔵 **OPEN** — plausible, under investigation | **1** |
| ❌ **NOT TRUE** — contradicted by the evidence | **16** |
| ⛔ **NO BASIS** — no mechanism, not testable as framed | **16** |
| ☠️ **Harm flag** — acting on this could injure or kill | **9** |

**Full scoring with PMIDs → [INTEGRITY_AUDIT.md](INTEGRITY_AUDIT.md)**

---

## Find what matters to you

| You are… | Start here | Why |
|---|---|---|
| 🩸 **Living with Type 1** | [SAFETY.md](SAFETY.md) → [Disclosure 15](disclosure5.md) → [Disclosure 11](disclosure4.md) | What's dangerous in the source, what's genuinely working now, and what's actually curing people in trials |
| 🩺 **Living with Type 2** | [Disclosure 7](disclosure3.md) → [Disclosure 9](disclosure3.md) → [the hyperinsulinemia debate](docs/endocrinology/the-hyperinsulinemia-debate.md) | Why your cells stopped responding, and the real argument about insulin therapy — including where it stops being true |
| 👪 **Parent or carer** | [Kids' pages](docs/kids/README.md) → [Helping a friend](docs/kids/helping-a-friend.md) | Explains the whole system in 25 minutes, plus emergency signs in language a child can hold onto |
| 🧒 **A kid** | [Insulin, for kids](docs/kids/README.md) | One idea that explains everything else, and how we found out |
| 👩‍⚕️ **A doctor, nurse, or pharmacist** | [When a patient brings you this](docs/clinical/when-a-patient-brings-you-this.md) | 10-minute briefing: triage, what they're right about, what's lethal, how to keep the patient |
| 🔬 **An endocrinologist** | [Endocrinology set](docs/endocrinology/README.md) | Every therapeutic claim mapped to the trial that tested it. All of them failed |
| ⚗️ **A scientist or engineer** | [Technical set](docs/technical/README.md) | Molecular architecture, signaling, and a quantitative teardown of the physics |
| 🏭 **Trying to make insulin** | [The purity gap](docs/manufacturing/the-purity-gap.md) → [What a real program needs](docs/manufacturing/what-a-real-program-needs.md) | Why a filtered supernatant isn't medicine, quantified — then the honest build plan |
| 🧲 **Here about the frequency device** | [Why the physics layer fails](docs/technical/why-the-physics-layer-fails.md) | Worked arithmetic. It fails its own equation by a factor of hundreds |
| 📰 **A journalist** | [INTEGRITY_AUDIT.md](INTEGRITY_AUDIT.md) → [the nine lethal claims](INTEGRITY_AUDIT.md#the-nine-sentences-that-could-kill-someone) | Everything scored, sourced, and ranked by danger |
| 🤔 **Just curious** | [Seven things that are true and surprising](docs/all-ages/README.md) | 20 minutes, no background needed, and it ends by teaching you to check claims yourself |

---

# Part I — The fifteen disclosures

Each is a claim from the source, stated plainly, then checked. Template: *Explain it to a
friend · Old school · This disclosure says · Status · Kid takeaway.*

## Layer A — The Molecule → [disclosure1.md](disclosure1.md)

### 1. Three staples, and only one right answer out of fifteen · ✅

Insulin is two short chains pinned together by three disulfide bonds. Six cysteines can pair
up **fifteen** different ways and **exactly one of them is insulin**. The other fourteen have
the same atoms, the same mass, and the same band on a gel — and no activity at all.

That single number explains why insulin manufacturing is hard, why yeast is valuable, and why
"it looks pure" proves nothing.

### 2. Yeast folds it for you; bacteria don't · ✅

*E. coli* makes the protein and dumps it in insoluble heaps that need 8 M guanidine and a
refolding cascade to recover. Yeast folds it correctly in its own endoplasmic reticulum and
**secretes it into the broth** — no lysis, no chaotropes, no refolding.

The source presents this as suppressed future knowledge. **It's current industrial practice.**
Roughly half the world's 40+ tonnes a year already comes from yeast at Novo Nordisk, and
*Pichia*-derived insulin has been on the market for years.

### 3. We threw half the molecule away — and giving it back didn't work · 🟡 → ❌

Your body builds insulin as a longer chain and snips out the middle. That discarded piece —
**C-peptide** — was classified as inert packing material for sixty years. It isn't. It's
bioactive, it activates an enzyme that regulates nerve function, and it stimulates nitric
oxide in blood vessels. Every person with Type 1 has been receiving insulin stripped of it.

**Then somebody ran the trial.** Cebix, Phase 2b, 250 patients, 52 weeks, diabetic
neuropathy. **Placebo beat the drug on the primary endpoint.** The company dissolved thirty
days after unblinding. The proposed receptor, GPR146, later failed independent replication.

The mechanism is real. The clinical story is not the one the source tells.
→ [Full story](docs/endocrinology/c-peptide-the-full-story.md)

## Layer B — The Delivery → [disclosure2.md](disclosure2.md)

### 4. The liver is supposed to get it first · ✅ physiology / ❌ solved

Your pancreas doesn't release insulin into general circulation. It releases into the **portal
vein**, straight to the liver, which extracts 50–80% on first pass. A syringe in your belly
abolishes that gradient entirely — so to get enough to the liver, everything else gets far
more insulin than nature ever delivered there.

Real limitation, genuinely under-taught. **And people built the fix.** Lilly's
hepato-preferential insulin beat glargine on HbA1c with less nocturnal hypoglycemia and weight
*loss* — then was discontinued in December 2015 for raising liver fat and enzymes. A rival
helped patients with poor control and **harmed** those with good control. Zero are approved.

### 5. The molecule can be its own glucose sensor — in rats · ✅ chemistry / ❌ humans

"Smart insulin" switches itself on when glucose rises and off when it falls. The chemistry is
real and the conjugation site is right.

**No glucose-responsive insulin has ever worked in a human — and the chemistry the source
describes has never even been tried in one.** Merck spent over half a billion dollars on
MK-2640, which used *different* sensing chemistry (a mannose-receptor mechanism, not
boronate); in people with Type 1 it showed **no glucose-dependent change in clearance at all**
and was 25× less potent than regular insulin. **Every boronate construct remains
preclinical.** Novo's NNC2215 (*Nature*, 2024) is a genuine advance and across the glucose
range that actually occurs in a body it's about a **3× modulator, not a switch** — rats and
pigs only. Lilly paid up to ~$1bn for Protomer in 2021 to enter the field; still no human
efficacy data.

And the "one shot lasts weeks" idea runs backwards: the longest-acting insulins we have are
*weekly*, and in Type 1 they **increase** severe hypoglycemia — **10% vs 3%**.

### 6. Oral insulin keeps failing, and the reason is money · ✅ / ❌

Growing proinsulin in plant chloroplasts is real — up to **47% of total leaf protein**. But
the famous mouse result was **immune tolerance preventing diabetes onset**, not glycemic
control by absorbed insulin. It never entered human efficacy trials.

The instructive failure is Novo's: oral insulin 338 **matched injected glargine on HbA1c in
Phase 2** — and was killed because 1–2% oral bioavailability made the drug too expensive to
manufacture. **The science worked and the economics killed it**, which is the exact inverse of
the source's thesis. Oramed's Phase 3 (n=710) then missed its endpoint. No oral insulin is
approved anywhere.

## Layer C — The Resistance → [disclosure3.md](disclosure3.md)

### 7. The cell isn't broken. It's full. · ✅ mechanism / 🟡 framing

> A freight car is packed to the roof. The doors bulge. The yardmaster arrives with ten more
> crates, turns the key, and nothing moves. So he decides the key is broken and sends for a
> hammer.

The key works. **The car is full.** When fat accumulates inside muscle and liver cells where
it doesn't belong, specific lipids switch on an enzyme that **deliberately disables the
insulin relay**. The cell is refusing delivery — because letting more fuel in while already
saturated would damage its own mitochondria.

This is mainstream biochemistry, demonstrated in humans, and it genuinely reframes Type 2
diabetes. *(The freight-car metaphor is the best thing in the source document.)*

### 8. Muscle has a second door · ✅ ☠️

There are **two** ways to get glucose into a muscle cell. One needs insulin. The other just
needs the muscle to *work* — and it runs through completely different machinery: no insulin
receptor, no IRS-1, no PI3K, no Akt. It keeps working when the insulin pathway is jammed.

Real, and badly under-taught. **☠️ And here is the lethal subtlety:** it is
insulin-*signaling*-independent, **not insulin-independent**. Without basal insulin on board,
exercise drives glucose **up** and floods you with ketones. A person with Type 1 who exercises
*instead of* dosing gets ketoacidosis, not euglycemia.

### 9. The brake is real, and you still can't leave the glucose high · 🟡 → ❌ ☠️

The source concludes insulin therapy in Type 2 diabetes is "an iatrogenic disaster." The
randomized evidence says otherwise:

| Trial | Result |
|---|---|
| **ORIGIN** — 12,537 patients, 6.2 years | **Neutral.** HR 1.04 |
| **UKPDS 10-year follow-up** | **Benefit** — all-cause death ↓13%, MI ↓15% |
| **ACCORD** | Harm from an aggressive *target*, and in patients who **failed** to reach it |

One claim is flatly backwards: the source says exogenous insulin kills beta cells. Short-term
intensive insulin in newly diagnosed Type 2 produces **45–51% one-year remission** versus ~27%
on oral agents. Beta-cell *rest* preserves function.

## Layer D — The Replacement → [disclosure4.md](disclosure4.md)

### 10. Alpha cells can become beta cells — and the immune system still finds them · ✅ / ❌ ☠️

The pancreas has a second cell type sitting right next to the insulin-makers, close enough in
lineage that you can talk one into becoming the other. Real — demonstrated in mice, and in
**human** donor cells that reversed diabetes in mice for six months.

**The cure claim is contradicted by Figure 5 of its own source paper.** Tested against
cytotoxic T cells from patients with recent-onset Type 1:

> *"Insulin-producing α-cells were sensitive to PPI-directed CTLs, similar to β-cells."*

Which makes sense, and is the whole problem: the converted cell's job is to make
preproinsulin, and **preproinsulin is the main thing the immune system is attacking.** In
autoimmune mice the new cells worked about four months, then diabetes returned.

### 11. Stem-cell islets are curing people right now · ✅

Not a theory. *New England Journal of Medicine*, 2025:

- **10 of 12 participants insulin-independent at one year**
- **All 12** free of severe hypoglycemic events, HbA1c under 7%, time-in-range over 70%

Grown from a stem cell line, so donor supply is no longer the constraint. **This is the most
important thing in the repository.**

**The catch is the whole catch:** it requires immunosuppression, **two participants died**
— one of cryptococcal meningitis attributed to the regimen, one of progression of preexisting
neurocognitive impairment that was not attributed to the therapy — and it is still
investigational. The companion
programme that tried to avoid immunosuppression by encapsulating the cells **failed**. The
field has solved *making* the cells and has **not** solved protecting them.

### 12. You can delay Type 1 before it starts · ✅

Type 1 doesn't begin the day you get sick — the immune attack runs silently for months or
years first, and it's detectable. **Teplizumab** pushes clinical onset back by about two
years: **48.4 months vs 24.4 on placebo.**

FDA approved 2022, expanded down to **age 1 in April 2026**, and in June 2026 approved for
preserving insulin production in newly diagnosed children. It delays; it doesn't cure. It is
also the counterexample to the source's whole frame — arrived at by exactly the slow,
unglamorous trial machinery the document dismisses.

## Layer E — The Economics and the Machine → [disclosure5.md](disclosure5.md)

### 13. It costs about three dollars, and the gap was never manufacturing · ✅ / ❌ on the number

| Published production cost, regular human insulin | **$2.28–3.37** per vial |
|---|---|
| Active ingredient alone | **$0.86** |
| US list price, at peak | **$250–300** |

That gap was patents on devices and formulations, a rebate system rewarding high list prices,
and no price negotiation. **People rationed. People died rationing.**

Some of it got fixed: list prices cut **70–78%** in 2023–24, out-of-pocket capped at **$35/month**
for many. It took sustained public pressure, and it worked.

**But the source claims under a cent per vial** — that's 86× below the raw drug substance by
itself. The true number is damning enough without inflating it, and inflating it loses exactly
the readers who can check.

*And the discoverers agreed with you: Banting, Best, and Collip sold the patent for **one
dollar each**.*

### 14. Open-source insulin is a QC problem, not a biology problem · 🟡 ☠️

You could get yeast to secrete insulin precursor in a well-equipped community lab. **You could
not safely inject it**, and the reason isn't bureaucracy:

| Requirement | Filtered supernatant | Gap |
|---|---|---|
| Mature two-chain insulin | **single-chain precursor — largely inactive** | wrong molecule |
| Endotoxin ≤80 EU/mL | 10⁴–10⁸ EU/mL | **10²–10⁶×** |
| Host protein ≤100 ppm | 10⁵–10⁶ ppm | **10³–10⁴×** |
| Known potency | unknowable without HPLC | — |

**☠️ The detail that reframes everything:** what yeast secretes is a *precursor* whose short
linker physically blocks receptor binding. It isn't weak insulin — it's **mostly inactive
protein**. So the intuitive fear, overdose, is backwards. The likely failure mode is
**under-dosing into ketoacidosis**, in hours.

The goal is still worth pursuing. → [An honest build plan](docs/manufacturing/what-a-real-program-needs.md)

### 15. The boring loop beat every elegant molecule · ❌ ☠️

The source dismisses insulin pumps and continuous monitors as a clumsy stopgap. **Exactly
backwards.**

| Evidence | Result |
|---|---|
| Meta-analysis, 22 studies, 2,376 participants | **+10.9 points time in range**, HbA1c −0.37% |
| Registry, 250 centres, **n = 13,922** | **Hypoglycemic coma IRR 0.68 — significantly LOWER** |
| NHS England paediatric rollout | Time in range 49% → 63% in six months |

**The one real caveat the source could have raised and didn't:** that same registry found
**DKA higher** with closed loop (IRR 1.81), concentrated in users with HbA1c ≥8.5%. That
argues for ketone monitoring and training — not for walking away.

Every elegant molecule in this repository failed in humans. The unglamorous engineering
worked.

> **Don't let a beautiful future talk you out of an unglamorous present that works.**

---

# Part II — What was false

**The entire physics layer, and it is load-bearing.** The source claims insulin has a
characteristic resonance at **11.428 kHz** that can be broadcast through the skin to activate
insulin receptors with no insulin present. Worked quantitatively in
[why the physics layer fails](docs/technical/why-the-physics-layer-fails.md):

- 11.428 kHz is **267× below the lowest rotational transition** a 5.8 kDa molecule can have
- The source's own formula gives a different answer than the source's own number
- Thermal energy exceeds the quantum by **5.65 × 10⁸**
- The molecule's angular momentum randomizes **~10⁹ times per carrier cycle**
- Skin depth at that frequency is **3.84 m** — VLF passes through a body unattenuated, so the
  elaborate transdermal mechanism solves a problem that doesn't exist
- Piezoelectricity is **linear**, so it cannot rectify. A category error, not an overstatement

**The amino acid sequence is bovine.** A8-Ala and A10-Val — two of the three substitutions
defining bovine insulin — paired with a human B-chain, printed under human insulin's molecular
formula. A chimera that exists in no species. Anyone building a synthetic gene from that table
expresses the wrong protein.

**Every clinical endpoint cited as a success actually failed.** C-peptide (placebo won).
Glucose-responsive insulin (no effect in humans). Liver-targeted insulin (discontinued for
hepatic steatosis). Oral insulin (missed primary endpoint). Immune evasion (contradicted by
its own source paper).

**The pattern:** the source is strong on *mechanism* and wrong at every point where a mechanism
met a trial. That gap is the real subject of this repository.

**Already audited twice.** The same physics framework was scored claim-by-claim in
[FallOfPhysics](https://github.com/utahisnotastate/FallOfPhysics) and
[RiseOfGeometry](https://github.com/utahisnotastate/RiseOfGeometry), reaching the same verdicts
independently, with **runnable null-test protocols**. Provenance traces to a specific
mid-century corpus: Bearden, Dubrov, Inomata, Eerkens, Puharich.

# Part III — What was right

Listed because dismissing the whole document is both inaccurate and, if you ever have to talk
someone out of the dangerous parts, counterproductive.

1. **The over-stuffed freight car** — the best explanation of lipid-overload insulin resistance
   at any level
2. **Yeast secretion beats *E. coli* inclusion bodies** — correct, and under-appreciated
   outside the industry
3. **C-peptide was wrongly dismissed as inert** — genuinely bioactive
4. **The liver should see insulin first** — a real limitation of subcutaneous therapy
5. **The price was indefensible** — true, consequential, and the legitimate grievance driving
   the whole document

---

## Status key

| | Meaning |
|---|---|
| ✅ **VERIFIED** | Supported by peer-reviewed evidence, as stated |
| 🟡 **PARTLY TRUE** | Real science; overstated, misattributed, or out of date |
| 🔵 **OPEN** | Plausible, under genuine investigation, not established |
| ❌ **NOT TRUE** | Contradicted by evidence, or asserts what no study supports |
| ⛔ **NO BASIS** | No mechanism, no evidence; not testable as framed |
| ☠️ | Harm flag — acting on this claim could injure or kill |

## Repository map

```
README.md                  ← you are here
SAFETY.md                  ← read first if insulin is part of your life
INTEGRITY_AUDIT.md         ← all 61 claims, scored, with PMIDs
CORRECTIONS.md             ← errors found in this repo, logged publicly
disclosure1–5.md           ← the 15 disclosures, by layer

paper/                     ← the publishable finding, with raw data and analysis scripts

docs/
  kids/                    ← ages 7–12, four pages, structure-first
  all-ages/                ← general adult reader
  technical/               ← molecular architecture, signaling, physics teardown
  endocrinology/           ← hyperinsulinemia, C-peptide, the regenerative frontier
  clinical/                ← briefing + quick-reference card for non-specialists
  manufacturing/           ← the purity gap, a real build plan, formulation

archive/                   ← the source's claims, inventoried and numbered
references/                ← bibliography, verified vs. unverified flagged
```

## On method

Three independent literature reviews were run and cross-checked. Citations verified against
NCBI are marked ✅ in the [bibliography](references/bibliography.md); those from secondary
sources are marked ⚠️. **Seven unresolved items are listed openly** at the end of that file
rather than papered over.

Physics calculations are reproducible from the constants given, and the arithmetic is shown.

Where the source is right, it says so. Where the evidence is genuinely contested — and on
insulin resistance as adaptation, it is — it says that too, with the papers on both sides.

## Corrections welcome

Labels move with evidence, in either direction. If you have a peer-reviewed source that
changes a verdict, open an issue or a pull request — including, and especially, one that moves
a claim from ❌ back to ✅.

**Every correction is logged publicly in [CORRECTIONS.md](CORRECTIONS.md)** with what was
wrong, how it was caught, and what changed — annotated in place rather than silently
overwritten. There is one entry already: this repository misattributed MK-2640's sensing
chemistry, and was corrected by a model it was running an experiment on.

Two things to know before filing:

- **Every number here carries a source, or it comes out.**
- **The ☠️ harm flags are not stylistic.** Softening a safety statement needs evidence, not
  argument.

## License

[MIT](LICENSE) — use it, teach with it, translate it, remix it.

If you reuse the content, please carry [SAFETY.md](SAFETY.md) and the status labels with it.
The verdicts are what make the rest safe to read, and text separated from them can mislead in
precisely the way this repository exists to prevent.

**This is educational material, not medical advice.** It establishes no clinician–patient
relationship. If you have diabetes, your endocrinologist knows your case and this repository
does not.

## Related projects

Four repositories applying one method — inventory every claim, score it against the evidence,
keep what survives — to the same oracle's output across different domains.

| Repository | Domain | Method |
|---|---|---|
| [FallOfPhysics](https://github.com/utahisnotastate/FallOfPhysics) | Wave physics, signal processing, bio-instrumentation | ESTABLISHED / TESTABLE / SPECULATIVE / NOT SUPPORTED + 11 experiment protocols |
| [RiseOfGeometry](https://github.com/utahisnotastate/RiseOfGeometry) | Geometry and physics | ✅ / 🟡 / 🧪 / 📜 / ❌ across 31 disclosures, ~105 claims |
| [ufwwaragainstthemitochondria](https://github.com/utahisnotastate/ufwwaragainstthemitochondria) | Cell biology and metabolism | 15 disclosures + integrity audit + academic formalisms |
| [ufwwaragainstmemorization](https://github.com/utahisnotastate/ufwwaragainstmemorization) | Chemistry pedagogy | Teach the organizing structure, not the list |

The fourth contributed the teaching method rather than content: **give the reader the
structure that generates the facts, instead of the facts.** The [kids'
set](docs/kids/README.md) is built that way — one organizing problem (fuel arrives in lumps,
you burn it smoothly, so you must store it) from which insulin, glucagon, ketoacidosis, and
both diseases can be *derived* rather than memorized.
