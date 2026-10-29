# -*- coding: utf-8 -*-
"""Build paper/manuscript.pdf from paper/MANUSCRIPT.md.

Requires XeLaTeX (MiKTeX or TeX Live). Run from anywhere:

    python paper/build-pdf.py
    cd paper/build && xelatex manuscript.tex && xelatex manuscript.tex

Two passes are needed for longtable column widths to settle.

Every non-ASCII character in the manuscript is mapped to a LaTeX command, so
the output has no font dependencies beyond Latin Modern.
"""
import io, re, sys, os

SRC = r'C:\code\ufwwarforinsulin\paper\MANUSCRIPT.md'
OUT = r'C:\code\ufwwarforinsulin\paper\build\manuscript.tex'

SUP = {'\u207b': '-', '\u2070': '0', '\u00b9': '1', '\u00b2': '2', '\u00b3': '3',
       '\u2074': '4', '\u2075': '5', '\u2076': '6', '\u2077': '7', '\u2078': '8',
       '\u2079': '9'}
SUB = {'\u2080': '0', '\u2081': '1', '\u2082': '2', '\u2083': '3', '\u2084': '4',
       '\u2085': '5', '\u2086': '6', '\u2087': '7', '\u2088': '8', '\u2089': '9'}
CHAR = {
    '\u2014': '---', '\u2013': '--', '\u00a7': '\\S{}', '\u00d7': '$\\times$',
    '\u00b1': '$\\pm$', '\u2248': '$\\approx$', '\u2265': '$\\geq$',
    '\u2264': '$\\leq$', '\u2212': '$-$', '\u00b7': '$\\cdot$',
    '\u00f6': '\\"o', '\u00e9': "\\'e", '\u00e8': '\\`e',
    '\u03ba': '$\\kappa$', '\u03b1': '$\\alpha$', '\u03b2': '$\\beta$',
    '\u03b8': '$\\theta$', '\u03b5': '$\\varepsilon$', '\u0394': '$\\Delta$',
    '\u03a6': '$\\Phi$', '\u2207': '$\\nabla$', '\u03bc': '$\\mu$',
    '\u2003': '\\quad{}', '\u2002': '\\,', '\u00a0': '~',
    '\u2019': "'", '\u2018': "`", '\u201c': '``', '\u201d': "''",
    '\u2026': '\\ldots{}', '\u2192': '$\\rightarrow$', '\u226a': '$\\ll$',
}
ESC = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
       '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
       '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}


def inline(t):
    """Markdown inline -> LaTeX, for one run of text."""
    # protect code spans
    codes = []
    def grab(m):
        codes.append(m.group(1))
        return '\x00%d\x00' % (len(codes) - 1)
    t = re.sub(r'`([^`]+)`', grab, t)

    t = ''.join(ESC.get(c, c) for c in t)

    # ASCII double quotes -> directional LaTeX quotes
    parts = t.split('"')
    if len(parts) > 1:
        t = parts[0]
        for k, seg in enumerate(parts[1:]):
            t += ('``' if k % 2 == 0 else "''") + seg


    # unicode super/subscript runs
    t = re.sub('[' + ''.join(SUP) + ']+',
               lambda m: '$^{' + ''.join(SUP[c] for c in m.group(0)) + '}$', t)
    t = re.sub('[' + ''.join(SUB) + ']+',
               lambda m: '$_{' + ''.join(SUB[c] for c in m.group(0)) + '}$', t)
    t = ''.join(CHAR.get(c, c) for c in t)

    # emphasis
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])', r'\\emph{\1}', t)
    # markdown links -> text only (all are repo-relative)
    t = re.sub(r'\[([^\]]+)\]\((?!\d)[^)]*\)', r'\1', t)

    for i, c in enumerate(codes):
        c = ''.join(ESC.get(ch, ch) for ch in c)
        c = ''.join(CHAR.get(ch, ch) for ch in c)
        t = t.replace('\x00%d\x00' % i, r'\texttt{\small %s}' % c)

    # strip any leftover stray non-ascii
    t = ''.join(ch if ord(ch) < 127 else '' for ch in t)
    return t


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


