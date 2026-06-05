---
source: OSTA
title: "2 Spatial omics"
original_url: https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html
ingested_at: 2026-06-04T01:50:40+00:00
status: source_ingested
---

# 2  Spatial omics

## 2.1 Introduction

Spatial omics (or spatially-resolved omics) refers to a set of recently-developed technologies that enable molecular measurements (e.g. gene expression) with spatial resolution. Spatially-resolved transcriptomics and spatial proteomics were named the **Method of the Year 2020** ([“Method of the Year 2020: Spatially Resolved Transcriptomics” 2021](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-MethodOfYear2020)) and **Method of the Year 2024** ([“Method of the Year 2024: Spatial Proteomics” 2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-MethodOfYear2024)) by the journal *Nature Methods*, and have each become widely applied in a range of biological contexts.

### 2.1.1 Data modalities and technological platforms

In general, there are now a wide variety of data modalities that can be measured (e.g. gene expression, chromatin accessibility, histone modifications, and antibody-based protein abundance), with diverse measurement streams (e.g. high-throughput sequencing, imaging, and mass spectrometry), all of which give molecular measurements in a spatial context for a given tissue area.

Technological platforms differ drastically in terms of the experimental procedures used (sequence or ion counts versus fluorescence intensities), the feature space (dozens of proteins in imaging mass cytometry, to full transcriptome in Visium or Visium HD, to genome-wide assessments of chromatin accessibility), and spatial resolution (e.g. single-cell resolution, or multiple cells per measurement location). In general, this also means there are tradeoffs between the spatial resolution, number of features, and sensitivity of the assays.

Platforms may be broadly grouped into “sequencing-based” and “imaging-based” technologies; some of the latter can be further classified into “molecule-based” or not. The main platforms are described in more detail below. Sequencing-based platforms tend to provide higher gene coverage (e.g. full transcriptome), while imaging-based platforms tend to provide higher spatial resolution (e.g. single-cell or subcellular resolution).

### 2.1.2 Commercially available platforms

In this book, we focus on commercially available platforms, since these are the most widely used and accessible. However, the data representations are often similar for other related platforms. The initial chapters of this book are split into separate parts for sequencing-based and imaging-based platforms, since several analysis techniques are specific to each of these, followed by chapters for platform-independent and other analyses.

In the sections below, we give a brief overview of several commercially available platforms. For more in-depth background, several recent reviews are available, covering available platforms, analysis methods, outstanding challenges, and additional topics ([Bressan, Battistoni, and Hannon 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Bressan2023-dawn); [Moses and Pachter 2022](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Moses2022-museum); [Tian, Chen, and Macosko 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Tian2023-vistas); [Lundberg and Borner 2019](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Lundberg2019-proteomics); [Gulati et al. 2025](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Gulati2024-profiling); [Paul et al. 2021](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Paul2021-imaging); [Mund, Brunner, and Mann 2022](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Mund2022-unbiased); [Palla et al. 2022](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Palla2022-components); [Moffitt, Lundberg, and Heyn 2022](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Moffitt2022-emerging); [Rao et al. 2021](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Rao2021-exploring); [Cheng et al. 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Cheng2023-comprehensive)).

## 2.2 Sequencing-based spatial transcriptomics

Sequencing-based platforms capture molecular information (which could represent gene expression, DNA binding, antibody-conjugated tags, etc.) at a set of spatial measurement locations for a tissue section placed on a slide. The spatial location is tagged via a unique barcode for each measurement location, and reads are summarized (e.g. as counts) according to features such as genes or bins.

The advantage of sequencing is that typically the features represent an untargeted set of molecular entities, thus not requiring panel selection and optimization. In practice, many spatial assays still require panels (e.g. spatial variants of CITE-seq ([Liu et al. 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Liu2023-spatial-CITE-seq))), and assays such as Visium (v2 WT) and Visium HD (WT) use transcriptome-wide gene capture panels, and thus cannot always be applied to non-model organisms.

