# PI Profile & Research Line — Daniel Dimitrov

*Lookup document for writing group-leader applications (research statements, cover letters, chalk-talk prep). Funding-agnostic — any specific call (ERC or otherwise) instantiates from this. Grounded in the candidate's own published framing: the Perspective (Dimitrov & Schrod et al., Nat Rev Genet — "Interpretation, extrapolation and perturbation of single cells") and Cellina (Moeed et al., preprint — "Querying counterfactuals on tissue graphs with supervised disentanglement"). Full authorship-annotated paper index: [`previouswork.md`](previouswork.md).*

---

## 1. Profile

- **Position:** Postdoc, Oliver Stegle lab — joint **DKFZ Heidelberg (Division B260)** / **EMBL** affiliation. Purely computational.
- **One-line identity:** Built and maintains the descriptive infrastructure and the reference benchmark the cell–cell communication (CCC) field uses; now leading its shift from descriptive to causal models.
- **Citation trajectory:** 76 (2022) → 289 → 826 → 1,458 (2025) → 1,094 (H1 2026). Steep and rising.

### Key numbers (dated — refresh before each application)

| Metric | Value | Retrieved |
|---|---|---|
| Citations (Google Scholar) | 4,000+ | 2026-07-21 |
| h-index / i10-index | 14 / 16 | 2026-07-21 |
| LIANA (R) GitHub stars | 247 | 2026-08-22 |
| liana-py GitHub stars | 310 | 2026-08-22 |
| liana-py PyPI downloads | >300k total (mid-2026); 15.3k last month | 2026-08-22 |
| decoupler-py stars (scverse) / decoupleR (R) stars | 291 / 304 | 2026-08-22 |
| decoupler PyPI downloads (co-author) | ~471k total (mid-2026); 33.3k last month | 2026-08-22 |

