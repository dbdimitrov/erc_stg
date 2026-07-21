#!/usr/bin/env python3
"""PDF -> clean Markdown with inline full-page figure renders.
- text via pymupdf4llm (ignore_images: no fragment junk)
- reporting-summary pages excluded
- References/Bibliography sections dropped
- figure-caption pages rendered full-page via pdftoppm and embedded inline
"""
import sys, os, re, subprocess, pathlib
import fitz  # PyMuPDF
import pymupdf4llm

BASE = pathlib.Path("/Users/b260-admin/Repos/erc_stg/my_manuscripts")
MD_DIR = BASE / "markdown"
FIG_DIR = MD_DIR / "figures"

# Figure caption at line start: "Fig. 1 |", "Fig. 1 LIANA", "Figure 1. ...", "Fig 1.  ..."
# Requires a separator OR whitespace-then-capital/paren after the number, so that
# inline references ("Fig. 1a shows", "see Fig. 2 for") do not match.
FIG_CAPTION = re.compile(
    r'(?m)^\s*(?i:fig(?:ure)?)\.?\s*\d+\s*(?:[|:.–—-]|[\s  ]+[A-Z(])')
REPORTING = re.compile(r'nature portfolio wishes to improve|life sciences reporting summary|^\s*reporting summary\s*$', re.I | re.M)
DROP_HEADING = re.compile(r'^\s*(references|bibliography|reporting summary)\s*$', re.I)

def clean_heading(line):
    # strip markdown heading markers and emphasis/formatting to test heading name
    t = re.sub(r'^#+\s*', '', line)
    t = re.sub(r'[*_~`<>]|</?u>|</?b>|</?i>', '', t)
    return t.strip()

def drop_reference_sections(md):
    """Remove sections whose heading is References/Bibliography/Reporting summary,
    up to the next heading of same-or-higher level."""
    lines = md.splitlines()
    out = []
    i = 0
    skipping = False
    skip_level = 0
    for line in lines:
        m = re.match(r'^(#+)\s', line)
        if m:
            level = len(m.group(1))
            name = clean_heading(line)
            if DROP_HEADING.match(name):
                skipping = True
                skip_level = level
                continue
            elif skipping and level <= skip_level:
                skipping = False
        if not skipping:
            out.append(line)
    return "\n".join(out)

def convert(pdf_id, name):
    pdf = BASE / "pdfs" / f"{pdf_id}.pdf"
    doc = fitz.open(pdf)
    npages = doc.page_count
    page_txt = [doc.load_page(p).get_text() for p in range(npages)]
    # reporting-summary boundary: first page whose text carries the form signature
    content_end = npages
    for pno in range(npages):
        if REPORTING.search(page_txt[pno]):
            content_end = pno
            break
    # keep pages before the form that actually have a text layer (>=40 chars);
    # skipping near-empty/image-only pages also prevents slow Tesseract OCR.
    content_pages = [p for p in range(content_end) if len(page_txt[p].strip()) >= 40]
    # figure-bearing pages among content pages
    fig_pages = [p for p in content_pages if FIG_CAPTION.search(doc.load_page(p).get_text())]

    figdir = FIG_DIR / name
    figdir.mkdir(parents=True, exist_ok=True)
    # render figure pages full-page via pdftoppm (1-based page numbers)
    rendered = {}
    for p in fig_pages:
        pg = p + 1
        prefix = str(figdir / f"page")
        subprocess.run(["pdftoppm", "-f", str(pg), "-l", str(pg), "-r", "150",
                        "-png", str(pdf), prefix + f"-{pg:03d}"],
                       check=True, capture_output=True)
        # pdftoppm appends page number; find the produced file
        produced = sorted(figdir.glob(f"page-{pg:03d}*.png"))
        if produced:
            rendered[p] = produced[-1].name

    # per-page markdown
    chunks = pymupdf4llm.to_markdown(str(pdf), pages=content_pages,
                                     ignore_images=True, page_chunks=True,
                                     show_progress=False)
    parts = []
    for idx, ch in enumerate(chunks):
        pno = content_pages[idx]  # chunks returned in the order of `pages`
        parts.append(ch["text"])
        if pno in rendered:
            cap = ""
            m = FIG_CAPTION.search(doc.load_page(pno).get_text())
            if m:
                # grab the caption line
                line = doc.load_page(pno).get_text().splitlines()
                capline = next((l for l in line if FIG_CAPTION.match(l)), "Figure")
                cap = capline.strip()[:120]
            parts.append(f"\n\n![{cap}](figures/{name}/{rendered[pno]})\n")
    md = "\n".join(parts)
    md = drop_reference_sections(md)
    # strip garbled OCR "picture text" blocks (figures are carried as full-page renders)
    md = re.sub(r'<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->',
                '', md, flags=re.S)
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    (MD_DIR / f"{name}.md").write_text(md, encoding="utf-8")
    doc.close()
    return dict(name=name, pages=npages, content_end=content_end,
                fig_pages=[p+1 for p in fig_pages], rendered=len(rendered),
                md_chars=len(md))

if __name__ == "__main__":
    import json
    pairs = [tuple(a.split(":")) for a in sys.argv[1:]]
    for pid, nm in pairs:
        r = convert(pid, nm)
        print(json.dumps(r))
