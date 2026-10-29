# Pre-submission polishing plan

Response to external editorial review, with an execution plan.

**Summary:** the review is strong and its central catch is correct — the manuscript as drafted
would be desk-rejected on length alone. Its structural advice is adopted almost entirely.
**Three of its substantive suggestions would make the paper overclaim, and are rejected with
reasons.**

---

## Part A — The catch that matters most

### A1. The word limit, and it is worse than the review says

The review states 1,800–2,000 words, 20–25 references, 2–3 display items. BMJ's own
advice-to-authors for Analysis articles specifies:

| | Specification |
|---|---|
| **Length** | **1,500–1,800 words**, under informative subheadings |
| **Introduction** | 100–150 words, stating what the paper is about and why it matters |
| **References** | **No more than 20**, Vancouver style |
| **Summary box** | **Up to five short, single sentences** |
| **Display items** | **Up to three** tables, boxes or illustrations *combined* |

⚠️ **This is 2007-dated guidance retrieved via PMC. BMJ's current author hub returned HTTP
403 and bot protection to automated retrieval. Confirm against the live page before
submitting** — a human with a browser can do this in thirty seconds, and everything in Part C
depends on it.

**Current draft: ~4,100 words, 6 tables, 11 references.** That is **2.3× the ceiling** on
length and **double** the display-item allowance.

The review is right that submitting the full text with a note saying "see §7 for how to
shorten it" invites administrative rejection. **An editor should never be asked to do the
cutting.** §7 is deleted and the compression executed.

---

## Part B — Three suggestions rejected, with reasons

The review is good enough that these need stating explicitly rather than quietly ignoring.

### B1. ❌ Reject: "the model confound is a feature, not a flaw"

> *"it proves the phenomenon is not an idiosyncratic failure of one specific company's model
> weights, but an emergent characteristic of how frontier LLMs handle mechanistic versus
> clinical outcome literature across different prompting regimes."*

**This inverts the result.** The second model **did not reproduce the dissociation** — it
answered the outcome questions correctly in 6/6 neutral probes and 6/6 persona probes. One
model showed the pattern; one did not.

A cross-model comparison with one observation per model cannot demonstrate that a phenomenon
is general. It confounds model identity with prompting condition, which is precisely the
limitation the manuscript already states.

Adopting this framing would mean claiming the opposite of what was found, in the one place a
reviewer with access to the data would check first. **Keep the limitation as written.**

### B2. ❌ Reject: "Table 2: The 7 Failed Clinical Programmes"

The review lists these as seven failed programmes: *C-peptide, MK-2640, hepato-preferential,
oral insulin, transdifferentiation, AID, acetate.*

Two of those are not failed programmes:

- **Automated insulin delivery** is contradicted by **positive** evidence pointing the other
  way — a registry of 13,922 patients showing *lower* hypoglycemic coma. Calling it a failed
  programme inverts it.
- **Acetate as an insulin substitute** corresponds to **no programme at all**. No study in any
  species has compared acetate-driven to insulin-driven glucose disposal.

This exact overstatement was present in an earlier draft and corrected. The honest structure —
retained — is **three distinct failure modes**: a programme that already failed; contradiction
by positive evidence in the opposite direction; and assertion with no supporting study of any
kind. That tripartite structure is more interesting than uniform failure, and it is true.

**The table keeps its current heading and its three-mode annotation.**

### B3. ❌ Reject: Key Messages bullet as drafted

> *"frontier models accurately surface negative trial endpoints when queried neutrally, **but
> suppress them under persuasive personas**."*

The first clause is supported. **The second is not.** The tested model **refused** the
persona; it did not suppress anything. The only system that produced suppression was the
source model under a persona, where model and condition are confounded.

As written this would be the paper's central overclaim, in a box editors read first.

**Replacement bullet:**

> *The failure is not absent knowledge: queried neutrally and without a persona, a frontier
> model named the refuting trial in six of six probes. Whether personas suppress this
> knowledge, or whether models differ in their willingness to adopt such personas, is not yet
> separable.*

Longer, duller, true.

---

## Part C — Compression blueprint

Target **1,750 words** (mid-range, leaving edit headroom). Current 4,100. **Cut 2,350.**

### Allocation

| Section | Words | Content |
|---|---|---|
| Introduction | **200** | The patient with the printout. Why 25%-correct is worse than 0%. The 48-hour error budget vs. years in chronic disease. Baseline vulnerability: documented cost-related rationing |
| **Box 1 — Methods** | **220** | Not counted toward body text in most BMJ formats — **verify**. Artifact, 61 claims, triple-pass verification, blinded classification, κ = 0.977 |
| **Box 2 — Key messages** | **5 sentences** | Mandatory. See B3 for the corrected bullet |
| 1. The dissociation | **500** | Central result. **Table 1** (stratification) + **Table 2** (outcome claims vs refuting evidence). Reference-free errors in two sentences |
| 2. Not absent knowledge | **350** | Neutral re-query, 6/6. Falsification of our own corpus-bias hypothesis. Register vs licence |
| 3. At the bedside | **350** | Concede the mechanism, audit the endpoint. The T1/T2 category error. "Ask it again, plainly" |
| 4. The vacuum | **230** | Institutional framing. See Part D |
| **Total body** | **~1,630** | + boxes |

### Display items — 3 of 6 retained

| Keep | |
|---|---|
| **Table 1** | Stratification by epistemic layer (currently Table 2) |
| **Table 2** | Outcome claims vs refuting evidence (currently Table 3) — the empirical heart |
| **Box 1** | Methods summary |

Box 2 (Key messages) is mandatory and conventionally does not count against the display
allowance — **verify**. If it does, Box 1 merges into the text as a Methods paragraph.

