"""Reproducible SVG for Figure 1 of the research plan (Helmholtz).

Run: python3 figures/make_fig1.py
  -> figures/research_plan_fig1.svg (+ .pdf/.png via rsvg-convert)

Canvas 14.6 cm x 9.5 cm, viewBox 1460 x 950 user units (1 unit = 0.1 mm).
1 pt = 3.53 units, so body labels 7-8 pt -> font-size 24-27,
panel titles 8.5 pt bold -> 30, 0.6 pt strokes -> stroke-width 2.1.

Visual language: NRG-perspective boxed panels (pale tinted fills, dark-slate
rules, bold titles above-left), plus the tissue-as-graph-of-cells glyph.
Four bands in aim order, top to bottom, joined by downward arrows, with a
dashed red "steer" return from Aim 4 to Aim 3 along the right margin.
"""
import math, subprocess, shutil, pathlib

W, H = 1460, 950

# ---- palette
INK   = "#2E3A47"          # strokes / text
BLUE  = "#2E6FB7"          # intrinsic / identity accent
RED   = "#C0392B"          # niche / steer accent
MUT   = "#7C8894"
F1, F2, F3, F4 = "#DCE8F5", "#E2EDE4", "#F6ECD6", "#F7DEDE"
WHITE = "#FFFFFF"
CELL  = "#EDF1F4"
CELLE = "#94A2AE"

FS_T, FS_S, FS_L, FS_XS = 30, 27, 26, 24     # title / subtitle / label / small
SW_P, SW_B, SW_E = 2.1, 1.8, 1.4             # panel / box / edge
FONT = "font-family='Helvetica, Arial, sans-serif'"

out = []
def add(s): out.append(s)

# ---------------------------------------------------------------- primitives
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def tw(s, size, bold=False):
    """conservative rendered width of a Helvetica string, in user units"""
    return len(s) * size * (0.66 if bold else 0.62)

def wrap(s, maxw, size, bold=False):
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if cur and tw(trial, size, bold) > maxw:
            lines.append(cur); cur = w
        else:
            cur = trial
    if cur: lines.append(cur)
    return lines

def text(x, y, s, size=FS_L, weight="normal", anchor="middle", fill=INK, italic=False, rot=None):
    it = "font-style='italic'" if italic else ""
    tr = f"transform='rotate({rot},{x:.1f},{y:.1f})'" if rot is not None else ""
    add(f"<text x='{x:.1f}' y='{y:.1f}' font-size='{size}' font-weight='{weight}' "
        f"text-anchor='{anchor}' fill='{fill}' {FONT} {it} {tr}>{esc(s)}</text>")

def mtext(x, y, s, maxw=None, size=FS_L, weight="normal", anchor="middle", fill=INK,
          italic=False, lh=None):
    """multi-line text. `s` may be a list of explicit lines or a string to wrap.
    y is the baseline of the first line; returns the baseline of the last."""
    lh = lh or size * 1.10
    lines = s if isinstance(s, (list, tuple)) else wrap(s, maxw, size, weight == "bold")
    for i, ln in enumerate(lines):
        text(x, y + i * lh, ln, size, weight, anchor, fill, italic)
    return y + (len(lines) - 1) * lh

def rect(x, y, w, h, fill="none", stroke=INK, sw=SW_B, rx=10, dash="", op=1.0):
    d = f"stroke-dasharray='{dash}'" if dash else ""
    add(f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='{rx}' "
        f"fill='{fill}' fill-opacity='{op}' stroke='{stroke}' stroke-width='{sw}' {d}/>")

def line(x1, y1, x2, y2, stroke=INK, sw=SW_E, dash="", arrow=False, red=False):
    d = f"stroke-dasharray='{dash}'" if dash else ""
    m = f"marker-end='url({'#arrR' if red else '#arr'})'" if arrow else ""
    add(f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' "
        f"stroke='{stroke}' stroke-width='{sw}' stroke-linecap='round' {d} {m}/>")

