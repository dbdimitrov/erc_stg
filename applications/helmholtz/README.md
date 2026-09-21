# Helmholtz Munich AIH PI call — application package

*Track (i) AI in Biomedicine. Deadline 27 Sept 2026; invitations 16 Oct; Recruiting Symposium 27 Oct 2026. Single PDF: cover letter, CV, publication list (≤3 highlighted + impact), research plan (max 3 pages), ≥3 referees. Contacts: Prof. Carsten Marr (scientific), Anna Sacher (admin).*

## Files

| Requirement | File | Status |
|---|---|---|
| Publication list, 3 highlighted | `publication_summary.md` | drafted, user-edited |
| Research plan (max 3 pp) | `research_plan.tex` → `research_plan.pdf` via `build/render.sh` (latexmk, xelatex, natbib `\citep`, `naturemag.bst`) | **v2 draft**; body+figure+table ≈ 2.7 pages, references start on page 3 and end on page 4 |
| Figure 1 | `figures/make_fig1.py` → `figures/research_plan_fig1.{svg,pdf,png}` | v2; reproducible |
| Bibliography | `research_plan.bib` (59 entries, DOIs verified 2026-09-21) + `research_plan_refs_notes.md` | done |
| Referees | `references.md` | from Aithyra package; re-check |
| Cover letter / email | `cover_email.md` | to do |
| Institute intelligence | `additional_info/` | done |

Render: `./build/render.sh` (latexmk -xelatex; TNR 11 pt, 2 cm margins, natbib superscript numbers, Nature bst; aux files in `build/latex/`). Prints the page count. The markdown drafts are archived in `build/research_plan_v1.md` and `build/research_plan_v2_source.md`; **edit `research_plan.tex` from now on.** `url`/`note` fields were stripped from the bib so references stay short.

## Research plan — locked decisions (v2, 2026-09-21; supersedes v1)

Blueprint: `build/audit_v2.md` (auditor pass). v1 kept at `build/research_plan_v1.{md,pdf}`.

1. **Title:** "What if, and why: tissue representations one can intervene on, interpret and test". "Test" is bound to Aim 1 by one clause in the opening.
2. **Aim order:** 1 *Gather data and build ground truth* → 2 *Build tissue representations* → 3 *Intervene* → 4 *Interpret*. Data first in text, figure and table; the benchmark is Aim 1's deliverable, not an aim.
3. **Two model families, equals, developed separately** (not one model): decomposable/interpretable by design (KIARA lineage; LIANA/OmniPath vocabulary; prior knowledge optional) and high-capacity/black-box (class of TERRA/Nicheformer/Novae, cited as the class, never as a bar cleared). One first model of each kind (KIARA, Cellina), each developed into a line. Counterfactual requirement stated once for both. No scale claim.
4. **Aim 1 ground truth, three sources:** spatial perturbation screens cited as one unnamed group (Perturb-CAST inside the group only, never named, no DKFZ framing); measured contacts (LIPSTIC/uLIPSTIC, match-seq = the one with a causal layer, CytoSignal PLA ground truth for five LR pairs); LLM-agent-curated validated interactions extending scBaseCount-style curation, extractor benchmarked. No atlas harmonization. TERRA cited once as motivation (112M cells; panels absorbed as a batch token; absent ≠ unexpressed). Moleculent has no publication → not cited.
5. **Aim 3:** node (what neighbours express; parameterized via the LR layer) and edge (which neighbours) perturbations, same interface on both families; TERRA/SpatialProp/MintFlow cited as unvalidated attempts. Banned phrase: "Cellina's validated node perturbations". Safe: "pathway-targeted neighbour perturbations built from prior knowledge recover their responses".
6. **Aim 4, two orthogonal lines:** decomposable models read through their structure (KIARA: global cell-type vs local niche); black-box read post hoc (SAEs + blind LLM description + independent judge). ehrx one sentence. PK-informed SAEs one clause. Bridge rule: an interpretation counts only if steering a feature or zeroing a term changes the Aim 3 counterfactual.
7. **Fit:** CHC via Nicheformer + Open Problems; partners by topic only; CRC anchor; two-step translation. M1 Clinical AI Consultants and the H&E/pathology speculation dropped (auditor call; restore if wanted).
8. **Timeline table:** rows years 1–2 / 2–4 / 4–5, columns in aim order + group size. Funding facts only: MSCA fellowship, named key person on CZI grant (Saeys), ERC StG eligible 2027 on Aims 2–4. Venues sentence folded into the Fit paragraph.
9. **Figure (v2):** perspective-style boxed bands, four aims top-down, tissue-as-graph glyph the only Cellina borrow; two equal family boxes in Aim 2; dashed red steer arrow from Aim 4 to Aim 3; only LIANA/OmniPath named. 14.6 × 9.5 cm at 0.86 textwidth.
10. **Layout:** LaTeX source with `\citep`; body+figure+table ≈ 2.7 pages; references (35 cited of 59 in bib) at 8 pt two columns, starting on page 3.
11. **Voice:** unchanged (first person, future tense with hedges, no slop, signature lines kept).

## Facts to keep straight (from the bib check)

- Perturb-CAST = Breinig et al., *Nat Biomed Eng* 2026, DKFZ; Stegle & Gerstung senior, Heidari third author.
- Cell PII S0092-8674(26)00998-0 = scBaseCount (Youngblut et al., Arc): agentic *curation* of expression data, not an interaction-mining paper.
- SAFFRON (Handa et al. 2026): SAEs on spatial FMs; none beats baselines on local microenvironment. Kendiukhov 2026: SAE features encode co-expression, not causal logic.
- Nicheformer first author Tejada-Lapuerta; TERRA = Birk et al., Lotfollahi senior; Perturb-FISH is *Cell* 2025; CRISPRmap = Gu et al., *Nat Biotechnol* 2025.

- CytoSignal = Liu et al., *Nat Genet* 2026 (Welch lab); ground truth = PLA on adjacent sections, 5 LR pairs, mouse embryo. match-seq = Du et al. (Bassik lab), bioRxiv Sept 2026. Moleculent: no publication as of 2026-09-21.

## Open items

- [ ] Decide whether references count towards the 3 pages. If yes: cut ~0.6 page of text.
- [x] Preprint entries no longer print the DOI twice (`url` stripped where `doi` present).
- [ ] Cover letter; re-check `references.md` trio for Helmholtz; CV referee trio consistency.
- [ ] Numbers to refresh at submission: 300,000 downloads, citations, Cellina venue status.
