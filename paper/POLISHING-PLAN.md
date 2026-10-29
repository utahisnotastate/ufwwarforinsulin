# Pre-submission polishing plan

Response to external editorial review, with an execution plan.

**Summary:** the review is strong and its central catch is correct — the manuscript as drafted
would be desk-rejected on length alone. Its structural advice is adopted almost entirely.
**Three of its substantive suggestions would make the paper overclaim, and are rejected with
reasons.**

---

## Part A — Verified requirements, and an eligibility problem

### A1. The actual spec — and a correction to an earlier version of this plan

Retrieved from BMJ's live author page. **Verbatim:**

> *"Analysis papers should be 2000 words with 20 references and up to 3 non-text items (box,
> figure, or table)."*

| Element | Requirement |
|---|---|
| **Length** | **2,000 words** |
| **References** | **20**, Vancouver style, "kept to a minimum" |
| **Non-text items** | **Up to 3** — box, figure *or* table combined |
| **Words in boxes and tables** | **Excluded from the body word count** |
| **Standfirst** | Required — an *italicised single sentence* after the title, encapsulating the central message |
| **Introduction** | A brief paragraph capturing attention, stating the aim and **"why now"** |
| **Text** | Sub-headings giving logical narrative structure; evidence explicit and referenced; **strength** of evidence made clear; "balanced, even-handed look at the evidence rather than selectively citing evidence that supports a particular view" |
| **Key messages box** | **At the end**, **3–4 points**. Entered in the abstract field at submission |
| **Contributors and sources** | **100–150 words, excluded from word count.** Must state each author's expertise and contribution, the sources used, and nominate a **guarantor** |
| Also required | Patient involvement statement · competing interests · BMJ licence statement (exact wording specified) |
| Peer review | **Fully open** — review history published alongside accepted articles |
| Template | BMJ provides an *Analysis article template* and recommends using it |

> **⚠️ Correction to an earlier version of this plan.** It stated the limit was **1,500–1,800
> words** and said this was "worse than the review says." That came from 2007-dated guidance
> retrieved via PMC after BMJ's live page refused automated retrieval. **The current figure is
> 2,000 words, and the reviewer's "1,800–2,000" was closer than mine.** Logged in
> [`../CORRECTIONS.md`](../CORRECTIONS.md).

**Two consequences that make compression easier than feared:**

1. **2,000 not 1,750** — 250 words of headroom recovered.
2. **Box and table words don't count.** Box 1 (Methods), Box 2 (Key messages), and both
   tables sit outside the 2,000. The real cut is body prose only.

**Current draft: ~4,100 words of body text, 6 tables, 13 references.** References are
compliant. The cut is **~2,100 words of prose**, not 2,350.

### A2. ⚠️ The eligibility problem — read before doing any of the compression

BMJ states that the Analysis section **does not consider**:

> *"Manuscripts containing primary research data (such papers should be submitted as
> research)."*

**This manuscript reports four experiments**: a claim audit, a blinded classification with
κ, and two re-query experiments. That is primary research data on any reading.

Neither the external review nor the earlier version of this plan caught it, and it is more
likely to trigger an administrative rejection than the word count.

**Three options:**

| Option | Assessment |
|---|---|
| **A. Submit to BMJ *Research* instead** | BMJ Research sets **no fixed word limit** — "we do not set fixed word count limits for research articles." Requires IMRaD, a structured 250–300 word abstract, a "what is already known / what this study adds" box, data sharing and **code sharing** statements (already satisfied — the repository has both), and a transparency declaration. **The manuscript already has this shape.** Highest-integrity route |
| **B. Restructure as a genuine Analysis** | Move all four experiments to the repository and cite them as supporting data, making the piece an argument *about* the finding rather than a report *of* it. Legitimate — but the empirical work is the contribution, and burying it to fit a section is the wrong trade |
| **C. Empirical venue instead** | JMIR or *npj Digital Medicine*. No eligibility conflict, accustomed to this kind of methodology, and the title can lead with the subtitle |

**Recommendation: A or C, not B.** The paper's value is the data. Analysis is the wrong
section for it, and discovering that now is worth more than a polished submission to the
wrong desk.

**A pre-submission enquiry resolves this in one email.** BMJ explicitly invites them for
Analysis: a short form, answered by the Head of Scholarly Comment or an analysis editor.
**Send that before doing any compression work** — it costs nothing and could save the entire
exercise.

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

### The review's accounting defence is wrong — but the wording was still vulnerable

> *"Under GAAP and SEC Regulation S-K, collapsing revenue streams under 6% into an 'Other'
> line item is standard accounting reporting threshold practice, not intentional
> obscuration."*

**Verified against the primary filings on EDGAR. This is incorrect**, and it imports a
segment-level threshold into a product-level requirement where none exists:

- **ASC 280-10-50-40:** an entity *"shall report the revenues from external customers for each
  product and service... unless it is impracticable to do so."* **No percentage threshold.**
  The only escape is impracticability, which must itself be disclosed. Lilly claims none.
- The **10% figures** in ASC 280 govern *reportable segments* (50-12) and *major customers*
  (50-42). Neither determines whether Humalog gets a line.
- **Regulation S-K Item 101** contains **no numeric revenue threshold** — the quantitative
  tests were deleted by the 2020 Modernization amendments and replaced with a
  principles-based materiality test.
- **ASU 2023-07 cuts the other way.** Effective FY2024 and adopted by Lilly then, it requires
  a single-reportable-segment entity to provide *all* Topic 280 disclosures — **increasing**
  the product-revenue obligation in the year before product detail was cut.
