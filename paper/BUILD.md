# Building the manuscript

`MANUSCRIPT.md` is the source of truth. Both output formats are generated from it, and both
are committed so you don't have to build anything to read them.

| Output | File | Use |
|---|---|---|
| **PDF** | [manuscript.pdf](manuscript.pdf) | Reading, preprint, medRxiv. 27 pages, single-spaced, typeset |
| **Word** | [manuscript.docx](manuscript.docx) | **Journal submission.** 49 pages, double-spaced, continuous line numbers |

Most journals — BMJ and JMIR included — want the Word file with line numbers so reviewers can
cite "line 284." That is what `manuscript.docx` is for.

## Rebuilding

### Word (.docx)

Needs Node. The `docx` library installs into `build/`, which is gitignored.

```bash
python paper/md2json.py                 # MANUSCRIPT.md -> build/manuscript.json
cd paper/build
npm install docx                        # first time only
NODE_PATH="$(pwd)/node_modules" node ../json2docx.js
```

Two stages on purpose: [`md2json.py`](md2json.py) does the markdown parsing, so the block
structure is testable on its own, and [`json2docx.js`](json2docx.js) only lays out what it is
handed.

### PDF

Needs XeLaTeX (MiKTeX or TeX Live).

```bash
python paper/build-pdf.py               # MANUSCRIPT.md -> build/manuscript.tex
cd paper/build
xelatex manuscript.tex && xelatex manuscript.tex
```

Two passes, so longtable column widths settle.

## Verifying output

The `.docx` was checked three ways, and anyone changing the build should repeat all three:

1. **Schema validation** — the `docx` skill's `scripts/office/validate.py`. Currently passes
   with no errors.
2. **Content integrity** — extract every `<w:t>` from `word/document.xml` and compare the word
   count against the markdown. Currently 12,607 vs 12,563, a ratio of 1.004; the small excess
   is table-cell boundaries becoming spaces. Also spot-check distinctive strings that are easy
   to mangle: `κ = 0.928`, `Plum-Mörschel`, `NCT04606576`, the SHA-256 prefix.
3. **Look at it.** Render to PDF and read the pages. Without LibreOffice you can drive Word
   read-only through COM (`pywin32`), which is how the committed version was checked.

The third one is not optional. The PDF build was clean on every automated check while still
containing a duplicated sentence in the abstract — a defect that only became visible once the
text was set in type.

## Known formatting notes

- Superscripts and subscripts are real Unicode in the `.docx` (10⁻⁴) and converted to LaTeX
  math in the PDF. Both render correctly; they are not the same mechanism.
- The PDF maps all 26 distinct non-ASCII characters to LaTeX commands, so it has no font
  dependency beyond Latin Modern. The `.docx` keeps Unicode and relies on Cambria.
- Tables set their own column widths from mean cell length, floored so no column collapses.
  If you add a table with one very long unbroken token, check that column.
