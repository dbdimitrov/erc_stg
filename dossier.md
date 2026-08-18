# PI Research Dossier — Daniel Dimitrov

### Grounded revision — single source of truth

*Focused on the decisions taken this cycle and grounded in the candidate's own published framing: the NRG Perspective (Dimitrov & Schrod et al., Nat Rev Genet 2026 — "Interpretation, extrapolation and perturbation of single cells") and the Cellina preprint (Moeed et al. 2026 — "Querying counterfactuals on tissue graphs with supervised disentanglement"). All superseded material removed. Target: ERC Starting Grant, LS panel, 2027 call.*

---

## 0. Locked decisions

1. **Cycle:** ERC-2027-StG (deadline ~Oct 2026). Self-imposed timeline (2027 window is 0–10 yrs post-PhD); optimise what is achievable by the deadline.
2. **Structure:** one causal line, not a demoted aim and not a 50/50 split. The programme is the candidate's own trajectory maturing from **descriptive to causal** models of cell–cell communication (CCC) — his phrase and the opening thesis of the Perspective — grounded in benchmarking rigour, extended toward emerging perturbation/spatial data.
3. **Causal engine:** representations that are **disentangled from confounders and invariant across regimes** (the Perspective's causal-representation-learning framing). A generalist CCC model earns trust **iff** it enables accurate **out-of-distribution (context-transfer) in-silico perturbation** — the Cellina test that "a model that conflates intrinsic and extrinsic variation cannot succeed."
4. **Feasibility floor:** methods work on **existing data** (Cellina runs today on CRC and mouse-brain spatial data). Emerging spatial perturbation screens are upside, not a dependency — and, per Cellina, still lack the resolution, transcriptome-wide readout and matched controls needed as ground truth.
5. **Panel:** LS (genomics / computational biology), decisively → experimental validation anchor is load-bearing; headline is biological discovery in **multicellular, context-dependent communication programmes**, ML is the trusted engine underneath.
6. **Scope:** three aims, one line. No EHR strand, no standalone autointerpretability aim. Interpretability survives only as a property of the model (interpretable/disentangled factors).

## 1. Candidate & target

- **Now:** Postdoc, EMBL Heidelberg. Purely computational.
- **Target:** ERC-2027-StG → independent PI in Europe; LS comp-bio panel (confirm exact code at call publication).
- **Biological target (the class, not a fixed disease):** **multicellular, context-dependent communication programmes** in tissue — the system *type* the method constrains, and the axis on which a validation system should be chosen (see §8/§11). The organ/disease is an instance selected for system-fit, not the scope. Demonstrated instances already in hand: colorectal-cancer and mouse-brain spatial tissue (Cellina); the gut metaplasia atlas (co-author). Candidate system shapes going forward: self-organising organoids, tumour microenvironment, immune/inflammatory niches.
- **One external dependency to start now:** a prospective experimental validation collaborator (§11).

## 2. Bibliometrics (Google Scholar, mid-2026)

Total citations **3,777**; **h-index 13**, **i10-index 16**. Trajectory 76 (2022) → 289 → 826 → 1,458 (2025) → 1,094 (H1 2026). Steep and rising.

## 3. Publication record (author positions verified against the PDFs)

✅ lead · ✳️ co-first / co-corresponding (equal-contribution statement — foreground explicitly) · — co/middle author.

| Paper | Venue / Year | Position | Cites |
|---|---|---|---|
| Comparison of methods for CCC inference | Nat Commun 2022 | ✅ first author | 681 |
| LIANA+ | Nat Cell Biol 2024 | ✅ first author | 285 |
| Interpretation, extrapolation & perturbation of single cells (**the Perspective**) | Nat Rev Genet 2026 | ✳️ **co-first (listed first) + corresponding** | 10 |
| Querying counterfactuals on tissue graphs — **Cellina** | preprint 2026 | ✳️ **last + co-corresponding** (first author: Moeed, supervised student) | — |
| decoupleR | Bioinformatics Adv 2022 | — co-author | 1,082 |
| Best practices for single-cell analysis | Nat Rev Genet 2023 | — co-author | 1,223 |
| Single-cell integration reveals metaplasia in gut diseases | Nature 2024 | — co-author | 112 |
| Multi-omics + prior knowledge (immune) | Nat Immunol 2024 | — 2nd author | 66 |
| Multicellular factor analysis | eLife 2023 | — 3rd author | 57 |
| MetalinksDB | Brief Bioinform 2024 | ✳️ co-first | 30 |
| LIANA + Tensor-cell2cell | Cell Rep Methods 2024 | ✳️ co-first | 29 |
| OmniPath | Nucleic Acids Res 2026 | — co-author | 20 |

**Positioning:** B1 leads on the two refereed first-author flagships (CCC comparison; LIANA+) as the delivered core, with the Perspective as the published conceptual scaffold for the causal line. Leadership and agenda-setting signals — the axis the StG actually evaluates for a pre-lab applicant — are strong here: (a) sole first-author flagships that set a research direction the field adopted; (b) founding and maintaining LIANA/OmniPath with independent, external adoption; (c) supervising a student to first-authorship (Moeed on Cellina) under the candidate's senior authorship; (d) the Perspective as an agenda-setting statement. The forthcoming **LIANA++** (sole corresponding) adds a further senior-author flagship led entirely by the candidate.

## 4. Forthcoming papers (preprints by the deadline)

1. **LIANA++** (multimodal CCC — spatial, multiome) — candidate is last and corresponding. 
2. **Cell-type/niche-specific perturbation effect modelling** — core to Aim 2/3. KIARA.
3. **Cellina** (last + co-corresponding) — the seed of Aim 2; possible venue upgrade, do not assume.

## 5. Data assets

- Multicellular / spatial systems already in hand: colorectal-cancer and mouse-brain spatial data (Cellina); gut metaplasia atlas (co-author) — **core** demonstrated instances of context-dependent programmes (the class matters, not the organ).
- Public perturbation data (Perturb-seq, cytokine/CRISPR co-culture) for OOD context-transfer validation — **core** (enumerate exact sets, §11).

## 6. PI-readiness assets (foreground in CV)

- **Supervision:** 5 PhD, 3 MSc, 2 BSc. Cleanest evidence: **Moeed first-author on Cellina** under the candidate's senior authorship; Atheer's merged `inflow-score` PR in liana-py (directing student work into a released codebase). Elyas under MetalinksDB; 
- **Software adoption (rare, external, hard-to-fake):** LIANA (245 GitHub stars), LIANA+ (309 GitHub stars; PyPI >300k), decoupleR (~471k PyPI; co-author), OmniPath ecosystem. 

---

## 7. Core direction (grounded in the candidate's own framing)

**From descriptive to causal models of cell–cell communication in multicellular, context-dependent programmes — one line.**

The Perspective's thesis is the spine: single-cell analysis is moving from descriptive atlasing to inferring causal effects, and the field's central obstacle is that observational single-cell data yields only "partial views of causality." The candidate is positioned to close this for CCC specifically because he (a) built and maintains the descriptive CCC infrastructure the field uses (LIANA+/OmniPath, real adoption), (b) authored the reference **benchmark** the CCC field trusts, and (c) authored the **Perspective** that laid out the causal-representation route and the **Cellina** method that first instantiates it for tissue counterfactuals.

The causal engine is the Perspective's own prescription: representations **disentangled from confounders and invariant across regimes**, using observational heterogeneity as "natural perturbations" and interventional/spatial data where available. Cellina makes this concrete — supervised disentanglement of **intrinsic** cell identity (z) from **extrinsic** microenvironment (s), enabling **tissue graph counterfactuals** (edge and node perturbations).

The trust argument answers the reception risk the Perspective itself documents — that foundation models are distrusted because simple baselines often match or beat them. The response is not to defend the architecture but to **prove function**: a generalist model that enables accurate **out-of-distribution in-silico perturbation** is trustworthy, exactly as Cellina argues that a model conflating intrinsic and extrinsic variation *cannot* pass the context-transfer test. Counterfactuals are treated **operationally, not in the strict Pearlian sense** (Cellina's own stance) — the honest estimand is stated, not overclaimed.

## 8. Aims (three; one line)

- **Aim 1 — Context-aware causal benchmarks & ground truth for CCC (the trusted core).** Build a context-conditioned benchmark for causal CCC inference from existing perturbation data (Perturb-seq, cytokine/CRISPR co-culture) plus priors (OmniPath), with the biologically-relevant, gene-level metrics Cellina already uses (directional recovery, signed precision) rather than distributional fit alone. Directly extends the benchmarking reputation and answers the Perspective's "reliable ground-truth" gap. *Any literature-mined/LLM ground-truth component is included only if the extractor is itself benchmarked (precision/recall, provenance); otherwise cut (§10.3).*
- **Aim 2 — A generalist, causal CCC model via invariance + disentanglement.** Generalise Cellina from spatial-neighbourhood counterfactuals toward CCC counterfactuals across regimes, using invariance across environments as the identification lever (Perspective) and intrinsic/extrinsic supervised disentanglement as the inductive bias that makes the factorisation identifiable (Cellina, citing Locatello). Trust criterion = accurate **OOD context-transfer** prediction; counterfactuals interpreted operationally. Interpretable factors ride along as a property.
- **Aim 3 — Validation in a multicellular, context-dependent system (chosen for system-fit, not disease).** The target is a *class* of biology — communication programmes among interacting cell types whose behaviour depends on context — so the validation system is selected on fit (§11), not a disease label. Lead with **OOD context-transfer** prediction (the Cellina protocol). Known-biology recovery — e.g. the TGFβ- and NFκB/MAPK-driven fibroblast programmes and FN1/MMP3 already recovered in CRC (Cellina) — is a **sanity check only**, not the headline (a foundation-model sceptic reads "recovers the known" as priors echoing back). Secure **≥1 prospective experimental anchor** in a fitting system — load-bearing for an LS panel. Pre-registered, falsifiable criteria. *Flexible is not arbitrary:* whatever system is chosen, state plainly why cell–cell communication genuinely **drives** that phenotype and why predicting its perturbation response matters — otherwise the biology reads as decoration bolted onto the method.

## 9. Risks (live only)

1. **Preprint dependency.** The causal execution papers are preprints at the deadline; they ride as clearly-labelled preprints while the refereed record (two first-author flagships + the Perspective) carries B1. No implying otherwise.
2. **Foundation-model distrust (LS panel).** The Perspective documents it; disarm by prove-function (OOD), lead-with-discovery, and benchmarking trust — not by adding fashionable ML.

## 10. Open criticisms

### Already answered in the candidate's own work (cite it — this is the credibility argument)

- **Causal estimand honesty.** Cellina already reserves "causal" for operational counterfactuals, explicitly *not* strict Pearlian, and states it does not yet impose identifiability assumptions. Carry this exact stance into the proposal.
- **Disentanglement is not free (Locatello).** Cellina already uses supervised disentanglement as the inductive bias precisely because unsupervised factorisation is not identifiable — the standard ML-referee attack is pre-answered.
- **OOD validation as the trust test.** The context-transfer protocol (held-out cell types / rewired domains) is already the evaluation, with a principled failure mode.
- **Prior-knowledge circularity.** The Perspective already documents priors' bias toward well-studied pathways and that modules often capture indirect effects — awareness is on record.

## 11. Actions

1. **[HIGH] Prospective validation collaborator (Aim 3).** Choose on *system-fit*. A fitting system has: (i) multiple interacting cell types in a tissue/niche/organoid context (not single-cell-intrinsic biology); (ii) a perturbation handle (genetic, chemical, or spatial/neighbourhood); (iii) a single-cell or spatial readout; (iv) conditions/contexts that can be held out for OOD testing. Candidate shapes: self-organising organoids, tumour microenvironment, immune/inflammatory niches. Even a support letter flips the causal aim from computational-only to experimentally anchored; decide before B1: work package vs. letter.
2. Enumerate the exact single-cell/spatial/perturbation datasets for Aims 1–3 (name the sets for whatever system is chosen).
3. Write the estimand sentence (§10.1) and the novelty-delta sentence (§10.4).
4. Prioritise the **LIANA++ preprint** with sole corresponding authorship (strongest leadership flagship in the pipeline).
5. Identify the exact 2027 LS panel + confirmed deadline; start the **Host Institution commitment-letter** process early (the only letter the ERC file needs).
6. Pull live software-adoption numbers with retrieval dates at drafting.