Resource 


## Combining LIANA and Tensor-cell2cell to decipher cell-cell communication across multiple samples 

#### Graphical abstract 


#### Authors 

Hratch M. Baghdassarian, Daniel Dimitrov, Erick Armingol, Julio Saez-Rodriguez, Nathan E. Lewis 

#### Correspondence 

pub.saez@uni-heidelberg.de (J.S.-R.), nlewisres@ucsd.edu (N.E.L.) 


#### In brief 

By integrating LIANA and Tensorcell2cell, Baghdassarian et al. provide a unified protocol for unsupervised analysis of cell-cell communication (CCC) across multi-sample single-cell datasets. By facilitating CCC method selection and identification of context-driven communication programs, this approach garners insights into diverse biological processes. This work is accompanied by user-friendly tutorials for both Python and R. 

#### Highlights 

- d Integrated LIANA and Tensor-cell2cell for cell-cell communication analysis across samples 

- d Enables flexible selection of methods and resources for cellcell communication inference 

- d Provides step-by-step analysis, accompanied by online tutorials in Python and R 

- d Demonstrates broad applicability to single-cell data in diverse biological conditions 


Baghdassarian et al., 2024, Cell Reports Methods 4, 100758 April 22, 2024 ª 2024 The Author(s). Published by Elsevier Inc. https://doi.org/10.1016/j.crmeth.2024.100758 

**ll** 


**ll** OPEN ACCESS 


### Resource 

# Combining LIANA and Tensor-cell2cell to decipher cell-cell communication across multiple samples 

Hratch M. Baghdassarian,<sup>1,2,5</sup> Daniel Dimitrov,<sup>3,5</sup> Erick Armingol,<sup>1,2,5</sup> Julio Saez-Rodriguez,<sup>3,6,</sup> * and Nathan E. Lewis<sup>2,4,6,7,</sup> * 

1Bioinformatics and Systems Biology Graduate Program, University of California, San Diego, La Jolla, CA 92093, USA 

2Department of Pediatrics, University of California, San Diego, La Jolla, CA 92093, USA 

3Heidelberg University, Faculty of Medicine, and Heidelberg University Hospital, Institute for Computational Biomedicine, 69120 Heidelberg, Germany 

4Department of Bioengineering, University of California, San Diego, La Jolla, CA 92093, USA 

5These authors contributed equally 

6Senior author 

7Lead contact 

*Correspondence: pub.saez@uni-heidelberg.de (J.S.-R.), nlewisres@ucsd.edu (N.E.L.) https://doi.org/10.1016/j.crmeth.2024.100758 

MOTIVATION Multiple cell-cell communication (CCC) tools exist, yet results are specific to the tool of choice due to the diverse assumptions made across computational frameworks. Moreover, tools are often limited to analyzing single samples or performing pairwise comparisons. As experimental design complexity and sample numbers continue to increase in single-cell datasets, so does the need for versatile methods to decipher cell-cell communication in such scenarios. By integrating LIANA and Tensor-cell2cell, we present a protocol that enables the use of a diverse array of tools and resources to assess interpretable CCC programs across multiple samples. 

###### SUMMARY 

In recent years, data-driven inference of cell-cell communication has helped reveal coordinated biological processes across cell types. Here, we integrate two tools, LIANA and Tensor-cell2cell, which, when combined, can deploy multiple existing methods and resources to enable the robust and flexible identification of cell-cell communication programs across multiple samples. In this work, we show how the integration of our tools facilitates the choice of method to infer cell-cell communication and subsequently perform an unsupervised deconvolution to obtain and summarize biological insights. We explain how to perform the analysis step by step in both Python and R and provide online tutorials with detailed instructions available at https://ccc-protocols.readthedocs.io/. This workflow typically takes �1.5 h to complete from installation to downstream visualizations on a graphics processing unit-enabled computer for a dataset of �63,000 cells, 10 cell types, and 12 samples. 

###### INTRODUCTION 

Cell-cell communication (CCC) coordinates higher-order biological functions in multicellular organisms,<sup>1,2</sup> dictating phenotypes in response to different contexts such as disease state, spatial location, and organismal life stage. In recent years, many tools have been developed to leverage single-cell and spatial transcriptomics data to study CCC events driving various biological processes.<sup>2–4</sup> While each computational strategy contributes unique and valuable developments, many are tool specific and challenging to integrate due to the large number of different inference methods and resources housing prior knowledge.<sup>2,5–7</sup> Moreover, most tools do not account for the relationships of 

coordinated CCC events (CCC programs) across different contexts,<sup>8</sup> either disregarding context altogether by analyzing samples individually or being limited to pairwise comparisons. Thus, as the ability to generate large single-cell and spatial transcriptomics datasets and the interest in studying CCC programs continue to increase,<sup>9–11</sup> the need to robustly decipher CCC is becoming essential. 

###### Comparison with other methods 

A plethora of ligand-receptor (LR) methods have emerged, most of which were published with their own resources.<sup>1,5,12</sup> Many of these provide distinct scoring functions to prioritize interactions, yet studies have reported low agreement between their 


Cell Reports Methods 4, 100758, April 22, 2024 ª 2024 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). 

1 


![Figure 1. Integration of LIANA and Tensor-](figures/liana-tensor-cell2cell/page-003-03.png)

**ll** OPEN ACCESS 

### Resource 

the key inputs of our tools. Then, we guide the selection of methods and prior-knowledge resources to score intercellular communication using LIANA’s consensus method and resource to infer the potential CCC events for each sample. We use Tensor-cell2cell to summarize the intercellular communication events across samples, and we describe key technical considerations to enable consistent decomposition results. Finally, we guide the interpretation of the decomposition results and show multiple downstream analyses and visualizations to facilitate interpretation of the context-dependent CCC programs. For example, we illustrate how biologically relevant results can be obtained by coupling the outputs with pathway enrichment analyses. We also provide quick-start and in-depth online tutorials with detailed descriptions of all steps described in this protocol and their crucial parameters. All these materials are available in both Python and R at https://ccc-protocols.readthedocs.io/. While here we showcase an analysis on coronavirus disease 2019 (COVID-19) data, online tutorials also show applications on transcriptomics data of lupus peripheral blood mononuclear cells and spatial transcriptomics data of myocardial infarction, further demonstrating the adaptability of our combined tools. Collectively, these materials provide a comprehensive and flexible playbook to investigate CCC from single-cell transcriptomics. 

###### Applications of the protocol 

LIANA and Tensor-cell2cell have been used for diverse purposes. LIANA was initially used to compare and evaluate different ligand-receptor methods in diverse biological contexts. Tensor-cell2cell was originally applied to link CCC programs with different severities of COVID-19 and autism spectrum disorder (ASD).<sup>12</sup> Briefly, LIANA evaluated different methods and showed that they have limited agreement in terms of communication mechanisms,<sup>5,12</sup> while Tensorcell2cell revealed distinct CCC program dysregulations associated with severe COVID-19 specifically rather than moderate cases, as well as combinations of programs distinguishing ASD from neurotypical samples. Notably, LIANA provides a consensus resource and can aggregate multiple methods into consensus communication scores. Additionally, there is a natural complementarity between the two tools, as Tensorcell2cell can use input scores from any CCC method (Figure 1) and generates consistent decomposition results across methods. Thus, our tools are highly generalizable and applicable to the analysis of any single-cell transcriptomics datasets. For example, LIANA has been used for the analysis of myocardial infarction<sup>22</sup> and transforming growth factor b signaling in breast cancer,<sup>23</sup> among others. Our tools are also applicable to other data modalities containing potentially interacting cell populations. Specifically, one can adapt LIANA or use existing spatial tools<sup>24</sup> and combine their outputs with Tensor-cell2cell to generate spatially informed CCC insights across contexts. Similarly, one can also obtain metabolite-mediated intercellular interactions<sup>25,26</sup> and decompose those into patterns across contexts with Tensor-cell2cell.<sup>27</sup> One can also apply Tensor-cell2cell to extract CCC programs occurring at specific tissues<sup>28</sup> or at a whole-body organism level.<sup>28,29</sup> In this protocol, we focus on how one can leverage 