def path(d, stroke=INK, sw=SW_E, fill="none", dash="", arrow=False, red=False):
    ds = f"stroke-dasharray='{dash}'" if dash else ""
    m = f"marker-end='url({'#arrR' if red else '#arr'})'" if arrow else ""
    add(f"<path d='{d}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}' "
        f"stroke-linejoin='round' stroke-linecap='round' {ds} {m}/>")

def down_arrow(x, y1, y2):
    line(x, y1, x, y2, stroke=INK, sw=SW_P, arrow=True)

def plus(cx, cy, s=9, col=INK, sw=2.4):
    line(cx - s, cy, cx + s, cy, stroke=col, sw=sw)
    line(cx, cy - s, cx, cy + s, stroke=col, sw=sw)

def bolt(cx, cy, s=1.0, fill=RED):
    d = (f"M{cx:.1f},{cy - 17 * s:.1f} l{-11 * s:.1f},{19 * s:.1f} l{7 * s:.1f},0 "
         f"l{-5 * s:.1f},{15 * s:.1f} l{15 * s:.1f},{-21 * s:.1f} l{-7.5 * s:.1f},0 "
         f"l{6 * s:.1f},{-13 * s:.1f} z")
    add(f"<path d='{d}' fill='{fill}' stroke='{WHITE}' stroke-width='1.2'/>")

def minibars(cx, cy, hts, col=MUT, w=4.0, gap=2.4):
    n = len(hts); tot = n * w + (n - 1) * gap; x0 = cx - tot / 2
    for i, h in enumerate(hts):
        add(f"<rect x='{x0 + i * (w + gap):.1f}' y='{cy + 5 - h:.1f}' width='{w}' "
            f"height='{h:.1f}' fill='{col}'/>")

def cellg(cx, cy, r=13, fill=CELL, stroke=CELLE, sw=1.6, hts=(7, 11, 5), bar=MUT):
    add(f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r}' fill='{fill}' stroke='{stroke}' "
        f"stroke-width='{sw}'/>")
    minibars(cx, cy, hts, bar)

HTS = [(6, 11, 4), (10, 5, 8), (5, 9, 11), (8, 6, 4), (11, 7, 9), (4, 10, 6)]

def graph(cx, cy, R=36, r=12, n=6, hot=(), swap=False, rot0=-90, focal=BLUE):
    """tissue-as-graph-of-cells: focal cell in a dashed ring, thin edges to neighbours"""
    pts = []
    for i in range(n):
        a = math.radians(rot0 + (30 if swap else 0)) + i * 2 * math.pi / n
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    for i, (x, y) in enumerate(pts):
        line(cx, cy, x, y, stroke="#B6C0C9", sw=1.3)
        x2, y2 = pts[(i + 1) % n]
        line(x, y, x2, y2, stroke="#D2D9DF", sw=1.1)
    for i, (x, y) in enumerate(pts):
        if i in hot:
            cellg(x, y, r=r - 1, fill="#F3C9C4", stroke=RED, hts=HTS[i % 6], bar=RED)
        elif swap:
            cellg(x, y, r=r - 1, fill="#D8E4F2", stroke=BLUE, hts=HTS[(i + 3) % 6], bar=BLUE)
        else:
            cellg(x, y, r=r - 1, hts=HTS[i % 6])
    add(f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r + 8}' fill='none' stroke='{focal}' "
        f"stroke-width='1.8' stroke-dasharray='5,4'/>")
    cellg(cx, cy, r=r, fill=WHITE, stroke=focal, sw=2.0, hts=(9, 5, 11), bar=focal)

def densegrid(x, y, cols, rows, s=19, gap=4, fill="#C2CFDA", stroke="#9AA9B6"):
    for j in range(rows):
        for i in range(cols):
            add(f"<rect x='{x + i * (s + gap):.1f}' y='{y + j * (s + gap):.1f}' "
                f"width='{s}' height='{s}' rx='2' fill='{fill}' stroke='{stroke}' "
                f"stroke-width='0.9'/>")
    return x + cols * (s + gap) - gap, y + rows * (s + gap) - gap

