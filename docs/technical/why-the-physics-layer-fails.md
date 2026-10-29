# Why the physics layer fails

**Audience:** anyone with undergraduate physics or physical chemistry.
**Claims addressed:** X1–X17 in the [claim inventory](../../archive/source-claim-inventory.md).
**Verdict:** 15 of 17 have no scientific basis. Two — X8 (the Whittaker decomposition) and X13
(the gravitoelectromagnetic algebra) — have a genuine established kernel wrapped in an
unsupported extrapolation, and this document is careful to separate those. Four others have
real physics adjacent to them that deserves credit.

This document does not dismiss the physics layer by assertion. It works the numbers, using the
source's own equations wherever it supplies them, and shows where each argument breaks. Every
calculation here is reproducible from the constants given.

The short version: the central claim is that you can transmit the "rotational signature" of
insulin into the body with a 11.428 kHz radio carrier and make cells take up glucose without any
insulin present. Four independent arguments kill this, and any one of them is sufficient.

---

## 1. 11.428 kHz is below the entire rotational spectrum, not a line within it

The source gives the rigid-rotor relation explicitly:

$$\nu_B = \frac{h}{8\pi^2 I}, \qquad I = \mu r^2$$

and asserts that for the zinc-coordinated insulin hexamer this evaluates to **11.428 kHz**.

The first thing to notice is that the source has misread its own equation. $h/8\pi^2I$ is the
**rotational constant** $B$ — a scale parameter — not a transition frequency. For a rigid rotor
the allowed transitions are

$$\nu = 2B(J+1), \qquad J = 0, 1, 2, \dots$$

so the **lowest frequency anything can absorb or emit is $2B$**, and every other line sits
above it. There is no sub-$2B$ part of the spectrum to hide a signal in.

Now evaluate. Human insulin monomer, 5,808 Da, protein density ~1350 kg/m³ giving an equivalent
sphere radius of 1.195 nm (experimental hydrodynamic radius 1.2–1.6 nm — a good check):

| quantity | value |
|---|---|
| $m$ | $9.644\times10^{-24}$ kg |
| $R$ | $1.195\times10^{-9}$ m |
| $I = \tfrac{2}{5}mR^2$ | $5.51\times10^{-42}$ kg·m² |
| $B = h/8\pi^2I$ | $1.52\times10^{6}$ Hz = 1.52 MHz |
| **lowest transition, $2B$** | **3.05 MHz** |

To land at 11.428 kHz you would need

$$J+1 = \frac{11{,}428}{2 \times 1.52\times10^{6}} = 0.00375$$

a non-integer less than one. **No such state exists.** The claimed frequency is **267× below
the lowest transition any 5.8 kDa object can have.**

You cannot repair this by choosing a larger molecule. $B$ scales as $1/I$, so pushing $2B$ down
to 11 kHz requires a mass roughly $10^7$ times greater — a ~60 GDa particle, about the size of
a small virus capsid aggregate, not a hormone. Running the same calculation on the hexamer
(34,900 Da, $R \approx 2.4$ nm) gives $B = 62.9$ kHz and a lowest transition of **126 kHz**,
still an order of magnitude above the claimed figure and outside the source's own stated
10–100 kHz window.

One more diagnostic detail: **11.428 ≈ 80/7 = 11.4286.** The figure has the arithmetic
signature of a derived ratio rather than a measurement, and no spectroscopic source reports it.
A quantity quoted to four significant figures that does not reproduce from its own stated
equation was not calculated. It was chosen.

Everything below applies even if you grant the number.

---

## 2. Thermal energy swamps the quantum by nine orders of magnitude

A quantum of 11.428 kHz radiation carries

$$E = h\nu = 7.57\times10^{-30}\ \text{J}$$

The thermal energy available to every degree of freedom in a 37 °C body is

$$k_BT = 4.28\times10^{-21}\ \text{J}$$

$$\frac{k_BT}{h\nu} = 5.65\times10^{8}$$

Thermal agitation exceeds the proposed quantum by **565 million times**. Any ladder of
rotational states separated by this energy is populated essentially uniformly by ambient heat;
the Boltzmann factor $e^{-h\nu/k_BT}$ is $1 - 1.8\times10^{-9}$, i.e. indistinguishable from 1.