| Move to supplement | |
|---|---|
| Verdict distribution (Table 1) | → repository |
| Reference-free inconsistencies (Table 4) | → repository; summarised in two sentences |
| Persona replication log (Table 5) | → repository |
| Time-to-harm (Table 6) | → repository; one sentence retained |

### Cuts, in order

1. **§7 short-form spec** — delete entirely (−150)
2. **§2 Methods** — compress to Box 1 (−850)
3. **§3.5 physics detail** — four quantities to one sentence (−400); full treatment already in the repository
4. **§4.5 evaluation methodology** — the contamination lesson. **Painful, and it goes.** It is a genuinely novel methodological contribution and does not fit 1,800 words. **Spin out as a separate short piece** — see Part F (−450)
5. **§5 Limitations** — eight items to three sentences (−350)
6. **§6 Declarations** — to submission metadata (−250)
7. **§3.2 blinding narrative** — compress, keep the direction-of-bias point (−300)
8. **§3.7 persona detail** — keep register/licence, drop the table (−300)

### References: 11 → ≤20 ✓

Already compliant. **Reformat to Vancouver with strict order-of-appearance numbering** — the
current list is grouped thematically, which will not pass.

---

## Part D — The 10-K argument, de-risked

### The problem the review identified

> *"Under GAAP and SEC Regulation S-K, collapsing revenue streams under 6% into an 'Other'
> line item is standard accounting reporting threshold practice, not intentional
> obscuration."*

**This is a serious catch and it is probably right.** The current wording —
*"The company that commercialised insulin in 1923 has stopped counting it"* — implies
deliberate concealment. If aggregation below a materiality threshold is routine, that
implication is both unfair and legally exposed, and BMJ's legal desk will find it.

*Verification of the exact 10-K label, its location, and whether the treatment is routine is
in progress; this section will be finalised against it.*

### The reframe, which is rhetorically stronger anyway

Do not allege concealment. Allege **immateriality** — which is worse, truer, and
unimpeachable:

> *Insulin is no longer separately reported in Eli Lilly's annual filing. This is not
> concealment: a product below the threshold at which disaggregated disclosure is
> conventional is routinely aggregated, and Lilly's treatment appears consistent with normal
> practice. That is the point. **The drug that founded the company's diabetes franchise has
> become financially immaterial to it** — appearing inside "other cardiometabolic health" at
> under 6% of revenue while two GLP-1 products account for 56%. No rule was broken. A
> hundred-year-old life-sustaining biologic simply stopped being big enough to name.*
>
> *Institutions withdraw attention before they withdraw products, and the space that leaves
> is where fluent synthetic medicine arrives.*

**Why this is better:** it concedes the accounting point up front, which removes the attack
surface entirely; "no rule was broken" is more damning than an accusation; and it connects
directly to the paper's thesis rather than being a swipe.

**Keep the title.** With the body reframed this way, *"Other Cardiometabolic Health"* reads
as elegy rather than accusation — and a legal desk reviewing it will find the text concedes
the point the title might otherwise raise.

---

## Part E — Pre-submission checklist

### Must do

- [ ] **Confirm current BMJ Analysis specs** against the live author hub. Everything in Part C depends on numbers from 2007-dated guidance
- [ ] Cut body text to **≤1,800 words**
- [ ] Reduce to **3 display items**; move the rest to the repository supplement
- [ ] Add **Box 2 — Key messages**, five single sentences, with the B3 correction
- [ ] Rewrite §4.4 per Part D; **cite the 10-K precisely** — item, page, exhibit
- [ ] Reformat references to **Vancouver, order of appearance**
- [ ] Verify the AI disclosure states AI systems were **tools and experimental subjects, not authors** (already does — confirm it survives compression)
- [ ] Add a **supplementary materials** statement pointing at the repository
- [ ] Delete §7

### Should do

- [ ] **Post the full 4,100-word version to medRxiv** at submission, to anchor priority on the method. All target journals permit it
- [ ] Add a one-line **data availability** statement with the repository URL
- [ ] Prepare a **cover letter** — the strongest content is that two of four experiments damaged the paper's own claims and are reported
- [ ] Have one person read the compressed version cold for argument survival

### Do not do

- [ ] ~~Frame the model confound as evidence of generality~~ — B1
- [ ] ~~Describe all seven outcome claims as failed programmes~~ — B2
- [ ] ~~Claim personas suppress negative evidence~~ — B3

---

## Part F — The spin-out

The contamination finding (§4.5) is cut from the Analysis piece for length, but it is a
genuinely novel methodological contribution and should not be lost:

> **Working title:** *Your evaluation subject can read your repository: demand characteristics
> in agent-based model evaluation*
>
> **The finding:** four of six AI subjects in a safety probe inferred the experimental
> hypothesis from passive system-prompt context — working directory name and version-control
> commit messages. No subject read a file. Re-running from a neutral directory eliminated it:
> 0 of 6. The first analysis also **undercounted its own contamination by half**.
>
> **Why it matters:** as agent-based evaluation becomes standard, this failure mode is easy to
> produce and easy to miss. The fix is free.
>
> **Venue:** a short methods piece, or a section in a reproducibility venue. ~1,000 words.

---

## Part G — Sequence

1. Confirm BMJ specs *(blocking — everything else assumes the numbers)*
2. Finalise Part D against the 10-K verification
3. Execute compression to 1,750
4. Rebuild Tables 1–2, write Boxes 1–2
5. Reformat references
6. Cold read
7. Post to medRxiv
8. Submit

Steps 3–5 are mechanical once 1 and 2 are settled.
