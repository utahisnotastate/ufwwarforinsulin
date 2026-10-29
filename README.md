# UFW: War For Insulin

> **⚠️ Read [SAFETY.md](SAFETY.md) first if you or anyone close to you takes insulin.**
> Nothing in this repository replaces insulin. There is no device, diet, frequency, or protocol
> here that substitutes for the hormone, and a person with Type 1 diabetes who stops taking it
> is in ketoacidosis within 12–48 hours.

---

This project began with a long "future disclosure" on insulin — a channeled transmission
claiming to retrieve medical knowledge from the future. Seven cycles, dozens of claims,
covering pathophysiology, decentralized manufacturing, next-generation molecules, a permanent
cure, and an entire layer of physics.

Rather than publish it, or throw it out, **we checked every claim in it.**

Sixty-one substantive claims, scored against PubMed, *Nature*, NEJM, *Lancet*,
ClinicalTrials.gov, UniProt, USP, and SEC filings. The result is in
**[INTEGRITY_AUDIT.md](INTEGRITY_AUDIT.md)**, and it is the spine of this repository.

What came out is more interesting than what went in. About a quarter of the claims hold up,
and several of those are the kind that make you wonder how they aren't common knowledge.
About a fifth are real science overstated. The rest are wrong — and nine of them are wrong in
ways that can kill an insulin-dependent reader.

So this is a disclosure document with its receipts attached.

---

## Quick scoreboard

| | Count |
|---|---|
| ✅ **VERIFIED** — holds up as stated | **14** |
| 🟡 **PARTLY TRUE** — real science, overstated or out of date | **12** |
| 🔵 **OPEN** — plausible, under investigation | **1** |
| ❌ **NOT TRUE** — contradicted by evidence | **16** |
| ⛔ **NO BASIS** — no mechanism, not testable as framed | **18** |
| ☠️ **Harm flag** — acting on this could injure or kill | **9** |

Full scoring, with PMIDs: **[INTEGRITY_AUDIT.md](INTEGRITY_AUDIT.md)**
The original claims, inventoried and numbered: **[archive/](archive/source-claim-inventory.md)**

---

## Start here — pick your level

| If you are… | Go to | Time |
|---|---|---|
| **A kid (7–12)**, or reading with one | [docs/kids/](docs/kids/README.md) | 15 min |
| **Curious, no science background** | [docs/all-ages/](docs/all-ages/README.md) | 20 min |
| **A scientist or engineer** | [docs/technical/](docs/technical/README.md) | 45 min |
| **An endocrinologist** | [docs/endocrinology/](docs/endocrinology/README.md) | 40 min |
| **A doctor whose patient brought this in** | [docs/clinical/](docs/clinical/when-a-patient-brings-you-this.md) | 10 min |
| **Someone who wants to make insulin** | [docs/manufacturing/](docs/manufacturing/README.md) | 60 min |

The kids' set includes [a page on helping a friend with diabetes](docs/kids/helping-a-friend.md)
that is worth ten minutes of any child's time, whether or not they care about the rest.

---

## Part I — The fifteen disclosures

Each follows the same template: *Explain it to a friend* · *Old school* · *This disclosure
says* · *Status* · *Kid takeaway*.

### Layer A — The Molecule · [disclosure1.md](disclosure1.md)

| # | Disclosure | Status |
|---|---|---|
| 1 | Three staples, and only one right answer out of fifteen | ✅ |
| 2 | Yeast folds it for you; bacteria don't | ✅ |
| 3 | We threw half the molecule away — and giving it back didn't work | 🟡 → ❌ |

### Layer B — The Delivery · [disclosure2.md](disclosure2.md)

| # | Disclosure | Status |
|---|---|---|
| 4 | The liver is supposed to get it first | ✅ physiology / ❌ solved |
| 5 | The molecule can be its own glucose sensor (in rats) | ✅ chemistry / ❌ humans |
| 6 | Oral insulin keeps failing, and the reason is money | ✅ / ❌ |

### Layer C — The Resistance · [disclosure3.md](disclosure3.md)

| # | Disclosure | Status |
|---|---|---|
| 7 | The cell isn't broken. It's full. | ✅ mechanism / 🟡 framing |
| 8 | Muscle has a second door | ✅ ☠️ |
| 9 | The brake is real, and you still can't leave the glucose high | 🟡 → ❌ ☠️ |

### Layer D — The Replacement · [disclosure4.md](disclosure4.md)

| # | Disclosure | Status |
|---|---|---|
| 10 | Alpha cells can become beta cells — and the immune system still finds them | ✅ / ❌ ☠️ |
| 11 | Stem-cell islets are curing people now, at the price of immunosuppression | ✅ |
| 12 | You can delay Type 1 before it starts | ✅ |

### Layer E — The Economics and the Machine · [disclosure5.md](disclosure5.md)

