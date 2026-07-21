## LIANA+ provides an all-in-one framework for cell-cell communication inference

*Dimitrov et al., Nature Cell Biology (2024) · **Author role: FIRST author***

**Problem:** Over 100 CCC tools exist, each capturing only a partial view: most handle a single task or data type, focus on protein-mediated interactions from transcriptomics alone, and largely ignore metabolite-mediated signalling, spatial multi-omics, cross-condition designs, and links to intracellular signalling.

**Approach:** LIANA+, a scalable Python framework built on scverse (AnnData/MuData) I/O and a unified prior-knowledge base (OmniPath, BioCypher). Components: (1) re-implements 8-9 ligand-receptor methods (CellPhoneDB, CellChat, Connectome, NATMI, logFC, SingleCellSignalR, geometric mean, scSeqComm) with a flexible consensus; (2) spatial inference via multi-view modelling of global relationships plus 8 local metrics (spatially weighted cosine/Pearson/Spearman/Jaccard, masked Spearman from scHOT, weighted product, bivariate Moran's R from SpatialDM); (3) cross-condition strategies -- hypothesis-driven differential analysis via PyDESeq2 and hypothesis-free factorizations via NMF, Tensor-cell2cell, and Bayesian multi-view factor analysis (MOFA-style, giving per-cell-type-pair importances); (4) sign-coherent causal subnetwork search linking ligand-receptor events to downstream TFs. Works on dissociated single-cell and spatial multi-omics data.

**Key contributions:** Demonstrated on a murine Parkinson's 6-OHDA lesion model with spatial metabolome (MALDI-MSI) + transcriptome (Visium): recovered dopamine's association with Drd2/D2R and MSN1/2 cell types (Tangram deconvolution), localizing interactions to intact striatum. On human myocardial infarction snRNA + Visium data: identified ischaemia/fibrosis intercellular programmes (integrin-FN1/SPP1/TNC/THBS1) and reconstructed FB-to-myeloid signalling to SMAD1/3 via MAPK1/14, ATM, EP300, YAP. Showed spatially agnostic LR inference weakly reflects colocalization (evaluated with Slide-tags).

**Data & tools:** LIANA+ (https://github.com/saezlab/liana-py); docs/vignettes (https://liana-py.readthedocs.io/). Depends on OmniPath, BioCypher, PyDESeq2, Tensor-cell2cell, MuData/AnnData, Tangram, decoupler.

**Relevance to future work:** The consolidated multi-omics, spatial, and cross-condition CCC toolkit that supersedes the original LIANA; the reference platform for building metabolite-mediated, spatial, and intracellular-linked signalling analyses on Daniel's stack.
