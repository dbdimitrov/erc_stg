"""Reproducible SVG for Figure 1 of the research plan.
Run: python3 figures/make_fig1.py  -> figures/research_plan_fig1.svg (+ .pdf/.png via rsvg-convert)
Visual language: Cellina Fig. 1 (focal cell with bar-chart neighbours; blue = intrinsic z, red = extrinsic s,
lightning bolt = perturbation) and the NRG perspective (boxed panels, bold titles, muted palette).
"""
import math, subprocess, shutil, pathlib

W, H = 1000, 626
BLUE, RED, GREY, DGREY, INK = "#2f6db3", "#b83a3a", "#c9c9c9", "#7a7a7a", "#333333"
LBLUE, LRED, PANEL, OLIVE = "#dce8f5", "#f3dcdc", "#fafafa", "#6b8e4e"
FONT = "font-family='Helvetica, Arial, sans-serif'"
out = []
def add(s): out.append(s)

def text(x, y, s, size=12, weight="normal", anchor="middle", fill=INK, style=""):
    add(f"<text x='{x}' y='{y}' font-size='{size}' font-weight='{weight}' text-anchor='{anchor}' fill='{fill}' {FONT} {style}>{s}</text>")

def rect(x, y, w, h, fill="none", stroke=INK, sw=1, rx=6, dash=""):
    d = f"stroke-dasharray='{dash}'" if dash else ""
    add(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{rx}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}' {d}/>")