def emit_table(rows, out, caption=None):
    header, body = rows[0], rows[2:]
    n = len(header)
    # proportional widths from mean cell length, floored so nothing collapses
    CH = 0.0455          # approx width of one footnotesize char, inches
    lens, mins = [], []
    for j in range(n):
        cells = [r[j] for r in [header] + body if j < len(r)]
        vals = [len(c) for c in cells]
        lens.append(max(6, sum(vals) / max(1, len(vals))))
        # longest single token decides the minimum this column can be
        longest = 0
        for c in cells:
            for w in re.split(r'[\s/]+', re.sub(r'[*`]', '', c)):
                longest = max(longest, len(w))
        mins.append(min(1.9, max(0.40, (longest + 1) * CH)))

    usable = 6.25 - 0.14 * n
    tot = sum(lens)
    widths = [usable * l / tot for l in lens]

    # raise any column below its minimum, taking the space from columns with slack
    for _ in range(12):
        deficit = sum(max(0.0, mins[j] - widths[j]) for j in range(n))
        if deficit < 1e-4:
            break
        slack = [max(0.0, widths[j] - mins[j]) for j in range(n)]
        tot_slack = sum(slack)
        if tot_slack < 1e-6:
            break
        for j in range(n):
            if widths[j] < mins[j]:
                widths[j] = mins[j]
            else:
                widths[j] -= deficit * slack[j] / tot_slack
    sc = usable / sum(widths)
    widths = [w * sc for w in widths]

    spec = ''.join(r'>{\RaggedRight\arraybackslash}p{%.2fin}' % w for w in widths)
    # estimate height: header + one line per row, plus wrapping allowance
    est = 3
    for r in body:
        longest = max((len(c) for c in r), default=0)
        est += max(1, int(longest / 70) + 1)
    if est <= 12:
        out.append(r'\needspace{%d\baselineskip}' % (est + 2))
    out.append(r'{\footnotesize\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.25}')
    out.append(r'\begin{longtable}{@{}%s@{}}' % spec)
    if caption:
        out.append(r'\caption*{\normalsize\raggedright %s}\\[2pt]' % caption)
    out.append(r'\toprule')
    out.append(' & '.join(r'\textbf{%s}' % inline(h) for h in header) + r' \\')
    out.append(r'\midrule\endfirsthead')
    out.append(r'\toprule')
    out.append(' & '.join(r'\textbf{%s}' % inline(h) for h in header) + r' \\')
    out.append(r'\midrule\endhead')
    out.append(r'\bottomrule\endfoot')
    for r in body:
        cells = (r + [''] * n)[:n]
        out.append(' & '.join(inline(c) for c in cells) + r' \\')
    out.append(r'\end{longtable}}')
    out.append('')


