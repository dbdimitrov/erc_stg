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
