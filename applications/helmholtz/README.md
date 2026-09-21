# Helmholtz Munich AIH PI call — application package

*Track (i) AI in Biomedicine. Deadline 27 Sept 2026; invitations 16 Oct; Recruiting Symposium 27 Oct 2026. Single PDF: cover letter, CV, publication list (≤3 highlighted + impact), research plan (max 3 pages), ≥3 referees. Contacts: Prof. Carsten Marr (scientific), Anna Sacher (admin).*

## Files

| Requirement | File | Status |
|---|---|---|
| Publication list, 3 highlighted | `publication_summary.md` | drafted, user-edited |
| Research plan (max 3 pp) | `research_plan.md` → `research_plan.pdf` via `build/render.sh` | **v1 draft**; body+figure+table = 3 pages, references spill ~0.7 page |
| Figure 1 | `figures/make_fig1.py` → `figures/research_plan_fig1.{svg,pdf,png}` | v1; reproducible, restyle later in Illustrator/Inkscape if wanted |
| Bibliography | `research_plan.bib` (52 entries, DOIs verified 2026-09-21) + `research_plan_refs_notes.md` | done |
| Referees | `references.md` | from Aithyra package; re-check |
| Cover letter / email | `cover_email.md` | to do |
| Institute intelligence | `additional_info/` | done |

Render: `./build/render.sh` (pandoc → xelatex, Nature numeric CSL, TNR 11 pt, 2 cm margins; header in `build/header.tex`). Prints the page count.

## Research plan — locked decisions (grill-me session, 2026-09-21)

1. **Title:** "What if, and why: tissue representations one can intervene on, interpret and test".
2. **Architecture:** four aims. Aim 1 *Build* (top of figure) is the thing itself; Aims 2 *Intervene*, 3 *Interpret*, 4 *Test* are what make the build worthwhile. "The three without building them sound ungrounded."
3. **Aim 1 (the model):** generative model of tissue with a latent structured by design: intrinsic identity (z), extrinsic microenvironment (s) [Cellina], explicit perturbation/context term in a programme space [KIARA]. LIANA/OmniPath ligand–receptor + pathway layer = vocabulary for interventions and feature names. Prior knowledge is an *optional* inductive bias, never a requirement. No scale claim ("compete on what the representation can be asked, not on cells"). Trained on spatial atlases + spatial perturbation screens (Perturb-CAST, CRISPRmap, Perturb-FISH, Perturb-map). Transcriptomics first, proteomics later.
4. **Aim 2 (intervene):** counterfactual queries of two kinds: ligand/treatment interventions (node perturbation; cite TERRA, SpatialProp as existing attempts) and response to a different neighbourhood (edge perturbation; cite MintFlow). Scored on held-out contexts, gene level, vs linear and spatially-uninformed baselines. Causality claim kept with the operational hedge (not Pearlian).
5. **Aim 3 (interpret):** two strands. (a) Mechanistic, effect-level: KIARA decomposition into global cell-type-specific vs local niche response, built on OmniPath/LIANA priors. (b) Feature-level: SAEs + LLM autointerpretation with judge; ehrx in **one sentence, no details**. Join: an interpretation counts only if steering the feature changes the counterfactual → candidate targets.
6. **Aim 4 (test):** Open Problems task series for tissue representations (Novae, Nicheformer, TERRA, VirTues, ours). Ground truth: interventional (spatial screens), observational (validated interactions curated by LLM agents, extending scBaseCount's agentic curation; extraction itself benchmarked), mechanistic (prior knowledge, scores interpretations only). Mandatory spatially-uninformed baseline floor. Not communication-only.
7. **Page budget:** opening ~0.35, starting point ~0.35, figure ~0.4, aims ~1.5, fit/translation/table ~0.4. No separate past-research section (publication summary covers it).
8. **Fit / clinic:** CRC anchor disease; name Theis's ecosystem (Nicheformer, Open Problems) and DKFZ (Perturb-CAST); other PIs by group topic only (cells→patients, tumour neighbourhoods, pathology/microscopy images); Marr only via the M1 Clinical AI Consultants programme. Two-step translation: target nomination, then patient-level readout. No clinical tool / trial / virtual patient claims.
9. **Timeline/team/funding:** compact table (years 1–2 / 2–4 / 4–5 × aims + group size). One sentence: ERC StG (eligible from 2027) on Aims 1–3; record = MSCA + named key person on CZI LIANA+ grant (Saeys). **Nothing invented** (no DFG/internal projects).
10. **Venues:** Nature Methods and sister journals primary; ML venues secondary but present, one sentence.
11. **Figure:** Cellina Fig. 1 visual language (focal cell v with bar-chart neighbours; blue z / red s; lightning bolt) + perspective's boxed panels. Top: tissue → graph → encoder → structured latent (+ dashed optional prior knowledge) → decoder. Bottom: Intervene / Interpret / Test, with a red "steer" arrow from Interpret back to Intervene.
12. **Voice:** first person, future tense with the user's hedges (will / I envision / I anticipate); no spec-sheet present tense; no slop vocabulary; minimal em-dashes; keep the two signature lines (generalization epigram; "ill-posed in general, well-posed in practice").

## Facts to keep straight (from the bib check)

- Perturb-CAST = Breinig et al., *Nat Biomed Eng* 2026, DKFZ; Stegle & Gerstung senior, Heidari third author.
- Cell PII S0092-8674(26)00998-0 = scBaseCount (Youngblut et al., Arc): agentic *curation* of expression data, not an interaction-mining paper.
- SAFFRON (Handa et al. 2026): SAEs on spatial FMs; none beats baselines on local microenvironment. Kendiukhov 2026: SAE features encode co-expression, not causal logic.
- Nicheformer first author Tejada-Lapuerta; TERRA = Birk et al., Lotfollahi senior; Perturb-FISH is *Cell* 2025; CRISPRmap = Gu et al., *Nat Biotechnol* 2025.

## Open items

- [ ] Decide whether references count towards the 3 pages. If yes: cut ~0.7 page (drop optional refs; trim text) or move to 2-column/8 pt.
- [ ] Preprint entries render the DOI twice under the Nature CSL (url + doi fields); strip `url` for bioRxiv entries or switch CSL.
- [ ] Table wording: "RSE" → spell out; "Community adoption" is vague.
- [ ] Cover letter; re-check `references.md` trio for Helmholtz; CV referee trio consistency.
- [ ] Numbers to refresh at submission: 300,000 downloads, citations, Cellina venue status.
