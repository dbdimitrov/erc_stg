## Defining and benchmarking open problems in single-cell analysis

*Luecken et al., Nature Biotechnology (2025) · **Author role: Contributing author (middle)***

**Problem:** Over 1,700 single-cell analysis algorithms exist, but benchmarks that guide method selection are non-standardized, static, and often self-serving — developers pick datasets/metrics that flatter their own tools. Existing benchmarks of the same task (e.g., four batch-integration benchmarks) share <10% of datasets/metrics and disagree on the best method, and their result-paper format cannot be updated as the field evolves.

**Approach:** Open Problems is an open-source, extensible, community-guided living benchmarking platform (https://openproblems.bio; https://github.com/openproblems-bio/openproblems). Each task decomposes into datasets (input + ground truth), methods, and metrics, built as Viash components (single Bash/Python/R scripts + config.vsh.yaml) run in versioned Docker containers on cloud infrastructure. New methods are added via pull request, auto-tested in the cloud, and results auto-published. Every method is scored on every dataset by every metric, ranked by average normalized score.

**Key contributions:** 12 tasks (9 base + subtasks), 81 datasets, 171 methods, 37 metrics, defined through GitHub, weekly meetings, and a 2021 hackathon. Delivers neutral best-practice recommendations (e.g., logistic regression beats complex models for label projection; simple models win for perturbation prediction). Seeded NeurIPS 2021/2022 multimodal-integration competitions (260 and 1,600+ participants).

**Data & tools:** openproblems repo, nbt2025-manuscript (figures), Viash, Docker, data from Figshare and CELLxGENE. CCC task methods: CellPhoneDB, LIANA, SingleCellSignalR, Connectome, NATMI. Ties to Single-Cell Best Practices (https://www.sc-best-practices.org/).

**Relevance to future work:** Daniel Dimitrov co-led the cell–cell communication (CCC) task, which found that expression-magnitude methods (CellPhoneDB, LIANA's ensemble) beat specificity-based ones, and max aggregation beats mean — direct evidence informing LIANA+ design. Agents evaluating CCC or any single-cell method should use Open Problems as the neutral, reusable benchmarking standard rather than bespoke comparisons.
