# Previous Work — Daniel Dimitrov

> **For future agents.** This file is the authorship-annotated index of Daniel Dimitrov's
> publications collected under `my_manuscripts/`. Each paper has:
> - a **full Markdown conversion** (formatting + main figures rendered inline) in `my_manuscripts/markdown/<name>.md`
> - a **structured technical brief** (Problem / Approach / Key contributions / Data & tools / Relevance) in `my_manuscripts/summaries/<name>.md`
>
> Papers are split into **lead-authored** (first / co-first / last & corresponding) and
> **contributing** (middle-author) work. Author roles were verified against the equal-contribution
> and corresponding-author footnotes in each PDF.
>
> **Scholar profile** ([`dDujacgAAAAJ`](https://scholar.google.com/citations?user=dDujacgAAAAJ&hl=en)):
> **4000+ citations · h-index 14 · i10-index 16.** Citation counts below are from Google Scholar
> as of **2026-07-21** and drift upward over time.

---

## Lead-authored (first / co-first / last & corresponding)

### Cellina — Querying Counterfactuals on Tissue Graphs with Supervised Disentanglement
**LAST author & co-corresponding** (with O. Stegle) · arXiv preprint 2026 · 0 citations
The current flagship method: a graph-VAE that disentangles a cell's *intrinsic* identity latent from its *extrinsic* spatial-microenvironment latent to answer spatial "what-if" (edge/node) counterfactuals on tissue graphs.
📄 [Full](my_manuscripts/markdown/cellina.md) · 🔎 [Brief](my_manuscripts/summaries/cellina.md)

### Interpretation, extrapolation and perturbation of single cells
**CO-FIRST and CORRESPONDING author** (with S. Schrod; O. Stegle senior) · Nature Reviews Genetics 2025 · 22 citations
Review framing the shift from descriptive single-cell atlasing toward causal/mechanistic and perturbation-effect modelling — the conceptual backdrop for the current spatial-perturbation research.
📄 [Full](my_manuscripts/markdown/single-cell-interpretation-perturbation.md) · 🔎 [Brief](my_manuscripts/summaries/single-cell-interpretation-perturbation.md)

### LIANA+ provides an all-in-one framework for cell–cell communication inference
**FIRST author** · Nature Cell Biology 2024 · 300 citations
Scalable, knowledge-based framework decoding inter- and intracellular signalling from single-cell and spatially resolved (multi-condition) data; the `liana-py` successor to the original LIANA.
📄 [Full](my_manuscripts/markdown/liana-plus.md) · 🔎 [Brief](my_manuscripts/summaries/liana-plus.md)

### Comparison of methods and resources for cell–cell communication inference from single-cell RNA-Seq data
**FIRST author** · Nature Communications 2022 · 706 citations
The foundational LIANA benchmark: systematically compared 16 CCC resources × 7 methods, showing predictions are strongly method- and resource-dependent and motivating consensus scoring.
📄 [Full](my_manuscripts/markdown/liana.md) · 🔎 [Brief](my_manuscripts/summaries/liana.md)

### Combining LIANA and Tensor-cell2cell to decipher cell–cell communication across multiple samples
**CO-FIRST author** (with H. Baghdassarian) · Cell Reports Methods 2024 · 29 citations
A unified protocol pairing LIANA's method selection with Tensor-cell2cell's unsupervised decomposition to recover context-driven communication programmes across multi-sample datasets.
📄 [Full](my_manuscripts/markdown/liana-tensor-cell2cell.md) · 🔎 [Brief](my_manuscripts/summaries/liana-tensor-cell2cell.md)

### MetalinksDB: a flexible and contextualizable resource of metabolite–protein interactions
**CO-FIRST author** (with E. Farr) · Briefings in Bioinformatics 2024 · 31 citations
A contextualizable knowledge base of metabolite–protein interactions enabling metabolite-mediated cell–cell communication inference (feeds LIANA+'s metabolite CCC).
📄 [Full](my_manuscripts/markdown/metalinksdb.md) · 🔎 [Brief](my_manuscripts/summaries/metalinksdb.md)

### BingleSeq: a user-friendly R package for bulk and single-cell RNA-Seq data analysis
**FIRST author** · PeerJ 2020 · 12 citations
Daniel's earliest lead work — an accessible Shiny application for differential-expression and clustering analysis spanning both bulk and single-cell RNA-Seq.
📄 [Full](my_manuscripts/markdown/bingleseq.md) · 🔎 [Brief](my_manuscripts/summaries/bingleseq.md)

### How will artificial intelligence and bioinformatics change our understanding of IgA Nephropathy in the next decade?
**CO-FIRST author** (with R. D. Bülow) · Seminars in Immunopathology 2021 · 29 citations
Perspective on integrating multi-scale molecular/cellular data and machine learning to dissect IgA nephropathy pathophysiology.
📄 [Full](my_manuscripts/markdown/iga-nephropathy-ai.md) · 🔎 [Brief](my_manuscripts/summaries/iga-nephropathy-ai.md)

---

## Contributing (middle-author)

### OmniPath: integrated knowledgebase for multi-omics analysis
Contributing author · Nucleic Acids Research 2026 · 22 citations
The integrated prior-knowledge backbone underpinning LIANA+, decoupleR, MetalinksDB and RIDDEN.
📄 [Full](my_manuscripts/markdown/omnipath.md) · 🔎 [Brief](my_manuscripts/summaries/omnipath.md)

### Defining and benchmarking open problems in single-cell analysis
Contributing author · Nature Biotechnology 2025 · 78 citations
Community "Open Problems" living-benchmark platform; Daniel contributed to the cell–cell communication task.
📄 [Full](my_manuscripts/markdown/open-problems-singlecell.md) · 🔎 [Brief](my_manuscripts/summaries/open-problems-singlecell.md)

### RIDDEN: Data-driven inference of receptor activity from transcriptomic data
Contributing author (3rd) · PLoS Computational Biology 2025 · 2 citations
Footprint-based, receiver-side inference of receptor activity — a complement to LIANA+ built on OmniPath + LINCS L1000.
📄 [Full](my_manuscripts/markdown/ridden.md) · 🔎 [Brief](my_manuscripts/summaries/ridden.md)

### Unveiling the role of sex in the metabolism of indoxyl sulfate and apixaban
Contributing author (2nd) · Scientific Reports 2025 · 7 citations
Sex-stratified pharmacology in CKD; Daniel contributed the transcriptomics/proteomics differential-expression and functional-enrichment analysis (decoupleR).
📄 [Full](my_manuscripts/markdown/sex-indoxyl-apixaban.md) · 🔎 [Brief](my_manuscripts/summaries/sex-indoxyl-apixaban.md)

### Single-cell integration reveals metaplasia in inflammatory gut diseases
Contributing author · Nature 2024 · 115 citations
Human Cell Atlas landmark; Daniel's cell–cell communication analysis pinpointed inflammatory-niche signalling axes.
📄 [Full](my_manuscripts/markdown/gut-metaplasia.md) · 🔎 [Brief](my_manuscripts/summaries/gut-metaplasia.md)

### Integrating single-cell multi-omics and prior biological knowledge for a functional characterization of the immune system
Contributing author (2nd) · Nature Immunology 2024 · 69 citations
Review of knowledge-driven functional analysis of immune single-cell/spatial multi-omics.
📄 [Full](my_manuscripts/markdown/immune-multiomics-review.md) · 🔎 [Brief](my_manuscripts/summaries/immune-multiomics-review.md)

### Clarifying the murk: bacterial dynamics in response to crude oil, Corexit-dispersant and sunlight (Gulf of Mexico)
Contributing author · Frontiers in Marine Science 2024 · 12 citations
Environmental metaproteomics of marine microbial communities — from Daniel's earlier University of Glasgow / Stirling period.
📄 [Full](my_manuscripts/markdown/marine-proteomics.md) · 🔎 [Brief](my_manuscripts/summaries/marine-proteomics.md)

### Multicellular factor analysis of single-cell data for a tissue-centric understanding of disease (MOFAcell)
Contributing author (3rd) · eLife 2023 · 57 citations
Repurposes MOFA on pseudobulk multi-views to learn multicellular programmes across samples — conceptual sibling to LIANA+/Tensor-cell2cell.
📄 [Full](my_manuscripts/markdown/mofacell.md) · 🔎 [Brief](my_manuscripts/summaries/mofacell.md)

### Best practices for single-cell analysis across modalities
Contributing author (Single-cell Best Practices Consortium) · Nature Reviews Genetics 2023 · 1,242 citations
Consortium best-practices review spanning transcriptomics, chromatin, surface protein, immune-repertoire and spatial modalities.
📄 [Full](my_manuscripts/markdown/singlecell-best-practices.md) · 🔎 [Brief](my_manuscripts/summaries/singlecell-best-practices.md)

### decoupleR: ensemble of computational methods to infer biological activities from omics data
Contributing author · Bioinformatics Advances 2022 · 1,154 citations
Unified ensemble of enrichment methods (ULM, MLM, etc.) for inferring TF/pathway/functional activities; reused throughout Daniel's toolkit.
📄 [Full](my_manuscripts/markdown/decoupler.md) · 🔎 [Brief](my_manuscripts/summaries/decoupler.md)

---

*Generated 2026-07-21. Source PDFs in `my_manuscripts/pdfs`; extracted text in `my_manuscripts/raw/`.*
