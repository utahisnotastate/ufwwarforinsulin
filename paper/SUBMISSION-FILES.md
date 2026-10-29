# What to upload, and under which designation

For the BMJ submission portal's **File Upload** step. Article type: **Original research**.

All files are in `paper/`. Upload in this order — the portal lists them to the editor in
upload order, and Main Document should be first.

| # | File | File Designation | Pages |
|---|---|---|---|
| 1 | `manuscript.docx` | **Main Document** | 49 |
| 2 | `supplementary.docx` | **Supplemental Material** | 47 |
| 3 | `statistical-analysis-plan.docx` | **SAP Plan** | 6 |
| 4 | `research-checklist.docx` | **Research Checklist** | 4 |
| 5 | `icmje-disclosure.docx` | **ICMJE Conflicts of Interest Form** † | 4 |

† **Read the note on the ICMJE form below before uploading item 5.**

The cover letter (`cover-letter.docx`) usually goes in a **text box** on an earlier screen,
not the file upload. Paste it there. Upload it as a file only if the portal has no box.

---

## The ICMJE form — the one thing you cannot generate here

**`icmje-disclosure.docx` is not the official ICMJE form.** The official form is produced by
the ICMJE's own online tool, which generates a PDF with your name on it. No one can make that
file for you; it has to come from the tool.

**Do this:**

1. Go to `icmje.org/disclosure-of-interest/`
2. Work through it using `icmje-disclosure.docx` as your answer key — it has every section
   written out, so you are transcribing rather than deciding
3. Download the PDF it generates
4. Upload **that PDF** under *ICMJE Conflicts of Interest Form*
5. Upload `icmje-disclosure.docx` as well, under *Supplemental Material for Editors only* —
   it explains the one declarable interest in plain prose, which a tick-box form cannot

**The answer that matters, and must not be left off:** you generated the document the paper
audits. It goes under "other relationships or activities," not under any financial heading.
It is already stated in the abstract, in §2.1, in §5.8 and in §7.2 of the manuscript, so a
form that omitted it would contradict the paper.

---

## Designations you do *not* need

| Designation | Why not |
|---|---|
| **Figure** | The paper has none. Everything is tabular, and the tables are inline in the Main Document where BMJ wants them |
| **Supplemental Material – video** | Nothing to show |
| **Main Document – marked copy** | Only for revisions. If they invite one, that is a tracked-changes copy against the version they reviewed |
| **Patient Consent Form** | No patients were involved, in any capacity. §7.5 and §7.6 say so explicitly |
| **PrePublication** | Only if they ask for prior-publication evidence. The medRxiv posting is declared in the cover letter |
| **Response to Reviewer Comments** | Only at revision |

---

## Before you click submit

- [ ] **Article type is Original research.** Not Analysis — BMJ states Analysis does not
      consider manuscripts containing primary research data, and this reports five
      experiments at ~11,000 words against a 2,000-word limit.
- [ ] **Decide the title.** `"Other Cardiometabolic Health"` reads as a Comment title and an
      editor may query it under Original research. The subtitle stands alone perfectly well.
      Submitting with the quoted title is defensible; dropping it costs nothing scientifically.
- [ ] **If review is blinded**, strip the author block — the first five lines of the Main
      Document — and replace the two repository URLs (in §7.9 Data availability and §2.1)
      with "[repository URL withheld for review]". Tell the editor in the cover letter that
      it is available to them. Everything else is already free of identifying detail.
- [ ] **Have the unredacted source document to hand.** The paper offers it to editors and
      reviewers on request, and its SHA-256 is published so the copy you supply can be
      verified. Expect to be asked.
- [ ] **Post to medRxiv** at submission, as the cover letter states.
- [ ] **Word count** — give the body count, ~11,000. It is long for BMJ Research. If they ask
      for cuts, the Limitations and Declarations hold the slack, not the Results.

---

## Rebuilding any of these

Source of truth is the matching `.md` in `paper/`. See [BUILD.md](BUILD.md).

```bash
python paper/md2json.py SUPPLEMENTARY-MATERIAL.md supplementary
cd paper/build && NODE_PATH="$(pwd)/node_modules" node ../json2docx.js supplementary --supplement
```

Drop `--supplement` for the Main Document; that flag switches off double spacing and line
numbers, which only the manuscript needs.

Every file above was checked three ways before being committed: schema validation, a word-count
and spot-check comparison against its markdown source, and rendering to PDF to be read. The
third is not optional — see BUILD.md for why.
