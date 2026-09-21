---
source_url: https://www.helmholtz-munich.de/en/aih/news-detailseite/weeks-of-work-in-a-few-hours-ai-tool-reads-cell-membranes
fetched: 2026-09-21
conversion: curl+pandoc
---


<img src="https://images.admiralcloud.com/v5/deliverEmbed/706a5444-322a-476a-b663-7e73405025aa/image/autocrop/1672/941/1?poc=true" title="KI-gestützte Analyse von Zellmembranen" itemprop="image" loading="lazy" width="1672" height="941" alt="KI-gestützte Analyse von Zellmembranen" />

© <span class="copyright-toggle__title" hidden="">KI-generierte Illustration mit ChatGPT (OpenAI)</span>

# Weeks of Work in a Few Hours: AI Tool Reads Cell Membranes

<span class="c-news-detail__categories"> AI Computational Health AIH IML </span> September 8, 2026

Cell membranes and the proteins within them control many vital processes and play a key role in health and disease. But studying them in 3D images of cells has so far meant slow, manual work. A team from Helmholtz Munich, the Technical University of Munich (TUM) and the Biozentrum of the University of Basel has developed MemBrain v2, an AI tool that automates this task – cutting work that once took weeks down to a few hours. The freely available software finds membranes, locates specific membrane proteins and analyzes how these are spatially arranged, showing how cellular processes are organized at the molecular level. Depending on the application, the AI requires little or no additional training data to do this. That lets researchers around the world study how cells work in detail – faster and on a much larger scale. The tool is presented in the journal Nature Methods.

Cryo-electron tomography (cryo-ET) is a special microscopy technique that lets researchers look inside cells – in three dimensions and at very high resolution. Because the cells are flash-frozen for this, they are preserved almost unchanged, from whole cell structures down to individual molecules. Membranes, however, have so far been difficult to analyze in this kind of data.

> "One challenge is that cryo-ET images can contain gaps in information due to technical limitations of the imaging process. As a result, certain membrane orientations are difficult or partly impossible to see. This is exactly where MemBrain v2 comes in, automating the process," explains first author Lorenz Lamm.

## Optimizing a Key Technology in Cell Biology

MemBrain-seg detects membranes directly, without requiring users to provide additional annotations or training data. MemBrain-pick also requires only a small amount of training data: In one test, researchers manually annotated the positions of protein complexes on just a single membrane. Based on these annotations, the tool localized the corresponding protein complexes on additional membranes with an F1 score of 91 percent. Until now, this 3D image data had to be labeled painstakingly by hand, and the results could rarely be reused for new datasets. Existing programs usually handled only single parts of the analysis – for example outlining the membranes or locating the proteins within them.

## Three Tools in One Software – and Little Data Suffices

For the first time, MemBrain v2 combines three steps in a single AI tool: it finds membranes (MemBrain-seg), locates the proteins embedded in them (MemBrain-pick) and measures how these proteins are arranged (MemBrain-stats).   
In several applications, the tool matched the results of painstaking manual analyses, but was considerably faster. It is also easy to use and can be applied to other research questions without major adjustments. Because all components are open source, the membrane-detection module is already widely used around the world and has, for example, been applied across datasets from the Chan Zuckerberg Imaging Institute.

> “By making these analyses faster and accessible to research groups worldwide, we can study cellular processes across much larger datasets. This can ultimately help us better understand how cells function – and what changes when disease develops,” says senior author Dr. Tingying Peng.

## Larger Datasets and Finer Distinctions Ahead

MemBrain v2 has already contributed to new biological insights: In a separate study, the tool showed that important photosynthesis proteins are spatially separated within the membrane – challenging previous models of their organization. In the future, it is set to distinguish different protein types even more precisely. 

> “I’m especially pleased that MemBrain v2 is now being used in many further studies, where it simplifies demanding analyses or makes them possible in the first place – making a concrete contribution to new biological insights,” says first author Lorenz Lamm.

 

### Original Publication

Lamm et al., 2026: MemBrain v2: an end-to-end tool for the analysis of membranes in cryo-electron tomography. Nature Methods. <a href="https://www.nature.com/articles/s41592-026-03178-8" target="_blank" rel="noreferrer">DOI: 10.1038/s41592-026-03178-8</a>

Software: <a href="https://github.com/CellArchLab/MemBrain-v2" target="_blank" rel="noreferrer">https://github.com/CellArchLab/MemBrain-v2</a> 