def line(x1, y1, x2, y2, stroke=INK, sw=1.2, dash="", arrow=False):
    d = f"stroke-dasharray='{dash}'" if dash else ""
    m = "marker-end='url(#arr)'" if arrow else ""
    add(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{stroke}' stroke-width='{sw}' {d} {m}/>")

def bars(cx, cy, heights, color=DGREY, w=3, gap=1.5, scale=1.0):
    """tiny bar chart centred at (cx, cy), heights in px"""
    n = len(heights); total = n*w + (n-1)*gap; x0 = cx - total/2
    for i, h in enumerate(heights):
        h = h*scale
        add(f"<rect x='{x0+i*(w+gap):.1f}' y='{cy+6-h:.1f}' width='{w}' height='{h:.1f}' fill='{color}'/>")

def cell(cx, cy, r=13, fill="#e6e6e6", stroke=GREY, sw=1, dash="", heights=(7,4,9,5), barcol=DGREY):
    d = f"stroke-dasharray='{dash}'" if dash else ""
    add(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}' {d}/>")
    bars(cx, cy, heights, barcol)

def star(cx, cy, R=34, n=6, focal_stroke=BLUE, nb_fill="#e6e6e6", nb_stroke=GREY, nb_bar=DGREY,
         edge=GREY, hot=(), hot_fill=LRED, hot_stroke=RED, hot_bar=RED, label=None):
    """focal cell v with n neighbours; indices in `hot` drawn as perturbed/new"""
    pts = []
    for i in range(n):
        a = -math.pi/2 + i*2*math.pi/n
        pts.append((cx + R*math.cos(a), cy + R*math.sin(a)))
    for (x, y) in pts:
        line(cx, cy, x, y, stroke=edge, sw=1)
    for i, (x, y) in enumerate(pts):
        hts = [(5,8,4,7),(8,3,6,5),(4,7,9,3),(6,5,3,8),(7,4,8,5),(3,8,5,6)][i % 6]
        if i in hot:
            cell(x, y, r=11, fill=hot_fill, stroke=hot_stroke, sw=1.4, heights=hts, barcol=hot_bar)
        else:
            cell(x, y, r=11, fill=nb_fill, stroke=nb_stroke, heights=hts, barcol=nb_bar)
    cell(cx, cy, r=13, fill="white", stroke=focal_stroke, sw=1.6, dash="3,2", heights=(6,9,4,7), barcol=INK)
    text(cx, cy+4, "<tspan font-style='italic'>v</tspan>", 10, fill=focal_stroke)
    if label: text(cx, cy+R+22, label, 10.5, fill=DGREY)

def bolt(x, y, s=1.0, fill=RED):
    p = f"M{x},{y} l{-4*s},{9*s} l{5*s},{-1*s} l{-3*s},{9*s} l{8*s},{-12*s} l{-5*s},{1*s} l{3*s},{-6*s} z"
    add(f"<path d='{p}' fill='{fill}' stroke='none'/>")

def trap(x, y, w, h, flip=False, fill="#6f6f6f", label=""):
    # encoder (narrows to the right) or decoder (widens)
    if not flip: pts = f"{x},{y} {x+w},{y+h*0.25} {x+w},{y+h*0.75} {x},{y+h}"
    else:        pts = f"{x},{y+h*0.25} {x+w},{y} {x+w},{y+h} {x},{y+h*0.75}"
    add(f"<polygon points='{pts}' fill='{fill}'/>")
    if label: text(x+w/2, y+h/2+5, label, 13, "bold", fill="white")

def latent(cx, cy, letter, color, caption, r=15):
    add(f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='white' stroke='{color}' stroke-width='2.2'/>")
    text(cx, cy+5, f"<tspan font-style='italic' font-weight='bold'>{letter}</tspan>", 14, fill=color)
    text(cx, cy+r+13, caption, 10, fill=color)

def tissue(x, y):
    """small tissue section: an irregular blob with a few coloured cell dots"""
    add(f"<path d='M{x},{y+20} c5,-22 40,-30 60,-16 c18,12 22,36 6,48 c-16,12 -46,10 -58,-4 c-8,-10 -10,-18 -8,-28 z' fill='#f1e4e4' stroke='{GREY}' stroke-width='1'/>")
    import random
    rnd = random.Random(3)
    cols = [BLUE, RED, OLIVE, DGREY, "#c9a227"]
    for i in range(26):
        px = x + 8 + rnd.random()*52; py = y + 4 + rnd.random()*40
        add(f"<circle cx='{px:.1f}' cy='{py:.1f}' r='2.2' fill='{rnd.choice(cols)}' opacity='0.85'/>")

# ---------------------------------------------------------------- canvas
add(f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>")
add("<defs><marker id='arr' markerWidth='8' markerHeight='8' refX='6' refY='3' orient='auto' markerUnits='strokeWidth'>"
    f"<path d='M0,0 L6,3 L0,6 z' fill='{INK}'/></marker>"
    "<marker id='arrR' markerWidth='8' markerHeight='8' refX='6' refY='3' orient='auto' markerUnits='strokeWidth'>"
    f"<path d='M0,0 L6,3 L0,6 z' fill='{RED}'/></marker></defs>")
add(f"<rect width='{W}' height='{H}' fill='white'/>")

# ---------------------------------------------------------------- TOP: Build (Aim 1)
rect(20, 16, 960, 246, fill=PANEL, stroke=DGREY, sw=1)
text(500, 40, "Build tissue representations that are intervenable and interpretable by design (Aim 1)", 14, "bold")

# tissue -> graph
tissue(48, 110); text(85, 185, "tissue section", 10.5, fill=DGREY)
line(128, 138, 160, 138, arrow=True)
star(232, 140, R=40, label="tissue graph")
# neighbours-in-graph annotation
line(292, 138, 322, 138, arrow=True)

# encoder
trap(326, 96, 62, 84, label="E")
text(357, 198, "encoder", 10.5, fill=DGREY)
# latents
latent(450, 118, "z", BLUE, "identity")
latent(450, 172, "s", RED, "microenvironment")
latent(528, 145, "e", OLIVE, "perturbation / context")
line(388, 118, 434, 118, stroke=BLUE, sw=1.4, arrow=False)
line(388, 172, 434, 172, stroke=RED, sw=1.4)
# bracket the three latents
rect(418, 90, 146, 118, fill="none", stroke=INK, sw=0.9, dash="4,3", rx=10)
text(491, 222, "structured representation", 11, "bold")
# perturbation bolt into e
bolt(538, 104, 0.7)
# decoder
line(560, 145, 594, 145, arrow=True)
trap(598, 96, 62, 84, flip=True, label="D")
text(629, 198, "decoder", 10.5, fill=DGREY)
# output: predicted cell (bars)
line(660, 145, 690, 145, arrow=True)
add(f"<circle cx='716' cy='145' r='16' fill='white' stroke='{INK}' stroke-width='1.4'/>")
bars(716, 145, (6,9,4,7), INK, w=3.4)
text(716, 180, "<tspan font-style='italic'>x&#770;</tspan><tspan font-size='8' baseline-shift='sub'>v</tspan>", 12)

# prior knowledge strip (optional, dashed) -> feeds latents and vocabulary
rect(760, 92, 210, 112, fill="#f4f7ee", stroke=OLIVE, sw=1.2, dash="5,3", rx=8)
text(865, 110, "prior knowledge", 12, "bold", fill=OLIVE)
text(865, 128, "ligand–receptor pairs · pathways", 10.5, fill=INK)
text(865, 144, "(LIANA+, OmniPath, MetalinksDB)", 10, fill=DGREY)
text(865, 168, "optional inductive bias;", 9.5, fill=DGREY, style="font-style='italic'")
text(865, 182, "vocabulary for interventions, names for features", 9.5, fill=DGREY, style="font-style='italic'")
line(760, 145, 738, 145, stroke=OLIVE, sw=1.2, dash="4,3")
add(f"<path d='M760,118 C700,60 610,60 566,90' fill='none' stroke='{OLIVE}' stroke-width='1.2' stroke-dasharray='4,3' marker-end='url(#arr)'/>")

# training data line
text(500, 248, "trained on spatial atlases and spatial perturbation screens (Perturb-CAST, CRISPRmap, Perturb-FISH, Perturb-map)", 10.5, fill=DGREY)

# arrows from top panel down into the three panels
for x in (185, 500, 815):
    line(x, 262, x, 282, arrow=True)

# ---------------------------------------------------------------- BOTTOM panels
PY, PH = 284, 326
panels = [(20, "Intervene (Aim 2)"), (340, "Interpret (Aim 3)"), (660, "Test (Aim 4)")]
for (px, title) in panels:
    rect(px, PY, 320, PH, fill=PANEL, stroke=DGREY, sw=1)
    text(px+160, PY+24, title, 14, "bold")

# ---- Intervene
bx = 20
text(bx+160, PY+44, "counterfactual queries on the tissue graph", 10.5, fill=DGREY, style="font-style='italic'")
# node perturbation
text(bx+80, PY+66, "node perturbation", 11, "bold")
text(bx+80, PY+80, "neighbours express a ligand", 9.5, fill=DGREY)
star(bx+80, PY+130, R=30, hot=(0,1,5), hot_fill=LRED)
bolt(bx+52, PY+88, 0.7)
# edge perturbation
text(bx+240, PY+66, "edge perturbation", 11, "bold")
text(bx+240, PY+80, "cell placed into a new niche", 9.5, fill=DGREY)
star(bx+240, PY+130, R=30, hot=(0,1,2,3,4,5), hot_fill=RED, hot_stroke=RED, hot_bar="white")
bolt(bx+212, PY+88, 0.7)
# arrows to predicted change
text(bx+160, PY+200, "predicted change in expression, Δ<tspan font-style='italic'>x</tspan><tspan font-size='8' baseline-shift='sub'>v</tspan>", 11)
for cx in (bx+80, bx+240):
    line(cx, PY+178, cx, PY+188, arrow=True)
# delta bars (signed)
def signed_bars(cx, cy, vals, w=5, gap=2):
    n=len(vals); total=n*w+(n-1)*gap; x0=cx-total/2
    line(x0-4, cy, x0+total+4, cy, stroke=GREY, sw=0.8)
    for i,v in enumerate(vals):
        col = RED if v>0 else BLUE
        y = cy - v if v>0 else cy
        add(f"<rect x='{x0+i*(w+gap):.1f}' y='{y:.1f}' width='{w}' height='{abs(v):.1f}' fill='{col}'/>")
signed_bars(bx+80, PY+228, (12,-5,8,-9,4,10))
signed_bars(bx+240, PY+228, (-8,11,-4,6,-12,7))
text(bx+160, PY+276, "scored on held-out tissues and contexts, at gene level,", 10, fill=INK)
text(bx+160, PY+290, "against linear and spatially-uninformed baselines", 10, fill=INK)
text(bx+160, PY+310, "e.g. TERRA, SpatialProp (node) · MintFlow (edge)", 9.5, fill=DGREY)

# ---- Interpret
ix = 340
text(ix+160, PY+44, "effects and features, validated by intervention", 10.5, fill=DGREY, style="font-style='italic'")
# effect-level: decomposition stacked bar (KIARA)
text(ix+82, PY+66, "effect level (KIARA)", 11, "bold")
text(ix+82, PY+80, "the cell vs its niche, per programme", 9.5, fill=DGREY)
# stacked horizontal bars for 3 programmes
labels = ["prog. A", "prog. B", "prog. C"]
fr = [(0.7,0.3),(0.35,0.65),(0.85,0.15)]
for i,(g,l) in enumerate(fr):
    y = PY+100+i*22; x0 = ix+40; wtot=110
    text(x0-6, y+10, labels[i], 9, anchor="end", fill=DGREY)
    add(f"<rect x='{x0}' y='{y}' width='{wtot*g:.1f}' height='13' fill='{BLUE}'/>")
    add(f"<rect x='{x0+wtot*g:.1f}' y='{y}' width='{wtot*l:.1f}' height='13' fill='{RED}'/>")
add(f"<rect x='{ix+40}' y='{PY+172}' width='9' height='9' fill='{BLUE}'/>"); text(ix+54, PY+180, "global, cell-type-specific", 9, anchor="start")
add(f"<rect x='{ix+40}' y='{PY+186}' width='9' height='9' fill='{RED}'/>"); text(ix+54, PY+194, "local, niche", 9, anchor="start")
# feature level: SAE -> LLM -> judge
text(ix+236, PY+66, "feature level (SAE + autointerp.)", 11, "bold")
# sparse feature vector
fx = ix+170; fy = PY+92
for i in range(9):
    on = i in (2,6)
    add(f"<rect x='{fx+i*9}' y='{fy}' width='7' height='14' fill='{RED if on else '#e3e3e3'}' stroke='{GREY}' stroke-width='0.5'/>")
text(fx+40, fy+26, "sparse feature", 9, fill=DGREY)
line(fx+84, fy+7, fx+100, fy+7, arrow=True)
rect(fx+102, fy-6, 46, 26, fill="white", stroke=INK, sw=1, rx=5); text(fx+125, fy+11, "LLM", 10, "bold")
text(fx+125, fy+34, "\"TGFβ response", 9, fill=DGREY); text(fx+125, fy+45, "in fibroblasts\"", 9, fill=DGREY)
line(fx+125, fy+50, fx+125, fy+64, arrow=True)
rect(fx+96, fy+66, 58, 24, fill="white", stroke=INK, sw=1, rx=5); text(fx+125, fy+82, "judge", 10, "bold")
line(fx+125, fy+90, fx+125, fy+98, stroke=OLIVE, sw=1.2, dash="4,3")
text(fx+125, fy+110, "vs prior knowledge", 9, fill=OLIVE)
text(fx+125, fy+122, "✓ nameable", 10, fill=OLIVE, weight="bold")
# rule
rect(ix+18, PY+226, 284, 40, fill="#fff7f7", stroke=RED, sw=1, rx=6)
text(ix+160, PY+243, "an interpretation counts only if steering the feature", 10, fill=INK)
text(ix+160, PY+257, "changes the counterfactual  →  candidate target", 10, "bold", fill=RED)
text(ix+160, PY+290, "features that are nameable and whose steering shifts", 10)
text(ix+160, PY+304, "the predicted response become the targets to test", 10)
# steering arrow back to Intervene
add(f"<path d='M{ix+18},{PY+246} C{ix-20},{PY+246} {ix-20},{PY+205} {bx+322},{PY+205}' fill='none' stroke='{RED}' stroke-width='1.4' stroke-dasharray='5,3' marker-end='url(#arrR)'/>")
text(ix-2, PY+266, "steer", 9.5, fill=RED, style="font-style='italic'")

# ---- Test
tx = 660
text(tx+160, PY+44, "open, live benchmarks for tissue representations (Open Problems)", 10.5, fill=DGREY, style="font-style='italic'")
# leaderboard
lx, ly = tx+78, PY+74
models = [("ours", 0.86, INK), ("model A", 0.74, DGREY), ("model B", 0.69, DGREY), ("model C", 0.62, DGREY), ("model D", 0.55, DGREY)]
base = 0.66
wmax = 200
for i,(nm, v, col) in enumerate(models):
    y = ly + i*18
    text(lx-6, y+10, nm, 9.5, anchor="end", fill=col)
    add(f"<rect x='{lx}' y='{y}' width='{v*wmax:.1f}' height='12' fill='{col if nm=='ours' else '#bdbdbd'}'/>")
bxl = lx + base*wmax
line(bxl, ly-6, bxl, ly+5*18, stroke=RED, sw=1.4, dash="4,3")
text(bxl, ly-10, "baseline floor (spatially uninformed)", 9, fill=RED)
text(lx+wmax/2, ly+5*18+12, "held-out contexts · gene-level metrics", 9.5, fill=DGREY)
# ground-truth sources
text(tx+160, PY+200, "ground truth", 11, "bold")
gts = [("interventional", "spatial perturbation screens", RED),
       ("observational", "validated interactions, curated by LLM agents", BLUE),
       ("mechanistic", "prior knowledge (scores interpretations only)", OLIVE)]
for i,(a,b,c) in enumerate(gts):
    y = PY+222 + i*24
    add(f"<circle cx='{tx+36}' cy='{y}' r='5' fill='{c}'/>")
    text(tx+48, y+4, f"<tspan font-weight='bold'>{a}</tspan>: {b}", 9.5, anchor="start")
text(tx+160, PY+308, "Novae · Nicheformer · TERRA · VirTues · ours", 9.5, fill=DGREY)

add("</svg>")
p = pathlib.Path(__file__).parent / "research_plan_fig1.svg"
p.write_text("\n".join(out), encoding="utf-8")
print("wrote", p)
if shutil.which("rsvg-convert"):
    for fmt in ("pdf", "png"):
        extra = ["-z", "2.5"] if fmt == "png" else []
        subprocess.run(["rsvg-convert", "-f", fmt, *extra, "-o", str(p.with_suffix("."+fmt)), str(p)], check=True)
        print("wrote", p.with_suffix("."+fmt))
