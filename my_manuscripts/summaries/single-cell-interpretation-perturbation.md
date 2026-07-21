## Interpretation, extrapolation and perturbation of single cells

*Dimitrov et al., Nature Reviews Genetics (2025) · **Author role: CO-FIRST and CORRESPONDING author (with S. Schrod; O. Stegle senior)***

**Problem:** Single-cell analysis is shifting from descriptive atlasing toward inferring causal and mechanistic relationships — explaining not just *how* but *why* cells differ. A proliferation of ML methods for identifying dependencies and extrapolating perturbation effects has left the field fragmented, with inconsistent terminology across specialized subfields and no principled guide for method selection.

**Approach:** A review that connects methods by their shared modelling concepts rather than surface features. It proposes a unifying, multi-layered ontology positioning each method along three axes: the causal signatures it leverages (from endogenous/observational vs deliberate/interventional perturbations, profiled across temporal, spatial, and multi-omic layers), the computational task it addresses, and the recurring modelling concepts it embodies.

**Key contributions:** Five core modelling concepts (Box 1) — representation learning, causal inference (Pearl's do-calculus), mechanistic discovery, disentanglement, and population tracing (optimal transport / flow matching / Schrödinger bridges) — each with explicit stated assumptions. The ontology progresses from single-gene alterations → gene programmes → directed regulatory mechanisms, plus effect extrapolation to unseen contexts, perturbations, and combinations, and an iterative experiment-prediction "Guide" loop. A queryable, extendable online resource holds per-method technical detail.

**Data & tools:** Comprehensive tables of interventional technologies (Perturb-seq, FiCS Perturb-seq, ECCITE-seq, CROP-seq, Mix-seq, Mosaic, spatial screens Perturb-Map/CRISPRmap/PERTURB-CAST) and 200+ computational tools mapped to tasks (differential analysis, responsiveness, linear/nonlinear gene programmes, GRNs, causal structure, effect prediction, OT-based tracing). Covers foundation models (scGPT, scPRINT, Geneformer) and their causal-reasoning limits.

**Relevance to future work:** The authoritative conceptual scaffold for Daniel's perturbation-modelling agenda. Any agent building single-cell causal/perturbation models should use its ontology to situate a method, identify which assumptions apply, and select benchmarks — and note the recurring caveat that expressive nonlinear/deep models trade interpretability for predictive power.
