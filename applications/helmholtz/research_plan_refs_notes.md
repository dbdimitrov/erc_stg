# Reference notes — `research_plan.bib`

Companion to `research_plan.bib` for the 3-page research plan **"Interpretable and Intervenable Tissue Representations"** (PI application, Helmholtz Munich).

Each entry: **key** — what the paper actually does (from its abstract/record) — *where I might cite it*.

Verification status: every DOI in the `.bib` was resolved against the Crossref REST API and title/journal/year/first-author checked against the record; every arXiv ID was resolved against the arXiv API. Entries with **no** DOI or arXiv ID are marked `% UNVERIFIED` in the `.bib` and flagged below. Verified 2026-09-21.

---

## A. Spatial / tissue foundation models and representations

- **`blampey2025novae`** — Graph-based foundation model trained on ~30M cells across 18 tissues; zero-shot spatial-domain inference across gene panels, tissues and technologies, native batch correction, nested domain hierarchy. *Opening paragraph: the current generation of spatial representation learners — and the reference model that SAFFRON shows is best-in-class on global gradients but not local niches.*
- **`tejadalapuerta2025nicheformer`** — Transformer pretrained on SpatialCorpus-110M (57M dissociated + 53M spatial cells, 73 tissues); learns spatially aware cell representations and transfers spatial context onto dissociated scRNA-seq. *Same paragraph; the Theis/Helmholtz in-house precedent, useful for showing fit with Helmholtz Munich.*
- **`birk2026terra`** — Spatial-transcriptomics foundation model trained on 112M human cells; one backbone gives cell-, gene- and neighbourhood-scale embeddings and supports zero-shot in-silico spatial perturbation on unseen tissues. *State of the art for "one backbone, many scales" — and the closest existing competitor on the intervention axis, so cite it where I argue that zero-shot perturbation in these models is asserted rather than validated.*
- **`wenckstern2026virtues`** — Virtual Tissues foundation model for spatial *proteomics*: marker-aware multi-scale representations of proteins, cells, niches and tissues from multiplex imaging; zero-shot annotation across panels, TNBC biomarkers predicting anti-PD-L1 response and survival. *Cite for modality breadth (proteomics, not only transcriptomics) and as the clearest existing link from tissue representations to a clinical decision.*
- **`cui2024scgpt`** — Generative pretrained transformer on >33M cells; transfer learning for annotation, integration, perturbation-response prediction and GRN inference. *Background on single-cell FMs; also the substrate for the SAE work in section D.*
- **`theodoris2023geneformer`** — Context-aware attention model pretrained on ~30M transcriptomes; encodes network hierarchy in attention, boosts limited-data tasks, nominates cardiomyopathy targets. *Same; the canonical "interpretability via attention" claim I want to contrast with SAE-based interpretability.*
- **`hao2024scfoundation`** — 100M-parameter model over ~20,000 genes, pretrained on >50M human cells with an asymmetric transformer; SOTA on expression enhancement, drug response, perturbation prediction, annotation, gene modules. *Optional scale citation alongside scGPT/Geneformer.*
- **`zeng2025cellfm`** — 800M-parameter model on 100M human cells (RetNet backbone); reports gains on annotation, perturbation prediction and gene-function prediction. *Optional; use only if I need a second scale data point.*
- **`ahlmanneltze2025linear`** — Compares five foundation models and two other deep models against deliberately simple baselines for single and double perturbation effects: **none beat the baselines**. *The load-bearing critique. Cite in the motivation: scale alone has not bought extrapolation, which is why I propose interpretability and intervention as the design targets rather than parameter count.*
- **`bendidi2024benchmarking`** — Evaluation framework for transcriptomics deep learning on perturbation data; scVI and plain PCA outperform existing transcriptomics FMs on real-world perturbation analysis. *Supporting citation to the same point, from the ML side.*
- **`wu2024perturbench`** — Benchmarking platform with curated perturbation datasets and metrics; no architecture clearly wins, simple architectures are competitive, widely used models show mode collapse. *Same point; also a concrete benchmark I can commit to evaluating against.*

## B. Perturbation modelling

