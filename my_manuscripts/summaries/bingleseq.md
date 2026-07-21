## BingleSeq: a user-friendly R package for bulk and single-cell RNA-Seq data analysis

*Dimitrov & Gu, PeerJ (2020) · **Author role: FIRST author***

**Problem:** Both bulk RNA-Seq differential expression (DE) and single-cell RNA-Seq (scRNA-Seq) analysis produce count matrices that require programming expertise to analyze. Few existing tools flexibly handle both experiment types, creating a barrier for biologists without coding experience.

**Approach:** BingleSeq is a shiny-based R package with a multi-tabbed, reactive dashboard UI built as modular shiny components. Each tab maps to a key pipeline step, and modules are generated lazily for efficiency. Plots are made interactive via ggplot-to-ggplotly conversion. For each analysis type it exposes three state-of-the-art package options plus tunable parameters.

**Key contributions:** A single application covering both bulk and scRNA-Seq. Bulk pipeline: filtering (CPM/Max/Median), batch correction (Harman, ComBat/sva), DE via DESeq2, edgeR, and limma, with PCA/volcano/MA/barchart/heatmap visualizations. scRNA-Seq pipeline: Seurat-based normalization/clustering plus monocle and SC3 clustering, tSNE, marker DE (T-test, Wilcoxon, DESeq2, MAST). Functional annotation via GOseq (GO + KEGG) and footprint-based activity inference with DoRothEA (TF, coupled to viper aREA) and PROGENy (14 signaling pathways). A rank-based consensus and Venn overlap approach to reconcile disagreeing DE methods, boosting confidence.

**Data & tools:** Package at https://github.com/dbdimitrov/BingleSeq/. Built on shiny, ggplotly; wraps DESeq2, edgeR, limma, Seurat, monocle, SC3, MAST, GOseq, GO.db, DoRothEA, viper, PROGENy, compcodeR (synthetic benchmark). Test data: HSV-1 vs interferon-B bulk (ENA PRJEB27501) and 10x PBMC 3k scRNA-Seq. Supports human, mouse, drosophila, zebrafish, E. coli K12.

**Relevance to future work:** Daniel's entry point into computational biology and the Saez-Rodriguez footprint ecosystem (DoRothEA/PROGENy/viper), which recurs in decoupleR. Establishes his recurring themes: consensus across methods, benchmarking, and lowering the barrier to omics analysis. Useful grounding for any agent working on RNA-Seq tooling, DE method comparison, or accessible bioinformatics interfaces.
