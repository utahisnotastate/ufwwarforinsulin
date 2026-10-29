# SAFETY — read this before anything else in this repository

This repository contains a mix of **verified science**, **unproven-but-real research**, and
**claims that are false**. The whole point of the repo is to label which is which. But labels
only help if you read them, and some of the false claims in the source material are the kind
that kill people. So this page states the lethal ones up front, without hedging.

---

## The four statements that can kill you

### 1. If you have Type 1 diabetes, nothing in this repository replaces your insulin

Type 1 diabetes is the destruction of the cells that make insulin. There is no diet, no
exercise protocol, no electromagnetic device, no supplement, and no frequency that substitutes
for the hormone. Without exogenous insulin, a person with Type 1 diabetes develops **diabetic
ketoacidosis (DKA)** and dies. The typical timeline from total insulin cessation to
life-threatening DKA is **12 to 48 hours**, not weeks.

The source material behind this repo proposes a transdermal "VLF formon transducer" — an ESP32
driving a coil at 11.428 kHz — that supposedly triggers cellular glucose uptake without
insulin. **This device does not work. It cannot work. There is no mechanism.** The physics is
addressed in detail in [`INTEGRITY_AUDIT.md`](INTEGRITY_AUDIT.md) and
[`docs/technical/why-the-physics-layer-fails.md`](docs/technical/why-the-physics-layer-fails.md).
Building it is harmless. Using it instead of insulin is fatal.

### 2. Do not inject anything you made yourself

This repository contains a real, technically accurate description of how recombinant insulin is
produced, including the yeast-secretion route. It is written for people who work in labs, for
students, and for organizations like the Open Insulin Project who are trying to solve this
legitimately.

It is **not** a recipe for a drug you can put in your body. The gap between "there is insulin
in this liquid" and "this liquid is safe to inject" is the entire discipline of pharmaceutical
manufacturing, and it is not a formality. Specifically:

- **You cannot know the potency.** Insulin is dosed in units. A vial that is 30% stronger than
  you think will cause severe hypoglycemia; one that is 50% weaker will let you drift into DKA.
  Determining IU/mL requires a validated bioidentity and potency assay, not a protein
  concentration reading.
- **Endotoxin.** Culture supernatant carries bacterial endotoxin. Injected endotoxin causes
  fever, shock, and death at microgram quantities. A 0.22 µm filter removes cells. It does
  **not** remove endotoxin.
- **Sterility.** A 0.22 µm filter is a sterilizing filter only inside a validated aseptic
  process. On a bench, it is a step that reduces bioburden in a container that is not sterile.
- **Misfolded species.** Incorrectly folded insulin and aggregates are immunogenic. An immune
  response to injected insulin can make you resistant to *all* insulin, including the
  pharmaceutical kind that would otherwise save your life.

The full quantitative treatment is in
[`docs/manufacturing/the-purity-gap.md`](docs/manufacturing/the-purity-gap.md). Read it before
you decide the warning is boilerplate. It is not boilerplate; it is the reason this is hard.

### 3. If you take insulin, do not reduce or stop it based on this document

The source material argues that insulin resistance is a protective cellular response and that
giving insulin to people with Type 2 diabetes makes them worse. There is a **real and serious**
scientific debate inside that claim, and this repo covers it honestly — see
[`disclosure3.md`](disclosure3.md) and
[`docs/endocrinology/the-hyperinsulinemia-debate.md`](docs/endocrinology/the-hyperinsulinemia-debate.md).

But "there is a legitimate debate about long-term insulin strategy in Type 2 diabetes" and
"you should stop your insulin" are not the same sentence, and the distance between them is
measured in hospital admissions. Changes to an insulin regimen are made with a clinician, with
glucose monitoring, and gradually. Abrupt self-directed cessation is how people end up in
intensive care.

### 4. "It's natural" and "it's cheap" are not safety claims

Several ideas in the source material are attractive because they are decentralized, low-cost,
and anti-institutional. Those are real virtues and the access problem they are reacting to is
real — insulin rationing kills Americans every year, and that is documented in
[Disclosure 13](disclosure5.md). But the cost of insulin being indefensible does not make
unvalidated insulin safe. Both things are true at once.

---

## Know the emergency signs

**Diabetic ketoacidosis (DKA)** — too little insulin. Excessive thirst, frequent urination,
nausea and vomiting, abdominal pain, rapid deep breathing, breath that smells fruity or like
nail polish remover, confusion, drowsiness. **This is a medical emergency. Call emergency
services.**

**Severe hypoglycemia** — too much insulin. Shakiness, sweating, confusion, slurred speech,
loss of coordination, seizure, unconsciousness. If the person is conscious and can swallow,
give fast sugar (juice, glucose tabs). If they are unconscious or seizing, **do not put
anything in their mouth** — give glucagon if available and call emergency services.

**US:** 911. **UK:** 999. **EU:** 112. Your local emergency number otherwise.

---

## Who this repository is for

It is for readers who want to understand insulin — the molecule, the biology, the
manufacturing, the economics, and the research frontier — at whatever depth suits them. It is
written at six levels, mapped in the [README](README.md).

It is **not** medical advice, and no document in it establishes a clinician–patient
relationship. If you have diabetes, your endocrinologist knows your case and this repository
does not.

---

## A note for clinicians

If a patient has brought you this repository, or material like it, there is a briefing written
for exactly that situation:
[`docs/clinical/when-a-patient-brings-you-this.md`](docs/clinical/when-a-patient-brings-you-this.md).
It covers which of their claims are actually correct (several are), which are not, and how to
have the conversation without losing the patient's trust — because the access grievance driving
this material is legitimate, and dismissing all of it tends to confirm the patient's belief
that they are not being listened to.