- **`dimitrov2026interpretation`** — My own perspective; dual first author with S. Schrod (Dimitrov†, Schrod†, Rohbeck, Stegle). Organises ML methods for inferring causal effects and extrapolating perturbation responses in single-cell data by modelling concept, and proposes a unifying ontology. *Cite as the conceptual frame for the whole plan — the argument that current models give only partial views of causality because microenvironment is unmeasured and unmodelled.*
- **`moeed2026cellina`** — **Cellina**: formalises tissue-graph counterfactuals as node (neighbour expression) and edge (rewiring) interventions, and learns disentangled intrinsic vs. extrinsic cell representations with biological supervision; benchmarked on >2.5M cells, the only method consistently beating spatially uninformed baselines. *My own preliminary result — last and co-corresponding author (with O. Stegle), first-authored by a PhD student under my day-to-day supervision — and the direct launchpad for Aim 1 — the proof that intervenable tissue representations are tractable.*
- **`lotfollahi2023cpa`** — Compositional perturbation autoencoder predicting responses to unseen dosages, cell types, time points, species and drug combinations; imputes 97.6% of missing combinations in a genetic-interaction screen. *Related work: compositional/latent-arithmetic perturbation models on dissociated data.*
- **`roohani2024gears`** — Couples deep learning with a gene–gene knowledge graph to predict responses to unseen multigene perturbations; 40% higher precision on genetic-interaction subtypes. *Same paragraph; the knowledge-graph-prior branch.*
- **`piran2024biolord`** — Deep generative disentanglement of single-cell data into known and unknown attributes, generating experimentally inaccessible states by virtual shifts. *Direct methodological ancestor of the supervised-disentanglement inductive bias in Cellina.*
- **`boyeau2025mrvi`** — MrVI: deep generative model for cohort-scale studies that stratifies samples and quantifies molecular differences without predefined cell states; finds clinically relevant strata in COVID-19 and IBD. *Cite where I argue that patient/sample-level structure must be part of a tissue representation, not a post-hoc covariate.*
- **`bereket2023samsvae`** — Models a perturbed sample's latent as a sample-specific latent plus sparse global intervention effects; compositional, disentangled, interpretable, strong on low-resource combinatorial reasoning. *Related work on sparse, mechanism-level latent interventions — the closest prior in spirit to combining sparsity with intervenability.*
- **`sun2025spatialprop`** — GNN framework predicting effects of multi-gene, multi-cell-type perturbations across whole tissue sections from natural microenvironment heterogeneity; introduces CausalInteractionBench. *Key competing method for Aim 1, and a ready-made causal benchmark I can evaluate against.*
- **`akbarnejad2025mintflow`** — Flow-matching model disentangling intrinsic from microenvironment-induced expression without priors or predefined domains; enables in-silico microenvironment perturbation. *Competing method; also the Lotfollahi-lab counterpart to TERRA, so cite the pair together.*
- **`dong2025simvi`** — Annotation-free disentanglement of cell-intrinsic vs. spatially induced latent variables with identifiability theory, enabling single-cell-resolution spatial-effect estimates. *The theoretical grounding for intrinsic/extrinsic disentanglement — cite where I justify identifiability.*
- **`wu2023graphvci`** — Graph variational causal inference predicting counterfactual expression under unreceived perturbations, refining the GRN during pretraining. *Related work on counterfactual formulations; useful to show the counterfactual framing predates spatial and I am extending it to tissue graphs.*

## C. Spatial perturbation screens (in vivo / in situ CRISPR)

- **`dhainaut2022perturbmap`** — Perturb-map: parallel knockouts read out in situ by protein barcodes in mouse lung tumours, scoring growth, histopathology and immune composition per knockout; Tgfbr2 loss yields a T-cell-excluded state. *The founding interventional-spatial dataset type; cite where I state that ground-truth spatial interventions now exist.*
- **`gu2025crisprmap`** — Optical pooled screen reading guide barcodes in situ by combinatorial oligo hybridisation, combined with multiplexed IF and RNA detection; works in primary cells, iPSC-derived neurons and tissue. *Second readout modality; cite in the data-availability paragraph.*
- **`breinig2026perturbcast`** — **PERTURB-CAST** (+ CHOCOLAT-G2P): RNA-templated-ligation probes let perturbation identity and transcriptome-wide phenotype be read from the same Visium section, applied to higher-order combinatorial perturbations in autochthonous mosaic liver tumours. *Strongest local tie-in: Heidelberg/DKFZ, Stegle and Gerstung co-authors — cite as a collaboration-ready in vivo interventional resource. Note the method name is not in the title.*
- **`binan2025perturbfish`** — Perturb-FISH: imaging spatial transcriptomics with parallel optical detection of amplified guides; recovers Perturb-seq-consistent intracellular effects and finds density-dependent *intercellular* regulation of innate immunity, with a calcium functional readout. *The single best evidence that neighbourhood context changes perturbation outcome — cite directly under the intervenability aim.*
- **`baysoy2026perturbdbit`** — Perturb-DBiT: co-sequences spatial whole transcriptomes and sgRNAs on the same section; 80,000+ sgRNA panels across tumour colonies, linking perturbations to clonal dynamics and immune infiltration. *Scale argument for training interventional spatial models.*
- **`saunders2025perturbmulti`** — Perturb-Multimodal: paired imaging (RCA-MERFISH) and sequencing readout of pooled perturbations in intact tissue; hundreds of perturbations in mouse liver dissecting zonation, UPR and steatosis. *Multimodal readout; cite alongside Perturb-FISH.*
- **`shen2026spatialperturbseq`** — Spatial perturb-seq: in vivo CRISPR screening compatible with sequencing- and probe-based platforms (Stereo-seq and Xenium implemented); resolves cell-autonomous vs. microenvironmental knockout effects in mouse brain. *The Xenium-era example; cite where I say the readout technology is no longer the bottleneck.*
- **`hu2025space`** — SPACE (preprint): multimodal spatial CRISPR screening with ~18,000-gene whole-transcriptome plus ~68 protein markers at subcellular resolution; 43 knockouts across ~100,000 cells in CAF–tumour spheroids. *Optional; use only if I want a 3D/organoid data point. Platform not stated in the abstract.*
- **`pitino2025stamp`** — STAMP: immobilises suspension cells onto imaging slides so imaging platforms replace sequencing for single-cell genomics at scale (10.9M cells, >6B transcripts), RNA + protein + H&E. *Not itself a spatial screen — cite only for throughput economics of imaging-based perturbation studies.*