the different CCC methods and resources, generalized by LIANA, to infer context-dependent CCC programs with Tensor-cell2cell from single-cell transcriptomics data. 

###### RESULTS 

In this section, we introduce our protocol (Figure 2) using Python. The same protocol is implemented in R and is available online at https://ccc-protocols.readthedocs.io/en/latest/notebooks/ccc_ R/QuickStart.html. 

###### Step 1: Installation and environment setup 

Install Anaconda or Miniconda through the official instructions at https://docs.anaconda.com/anaconda/install/index.html. 

Then, open a terminal to create and activate a conda environment. 

|conda create -n ccc_protocols|
|---|
|conda activate ccc_protocols|


If you will be using a graphics processing unit (GPU), then install PyTorch using conda. 

conda install pytorch torchvision torchaudio pytorchcuda=11.8 -c pytorch -c nvidia 

Install Tensor-cell2cell, LIANA, and decoupler using PyPI. 

|pip install cell2cell liana decoupler|
|---|


For fully reproducible runs of our tutorials in both Python and R, we have specified the required packages and their versions in the software requirements table (STAR Methods). You can also follow instructions in the environment setup section to install a clean virtual environment with all package requirements. 

Notebooks to run this tutorial can be created by starting a Jupyter Notebook. 

|jupyter notebook|
|---|


###### Step 2: Initial setups 

First, if you are using an NVIDIA GPU with Compute Unified Device Architecture (CUDA) cores, then set ‘‘use_gpu = True’’ and enable PyTorch with the following code block. Otherwise, set ‘‘use_gpu = False’’ or skip this part. 

|use_gpu = True|
|---|
|if use_gpu:|
|import tensorly as tl|
|tl.set_backend(’pytorch’)|


Cell Reports Methods 4, 100758, April 22, 2024 3 


**ll** OPEN ACCESS 

Resource 


Then, import all the packages we will use in this tutorial. 

import cell2cell as c2c import liana as li import pandas as pd import decoupler as dc import scanpy as sc import matplotlib.pyplot as plt %matplotlib inline import plotnine as p9 import seaborn as sns 

percent_top=None, log1p=False, inplace=True) adata = adata[adata.obs.pct_counts_mt < 15, :] 

This is followed by removing cells with a high number of total unique molecular identifier (UMI) counts, potentially representing more than one single cell (doublets): 

adata = adata[adata.obs.n_genes < 5500,:] 

Afterward, specify the data and output directories. 

data_folder = ’../../data/quickstart/’ output_folder = ’../../data/quickstart/outputs/’ c2c.io.directories.create_directory(data_folder) c2c.io.directories.create_directory(output_folder) 

