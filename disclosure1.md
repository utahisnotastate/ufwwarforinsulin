# Layer A — The Molecule (Disclosures 1–3)

[← README](README.md) · [Layer B →](disclosure2.md)

---

## Disclosure 1 — Three staples, and only one right answer out of fifteen

**Explain it to a friend.** Insulin is two short strings of beads held together by three tiny
clasps. There are six places a clasp could attach, which means fifteen possible ways to pin
them — and only one of those fifteen is insulin. The other fourteen are junk. Everything hard
about making insulin is making sure the clasps land in the right places.

**Old school.** Insulin is a protein; express the gene and you get the protein.

**This disclosure says.** You don't. You get a string. The folding is a separate problem from
the making, and it is the *actual* problem. Bacteria produce the string and dump it in an
insoluble heap. Getting from heap to correctly-pinned molecule is most of the industrial
process: harsh chemicals to unfold everything, then careful chemistry to coax it back.

**Status.** ✅ **VERIFIED.** Disulfides A6–A11, A7–B7, A20–B19. The source gets this exactly
right.

**But.** The source then prints an A-chain sequence that is **bovine**, not human — A8 Ala and
A10 Val instead of Thr and Ile — while quoting human insulin's molecular formula. Anyone
ordering a gene from it gets the wrong molecule. [Details](docs/technical/molecular-architecture.md).

**Kid takeaway.** It's not about making the beads. It's about getting the clasps in the right
holes.

---

## Disclosure 2 — Yeast folds it for you; bacteria don't

**Explain it to a friend.** Bacteria are a photocopier with no stapler. Yeast is a photocopier
that staples, collates, and slides the finished document under the door.

**Old school.** Insulin comes from *E. coli*, the way it has since 1982.

**This disclosure says.** Yeast is a eukaryote. It has an internal workshop — the endoplasmic
reticulum — with chaperones and protein disulfide isomerase whose entire job is getting
disulfides right. Give yeast a single-chain precursor with a short linker holding the two
chain segments near each other, add a secretion signal, and it folds the molecule correctly
*and secretes it into the broth.* No lysis. No 8 M guanidine. No refolding cascade.

**Status.** ✅ **VERIFIED** — and more verified than the source realizes.

**The twist.** The source presents this as suppressed future knowledge. It is current
industrial practice. **Roughly half the world's 40+ tonnes of insulin a year is already made
this way** by Novo Nordisk in *S. cerevisiae*, and *Pichia*-derived insulin is sold by Biocon
and Wockhardt. The source is describing the present tense and calling it the future.

**Kid takeaway.** We taught bread yeast to make a human hormone, and it does the fiddly part
for free.

---

## Disclosure 3 — We threw half the molecule away, and giving it back didn't work

**Explain it to a friend.** Your body builds insulin as one long piece and then snips out the
middle. For sixty years we assumed the snipped-out middle was packing peanuts. It isn't. But
when someone finally ran the trial to give it back, it didn't help.

**Old school.** C-peptide is an inert byproduct of proinsulin processing. Discard it.

**This disclosure says.** C-peptide is a signaling molecule. It binds cell membranes, activates
Na⁺/K⁺-ATPase, and stimulates nitric oxide production in blood vessel linings. Every person
with Type 1 diabetes has been receiving insulin stripped of the molecule that always
accompanied it in nature — and they get exactly the nerve, kidney, and eye damage you'd
predict.

**Status.** 🟡 **PARTLY TRUE** — then ❌ **NOT TRUE** at the finish.

The bioactivity is real. The proposed receptor (GPR146) **failed independent replication**. And
the trial that mattered — Cebix's 250-patient, 52-week Phase 2b in diabetic neuropathy —
**failed, with placebo outperforming drug on the primary endpoint.** The company dissolved
thirty days after unblinding. The senior author was the field's own leading advocate.

**Why we kept it anyway.** This is the single best illustration in the repository of the
pattern that runs through all of it: **a beautiful mechanism is not an outcome.**
[Full story](docs/endocrinology/c-peptide-the-full-story.md).

**Kid takeaway.** Scientists threw away a piece they thought was trash. It turned out to do
something — but putting it back didn't fix anything, and that's part of the story too.

---

[← README](README.md) · [Layer B — The Delivery →](disclosure2.md)