## D. Interpretability / autointerpretability

- **`bills2023neurons`** — `% UNVERIFIED` (web article, no DOI/arXiv ID; URL confirmed live). Uses a language model to generate and score natural-language explanations of individual neurons in another language model. *Cite as the origin of autointerpretability, in the cross-domain precedent sentence.*
- **`bricken2023monosemanticity`** — `% UNVERIFIED` (Transformer Circuits Thread, no DOI/arXiv ID; author list from the publisher's own BibTeX). Trains a sparse autoencoder on a one-layer transformer's MLP activations; dictionary features are far more monosemantic than raw neurons. *Cite as the methodological template I import: superposition motivates sparse dictionaries, not neuron-level reading.*
- **`templeton2024scaling`** — `% UNVERIFIED` (Transformer Circuits Thread, no DOI/arXiv ID). Scales SAE dictionary learning to a production model, extracting millions of interpretable, causally steerable features including abstract and safety-relevant concepts. *Cite for the key property I want in tissue models: features that are both readable **and** steerable — interpretability and intervenability are the same object.*
- **`paulo2025autointerp`** — Open-source pipeline using LLMs to explain SAE latents at scale, plus five cheaper scoring methods including intervention scoring. *Cite for the automated-evaluation half: how I would score thousands of tissue features without hand annotation.*
- **`pedrocchi2025saescfm`** — SAEs on scGPT, scFoundation and Geneformer hidden states; features capture biological *and* batch signal and can be intervened on — suppressing batch features improves integration, activating drug features steers control cells dose-dependently. *The nearest existing work to Aim 2; cite as proof of concept on dissociated FMs and as the gap I extend to spatial.*
- **`kendiukhov2026celltype`** — SAEs on residual-stream activations across all 12 scGPT layers; biological FMs need far stronger L1 regularisation than LMs, and later-layer features recover cell-type-aligned gene programs. *Practical citation for the training-regime difference between biological and language SAEs.*
- **`kendiukhov2026atlas`** — TopK SAE atlases of Geneformer V2-316M and scGPT (82,525 and 24,527 features); 99.8% invisible to SVD, 29–59% annotate to GO/KEGG/Reactome/TRRUST, but representations encode co-expression rather than causal regulatory logic. *Cite for the negative result that motivates the plan: interpretable ≠ causal, so interpretability must be paired with intervention.*
- **`simon2025interplm`** — InterPLM: SAEs on ESM-2 embeddings recover thousands of interpretable features (binding sites, motifs, domains) that neurons do not align with; adds LLM-based feature description, missing-annotation recovery and steered generation. *The cross-domain analogue in biology — cite as evidence the recipe transfers from language to biological sequence, and therefore plausibly to tissue.*
- **`handa2026saffron`** — SAFFRON: Matryoshka SAE decomposing spatial foundation model embeddings into interpretable features, benchmarking local microenvironment vs. global spatial-gradient variation; Novae learns global gradients better than naive baselines but **no SFM beats baselines on local microenvironment patterns**. *The single most important citation for Aim 2: SAEs already work on spatial models, and their verdict is that local niche structure is unlearned — exactly the gap my programme targets.*
- **`le2024pathologysae`** — SAE on a pathology foundation model's embeddings, yielding features for distinct biological characteristics, geometric structure and acquisition artifacts. *Optional; cite if I want an imaging-modality precedent alongside InterPLM.*
- **`shmatko2025delphi`** — Delphi-2M: GPT-style generative model of competing disease progression trained on 0.4M UK Biobank participants, externally validated on 1.9M Danes, predicting rates of >1,000 diseases and generating synthetic 20-year trajectories. *Cite in the clinical-translation paragraph: what a generative foundation model looks like when it is used for decisions, as the destination for tissue representations.*
- **`steinberg2024motor`** — Self-supervised time-to-event foundation model pretrained on timestamped EHR/claims sequences; handles censoring natively and transfers with far less labelled data. *Same paragraph; the label-efficiency argument.*
- **`gadd2026survivehr`** — Competing-risk generative transformer on 7.6B coded events from 23M UK primary-care patients; calibrated risk stratification over diagnoses, investigations, medications and mortality. *Same paragraph; the scale data point for EHR FMs.*

## E. Benchmarking / community

- **`luecken2025openproblems`** — Defines and benchmarks open problems in single-cell analysis (the Open Problems community effort). I am a co-author and led the design of the cell–cell communication task. *Cite in the evaluation section as the community infrastructure I would contribute spatial-perturbation tasks to. Note: PubMed carries no abstract for this record, so the summary is from title and my own involvement.*
- **`youngblut2026scbasecount`** — scBaseCount: an **AI-agent-curated**, standardized, auto-updated single-cell data repository (Arc Institute) — LLM agents scrape SRA, infer metadata and reprocess raw reads into uniformly processed count matrices that refresh continuously. *This is the paper behind the Cell PII I was given. Cite where I argue that benchmark-data curation itself should be agentic and continuously refreshed, rather than a frozen one-off release.*
- **`heumos2023bestpractices`** — Reviews independent benchmarking studies across unimodal and multimodal single-cell analysis and recommends best-practice pipelines per modality. I co-authored the cell–cell communication recommendations. *Cite for the evaluation-first culture I bring, and as evidence of community standing.*

## F. Applicant's own work

- **`dimitrov2022comparison`** — Systematic comparison of 16 cell–cell communication resources and 7 inference methods, showing predictions depend strongly on both choices, agreement between methods is low, and no method is robustly supported by independent spatial or cytokine data. *Track record: the benchmark that exposed the field's limitations and seeded LIANA.*
- **`dimitrov2024lianaplus`** — LIANA+: scalable framework unifying and extending ligand–receptor methods to decode inter- and intracellular signalling across single-cell, spatial and multi-omic data and across conditions. *Track record: the software line and the descriptive baseline my programme moves beyond, from summaries of communication to representations that can be queried.*
- **`baghdassarian2024liana`** — Protocol (Python and R) combining LIANA with Tensor-cell2cell to decompose communication into coordinated programmes across many samples. *Track record: cross-condition representation of communication; co-first author.*
- **`farr2024metalinksdb`** — MetalinksDB: knowledge graph of metabolite–protein interactions, an order of magnitude larger than existing metabolite–receptor resources and tunable to disease, pathway and tissue context. *Track record: prior-knowledge layer that supplies the biological supervision signal for disentanglement; co-first author.*
- **`turei2021omnipath`** — OmniPath: integrates >100 resources on inter- and intracellular signalling, transcriptional and post-transcriptional regulation plus annotations into one human knowledge resource. *Cite as the prior-knowledge substrate underpinning both LIANA+ and the supervised-disentanglement approach.*

---

## Summary of verification status

**52 entries. 49 fully verified** against a resolving DOI or arXiv ID.

**3 marked `% UNVERIFIED`** — all three are web-only publications for which no DOI or arXiv ID exists, not cases of doubtful provenance. Their URLs and author lists were read from the live pages (the two Anthropic entries from the publisher's own embedded BibTeX):

- `bills2023neurons`
- `bricken2023monosemanticity`
- `templeton2024scaling`

Partial gaps inside otherwise verified entries:

- `birk2026terra`, `sun2025spatialprop`, `handa2026saffron` use bioRxiv's newer `10.64898` DOI prefix rather than `10.1101`. All three resolve in Crossref; the prefix is not an error.
- `birk2026terra`, `akbarnejad2025mintflow`, `hu2025space` carry a trailing `and others` (large consortium author lists; senior authors are kept explicit ahead of it so BibTeX does not truncate them). `luecken2025openproblems` and `heumos2023bestpractices` had an unnamed consortium placeholder mid-list in the source record; it was dropped rather than rendered as `and others`, which would have truncated every author after it. No consortium names were invented.
- `baysoy2026perturbdbit` has no volume/issue/pages assigned yet (online 11 June 2026).
- `luecken2025openproblems` has no abstract in PubMed; its summary line comes from the title and the applicant's own involvement.

## Corrections to assumptions in the original reference list

1. **Nicheformer's published first author is Tejada-Lapuerta A., not Schaar A.C.** (Schaar is first on the 2024 bioRxiv preprint, second in Nature Methods). Key is `tejadalapuerta2025nicheformer`.
2. **The Ahlmann-Eltze/Huber/Anders title is "Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines."** There is no paper called "Simple linear baselines match deep perturbation models."
3. **VirTues is now two artifacts with different titles**: Nature 2026 ("The Virtual Tissues foundation model resolves spatial proteomics across scales") and arXiv:2501.06039 ("AI-powered virtual tissues…"). The `.bib` cites the Nature version with the preprint in a note. The ICLR 2025 appearance was an MLGenX *workshop* spotlight, not the main conference.
4. **The NRG perspective is titled "Interpretation, extrapolation and perturbation of single cells"**, with exactly four authors (Dimitrov, Schrod, Rohbeck, Stegle). Volume 27, issue 5, pages 349–370 confirmed.
5. **MrVI is Nature Methods 2025, not 2024**; "multi-resolution variational inference" is the model name, not the title.
6. **There is no 2025 preprint named "CRISPR-map."** The spatial method is Gu et al., *Nature Biotechnology* 43(7):1101–1115 (2025), "CRISPRmap". (An unrelated 2013 *Nucleic Acids Research* tool also carries the name.)
7. **Perturb-CAST exists but the attribution was wrong.** It is Breinig et al., *Nature Biomedical Engineering* 10(1):125–143 (2026) — DKFZ/Heidelberg, with Stegle and Gerstung as senior authors and **Elyas Heidari as third author**, not first, and not Robinson lab Zurich. The method name appears only in the abstract, not the title.
8. **Perturb-FISH is *Cell* 2025, not Nature Biotechnology.** The Nat Rev Genet 2025 item under Binan's name is a two-page research highlight, not the method paper.
9. **Perturb-Multi is published**: Saunders et al., "Perturb-Multimodal", *Cell* 188(17):4790–4809.e22 (2025), Zhuang and Weissman labs.
10. **The Cell PII S0092-8674(26)00998-0 resolves to scBaseCount** (Youngblut et al., *Cell* 189(19):5932–5944.e6, 2026, doi:10.1016/j.cell.2026.08.025) — an AI-agent-curated, auto-updating single-cell data repository from the Arc Institute, not a benchmarking-methodology paper as such.
11. **SpatialProp and MintFlow both exist**, but as preprints only (bioRxiv); MintFlow is not indexed in PubMed.
12. **SAFFRON (Handa et al. 2026) is the direct precedent for Aim 2** — sparse autoencoders applied to spatial transcriptomics foundation models, concluding that no SFM beats naive baselines on local microenvironment structure.


## Ground-truth references added for v2 (2026-09-21)

# Ground-truth resources for benchmarking tissue / cell–cell communication models

Companion notes to `groundtruth_refs.bib`. Verification date: **2026-09-21**.
Verification method: DOIs resolved against the Crossref REST API (`api.crossref.org/works/<doi>`)
or the bioRxiv details API (`api.biorxiv.org/details/biorxiv/<doi>`) for preprints; content
claims checked against the publisher/PMC full text or the bioRxiv-served abstract.
Every field in the .bib (author list, journal, volume, issue, pages, year, DOI) is **VERIFIED**
unless explicitly flagged below.

---

## 1. `pasqual2018lipstic` — LIPSTIC

**What it is.** LIPSTIC (Labelling Immune Partnerships by SorTagging Intercellular Contacts) is a
genetically encoded intercellular enzymatic labelling system: a sortase A fused to a ligand on the
"donor" cell transfers a biotinylated substrate onto an acceptor peptide (G5) fused to the cognate
receptor on the "recipient" cell, so that only cells that physically engaged through that
receptor–ligand pair carry the label. Demonstrated in vivo for CD40L–CD40 in T cell–dendritic cell
interactions in mouse lymph nodes.

**Ground truth it yields.** A direct, physically grounded, *in vivo* readout of which individual
cells have engaged which partner cells, recoverable by flow cytometry/sorting and therefore
combinable with scRNA-seq. This is the canonical positive-control label for "did cell A actually
touch cell B", i.e. exactly the quantity CCC inference methods only ever predict indirectly.

**Caveats.** The original LIPSTIC is *pair-specific*: it records interactions only through the one
engineered receptor–ligand pair (CD40L–CD40), so it cannot enumerate an unbiased interactome. It
requires transgenic mice and is dissociation-based (no tissue coordinates are retained), so it gives
pair identity but not spatial position.

**Flags.** All bibliographic fields VERIFIED (Crossref: Nature 553(7689):496–500, 2018,
10.1038/nature25442).

---

## 2. `nakandakarihiga2024ulipstic` — uLIPSTIC

**What it is.** The universal version of LIPSTIC. Sortase and the G5 acceptor are displayed on the
cell surface generically rather than fused to a specific receptor–ligand pair, so label transfer
happens on *any* sufficiently close/durable cell–cell contact, irrespective of which molecules
mediate it. The paper couples uLIPSTIC with single-cell transcriptomics to catalogue immune
populations physically interacting with intestinal epithelial cells and to follow the interactome of
LCMV-specific CD8⁺ T cells across organs after systemic infection.

**Ground truth it yields.** Labelled *interacting cell pairs in vivo* with a paired transcriptome
for the labelled cell — i.e. an experimentally measured, receptor-agnostic contact graph over cell
types/states. This is the single strongest available benchmark target for CCC methods that claim to
predict which cell types communicate in a tissue, and it is generated in native tissue rather than
in dissociated or reaggregated cells.

**Caveats.** Still requires transgenic mice (mouse-only, no human tissue); labelling reports
*contact*, not which ligand–receptor pair carried the signal, so it validates the cell-pair layer of
a CCC prediction but not the LR-pair layer; label intensity depends on contact duration/avidity, so
transient interactions are under-recovered; readout is after dissociation, so spatial coordinates
are lost.

**Flags.** All bibliographic fields VERIFIED (Crossref: Nature 627(8003):399–406, 6 March 2024,
10.1038/s41586-024-07134-4; 18 authors as listed). The preprint DOI in the `note` field
(10.1101/2023.03.16.533003) VERIFIED via the bioRxiv API — note the preprint carries a different
title, "Universal recording of cell-cell contacts in vivo for interaction-based transcriptomics"
(posted 20 March 2023).

---

## 3. `du2026matchseq` — match-seq (the requested bioRxiv preprint)

**What it is.** The preprint at `biorxiv.org/content/10.64898/2026.09.16.752238v1` is
**"In vivo intercellular CRISPR screens using viral proximity barcoding reveal regulators of
tumor-immune interactions"** (Du, Kohno, Wang, Papanicolaou, Vaughan-Jackson, Daigh, Peng, Spees,
McCormick, Diehl, Bintu, Qiu, Satpathy, Bassik; corresponding author Michael Bassik, Stanford;
posted 18 September 2026). **Yes — it is a proximity-labelling / interaction-recording technology.**
It introduces **match-seq**, an imaging-free, sequencing-based cell-proximity tracing system in
which virus-like particles transmit barcoded mRNAs from sender cells to nearby receiver cells; the
spatial linkage is then reconstructed computationally from barcode sequencing after tissue
dissociation. Applied in a syngeneic murine tumour model, it labels all immune lineages and
reconstructs cell-type niches recapitulating known tumour spatial biology, and is coupled to pooled
CRISPR + scRNA-seq to screen for cancer-cell genes that reshape the local microenvironment
(Tgfb1 → CD8 T cells/macrophages, Traf7 → CD4 T cells, Nectin3 → NK cells; validated by in vivo
immune depletion).

**Ground truth it yields.** (i) An experimentally measured neighbour graph — barcode sharing between
sender and receiver cells — with a matched single-cell transcriptome per cell, i.e. *observed*
proximity to score predicted CCC against; and (ii) uniquely among the entries here, a **causal**
layer: perturbation of a sender gene with a measured readout on the local microenvironment
composition and state. That second layer is what a CCC model would need to be benchmarked on
*interventionally* rather than correlatively.

**Caveats.** Preprint, not peer reviewed. Barcode transfer reports a proximity neighbourhood, not a
molecularly specified receptor–ligand engagement, and the "spatial" reconstruction is inferred after
dissociation rather than measured in situ. Mouse tumour model only. Requires engineered sender cells
(VLP machinery + barcode), so it is not applicable to primary human tissue.

**Flags.** Title, author list, DOI, posting date, abstract VERIFIED via the bioRxiv details API.
Author *given names* were taken from the article page (the API returns initials only) —
**VERIFIED via page fetch, not via Crossref**; bioRxiv has no Crossref-registered author list for
this record. Middle initials are deliberately omitted because no fetched source supplied them.
No journal volume/pages exist (preprint).

---

## 4. Moleculent — **NO PRIMARY PUBLICATION FOUND** (no .bib entry)

**Finding.** Moleculent AB (Stockholm, founded 2021; CEO Olle Ericsson, CTO Fredrik Roos, both ex-
Vanadis Diagnostics; $26M Series A June 2024 led by ARCH Venture Partners + Eir Ventures, extended
by $20M; "Techstart" early-access programme announced November 2025) describes an imaging-based,
high-plex platform that measures **cell–cell protein (ligand–receptor) interactions directly in
intact FFPE human tissue**, with an initial immuno-oncology focus. This is exactly the kind of in
situ CCC ground truth the research plan wants. **However, as of 2026-09-21 I could not find any
primary publication or preprint describing it.** Searches run: Crossref, Europe PMC
(`"Moleculent"`, `AFF:"Moleculent"`, `AUTH:"Ericsson O"` 2024–2026 — all returned only fuzzy,
unrelated hits, i.e. zero true matches), bioRxiv, and the company's own site (no publications page,
no named assay). The technology appears to be **pre-publication / early access only**.

