# -*- coding: utf-8 -*-
"""Parse MANUSCRIPT.md into a structured JSON block list for the .docx builder.

Splits the markdown into typed blocks (heading / para / table / quote / list / rule)
and resolves inline emphasis and code into runs, so the Node side only has to lay
out what it is given.

    python paper/md2json.py        ->  paper/build/manuscript.json
"""
import io, re, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'MANUSCRIPT.md')
OUT = os.path.join(HERE, 'build', 'manuscript.json')


def runs(text):
    """Inline markdown -> list of {t, b, i, c} runs (bold / italic / code)."""
    out, i = [], 0
    pat = re.compile(r'(\*\*.+?\*\*|(?<![\w*])\*[^*\n]+?\*(?![\w*])|`[^`]+`|\[[^\]]+\]\([^)]*\))')
    for m in pat.finditer(text):
        if m.start() > i:
            out.append({'t': text[i:m.start()]})
        s = m.group(0)
        if s.startswith('**'):
            out.append({'t': s[2:-2], 'b': True})
        elif s.startswith('`'):
            out.append({'t': s[1:-1], 'c': True})
        elif s.startswith('['):
            label = re.match(r'\[([^\]]+)\]', s).group(1)
            out.extend(runs(label))
        else:
            out.append({'t': s[1:-1], 'i': True})
        i = m.end()
    if i < len(text):
        out.append({'t': text[i:]})
    return [r for r in out if r.get('t')]


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in line.split('|')]


def parse(md):
    lines = md.split('\n')
    blocks = []

    # Front matter: everything before the first horizontal rule keeps its own
    # line breaks, except where an emphasis span is still open across lines.
    first_rule = next((k for k, l in enumerate(lines)
                       if set(l.rstrip()) == {'-'} and len(l.rstrip()) >= 3), None)
    start = 0
    if first_rule is not None and first_rule < 30:
        groups, cur = [], []
        for l in lines[:first_rule]:
            l = l.rstrip()
            if not l.strip():
                continue
            m = re.match(r'^(#{1,6})\s+(.*)$', l)
            if m:
                if cur:
                    groups.append(cur); cur = []
                blocks.append({'k': 'h', 'level': len(m.group(1)),
                               'runs': runs(m.group(2))})
                continue
            cur.append(l)
            if ' '.join(cur).count('*') % 2 == 0:
                groups.append(cur); cur = []
        if cur:
            groups.append(cur)
        for g in groups:
            blocks.append({'k': 'meta', 'runs': runs(' '.join(g))})
        blocks.append({'k': 'rule'})
        start = first_rule + 1
        lines = lines[start:]

    para, qbuf, item = [], [], []
    list_kind = None
    pending_caption = None
    i = 0

    def flush_para():
        nonlocal pending_caption
        if para:
            joined = ' '.join(x.strip() for x in para)
            para.clear()
            if re.match(r'^\*\*Table\s', joined):
                pending_caption = joined
                return
            blocks.append({'k': 'p', 'runs': runs(joined)})

    def flush_item():
        if item:
            blocks.append({'k': 'li', 'kind': list_kind,
                           'runs': runs(' '.join(x.strip() for x in item))})
            item.clear()

    def flush_list():
        nonlocal list_kind
        flush_item()
        list_kind = None

    def flush_quote():
        if qbuf:
            chunks, cur = [], []
            for q in qbuf:
                if q.strip():
                    cur.append(q.strip())
                elif cur:
                    chunks.append(' '.join(cur)); cur = []
            if cur:
                chunks.append(' '.join(cur))
            if chunks:
                blocks.append({'k': 'quote',
                               'paras': [runs(c) for c in chunks]})
            qbuf.clear()

    while i < len(lines):
        t = lines[i].rstrip()

        if t.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|?\s*$', lines[i + 1]):
            flush_para(); flush_list(); flush_quote()
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(split_row(lines[i]))
                i += 1
            del rows[1]
            blocks.append({
                'k': 'table',
                'caption': runs(pending_caption) if pending_caption else None,
                'header': [runs(c) for c in rows[0]],
                'rows': [[runs(c) for c in r] for r in rows[1:]],
                'raw': rows,
            })
            pending_caption = None
            continue

        m = re.match(r'^(#{1,6})\s+(.*)$', t)
        if m:
            flush_para(); flush_list(); flush_quote()
            blocks.append({'k': 'h', 'level': len(m.group(1)), 'runs': runs(m.group(2))})
            i += 1
            continue

        if set(t) == {'-'} and len(t) >= 3:
            flush_para(); flush_list(); flush_quote()
            blocks.append({'k': 'rule'})
            i += 1
            continue

        if t.startswith('>'):
            flush_para(); flush_list()
            qbuf.append(t[1:])
            i += 1
            continue
        elif qbuf:
            flush_quote()

        mb = re.match(r'^(\s*)[-*]\s+(.*)$', t)
        mn = re.match(r'^(\s*)\d+\.\s+(.*)$', t)
        if mb or mn:
            flush_para()
            kind = 'bullet' if mb else 'number'
            if list_kind and list_kind != kind:
                flush_list()
            flush_item()
            list_kind = kind
            item.append((mb or mn).group(2))
            i += 1
            continue

        if not t.strip():
            if list_kind:
                flush_list()
            else:
                flush_para()
            i += 1
            continue

        if list_kind:
            item.append(t.strip())
        else:
            para.append(t)
        i += 1

    flush_para(); flush_list(); flush_quote()
    return blocks


def main():
    md = io.open(SRC, encoding='utf-8').read()
    blocks = parse(md)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(
        json.dumps(blocks, ensure_ascii=False, indent=1))
    from collections import Counter
    c = Counter(b['k'] for b in blocks)
    print('wrote', OUT)
    print('blocks:', dict(c))
    print('tables with captions:',
          sum(1 for b in blocks if b['k'] == 'table' and b['caption']))


main()