def convert(md):
    lines = md.split('\n')
    out = []

    # --- title block: everything before the first horizontal rule ---
    first_rule = next((k for k, l in enumerate(lines)
                       if set(l.rstrip()) == {'-'} and len(l.rstrip()) >= 3), None)
    start = 0
    if first_rule is not None and first_rule < 30:
        fm = [l.rstrip() for l in lines[:first_rule]]
        title = sub = None
        meta = []
        for l in fm:
            if l.startswith('# '):
                title = inline(l[2:].strip())
            elif l.startswith('## '):
                sub = inline(l[3:].strip())
            elif l.strip():
                meta.append(l.strip())
        out.append(r'\begin{titlepage}\thispagestyle{empty}')
        out.append(r'\vspace*{1.2in}')
        out.append(r'\begin{center}')
        if title:
            out.append(r'{\LARGE\bfseries %s}\par\vspace{14pt}' % title)
        if sub:
            out.append(r'{\large %s}\par\vspace{26pt}' % sub)
        out.append(r'\end{center}')
        groups, cur = [], []
        for m in meta:
            if not m:
                continue
            cur.append(m)
            # a group closes once its emphasis markers balance
            if ' '.join(cur).count('*') % 2 == 0:
                groups.append(cur)
                cur = []
        if cur:
            groups.append(cur)
        buf = [inline(' '.join(g)) for g in groups]
        out.append(r'\begin{center}\begin{minipage}{0.84\textwidth}')
        out.append((r'\\' + '\n').join(buf))
        out.append(r'\end{minipage}\end{center}')
        out.append(r'\vfill\end{titlepage}')
        out.append('')
        start = first_rule + 1

    i = start
    in_quote = False
    list_stack = []
    para = []          # buffered plain-paragraph lines
    pending = {'cap': None}   # a table caption waiting for its table
    qbuf = []          # buffered blockquote lines
    item = []          # buffered current list-item lines

    def flush_para():
        if para:
            joined = ' '.join(x.strip() for x in para)
            if re.match(r'^\*\*Table\s', joined):
                pending['cap'] = inline(joined)
                para.clear()
                return
            out.append(inline(joined))
            out.append('')
            para.clear()

    def flush_item():
        if item:
            out.append(r'\item %s' % inline(' '.join(x.strip() for x in item)))
            item.clear()

    def flush_quote():
        nonlocal in_quote
        if qbuf:
            chunks, cur = [], []
            for q in qbuf:
                if q.strip():
                    cur.append(q.strip())
                else:
                    if cur:
                        chunks.append(' '.join(cur)); cur = []
            if cur:
                chunks.append(' '.join(cur))
            if chunks:
                if not in_quote:
                    out.append(r'\begin{mdquote}')
                    in_quote = True
                for c in chunks:
                    out.append(inline(c))
                    out.append('')
            qbuf.clear()
        if in_quote:
            out.append(r'\end{mdquote}')
            out.append('')
            in_quote = False

    def close_lists():
        flush_item()
        while list_stack:
            out.append(r'\end{%s}' % list_stack.pop())
            out.append('')

    while i < len(lines):
        t = lines[i].rstrip()

        # ---- table
        if t.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|?\s*$', lines[i + 1]):
            flush_para(); close_lists(); flush_quote()
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(split_row(lines[i]))
                i += 1
            emit_table(rows, out, pending['cap'])
            pending['cap'] = None
            continue

        # ---- heading
        m = re.match(r'^(#{1,6})\s+(.*)$', t)
        if m:
            flush_para(); close_lists(); flush_quote()
            lvl, txt = len(m.group(1)), inline(m.group(2))
            if lvl == 1:
                out.append(r'\TitleLine{%s}' % txt)
            elif lvl == 2:
                out.append(r'\section*{%s}' % txt)
            elif lvl == 3:
                out.append(r'\subsection*{%s}' % txt)
            else:
                out.append(r'\subsubsection*{%s}' % txt)
            out.append(r'\nopagebreak')
            out.append('')
            i += 1
            continue

        # ---- horizontal rule
        if set(t) == {'-'} and len(t) >= 3:
            flush_para(); close_lists(); flush_quote()
            out.append(r'\medskip\hrule\medskip')
            out.append('')
            i += 1
            continue

        # ---- blockquote
        if t.startswith('>'):
            flush_para(); close_lists()
            qbuf.append(t[1:])
            i += 1
            continue
        elif qbuf or in_quote:
            flush_quote()

        # ---- list item
        mb = re.match(r'^(\s*)[-*]\s+(.*)$', t)
        mn = re.match(r'^(\s*)\d+\.\s+(.*)$', t)
        if mb or mn:
            flush_para()
            kind = 'itemize' if mb else 'enumerate'
            flush_item()
            if not list_stack:
                out.append(r'\begin{%s}' % kind)
                list_stack.append(kind)
            elif list_stack[-1] != kind:
                out.append(r'\end{%s}' % list_stack.pop())
                out.append(r'\begin{%s}' % kind)
                list_stack.append(kind)
            item.append((mb or mn).group(2))
            i += 1
            continue

        # ---- blank
        if not t.strip():
            if list_stack:
                close_lists()
            else:
                flush_para()
            i += 1
            continue

        # ---- continuation
        if list_stack:
            item.append(t.strip())
        else:
            para.append(t)
        i += 1

    flush_para(); close_lists(); flush_quote()
    return '\n'.join(out)


PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setmonofont{Latin Modern Mono}[Scale=0.88]
\usepackage[a4paper,top=1in,bottom=1in,left=1.1in,right=1.1in]{geometry}
\usepackage{longtable,booktabs,array}
\usepackage{needspace}
\usepackage{ragged2e}
\usepackage[labelformat=empty,skip=4pt]{caption}
\usepackage{microtype}
\usepackage{enumitem}
\setlist{itemsep=1pt,topsep=4pt,parsep=0pt}
\usepackage{titlesec}
\titleformat{\section}{\normalfont\large\bfseries}{}{0pt}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries}{}{0pt}{}
\titlespacing*{\section}{0pt}{16pt}{6pt}
\titlespacing*{\subsection}{0pt}{12pt}{4pt}
\usepackage{xcolor}
\definecolor{qbg}{gray}{0.955}
\definecolor{qrule}{gray}{0.62}
\usepackage{mdframed}
\newmdenv[backgroundcolor=qbg,linecolor=qrule,linewidth=0.8pt,
          leftline=true,rightline=false,topline=false,bottomline=false,
          innerleftmargin=9pt,innerrightmargin=9pt,innertopmargin=7pt,
          innerbottommargin=7pt,skipabove=8pt,skipbelow=8pt]{mdquote}
\usepackage{fancyhdr}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\footnotesize\itshape Mechanism without outcome}
\fancyhead[R]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\usepackage[hidelinks]{hyperref}
\newcommand{\TitleLine}[1]{%
  \begin{center}\LARGE\bfseries #1\end{center}\vspace{2pt}}
\emergencystretch=3em

\raggedbottom
\begin{document}
"""


def main():
    md = io.open(SRC, encoding='utf-8').read()
    body = convert(md)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(
        PREAMBLE + body + '\n\\end{document}\n')
    print('wrote', OUT)
    print('tex lines:', body.count('\n') + 1)


main()
