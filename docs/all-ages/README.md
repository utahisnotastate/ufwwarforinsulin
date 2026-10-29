# Insulin: seven things that are true and surprising

**Who this is for:** adults and older teenagers. No science background assumed. If you'd like
the simpler version first, the [kids' pages](../kids/README.md) are genuinely good and will take
you ten minutes.

**Before anything else:** if you or someone close to you takes insulin, read
[SAFETY.md](../../SAFETY.md). It is short and it matters.

---

## Why this document exists

This repository started with a long "future disclosure" document about insulin — a channeled
transmission claiming to retrieve medical knowledge from the future. It mixes three things
together: real science, speculative research, and physics that is simply false.

Rather than throw it out, we checked every claim in it. The scorecard is in
[INTEGRITY_AUDIT.md](../../INTEGRITY_AUDIT.md).

What came out of that is more interesting than the original. Because several of the claims
turned out to be **true, important, and widely under-appreciated** — the kind of thing where you
think *how is this not common knowledge?* And a few turned out to be the kind of false that gets
people killed.

Here are the seven that survived, in plain language.

---

## First, the structure everything hangs off

Before the seven, one idea. If you take this in, the rest stops being a list of facts to
remember and becomes something you can reason about — and you'll be able to catch bad claims
yourself.

**Your fuel arrives in lumps. You burn it smoothly.**

You eat three or four times a day. Your heart, brain, kidneys, and muscles consume energy
every second, awake and asleep. That mismatch between bursty supply and continuous demand has
exactly one solution, and it's the same one a city or a warehouse would use: **store the
surplus when it arrives, release it when you need it.**

Storage requires control. If every cell simply absorbed glucose whenever it floated past,
nothing would ever be put away and you'd be in trouble four hours after every meal. So cells
keep their glucose doors **shut by default** — and that locked door, which looks like a design
flaw, is the thing that makes storage possible.

A locked door needs a key, and someone deciding when to turn it.

That job belongs to about a million clusters of cells in your pancreas called the **islets of
Langerhans**. They continuously sample your blood. Glucose rising → they release **insulin**,
which unlocks cells so fuel can go into storage in liver, muscle, and fat. Glucose falling →
the same islets release **glucagon**, which tells the liver to unpack storage and push fuel
back out.

```
   glucose UP  ──►  insulin   ──►  unlock, take fuel in, store it
   glucose DOWN ─►  glucagon  ──►  unpack storage, release fuel
```

Two opposing hormones from one organ, holding blood glucose in a narrow band your entire
life. It's a thermostat.

Now notice what you can derive from this without being told:

- **Insulin is a signal, not a fuel.** It contains no energy. It carries an instruction.
- **Losing insulin is not "high blood sugar."** It's losing the ability to store or use fuel at
  all. The cells starve surrounded by food, the body panics and burns fat for emergency energy,
  and the acidic by-products — **ketones** — accumulate. That's **ketoacidosis**, and it's what
  actually kills people in Type 1 diabetes, within **12 to 48 hours**.
- **There must be two different ways to break this.** Either the key is gone, or the locks stop
  responding. Those would be completely different diseases with completely different
  treatments — which is exactly what Type 1 and Type 2 are.

Everything below is a consequence of that structure.

---

## 1. Insulin is a key, not a fuel

The single most common misunderstanding. Insulin doesn't give you energy and doesn't contain
energy. It's a signal.

When you eat, your blood fills with glucose — simple sugar, which is what all food eventually
becomes. Glucose in your blood is useless; it has to get *inside* your cells to be burned. Cells
keep their glucose doors shut by default.

Insulin is the signal that opens them. Your pancreas releases it when it detects glucose rising,
cells open up, glucose moves in, blood levels fall. It's a thermostat, running constantly, with
a response time measured in minutes.

**Type 1 diabetes** is the autoimmune destruction of the cells that make insulin. The signal is
gone. Glucose piles up in the blood while cells starve. It is not caused by diet or lifestyle,
it usually appears in childhood or young adulthood, and it is not survivable without injected
insulin.

**Type 2 diabetes** is a different disease that unfortunately shares a name. The signal is
usually present — often in excess — but cells stop responding to it. That's the next item, and
it's the one that will change how you think about this.

---

## 2. "Insulin resistance" may be a cell protecting itself, not a cell malfunctioning

Here is the framing most people carry: in Type 2 diabetes, the lock is broken. The cell *can't*
respond. Something has failed.

There's a strong case that this is backwards.

> Picture a freight car already packed to the roof with crates. The doors bulge. The yardmaster
> arrives with ten more crates, turns the key — and nothing moves. He concludes the key is
> broken and fetches a hydraulic ram.

The cell in Type 2 diabetes is not broken. It is **full**. Specifically, when fat accumulates
inside muscle and liver cells where it doesn't belong, certain lipid species build up in the
membrane, switch on an enzyme family called protein kinase C, and that enzyme deliberately
disables the insulin signaling chain — by tacking a chemical group onto a relay protein in a
spot that jams it.

The cell is refusing delivery. If it kept letting glucose in while already saturated with fuel,
its mitochondria would be overwhelmed and it would damage itself. Resistance is the brake, and
the brake is working.

This is real, mainstream biochemistry — most associated with Gerald Shulman's group at Yale —
and it genuinely reframes the disease. The high blood sugar is overflow, not the fire.

**The honest caveat,** because this is exactly where the source material goes off the rails: a
protective brake can still be destroying you. Chronic high blood sugar damages eyes, kidneys,
nerves, and arteries regardless of why it is high. "The cell is protecting itself" is a true
statement about mechanism. It is not permission to leave blood glucose high, and it is
absolutely not a reason to stop prescribed insulin. See [item 7](#7-the-boring-thing-is-the-thing-thats-working).

---

## 3. Your liver is supposed to get the insulin first, and a syringe in your belly breaks that

This one is strange once you see it, and almost nobody outside endocrinology thinks about it.

Your pancreas doesn't release insulin into your general bloodstream. It releases it into the
**portal vein**, which runs directly to the liver. The liver pulls out roughly half to
three-quarters of it on the first pass and uses it to switch off its own glucose production.

So in a healthy body there's a steep gradient: the liver is bathed in insulin, and the rest of
the body — muscles, arteries, kidneys — gets what's left, which is much less.

Inject insulin into the fat under your skin and that gradient is gone. The insulin enters the
general circulation and reaches everything at once. To get enough to the liver to do its job,
everything else has to be exposed to far more insulin than nature ever intended.

This isn't trivia. Chronically elevated insulin in peripheral tissue has its own effects on
blood vessels, sodium handling in the kidney, and growth signaling. It's a real cost of the
delivery route, and it's been understood for decades.

**And yet:** several companies built liver-targeted insulins specifically to fix this. Lilly's
insulin peglispro reached large Phase 3 trials. It did what it promised at the liver — and was
abandoned because it raised liver fat and liver enzymes. The physiological argument was right.
The drug still didn't make it. That gap between "mechanistically correct" and "works in people"
is the single most important lesson in this whole document.

---

## 4. For sixty years, we threw away half the molecule

When your body makes insulin it first builds a longer precursor, **proinsulin**, which then gets
snipped. The useful part is insulin. The piece cut out and discarded is called **C-peptide** —
"connecting peptide," because it connected the two halves during folding.

C-peptide was classified as inert packing material. Manufactured insulin contains none of it. So
for decades, every person with Type 1 diabetes has received insulin without the molecule that
always accompanied it in nature.

Then, starting in the 1990s, researchers found C-peptide isn't inert at all. It binds cell
surfaces, activates an enzyme that regulates nerve cell function, and stimulates nitric oxide
production in blood vessel linings. In animals and small human studies it improved nerve
conduction and kidney measures.

So: the thing we threw away was a signaling molecule, and the people missing it get exactly the
nerve, kidney, and eye complications you'd predict. That's a hell of a story, and it's the most
compelling claim in the source material.

**Here's the ending the source doesn't tell you.** A company called Cebix developed a
long-acting C-peptide and ran a properly controlled Phase 2b trial in diabetic neuropathy. In
2015 it reported that the drug was **no better than placebo**. Cebix shut down and laid off its
staff.

That doesn't mean C-peptide is biologically inert — the basic science stands. It means the
clinical story is unresolved at best, and the source's claim that restoring C-peptide
*"reverses"* microvascular damage is not supported by the trial that was actually run to test
it.

We left this in because it's the honest shape of a lot of medicine: a beautiful mechanism, a
compelling narrative, and a trial that says no. Both halves are the story.

---

## 5. Muscle can take up glucose with no insulin involved at all

Genuinely useful, genuinely under-taught.

There are two separate ways to get glucose into a muscle cell. One is the insulin pathway. The
other is **contraction** — when muscle actually works, it triggers glucose uptake through a
completely different internal route, driven by the energy stress of contracting and by calcium
release.

These are independent. The contraction route works in people whose insulin pathway is badly
impaired. It is, mechanically, a second door.

This is why exercise lowers blood glucose, and why it keeps working in people with significant
insulin resistance. It's also why people with Type 1 have to plan around activity — their muscles
will pull glucose out of the blood whether or not they have insulin on board, which is also how
exercise can cause hypoglycemia hours later.

**The caveat, and it's an important one:** this does not mean exercise substitutes for insulin
in Type 1 diabetes. It doesn't, and attempting it is dangerous — without insulin the liver
keeps dumping glucose and the body keeps making ketones, so you can head into ketoacidosis
while exercising. It's a genuine second pathway for glucose *disposal*, not a replacement for
the hormone.

---

## 6. The molecule costs a few dollars. The price was never about the molecule.

Insulin is made by yeast or bacteria carrying the human gene. They do the hard part. Feedstock
is essentially sugar water.

Researchers have actually costed this out properly — including purification, quality control,
fill-finish, and a normal profit margin. The published estimates land in the range of a few
dollars per vial for human insulin, somewhat more for modern analogues. Meanwhile US list prices
climbed above $250–300 a vial.

That gap was never a manufacturing problem. It was patents on delivery devices and formulations,
a rebate system that rewarded high list prices, and no effective price negotiation. People
rationed. People died rationing — the deaths are documented and named.

Some of this has actually been fixed. Under pressure, the three major manufacturers cut list
prices sharply in 2023–2024, and out-of-pocket costs are now capped at $35/month for Medicare
beneficiaries and, voluntarily, for many others. That is a genuine win, it came from sustained
public pressure, and it is worth knowing that it worked.

And the discoverers would have wanted it. Banting, Best, and Collip sold the insulin patent to
the University of Toronto for **one dollar each**, on the explicit grounds that it shouldn't be
owned.

**The dangerous inference to avoid:** "cheap to make" does not mean "safe to make at home." The
few dollars is the cost *including* the testing that makes it injectable. Strip that out and you
don't have cheap insulin, you have an unknown liquid. The [manufacturing
docs](../manufacturing/README.md) cover exactly why, in detail, for people who want the real
numbers.

---

## 7. The boring thing is the thing that's working

The source material dismisses insulin pumps and continuous glucose monitors as a clumsy interim
technology, soon to be replaced by something elegant.

That has it almost exactly backwards. The unglamorous engineering — a sensor under the skin, a
pump, and a control algorithm talking to each other — is the biggest practical improvement in
Type 1 diabetes care since the discovery of insulin itself. These **automated insulin delivery**
systems adjust dosing every few minutes, all night, without the person doing anything, and
they measurably increase time spent in healthy glucose range while reducing dangerous lows.

Meanwhile, the elegant molecular solutions have a hard history. Glucose-responsive "smart
insulin" that switches itself on and off is a beautiful idea with decades of work behind it and
promising recent animal data — and the one that reached human testing didn't deliver. Oral
insulin has failed repeatedly in late-stage trials. Liver-targeted insulin failed. These are all
good ideas. None of them is available to you.

The lesson isn't cynicism about research — stem-cell-derived islets are genuinely restoring
insulin production in human trials right now, and that may be the real cure. The lesson is
**don't let an elegant future talk you out of an unglamorous present that works.**

---

## What was false

The source material also contained an entire layer of physics: that insulin has a
characteristic radio frequency (11.428 kHz), that broadcasting it through the skin with a coil
and a microcontroller activates insulin receptors with no insulin present, and that this makes
the hormone unnecessary.

None of it is true. There is no mechanism, the numbers don't work — they don't even satisfy the
source's own equation — and the whole thing is worked through quantitatively in
[why the physics layer fails](../technical/why-the-physics-layer-fails.md).

It matters because it isn't decoration. It's the part that tells a person with Type 1 diabetes
they could put down the syringe. That is a lethal instruction, and it is the reason this
repository leads with a safety page instead of a table of contents.

---

## How to check a claim like this yourself

This is the part worth keeping after you've forgotten the rest, because the next document like
this one is already being written somewhere.

None of what follows requires a science degree. Every one of these tests was applied in the
[audit](../../INTEGRITY_AUDIT.md), and together they caught every false claim in the source.

**1. Did a trial actually happen, and what did it say?**

This single question did more work than everything else combined. The source material names
real mechanisms and real molecules — and for almost every one, somebody *ran the trial*, and
it failed. C-peptide: placebo beat the drug. Smart insulin: no effect in humans. Liver-targeted
insulin: worked, then caused liver damage. Oral insulin: missed its endpoint.

A mechanism is a reason to *run* a trial. It is not a result. "This should work because
biology" is where medicine starts, not where it ends — and the gap between the two is where
almost all medical overclaiming lives.

**2. Does the number come out of its own equation?**

The source gives insulin a "resonance frequency" of 11.428 kHz, and also gives the formula it
supposedly comes from. Put the numbers into the formula and you get something else entirely —
by a factor of hundreds. You don't need to know what the formula means to run that check. You
just need to do the arithmetic.

Four significant figures that don't reproduce from the stated equation were not measured.
They were chosen.

**3. Is the precision plausible?**

"11.428 kHz" claims accuracy of about one part in ten thousand. For a molecule tumbling in
warm water, the physics allows no such precision — the real spread is thousands of times wider
than the number itself. **Precision that exceeds what the method could possibly deliver is a
reliable tell**, and you can often spot it without knowing the subject.

**4. Who else reproduced it?**

Insulin was confirmed because labs around the world made it within a year and got the same
result. The physics claims here trace back to a handful of self-published authors from the
1970s and 80s, cited by each other, never independently replicated. One result from one source
is a hypothesis. Many results from independent sources is a finding.

**5. Does it fail where it should?**

Real effects break in predictable ways. Stop insulin, blood sugar rises — that's the theory
making a risky prediction and surviving. Claims that explain every outcome, and that no
observation could contradict, aren't strong. They're unfalsifiable, which is weaker.

**6. Does the conclusion match the evidence, or exceed it?**

The most dangerous claims here aren't fabrications. They're **real findings stretched past
breaking**. Insulin resistance really may be partly protective — that's in *Diabetes*, 2015.
"So stop taking insulin" does not follow, and the paper's authors don't say it. Watch for the
sentence where a careful finding turns into a confident instruction. That's usually the exact
point where it stopped being true.

> **A compressed version:** mechanism isn't outcome · check the arithmetic · suspicious
> precision · who replicated it · what would disprove it · where did the conclusion outrun
> the evidence.

---

## Where to go next

| You are | Go here |
|---|---|
| Curious, want more depth | [Technical docs](../technical/README.md) |
| A clinician seeing a patient about this | [Clinical briefing](../clinical/when-a-patient-brings-you-this.md) |
| An endocrinologist | [Endocrinology set](../endocrinology/README.md) |
| Interested in making insulin | [Manufacturing set](../manufacturing/README.md) |
| Wanting the claim-by-claim scorecard | [INTEGRITY_AUDIT.md](../../INTEGRITY_AUDIT.md) |