We begin by loading the single-cell transcriptomics data. For this tutorial, we will use a lung dataset of 63,000 immune and epithelial cells across three control, three moderate, and six severe COVID-19 patients (Zenodo Data: https://doi.org/10.5281/ zenodo.7706962).<sup>30</sup> We use a convenient function to download the data and store it in the AnnData format, on which the scanpy<sup>31</sup> package is built. 

adata = c2c.datasets.balf_covid(data_folder + ’/LiaoBALF-COVID-19.h5ad’) 

###### Step 3: Data preprocessing 

Data preprocessing is crucial for the correct application of this (Figure 2A). Here, we only highlight the essential steps. However, other aspects of data preprocessing should be considered and performed according to the best practices of single-cell analysis (https://github.com/theislab/single-cell-best-practices). Quality control (timing: <5 min) 

The loaded data have already been preprocessed to a degree and come with cell annotations. Nevertheless, we highlight some of the key steps. To mitigate noise, we filter non-informative cells and genes. 

sc.pp.filter_cells(adata, min_genes=200) sc.pp.filter_genes(adata, min_cells=3) 

We additionally remove a high mitochondrial content. 

Caution: Here, we covered the absolute basics. We omit other common practice steps, such as the removal of doublets and cells with high ribosomal content and the correction of ambient RNA. Additionally, in certain scenarios, particularly in those where technical variation is expected to be notable, the application of quality control steps by sample is desirable.<sup>21</sup> Normalization (timing: <2 min) 

We have now removed the majority of noisy readouts and can proceed to count normalization, as most CCC tools typically use normalized count matrices as input. Normalized counts are usually obtained in two essential steps, the first being count depth scaling, which ensures that the measured count depths are comparable across cells. This is then usually followed up with log1p transformation, which stabilizes the variance of the counts and enables the use of linear metrics downstream. 

# Save the raw counts to a layer adata.layers["counts"] = adata.X.copy() # Normalize the data 

sc.pp.normalize_total(adata, target_sum=1e4) sc.pp.log1p(adata) 

###### Critical: A key parameter of this command is as follows: 

- d ‘‘target_sum’’ ensures that after normalization, each observation (cell) has a total count equal to that number. 

These normalization steps ensure that the aggregation of cells into cell types, a common practice for CCC inference, is done on comparable cells with approximately normally distributed feature values. 

Troubleshooting: Expression matrices with ‘‘not a number’’ (nan), negative, or infinity (inf) values cause errors. Users should stick to common normalization techniques, and any nan, negative, or inf values must be filled to avoid errors. 

###### Step 4: Inferring CCC 

adata.var[’mt’] = adata.var_names.str.startswith (’MT-’) sc.pp.calculate_qc_metrics(adata, qc_vars=[’mt’], 

Following preprocessing of the single-cell transcriptomics data, we proceed to the inference of potential CCC events (Figure 2B). In this case, we will use LIANA to infer the ligand-receptor interactions for each sample. LIANA is available in Python and R and supports Scanpy, SingleCellExperiment, and Seurat 

4 Cell Reports Methods 4, 100758, April 22, 2024 


Cell Reports Methods 

— <mark>=</mark> 


![Figure 2. Overview of the protocol for inferring cell-cell communication through LIANA and Tensor-cell2cell](figures/liana-tensor-cell2cell/page-006-06.png)


**ll** OPEN ACCESS 

### Resource 


Figure 3. LIANA is a user-friendly and modular ligand-receptor analysis framework LIANA provides a variety of methods and resources to infer cell-cell communication, making it easy to use multiple existing methods in a coherent manner. It also provides consensus scores and resources to provide generalized results. Figure was adapted from Dimitrov et al.<sup>5</sup> 

LIANA classifies the scoring functions from the different methods into two categories: those that infer the ‘‘magnitude’’ and ‘‘specificity’’ of interactions. The magnitude of an interaction is a measure of the strength of the interaction, and the specificity of an interaction is a measure of how specific an interaction is to a given pair of cell groups. Generally, these categories are complementary, and the magnitude of the interaction is often in agreement with the specificity of the interaction. In other words, a ligand-receptor interaction with a high magnitude score in a given pair of cell types is likely to also be specific, and vice versa. 

###### Selecting a method to infer CCC 

While there are many commonalities between the different methods implemented in LIANA, there also are many variations and different assumptions affecting how the magnitude and specificity scores are calculated (see STAR Methods). These variations can result in limited agreement in inferred predictions when using different CCC methods.<sup>5,13,14</sup> To this end, in LIANA, we additionally provide a ‘‘rank_aggregate’’ score, which can be used to aggregate any of the scoring functions above into a consensus score. 

By default, LIANA calculates an aggregate rank using a re-implementation of the RobustRankAggregate method<sup>36</sup> and generates a probability distribution for ligand-receptors that are ranked consistently better than expected under a null hypothesis (see STAR Methods). The consensus of ligand-receptor interactions across methods can therefore be treated as a p value. We show in detail how LIANA’s rank aggregate or any of the individual methods can be used to infer communication events from a single sample or context at ‘‘Python Tutorial 02 InferCommunication-Scores’’ (https://ccc-protocols.readthedocs. io/en/latest/notebooks/ccc_python/02-Infer-CommunicationScores.html). 

Critical: When using LIANA with Tensor-cell2cell, we recommend selecting a scoring function that reflects the magnitude of the interactions, as how the interactions’ specificity relates to changes across samples is unclear. In this protocol, we will use the ‘‘magnitude_rank’’ scoring function from LIANA, under the assumption that ensemble ap- 

proaches are potentially less biased than any single method alone.<sup>15</sup> 

We further show that Tensor captures consistent CCC programs when using different methods and add a tutorial to explore method consistency on any dataset: https://cccprotocols.readthedocs.io/en/latest/notebooks/ccc_python/S3B_ Score_Consistency.html. 

Troubleshooting: The default decomposition method of Tensor-cell2cell is a non-negative tensor component analysis, which, as implied, expects non-negative values as the inputs. Thus, when selecting the method of choice, make sure that you do not have negative CCC scores. If so, you can replace them by zeros or the minimum positive value. 

###### Selecting ligand-receptor resources 

When considering ligand-receptor prior-knowledge resources, a common theme is the trade-off between coverage and quality, and similarly, each resource comes with its own biases.<sup>5</sup> LIANA takes advantage of OmniPath,<sup>37</sup> which includes expert-curated resources of CellPhoneDBv2,<sup>32</sup> CellChat,<sup>19</sup> ICELLNET,<sup>38</sup> connectomeDB2020,<sup>34</sup> and CellTalkDB,<sup>39</sup> as well as 10 others.<sup>5,37</sup> LIANA further provides a consensus expert-curated resource from the aforementioned five resources, along with some curated interactions from SignaLink.<sup>40</sup> In this protocol, we will use the consensus resource from LIANA, though any of the other resources are available via LIANA, and one can also use LIANA with their own custom resource. 

Selecting any of the lists of ligand-receptor pairs in LIANA can be done through the following command. 

lr_pairs = li.resource.select_resource(’consensus’) 

Here, ‘‘consensus’’ indicates the use of LIANA’s consensus resource, but it can be replaced by any other available resource (e.g., ‘‘cellphonedb,’’ ‘‘cellchatdb,’’ ‘‘connectomeDB,’’ etc.). 

Note that any of the resources available in LIANA can be used by passing them as a string to ‘‘resource_name.’’ All of LIANA’s 

6 Cell Reports Methods 4, 100758, April 22, 2024 


![Figure 3. LIANA is a user-friendly and modular](figures/liana-tensor-cell2cell/page-007-07.png)

**ll** OPEN ACCESS 

### Resource 

resources can be listed with ‘‘li.resource.show_resources().’’ Users can also provide custom resources as a pandas DataFrame to run in LIANA so long as they are formatted the same as other resources (i.e., include two columns named ligand and receptor, containing the respective partners in the ligand-receptor interactions). Hence, users may pass a dataframe containing a personalized list of interactions to liana using the ‘‘resource’’ parameter in the next ‘‘rank_aggregate’’ function below. 

Troubleshooting: Users should choose a resource with gene identifiers and an organism that corresponds to that of their data. By default, LIANA uses human gene symbol identifiers but additionally provides a murine resource as well as functionalities to convert via orthology to other organisms. Running LIANA for each sample (timing: 4 min) 

Here, we will run LIANA’s ‘‘rank_aggregate’’ with six methods (by default, CellPhoneDBv2, CellChat, SingleCellSignalR, NATMI, Connectome, and log2FC) on all of the samples in the dataset. 

at least 10% of the cells (by default) in both clusters involved in the interaction. Any interactions that do not pass these criteria are not returned by default. To return those, the user can use the ‘‘return_all_lrs’’ parameter. These results will later be used to generate a tensor of ligand-receptor interactions across contexts that will be decomposed into CCC programs by Tensor-Cell2cell. Thus, how non-expressed interactions are handled is critical to consider when building the tensor later on (see ‘‘Python Tutorial 03 Generate-Tensor’’ (https:// ccc-protocols.readthedocs.io/en/latest/notebooks/ccc_python/ 03-Generate-Tensor.html). 

One can visualize the output as a dot plot while including every sample in the dataset. 

li.pl.dotplot_by_sample(adata=adata, colour=’magnitude_rank’, size=’specificity_rank’, 


source_labels=["B", "pDC", "Epithelial"], 

li.mt.rank_aggregate.by_sample(adata, sample_key=’sample_new’, 

groupby=’celltype’, resource_name=’consensus’, expr_prop=0.1, min_cells=5, n_perms=100, use_raw=False, verbose=True, inplace=True ) 

###### Critical: Key parameters here are as follows: 

- d ‘‘adata’’ stands for AnnData, the data format used by scanpy.<sup>31</sup> 

- d ‘‘sample_key’’ corresponds to the sample identifiers, available as a column in the ‘‘adata.obs’’ dataframe. 

- d ‘‘groupby’’ corresponds to the cell group label stored in ‘‘adata.obs.’’ 

- d ‘‘resource_name’’ is the name of any of the resources available via LIANA. 

- d ‘‘expr_prop’’ is the expression proportion threshold (in terms of cells per cell type expressing the protein) for any protein subunit involved in the interaction, according to which we keep or discard the interactions. 

- d ‘‘min_cells’’ is the minimum number of cells per cell type required for a cell type to be considered in the analysis. 

- d ‘‘n_perms’’ is the number of permutations for p value estimation. 

- d ‘‘use_raw’’ is a Boolean that indicates whether to use the ‘‘adata.raw’’ slot; here, the log-normalized counts are assigned to ‘‘adata.X,’’ and other options include passing the name of a layer via the ‘‘layer’’ parameter or using the counts stored in ‘‘adata.raw.’’ 

Critical: LIANA considers interactions as occurring only if the ligand and receptor, and all of their subunits, are expressed in 

target_labels=["Macrophages", "Mast", "pDC", "NK"], ligand_complex=[’VIM’, ’SCGB3A1’], receptor_complex=[’CD44’, ’MARCO’], sample_key=’sample_new’, inverse_colour=True, inverse_size=True, figure_size=(14, 10), size_range=(1, 6), ) 

Key parameters here are as follows: 

- d ‘‘source_labels’’ is a list containing the names of the sender cells of interest. 

- d ‘‘target_labels’’ is a list containing the names of the receiver cells of interest. 

- d ‘‘ligand_complex’’ is a list containing the names of the ligands of interest. 

- d ‘‘receptor_complex’’ is a list containing the names of the receptors of interest. 

- d ‘‘sample_key’’ is a string containing the column name where samples are specified. 

This command leads to the generation of Figure 4. 

Pause point: We can export the LIANA results by sample to a CSV and save them for later use. 

adata.uns[’liana_res’].to_csv(output_folder + ’/LIANA_by_sample.csv’, index=False) 

Alternatively, one could just export the whole AnnData object, together with the ligand-receptor results stored at ‘‘adata.uns [‘liana_res’].’’ 

adata.write_h5ad(output_folder + ’/adata_processed. h5ad’, compression=’gzip’) 

Cell Reports Methods 4, 100758, April 22, 2024 7 


![Figure 4. Dot plot of cell-cell communication](figures/liana-tensor-cell2cell/page-009-09.png)

**ll** OPEN ACCESS 

### Resource 

   - ‘‘outer’’ considers all cell types and ligand-receptor pairs that are present across contexts (union). 

   - ‘‘outer_lrs’’ considers only cell types that are present in all contexts (intersection) but all ligand-receptor pairs that are present across contexts (union). 

   - ‘‘outer_cells’’ considers only ligand-receptor pairs that are present in all contexts (intersection) but all cell types that are present across contexts (union). 

- d ‘‘outer_fraction’’ controls the elements to include in the union scenario of the how options. Only elements that are present at least in this fraction of samples/contexts will be included. When this value is 0, the tensor includes all elements across the samples. When this value is 1, it acts as using how = ‘‘inner.’’ 

- d ‘‘context_order’’ is a list specifying the order of the samples. The order of samples does not affect the results, but it is useful for posterior visualizations. 

We can check the shape of this tensor to verify the number of samples, ligand-receptor pairs, sender cells, and receiver cells, respectively: 

tional metadata. If you want to include metadata about major groups for those dimensions, then you have to replace the corresponding ‘‘None’’ with a dictionary as described before. 

Pause point: We can export our tensor and its metadata for performing the tensor decomposition later: 

c2c.io.export_variable_with_pickle(variable=tensor, filename=output_folder + ’/Tensor.pkl’) c2c.io.export_variable_with_pickle(variable=meta_ tensor, 

filename=output_folder + ’/Tensor-Metadata.pkl’) tensor = c2c.io.read_data.load_tensor (output_folder + ’/Tensor.pkl’) meta_tensor = c2c.io.load_variable_with_pickle (output_folder + ’/Tensor-Metadata.pkl’) 

###### Then, we can load them with: 


tensor.shape 

In addition, optionally, we can generate the metadata for coloring the elements in each of the tensor dimensions (i.e., for each of the contexts/samples, ligand-receptor pairs, sender cells, and receiver cells) in posterior visualizations. These metadata correspond to dictionaries for each of the dimensions containing the elements and their respective major groups, such as a signaling categories for a ligand-receptor interactions, a hierarchically more granular cell type, or a disease condition for a sample. In cases where we do not account for such information, we do not need to generate such dictionaries. 

For example, we can build a dictionary for the contexts/samples dictionary by using the metadata in the AnnData object. In this example dataset, we can find samples in the column ‘‘sample_new,’’ while their major groups (representing COVID-19 severity) are found in the column ‘‘condition.’’ 

context_dict = adata.obs.sort_values(by=’sample_ new’) \ .set_index(’sample_new’)[’condition’] \ .to_dict() 

tensor = c2c.io.read_data.load_tensor (output_folder + ’/Tensor.pkl’) meta_tensor = c2c.io.load_variable_with_pickle (output_folder + ’/Tensor-Metadata.pkl’) 

Running Tensor-cell2cell across samples (timing: 5 min with a ‘‘regular’’ run or 40 min with a ‘‘robust’’ run, using a GPU in both cases) 

Now that we have built the tensor and its metadata, we can run tensor component analysis via Tensor-cell2cell with one simple command that we implemented for our unified tools. 

c2c.analysis.run_tensor_cell2cell_pipeline (interaction_tensor=tensor, tensor_metadata=meta_tensor, rank=None, tf_optimization=’robust’, random_state=0, device=’cuda’, output_folder=output_folder, ) 

Critical: Key parameters of this command are as follows: 

Then, the metadata can be generated with: 

dimension_dicts = [context_dict, None, None, None] meta_tensor = c2c.tensor.generate_tensor_metadata(interaction_tensor=tensor, metadata_dicts=dimension_dicts, fill_with_order_elements=True) 

Notice that the ‘‘None’’ elements in the variable dimensions_dicts represent the dimensions where we are not including addi- 

- d ‘‘rank’’ is the number of factors or latent patterns we want to obtain from the analysis. You can either indicate a specific number or leave it as ‘‘None’’ to perform the decomposition with a suggested number from an elbow analysis (Figure 5A). 

- d ‘‘tf_optimization’’ indicates whether running the analysis in the regular or the robust way. It essentially controls the convergence parameters of the tensor decomposition. The former employs less strict convergence parameters to obtain optimal results than the latter, which is also translated into a faster generation of results. 

Cell Reports Methods 4, 100758, April 22, 2024 9 


<mark>a</mark> ©@ Ce >ress 

Cell Reports Methods 


|~~Who.~~|~~woo~~|~~Mill~~|~~mule~~|=~~[~~||
|---|---|---|---|---|---|
|<br>~~A~~|<br>~~ee~~|<br>~~|||~~||<br>~~=~~||
|~~ce~~||||~~=~~—|_I~~=~~|
|~~A~~||||||
|~~‘alll ~~|~~c~~|~~M ~~|~~La.~~|||
|~~7~~|~~er~~|~~e)~~|~~eT~~|||
|~~|~~||<br>~~|||||~~|<br>|||
|~~hts ~~|~~ch~~|~~ill ~~|~~ul~~|||
|||~~a~~||||
|~~|~~|~~er~~||~~|~~|||


![Figure 5. Cell-cell communication programs](figures/liana-tensor-cell2cell/page-011-11.png)

### Resource 


Figure 6. Identifying patterns and differences across groups of conditions Context or sample loadings can be used to compare statistically different condition groups within the same cell-cell communication program. Here, COVID-19 patients are grouped by severity, and pairwise t tests are performed. Here, * and ** indicate p values lower than 0.05 and 0.01, respectively, while ns means notsignificant (or p value greater than 0.05). The case of ‘‘ns’’ indicates that the significance is lost after multiple test correction (false discovery rate, in this case). 

_ = c2c.plotting.context_boxplot(context_loadings=tensor.factors[’Contexts’], metadict=context_dict, nrows=3, figsize=(16, 12), group_order=groups_order, statistical_test=’t-test_ind’, pval_correction=’fdr_bh’, cmap=’plasma’, verbose=False, filename=fig_filename ) 

Critical: In this case, we can change the statistical test and the multiple-test correction with the parameters ‘‘statistical_test’’ and ‘‘pval_correction.’’ Here, we used an independent t test and a Benjamini-Hochberg correction. Additionally, we can set ‘‘verbose = True’’ to print exact test statistics and p values. 

We can also generate heatmaps for the elements with loadings above a certain threshold in a given dimension (Figure S1). 

Furthermore, we can cluster these elements by the similarity of their loadings across all factors. 

fig_filename = output_folder + ’/Clustermap-LRs.pdf’ _ = c2c.plotting.loading_clustermap(loadings=tensor.factors[’Ligand-Receptor Pairs’], loading_threshold=0.1, use_zscore=False, figsize=(28, 8), filename=fig_filename, row_cluster=False ) 

Troubleshooting: Note that here, we plot the loadings of the dimension representing the ligand-receptor pairs. In addition, we prioritize the pairs with high loadings using the parameter ‘‘loading_threshold = 0.1.’’ In this case, the elements are included only if they are greater than or equal to that threshold in at least one of the factors. If we use ‘‘loading_threshold = 

Cell Reports Methods 4, 100758, April 22, 2024 11 


![Figure 6. Identifying patterns and differences across groups of conditions](figures/liana-tensor-cell2cell/page-012-12.png)

**ll** OPEN ACCESS 

Resource 


0,’’ then we would consider all of the elements. Considering all of the elements would require modifying the parameter ‘‘figsize’’ to enlarge the figure. 

Caution: Changing the parameter ‘‘use_zscore’’ to ‘‘True’’ would standardize the loadings of one element across all factors. This is useful to compare an element across factors and highlight the factors in which that element is most important. Modifying ‘‘row_cluster’’ to ‘‘True’’ would also cluster the factors depending on the elements that are important in each of them. 

Furthermore, factor-specific networks of cell-cell interactions (Figure S2) can be visualized by using the loadings of sender and receiver cells. 

lr_loadings = tensor.factors[’Ligand-Receptor Pairs’] 

###### Classic pathway enrichment (timing: <1 min) 

For the pathway enrichment analysis, we use ligand-receptor pairs instead of individual genes. KEGG was initially designed to work with sets of genes, so first we need to generate ligandreceptor sets for each of its pathways. A ligand-receptor pair is assigned as part of a pathway set if all of the genes in the pair are part of the gene set of such a pathway. 

Note that we use the ‘‘lr_pairs’’ database that we loaded in the selecting ligand-receptor resources section. 

threshold = 0.075 

c2c.plotting.ccc_networks_plot(tensor.factors, included_factors=[’Factor 3’, ’Factor 5’, ’Factor 10’], ccc_threshold=threshold, # Only important communication nrows=1, 

panel_size=(16, 16), # This changes the size of each figure panel. filename=output_folder + ’Factor-Networks.pdf’, ) 

- Critical: Key parameters of this command are as follows: 

   - d ‘‘included_factors’’ is a list of factors to plot. If ‘‘None’’ is passed, then all factor-specific networks are shown. 

   - d ‘‘ccc_threshold’’ is a loading value to set as threshold to select key cell-cell interactions. This threshold filters the outer products between sender and receiver cells, and it can be either arbitrary or determined as shown in the online tutorials. 

###### Step 6: Pathway enrichment analysis: Interpreting the context-driven communication 

The decomposition of ligand-receptor interactions across samples into loadings associated with the conditions reduces the dimensionality of the inferred interactions substantially. Nevertheless, we are still working with 1,054 interactions across multiple factors associated with the disease labels. To this end, as is commonly done when working with omics data types, we can perform pathway enrichment analysis to identify the general biological processes of interest. By using the loadings for each ligand-receptor pair (Figure 5B), we can rank them within each factor and use this ranking as input to enrichment analysis. Pathway enrichment thus serves two purposes: it further reduces the dimensionality of the inferred interactions and it enhances the biological interpretability of the inferred interactions. 

Here, we show the application of classical gene set enrichment analysis (GSEA) on the ligand-receptor loadings. We use GSEA<sup>41</sup> with KEGG Pathways,<sup>42</sup> as well as a multivariate linear regression from decoupler-py<sup>43</sup> with the PROGENy pathway resource.<sup>44</sup> 

First, we assign ligand-receptor loadings to a variable. 

# Generate list with ligand-receptors pairs in DB lr_list = [’^’.join(row) for idx, row in lr_pairs. iterrows()] # Specify the organism and pathway database to use for building the LR set organism = "human" pathwaydb = "KEGG" # Generate ligand-receptor gene sets lr_set = c2c.external.generate_lr_geneset(lr_list, complex_sep=’_’, lr_sep=’^’, organism=organism, pathwaydb=pathwaydb, readable_name=True, output_folder=output_folder ) 

Critical: Key parameters of this command are as follows: 

- d ‘‘complex_sep’’ indicates the symbol separating the gene names in the protein complex. 

- d ‘‘lr_sep’’ is the symbol separating a ligand and a receptor complex. 

- d ‘‘organism’’ is the organism matching the gene names in the single-cell dataset. It could be either ‘‘human’’ or ‘‘mouse.’’ 

- d ‘‘pathwaydb’’ is the name of the database to be loaded, provided with the cell2cell package. Options are ‘‘GOBP,’’ ‘‘KEGG,’’ and ‘‘Reactome.’’ 

Run GSEA via cell2cell, which calls the ‘‘gseapy.prerank’’ function internally. 

pvals, scores, gsea_df = c2c.external.run_gsea (loadings=lr_loadings, lr_set=lr_set, output_folder=output_folder, weight=1, min_size=15, permutations=999, processes=6, random_state=6, significance_threshold=0.05, ) 

12 Cell Reports Methods 4, 100758, April 22, 2024 


**ll** OPEN ACCESS 

Resource 


title_size=20, tick_size=12, filename=fig_filename ) 


###### Footprint enrichment analysis (timing: <1 min) 

In footprint enrichment analysis, instead of considering the genes whose products (proteins) are directly involved in a process of interest, we consider the genes affected by it—i.e., those that change downstream as a consequence of the process.<sup>45</sup> In this case, we will use the PROGENy resource to infer the pathways driving the identified context-dependent patterns of ligand-receptor pairs. PROGENy was built in a data-driven manner using perturbation data.<sup>44</sup> Consequently, it assigns different weights to each gene in its pathway gene sets according to its importance. Thus, we need an enrichment method that can account for weights. To do so, we will use a multivariate linear regression implemented in decoupler-py.<sup>43</sup> 

Figure 7. Assigning functions to factors from GSEA By using the loadings of ligand-receptor pairs per factor, they can be ranked within a factor (factor-specific analysis), and this information can be used to run an enrichment analysis such as GSEA to associate each of the programs with different functions or pathways. This dot plot shows the enriched KEGG pathways per factor. Dot size indicates the –log(p value), while the color indicates the normalized enrichment score (NES) from the GSEA. 

Critical: Key parameters of this command are as follows: 

As we did in GSEA using Tensor-cell2cell, we first have to generate ligand-receptor gene sets while also assigning a weight to each ligand-receptor interaction. This is done by taking the mean between the ligand and receptor weights. For ligand and receptor complexes, we first take the mean weight for all subunits. We keep ligand-receptor weights only if all the proteins in the interaction are sign coherent and present for a given pathway. Load the PROGENy gene sets and then convert them to sets of weighted ligand-receptor pairs. 

- d ‘‘lr_set’’ is a dictionary associating pathways (keys) with sets of ligand-receptor pairs (values). 

- d ‘‘weight’’ represents the original parameter p in GSEA. It is an exponent that controls the importance of the ranking values (loadings, in our case). 

- d ‘‘min_size’’ indicates the minimum number of LR pairs that a set has to contain to be considered in the analysis. 

- d ‘‘permutations’’ indicates the number of permutations to perform to generate the null distribution. 

- d ‘‘random_state’’ is the reproducibility seed. 

- d ‘‘significance_threshold’’ is the p value threshold to consider significance. 

Now that we have obtained the normalized enrichment scores (NESs) and corresponding p values from GSEA, we can plot those using the following function from cell2cell (Figure 7). 

pathway_label = ’{} Annotations’.format(pathwaydb) fig_filename = output_folder + ’/GSEA-Dotplot.pdf’ with sns.axes_style("darkgrid"): 

dotplot = c2c.plotting.pval_plot.generate_dot_plot (pval_df=pvals, score_df=scores, significance=0.05, xlabel=’’, ylabel=pathway_label, cbar_title=’NES’, cmap=’PuOr’, figsize=(5, 12), label_size=20, 

# We first load the PROGENy gene sets 

net = dc.get_progeny(organism=’human’, top=5000) 

# Then convert them to sets with weighted ligand-receptor pairs 

lr_progeny = li.rs.generate_lr_geneset(lr_pairs, net, lr_sep="^") 

Run footprint enrichment analysis using the ‘‘mlm’’ method from decoupler-py: 

###### ="^") 

estimate, pvals = dc.run_mlm(lr_loadings.transpose(), lr_progeny, 

source="source", target="interaction", use_raw=False 

Here, ‘‘estimate’’ and ‘‘pvals’’ correspond to the t values and p values assigned to each pathway. 

Finally, we generate a heatmap for the 14 pathways in PROGENy across all factors (Figure S3A). 

fig_filename = output_folder + ’/PROGENy.pdf’ _ = sns.clustermap(estimate, xticklabels=estimate.columns, 

Cell Reports Methods 4, 100758, April 22, 2024 13 


![Figure 7. Assigning functions to factors from GSEA](figures/liana-tensor-cell2cell/page-014-14.png)

**ll** OPEN ACCESS 

Resource 


cmap=’coolwarm’, z_score=4) plt.savefig(fig_filename, dpi=300, bbox_inches=’tight’) 

From the heatmap, we can also generate a bar plot for the PROGENy pathways for a specific factor (Figure S3B). 

selected_factor = ’Factor 5’ fig_filename = output_folder + ’/PROGENy-{}.pdf’.format(selected_factor.replace(’ ’, ’-’)) dc.plot_barplot(estimate, selected_factor, vertical=True, cmap=’coolwarm’, save=fig_filename) 

###### DISCUSSION 

In this protocol, we illustrate how LIANA and Tensor-cell2cell can be used together to provide robust and flexible solutions to infer CCC programs across contexts. In addition to established methods for studying ligand-receptor interactions<sup>19,32</sup> that LIANA also includes, approaches geared toward the systematic inference of CCC programs across diverse conditions are less common. A few of them, such as CellChat,<sup>19</sup> summarize pathway-focused similarities across conditions based on pairwise comparisons, while MultiNicheNet<sup>20</sup> depends on differential expression analysis and requires a hypothesis to be defined a priori. MultiNicheNet was recently proposed to systematically identify deregulated CCC interactions along with associated intracellular signaling. MultiNicheNet uses a flexible statistical framework and is capable of handling complex experimental designs. However, MultiNicheNet depends on differential expression analysis and hence requires a predefined hypothesis. As such, we see MultiNicheNet and Tensor-cell2cell as complementary, since the latter can identify patterns across all cell types and conditions in an untargeted manner. An analogous strategy to Tensor-cell2cell can be adopted by using factor analysis<sup>11</sup> in LIANA to identify patterns directly from the CCC scores.<sup>46</sup> Hence, Tensor-cell2cell and LIANA can help researchers to generate a specific hypothesis and identify cell types to later use MultiNicheNet as a downstream analysis to additionally infer intracellular signaling triggered by key ligands. 

Since our pipeline is intended as a generalizable approach for use with many different resources and methods, we additionally assessed the robustness of our results across different inputs. Specifically, we showed how communication scores may be different for individual samples across methods (see Tutorial 02 inthe onlinetutorials), whereas those differences may bemitigated by using the consensus score or when running Tensor-cell2cell across multiple samples (see Python Supplementary Tutorials S3A-2 and S3B in the online tutorials). Moreover, we provide an in-depth assessment of Tensor-cell2cell’s sensitivity to missing values and batch effects (STAR Methods). Additional benchmarks can befoundintheoriginalTensor-cell2cell<sup>12</sup> and recentLIANA+<sup>46</sup> articles, where we have shown that Tensor-cell2cell consistently 

captures CCC events deregulated across diverse contexts and conditions. Finally, we demonstrate the broad applicability of our protocol by also providing an example of defining contexts to analyze CCC using spatial transcriptomics (see STAR Methods and Python Supplementary Tutorial S4 in the online tutorials). Although the example using spatial transcriptomics presented in our extended tutorials is a simplified application of the concept, it could be extended to compare multiple samples if users are able to align tissues from different donors. Similarly, our protocol can also aid users in applications beyond single-cell transcriptomics data, including extracting metabolite-mediated CCC programs<sup>27</sup> or similar extensions to multiomics data.<sup>46</sup> 

###### Limitations of the study 

Similar to any other approach to infer CCC from transcriptomics data, our protocol also inherits assumptions leading to certain limitations. These include the assumption that gene co-expression is indicative of active signaling events, which are largely mediated by proteins and their interactions, while also disregarding multiple biological processes, such as protein translation, post-translationalmodifications, secretion, diffusion,and trigger ofintracellular events, that precede and follow the interaction itself.<sup>2,5</sup> Moreover, the aggregation of single cells into cell groups is essential when inferring potential CCC events, which could occlude some signals in heterogeneous tissues,<sup>2,3</sup> thereby biasing the insights that can be obtained. Furthermore, the input of Tensor-cell2cell is a 4D tensor, so it requires that all elements be measured across all features and samples (i.e., cell types and genes expressing ligands and receptors). Consequently, one should consider how to handle missing values across samples that do not capture the same cell typesand/orexpressedgenes.Decidingwhetherthosereflectbiologically meaningful zeros or a technical artifact may lead to variations in the resulting CCC programs. We provide an extended explanation of the related parameter choices that may help users decide how to handle this challenge (STAR Methods). 

###### STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

- d RESOURCE AVAILABILITY 

   - B Lead contact 

   - B Materials availability 

   - B Data and code availability 

- d METHOD DETAILS 

   - B Computational Infrastructure 

   - B Timing 

   - B Protocol details 

   - B Benchmarking batch effects and missing values 

- d QUANTIFICATION AND STATISTICAL ANALYSIS B Notations for the scoring functions in LIANA 

###### SUPPLEMENTAL INFORMATION 

Supplemental information can be found online at https://doi.org/10.1016/j. crmeth.2024.100758. 

14 Cell Reports Methods 4, 100758, April 22, 2024 


**ll** OPEN ACCESS 

### Resource 

###### ACKNOWLEDGMENTS 

D.D. was supported by the European Union’s Horizon 2020 research and innovation programme (860329 Marie-Curie ITN ‘‘STRATEGY-CKD’’). E.A. was supported by the Chilean Agencia Nacional de Investigacio´ n y Desarrollo (ANID) through its scholarship program DOCTORADO BECAS CHILE/2018 - 72190270, the Fulbright Chile Commission, and the Siebel Scholars Foundation. This work was further supported by the NVIDIA Corporation through its Academic Hardware Grant Program. N.E.L. was supported in part by NIGMS R35 GM119850. H.M.B. was also supported by an ORISE fellowship. 

###### AUTHOR CONTRIBUTIONS 

H.M.B., D.D., and E.A. conceived the project, adapted the computational tools, developed the protocol, and wrote the initial version of the manuscript. J.S.-R. and N.E.L. revised the manuscript and supervised the project. H.M.B., D.D., and E.A. contributed equally. J.S.-R. and N.E.L. are both corresponding authors and have contributed equally. 

###### DECLARATION OF INTERESTS 

J.S.-R. reports funding from GSK, Pfizer, and Sanofi and fees/honoraria from Travere Therapeutics, Stadapharm, Astex, Pfizer, and Grunenthal. N.E.L. reports funding during the course of this work from Sanofi, Amgen, Sartorius, and Ionis and is a co-founder of NeuImmune, Inc., and Augment Biologics. 

Received: August 10, 2023 Revised: December 22, 2023 Accepted: March 22, 2024 Published: April 16, 2024 

### Resource 


##### STAR+METHODS 

###### KEY RESOURCES TABLE 

|REAGENT or RESOURCE|SOURCE|IDENTIFIER|
|---|---|---|
|Deposited data|||
|COVID BALF single-cell RNA-seq dataset|Liao et al.<sup>30</sup>|GEO: GSE145926; Zenodo Data:https://doi.org/10.5281/<br>zenodo.7706962|
|PBMC single-cell RNA-seq dataset|Kang et al.<sup>47</sup>|GEO: GSE96583; Zenodo Data:https://doi.org/10.5281/<br>zenodo.10069528|
|Myocardial Infarction spatial<br>transcriptomics dataset|Kuppe et al., 2022<sup>22</sup>|Zenodo Data:https://doi.org/10.5281/zenodo.6578047|
|Software and algorithms|||
|Protocol source code|This paper|https://doi.org/10.5281/zenodo.10700956|
|Code for benchmarking batch effects<br>and missing values|This paper|https://doi.org/10.5281/zenodo.10713331|


###### RESOURCE AVAILABILITY 

###### Lead contact 

Further information and requests for resources should be directed to and will be fulfilled by the lead contact, Nathan E. Lewis (nlewisres@ucsd.edu). 

###### Materials availability 

This study did not generate new unique reagents. 

###### Data and code availability 

- d This paper analyzes existing, publicly available data. These accession numbers for the datasets are listed in the key resources table. In particular, the BALF single-cell RNA-seq dataset is available at https://zenodo.org/record/7706962, the PBMC singlecell RNA-seq dataset is available at https://zenodo.org/records/10069528, and the Myocardial Infarction spatial transcriptomics dataset is available at https://zenodo.org/record/6578047. 

- d All original code has been deposited at Zenodo and is publicly available as of the date of publication. DOIs are listed in the key resources table. Additionally, source code is available at https://github.com/saezlab/ccc_protocols and can be viewed at https://ccc-protocols.readthedocs.io/. 

- d Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request. 

###### METHOD DETAILS 

###### Computational Infrastructure 

All code was ran on a computer with the following specifications. 

- d CPU: AMD Ryzen Threadripper 3960x (24 cores) 

- d Memory: 128GB DDR4 

- d GPU: NVIDIA RTX A6000 48GB 

However, the minimal requirements for running this protocol are. 

- d CPU: 64-bit Intel or AMD processor (4 cores) 

- d Memory: 16GB DDR3 

- d GPU: NVIDIA GTX 1050 Ti (Optional) 

- d Storage: At least 10GB available 

###### Timing 

- Expected timing for this protocol using the dataset in the key resources table: Step 1. Installation of Anaconda/Miniconda and Python packages: 5–30 min. Step 2. Initial setups: �1 min. 

- Step 3. Data preprocessing: 5–7 min. 

Cell Reports Methods 4, 100758, April 22, 2024 e1 


**ll** OPEN ACCESS 

Resource 


Step 4. Inferring cell-cell communication with LIANA: �5 min. Step 5. Comparing cell-cell communication across multiple samples with Tensor-cell2cell: Running selection of number of factors via elbow analysis and the tensor decomposition takes 5 min with the ‘regular’ pipeline, while the ‘robust’ pipeline takes 40 min. Step 6. Functional Enrichment Analysis of KEGG and PROGENy pathways respectively using GSEA and linear regression take 1 min each. 

###### Protocol details 

To run our protocol presented in this manuscript and the tutorials available online (https://ccc-protocols.readthedocs.io/), software specifications are summarized in the Software Requirements Table. To facilitate the setup of a virtual environment containing all required packages with their corresponding versions, we provide an executable ‘setup_env.sh‘ script together with instructions on a Github repository we prepared for this protocol: https://github.com/saezlab/ccc_protocols/tree/main/env_setup. Software Requirements Table 

|Package Name|Package Version|Language|Install With|
|---|---|---|---|
|jupyter|||conda|
|ipywidgets|||conda|
|pip|R22|Python|conda|
|scanpy|R1.9|Python|conda|
|*cuda-toolkit|||conda|
|*pytorch-cuda|11.8||conda|
|*torchvision|||conda|
|*torchaudio|||conda|
|pytorch, *cuda enabled|||conda|
|scvi-tools|R0.18|Python|conda|
|scikit-misc|0.1.4|Python|conda|
|cell2cell|0.7.3|Python|pip|
|liana|1.0.3|Python|pip|
|decoupler|1.5.0|Python|pip|
|omnipath|1.0.7|Python|pip|
|plotnine|R0.12.4|Python|pip|
|seaborn|0.11.2|Python|pip|
|statannotations|0.5.0|Python|pip|
|matplotlib|3.7.3|Python|pip|
|singlecellexperiment||R|conda|
|remotes|R2|R|conda|
|devtools|R2|R|conda|
|seuratobject||R|conda|
|biocmanager|R1.30|R|conda|
|seurat|R4|R|conda|
|hd5r||R|conda|
|furrr||R|conda|
|textshape||R|conda|
|forcats||R|conda|
|rstatix||R|conda|
|ggpubr||R|conda|
|scater||R|conda|
|zellkonverter||R|conda|
|liana|0.1.13|R|remotes|
|seurat-disk|0.0.0.9020|R|remotes|
|decoupleR|2.3.3|R|biocmanager|


*: For GPU enabled use only. 

Python packages should always be installed. R language packages only need to be installed if planning to run the notebooks in R. 

e2 Cell Reports Methods 4, 100758, April 22, 2024 


**ll** OPEN ACCESS 

### Resource 


Advice to deal with potential issues running this protocol, either in its original or personalized forms, is summarized in the Troubleshooting Table. 

Troubleshooting Table. 

|Step|Problem|Possible reason|Solution|
|---|---|---|---|
|3 & 4|Error: Expression matrix contains<br>non-fnite values (nan or inf)<br>Warning: Make sure that normalized<br>counts are passed|Mishandling counts processing|Ensure that the matrix containing normalized<br>counts is passed. Replace nan and inf values<br>by zeros.|
|4.1|Negative values in LIANA outputs|Using preprocessed data with negative<br>expression values.|Avoid using preprocessing methods that<br>generate negative values (e.g., centering the<br>data to the mean values, using batch-<br>corrected expression values, etc.).|
|4.2|Not enough ligand-receptor pairs<br>in the data for the analysis|Mismatched symbol IDs|LIANA by default uses a resource with gene<br>symbol IDs. When working with e.g., Ensembl<br>IDs users need to provide an external resource;<br>seehttps://ccc-protocols.readthedocs.io/en/<br>latest/notebooks/ccc_python/02-Infer-<br>Communication-Scores.html|
|5.1|CCC scores representing opposed<br>importance|When using ‘magnitude_rank’ scores<br>from LIANA, lower values are more<br>important. However, Tensor-cell2cell<br>prioritizes high values as the important<br>ones.|Build the 4D tensor using an ‘inverse_fun‘ to<br>make lower values to be the most important<br>scores.|
|5.2|Rank selection through the elbow<br>analysis is not behaving properly|High sparsity or number of missing<br>values in the tensor|Re-run LIANA with less stringent parameters<br>(e.g., smaller expr_pror). Re-build the tensor<br>with more strict how parameters (e.g., using<br>how = ‘inner’ or increasing outer_fraction).|
|5.3|Visualization of loadings are not<br>properly displayed in heatmaps|Too many or few elements in the<br>dimension to visualize|To visualize all elements, use the parameter<br>‘loading_threshold = 0<sup>0 </sup>to create the heatmaps.<br>If you have too many elements, you can<br>prioritize those with high loadings, so a<br>threshold can be set. E.g., ‘loading_<br>threshold = 0.1<sup>0</sup>|


###### Benchmarking batch effects and missing values 

To help users make informed decisions regarding choices in their computational pipeline, we benchmarked two key factors that can influence Tensor-cell2cell<sup>0</sup> s outputs: batch effects and missing data (which result in missing tensor indices) across samples. For comprehensive details on the motivation, methods, and results of this benchmarking, please see the online description.<sup>48</sup> 

Here we describe our pipeline for both the Missing Indices and Batch Effects benchmarking simulations. All associated code can be found in the following repository: https://github.com/hmbaghdassarian/tc2c_benchmark. For downstream analyses, unless otherwise specified, all linear regressions were performed using a generalized linear model (GLM) with an identity link function; multivariate regressions with >1 independent variable were combined additively and do not include interaction terms. Additionally, all p-values were multiple-test-corrected using the Benjamini-Hochberg (BH) method to control for false discovery rates (FDRs). 

We simulated single-cell RNA-sequencing expression data using Splatter,<sup>49</sup> adapting a previously described computational approach.<sup>50</sup> We generated a single-cell expression matrix containing 2000 genes and 5000 cells evenly distributed across 6 cell types and 5 samples. Each sample represents a context. 

Next, for each sample, we applied quality control filters to the cells and genes as implemented previously.<sup>50</sup> Briefly, low-quality cells were identified and filtered using the scuttle package based on standard metrics (mitochondrial fraction, library size, and number of genes detected); genes detected in fewer than 1% of cells are discarded. Next, counts were normalized using scran pooling<sup>51</sup> and a log+1 transformation. For batch-effect benchmarking, batch correction was further implemented; Scanorama<sup>52</sup> was run on the log-normalized counts matrix and scVI<sup>53</sup> was run on the raw counts matrix. 

From the expression counts matrices, a random subset of 200 genes were chosen to simulate a ligand-receptor interaction network as previously described.<sup>12</sup> Briefly, we use StabEco’s<sup>54</sup> BiGraph function, with the power law exponent value set to 2 and the average degree value set to 3, to generate a scale-free, directed, bipartite network of the 200 genes. Half the genes were assigned to be ligands and the other half to be receptors. Not all genes were part of the connected network (70/200), and these were excluded 

Cell Reports Methods 4, 100758, April 22, 2024 e3 


**ll** OPEN ACCESS 

Resource 


from downstream analyses. This interaction network was used as custom ligand-receptor resource input to LIANA’s cell-cell communication scoring. 

Then, 4D-Communication tensors were built from the output of LIANA as described in our protocol. To generate missing indices in the 4D-Communication Tensor, we iteratively omitted a random subset of genes or cell types from the expression data. Specifically, we iterated through combinations of the following two variables: the fraction of cell types to remove in a given sample (16, 13, 12, and 23), the fraction of genes (within the 130 in the simulated LR interaction network) to remove in a given sample (110, 310, 12), and the fraction of samples to apply these omissions to (15, 25, 23). We compared this to a gold-standard tensor with no missing indices. 

We compared decomposition outputs using CorrIndex<sup>55</sup> as previously described.<sup>12</sup> Briefly, the CorrIndex represents a dissimilarity between decomposition outputs and lies between 0 and 1; we convert this to a similarity metric by using (1-CorrIndex). 

For batch-correction, iterating across increasing levels of batch severity, we generated four counts matrices. 

- (1) Gold-standard: a processed counts matrix with no batch effects 

- (2) Log-normalized: a processed counts matrix with batch effects present 

- (3) Scanorama batch-corrected: a processed counts matrix with batch effects corrected for using Scanorama 

- (4) scVI batch-corrected: a processed counts matrix with batch effects corrected for using scVI 

We ran the combined LIANA and Tensor-cell2cell pipeline on each of these counts matrices. Finally, we assessed the similarity between each of the decomposition outputs as follows. 

- d Log-normalized similarity: Similarity between Tensor-cell2cell<sup>0</sup> s decomposition output from the log-normalized counts matrix (2) and that of the gold-standard input (1) 

- d Scanorama similarity: Similarity between Tensor-cell2cell<sup>0</sup> s decomposition output from the Scanorama batch-corrected counts matrix (3) and that of the gold-standard input (1) 

- d scVI similarity: Similarity between Tensor-cell2cell<sup>0</sup> s decomposition output from the scVI batch-corrected counts matrix (4) and that of the gold-standard as input (1) 

Additionally, for batch correction benchmarking, each counts matrix was quantified for its level of batch severity using two previously applied metrics<sup>50,56</sup> : (1) kBET,<sup>57</sup> is an inverse measure of ‘‘mixability’’, or the extent to which batch effects are removed, and (2) normalized mutual information (NMI) between cell type identity and cluster identity - a measure of ‘‘clusterability’’, or the extent to which biological variation is conserved. For the clusterability metric, we subtracted the NMI from 1 to quantity batch severity. In this manner, both mixability and clusterability ranged between 0 and 1, with increasing values indicating increasing batch severity. Clusterability was assessed using both k-means clustering<sup>58</sup> and Louvain clustering.<sup>59</sup> 

Batch severity does not affect the results of our pipeline. We saw that the gold-standard matrix performed as expected, showing clear Louvain clusterability and little-to-no mixability. The log-normalized matrix also performed as expected across all batch severity metrics. While the batch-corrected counts matrices increased along with the Splatter parameters on occasion, the increases were overall less severe than that of the log-normalized matrix (Figure S4). The gold-standard counts matrices demonstrate comparably low batch severity across all iterations (Figure S5A). We also saw that across all batch severity metrics, similarity does not decrease beyond 0.963, indicating that Tensor-cell2cell is robust to batch effects (Figure S5B). Furthermore, we evaluated whether the fraction of negative counts is a confounder of batch severity (Figures S5C–S5E). The fraction of negative counts does not substantially affect the Scanorama similarity as indicated by the small regression coefficient estimate and insignificant p-value (Figure S5F). This tells us that using batch correction methods that introduce negative values and simply replacing those with 0 prior to running communication scoring can be appropriate for recovering biological signals from Tensor-cell2cell. 

If batch correction improves decomposition, we would expect batch-corrected similarity (Scanorama and scVI) to a) score higher than log-normalized similarity across batch similarity metrics and b) decrease at a lower rate with increasing batch severity than lognormalized similarity. Across batch severity metrics, we see that this tends not to be the case, though all similarity types maintain a high similarity score across batch severity levels (Figure S6) Overall, while batch effect correction may not be necessary to recover biological signals using Tensor-cell2cell, if the user feels it is important, they can be comfortable in implementing the batch correction method of choice. 

Regarding missing values, we found that there was a significant decrease in the similarity of Tensor-cell2cell<sup>0</sup> s output with that of the gold-standard as the fraction of missing indices increased when filling both with NaN (masked) or zero (not masked). However, those that were not masked had a substantially larger decrease in similarity than those that were (Figure S7A). When considering the two filling methods in combination with the missing fraction, we see that similarity is lower by 0.094 on average when filling with zero (Figure S7B). Altogether, our pipeline is robust enough to impute missing values and sensitive enough to handle true biological zeros. 

###### QUANTIFICATION AND STATISTICAL ANALYSIS 

Notations for the scoring functions in LIANA 

k is the k-th ligand-receptor interaction 

L - expression of ligand L 

e4 Cell Reports Methods 4, 100758, April 22, 2024 


**ll** OPEN ACCESS 

Resource 


R - expression of receptor R 

C - cell cluster 

i - cell group i 

j - cell group j 

M - the library-size normalized and log1p-transformed gene expression matrix 

X - normalized gene expression vector 

We denote the two interaction proteins, via their genes L & R, yet we use this for convenience as these can also denote the interaction of any other event category, such as those between membrane-bound or extracellular matrix proteins. Furthermore, in the case of heteromeric complexes L & R denote the summarized expression of the complex. CellPhoneDBv2<sup>32</sup> function. 

Magnitude: 1) LRmeank;i;j = LCi +2RCj Specificity: A permutation approach also adapted by other methods, see 4) Geometric Mean function. 

f Magnitude: 2) LRgeometric:meank;i;j = pLCi $RCj Specificity:: An adaptation of CellPhoneDB’s permutation approach; see 4) CellChat’s<sup>19</sup> LR probabilities* function. Magnitude: 3) LRprobk;i;j = KhTriMean+TriMeanðLðciLÞci$ ÞTriMean$TriMeanðRðcRj Þcj Þ 

Specificity:: An adaptation of CellPhoneDB’s permutation approach; see 4) CellChat’s<sup>19</sup> LR probabilities* function. 

where Kh = 0.5 by default and ‘TriMean‘ represents Tuckey’s Trimean function: 

TriMean ðXÞ = Q0:25ðXÞ+2$Q0:5ðXÞ+Q0:75ðXÞ 4 

Specificity: An adaptation of CellPhoneDB’s permutation approach; see 4) 

