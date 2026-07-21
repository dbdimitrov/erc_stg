## Querying Counterfactuals on Tissue Graphs with Supervised Disentanglement

*Moeed et al., arXiv preprint (2026) · **Author role: LAST author & co-corresponding (with O. Stegle)***

**Problem:** Predicting how a cell's expression would change under altered spatial neighbor context ("tissue graph counterfactuals") lacks a unified definition. Existing perturbation models assume shared stimuli applied uniformly and treat cells as i.i.d., violating the reality that each cell's state is shaped by a unique local neighborhood.

**Approach:** The authors first formalize tissue graph counterfactuals as two spatial intervention classes: edge perturbation (rewiring a cell's neighborhood N(v) to an alternative neighbor pool) and node perturbation (modifying neighbor feature vectors on a gene subset via a gene-specific transformation T_g). Cellina is a graph VAE with a Negative Binomial likelihood that factorizes each cell into an intrinsic latent z (cell identity) and an extrinsic latent s (spatial microenvironment), decoding p(x|z,s). Disentanglement is enforced by supervision: a cell-type classifier anchors z, an adversarial domain discriminator strips spatial-domain information from z, routing it to s. Two variants: base Cellina (degree-normalized MLP aggregation of neighbor expression) and Cellina-GAT (GATv2 message passing plus a graph-supervised contrastive loss on s). Training alternates discriminator and VAE-encoder/decoder steps.

**Key contributions:** A unified framework for edge/node tissue counterfactuals; a dual-encoder graph VAE that beats spatially-informed (MintFlow, SpatialProp, SIMVI) and non-spatial (scGen, CPA, mean-shift) baselines on Pearson, Signed Precision, RMSE_LFC across 2.4M CRC cells and a mouse-brain MERFISH cohort; unsupervised discovery of CRC subdomains (TGFB-dominant CRC1, NFkB/MAPK CRC2) with PROGENy-guided pathway-targeted neighbor perturbations recapitulating FN1/MMP3 fibroblast programs.

**Data & tools:** Code https://github.com/PMBio/cellina, reproducibility https://github.com/PMBio/cellina-reproducibility, tutorials https://cellina.readthedocs.io. CRC data (Crowell et al.) from Zenodo https://zenodo.org/records/15574384; mouse-brain MERFISH (Zhang et al.) from CZI CELLxGENE. Uses GATv2, PyTorch Geometric, scanpy, PROGENy, Hotspot.

**Relevance to future work:** Cellina is Daniel's flagship spatial-counterfactual/virtual-cell method, formalizing neighborhood interventions and providing the disentanglement primitives (intrinsic vs extrinsic latents) an agent should build on for tissue-level perturbation modeling.
