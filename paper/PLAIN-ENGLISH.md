# The paper, in plain English

*No jargon. If you only read one file here, read this one.*

**The paper itself:** [manuscript.pdf](manuscript.pdf) · 27 pages
**Want to help?** Skip to [how to give feedback](#how-to-give-feedback) at the bottom. You do
not need a medical degree to be useful.

---

## The story

Someone asked a chatbot to pretend it could see the future, and asked it about insulin. It
wrote sixty pages. Confident, technical, full of real scientists' names and real molecule
numbers.

It also told readers they could stop taking insulin and use a radio device instead. **That
would kill a person with type 1 diabetes in about two days.**

So every claim in it was checked against the actual medical literature. Not skimmed —
checked, one at a time, against the published trials.

## What came back

It wasn't just wrong. It was wrong **in a pattern**, and the pattern is the whole point.

Imagine a kid who has memorised how a car engine works — pistons, spark plugs, fuel
injection, all correct — and then tells you confidently that you can run the car on orange
juice.

| What the document was talking about | How it did |
|---|---|
| **How a biological thing works** | Often right |
| **Whether a treatment helps a person** | Wrong **every single time** — 0 out of 8 |
| **Any specific number** | Wrong **every single time** — 0 out of 9 |

That split is the finding. Not "AI says false things," which everyone knows. It's that the
falseness lives in a *predictable place*: at the exact moment a claim stops describing nature
and starts promising a result.

**And here is the part that makes it useful rather than merely interesting.** Every one of
those false promises matched a real drug programme that had **already been tried and had
already failed**. The document wasn't inventing fantasies. It was quietly reporting failures
as successes.

## Why a doctor should care

A patient walks in with this printout. The instinct is to say "that's nonsense, throw it
away."

That is the wrong move, and the paper shows why. **They are probably right about the
biology.** Dismiss the whole thing and you have told the patient you didn't read it — and
you have handed the document more credibility than it had earned.

What deserves attacking is the narrow part that is actually wrong: *does this treatment
work in people?*

There is also a time problem that makes this disease specific. With most health
misinformation you have months or years to correct course. **Stop taking insulin and you are
in an emergency room within 12 to 48 hours.** There is no slow version of this mistake.

## What is actually good about the paper

Honestly? Not the finding. The finding is interesting, but it is one document.

What is good is that **the paper keeps attacking itself, and reports it when the attack
lands.**

- There was an explanation for the pattern. It was tested. **It was wrong.** That is in the
  paper.
- Raters classified the claims blind. The blinding **made the result weaker**. In the paper.
- One experiment got contaminated — the test subjects worked out what was being tested. It
  was **thrown away**, and the reason published so other researchers avoid it.
- A reviewer found the headline number depended on a definition that had never been written
  down. Remove it and the result **stops being statistically significant**. That is now in
  the abstract, in bold.
- Two outsiders re-read the source document and found **four times as many claims**. So the
  counts don't reproduce — also in the abstract.
- A fourth experiment was designed, registered, and then **abandoned** because it couldn't be
  run cleanly. The abandonment is published.
- There is a public corrections file listing **eleven mistakes**, including one where this
  project under-reported a death count from a clinical trial.

Most papers hide this. The argument here is that a paper about checking claims has no
business hiding the times its own claims didn't check out.

## What is weak, plainly

Anyone sharing this should be able to state the weaknesses as fluently as the strengths.

- **One document, and the author wrote it.** It might be a fact about AI, or just a fact
  about that one prompt. This study cannot tell you which.
- **No human ever checked the categories.** Every helper was a machine. Machines agreeing
  with machines is not independence.
- **13 test questions is a small sample.** Roughly one answer in four could be wrong and it
  wouldn't have shown up.
- **The number of claims isn't stable**, so every percentage is really "according to how this
  one person chopped it up."
- **No patient and no clinician was ever involved.** The advice about consultations has never
  been tried in a consultation.

## About the title

*"Other Cardiometabolic Health."*

That is the exact line in Eli Lilly's 2025 financial filing where insulin's revenue went. The
year before, it was three named products you could look up. Now it is a bucket with no label
on it.

Nothing illegal happened, and the paper says so clearly — the change swept up several
products, not just insulin. But the company that gave the world insulin in 1923 no longer
tells you what it earns from it, and the paper's quiet point is that when institutions stop
saying things clearly, something else fills the silence.

---

## How to give feedback

**You do not need to be a scientist.** The most useful feedback so far has come from people
attacking one specific thing rather than reacting to the whole.

Open an [issue](https://github.com/utahisnotastate/ufwwarforinsulin/issues) and pick whichever
of these you can actually speak to:

**If you have diabetes, or care for someone who does**
- Would the advice in §4.3 land well if a doctor said it to you? Or would it feel
  patronising?
- Is there something obviously missing about what it's like to be handed material like this?

**If you are a clinician**
- Is the "they're right about the mechanism, wrong about the outcome" framing usable in a real
  consultation, or is it too clever for a fifteen-minute appointment?
- Table 3 lists the trial evidence against each false claim. Is any of it mischaracterised?

**If you do statistics**
- The primary analysis is an ordinal permutation test, chosen because the simpler version
  wasn't robust to where you draw the line. Is that the right call, or a dodge?
- Everything is reproducible: `analysis-sensitivity.py` and friends.

**If you work on AI evaluation**
- §4.5 argues you must verify a test subject's isolation *from inside its own context*, every
  single time. This was learned the hard way, three times. Does it match your experience?

**If you just think something smells wrong**
- Say which sentence and why. That is genuinely the most valuable kind of issue.

**The one thing that would help most**, if anyone has the time: nobody has audited the
[258-claim](data-extraction-1.md) or [237-claim](data-extraction-2.md) independent
extractions. Both are published. Checking even a slice of one against the literature would
test this paper harder than anything in it.

Corrections are logged publicly with the original wording kept, including the embarrassing
ones. A correction that moves a verdict is the most useful thing anyone can contribute.