Spatial resolution varies between platforms, and depends on the size and spacing between the spatial measurement locations. Depending on the spatial resolution and tissue cell density in a given biological sample, each spatial measurement location may contain zero, one, or multiple cells. For these platforms, the spatial measurement locations are often referred to as “spots”, “beads”, or “bins”.

## 2.3 Imaging-based spatial transcriptomics

Imaging-based platforms (or molecule-based platforms) identify the spatial locations of individual RNA molecules by sequential in situ hybridization (ISH) or in situ sequencing (ISS), for targeted panels of up to hundreds or thousands of genes. Since transcripts are individually identified, the raw data is collected at subcellular spatial resolution.

Image segmentation is used to identify the boundaries of individual cells or nuclei, and assign RNA molecules to cells or nuclei during preprocessing. Segmentation into cells is challenging, especially due to overlapping cells (i.e. cells have 3-dimensional organization and the plane that a tissue section represents may have material from multiple cells at a given x/y location). After segmentation, gene counts may be aggregated to the cell level, or analyses may be performed directly at the molecule level. Cell-level analyses may re-use methods developed for spot-level spatial transcriptomics data or single-cell data.

The selection of targeted sets of biologically informative genes for an experiment, referred to as panel design, is a key consideration during experimental design ([Baran and Doğan 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Baran2023-marker); [Kuemmerle et al. 2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Kuemmerle2024-probe-set); [Y. Zhang et al. 2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Zhang2024-panel)). Several commercially available options for targeted gene sets suitable for certain biological contexts are available.

## 2.4 Other types of spatial omics data

### 2.4.1 Spatial proteomics

Imaging-based proteomics, also called multiplexed imaging, represents a broad array of spatial detection technologies, the vast majority of which are antibody-based. Semba and Ishimoto ([2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Semba2024-multiplexed)) categorize these antibody-based technologies into either “single-shot” (e.g. imaging mass cytometry; IMC) or “multicycle” (e.g. Lunaphore) imaging approaches. Single-shot refers to the set of, for example, heavy metal ions (representing protein presence), resulting from a laser ablation of a pre-stained sample. Multicycle approaches refer to sets of antibodies that are sequentially stained and stripped, with an imaging step at each cycle. The two most common single-shot spatial proteomics platforms are IMC and MIBIscope, with maximum pixel resolution of 0.4 µm and 1 µm, respectively, and each platform measuring upwards of 40 channels (proteins) ([Semba and Ishimoto 2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Semba2024-multiplexed)).

### 2.4.2 Other modalities

While the focus of the data analyses in this book is primarily on spatially-resolved gene and protein expression, here we also mention other modalities or data structures that are adjacent or emerging. These will not be directly covered in the data examples in the book, but some of the analysis steps discussed in the chapters may have applications to these other contexts.

Tissues are three-dimensional (3D) entities that are represented as 2D slices for many of the analyses discussed here. However, there will be various emerging datasets that have measurements made along a third dimension ([Schott et al. 2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Schott2024-Open-ST); [Vickovic et al. 2022](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Vickovic2022-three-dimensional)), whether this is directly measured (e.g. 3D imaging) or indirectly reconstructed from multiple per-slice measurements ([Schott et al. 2025](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Schott2025-protocol)). In some cases, the analyses discussed in this book will either still apply, or can be applied successively on multiple slices.

Multi-omics datasets (e.g. RNA expression and protein abundance, or RNA expression and chomatin accessibility) that are collected in a spatial context are now emerging (e.g. ([Liu et al. 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Liu2023-spatial-CITE-seq); [D. Zhang et al. 2023](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Zhang2023-spatial-epigenome))). Epigenomic modalities, in particular, may require alternative preprocessing steps, but some of the analyses mentioned in the chapters here could be re-used (e.g. clustering given a low-dimensional embedding) or adapted.

