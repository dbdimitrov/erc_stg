## RIDDEN: Data-driven inference of receptor activity from transcriptomic data

*Barsi et al., PLoS Computational Biology (2025) · **Author role: Contributing author (3rd)***

**Problem:** Receptors are the most frequent drug targets, yet existing cell–cell communication (CCC) methods focus on ligand–receptor pairs and rely on ligand/receptor gene co-expression, which does not reflect functional activation or protein-level activity. No prior method directly infers receptor activity from the receptor-regulated downstream gene expression footprint.

**Approach:** RIDDEN (Receptor actIvity Data Driven inferENce) is a footprint-based linear model. Curated ligand–receptor interactions from OmniPath were combined with 14,463 consensus perturbation profiles for 229 receptors from LINCS L1000 (level 5, landmark genes; genetic shRNA/CRISPR/overexpression and chemical ligand/drug perturbations, encoded +1/-1/0). OLS regression (statsmodels) per receptor–gene pair yields a receptor–gene weight matrix; activities are inferred via dot product of a sample's expression profile with the matrix, z-scored against 1,000 gene-label permutations. Receptors are assigned confidence levels A–E from cross-validation (median ROC AUC 0.71).

**Key contributions:** The largest transcriptomics-based receptor activity inference model. Matches/exceeds CytoSig on cytokine-signaling prediction (RIDDEN 0.61 vs CytoSig 0.59; A-confidence receptors outperform), validated on the Immune Dictionary single-cell data and beating NicheNet (0.54). Model weights recover receptor-family clustering and receptor–TF pathway relationships (via decoupleR + DoRothEA). Case study: RIDDEN-estimated PD-1 activity (not PD-1/PD-L1 mRNA) predicts nivolumab survival in ccRCC.

**Data & tools:** RIDDEN_tool (https://github.com/basvaat/RIDDEN_tool), RIDDEN_analysis (https://github.com/basvaat/RIDDEN_analysis), Zenodo DOI 10.5281/zenodo.15127392. Uses OmniPath, LINCS L1000, CytoSig, Immune Dictionary, NicheNet, TCGA, CCLE, decoupleR, DoRothEA, KEGG, IUPHAR/BPS, statsmodels, scikit-learn, Scanpy, scrublet, BBKNN, lifelines.

**Relevance to future work:** Complements Daniel Dimitrov's LIANA+ by adding a receiver-side, activity-based readout of receptors — enabling agents to move beyond co-expression CCC toward mechanistic, perturbation-grounded receptor activity as biomarkers in disease and immunotherapy contexts.