def papers(cx, cy):
    """stack of documents with a check mark"""
    for dx, dy, f in [(-9, 9, "#E9EEF3"), (0, 0, "#F4F7FA"), (9, -9, WHITE)]:
        rect(cx - 44 + dx, cy - 40 + dy, 80, 72, fill=f, stroke=INK, sw=1.5, rx=5)
    for k in range(4):
        line(cx - 28, cy - 30 + k * 13, cx + 20, cy - 30 + k * 13, stroke="#AEB9C4", sw=1.6)
    path(f"M{cx + 18},{cy + 20} l11,12 l22,-31", stroke="#3F8A4E", sw=4.4)

def respbars(cx, cy, vals, w=9, gap=6):
    n = len(vals); tot = n * w + (n - 1) * gap; x0 = cx - tot / 2
    line(x0 - 10, cy, x0 + tot + 10, cy, stroke=MUT, sw=1.4)
    for i, v in enumerate(vals):
        col = RED if v > 0 else BLUE
        yy = cy - v if v > 0 else cy
        add(f"<rect x='{x0 + i * (w + gap):.1f}' y='{yy:.1f}' width='{w}' "
            f"height='{abs(v):.1f}' rx='1.5' fill='{col}'/>")

# ---------------------------------------------------------------- canvas
add(f"<svg xmlns='http://www.w3.org/2000/svg' width='14.6cm' height='9.5cm' "
    f"viewBox='0 0 {W} {H}'>")
add("<defs>"
    "<marker id='arr' markerWidth='7' markerHeight='7' refX='5.6' refY='2.8' orient='auto' "
    f"markerUnits='strokeWidth'><path d='M0,0 L5.6,2.8 L0,5.6 z' fill='{INK}'/></marker>"
    "<marker id='arrR' markerWidth='7' markerHeight='7' refX='5.6' refY='2.8' orient='auto' "
    f"markerUnits='strokeWidth'><path d='M0,0 L5.6,2.8 L0,5.6 z' fill='{RED}'/></marker>"
    "</defs>")
add(f"<rect width='{W}' height='{H}' fill='white'/>")

X0, X1 = 14, 1380          # panels; the right margin carries the steer arrow
PAD = 16
CX0, CX1 = X0 + PAD, X1 - PAD
CW = CX1 - CX0             # 1334
MIDX = (X0 + X1) / 2

B1, B1H = 10, 210          # bands: 22 / 24 / 23 / 22 % of height
B2, B2H = 242, 226
B3, B3H = 490, 222
B4, B4H = 734, 205

def panel(y, h, fill, title):
    rect(X0, y, X1 - X0, h, fill=fill, stroke=INK, sw=SW_P, rx=12)
    text(CX0, y + 38, title, FS_T, "bold", anchor="start")

def subbox(x, y, w, h):
    rect(x, y, w, h, fill=WHITE, stroke=INK, sw=SW_B, rx=9, op=0.72)

# ================================================================ BAND 1
panel(B1, B1H, F1, "Gather data and build ground truth (Aim 1)")
text(CX1, B1 + 38, "benchmark, baseline floor", FS_S, anchor="end", italic=True)

BY, BH = 58, 152
GC = BY + 50
widths = [280, 336, 300, 382]
xs, cur = [], CX0
for w in widths:
    xs.append(cur); cur += w + 12
cs = [x + w / 2 for x, w in zip(xs, widths)]
for x, w in zip(xs, widths):
    subbox(x, BY, w, BH)

graph(cs[0], GC)
mtext(cs[0], BY + 116, ["spatial atlases"])

graph(cs[1], GC, hot=(1,))
bolt(cs[1] + 38, GC - 34, 1.05)
mtext(cs[1], BY + 116, ["spatial perturbation", "screens"])