**Two conflations to avoid.**
- **Molecular Pixelation (MPX) is *not* Moleculent.** MPX is from **Pixelgen Technologies AB**, a
  different Stockholm company (author affiliations on the paper: "Pixelgen Technologies AB,
  Stockholm, Sweden"; competing-interests statement: "All authors are employees or advisors to
  Pixelgen Technologies, which commercializes products based on Molecular Pixelation"). It is
  entered below as `karlsson2024molecularpixelation` for completeness, but it is a *different*
  company and a *different* problem (see §5).
- The bioRxiv preprint "Multiomic Spatial Imaging Assay (MSIA)" (doi 10.64898/2026.02.26.708124),
  which surfaces on searches for high-plex in situ protein–protein interaction detection in FFPE, is
  from **Advanced Cell Diagnostics / Bio-Techne** (corresponding author Li-Chong Wang), *not*
  Moleculent. Checked and excluded.

**Flags.** Company facts (founders, funding, platform description, early-access programme) sourced
from Businesswire/GenomeWeb/GenEng press coverage and moleculent.com — **UNVERIFIED against any
peer-reviewed or preprint source.** Existence of a primary publication: **searched and not found**;
treat as "no citable publication yet" rather than as proof of absence. Recommend re-checking before
submission.

---

## 5. `karlsson2024molecularpixelation` — Molecular Pixelation (MPX), Pixelgen Technologies

**What it is.** An optics-free, DNA-sequencing-based method for *subcellular* spatial proteomics of
single cells: antibody–oligonucleotide conjugates are assembled into >1,000 DNA "pixel"
neighbourhoods per cell, yielding a 3D spatial proteomics network over 76 surface proteins per cell.

**Ground truth it yields.** Relative spatial organisation and co-localisation/polarisation of
*surface receptors on a single cell* — useful for the receptor-availability and receptor-clustering
assumptions that CCC methods make implicitly, and as an orthogonal check on whether a receptor is
actually presented at a contact face.

**Caveats.** This is **within-cell** surface topology, not **between-cell** contact: it is measured
on dissociated single cells in suspension, not in tissue, and it does not record which cell a given
cell was touching. It is therefore adjacent ground truth, not a CCC benchmark. Include only if the
plan discusses receptor-presentation assumptions; do not present it as tissue CCC ground truth.

**Flags.** All bibliographic fields VERIFIED (Crossref: Nature Methods 21(6):1044–1052, 8 May 2024,
10.1038/s41592-024-02268-9). Affiliation VERIFIED from PMC11166577.

---

## 6. `liu2026cytosignal` — CytoSignal (Welch lab)

**Key correction to the brief.** The paper is **Liu et al., *Nature Genetics* 58(6):1396–1408
(2026)**, doi `10.1038/s41588-026-02624-9` — first author **Jialin Liu**, senior author Joshua D.
Welch. It is *not* Zhao et al. and *not* Nature Methods/Nature Biotechnology. The bib key is
therefore `liu2026cytosignal`, not `zhao2026cytosignal`. (Preprint: bioRxiv 10.1101/2024.03.08.584153.)

**What it is.** A method that scores ligand–receptor signalling at *cellular resolution and specific
tissue locations* from spatial transcriptomics, on the premise that signalling occurs where ligand
and receptor are co-expressed in spatial proximity. It separates contact-dependent from diffusible
interactions, detects signalling gradients and signalling-associated genes, supports differential
signalling across samples, and infers temporal dynamics per location.

**What the ground truth actually is — also a correction.** It is **not** a compiled database of
literature-validated ligand–receptor pairs, and **not** knockout/perturbation data. It is an
**orthogonal in situ imaging assay**: *proximity ligation assay (PLA)*, which fluoresces only when
the two proteins are within ~40 nm. The authors ran paired experiments on **spatially adjacent
sections of the same mouse embryo** — Visium HD spatial transcriptomics on one section, PLA on the
adjacent one — for **five ligand–receptor pairs: Igf2–Igf2r, Spp1–Cd44, Fgf8–Fgfr1, Efna3–Epha5,
Dll1–Notch1**. PLA fluorescence was registered onto the transcriptomic coordinates by computational
image registration, and methods were scored by the AUC of a classifier predicting binary PLA
positivity per region. CytoSignal outperformed CellChat, CellPhoneDB, LIANA+ and SpatialDM across
tissue domains. **This is arguably the most directly reusable location-resolved LR ground truth
currently published**, and it is a protein-level measurement, independent of the transcriptomic
input the methods use.

**Caveats.** Only five LR pairs; one tissue (mouse embryo); PLA is measured on an *adjacent* section,
so registration error and section-to-section biological variation propagate into the label; PLA
positivity is binary and antibody-dependent (sensitivity/specificity per pair are not uniform);
"within 40 nm" reports proximity of the two proteins, not productive signalling. Ground-truth scale
is small, so benchmark variance will be high.

**Flags.** All bibliographic fields VERIFIED (Crossref: Nature Genetics 58(6):1396–1408, June 2026;
14 authors as listed). The preprint DOI in the `note` field (10.1101/2024.03.08.584153) VERIFIED via
the bioRxiv API (posted 13 March 2024). Ground-truth description VERIFIED from the PMC full text
(PMC13263138).

---

## 7. `giladi2020picseq` — PIC-seq

**What it is.** Physically Interacting Cell sequencing: doublets of physically interacting cells are
deliberately sorted (rather than discarded as artefacts) and sequenced, and a computational model
deconvolves each PIC into its constituent cell types and identifies the crosstalk-induced expression
that is specific to the interacting state. Applied to T cell–dendritic cell interactions in vitro
and in vivo, mapping interaction preferences in mouse draining lymph nodes.

**Ground truth it yields.** An experimentally observed frequency table of *which cell types are
physically found together*, plus the transcriptional signature attributable to being in contact.
Useful both as a cell-pair-level benchmark and as a target for methods claiming to predict the
downstream transcriptional consequence of communication.

**Caveats.** Interactions must survive tissue dissociation and sorting, which biases strongly toward
strong/durable adhesive pairs and against fragile or transient contacts; no spatial coordinates;
doublet-vs-true-PIC ambiguity is handled statistically, not experimentally; no LR-pair resolution.

**Flags.** All bibliographic fields VERIFIED (Crossref: Nature Biotechnology 38(5):629–637, 2020,
10.1038/s41587-020-0442-2).

---

## 8. `boisset2018proximid` — ProximID

**What it is.** Builds a cellular network from physical cell interactions by micro-dissecting small
cell clusters from gently dissociated tissue and sequencing their constituent cells individually, so
partners are known by construction and no prior knowledge of the participating cell types is needed.
Recovered megakaryocyte–neutrophil and plasma cell–myeloblast/promyelocyte interactions in mouse
bone marrow, and a Tac1⁺ enteroendocrine cell–Lgr5⁺ stem cell interaction in small-intestinal crypts.

**Ground truth it yields.** An unbiased, discovery-mode physical interaction network over cell types
in a tissue — a useful *recall* benchmark (does a CCC method recover experimentally observed
preferential partnerships?) without the circularity of LR-database-derived "truth".

**Caveats.** Low throughput (hundreds of cells, not atlas scale); same dissociation bias as PIC-seq;
mouse tissue; no LR-pair resolution and no spatial coordinates. Now eight years old — use as a
historical positive-control set rather than a primary benchmark.

**Flags.** All bibliographic fields VERIFIED (Crossref: Nature Methods 15(7):547–553, 2018,
10.1038/s41592-018-0009-z).

---

## 8b. Disclosure on the 2024–2026 recency requirement

The brief asked for up to three further **2024–2026** technologies that record physical cell–cell
contacts or ligand–receptor engagement *in situ*. **No such well-established technology was found
beyond match-seq (§3) and uLIPSTIC (§2).** PIC-seq (2020) and ProximID (2018) are included instead,
outside the requested window and dissociation-based rather than in situ, as the foundational
precedents against which match-seq explicitly positions itself. A Europe PMC sweep of 2024–2026
titles combining proximity labelling / cell–cell contact with tissue / in vivo / in situ (35 hits)
returned almost exclusively *molecular* proximity labelling — TurboID/photocatalytic/µMap-style
methods that map protein interactomes or subcellular proteomes (including µMap-FFPE, *JACS* 2025,
which does work in FFPE tissue but profiles bait-proximal *proteins*, not cell partners) — none of
which yields cell-pair ground truth. Treat the absence as "searched, nothing well established
found", not as proof of absence.

---

## 9. TERRA and gene-panel heterogeneity (pointer for the atlas-limitation argument)

`birk2026terra` (already in `research_plan.bib`, doi 10.64898/2026.07.29.741565, 112M cells —
confirmed) does **not** harmonise the discordant feature spaces explicitly: it tokenises each gene by
a gene-symbol token (plus value, gene-rank and cell-rank tokens; Fig. 1d) and absorbs the remaining
panel discordance into a **batch metatoken** added during pretraining — the preprint states it
"included a batch metatoken to help account for assay- and sample-specific technical variation,
including differences in gene panels, detection sensitivity, and noise characteristics", supplied to
both context and target streams and padded at inference. So panel heterogeneity is handled as a
*nuisance batch effect inside a JEPA objective*, not as an explicit feature-space alignment — which
is precisely the weak point to press on when arguing that such atlases cannot by themselves
adjudicate ligand–receptor claims (a ligand or receptor absent from a panel is not distinguishable
from one that is not expressed).

**Flags.** Quoted mechanism VERIFIED from the preprint full text (`...741565v1.full`); cell count
(112M) VERIFIED. Figure number (Fig. 1d) reported by the full-text fetch —
**UNVERIFIED against the rendered figure itself**; cite the sentence, not the figure number, if
precision matters.

---

## Summary of what each source can and cannot adjudicate

| Entry | Contact pairs | LR-pair identity | In situ coordinates | Human tissue | Causal / perturbational |
|---|---|---|---|---|---|
| LIPSTIC | yes | fixed single pair | no | no (mouse) | no |
| uLIPSTIC | yes (receptor-agnostic) | no | no | no (mouse) | no |
| match-seq | yes (proximity) | no | inferred, not measured | no (mouse) | **yes** (CRISPR screen) |
| PIC-seq | yes | no | no | no (mouse) | no |
| ProximID | yes | no | no | no (mouse) | no |
| CytoSignal / PLA | implied | **yes (5 pairs)** | **yes** | no (mouse embryo) | no |
| MPX | no (within-cell) | no | subcellular only | yes (blood cells) | no |

The gap this table exposes — no single resource gives contact pairs *and* LR identity *and* tissue
coordinates *and* human tissue — is itself the argument for a benchmarking programme.
