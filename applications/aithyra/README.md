# AITHYRA AI/ML Starting PI — application package

*Target: the **next** AI/ML Starting PI round (expected ~spring 2027 — the last round closed 30 April 2026 and is in review). Submission: application@aithyra.at, subject line "AITHYRA AI/ML PI". Posting: [aithyra.at — Become an AI/ML Starting Principal Investigator](https://aithyra.at/about/open-positions/become-an-ai-ml-starting-principal-investigator-at-aithyra). Offer terms: €700k/year, 5+4 years, rolling tenure possible after year nine.*

## Package map (posting requirement → file)

| # | Requirement (verbatim from posting) | File | Limit |
|---|---|---|---|
| 1 | Curriculum Vitae with full publication list and ORCID | `../../DanielDimitrov_GenericCV.docx` + [`cv_facts.md`](../../cv_facts.md) | — *(add ORCID id to CV header)* |
| 2 | "list of up to 3 most important papers with a short comment including specification of your contributions (each max. 100 words)" | [`publication_summary.md`](publication_summary.md) | ≤100 words per comment |
| 3 | "Funding plans including funding record; max. 1 page in total" | [`funding_plans.md`](funding_plans.md) | 1 page |
| 4 | "names and addresses of three references" | [`references.md`](references.md) | — |
| 5 | Research statement "including statements on (i) how your research interfaces with/benefits from AI and (ii) how your research could be scaled/what is achievable through scaling (max. 3 pages)" | [`research_statement.md`](research_statement.md) | 3 pages |
| — | Cover email (not required; good practice) | [`cover_email.md`](cover_email.md) | short |

## Locked decisions (2026-08-22, with the candidate; superseded entries struck)

1. **Dating:** every claim truthful as of drafting (Aug 2026); date-sensitive lines carry **[refresh]** flags to upgrade at submission.
2. **Third paper slot: Cellina** (arXiv preprint; last + co-corresponding; student first author). ~~Initially NRG Perspective~~ — superseded in round 1 (see "Decisions resolved" below); the Perspective stays foregrounded in the statement (always "co-first listed first + **co-corresponding**"). Slots 1–2: CCC benchmark (Nat Commun 2022), LIANA+ (Nat Cell Biol 2024).
3. **Referees: Saez-Rodriguez · Stegle · Saeys.** ~~Initially Valdeolivas~~ — superseded in round 1; Valdeolivas optional fourth (adoption witness).
4. **Cast:** full method-first (dossier §6) — causal representation learning + counterfactual inference on tissue graphs; never blended with the biology-first cast. **Evaluation + infrastructure is the package through-line** (candidate directive).

## Refresh checklist (run when the 2027 call opens)

- [ ] Confirm the new deadline and that the required documents/format are unchanged.
- [ ] Re-verify all AITHYRA institution facts against the live posting (priority areas, directors, existing-group descriptions, email/subject).
- [ ] Refresh all metrics (citations, h-index, downloads, stars) from dossier §1.
- [ ] Pipeline upgrades: KIARA (in prep → preprint?), Cellina (preprint → accepted?), ehrx status, inflowflex status.
- [ ] Resolve all **[refresh]** / *[confirm]* / *[fill]* flags. **Hard pre-render gate:** `grep -n '\[refresh\|\[fill\|\[confirm\|\[verify\|\[pending' *.md` must return empty; strip all HTML comments and italic meta-lines.
- [x] ORCID: **0000-0002-5197-2112** (verified vs saezlab/liana DESCRIPTION + NCB record) — in cover email; add to CV header.
- [ ] CV: confirm full publication list present; **align the CV's own reference trio to Saez-Rodriguez/Stegle/Saeys** (the generic CV still ends in Valdeolivas — a mismatched referee #3 across documents is an easy committee catch); export CV + all documents to PDF and verify the statement renders ≤3 pages at 11 pt.
- [ ] Externally verify funding-programme facts (FWF ASTRA terms, WWTF calls, CZI EOSS status) — funder websites, not memory.
- [ ] Referee heads-up emails sent; confirm titles/addresses (references.md flags).
- [ ] NRG Perspective citation convention: using *Nat Rev Genet* 27, 349–370 (2026; online 2025) — keep consistent across CV/summary/statement.

## Verified source facts (don't re-litigate)

- Nat Commun 2022 contributions (published statement): J.S.R. conceived; D.D. set up the framework, performed the comparisons and evaluations (with support), guided the robustness analysis; all authors contributed to the manuscript. **Never write "I conceived" for this paper.**
- NCB 2024 contributions (verified from PDF): "D.D. and J.S.R. conceived the project. D.D. developed the software, carried out the case studies and drafted the manuscript."
- NRG Perspective has **three co-corresponding authors** (Dimitrov, Schrod, Stegle) → always "co-corresponding".
- Cellina (verified vs preprint): Pearson 0.85 (Cellina-GAT) vs 0.51 mean-shift, signed precision 0.40, +0.14/+0.17 over strongest baseline; SIMVI excluded from counterfactual evals (disentanglement-only comparison); SpatialProp is the node-perturbation comparator; per-section models on the ~2.4M-cell CRC cohort. **Note: dossier §7 has the loose "MintFlow, SpatialProp, SIMVI" grouping — flag to the dossier's owner.**
- Secondments: Ghent University Hospital (Glorieux lab) + EMBL (Zeller group) — **not** VIB.
- MSCA: STRATEGY-CKD, Horizon 2020 grant 860329 (verified via Nat Commun acknowledgements).

## Decisions resolved with the candidate (2026-08-22, round 1)

1. **Paper slot 3 → Cellina** (public arXiv preprint; the only citable artifact showing both a causal method and PI-mode supervision). NRG Perspective stays foregrounded in the research statement.
2. **Referee 3 → Yvan Saeys** (senior independent academic, funded CZI partner). Valdeolivas kept as optional fourth/informal. Confirm with Saeys before submission.
3. **Strand-3 commitments kept as drafted:** plate-based organoid/co-culture as lead system; costed wet-lab line (~€100–150k/yr consumables + wet-lab postdoc + shared technician from core funds).
4. **Candidate directive:** *evaluation + infrastructure is THE unique angle* — "something all the other PIs there and AI people are lacking." It is now the package's through-line (summary, (i), Why AITHYRA, cover email), not just a closing argument.

## Review log

| Round | Reviewers | Outcome |
|---|---|---|
| 1 | HR/compliance · ML director · LS director · search committee · fact-checker | HR: PASS WITH FIXES (ORCID, ref-3 address, flag gate). ML: BORDERLINE — hire only as "the evaluation person"; fix causal-language discipline, checkbox priority areas, complementarity, DML name-drop, venue promise. LS: BORDERLINE→shortlistable — SIMVI overclaim (fixed), no mechanism in "communication" models (fixed: LR-parameterised interventions), trust-criterion genotype confound (fixed: isogenic control arms), unfunded Strand 3 (fixed: costed line), loop slideware at spatial cycle times (fixed: plate-based loop + simulator-first). Committee: BORDERLINE leaning shortlist if Cellina visibly public — fixed wording; slot-3 + referee-3 decisions raised. Fact-check: 2 WRONG (conception claim, VIB) + 5 OVERCLAIMED (incl. SIMVI, co-corresponding) — all corrected in v2; contribution sentences now mirror published statements. |
| 2 | Fresh ML director · fresh LS director · fresh search committee · delta fact-checker (on v3) | **ML: SHORTLIST** ("fills the one competency the current roster lacks"; require Cellina ML-venue submission + KIARA preprint by the visit). **LS: SHORTLIST** conditioned on methods/evaluation-first remit (found the Fig-3b genotype-held-fixed control we now foreground; flipped the loop to gain-of-function dosing; named the k=1 sparse-intervention gap). **Committee: SHORTLIST, contested** (caught the ERC-window error → fixed to 2027–2031 incl. cv_facts.md; forced internal notes into HTML comments). **Fact-check: 0 wrong / 0 overclaimed** across 27 delta checks. All accepted fixes applied in v4. |
| 3 | Single pre-flight verifier: compliance + cross-document consistency + fact-check on v4 | **GO after fixes** (all applied in v5): all 10 fact-checks OK; consistency clean except stale README entries (fixed); referee addresses were trapped inside strip-gated flags (promoted in-band); statement trimmed to ~1,810 words (verify the 3-page render before submission); "supervision providing identifiability" softened to the dossier's precise phrasing; "validated" → "tested in silico" for the pathway-vector direction. Interview-defence note kept: the "same genotype" gloss on the subdomain control is patient-level — intratumoural subclonality is not formally excluded. |

## Pre-submission / pre-interview actions for the candidate (from the panels — real-world, not document edits)

1. **KIARA preprint must be public before applying** (both ML passes: non-negotiable; converts the biggest CRITICAL). On plan: Q1 2027 preprint vs ~spring 2027 deadline — tight; protect that timeline.
2. **Submit an ML-venue paper before interviews**: the counterfactual-evaluation protocol as a NeurIPS Datasets & Benchmarks-track contribution is the panel-suggested fit; alternatively Cellina/identifiability to an ICLR-class venue.
3. **Confirm Saeys** will write; longer-term, cultivate one senior *no-shared-funding* adopter referee for the interview stage.
4. **Fill the Cellina arXiv ID** everywhere ("a preprint cited without an ID reads as unposted").
5. **Research to-do that pre-empts the killer interview question:** measure Cellina at k=1–10 single-ligand, prior-specified node perturbations (the sparse regime experiments live in; the paper's own k-sweep degrades toward it). Even a negative number, owned, beats being caught without one.
6. **Interview-prep bank** (from the simulated panels): identifiability theorem + assumptions + what supervision buys over a conditional VAE; KIARA first-stage-misspecification negative control; acquisition function + cost/cycle-time/batch-size of one loop round; who conceived the causal agenda (independence from Stegle); which Cellina design decisions were the candidate's; why GOF dosing before KO (ligand redundancy); MintFlow's in-domain advantage (under-claimed ammo); PROGENy circularity = "sanity check", never "recovers known biology".
7. **Drafted plan-numbers to sanity-check with the candidate:** escalation gate "e.g., top-10 signed precision ≥ 0.5"; steady-state group composition (~4 comp + wet-lab postdoc + technician + RSE time); €100–150k/yr consumables; several dosing rounds/year; lead phenotype = ligand-driven fibroblast programme activation (TGFβ/NFκB axes).
