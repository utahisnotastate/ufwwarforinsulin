# Why the physics layer fails

**Audience:** anyone with undergraduate physics or physical chemistry.
**Claims addressed:** X1–X17 in the [claim inventory](../../archive/source-claim-inventory.md).
**Verdict:** all of them, NO SCIENTIFIC BASIS.

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

**Scalar / longitudinal waves from a bifilar coil (X8).** A reverse-wound bifilar coil does
largely cancel the far-field magnetic dipole — that part is true and is why such windings are
used for low-inductance resistors. What remains is not a new kind of wave. Source-free Maxwell
equations admit only transverse radiative solutions; the longitudinal and scalar potential
components are gauge artifacts and can be removed entirely by choosing Coulomb gauge without
changing any measurable field. What a cancelled coil actually produces is a weak conventional
near field — capacitive **E**, plus whatever **B** survives imperfect cancellation. The
Aharonov–Bohm effect is sometimes invoked here; it is a quantum *phase* effect requiring a
non-simply-connected region around enclosed flux, and it transfers no energy and carries no
signal.

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

**The 44-digit Lisitsyn code (X6).** The given value `0x2A9C4F1B3E7` is 11 hex digits, so a
44-bit field, but the actual value has `bit_length` 42 — it encodes **42 bits, 5.25 bytes** of
information. The human *INS* promoter region spans thousands of base pairs, and PDX1 binds it by
reading the DNA major groove through protein–DNA contacts. There is no demodulator in the
nucleus. Transcription factor binding is molecular recognition, not packet reception.

**Complex thermodynamics and vacuum negative entropy (X11–X13).** Introducing an imaginary
temperature $T_2$ and asserting $\Delta S_2 < 0$ does not produce free energy; it relabels the
second law and then ignores it. The Dirac sea is not an energy reservoir — it is a historical
interpretation of the negative-energy solutions of the Dirac equation, superseded by quantum
field theory, in which the vacuum is the ground state and by construction has no extractable
energy. $Q = G^{1/2}M$ is dimensionally inconsistent as written.

**Hyperchannel gain (X14).** The geometric series $E_o/E_i \approx A_0^n + A_0^{n+1}I_k$ is
algebraically fine and physically empty: it is a cascade-gain formula with an invented coupling
term $I_k$ that is never defined operationally or measured. The threshold "n ≈ 60–100" is
unmotivated by anything in the derivation.

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