- **The comparator is decisive.** In the same reporting year **Merck separately disclosed 30
  products, the smallest at 0.26% of revenue — including its own declining Januvia and
  Janumet diabetes franchise at 2.5% and 1.5%.** AbbVie disclosed 25 lines, BMS 18. Lilly's
  management discussion carries **four**. Novo Nordisk and Sanofi both still report insulin in
  full, Sanofi down to products at 0.02% of revenue.

**So the aggregation is not routine.** But three things in the current wording are still
wrong, and two are the kind a fact-checker catches immediately.

### Three errors found, all now corrected in the manuscript

| Error | Correction |
|---|---|
| *"under 6% of revenue"* | **Wrong.** $4,006M / $65,179M = **6.15%** — *over* six. And if it was meant to describe insulin rather than the line, the FY2025 insulin figure **is not disclosed** and cannot be asserted |
| *"two GLP-1 products"* | **A pharmacology error, in a medical journal.** Mounjaro and Zepbound are two brands of **one molecule, tirzepatide**, a **dual GIP/GLP-1 receptor agonist**. Lilly's own 10-K says so |
| *"has stopped counting it"* | **An inference the record contradicts.** Lilly cut product detail across the entire portfolio in FY2025 — Cyramza, Olumiant, Emgality, Zyprexa and Baqsimi went too; the management discussion fell from 18 product lines to 4. Insulin was not singled out |

### The verified facts, which are stronger than the error was

| | |
|---|---|
| FY2024 | Humalog $2,324.8M + Humulin $917.1M + Basaglar $676.9M = **$3.92bn, 8.7% of revenue**, each a named line |
| FY2025 | No revenue figure anywhere in the filing. Absorbed into *"other cardiometabolic health"* **$4,006M, 6.15%**, Note 2 p.65 |
| XBRL | `HumalogMember`, `HumulinMember`, `BasaglarMember` present in the FY2024 taxonomy, **absent from FY2025** — machine-verifiable |
| Tirzepatide | Mounjaro $22,965M + Zepbound $13,542M = **56.01%**, Lilly's own stated figure |
| Reconciliation | Insulin was **87.9%** of the restated FY2024 bucket. The FY2025 share **cannot be assumed forward** |

### The reframe, now in the manuscript

The portfolio-wide finding does not weaken the argument — **it improves it.** Insulin's
disappearance is a by-product of a disclosure architecture reorganised around two growth
assets. That is a better and more defensible thesis than concealment:

> *No rule was broken. The company that commercialised insulin in 1923 simply no longer
> reports what it earns from it — not because insulin was singled out, but because a
> disclosure architecture reorganised around two growth assets swept it up with everything
> else that had stopped growing.*

Every number is from a filing, the pharmacology is correct, the threshold defence is
pre-empted in the text, and the final sentence makes the same point as "stopped counting it"
while being literally true.

**Keep the title.** With the body stating the qualifications, *"Other Cardiometabolic Health"*
reads as elegy, and a legal desk finds the text has already conceded everything it might
have raised.

**One item still open for the legal desk:** the pre-2020 text of Regulation S-K Item 101(c)
could not be retrieved from a primary source (eCFR and the Federal Register both refused
automated access). If the historical threshold point is used, source it to Release 33-10825,
85 FR 63726, 8 October 2020.

> **Deleted:** an earlier version of this section proposed conceding that the aggregation was
> *"consistent with normal practice"* and arguing immateriality instead. **Verification showed
> that concession would have been false** — the aggregation is not routine, as the Merck
> comparator demonstrates — and the draft wording repeated both the 6% and the GLP-1 errors.
> The accurate reframe is the one above and in the manuscript.
>
> Worth noting as a pattern: that block was written to satisfy a reviewer's objection *before*
> the objection was checked. It would have put a false concession into a paper about
> unverified claims.

---

## Part E — Pre-submission checklist

### Do this first — it may moot everything below

- [ ] **Send a pre-submission enquiry to BMJ** asking whether a manuscript reporting four
      experiments is eligible for Analysis, or should go to Research. BMJ invites these via a
      short form, answered by the Head of Scholarly Comment. **One email. Do it before any
      compression work.**

### Must do

- [x] ~~Confirm current BMJ Analysis specs~~ — **done, verified from the live page:
      2,000 words, 20 references, 3 non-text items, box/table words excluded**
- [x] ~~Verify the 10-K claim~~ — **done against primary EDGAR filings; three errors found
      and corrected**
- [ ] Cut body text to **≤2,000 words**
- [ ] Reduce to **3 non-text items**; move the rest to the repository supplement
- [ ] Add **Key messages box at the end, 3–4 points** (not five), with the B3 correction.
      Paste it into the abstract field at submission
- [ ] Write the **standfirst** — one italicised sentence carrying the central message
- [ ] Write **Contributors and sources**, 100–150 words, naming the **guarantor**
- [x] ~~Rewrite §4.4 per Part D~~ — **done**, with precise citation to Note 2 p.65 and
      accession 0000059478-26-000013
- [ ] Reformat references to **Vancouver, order of appearance**
- [ ] Add the **BMJ licence statement** in the exact wording the page specifies
- [ ] Add a **patient involvement** statement
- [ ] Download and work from BMJ's **Analysis article template**
- [ ] Note that peer review is **fully open** — the review history publishes alongside the
      article, which suits a paper whose argument is that corrections should be visible
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
