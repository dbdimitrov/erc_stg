# inflow + LRIC + MOFA-Flex: cell–cell communication across scales in next-generation spatial data

*Planned submission: Nature Methods · target: bioRxiv preprint concurrent with journal submission, H1 2027 · **Author role: corresponding, most likely last — the senior-author transition on the candidate's own LIANA line** · Status: methods implemented in LIANA+ (`mofaflow` branch of [saezlab/liana-py](https://github.com/saezlab/liana-py)); benchmarks and applications in progress, student-led.*

**Problem:** Next-generation spatial transcriptomics (Atera, Xenium 5K, CosMx 18K) now delivers transcriptome-wide coverage at genuine single-cell resolution, but cell–cell communication methods still behave as if the old trade-offs held: they aggregate by cell type (averaging away localized signalling heterogeneity), score ligand–receptor pairs agnostic of who is sending, ignore the spatial length scale of each interaction (conflating contact-dependent and long-range signalling — a known false-positive driver), and mostly stop at single slides, with no route to communication programs across samples, conditions, or timepoints.

**The idea — one ladder, three scales, one framework.** The paper climbs the scales in order, all inside LIANA+:

- **inflow (per cell):** a spatially informed *trivariate* statistic — source cell identity × ligand availability → receptor expression — scoring interaction strength *and* directionality at the level of individual cells, with no cell-type aggregation. The source axis takes one-hot labels or continuous cell-type matrices (e.g., deconvolution proportions), and protein complexes are handled natively.
- **LRIC (per interaction):** Ligand–Receptor Interaction Correlation, an expression-weighted cross pair-correlation function: g(r) asks whether ligand- and receptor-expressing cells are co-enriched at distance r *beyond what cell-type co-localization alone predicts*, recovering each interaction's characteristic length scale (contact vs long-range). The unweighted cross-PCF ships alongside as the pure tissue-architecture baseline.
- **MOFA-Flex (per cohort):** inflow scores feed a recent multi-view factor framework (bioFAM's MOFA-Flex) to extract shared versus sender-specific communication programs across samples and conditions — with multi-sample spatial layout support already landed.

Beneath all three sits a harmonized, annotated ligand–receptor resource (multimeric complexes, pathway and functional annotations) — the prior-knowledge layer the LIANA line is known for.

**Evidence to date:** all three methods are implemented and tutorial-verified in liana-py (per-cell inflow scoring; LRIC/cross-PCF with plotting; the end-to-end inflow→MOFA-Flex workflow on mouse brain), and an early CRC analysis shows interactions that co-localize within tissue subregions with condition-specific distributions shared across patients. **Planned before submission:** the benchmark suite (spatial metrics + parameter sweeps across CRC, Atera-breast, and Crohn's datasets), LRIC multi-sample statistics, receiver-side signalling with downstream TF activity, and resource finalization. Applications (Crohn's fistulae FAS niches, CRC malignancy, Atera breast/cervical) are student-led and preliminary.

**Relevance (group-leader narrative, in brief):** this is the independence signal — corresponding (likely last) author on the ecosystem the candidate created, showing the LIANA line now produces methods under their direction rather than by their hand. It is complementary to KIARA, not overlapping: the LIANA stack provides community-facing statistical screens over ligand–receptor prior knowledge; KIARA quantifies context effects model-side — the screens generate the hypotheses the models decompose.

---

## Status & open items (concise firewall)

- **Demonstrated:** inflow, LRIC/cross-PCF, and the MOFA-Flex integration implemented with executed tutorials; early CRC finding as above.
- **Planned:** the entire benchmark half (metrics, sweeps, three datasets); LRIC multi-sample statistics; the receiver-side + TF extension already promised in the draft abstract — it must land or be cut from the abstract before submission.
- **Preliminary:** all three applications (student-led); the optional SOFA arm; the resource's final interaction count (currently "~N" in the intro).