This is the same physics that explains why radio waves do not break chemical bonds, why
microwave ovens heat by dielectric relaxation rather than by exciting molecular transitions, and
why non-ionizing radiation is non-ionizing. There is no "coherence" trick that evades it: you
cannot selectively drive a transition whose energy gap is nine orders of magnitude below the
noise floor, any more than you can hear a pin drop over a jet engine by listening more carefully.

The source anticipates this objection and answers it with the "damplifier" principle — that
*lowering* power to below $10^{-7}$ W/cm² improves coupling because high power "destroys
coherence." This inverts the physics. Signal-to-noise does not improve as signal decreases.

---

## 3. A protein in water does not have rotational quantum states at all

This is the deepest problem, and it is conceptual rather than arithmetic.

The rigid-rotor energy ladder $E_J = \tfrac{\hbar^2}{2I}J(J+1)$ describes a molecule rotating
**freely** — in a dilute gas, between collisions. It is how microwave rotational spectroscopy
works, and it works beautifully for small molecules in the gas phase.

A protein in cytoplasm is not in the gas phase. It does not rotate freely; it undergoes
**rotational diffusion**, a heavily overdamped random walk in orientation driven by continuous
collisions with water. The governing quantity is the Stokes–Einstein–Debye rotational
correlation time:

$$\tau_c = \frac{\eta V}{k_B T}$$

With $\eta = 0.692$ mPa·s (water at 37 °C) and $V = \tfrac{4}{3}\pi R^3$:

| species | $\tau_c$ |
|---|---|
| insulin monomer | 1.17 ns |
| insulin hexamer | 9.36 ns |

These are measured quantities, not just theoretical — NMR relaxation and fluorescence
anisotropy give rotational correlation times for insulin in exactly this range. Now compare to
the carrier:

- Period of an 11.428 kHz wave: **87.5 µs**
- Hexamer rotational correlation time: **9.36 ns**
- **The molecule completely randomizes its orientation ~4,700 times during a single half-cycle
  of the carrier.**

Whatever orientational information you imagine the field imposing is averaged to zero thousands
of times before the field has finished one swing. There is no persistent phase relationship to
exploit.

A second timescale makes it worse. The **angular momentum** correlation time
$\tau_J = I/\zeta_{rot}$, with rotational friction $\zeta_{rot} = 8\pi\eta a^3$, comes out at
**77–183 fs**. Against an 87.5 µs carrier period, the molecule's angular momentum is
randomized by solvent collisions on the order of **10⁹ times per cycle**. No phase coherence of
any kind survives to be driven.

### The linewidth argument, which is the same point in the frequency domain

Damping that fast implies enormous spectral broadening:

$$\Delta\nu \approx \frac{1}{2\pi\tau_c} \approx 57\text{–}136\ \text{MHz}$$

(depending on whether you use the dry or hydrated radius). Compare that to the **level spacing**
computed in §1, $2B = 3.05$ MHz for the monomer: **the lines are 19–45× broader than the gaps
between them.** The rotational ladder is not merely hard to resolve; it is completely washed
out into a featureless Debye relaxation continuum.

This is precisely why rotational spectroscopy is done in dilute gas phase. In condensed phase,
rotation is diffusive rather than quantized-and-resolvable. There is no peak, no Q, and nothing
to tune to — and specifying a center frequency to four significant figures is spurious
precision by roughly seven orders of magnitude.

### And the wavelength forbids selective coupling anyway

$$\lambda = c/\nu = 2.62\times10^{4}\ \text{m} \approx 26\ \text{km}$$

against a molecule 2.4 nm across — a ratio of **1.1 × 10¹³**. The field is uniform across the
molecule to one part in ten trillion. There is no gradient, no phase structure, nothing that
could couple to an internal coordinate rather than translating the whole object. Dipole
coupling efficiency scales as $(d/\lambda)^2$, suppressing it by ~10⁻²⁶.

---

## 4. A rotational frequency cannot encode molecular identity

Grant everything above. The scheme still fails on information grounds.

$\nu_B$ depends on exactly one property: the moment of inertia, which is mass distribution.
It contains **no information** about amino acid sequence, surface chemistry, charge
distribution, or binding epitope. Any molecule of similar mass and shape has the same rotational
constant — cytochrome c, a small antibody fragment, and a random 35 kDa globular protein are
indistinguishable in this coordinate.

So even a perfect transmitter of "the rotational signature of insulin" would be transmitting a
quantity that is **not specific to insulin**. The source has selected, out of all possible
molecular observables, essentially the one that cannot carry the identity it needs to carry.

