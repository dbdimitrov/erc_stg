## Single-cell integration reveals metaplasia in inflammatory gut diseases

*Oliver et al., Nature (2024) · **Author role: Contributing author (middle)***

**Problem:** Over 25 scRNA-seq studies of the human gastrointestinal (GI) tract exist but are organ- or cell-type-siloed, lacking a unified reference. The origin and functional role of pyloric/pseudopyloric metaplasia (MUC6+ cells) in acute and chronic intestinal inflammation remained unresolved.

**Approach:** Systematic integration of 25 scRNA-seq datasets (385 samples, 189 healthy controls) using a new automated QC pipeline (scAutoQC) and scVI, yielding a ~1.1M-cell healthy pan-GI reference with 136 fine-grained cell states. 12 disease datasets (GI cancers, coeliac, ulcerative colitis, Crohn's, paediatric IBD) were anchored by transfer learning into a 1.6M-cell atlas (gutcellatlas.org). Analyses included consensus NMF (cNMF), pseudotime trajectories (Monocle3, Palantir), gene-level trajectory alignment (Genes2Genes), bulk deconvolution (BayesPrism), and cell-cell communication inference.

**Key contributions:** Discovery of MUC6+ inflammatory epithelial cells (INFLAREs) — pyloric-gland metaplastic cells arising from LGR5+ crypt stem cells in coeliac and IBD intestine, characterized at single-cell resolution for the first time. INFLAREs retain stemness yet play a dual role: mucosal healing (TFF3) but also pro-inflammatory chemokine signaling (CXCL16, CXCL2/3/5, CXCL17) recruiting T cells and neutrophils, with CXCL2/3/5→ACKR1 signaling to venous endothelium linked to anti-TNF/anti-integrin therapy resistance.

**Data & tools:** gutcellatlas.org resource; scAutoQC, scVI, cNMF, Monocle3, Palantir, Genes2Genes, BayesPrism deconvolution; smFISH/IHC validation. Cell-cell communication analysis (LIANA-family tooling from the Saez-Rodriguez lab).

**Relevance to future work:** Daniel's likely contribution is the cell-cell communication / functional analysis (LIANA), which pinpointed the INFLARE-fibroblast (AREG/EREG-EGFR/ERBB) and INFLARE-endothelial (CXCL-ACKR1) axes underpinning the metaplastic inflammatory niche. Demonstrates LIANA's application in a landmark Human Cell Atlas disease study and its value for mechanistic niche discovery in future tissue-atlas work.