*Note: The original CellChat implementation uses information of mediator proteins (e.g. activators and inhibitors) and signaling pathways, which is specific to the CellChat resource. Since LIANA allows combining any resource with different scoring methods, LIANA does not utilize this information, and hence the implementation of CellChat’s scoring function in LIANA was simplified to be resource-agnostic. 


where P is the number of permutations, and L� and R� are ligand and receptor expressions summarized according to the aggregation function per cluster used by each method, i.e., by default the arithmetic mean for CellPhoneDB and Geometric Mean, and TriMean for CellChat. 

SingleCellSignalR<sup>35</sup> function. 

Magnitude: 5) LRscorek;i;j = ~~p~~ <u>pL</u> ~~f f~~ CifL ~~f~~ Ci R ~~f~~ R ~~f~~ CjC+j m 

where m is the mean of the expression matrix M NATMI<sup>34</sup> function. 

Magnitude: 6) LRproductk;i;j = LCi RCj 

Specificity: 7) Specificity Weightk;i;j = ~~P~~ LnCLi Ci $ ~~P~~ RnCRi Cj 

Connectome<sup>33</sup> function. 

Magnitude: 6) LRproductk;i;j = LCi RCj 

Specificity: 8) LRz:meank;i;j = zLCi +2zRCj 

where z is the Z score of the expression matrix M Log2FC function. 