Receptor activation is a shape-recognition event. The insulin receptor ectodomain is held in an
autoinhibited inverted-V; insulin binding at site 1/site 2 drives it into a T-shaped
conformation that brings the transmembrane helices together so the intracellular kinase domains
can trans-phosphorylate (this part of the source's description, claim F1, is **correct** — see
the [receptor note](insulin-receptor-and-signaling.md)). That conformational change is produced
by a ligand making specific contacts and paying ~55 kJ/mol of binding free energy. An
oscillating far-field potential is not shaped like insulin and makes no contacts. There is no
transduction path.

---

## 5. The subsidiary claims

**Scalar / longitudinal waves from a bifilar coil (X8).** This one needs to be split into
three statements, because they have three different truth values and collapsing them is how
the argument gets its credibility.

1. **The Whittaker decomposition is established mathematics.** Whittaker showed in 1903–04
   that a scalar potential in a source-free region can be written as a superposition of paired
   counter-propagating wave sets. That is real, it is in the literature, and it is a
   *representation* — a change of bookkeeping, not new physics.
2. **A reverse-wound bifilar coil does largely cancel the far-field magnetic dipole.** Also
   true, and it is why such windings are used for low-inductance resistors.
3. **That the remainder constitutes a separate channel carrying power or information is
   neither established nor demonstrated** — and it is testable. Source-free Maxwell equations
   admit only transverse radiative solutions; the longitudinal and scalar components are
   gauge-dependent and removable in Coulomb gauge without changing any measurable field. What
   a cancelled coil actually produces is a weak conventional near field: capacitive **E**,
   plus whatever **B** survives imperfect cancellation.