cy3 = GC + 6
cellg(cs[2] - 48, cy3, r=20, hts=(9, 14, 6))
cellg(cs[2] + 48, cy3, r=20, fill="#D8E4F2", stroke=BLUE, hts=(7, 11, 13), bar=BLUE)
path(f"M{cs[2] - 24},{cy3 - 26} q24,-22 48,0", stroke=RED, sw=2.0, arrow=True, red=True)
rect(cs[2] - 13, cy3 - 56, 26, 18, fill="#F3C9C4", stroke=RED, sw=1.6, rx=4)
add(f"<circle cx='{cs[2]:.1f}' cy='{cy3 - 47}' r='3.2' fill='{RED}'/>")
mtext(cs[2], BY + 116, ["measured contacts"])

papers(cs[3], GC + 2)
mtext(cs[3], BY + 116, ["validated interactions,", "curated by LLM agents"])

down_arrow(MIDX, B1 + B1H + 2, B2 - 3)

# ================================================================ BAND 2
panel(B2, B2H, F2, "Build tissue representations (Aim 2)")
SBY, SBH = B2 + 50, 170
LW = (CW - 16) / 2
LX, RX = CX0, CX0 + LW + 16
subbox(LX, SBY, LW, SBH)
subbox(RX, SBY, LW, SBH)

# --- left: decomposable, interpretable by design
text(LX + LW / 2, SBY + 26, "decomposable, interpretable by design", FS_S, "bold")
rect(LX + 26, SBY + 34, LW - 52, 28, fill="none", stroke=MUT, sw=1.6, rx=8, dash="6,4")
text(LX + LW / 2, SBY + 54, "prior knowledge (LIANA/OmniPath)", FS_XS)
line(LX + LW / 2, SBY + 64, LX + LW / 2, SBY + 76, stroke=MUT, sw=1.6, dash="5,4", arrow=True)

bx0 = LX + 230
rows = [("basal", 210, "#9FB4C7"), ("perturbation", 150, "#E0B4AE"), ("niche", 182, BLUE)]
for i, (lab, bw, col) in enumerate(rows):
    y = SBY + 82 + i * 29
    text(bx0 - 12, y + 17, lab, FS_XS, anchor="end")
    rect(bx0, y, bw, 22, fill=col, stroke=INK, sw=1.2, rx=4)
for i in range(2):
    plus(bx0 + 232, SBY + 82 + i * 29 + 26, 9)
ytop, ybot = SBY + 82, SBY + 82 + 2 * 29 + 22
path(f"M{bx0 + 252},{ytop} l14,0 l0,{ybot - ytop} l-14,0", stroke=INK, sw=1.6)
line(bx0 + 268, (ytop + ybot) / 2, bx0 + 322, (ytop + ybot) / 2, stroke=INK, sw=SW_P, arrow=True)

# --- right: high-capacity, read post hoc
text(RX + LW / 2, SBY + 26, "black box, decoded once trained", FS_S, "bold")
GW = 203 + 16 + 54 + 22 + 30
gx = RX + (LW - GW) / 2
gy = SBY + 70
gx1, gy1 = densegrid(gx, gy, 9, 4, s=19, gap=4)
gmid = (gy + gy1) / 2
line(gx1 + 16, gmid, gx1 + 70, gmid, stroke=INK, sw=SW_P, arrow=True)
vx = gx1 + 92
for k in range(4):
    add(f"<rect x='{vx:.1f}' y='{gmid - 40 + k * 21:.1f}' width='30' height='17' rx='2' "
        f"fill='{'#8FA8BF' if k % 2 else '#C2CFDA'}' stroke='#9AA9B6' stroke-width='0.9'/>")

down_arrow(MIDX, B2 + B2H + 2, B3 - 3)

# ================================================================ BAND 3
panel(B3, B3H, F3, "Intervene (Aim 3)")
CY = B3 + 95
pitch = CW / 4
c3 = [CX0 + pitch / 2 + i * pitch for i in range(4)]
LBY = CY + 57

graph(c3[0], CY)
mtext(c3[0], LBY, ["observed"])

