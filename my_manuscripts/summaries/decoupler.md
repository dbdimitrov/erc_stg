## decoupleR: ensemble of computational methods to infer biological activities from omics data

*Badia-i-Mompel et al., Bioinformatics Advances (2022) · **Author role: Contributing author (middle)***

**Problem:** Omics data (transcriptomics, phospho-proteomics) are high-dimensional and hard to interpret mechanistically. Prior-knowledge-based activity inference (e.g. TF and kinase activities from downstream targets) reduces dimensionality and increases interpretability, but existing tool collections are fragmented and do not incorporate newer methods that model weighted mode of regulation.

**Approach:** decoupleR is a unified R (Bioconductor) and Python framework wrapping 11 activity-inference methods under a common syntax, taking two inputs: a molecular feature matrix (per-sample counts or log fold changes) and a prior-knowledge resource (gene sets / regulatory networks). Methods include AUCell, fast GSEA, GSVA, over-representation analysis, univariate linear model (ULM), multivariate linear model (MLM), and VIPER, plus a consensus score computed as a mean z-score across methods. It supports weighted, signed (mode-of-regulation) interactions that other frameworks lack, and provides wrappers to query OmniPath (100+ prior-knowledge databases: cell-type markers, gene regulatory networks, pathway footprints).

**Key contributions:** One framework spanning bulk, single-cell, and spatial omics in the two dominant analysis languages. A benchmark recovering perturbed TFs (DoRothEA network, transcriptomics) and kinases (kinase-substrate network, phospho-proteomics) from single-gene perturbation datasets showed the top performers were the consensus score, multivariate linear model, and ULM; methods that leverage interaction weights performed significantly better when weights were used. The Python implementation runs orders of magnitude faster than R, enabling single-cell/spatial scale.

**Data & tools:** Bioconductor (https://www.bioconductor.org/packages/release/bioc/html/decoupleR.html); Python at https://github.com/saezlab/decoupler-py; manuscript code at https://github.com/saezlab/decoupleR_manuscript; data at https://zenodo.org/record/5645208. Integrates OmniPath, DoRothEA.

**Relevance to future work:** decoupleR is a foundational utility across Daniel's downstream work (its ULM enrichment is reused in MetalinksDB and pairs with LIANA+). Any agent doing footprint/activity inference, pathway or TF scoring, or building on the Saez-lab stack should default to decoupleR and its consensus/linear-model recommendations.
