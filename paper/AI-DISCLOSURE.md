# Declaration of AI use

For the submission portal's question: *"Please provide details of any AI used in the
submission, such as what AI technology was used, the reason for its use, and what task it
performed."*

BMJ's policy asks authors to **name the tool, explain why it was used, and state what task it
performed**, to acknowledge it in the contributor section, to describe it more fully in the
methods where AI was used in the research itself, and — optionally — to supply a summary of
inputs, outputs and how the outputs were reviewed as supplementary material for the editor.
The statement below is built to that specification.

Answer **"Yes, I have used AI."**

---

## The full statement — paste this

**Yes. AI was used, in five distinct roles, and all five are declared here.** This submission
reports a study *of* AI-generated medical content, so artificial intelligence appears both as
the object of study and as a tool used to conduct the work and prepare the manuscript. Both
are declared, in full, below.

### 1. AI as the object of study

**Technology.** Google Gemini, accessed through the consumer product, running a
user-configured custom persona ("Custom Gem") named *Psycotronic Oracle 6*.

**Reason for use.** The study required a specimen of AI-generated medical text to audit at
claim level.

**Task performed.** It generated the entire document that this paper audits: a seven-turn
conversation of 20,089 words on insulin therapy, produced under a persona prompt instructing
it to retrieve medical knowledge from future timelines.

**A material fact, which I also declare as a competing interest: I wrote that persona prompt
and I generated the document myself**, in a private session on my own personal account. It
was never published, shared, posted, or shown to any patient. It is retained unaltered, and
its SHA-256 hash is published so that any copy I supply to editors or reviewers can be
verified as the one audited. This is stated in the abstract, in §2.1, in §5.8 and in §7.2 of
the manuscript, for two reasons: authoring the stimulus of a study is an interest in its
result, and it bounds the conclusion. The pattern I report may be a property of large
language models, or it may be a property of this prompt, and this design cannot distinguish
the two. I say so in the paper.

### 2. AI as experimental subject

**Technology.** Claude Opus 5 (Anthropic). One arm additionally pre-registered Claude
Sonnet 5.

**Reason for use.** Three of the five experiments ask what a current frontier model does when
given the same therapeutic questions under controlled conditions. The subject of such an
experiment is necessarily an AI system.

**Tasks performed.**

- **Neutral arm (§2.5).** Six probes — one mechanism question and one outcome question per
  therapeutic concept — each in fresh context, with no persona and **no tool use**, so that
  answers came from parametric knowledge only and matched the generation condition of the
  source document.
- **Persona arm (§2.5).** The identical questions, prefixed with a one-sentence speculative
  persona. Nought of six subjects adopted the persona, so the manipulation was never
  delivered. The arm is reported as uninformative rather than quietly dropped.
- **Positive controls (§3.7).** Seven matched concepts whose correct answer is affirmative,
  with the ground truth committed to version control *before* the probes were run, to test
  whether the models were simply answering "no" to everything.
- **A discarded arm (§2.6).** An earlier persona arm in which four of six subjects inferred
  the experimental hypothesis from passive context in their working environment. It was
  discarded for demand characteristics under a pre-registered decision rule, and the
  discarding is published rather than omitted.
- **An abandoned arm.** A sixth arm, pre-registering Claude Sonnet 5 as a cross-model rater,
  was **abandoned** when its isolation check failed. The abandonment and the unused input are
  both published.

### 3. AI as measurement instrument

**Technology.** Claude Opus 5, in independent, context-free sessions.

**Reason for use.** The classification and re-extraction steps had to be performed blind to
the verdicts. I could not perform them myself, having assigned those verdicts.

**Tasks performed.**

- **Blinded classification (§2.3).** Two independent sessions classified all 61 claims into
  four epistemic strata against a rubric fixed in advance, with no verdicts, no access to the
  audit, no searching, and no reading of other files. Cohen's κ is reported between them.
- **Independent blinded re-extraction (§3.8).** Two further independent sessions, blind to
  the inventory, the verdicts, the taxonomy and the hypothesis, re-extracted claims from the
  source document. **They returned 258 and 237 claims against my 61.** This result damages
  the paper and is reported in the abstract: my claim count does not reproduce, and every
  percentage in the paper is conditional on my segmentation.

**The limitation I state.** Every rater in every arm was a session of one model. Two samples
of one model share weights and therefore share systematic biases, so κ measures *stability of
classification under resampling*, not inter-rater reliability between independent judges. The
taxonomy has not been validated against human raters. This is §5.3, and it is restated
wherever κ appears.

### 4. AI as research assistant in verification

**Technology.** Claude Opus 5, with literature and web search.

**Reason for use.** Sixty-one claims spanning endocrinology, cell therapy, device
engineering, pharmacology and physics required a volume of source retrieval beyond what I
could perform unaided as an unfunded independent researcher.

