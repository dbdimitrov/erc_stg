# CV tailoring — record of what was applied (2026-08-29)

*Supersedes the earlier draft-recommendation version of this file, which was stale (it proposed
fixes already present in the .tex). Backup of the pre-tailoring CV: `DanielDimitrov_CV.tex.bak`.*

## Why

The posting's Basic Qualification #3 is "analysing large-scale genetic and multi-omics datasets and
integrating these with clinical or phenotypic data". The previous CV contained **zero** instances of
*genetic, clinical, phenotype, patient cohort, proteomics, biomarker, target, polygenic* — the
evidence existed but was invisible to a recruiter skim. That was the highest-leverage fixable gap.

## Applied

1. **Headline** → "Computational Biologist — Multi-omics, Spatial & Clinical Data for Target and
   Biomarker Discovery" (mirrors the posting's own "target, biomarker and patient-selection" framing).
2. **Summary** → adds "integrated with clinical and phenotypic data", "disease mechanism, biomarkers
   and targets". Download claim split: **300,000+ installs** (`liana-py`, his own) rather than the
   previous 600k, which silently absorbed co-authored `decoupleR`.
3. **Stegle bullet** → EHRx spelled out: EHR foundation models, feature steering, **polygenic-risk
   enrichment against UK Biobank genetic and clinical data**. Attributed "conceived and direct" —
   the PRS arm is student-run, so a hands-on claim would not survive interview.
4. **Saez lab, new bullet** → patient cohorts, CKD and IgA nephropathy (MSCA STRATEGY-CKD), and the
   HCA *Nature* gut-disease study with his own CCC analysis called out. Previously invisible.
5. **Ghent** → "transcriptomics & proteomics, CKD patient cohorts" (proteomics is named twice in the
   posting and appeared nowhere on the CV). Dates confirmed as **May–Jun 2022**, 2 months;
   `cv_facts.md:20` was wrong (said 2022-05–2023-06) and has been corrected.
6. **Photo removed** — UK convention, and it was 2.6 MB of a 1.6 MB PDF. PDF is now ~30 KB.
7. **Sidebar: Funding & Awards added** — MSCA ITN Fellowship (STRATEGY-CKD), CZI grant (named key
   person), Research-Based Learning Prize.
8. **Talks** → three additions from `cv_facts.md` (VIB Ghent invited seminar 2026, GAF Sofia 2025,
   AI Seminar @ EMBL 2026) and split into *Invited* / *Selected & institutional*, since three are
   invited and that distinction was not being made. AI & Biology @ EMBL 2026 stays non-invited
   per `cv_facts.md`.
9. **Supervision & Leadership section added** (page 2, which was ~50% empty) — leadership is the
   thinnest part of the case for an *Associate Director* title and is a preferred qualification.
10. **Publications header** → adds "4,000+ citations, h-index 14".
11. **Layout** — line spacing 1.06→1.0, margins 1.4→1.15 cm, tighter section spacing, pre-PhD
    entries (Glasgow thesis, MPI-CBG internship) compressed to one "Earlier:" line. Holds at
    2 pages; the two-column look is unchanged.

## Not applied

- **Peer review section** — user judged it irrelevant for an industry role. Agreed.
- **References → "available on request"** — left as-is (named senior referees are a positive
  signal). Optional change if uncomfortable putting supervisors' emails into an ATS.

## Open risks no CV edit fixes

- **Seniority.** GSK posted Principal Scientist ×2 (446240, 446659) and Director (445320) in the
  same family. AD sits mid-ladder at ~2 years post-PhD. User chose to target AD only.
- **Location — RESOLVED 2026-08-30.** The application form offers a choice of 3 sites, one being
  **Heidelberg**; the Stevenage/UK language applies only to candidates choosing Stevenage. Not a
  risk. (Public posting page went dark ~3 days before the stated 2 Sep close, but the started
  draft still accepts submission.)

## Em-dash / case / quality-wording pass (2026-08-30)

- Removed every `---` em-dash from the rendered CV: replaced with commas (Stegle/EHRx bullets,
  Education degree classifications, Supervision mentoring bullet), colons (headline, patient-cohorts
  bullet), or parentheses (Zeller/Glorieux/Experian/Earlier one-line roles, CZI grant); summary
  sentence restructured to avoid the parenthetical entirely. All `--` en-dashes (date ranges,
  `cell--cell`) left untouched.
- LIANA bullet re-worded to "delivered as reproducible, production-quality software", deliberately
  mirroring the job ad's basic qualification "delivering reproducible, production-quality analysis".
- Engineering sidebar line case-standardized: Git, continuous integration, unit testing, Conda,
  Docker, Agile development (brands capitalized, generic practices lowercase).
