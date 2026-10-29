# Layer E — The Economics and the Machine (Disclosures 13–15)

[← Layer D](disclosure4.md) · [README](README.md)

---

## Disclosure 13 — It costs about three dollars, and the gap was never manufacturing

**Explain it to a friend.** Yeast makes insulin out of sugar water. The molecule is cheap. For
twenty years Americans were charged hundreds of dollars for it, and some of them died
rationing.

**Old school.** Insulin is expensive because biologics are complicated to make.

**This disclosure says.** Not this one. Researchers costed it properly — purification, quality
control, fill-finish, a normal profit margin — and published it.

| | Cost per 1,000 IU vial |
|---|---|
| **Regular human insulin, full production cost** | **$2.28–3.37** |
| Glargine | $3.69–5.13 |
| Lispro / aspart | ~$4.50–6.16 |

*(Gotham, Barber & Hill, BMJ Global Health 2018)*

Meanwhile US list prices passed $250–300. That gap was patents on devices and formulations, a
rebate system that rewarded high list prices, and no price negotiation. **People rationed.
People died rationing.** Those deaths are documented and named.

**Status.** ✅ **VERIFIED** — and this is the legitimate grievance driving the whole source
document.

**But the source claims <$0.01 a vial, and that's wrong in a way that matters.** The raw drug
substance alone costs **$0.86** per vial at published export prices. The claim is 86× below
the API by itself and 228–337× below a credible all-in cost. The Open Insulin Foundation's own
planning figure is **$7.00**.

**And some of this got fixed.** Under sustained public pressure, all three manufacturers cut
list prices 70–78% in 2023–24. Out-of-pocket is capped at **$35/month** for Medicare
beneficiaries and voluntarily for many others. The honest remaining US gap is about **one order
of magnitude at the margin**, not three.

That's still a real grievance, and the global picture is far worse. But a document claiming a
1000× arbitrage loses exactly the readers who can check it. **The true number is damning
enough.**

**And the founders agreed with you.** Banting, Best, and Collip sold the insulin patent to the
University of Toronto **for one dollar each**, on the explicit grounds that it shouldn't be
owned.

**Kid takeaway.** The medicine is cheap to make. The price was a choice, which means people
could change it — and they partly did.

---

## Disclosure 14 — Open-source insulin is a quality-control problem, not a biology problem

**Explain it to a friend.** You could probably get yeast to make insulin in a well-equipped
community lab. You could not safely put it in your body, and the reason isn't bureaucracy.

**Old school.** Making a biologic requires a billion-dollar facility.

**This disclosure says.** The fermentation doesn't. A 5-litre instrumented bioreactor and a
properly built strain will secrete insulin precursor. The Open Insulin Foundation has been
working on exactly this since 2015.

**Status.** 🟡 **PARTLY TRUE** — the biology is accessible, and that is genuinely the
surprising part. ❌ for everything the source says comes after it.

Here is the gap, measured:

| What's needed | What a filtered supernatant gives | Gap |
|---|---|---|
| Mature two-chain insulin | **single-chain precursor — largely inactive** | wrong molecule |
| Endotoxin ≤80 EU/mL | 10⁴–10⁸ EU/mL | **10²–10⁶×** |
| Host protein ≤100 ppm | 10⁵–10⁶ ppm | **10³–10⁴×** |
| Known potency, 95–105% of label | unknowable without HPLC | — |

**The detail that reframes everything:** what yeast secretes is a *precursor* whose short
linker physically prevents the B-chain movement that receptor binding requires. It is not weak
insulin. It is **mostly inactive protein.** So the intuitive fear — overdose — is backwards.
The likely failure mode is **under-dosing**, and in Type 1 diabetes that means ketoacidosis in
hours.

A 0.22 µm filter removes cells. It removes no endotoxin, no host protein, no DNA. Endotoxin is
stable to 250 °C.

**None of which means the goal is wrong.** Local, community-governed insulin supply is worth
building — especially for low- and middle-income countries, where price and cold chain both
still bind. There is a build plan in
[what a real program needs](docs/manufacturing/what-a-real-program-needs.md). It starts with
buying an HPLC.

**Kid takeaway.** Making the medicine is the easy part. Proving it's safe is the whole job.

---

## Disclosure 15 — The boring loop beat every elegant molecule

**Explain it to a friend.** While everyone waited for smart insulin, a sensor, a pump, and some
code quietly became the biggest improvement in Type 1 diabetes care since 1921.

**Old school.** *(The source's version.)* Pumps and continuous monitors are a clumsy
"Generation 3" stopgap with moderate hypoglycemia risk from sensor lag, soon obsolete.

**This disclosure says.** Exactly backwards. **Automated insulin delivery** — a CGM, a pump,
and a control algorithm adjusting dose every few minutes, all night, with no decisions from the
person — is the best-evidenced therapy in Type 1 diabetes short of transplantation.

| Evidence | Result |
|---|---|
| Meta-analysis, 22 studies, 2,376 participants | **+10.9 points time in range**, HbA1c **−0.37%** |
| DPV registry, 250 centres, **n = 13,922** | **Hypoglycemic coma 0.62 vs 0.91 per 100 patient-years — IRR 0.68, significantly LOWER** |
| NHS England pediatric rollout | TIR 49% → 63% at six months |

**Status.** ❌ **NOT TRUE** — and this is the most clinically consequential error in the source
document. ☠️

On sensor lag: real, small, and explicitly modeled by the control algorithms. A Dexcom G7
characterization found a **2-minute** lag assumption minimized error; the "5–15 minutes"
figure comes from consumer material.

**The one genuine caveat the source could have raised and didn't:** that same registry found
**DKA higher** with closed loop — 1.74 vs 0.96 per 100 patient-years — concentrated in users
with HbA1c ≥8.5%. That argues for ketone monitoring and training. Not for walking away.

**Why this is the right disclosure to end on.** Every elegant molecule in this repository —
smart insulin, oral insulin, liver-targeted insulin, C-peptide — failed in humans. The
unglamorous engineering worked. The lesson isn't cynicism about research; stem-cell islets are
genuinely curing people. It's this:

> **Don't let a beautiful future talk you out of an unglamorous present that works.**

**Kid takeaway.** Sometimes the big breakthrough is a sensor, a pump, and some good code —
and it's already here.

---

[← Layer D](disclosure4.md) · [README](README.md) · [INTEGRITY_AUDIT](INTEGRITY_AUDIT.md)