The honest label on (3) is therefore not "nonsense" but **testable, with a strongly expected
null** — and a protocol already exists:
[FallOfPhysics E005](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E005-scalar-vs-transverse)
measures received power against the Friis baseline while applying the claimed scalar-enhancing
configuration without increasing drive current. See [§7](#7-this-has-already-been-audited-twice).

The Aharonov–Bohm effect is often invoked at this point. It is real and was confirmed in 1986,
and it genuinely shows that potentials have measurable consequences — but it is a quantum
*phase* effect requiring a non-simply-connected region around enclosed flux. It transfers no
energy and carries no signal.

**Keratin piezoelectric rectification (X5).** Keratin *is* weakly piezoelectric — this is real
and measured (Fukada, Zimmerman & Mascarenhas, *BBRC* 1975, on bovine horn). Three things kill
the claim anyway:

1. **The effect is tiny and shear-only.** Horn keratin's shear constant $d_{14} \approx 1.8$
   pC/N; wool ≈ 0.1 pC/N. Compare quartz at 2.3 pC/N and PZT at 300–600 pC/N. The converse
   effect at 1 V/m gives a strain around 10⁻¹² — unmeasurable. And the stratum corneum's
   keratin is dead, dehydrated, and not macroscopically poled, so fibril orientations average
   the shear response toward zero across the skin surface.
2. **Piezoelectricity is linear, so it cannot rectify.** The constitutive relation is
   $S = dE$. Rectification requires a *nonlinear, asymmetric* characteristic — a diode. A
   linear transducer produces output at the input frequency, full stop. "Piezoelectric
   rectification" is a category error, not an overstatement.
3. **There is nothing to decode with.** Even granting rectification, no mechanism is proposed
   — or available — by which an amplitude envelope on a 26-km carrier becomes a specific
   protein conformation.

**And the premise is self-refuting.** Skin depth in physiological saline (σ ≈ 1.5 S/m) at
11.428 kHz is

$$\delta = \sqrt{2/(\omega\mu\sigma)} = 3.84\ \text{m}$$

**VLF passes through an entire human body essentially unattenuated.** This is exactly why VLF
is used to communicate with submerged submarines. So there is no transdermal coupling problem
for the keratin mechanism to solve — and if a VLF carrier did what the source claims, it would
already be doing it to everyone standing near a switching power supply, a CRT flyback
transformer, or a naval VLF transmitter.

> **The real phenomenon nearby, which deserves credit.** There *is* a genuine effect in this
> neighborhood, and the source is distantly echoing it. **Electrophonic hearing** is well
> documented: people really do perceive sound from electrical and ultrasonic stimulation
> outside the ear canal, and ultrasonic bone-conduction hearing is established (Lenhardt et
> al., *Science*, 1991). Puharich and Lawrence, whom the source cites, really did file
> hearing-device patents. So transdermal and transcranial energy *can* produce perception.
>
> What has never been demonstrated is the specific mechanism claimed here — keratin acting as
> a biological crystal diode that demodulates a carrier. Perception of a stimulus is not
> demodulation of an encoded molecular signature, and bone conduction into the cochlea is not
> receptor activation in peripheral tissue.



**Meridians, cellulomas, and $J_{elec} = (1/c)\nabla\Phi$ (X7).** The conversion formula is
not a recognized relation and is dimensionally unmotivated; "anenergy," "second bioframe," and
"celluloma" are not terms with referents in anatomy or physiology.

But one component deserves a more careful label than the rest. **Skin impedance genuinely does
vary by location** — that is established and measurable, and there is a straightforward
protocol for it
([FallOfPhysics E006](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E006-skin-impedance)).
Whether *acupuncture points specifically* show reliably lower impedance is **contested rather
than refuted**: the systematic review by Ahn et al. (2008) found the evidence inconsistent
across studies. So the correct reading is a real, variable physical quantity with a disputed
mapping onto meridian points — and no support whatever for the orthogonal-frame machinery
built on top of it.

**The 44-digit Lisitsyn code (X6).** The given value `0x2A9C4F1B3E7` is 11 hex digits, so a
44-bit field, but the actual value has `bit_length` 42 — it encodes **42 bits, 5.25 bytes** of
information. The human *INS* promoter region spans thousands of base pairs, and PDX1 binds it by
reading the DNA major groove through protein–DNA contacts. There is no demodulator in the
nucleus. Transcription factor binding is molecular recognition, not packet reception.

The companion claim — that biological information rides on bands "extending up to
8.1 × 10²⁰ Hz" — has a one-line refutation worth doing explicitly:

$$E = h\nu = 6.626\times10^{-34} \times 8.1\times10^{20} = 5.37\times10^{-13}\ \text{J} = \mathbf{3.35\ MeV}$$

That is hard **gamma radiation**, far above the 1.022 MeV pair-production threshold. It is not
a brain signal; it is the energy scale of nuclear transitions, and tissue emitting it would be
a radiological emergency.

There is a runnable null test for the code claim itself:
[FallOfPhysics E010](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E010-impedance-code-test)
quantizes skin impedance across sites, computes per-site Shannon entropy, and tests retest
reliability across days — distinguishing a fixed low-entropy 44-symbol message from
sweat-and-noise physiology.

**Complex thermodynamics and vacuum negative entropy (X11–X12).** Introducing an imaginary
temperature $T_2$ and asserting $\Delta S_2 < 0$ does not produce free energy; it relabels the
second law and then ignores it. The Dirac sea is not an energy reservoir — it is a historical
interpretation of the negative-energy solutions of the Dirac equation, superseded by quantum
field theory, in which the vacuum is the ground state and by construction has no extractable
energy. A claim that Gibbs free energy spontaneously increases in an isolated system is a
second-law violation however it is notated.

**$Q = G^{1/2}M$ (X13) — more subtle than it looks, and worth getting right.** Substituting
$\sqrt{G}\,M$ for charge in Coulomb's law does reproduce Newton's law of gravitation. That is
**legitimate algebra**, and it is the basis of gravitoelectromagnetism, a real weak-field
approximation of general relativity. So the manipulation itself is not a blunder, and saying
so flatly would be wrong.

What fails is everything built on top of it:

- The **triple equality** $E = mc^2 = (c^2/\sqrt{G})Q$ is not dimensionally consistent. $E$ and
  $mc^2$ are joules; $c^2/\sqrt{G}$ carries units of m³/(kg·s²), so the equality holds only if
  $Q$ is assigned custom units chosen to make it work — and no single $Q$ satisfies all three
  equalities at once without being defined into existence.
- Reading $Q$ as "virtual charge" or "consciousness," and the relation as an **interconversion
  law**, adds a physical claim that the algebra never contained. An analogy between two
  inverse-square laws is not a conversion mechanism between matter and mind.

**Hyperchannel gain (X14) — likewise.** The underlying physics the source is reaching for is
**real**: coherent sources add in amplitude, so power scales as $N^2$. That is Dicke
superradiance (1954), and it is how phased-array antennas and lasers work.

What fails is the extrapolation. $E_o/E_i \approx A_0^n + A_0^{n+1}I_k$ is a standard geometric
series applied to an undefined quantity: the coupling term $I_k$ is never defined
operationally or measured, and the threshold "n ≈ 60–100" is unmotivated by anything in the
derivation. Coherent addition requires a **physical coupling channel**, which is exactly what
is missing.

And here too there is a real phenomenon nearby: **inter-brain synchrony is genuine**.
Hyperscanning studies reliably show neural synchronization between people during conversation,
music, and cooperation. It is an ordinary consequence of shared attention and shared timing,
not an exponential channel — but it exists, and the honest version is more interesting than
the invented one. Null protocol:
[FallOfPhysics E008](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E008-coherence-null-test).

---

---

## 5b. Where this idea comes from, and what the real literature says

The "transmit the molecule's signature instead of the molecule" concept is not original to this
source. It descends from **Jacques Benveniste's** 1988 *Nature* basophil "water memory" paper —
which failed independent replication (Hirst et al., *Nature* 1993;366:525–527) and was the
subject of the Maddox/Randi/Stewart investigation published in *Nature* the same year — and
from his later DigiBio "digital biology" work on recording and replaying molecular activity
electronically. **Luc Montagnier** continued the line (*Interdiscip Sci* 2009;1:81–90), using a
Benveniste-derived device, in a journal whose editorial board he chaired, reviewed in days,
and never independently replicated.

Knowing the lineage is useful because the objection is the same in every generation of it and
it is not really a physics objection at all: **information about a molecule is not a
substitute for the molecule.** The receptor is activated by specific non-covalent contacts with
specific atoms. A waveform does not supply atoms.

### What the legitimate bioelectromagnetics literature actually contains

It is thin, and none of it is in this paradigm — but it exists and it deserves accurate
representation rather than being swept in with the rest:

- **Carter CS et al., *Cell Metabolism* 2020;32(4):561–574** — static magnetic + electric
  fields improved insulin sensitivity in mouse models of Type 2 diabetes within ~3 days, with
  the effect abolished by removing hepatic superoxide. This is a *static field* study with a
  *redox* mechanism, not a resonance study. Mice and cells only; the paper carries a correction
  and an erratum (not retracted); the authors founded a company on it, declared.
- **PEMF for diabetic neuropathic pain** — a real but mediocre literature. Weintraub et al.
  (*Arch Phys Med Rehabil* 2009, n=225) found only a trend on the primary endpoint. A 2026
  meta-analysis of 13 RCTs (N=688) reports pooled SMD −1.01 but with **I² = 92.8%**, which the
  authors themselves call unstable.
- **PEMF and glycemic control: essentially nothing.** No systematic review or RCT using HbA1c
  as an endpoint could be located.

So: a weak signal for pain, a mouse study with a different mechanism and different field type,
and nothing at all on blood glucose in humans. That is the honest state of the field, and it
is a long way from ligand-free receptor activation.

### Where the real biomolecular resonance frontier actually is

This is the constructive version of the question, and it is worth answering because a reader
who finds the 11.428 kHz idea appealing is interested in something real.

| Degree of freedom | Frequency | Energy vs. kT (310 K) |
|---|---|---|
| **Claimed "insulin resonance"** | **11.428 kHz** | **1.8 × 10⁻⁹ kT** |
| Insulin rigid-rotor J=0→1 (gas phase, hypothetical) | 3.05 MHz | 5 × 10⁻⁷ kT |
| Insulin rotational relaxation in water (Debye) | 57–136 MHz | not a transition |
| Small-molecule rotational spectroscopy (real) | 1 GHz – 1 THz | 10⁻⁴ – 10⁻¹ kT |
| **Protein collective modes, H-bond network** | **0.1 – 10 THz** | **10⁻² – 1.5 kT** |
| Molecular vibrations (IR) | 10 – 100 THz | 1.5 – 15 kT |
| Electronic transitions (UV/vis) | 400 – 1500 THz | 60 – 230 kT |

**Proteins do have collective vibrational modes, and they are measurable** — by terahertz
time-domain spectroscopy and Raman. That is established. Whether those modes support
*coherent* long-range behavior is the **Fröhlich condensation** question: proposed in 1968,
still debated, with some suggestive THz evidence in lysozyme (Lundholm et al., 2015). Label
it 🟡 open.

Note where it sits: **0.1–10 THz is seven to nine orders of magnitude above the claimed
figure**, and it is the only band where the quantum is comparable to kT — which is precisely
why it is the only band where coherent molecular effects are even arguable. The source picked
a frequency eight orders of magnitude below the one place something interesting might be
happening.

If you want the honest version of "biomolecules have resonances that matter," that is the
literature to read. See also
[mitochondria/academic/formalisms/03_protein_folding_thz.md](https://github.com/utahisnotastate/ufwwaragainstthemitochondria/blob/main/academic/formalisms/03_protein_folding_thz.md),
which treats THz-TDS as a genuine probe (tier B) while rejecting the therapeutic
"hydration-shell clamping" extrapolation — the same split this document keeps making.

---

## 6. How to test it, if you want to

The honest thing about this hypothesis is that it is cheap to falsify, and that is worth saying
because nobody has to take any of the above on authority.

The assay is standard undergraduate cell biology:

1. Plate differentiated **3T3-L1 adipocytes** or **L6 myotubes** — both are classic
   insulin-responsive lines with large, well-characterized GLUT4 translocation responses.
2. Serum-starve, then expose to the field for the proposed duration, with proper sham controls
   (identical apparatus, drive disconnected) and the operator blinded to condition.
3. Read out either **2-deoxy-D-glucose uptake** (radiolabeled or colorimetric) or
   **phospho-Akt Ser473 by Western blot**, against an insulin-stimulated positive control.

A real effect on glucose uptake would be unmissable — insulin produces a 5–15× increase in
2-DG uptake in these cells. Positive results would be publishable immediately and would
constitute one of the most important findings in the history of cell biology.

No such result exists. The literature on electromagnetic fields and insulin signaling is small,
consists mostly of low-powered studies with inconsistent endpoints, and reports nothing
resembling ligand-free receptor activation. If you build the device, run this assay before you
believe anything it appears to do — and never, under any circumstances, run it on yourself in
place of insulin.

---

## 7. This has already been audited twice

The physics layer in the insulin transmission is not new material. It is the **same framework,
from the same oracle persona, with the same citations**, that appears in two other source
documents — and both have already been audited claim-by-claim in sibling repositories:

- **[FallOfPhysics](https://github.com/utahisnotastate/FallOfPhysics)** — wave physics, signal
  processing, bio-instrumentation. Labels: ESTABLISHED / TESTABLE / SPECULATIVE / NOT SUPPORTED.
  Ships **eleven experiment protocols (E001–E011)**, including null tests for the extraordinary
  claims.
- **[RiseOfGeometry](https://github.com/utahisnotastate/RiseOfGeometry)** — "Future Disclosure:
  Sacred Geometry," 31 disclosures, ~105 individual claims. Labels: ✅ established / 🟡 open /
  🧪 testable / 📜 historical / ❌ not supported.

**Both reach the same verdict this document reaches, independently.** That convergence is worth
more than any single analysis, so the mapping is given in full:

| Insulin claim | FallOfPhysics | RiseOfGeometry | Verdict there |
|---|---|---|---|
| **X2/X3/X4** Eerkens VLF macromolecular maser | — | **D12** | ❌ *"Molecules in liquid water don't hold rotational states. Collisions destroy them in picoseconds."* |
| **X5** Keratin diode demodulation | — | **D27** | ❌ not demonstrated — though electrophonic hearing ✅ and Puharich patents ✅ are real |
| **X6** 44-digit biological code | **E010** | **D06** | ❌ no such finding; 8.1 × 10²⁰ Hz = 3.35 MeV gamma |
| **X7** Acupuncture meridians / cellulomas | **E006** | **D24** | 🟡 impedance varies; point-specificity contested (Ahn 2008) |
| **X8** Scalar / longitudinal channel | **E005** | **D01** | Whittaker math ✅ (1903); extra power channel 🧪 testable, expected null |
| **X10** Damplifier topology | **E005** | **D07** | ❌ radionics; no blinded replication |
| **X11/X12** Inomata complex thermodynamics, ΔS₂ < 0 | concept doc | **D05, D11** | ❌ second-law violation |
| **X13** Q = G^(1/2)M | concept doc | **D28** | ✅ as GEM algebra; ❌ as interconversion law |
| **X14** Hyperchannel exponential gain | **E008** | **D09, D21** | ❌ — though N² coherent scaling ✅ (Dicke) and inter-brain synchrony ✅ |
| **X15** Dubrov biogravitation / conformons | — | **D04, D12** | ❌ no independent confirmation |
| **X16** Seven-stage biospheric evolution | — | **D26** | ❌ speculative |
| **X17** Fourth Law of Logic [A₁ ≡ Ā₂]₃ | claims doc | **D04** | ❌ not a recognized law — **T. E. Bearden, self-published** |
| Non-local / instantaneous transmission | **E009, E011** | **D17** | ❌ phase velocity carries no information |

Two things follow from this table.

**First, the provenance is now traceable.** The "Fourth Law of Logic" is Bearden's; the
"biogravitation" is Dubrov's; the complex thermodynamics is Inomata's; the macromolecular
maser is Eerkens'; the transdermal work is Puharich's. These are real people who published
real documents, almost all self-published or in non-indexed venues, mostly in the 1970s–80s
psychotronics literature. The transmission is not retrieving future knowledge — it is
recombining a specific, identifiable mid-century corpus. Recognizing the corpus is what lets
you check it.

**Second, there are runnable protocols.** The single biggest gap in a document like this is
that "no mechanism exists" is unfalsifiable-sounding even when correct. It isn't, and the
tests are cheap:

| Test | What it settles | Cost |
|---|---|---|
| [E005](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E005-scalar-vs-transverse) — scalar vs. transverse power | Does a bifilar/scalar configuration deliver power beyond the Friis baseline? | $$$ (lab) |
| [E008](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E008-coherence-null-test) — coherence null | Does group phase-locking produce super-linear output? | ~$5 |
| [E009](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E009-no-ftl-signaling) — no FTL signaling | Can any "instant channel" beat a light-speed RF link? | $$ |
| [E010](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E010-impedance-code-test) — 44-digit code entropy | Is skin impedance a fixed low-entropy code or sweat + noise? | ~$25 |
| [E011](https://github.com/utahisnotastate/FallOfPhysics/tree/main/experiments/E011-resonant-coupling-speed) — coupling speed | Does resonant transfer scale with distance (finite) or not (instant)? | ~$15–30 |
| [RoG E007](https://github.com/utahisnotastate/RiseOfGeometry/blob/main/experiments/E007-blinded-radionics-test.md) — blinded radionics | Does a drawn/symbolic circuit do anything a sham doesn't? | low |
| **§6 above** — 2-DG uptake / phospho-Akt | Does the VLF field trigger glucose uptake in insulin-responsive cells? | lab |

The last row is the one specific to insulin, and it is the one nobody has run. The other six
already have protocols written.

### A note on label harmonization

This repository's status key is a superset of the other two. For anyone cross-reading:

| Here | FallOfPhysics | RiseOfGeometry |
|---|---|---|
| ✅ VERIFIED | ESTABLISHED | ✅ established |
| 🟡 PARTLY TRUE | (split across labels) | 🟡 open / 📜 historical |
| 🔵 OPEN | SPECULATIVE | 🟡 open · 🧪 testable |
| ❌ NOT TRUE | NOT SUPPORTED | ❌ not supported |
| ⛔ NO BASIS | NOT SUPPORTED | ❌ not supported |
| ☠️ harm flag | *(no equivalent — this repo adds it)* | *(no equivalent)* |

The harm flag is the one thing the insulin domain needs that the physics repos didn't: a wrong
claim about scalar waves wastes your afternoon, and a wrong claim about insulin kills you in
two days.

---

## Why this matters more than the usual "that's pseudoscience"

The physics layer is not harmless decoration around good biology. In the source material it is
load-bearing: it is what licenses the conclusion that a person could manage blood glucose
without insulin. Claims X9 and D6 together say that hypoglycemia is impossible and insulin mass
is unnecessary. A person with Type 1 diabetes who acted on that would be in ketoacidosis inside
two days.

The rest of this repository takes the source's biology seriously because much of it is real.
That makes it more important, not less, to be unambiguous about the part that is not.

---

**See also**
- [`../../INTEGRITY_AUDIT.md`](../../INTEGRITY_AUDIT.md) — full claim-by-claim scoring
- [`insulin-receptor-and-signaling.md`](insulin-receptor-and-signaling.md) — what receptor
  activation actually requires, and why claim F1 is correct while X9 is not
- [`../../SAFETY.md`](../../SAFETY.md)