Scholar profile: [`dDujacgAAAAJ`](https://scholar.google.com/citations?user=dDujacgAAAAJ&hl=en).

## 2. Publication record

✅ lead · ✳️ co-first / co-corresponding (equal-contribution statement — foreground explicitly) · — co/middle author. Positions verified against the PDFs. Citations: Scholar, 2026-07-21.

| Paper | Venue / Year | Position | Cites |
|---|---|---|---|
| Comparison of methods for CCC inference | Nat Commun 2022 | ✅ first author | 706 |
| LIANA+ | Nat Cell Biol 2024 | ✅ first author | 300 |
| Interpretation, extrapolation & perturbation of single cells (**the Perspective**) | Nat Rev Genet | ✳️ **co-first (listed first) + corresponding** | 22 |
| Querying counterfactuals on tissue graphs — **Cellina** | preprint | ✳️ **last + co-corresponding** (first author: Moeed, supervised student) | — |
| decoupleR | Bioinformatics Adv 2022 | — co-author | 1,154 |
| Best practices for single-cell analysis | Nat Rev Genet 2023 | — co-author | 1,242 |
| Single-cell integration reveals metaplasia in gut diseases | Nature 2024 | — co-author | 115 |
| Multi-omics + prior knowledge (immune) | Nat Immunol 2024 | — 2nd author | 69 |
| Open Problems in single-cell analysis | Nat Biotechnol 2025 | — co-author (CCC task) | 78 |
| Multicellular factor analysis (MOFAcell) | eLife 2023 | — 3rd author | 57 |
| MetalinksDB | Brief Bioinform 2024 | ✳️ co-first | 31 |
| LIANA + Tensor-cell2cell | Cell Rep Methods 2024 | ✳️ co-first | 29 |
| OmniPath | Nucleic Acids Res 2026 | — co-author | 22 |

Earlier and smaller works (BingleSeq, IgA-nephropathy AI perspective, RIDDEN, marine proteomics, CKD pharmacology): see [`previouswork.md`](previouswork.md).

**Leadership signals (the axis committees evaluate for a pre-lab applicant):** (a) sole first-author flagships that set a research direction the field adopted (CCC benchmark; LIANA+); (b) founding and maintaining LIANA/OmniPath-ecosystem tooling with independent, external adoption; (c) supervising a student to first-authorship (Moeed on Cellina) under the candidate's senior authorship; (d) the Perspective as an agenda-setting, corresponding-author statement of the field's direction.

### Forthcoming (state honestly as preprints / in preparation)

1. **LIANA++** (multimodal CCC — spatial, multiome) — last & sole corresponding author.
2. **KIARA** — cell-type/niche-specific perturbation-effect modelling.
3. **Cellina** — preprint available; last + co-corresponding; under venue consideration.

## 3. PI-readiness

- **Supervision:** 5 PhD, 3 MSc, 2 BSc. Cleanest evidence: **Moeed first-author on Cellina** under the candidate's senior authorship; Atheer's merged `inflow-score` PR in liana-py (directing student work into a released codebase); Elyas on MetalinksDB (co-first outcome for the student's project).
- **Software adoption (rare, external, hard-to-fake):** LIANA / liana-py, decoupler, OmniPath ecosystem, MetalinksDB — numbers in §1 table.
- **Community:** Open Problems in Single-Cell Analysis — CCC task contributor; Single-cell Best Practices consortium author.

## 4. CV facts (fill before first application)

- **Invited talks / seminars:** *[fill]*
- **Teaching:** *[fill]*
- **Awards / fellowships:** *[fill]*
- **Peer review / editorial:** *[fill journals; note Open Problems + Best Practices community roles above]*
- **Grants held / co-written:** *[fill]*
- **PhD award date (for eligibility windows):** *[fill]*

## 5. Research line

**From descriptive to causal models of cell–cell communication in multicellular, context-dependent programmes — one line.**

The Perspective's thesis is the spine: single-cell analysis is moving from descriptive atlasing to inferring causal effects, and the field's central obstacle is that observational single-cell data yields only "partial views of causality." The candidate is positioned to close this for CCC specifically because he (a) built and maintains the descriptive CCC infrastructure the field uses (LIANA+/OmniPath, real adoption), (b) authored the reference **benchmark** the CCC field trusts, and (c) authored the **Perspective** that laid out the causal-representation route and the **Cellina** method that first instantiates it for tissue counterfactuals.

### Principles (invariant across any application or call)

1. **One causal line** — the programme is the candidate's own trajectory maturing from descriptive to causal models of CCC; not a portfolio of disconnected methods.
2. **Causal engine:** representations **disentangled from confounders and invariant across regimes** (the Perspective's causal-representation-learning framing). Cellina instantiates it: supervised disentanglement of **intrinsic** cell identity (z) from **extrinsic** microenvironment (s), enabling tissue-graph counterfactuals (edge and node perturbations).
3. **Trust criterion:** a generalist CCC model earns trust **iff** it enables accurate **out-of-distribution (context-transfer) in-silico perturbation** — "a model that conflates intrinsic and extrinsic variation cannot succeed" (Cellina). Prove function, don't defend architecture.
4. **Feasibility floor:** methods work on **existing data** (Cellina runs today on 2.4M-cell CRC and mouse-brain MERFISH data). Emerging spatial perturbation screens are upside, not a dependency.
5. **Estimand honesty:** counterfactuals are treated **operationally, not in the strict Pearlian sense** (Cellina's own stance) — the estimand is stated, never overclaimed.

### Programme (three strands)

- **Strand 1 — Context-aware causal benchmarks & ground truth for CCC (the trusted core).** A context-conditioned benchmark for causal CCC inference from existing perturbation data (Perturb-seq, cytokine/CRISPR co-culture) plus priors (OmniPath), with biologically-relevant gene-level metrics (directional recovery, signed precision) rather than distributional fit alone. Extends the benchmarking reputation; answers the Perspective's "reliable ground-truth" gap. Any literature-mined/LLM ground-truth component is included only if the extractor is itself benchmarked (precision/recall, provenance).
- **Strand 2 — A generalist, causal CCC model via invariance + disentanglement.** Generalise Cellina from spatial-neighbourhood counterfactuals toward CCC counterfactuals across regimes: invariance across environments as the identification lever (Perspective), intrinsic/extrinsic supervised disentanglement as the inductive bias that makes the factorisation identifiable (Cellina, citing Locatello). Trust criterion = accurate OOD context-transfer prediction. Interpretable factors ride along as a property of the model, not a standalone aim.
- **Strand 3 — Validation in a multicellular, context-dependent system, chosen for system-fit, not disease.** The target is a *class* of biology — communication programmes among interacting cell types whose behaviour depends on context. **System-fit criteria:** (i) multiple interacting cell types in a tissue/niche/organoid context; (ii) a perturbation handle (genetic, chemical, or spatial/neighbourhood); (iii) a single-cell or spatial readout; (iv) contexts that can be held out for OOD testing. Candidate shapes: self-organising organoids, tumour microenvironment, immune/inflammatory niches. Lead with OOD context-transfer prediction; known-biology recovery (e.g., the TGFβ- and NFκB/MAPK-driven fibroblast programmes and FN1/MMP3 already recovered in CRC by Cellina) is a sanity check, not the headline. Whatever system is chosen, state plainly why CCC genuinely **drives** that phenotype — otherwise the biology reads as decoration bolted onto the method.

### Long horizon (the "and then what?" — vision layer for lab-trajectory audiences)

1. **Perturbation-guided therapeutic hypothesis generation** in context-dependent systems (e.g., the tumour microenvironment) — the translational continuation once counterfactual predictions are trusted.
2. **Spatial-perturbation screens as they mature** — Cellina itself documents that current screens lack the resolution, transcriptome-wide readout and matched controls needed as ground truth; as that changes, the lab's benchmarks and models are the natural analysis layer.
3. **Trustworthy virtual tissue** — the long-run ambition of generalist models of multicellular systems, explicitly framed as *earned* through the trust criteria of Strands 1–2 (OOD perturbation accuracy), not assumed from scale.

## 6. Two casts — one core, two headline framings

Choose per application. Never blend into a middle version that satisfies neither audience.

- **Biology-first** (life-science institutes, comp-bio departments, LS-type panels): headline is **biological discovery in multicellular, context-dependent communication programmes** — which signals drive tissue behaviour, and what happens when they are perturbed. ML is the trusted engine underneath; benchmarking rigour and experimental anchoring carry credibility.
- **Method-first** (AI-branded institutes, ML-flavoured units): headline is **causal representation learning and counterfactual inference on tissue graphs** — disentanglement with identifiability via supervision, invariance across environments, OOD generalisation as the evaluation. CCC and tissue biology are the driving application; the benchmarking record is the evaluation culture the lab brings to a field that lacks it.

## 7. Reusable text blocks

### Short bio (~100 words)

> Daniel Dimitrov is a computational biologist working on cell–cell communication (CCC) in multicellular systems. He authored the reference benchmark for CCC inference (Nat Commun 2022) and built LIANA+ (Nat Cell Biol 2024), a widely adopted framework for decoding inter- and intracellular signalling from single-cell and spatial data. His current work moves the field from descriptive to causal models: he co-authored the Nature Reviews Genetics perspective charting this shift and senior-authored Cellina, a method for querying counterfactuals on tissue graphs via supervised disentanglement. He is a postdoc in Oliver Stegle's group (DKFZ/EMBL Heidelberg), with 4,000+ citations and software used across the single-cell community.

### Vision paragraph — biology-first cast

> Tissues work through communication: programmes of signalling among interacting cell types that depend on context — the niche, the neighbours, the disease state. My lab will move the study of these programmes from description to causation. Building on the benchmark and infrastructure my work established for communication inference, we will develop models that predict what a cell would do if its microenvironment were changed — and hold ourselves to the hardest test: accurate prediction in contexts the model has never seen, validated prospectively in a system where communication demonstrably drives the phenotype. The outcome is a principled way to ask "which signal, delivered where, changes tissue behaviour?" — the question underlying regeneration, tumour–microenvironment interactions, and inflammation.

### Vision paragraph — method-first cast

> Perturbation-effect models today assume shared stimuli applied uniformly to i.i.d. cells — an assumption tissues violate by construction, since every cell's state is shaped by a unique local neighbourhood. My lab will build the causal representation-learning stack for this setting: supervised disentanglement of intrinsic cell identity from extrinsic microenvironment to make the factorisation identifiable, invariance across environments as the identification lever, and counterfactual queries on tissue graphs as the interface. Trust is earned operationally — a model qualifies only if it predicts perturbation responses out-of-distribution, across held-out contexts — and evaluated against context-conditioned causal benchmarks the lab builds, extending the benchmarking rigour my work is known for to the causal setting.

### Estimand sentence

> We use "counterfactual" operationally, not in the strict Pearlian sense: the estimand is the predicted change in a cell's expression under a defined intervention on its tissue context — rewiring its neighbourhood (edge perturbation) or altering neighbour gene programmes (node perturbation) — evaluated by out-of-distribution context transfer, without claiming identification of unit-level counterfactuals.

### Novelty-delta sentence

> Existing perturbation models assume shared stimuli applied uniformly to i.i.d. cells; our delta is to model each cell's response as a function of its unique local neighbourhood — disentangling intrinsic identity from extrinsic context so that communication-mediated perturbation effects transfer to unseen tissue contexts, a setting no current CCC or perturbation framework addresses.

### Skeptic defenses (pre-answered in the candidate's own work — cite it)

- **"Is this really causal?"** — Cellina already reserves "causal" for operational counterfactuals, explicitly *not* strict Pearlian, and states it does not yet impose identifiability assumptions. Carry this exact stance; the honesty *is* the credibility argument.
- **"Disentanglement is not identifiable (Locatello)."** — Pre-answered: Cellina uses *supervised* disentanglement as the inductive bias precisely because unsupervised factorisation is not identifiable.
- **"Why trust a generalist model? Simple baselines match foundation models."** — The Perspective documents this distrust itself. The response is prove-function: OOD context-transfer prediction as the qualifying test, with a principled failure mode (a model conflating intrinsic and extrinsic variation cannot pass). Cellina already beats spatially-informed (MintFlow, SpatialProp, SIMVI) and non-spatial (scGen, CPA) baselines on this protocol.
- **"Prior knowledge is circular / biased to well-studied pathways."** — The Perspective documents priors' bias and that modules often capture indirect effects; awareness is on record, and Strand 1 benchmarks extractors rather than assuming them.
- **"Recovering known biology just echoes the priors."** — Agreed, and stated as such: known-biology recovery (TGFβ/NFκB-MAPK fibroblast programmes, FN1/MMP3 in CRC) is a sanity check; the headline evidence is OOD prediction.