- `BioConductor` corrected to official spelling `Bioconductor`; Consortia sidebar aligned with
  page 2: "Open Problems in Single-Cell Analysis" (capital C) in both.
- Three `% ----------` comment dividers in the preamble converted to `% ==========` so a `---` grep
  of the file is clean (non-rendered, cosmetic only).
- Recompiled twice with xelatex: no errors, output still exactly 2 pages.

## Bolding / talks pass (2026-08-30)

- **Bolding policy**: framework names unbolded in Experience (EHRx); explanatory keywords bolded
  instead — *cell-cell communication*, *300,000+ installs*, *production-quality software*,
  *candidate targets*. Page-2 Supervision keeps all four project names bolded (internally
  consistent list). "Earlier:" now bold.
- **Talks merged into one list**: dropped GAF Sofia 2025 and AI Seminar @ EMBL 2026 (user call,
  overrides the 2026-08-22 "focus items" note in cv_facts.md); "(invited)" tagged on VIB Ghent 2026
  and MOPITAS only — AI & Biology @ EMBL and VIB Spatial Omics stay untagged per the dossier's
  "do not label invited" rule. MOPITAS year corrected 2024 → 2025 (cv_facts.md updated).
- User manual edits taken as base: publications header (h-index removed), Supervision reworded to
  "co-conceived and mentor", co-organised line moved out of Supervision. Dangling semicolon from
  that edit fixed.
- Recompiled: 2 pages, no overfull boxes.
- **Correction (same day, later):** user confirmed ALL four remaining talks were invited — the
  cv_facts.md "do not label invited" note for AI & Biology @ EMBL 2026 and the "short talk" label
  for VIB Spatial Omics 2024 were stale and have been corrected in cv_facts.md (§3, dated notes).
  CV now lists all four under a bold "Invited:" header, matching the "Co-organised:" style.

## Whitespace redistribution pass (2026-08-30)

**Diagnosis.** Rendered both pages to PNG and measured: page 1 had ~35 mm of dead space below the
content, page 2 had ~82 mm. The text itself was set at `\setstretch{1.0}` with 9 pt section leads —
so the page read as *dense text plus a large trailing gap*, which is what "cramped" was describing.
The problem was distribution, not content volume; **cutting content would have made it worse.**

Applied in two passes, re-rendering and inspecting the images after each (a "2 pages" line in the
log proves nothing about distribution, and under `paracol` a page-1 overflow silently becomes a
third page):

- Pass A — `\setstretch` 1.0 → **1.06**; `\titlespacing` 9 pt/5 pt → **14 pt/6 pt**; `\pub` trailing
  space 6 pt → **9 pt**.
- Pass B — `cvitems` itemsep 2 → **3.5 pt**, topsep 2.5 → **3.5 pt**, closing space 5 → **7 pt**;
  `\cvrole` trailing space 2 → **3 pt**; one-line role/education separators 2 → **4 pt**; all sidebar
  `\\[3pt]` → **`\\[4pt]`**.
- **Margins deliberately untouched** (1.15 cm top/bottom). Highest-leverage knob and the one most
  likely to tip page 1 over; held in reserve.
- **Supervision & Leadership expanded** (page 2) — the 4 active projects broken out of one dense
  run-on bullet into a nested per-project list, and the authorship/codebase outcome promoted into
  the headline bullet. This is simultaneously where the dead space was and the thinnest dimension of
  an *Associate Director* case (team-leading/mentoring is a preferred qualification). Attribution
  language unchanged: "co-conceived and currently lead", EHRx PRS arm still described as
  feature-steering tested against UK Biobank, no hands-on genetics claim.

**Result:** page 1 trailing gap 35 → ~10 mm, page 2 82 → ~32 mm. Still exactly 2 pages, no overfull
boxes.

### Photo — decided against (again), 2026-08-30

User asked whether to re-add it since the target site is Heidelberg. No. German practice is
*Lichtbild-optional* post-AGG and large employers increasingly instruct recruiters to disregard
photos; the upside is neutral at best. Against that: it consumes the header space the spacing fix
needs, it adds no evidence a reviewer can act on, and the earlier removal took the PDF from 1.6 MB
to ~30 KB (`photo.png` is 2.6 MB). Keep it out. `photo.png` retained in the directory unused.

### No further filler needed

~32 mm of trailing space on page 2 of a two-page CV is a normal bottom margin, not a defect. Do not
chase it with content — in particular, do not add a third referee to fill the References row: the
open question on that block is whether to *remove* the supervisors' emails ("available on request"),
and industry applications are confidential from them for now.

### Nested-list punctuation (same pass)

Project lines set as `\textbf{Name}: description` — colon, not comma. Comma reads as apposition where
the reader expects a definition; colon is the same substitution used for the headline and
patient-cohorts bullet in the em-dash pass above.