Specificity: 9) LRlog2FCK;I;J = Log 2FCCi;L +2Log 2FCCj;R 

where log2FC for each gene is calculated as: 

log 2 FC = log2ðmean ðXiÞÞ � log2�mean�Xnoti �� 

Equation 10 

Rank Aggregate function. 

Cell Reports Methods 4, 100758, April 22, 2024 e5 


**ll** OPEN ACCESS 

Resource 


When generating a consensus from the different methods in LIANA, a rank aggregate<sup>36</sup> is calculated for the magnitude and specificity scores from the methods separately. First, a normalized rank matrix[0,1] is generated separately for magnitude and specificity as: 


where m is the number of ranked score vectors, n is the length of each score vector (number of interactions), ranki;j is the rank of the j-th element (interaction) in the i-th score rank vector, and maxðrankiÞ is the maximum rank in the i-th rank vector. 

For each normalized rank vector r, we then ask how probable it is to obtain rð<sup>null</sup> kÞ<sup><=rðkÞ, where r</sup> ð<sup>null</sup> kÞ<sup>is a rank vector generated under</sup> the null hypothesis. The RobustRankAggregate (https://github.com/cran/RobustRankAggreg) method expresses the probability rð<sup>null</sup> kÞ<sup><=rðkÞas bk;nðrÞ through a beta distribution. This entails that we obtain probabilities for each score vector ras:</sup> 


where we take the minimum probability r for each interaction across the score vectors, and we apply a Bonferroni correction to the p-values by multiplying them by n to account for multiple testing. 

For all the methods above, LIANA considers interactions as occurring only if the ligand and receptor, and all of their subunits, are expressed in a certain proportion of the cells (0.1 by default) in both clusters involved in the interaction. This can be formulated as an indicator function as follows: 

InL<sup>expr</sup> Cj<sup>:prop</sup> R 0:1 and R<sup>expr</sup> Cj<sup>:prop</sup> R 0:1o 

e6 Cell Reports Methods 4, 100758, April 22, 2024 
