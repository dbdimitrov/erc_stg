## Combining LIANA and Tensor-cell2cell to decipher cell-cell communication across multiple samples

*Baghdassarian et al., Cell Reports Methods (2024) · **Author role: CO-FIRST author (with H. Baghdassarian)***

**Problem:** CCC results are highly tool-dependent, and most tools analyze single samples or only pairwise comparisons. As sample numbers and experimental-design complexity grow, a versatile, method-agnostic workflow is needed to identify coordinated CCC programs across many samples/conditions.

**Approach:** A step-by-step protocol integrating two adapted tools: LIANA (method/resource selection and per-sample ligand-receptor scoring, including its RobustRankAggregate consensus over CellPhoneDBv2, CellChat, SingleCellSignalR, NATMI, Connectome, log2FC, geometric mean) and Tensor-cell2cell (non-negative tensor component analysis on a 4D communication tensor of ligand-receptor x sender x receiver x sample). LIANA outputs pass directly into a communication tensor via `li.multi.to_tensor_c2c`; decomposition yields context-driven CCC programs (factors) with loadings per dimension. Covers preprocessing (scanpy), QC/normalization, method/resource choice (recommends a magnitude-reflecting score, `magnitude_rank`, since specificity's cross-sample behavior is unclear), tensor-building options (`how`: inner/outer/outer_lrs/outer_cells; `outer_fraction`), rank selection via elbow analysis, robust vs regular TF optimization, GPU acceleration (PyTorch/tensorly), and downstream pathway-enrichment interpretation (decoupler).

**Key contributions:** A unified, reproducible, GPU-enabled Python and R workflow (~1.5 h for 63k cells, 10 cell types, 12 samples) demonstrating that Tensor-cell2cell recovers consistent CCC programs regardless of the underlying LIANA method. Showcased on BALF COVID-19 severity data (control/moderate/severe), with additional tutorials on lupus PBMCs and myocardial-infarction spatial data.

**Data & tools:** ccc-protocols tutorials (https://ccc-protocols.readthedocs.io/), Python and R. Packages: `cell2cell` (Tensor-cell2cell), `liana`, `decoupler`, `scanpy`, `tensorly`, PyTorch. COVID-19 BALF dataset (Zenodo 10.5281/zenodo.7706962, Liao et al.). Resources via OmniPath (consensus resource).

**Relevance to future work:** The canonical recipe for multi-sample, context-resolved CCC program discovery combining Daniel's LIANA with Tensor-cell2cell; the entry point for cross-condition CCC analyses and a template for coupling LIANA outputs with tensor/factorization methods.
