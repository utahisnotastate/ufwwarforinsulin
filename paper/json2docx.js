/**
 * Build paper/build/manuscript.docx from paper/build/manuscript.json.
 *
 *   python paper/md2json.py
 *   cd paper/build && node ../json2docx.js
 *
 * Journal-submission conventions: US Letter, 1" margins, 12pt serif,
 * double-spaced body, continuous line numbers, page numbers in the footer.
 */
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, LevelFormat,
  HeadingLevel, Footer, PageNumber, LineNumberRestartFormat, convertInchesToTwip,
} = require('docx');

const BUILD = __dirname.endsWith('build') ? __dirname : path.join(__dirname, 'build');
// node json2docx.js [stem] [--supplement]
const STEM = (process.argv[2] && !process.argv[2].startsWith('--')) ? process.argv[2] : 'manuscript';
const SUPPLEMENT = process.argv.includes('--supplement');
const blocks = JSON.parse(fs.readFileSync(path.join(BUILD, STEM + '.json'), 'utf8'));

const FONT = 'Cambria';
const MONO = 'Consolas';
const BODY = 24;        // half-points => 12pt
const SMALL = 19;       // 9.5pt, for tables
const PAGE_W = 12240;   // US Letter, DXA
const MARGIN = convertInchesToTwip(1);
const TEXT_W = PAGE_W - 2 * MARGIN;

/** JSON runs -> TextRun[] */
function toRuns(rs, { size = BODY, bold = false } = {}) {
  if (!rs || !rs.length) return [new TextRun({ text: '', size, font: FONT })];
  return rs.map(r => new TextRun({
    text: r.t,
    bold: !!r.b || bold,
    italics: !!r.i,
    font: r.c ? MONO : FONT,
    size: r.c ? size - 3 : size,
    color: '000000',
  }));
}

const RULE = { style: BorderStyle.SINGLE, size: 6, color: '000000' };
const NONE = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };

/** Column widths from mean cell length, floored so nothing collapses. */
function columnWidths(raw) {
  const n = raw[0].length;
  const means = [];
  for (let j = 0; j < n; j++) {
    const lens = raw.map(r => (r[j] || '').length);
    means.push(Math.max(6, lens.reduce((a, b) => a + b, 0) / lens.length));
  }
  const total = means.reduce((a, b) => a + b, 0);
  let w = means.map(m => Math.round(TEXT_W * m / total));
  const floor = Math.round(TEXT_W * 0.09);
  w = w.map(x => Math.max(floor, x));
  const scale = TEXT_W / w.reduce((a, b) => a + b, 0);
  w = w.map(x => Math.round(x * scale));
  w[n - 1] += TEXT_W - w.reduce((a, b) => a + b, 0);   // absorb rounding
  return w;
}

function buildTable(b) {
  const widths = columnWidths(b.raw);
  const cell = (rs, { head = false, last = false, w = 0 } = {}) => new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: head ? { type: ShadingType.CLEAR, fill: 'EFEFEF' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    borders: {
      top: head ? RULE : NONE,
      bottom: head ? RULE : (last ? RULE : NONE),
      left: NONE, right: NONE,
    },
    children: [new Paragraph({
      spacing: { line: 240, before: 0, after: 0 },
      children: toRuns(rs, { size: SMALL, bold: head }),
    })],
  });

  const rows = [new TableRow({
    tableHeader: true,
    children: b.header.map((h, j) => cell(h, { head: true, w: widths[j] })),
  })];
  b.rows.forEach((r, idx) => {
    const padded = Array.from({ length: b.header.length }, (_, j) => r[j] || []);
    rows.push(new TableRow({
      children: padded.map((c, j) => cell(c, { last: idx === b.rows.length - 1, w: widths[j] })),
    }));
  });

  return new Table({ columnWidths: widths, width: { size: TEXT_W, type: WidthType.DXA }, rows });
}

const children = [];
for (const b of blocks) {
  switch (b.k) {
    case 'h': {
      if (b.level === 1) {
        children.push(new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 240, line: 240 },
          children: toRuns(b.runs, { size: 34, bold: true }),
        }));
      } else {
        children.push(new Paragraph({
          heading: b.level === 2 ? HeadingLevel.HEADING_1 : HeadingLevel.HEADING_2,
          spacing: { before: b.level === 2 ? 360 : 280, after: 140, line: 240 },
          keepNext: true,
          children: toRuns(b.runs, { size: b.level === 2 ? 28 : 25, bold: true }),
        }));
      }
      break;
    }
    case 'meta':
      children.push(new Paragraph({
        spacing: { before: 0, after: 60, line: 280 },
        children: toRuns(b.runs, { size: 22 }),
      }));
      break;
    case 'p':
      children.push(new Paragraph({
        spacing: { before: 0, after: 180, line: SUPPLEMENT ? 300 : 480 },
        children: toRuns(b.runs),
      }));
      break;
    case 'li':
      children.push(new Paragraph({
        numbering: { reference: b.kind === 'bullet' ? 'bullets' : 'numbers', level: 0 },
        spacing: { before: 0, after: 100, line: 360 },
        children: toRuns(b.runs),
      }));
      break;
    case 'quote':
      b.paras.forEach((p, k) => children.push(new Paragraph({
        indent: { left: convertInchesToTwip(0.4), right: convertInchesToTwip(0.25) },
        spacing: { before: k === 0 ? 160 : 0, after: 160, line: 360 },
        shading: { type: ShadingType.CLEAR, fill: 'F4F4F4' },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: '9A9A9A', space: 8 } },
        children: toRuns(p, { size: 22 }),
      })));
      break;
    case 'table':
      if (b.caption) {
        children.push(new Paragraph({
          spacing: { before: 220, after: 110, line: 280 },
          keepNext: true,
          children: toRuns(b.caption, { size: 22 }),
        }));
      }
      children.push(buildTable(b));
      children.push(new Paragraph({ spacing: { before: 0, after: 220 }, children: [new TextRun('')] }));
      break;
    case 'code':
      b.lines.forEach(ln => children.push(new Paragraph({
        spacing: { before: 0, after: 0, line: 200 },
        shading: { type: ShadingType.CLEAR, fill: 'F6F6F6' },
        indent: { left: convertInchesToTwip(0.15) },
        children: [new TextRun({
          text: ln.length ? ln : ' ',
          font: MONO, size: 15, color: '000000',
        })],
      })));
      children.push(new Paragraph({ spacing: { before: 0, after: 160 }, children: [new TextRun('')] }));
      break;
    case 'rule':
      children.push(new Paragraph({
        spacing: { before: 120, after: 200 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'B0B0B0', space: 6 } },
        children: [new TextRun('')],
      }));
      break;
  }
}

const doc = new Document({
  creator: 'Utah Hans',
  title: 'Mechanism without outcome',
  description: 'A claim-level audit of AI-generated insulin misinformation',
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: '•',
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: convertInchesToTwip(0.4), hanging: convertInchesToTwip(0.22) } } },
        }],
      },
      {
        reference: 'numbers',
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: '%1.',
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: convertInchesToTwip(0.4), hanging: convertInchesToTwip(0.22) } } },
        }],
      },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: 15840 },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
      },
      ...(SUPPLEMENT ? {} : {
        lineNumbers: { countBy: 1, restart: LineNumberRestartFormat.CONTINUOUS, distance: 360 },
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], size: 20, font: FONT })],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  const out = path.join(BUILD, STEM + '.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, (buf.length / 1024).toFixed(0) + ' KB');
  console.log('blocks rendered:', children.length);
});