<img src="https://images.admiralcloud.com/v5/deliverEmbed/a287aa69-8a8d-47da-ac62-0884659cae44/image_webp/cropperjsfocus/256/256/0,0,640,640,0,1,1/320,320?poc=true" title="Prof. Dr. Julia Anne Schnabel" loading="lazy" width="256" height="256" alt="Porträt von Julia Schnabel (#87)" />

<span class="h4">Prof. Dr. Julia Anne Schnabel</span>

Director, Institute of Machine Learning in Biomedical Imaging

<a href="/en/iml/julia-schnabel" class="btn--arrow-next">View profile</a>

<img src="/typo3temp/assets/_processed_/3/a/csm_person_dummy_8fb29c1925.webp" loading="lazy" width="256" height="256" />

<span class="h4">Tingying Peng</span>

Group leader

<a href="/en/aih/tingying-peng" class="btn--arrow-next">View profile</a>

## Related news

<img src="https://images.admiralcloud.com/v5/deliverEmbed/5850b025-437f-4be8-b34a-95e63117c46b/image_webp/cropperjsfocus/3840/2562/0,0,3840,2562,0,1,1/1920,1281?poc=true" title="Newborn care" itemprop="image" loading="lazy" width="3840" height="2562" alt="Newborn care" />

Transfer, Computational Health, ICB, IML, June 16, 2026

### Helmholtz Munich and Partners Develop AI-Powered Sensor Patch for Neonatal Care

Researchers at Helmholtz Munich, together with international partners, have developed an ultrathin sensor patch capable of non-invasively monitoring key health parameters in preterm infants. The silk-based patch measures temperature, pH, sodium, and…

<a href="/en/newsroom/news-all/artikel/helmholtz-munich-and-partners-develop-ai-powered-sensor-patch-for-neonatal-care" class="btn--arrow-next" itemprop="url" title="Helmholtz Munich and Partners Develop AI-Powered Sensor Patch for Neonatal Care ">Read more</a>

<img src="https://images.admiralcloud.com/v5/deliverEmbed/605e9401-c414-4bb7-b3fc-a2747b86cf59/image_webp/cropperjsfocus/2785/1723/440.540410300532,179.10914166155356,2785.8400000000006,1723.2000000000003,0,1,1/1392.5,861.4999999999999?poc=true" title="Angioplasty Procedure: Stent Deployment in a Coronary Artery AdobeStock_1219692882" itemprop="image" loading="lazy" width="2785" height="1723" alt="Angioplasty Procedure: Stent Deployment in a Coronary Artery AdobeStock_1219692882" />

AI, Transfer, New Research Findings, Computational Health, AIH, April 24, 2025

### AI-Powered Analysis of Stent Healing

A research team from Helmholtz Munich, the Technical University of Munich (TUM) and the TUM University Hospital has developed DeepNeo, an AI-powered algorithm that automates the process of analyzing coronary stents after implantation. The tool…

<a href="/en/newsroom/news-all/artikel/ai-powered-analysis-of-stent-healing" class="btn--arrow-next" itemprop="url" title="AI-Powered Analysis of Stent Healing">Read more</a>

<a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.helmholtz-munich.de%2Fen%2Faih%2Fnews-detailseite%2Fweeks-of-work-in-a-few-hours-ai-tool-reads-cell-membranes" class="c-sharebar__link" target="_blank" rel="nofollow noopener noreferrer"><span class="in2icon-before-linkedin"> Share </span></a> <a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.helmholtz-munich.de%2Fen%2Faih%2Fnews-detailseite%2Fweeks-of-work-in-a-few-hours-ai-tool-reads-cell-membranes" class="c-sharebar__link" target="_blank" rel="nofollow noopener noreferrer"><span class="in2icon-before-facebook"> Share </span></a> <a href="https://bsky.app/intent/compose?text=abchttps%3A%2F%2Fwww.helmholtz-munich.de%2Fen%2Faih%2Fnews-detailseite%2Fweeks-of-work-in-a-few-hours-ai-tool-reads-cell-membranes" class="c-sharebar__link" target="_blank" rel="nofollow noopener noreferrer"><span class="in2icon-before-bluesky"> Share </span></a> <a href="mailto:?body=Link:%20https%3A%2F%2Fwww.helmholtz-munich.de%2Fen%2Faih%2Fnews-detailseite%2Fweeks-of-work-in-a-few-hours-ai-tool-reads-cell-membranes" class="c-sharebar__link" target="_blank" rel="nofollow noopener noreferrer"><span class="in2icon-before-mail"> Mail </span></a>

