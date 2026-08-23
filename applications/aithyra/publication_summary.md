# Publication Summary — three most important papers

<!-- Requirement: up to 3 papers, comment ≤100 words each incl. contribution. Recounted v6 (style pass 2026-08-23): 78 / 74 / 87 words (all ≤100 with margin). Citations: Google Scholar 2026-07-21 [refresh at submission]. Contribution sentences mirror the papers' published contribution statements (verified: Nat Commun PDF; NCB PDF: "D.D. and J.S.R. conceived the project. D.D. developed the software, carried out the case studies and drafted the manuscript."). Slot 3 decided 2026-08-22 with the candidate: Cellina (public arXiv preprint — the only citable artifact showing both a causal method and PI-mode supervision); the NRG Perspective remains foregrounded in the research statement. -->

**1. Dimitrov D, et al. Comparison of methods and resources for cell–cell communication inference from single-cell RNA-Seq data. *Nature Communications* 13, 3224 (2022). 706 citations.**

Sole first author: I set up the LIANA framework, performed the comparisons and evaluations, and guided the robustness analysis. This is the cell–cell communication field's reference benchmark: a systematic comparison of 16 interaction resources and 7 inference methods, showing that predictions depend strongly on both choices and motivating the consensus approach the field has since adopted. It seeded the LIANA software line (>300,000 downloads) and the commitment to evaluation that my proposed programme carries from descriptive to counterfactual inference.

---

**2. Dimitrov D, et al. LIANA+ provides an all-in-one framework for cell–cell communication inference. *Nature Cell Biology* 26, 1613–1622 (2024). 300 citations.**

Sole first author; I co-conceived the project, developed the software (liana-py), carried out the case studies, and drafted the manuscript. LIANA+ is the field's standard framework for inferring inter- and intracellular signalling from single-cell, spatial and multi-omics data across conditions, downloaded more than 300,000 times and independently adopted across the scverse ecosystem. It is the platform in which my group's models will ship, giving every new method an immediate route to thousands of users.

---

**3. Moeed A, Schrod S, Rohbeck M, Bonder MJ, Lutsik P, Stegle O†, Dimitrov D†. Querying counterfactuals on tissue graphs with supervised disentanglement (Cellina). arXiv preprint (2026). *Submitted to NeurIPS, 2026* (†co-corresponding; D.D. last author.)**

Last and co-corresponding author (with O. Stegle); first-authored by a PhD student under my day-to-day supervision. Cellina represents tissue as a graph and formalizes counterfactual perturbations of a cell's neighbourhood, using supervised disentanglement to separate intrinsic identity from microenvironmental context. Across benchmarks spanning over 2.5 million cells, its best variant leads the strongest baseline by +0.17 on both Pearson correlation and signed precision of predicted perturbation-induced expression changes. It is the founding method of my proposed programme, and the first study I have supervised end-to-end as senior author.
