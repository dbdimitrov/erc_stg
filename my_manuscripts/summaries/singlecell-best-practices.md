## Best practices for single-cell analysis across modalities

*Heumos et al., Nature Reviews Genetics (2023) · **Author role: Contributing author (Single-cell Best Practices Consortium)***

**Problem:** Single-cell technologies now span transcriptomics, chromatin accessibility, surface proteins, immune receptor repertoires, and spatial location, with >1,400 tools available. Existing scRNA-seq best-practice guides are outdated or incomplete, and no comprehensive, benchmark-grounded workflow spans modalities.

**Approach:** An expert-recommendation review that, wherever independent benchmarks exist, distills them into best-practice workflows; where they do not, it contrasts popular methods and community recommendations. It is organized by modality and analysis-step groups rather than one monolithic pipeline, complemented by a regularly updated online book (50+ chapters with code).

**Key contributions:** Consolidated, benchmark-backed recommendations across the analysis lifecycle. scRNA-seq: QC via median-absolute-deviation filtering, ambient-RNA correction (SoupX, CellBender), doublet detection (scDblFinder), normalization (shifted logarithm, scran, analytic Pearson residuals), feature selection by deviance, integration (Harmony, scVI/scANVI, Scanorama; scIB metrics), Leiden clustering, annotation (CellTypist, scArches, Azimuth), trajectory/RNA velocity (Slingshot, PAGA, scVelo, CellRank), pseudobulk DGE (edgeR, DESeq2, limma), enrichment (decoupleR, PROGENy, DoRothEA), compositional analysis (scCODA, MILO), cell-cell communication (recommending LIANA), and perturbation modeling (scGen, CPA). Dedicated sections cover scATAC-seq (peaks/bins, ArchR, Signac, cisTopic, snapATAC, chromVAR, PeakVI/MultiVI), CITE-seq surface protein (DSB/CLR normalization, totalVI, CiteFuse), immune repertoires (Scirpy, Dandelion), and spatial data (Squidpy, Giotto). Box 1 systematizes multimodal integration (paired via MOFA+/WNN, unpaired/diagonal via GLUE/SCOT, mosaic via StabMap/Multigrate, query-to-reference bridge integration).

**Data & tools:** Frameworks Scanpy, Seurat, Bioconductor/SingleCellExperiment, muon; the Single-Cell Best Practices online book. Names dozens of task-specific packages (verbatim above).

**Relevance to future work:** The canonical methods map for the single-cell field. An agent building on Daniel's work should use it to select benchmark-justified defaults per step and to place his own tools (LIANA for CCC, decoupleR/PROGENy for enrichment) within the recommended ecosystem.