**Task performed.** Three parallel AI-assisted literature review passes, conducted
independently and cross-checked against one another and against the primary sources. Sources
were PubMed, *Nature*, the *New England Journal of Medicine*, *The Lancet*,
ClinicalTrials.gov, UniProt, the United States Pharmacopeia, and SEC filings. Citations
verified against NCBI are marked separately in the deposited data from those reaching me
through secondary sources, and items that could not be resolved are listed rather than
omitted.

**The limitation I state.** The systems that assisted verification and the systems that
served as experimental subjects are frontier models of overlapping provenance, so a probe
that appears to "correct" the audit may be reproducing a shared prior rather than
contributing independent knowledge (§5.9). In one instance an unverified development-status
claim originating from a probe reached a manuscript draft before being caught; that
correction is logged publicly in §7.10.

### 5. AI in drafting the manuscript, the analysis code and this submission

**Technology.** Claude Opus 5 (Anthropic), used through Claude Code.

**Reason for use.** I am an independent researcher with no laboratory, no co-authors, no
statistical support and no institutional editorial assistance.

**Task performed.** Drafting and revising manuscript prose under my direction and to my
instructions; writing all five Python analysis scripts; writing the build pipelines that
generate the typeset PDF and the Word submission file; drafting the pre-registrations, the
supplementary material, the statistical analysis plan and the accompanying submission
documents; and conducting adversarial internal review of my own claims — one round of which
established that my headline statistic depended on a dichotomisation I had not disclosed, a
finding now reported in the abstract and led in the Limitations.

**This is trivially verifiable and I have made no attempt to obscure it.** Every commit in
the public repository cited in the manuscript carries a `Co-Authored-By: Claude` trailer, and
that repository is offered to editors and reviewers. I would rather declare it than leave it
to be discovered.

### What AI did not do

- **No AI system is an author**, consistent with ICMJE guidance and with BMJ policy. Only I
  am accountable for this work.
- No AI system decided what to conclude, which analysis to treat as primary, what to disclose
  as a limitation, or whether to publish. Those were my decisions and I am answerable for
  them.
- No AI-generated figure, image, diagram or data point appears in the paper. There are no
  figures. Every number is computed by a deposited script from deposited data and can be
  regenerated.
- No citation is included that was not resolved to a primary source; unresolved items are
  listed as unresolved.
- No dual-use content from the source document — specifically the device construction and
  firmware parameters it contains — was reproduced in any output, by me or by any AI system I
  used.

### Responsibility, and how to check it

I am the single author and the guarantor of this work. I accept full responsibility for all
of its content, **including the AI-assisted content** — for its accuracy, for proper
attribution of sources, and for its originality. Every statistic reported can be regenerated
by running the deposited scripts against the deposited data. The errors found during preparation are
logged publicly — eight in §7.10 of the manuscript, eleven entries in the repository's
corrections log, which also records process failures that never reached the paper. Two
materially weakened the result: a recoding that reduced the effect, and the discovery that the
dichotomous headline is not robust to the cut point.

I expect this manuscript to register on AI-detection screening. That would be a correct
result, not a false positive, and it is why this declaration is as detailed as it is.

### Material I can supply to editors

As your policy suggests, I can provide as supplementary material for editors: the verbatim
prompts given to every rater, subject and extractor; the complete unedited outputs of all
experimental arms; the pre-registrations with their version-control timestamps, which
establish that they preceded the runs; and the source document itself, in full and
unredacted, verifiable against its published hash.

---

## Short version, if the field has a character limit

> **Yes.** AI is both the object of study and a tool used throughout. **Google Gemini**, under
> a persona prompt I wrote, generated the 20,089-word document this paper audits — I generated
> it myself, and declare that as a competing interest. **Claude Opus 5** served in four further
> roles: as experimental subject in the re-query, persona and positive-control arms; as a blind
> measurement instrument for the classification of all 61 claims and for two independent
> re-extractions that returned 258 and 237 claims against my 61; as a research assistant for
> three cross-checked literature verification passes; and, through Claude Code, in drafting
> manuscript prose under my direction, writing the five analysis scripts and build pipelines,
> and conducting adversarial internal review. Every commit in the public repository records
> that AI co-authorship. **No AI system is an author.** I am the sole author and guarantor and
> accept full responsibility for all content, including AI-assisted content. Full detail is in
> §7.8 of the manuscript; prompts and raw outputs are available to editors on request.

---

## Keep these consistent

A declaration that contradicts the manuscript is worse than either document alone. These four
places must say the same thing, and currently do:

| Location | Content |
|---|---|
| This statement | The portal field |
| `MANUSCRIPT.md` §7.8 | Five roles, in a table |
| `MANUSCRIPT.md` §7.4 | Contributor-section acknowledgement, as BMJ asks |
| `COVER-LETTER.md` | The "Use of AI" paragraph |

If any of the five roles changes, change all four.