| # | Disclosure | Status |
|---|---|---|
| 13 | It costs about three dollars, and the gap was never manufacturing | ✅ / ❌ on the number |
| 14 | Open-source insulin is a QC problem, not a biology problem | 🟡 ☠️ |
| 15 | The boring loop beat every elegant molecule | ❌ ☠️ |

---

## Part II — What the source got wrong, in one screen

**The physics layer is entirely false, and it is load-bearing.** The source claims insulin has
a characteristic resonance at 11.428 kHz which can be broadcast through the skin to activate
insulin receptors with no insulin present. Worked quantitatively in
[why the physics layer fails](docs/technical/why-the-physics-layer-fails.md):

- 11.428 kHz is **267× below the lowest rotational transition** a 5.8 kDa molecule can have
- The quantum is **5.65 × 10⁸ times smaller than kT** at body temperature
- The molecule's angular momentum randomizes **~10⁹ times per carrier cycle**
- Skin depth at that frequency is **3.84 m** — VLF passes through a body unattenuated, so the
  keratin transduction mechanism solves a problem that doesn't exist
- Piezoelectricity is **linear**, so it cannot rectify. That's a category error, not an
  overstatement

**The A-chain sequence is bovine.** A8-Ala and A10-Val, paired with a human B-chain — a
chimera occurring in no species, printed under human insulin's molecular formula. Anyone
ordering a gene from it gets the wrong molecule.
[Details](docs/technical/molecular-architecture.md).

**Every clinical endpoint it cites as a success actually failed.** C-peptide (Cebix Phase 2b —
placebo won). Glucose-responsive insulin (MK-2640 — no glucose-dependent clearance in humans).
Hepato-preferential insulin (peglispro — discontinued for hepatic steatosis). Oral insulin
(Oramed Phase 3 — missed primary endpoint). Transdifferentiation immune evasion (contradicted
by the figure in its own source paper).

**The pattern:** the source is strong on *mechanism* and wrong at the point where mechanism met
a trial. That gap is the real subject of this repository.

---

## Part III — What it got right

Listed because dismissing the whole document is both inaccurate and, if you ever have to talk
someone out of the dangerous parts, counterproductive.

1. **The over-stuffed freight car** — the best explanation of lipid-overload insulin
   resistance in any register, at any level. Reused with credit in the kids' and all-ages docs.
2. **Yeast secretion beats *E. coli* inclusion bodies** — correct and under-appreciated
   outside the industry, though already standard inside it.
3. **C-peptide was wrongly dismissed as inert** — it is genuinely bioactive. The source just
   doesn't know how the story ends.
4. **The liver should see insulin first** — a real, under-taught limitation of subcutaneous
   therapy.
5. **The price of insulin was indefensible** — true, consequential, people died rationing, and
   it is the legitimate grievance driving the entire document.

---

## Status key

| | Meaning |
|---|---|
| ✅ **VERIFIED** | Supported by peer-reviewed evidence, as stated |
| 🟡 **PARTLY TRUE** | Real science; the claim overstates, misattributes, or is out of date |
| 🔵 **OPEN** | Plausible, under genuine investigation, not established |
| ❌ **NOT TRUE** | Contradicted by evidence, or asserts what no study supports |
| ⛔ **NO BASIS** | No mechanism, no evidence; not testable as framed |
| ☠️ | Harm flag — acting on this claim could injure or kill |

---

## Repository map

```
README.md                  ← you are here
SAFETY.md                  ← read first if insulin is part of your life
INTEGRITY_AUDIT.md         ← all 61 claims, scored, with PMIDs
disclosure1–5.md           ← the 15 disclosures, by layer

docs/
  kids/                    ← ages 7–12, three pages
  all-ages/                ← general adult reader
  technical/               ← molecular architecture, signaling, the physics teardown
  endocrinology/           ← hyperinsulinemia debate, C-peptide, the regenerative frontier
  clinical/                ← briefing + quick-reference card for non-specialists
  manufacturing/           ← the purity gap, a real build plan, formulation and stability

archive/                   ← the source's claims, inventoried and numbered
references/                ← bibliography, with verified vs. unverified citations flagged
```

---

## On method

Three independent literature reviews were run against the source's claims and cross-checked.
Where a citation's PMID was verified against NCBI it is marked ✅ in the
[bibliography](references/bibliography.md); where it came from a secondary source it is marked
⚠️. Eight unresolved items are listed openly at the end of that file rather than papered over.

Physics calculations are reproducible from the constants given, and the arithmetic is shown.

Where the source is right, it says so. Where the evidence is genuinely contested — and on
insulin resistance as adaptation, it is — it says that too, with the papers on both sides.

**This is educational material, not medical advice.** It establishes no clinician–patient
relationship. If you have diabetes, your endocrinologist knows your case and this repository
does not.

---

*Companion to [UFW: War Against the Mitochondria](https://github.com/utahisnotastate/ufwwaragainstthemitochondria).*