graph(c3[1], CY, hot=(0, 1, 4))
bolt(c3[1] + 40, CY - 36, 1.0)
mtext(c3[1], LBY, ["node: what", "neighbours express"])

graph(c3[2], CY, swap=True)
mtext(c3[2], LBY, ["edge: which", "neighbours"])

respbars(c3[3], CY, (26, -14, 19, -25, 11, -8, 22))
mtext(c3[3], LBY, ["predicted response,", "scored on Aim 1", "ground truth"])

for i in range(3):
    line(c3[i] + 56, CY, c3[i + 1] - 62, CY, stroke=INK, sw=SW_P, arrow=True)

down_arrow(MIDX, B3 + B3H + 2, B4 - 3)

# ================================================================ BAND 4
panel(B4, B4H, F4, "Interpret (Aim 4)")
IY, IH = B4 + 48, 145
subbox(LX, IY, LW, IH)
subbox(RX, IY, LW, IH)

# --- left: read the structure (same decomposition, one term highlighted)
text(LX + LW / 2, IY + 26, "read the structure", FS_S, "bold")
bx0 = LX + 215
for i, (bw, col) in enumerate([(210, "#9FB4C7"), (150, "#E0B4AE"), (182, RED)]):
    y = IY + 36 + i * 25
    rect(bx0, y, bw, 20, fill=col, stroke=RED if col == RED else INK,
         sw=2.6 if col == RED else 1.2, rx=4)
text(LX + LW / 2, IY + 130, "global cell-type vs local niche", FS_XS, italic=True)

# --- right: read the features (sparse dictionary fan-out, one feature highlighted)
text(RX + LW / 2, IY + 26, "read the features", FS_S, "bold")
gx, gy = RX + 46, IY + 40
gx1, gy1 = densegrid(gx, gy, 4, 4, s=17, gap=4)
dx = RX + 300
dys = [IY + 38 + k * 20 for k in range(4)]
for dy in dys:
    line(gx1 + 8, (gy + gy1) / 2, dx - 14, dy + 7, stroke="#C2CBD3", sw=1.2)
for k, dy in enumerate(dys):
    on = (k == 2)
    add(f"<rect x='{dx:.1f}' y='{dy:.1f}' width='120' height='14' rx='3' "
        f"fill='{'#F7DEDE' if on else '#EEF1F4'}' stroke='{RED if on else '#B6BFC7'}' "
        f"stroke-width='{2.4 if on else 1.0}'/>")
    for m in range(5):
        col = RED if (on and m == 3) else "#C3CBD3"
        add(f"<circle cx='{dx + 14 + m * 24:.1f}' cy='{dy + 7:.1f}' r='4' fill='{col}'/>")
text(RX + LW / 2, IY + 130, "described by an LLM, judged blind", FS_XS, italic=True)

# --- steer: dashed red feedback from Aim 4 up to Aim 3, along the right margin
RA = X1 + 22
y4, y3 = B4 + 100, B3 + 110
path(f"M{X1 + 2},{y4} L{RA},{y4} L{RA},{y3} L{X1 + 8},{y3}",
     stroke=RED, sw=2.1, dash="7,5", arrow=True, red=True)
sy = (y3 + y4) / 2
text(RA + 20, sy, "steer: does the", FS_XS, fill=RED, rot=-90)
text(RA + 44, sy, "counterfactual change?", FS_XS, fill=RED, rot=-90)

add("</svg>")

p = pathlib.Path(__file__).parent / "research_plan_fig1.svg"
p.write_text("\n".join(out), encoding="utf-8")
print("wrote", p)
if shutil.which("rsvg-convert"):
    for fmt in ("pdf", "png"):
        extra = ["-z", "2.5"] if fmt == "png" else []
        subprocess.run(["rsvg-convert", "-f", fmt, *extra, "-o", str(p.with_suffix("." + fmt)),
                        str(p)], check=True)
        print("wrote", p.with_suffix("." + fmt))