Another emerging modality within a spatial context is the measurement of metabolites, lipids, or proteins via mass spectrometry imaging (MSI), such as MALDI-MSI ([H. Zhang et al. 2024](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Zhang2024-MSI)); these assays are sometimes known as imaging mass spectrometry. MSI typically involves coating tissues with a matrix layer that promotes the ionization of analytes of interest (e.g. glycans; ([Palomino and Muddiman 2025](https://bioconductor.org/books/release/OSTA/pages/bkg-spatial-omics.html#ref-Palomino2024-mass))). Integration of MSI with other spatial modalities (e.g. to reveal cell types) may also be promising.

## 2.5 Appendix

### References

Baran, Yusuf, and Berat Doğan. 2023. “scMAGS: Marker Gene Selection from scRNA-Seq Data for Spatial Transcriptomics Studies.” *Computers in Biology and Medicine* 155 (106634). <https://doi.org/10.1016/j.compbiomed.2023.106634>.

Bressan, Dario, Giorgia Battistoni, and Gregory J. Hannon. 2023. “The Dawn of Spatial Omics.” *Science* 381. <https://doi.org/10.1126/science.abq4964>.

Cheng, Mengnan, Yujia Jiang, Jiangshan Xu, Alexios-Fotios A. Mentis, Shuai Wang, Huiwen Zheng, Sunil Kumar Sahu, Longqi Liu, and Xun Xu. 2023. “Spatially Resolved Transcriptomics: A Comprehensive Review of Their Technological Advances, Applications, and Challenges.” *Journal of Genetics and Genomics* 50: 625–40. <https://doi.org/10.1016/j.jgg.2023.03.011>.

Gulati, Gunsagar S., Jeremy Philip D’Silva, Yunhe Liu, Linghua Wang, and Aaron M. Newman. 2025. “Profiling Cell Identity and Tissue Architecture with Single-Cell and Spatial Transcriptomics.” *Nature Reviews Molecular Cell Biology* 26: 11–31. <https://doi.org/10.1038/s41580-024-00768-2>.

Kuemmerle, Louis B., Malte D. Luecken, Alexandra B. Firsova, Lisa Barros de Andrade e Sousa, Lena Straßer, Ilhem Isra Mekki, Francesco Campi, et al. 2024. “Probe Set Selection for Targeted Spatial Transcriptomics.” *Nature Methods* 21: 2260–70. <https://doi.org/10.1038/s41592-024-02496-z>.

Liu, Yang, Marcello DiStasio, Graham Su, Hiromitsu Asashima, Archibald Enninful, Xiaoyu Qin, Yanxiang Deng, et al. 2023. “High-Plex Protein and Whole Transcriptome Co-Mapping at Cellular Resolution with Spatial CITE-Seq.” *Nature Biotechnology* 41: 1405–9. <https://doi.org/10.1038/s41587-023-01676-0>.

Lundberg, Emma, and Georg H. H. Borner. 2019. “Spatial Proteomics: A Powerful Discovery Tool for Cell Biology.” *Nature Reviews Molecular Cell Biology* 20: 285–302. <https://doi.org/10.1038/s41580-018-0094-y>.

“Method of the Year 2020: Spatially Resolved Transcriptomics.” 2021. *Nature Methods* 18: 1. <https://doi.org/10.1038/s41592-020-01042-x>.

“Method of the Year 2024: Spatial Proteomics.” 2024. *Nature Methods* 21: 2195–96. <https://doi.org/10.1038/s41592-024-02565-3>.

Moffitt, Jeffrey R., Emma Lundberg, and Holger Heyn. 2022. “The Emerging Landscape of Spatial Profiling Technologies.” *Nature Reviews Genetics* 23: 741–59. <https://doi.org/10.1038/s41576-022-00515-3>.

Moses, Lambda, and Lior Pachter. 2022. “Museum of Spatial Transcriptomics.” *Nature Methods* 19: 534–46. <https://doi.org/10.1038/s41592-022-01409-2>.

Mund, Andreas, Andreas-David Brunner, and Matthias Mann. 2022. “Unbiased Spatial Proteomics with Single-Cell Resolution in Tissues.” *Molecular Cell* 82: 2335–49. <https://doi.org/10.1016/j.molcel.2022.05.022>.

Palla, Giovanni, David S. Fischer, Aviv Regev, and Fabian J. Theis. 2022. “Spatial Components of Molecular Tissue Biology.” *Nature Biotechnology* 40: 308–18. <https://doi.org/10.1038/s41587-021-01182-1>.

Palomino, Tana V., and David C. Muddiman. 2025. “Mass Spectrometry Imaging of n-Linked Glycans: Fundamentals and Recent Advances.” *Mass Spectrometry Reviews*, 1–25. <https://doi.org/10.1002/mas.21895>.

Paul, Indranil, Carl White, Isabella Turcinovic, and Andrew Emili. 2021. “Imaging the Future: The Emerging Era of Single-Cell Spatial Proteomics.” *The FEBS Journal* 288: 6990–7001. <https://doi.org/10.1111/febs.15685>.

Rao, Anjali, Dalia Barkley, Gustavo S. França, and Itai Yanai. 2021. “Exploring Tissue Architecture Using Spatial Transcriptomics.” *Nature* 596: 211–20. https://doi.org/<https://doi.org/10.1038/s41586-021-03634-9>.

Schott, Marie, Daniel León-Periñán, Elena Splendiani, Elisabetta Ferretti, Giuseppe Macino, Nikos Karaiskos, and Nikolaus Rajewsky. 2025. “Protocol for High-Resolution 3D Spatial Transcriptomics Using Open-ST.” *STAR Protocols* 6 (103521, 1). <https://doi.org/10.1016/j.xpro.2024.103521>.

Schott, Marie, Daniel León-Periñán, Elena Splendiani, Leon Strenger, Jan Robin Licha, Tancredi Massimo Pentimalli, Simon Schallenberg, et al. 2024. “Open-ST: High-Resolution Spatial Transcriptomics in 3D.” *Cell* 187: 3953–72. <https://doi.org/10.1016/j.cell.2024.05.055>.

Semba, Takashi, and Takatsugu Ishimoto. 2024. “Spatial Analysis by Current Multiplexed Imaging Technologies for the Molecular Characterisation of Cancer Tissues.” *British Journal of Cancer* 131: 1737–47. <https://doi.org/10.1038/s41416-024-02882-6>.

Tian, Luyi, Fei Chen, and Evan Z. Macosko. 2023. “The Expanding Vistas of Spatial Transcriptomics.” *Nature Biotechnology* 41: 773–82. <https://doi.org/10.1038/s41587-022-01448-2>.

Vickovic, Sanja, Denis Schapiro, Konstantin Carlberg, Britta Lötstedt, Ludvig Larsson, Franziska Hildebrandt, Marina Korotkova, et al. 2022. “Three-Dimensional Spatial Transcriptomics Uncovers Cell Type Localizations in the Human Rheumatoid Arthritis Synovium.” *Communications Biology* 5 (129). <https://doi.org/10.1038/s42003-022-03050-3>.

Zhang, Di, Yanxiang Deng, Petra Kukanja, Eneritz Agirre, Marek Bartosovic, Mingze Dong, Cong Ma, et al. 2023. “Spatial Epigenome–Transcriptome Co-Profiling of Mammalian Tissues.” *Nature* 616: 113–22. <https://doi.org/10.1038/s41586-023-05795-1>.

Zhang, Hua, Kelly H. Lu, Malik Ebbini, Penghsuan Huang, Haiyan Lu, and Lingjun Li. 2024. “Mass Spectrometry Imaging for Spatially Resolved Multi-Omics Molecular Mapping.” *Npj Imaging* 2 (20). <https://doi.org/10.1038/s44303-024-00025-3>.

Zhang, Yida, Viktor Petukhov, Evan Biederstedt, Richard Que, Kun Zhang, and Peter V. Kharchenko. 2024. “Gene Panel Selection for Targeted Spatial Transcriptomics.” *Genome Biology* 25 (35). <https://doi.org/10.1186/s13059-024-03174-1>.

Back to top
