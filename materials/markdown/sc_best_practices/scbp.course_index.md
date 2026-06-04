---
type: course-source-index
title: Single-cell Best Practices 课程素材索引
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated_draft
tags: [single-cell, scbp, course-material, auto-extract]
---

# Single-cell Best Practices 课程素材索引

本索引从 upstream Jupyter Book 全量 notebook/Markdown 构建，用于 Week 13-16 的单细胞、降维、聚类、差异分析和可视化备课。

## 工程入口

- Upstream raw bundle: `materials/raw/sc_best_practices/upstream`
- Runnable project: [`analysis_project/README.md`](analysis_project/README.md)
- Dataset manifest: [`analysis_project/datasets_manifest.json`](analysis_project/datasets_manifest.json)
- Extracted outputs: [`extracted_outputs/outputs_index.md`](extracted_outputs/outputs_index.md)

## 章节映射

| Order | Part | Title | Course weeks | Code | Environment |
|---|---|---|---|---|---|
| 00 | Preamble | [Single-cell best practices](analysis_project/chapters/00_preamble/chapter.source.md) | Week 16 | [code](analysis_project/chapters/00_preamble/chapter.py) | _config |
| 01 | Introduction | [Prior art](analysis_project/chapters/01_introduction_prior_art/chapter.source.md) | - | [code](analysis_project/chapters/01_introduction_prior_art/chapter.py) | advanced_data_structures_and_frameworks |
| 02 | Introduction | [Single-cell RNA sequencing](analysis_project/chapters/02_introduction_scrna_seq/chapter.source.md) | Week 14, Week 16 | [code](analysis_project/chapters/02_introduction_scrna_seq/chapter.py) | advanced_data_structures_and_frameworks |
| 03 | Introduction | [Raw data processing](analysis_project/chapters/03_introduction_raw_data_processing/chapter.source.md) | Week 14 | [code](analysis_project/chapters/03_introduction_raw_data_processing/chapter.py) | advanced_data_structures_and_frameworks |
| 04 | Introduction | [Fundamental data structures and frameworks](analysis_project/chapters/04_introduction_fundamental_data_structures_and_frameworks/chapter.source.md) | Week 14 | [code](analysis_project/chapters/04_introduction_fundamental_data_structures_and_frameworks/chapter.py) | advanced_data_structures_and_frameworks |
| 05 | Introduction | [Multimodal and spatial data structures](analysis_project/chapters/05_introduction_advanced_data_structures_and_frameworks/chapter.source.md) | Week 14, Week 16 | [code](analysis_project/chapters/05_introduction_advanced_data_structures_and_frameworks/chapter.py) | advanced_data_structures_and_frameworks |
| 06 | Introduction | [Interoperability](analysis_project/chapters/06_introduction_interoperability/chapter.source.md) | Week 14 | [code](analysis_project/chapters/06_introduction_interoperability/chapter.py) | advanced_data_structures_and_frameworks |
| 07 | Introduction | [GPU-accelerated analysis](analysis_project/chapters/07_introduction_rapids_singlecell/chapter.source.md) | Week 14 | [code](analysis_project/chapters/07_introduction_rapids_singlecell/chapter.py) | advanced_data_structures_and_frameworks |
| 08 | Preprocessing and visualization | [Quality Control](analysis_project/chapters/08_preprocessing_visualization_quality_control/chapter.source.md) | Week 16 | [code](analysis_project/chapters/08_preprocessing_visualization_quality_control/chapter.py) | preprocessing |
| 09 | Preprocessing and visualization | [Normalization](analysis_project/chapters/09_preprocessing_visualization_normalization/chapter.source.md) | Week 16 | [code](analysis_project/chapters/09_preprocessing_visualization_normalization/chapter.py) | preprocessing |
| 10 | Preprocessing and visualization | [Feature selection](analysis_project/chapters/10_preprocessing_visualization_feature_selection/chapter.source.md) | Week 16 | [code](analysis_project/chapters/10_preprocessing_visualization_feature_selection/chapter.py) | preprocessing |
| 11 | Preprocessing and visualization | [Dimensionality Reduction](analysis_project/chapters/11_preprocessing_visualization_dimensionality_reduction/chapter.source.md) | Week 13 | [code](analysis_project/chapters/11_preprocessing_visualization_dimensionality_reduction/chapter.py) | preprocessing |
| 12 | Identifying cellular structure | [Clustering](analysis_project/chapters/12_cellular_structure_clustering/chapter.source.md) | Week 13 | [code](analysis_project/chapters/12_cellular_structure_clustering/chapter.py) | annotation |
| 13 | Identifying cellular structure | [Annotation](analysis_project/chapters/13_cellular_structure_annotation/chapter.source.md) | Week 16 | [code](analysis_project/chapters/13_cellular_structure_annotation/chapter.py) | annotation |
| 14 | Identifying cellular structure | [Data integration](analysis_project/chapters/14_cellular_structure_integration/chapter.source.md) | Week 16 | [code](analysis_project/chapters/14_cellular_structure_integration/chapter.py) | annotation |
| 15 | Inferring trajectories | [Pseudotemporal ordering](analysis_project/chapters/15_trajectories_pseudotemporal/chapter.source.md) | Week 16 | [code](analysis_project/chapters/15_trajectories_pseudotemporal/chapter.py) | lineage-tracing |
| 16 | Inferring trajectories | [RNA velocity](analysis_project/chapters/16_trajectories_rna_velocity/chapter.source.md) | Week 16 | [code](analysis_project/chapters/16_trajectories_rna_velocity/chapter.py) | lineage-tracing |
| 17 | Inferring trajectories | [Lineage tracing](analysis_project/chapters/17_trajectories_lineage_tracing/chapter.source.md) | - | [code](analysis_project/chapters/17_trajectories_lineage_tracing/chapter.py) | lineage-tracing |
| 18 | Dealing with conditions | [Differential gene expression analysis](analysis_project/chapters/18_conditions_differential_gene_expression/chapter.source.md) | Week 15 | [code](analysis_project/chapters/18_conditions_differential_gene_expression/chapter.py) | compositional |
| 19 | Dealing with conditions | [Compositional analysis](analysis_project/chapters/19_conditions_compositional/chapter.source.md) | Week 15 | [code](analysis_project/chapters/19_conditions_compositional/chapter.py) | compositional |
| 20 | Dealing with conditions | [Gene set enrichment and pathway analysis](analysis_project/chapters/20_conditions_gsea_pathway/chapter.source.md) | Week 15 | [code](analysis_project/chapters/20_conditions_gsea_pathway/chapter.py) | compositional |
| 21 | Dealing with conditions | [Perturbation modeling](analysis_project/chapters/21_conditions_perturbation_modeling/chapter.source.md) | Week 15 | [code](analysis_project/chapters/21_conditions_perturbation_modeling/chapter.py) | compositional |
| 22 | Modeling mechanisms | [Gene regulatory networks](analysis_project/chapters/22_mechanisms_gene_regulatory_networks/chapter.source.md) | - | [code](analysis_project/chapters/22_mechanisms_gene_regulatory_networks/chapter.py) | cellcell |
| 23 | Modeling mechanisms | [Cell-cell communication](analysis_project/chapters/23_mechanisms_cell_cell_communication/chapter.source.md) | - | [code](analysis_project/chapters/23_mechanisms_cell_cell_communication/chapter.py) | cellcell |
| 24 | Deconvolution | [Bulk deconvolution](analysis_project/chapters/24_deconvolution_bulk_deconvolution/chapter.source.md) | - | [code](analysis_project/chapters/24_deconvolution_bulk_deconvolution/chapter.py) | - |
| 25 | Chromatin Accessibility | [Single-cell ATAC sequencing](analysis_project/chapters/25_chromatin_accessibility_introduction/chapter.source.md) | Week 16 | [code](analysis_project/chapters/25_chromatin_accessibility_introduction/chapter.py) | gene-regulatory-networks-atac |
| 26 | Chromatin Accessibility | [Quality Control](analysis_project/chapters/26_chromatin_accessibility_quality_control/chapter.source.md) | Week 16 | [code](analysis_project/chapters/26_chromatin_accessibility_quality_control/chapter.py) | gene-regulatory-networks-atac |
| 27 | Chromatin Accessibility | [Gene regulatory networks](analysis_project/chapters/27_chromatin_accessibility_gene_regulatory_networks_atac/chapter.source.md) | - | [code](analysis_project/chapters/27_chromatin_accessibility_gene_regulatory_networks_atac/chapter.py) | gene-regulatory-networks-atac |
| 28 | Spatial omics | [Single-cell data resolved in space](analysis_project/chapters/28_spatial_introduction/chapter.source.md) | Week 16 | [code](analysis_project/chapters/28_spatial_introduction/chapter.py) | spatial |
| 29 | Spatial omics | [Neighborhood analysis](analysis_project/chapters/29_spatial_neighborhood/chapter.source.md) | Week 16 | [code](analysis_project/chapters/29_spatial_neighborhood/chapter.py) | spatial |
| 30 | Spatial omics | [Spatial domains](analysis_project/chapters/30_spatial_domains/chapter.source.md) | Week 16 | [code](analysis_project/chapters/30_spatial_domains/chapter.py) | spatial |
| 31 | Spatial omics | [Spatially variable genes](analysis_project/chapters/31_spatial_spatially_variable_genes/chapter.source.md) | Week 16 | [code](analysis_project/chapters/31_spatial_spatially_variable_genes/chapter.py) | spatial |
| 32 | Spatial omics | [Spatial deconvolution](analysis_project/chapters/32_spatial_deconvolution/chapter.source.md) | Week 16 | [code](analysis_project/chapters/32_spatial_deconvolution/chapter.py) | spatial |
| 33 | Spatial omics | [Imputation](analysis_project/chapters/33_spatial_imputation/chapter.source.md) | Week 16 | [code](analysis_project/chapters/33_spatial_imputation/chapter.py) | spatial |
| 34 | Surface protein | [Quality control](analysis_project/chapters/34_surface_protein_quality_control/chapter.source.md) | Week 16 | [code](analysis_project/chapters/34_surface_protein_quality_control/chapter.py) | surface-protein |
| 35 | Surface protein | [Normalization](analysis_project/chapters/35_surface_protein_normalization/chapter.source.md) | Week 16 | [code](analysis_project/chapters/35_surface_protein_normalization/chapter.py) | surface-protein |
| 36 | Surface protein | [Doublet detection](analysis_project/chapters/36_surface_protein_doublet_detection/chapter.source.md) | - | [code](analysis_project/chapters/36_surface_protein_doublet_detection/chapter.py) | surface-protein |
| 37 | Surface protein | [Dimensionality Reduction](analysis_project/chapters/37_surface_protein_dimensionality_reduction/chapter.source.md) | Week 13 | [code](analysis_project/chapters/37_surface_protein_dimensionality_reduction/chapter.py) | surface-protein |
| 38 | Surface protein | [Batch correction](analysis_project/chapters/38_surface_protein_batch_correction/chapter.source.md) | - | [code](analysis_project/chapters/38_surface_protein_batch_correction/chapter.py) | surface-protein |
| 39 | Surface protein | [Annotation](analysis_project/chapters/39_surface_protein_annotation/chapter.source.md) | Week 16 | [code](analysis_project/chapters/39_surface_protein_annotation/chapter.py) | surface-protein |
| 40 | Adaptive immune receptor repertoire | [Immune Receptor Profiling](analysis_project/chapters/40_air_repertoire_ir_profiling/chapter.source.md) | - | [code](analysis_project/chapters/40_air_repertoire_ir_profiling/chapter.py) | - |
| 41 | Adaptive immune receptor repertoire | [Clonotype analysis](analysis_project/chapters/41_air_repertoire_clonotype/chapter.source.md) | - | [code](analysis_project/chapters/41_air_repertoire_clonotype/chapter.py) | - |
| 42 | Adaptive immune receptor repertoire | [Specificity analysis](analysis_project/chapters/42_air_repertoire_specificity/chapter.source.md) | - | [code](analysis_project/chapters/42_air_repertoire_specificity/chapter.py) | - |
| 43 | Adaptive immune receptor repertoire | [Integrating AIR and transcriptomics](analysis_project/chapters/43_air_repertoire_multimodal_integration/chapter.source.md) | Week 16 | [code](analysis_project/chapters/43_air_repertoire_multimodal_integration/chapter.py) | - |
| 44 | Multimodal integration | [Paired integration](analysis_project/chapters/44_multimodal_integration_paired_integration/chapter.source.md) | Week 16 | [code](analysis_project/chapters/44_multimodal_integration_paired_integration/chapter.py) | advanced-integration |
| 45 | Multimodal integration | [Advanced integration](analysis_project/chapters/45_multimodal_integration_advanced_integration/chapter.source.md) | Week 16 | [code](analysis_project/chapters/45_multimodal_integration_advanced_integration/chapter.py) | advanced-integration |
| 46 | Outlook | [Outlook](analysis_project/chapters/46_outlook/chapter.source.md) | - | [code](analysis_project/chapters/46_outlook/chapter.py) | _config |
| 47 | Acknowledgements | [Acknowledgements](analysis_project/chapters/47_acknowledgements/chapter.source.md) | - | [code](analysis_project/chapters/47_acknowledgements/chapter.py) | _config |
| 48 | Glossary | [Glossary](analysis_project/chapters/48_glossary/chapter.source.md) | - | [code](analysis_project/chapters/48_glossary/chapter.py) | _config |
| 49 | Changelog | [Changelog](analysis_project/chapters/49_changelog/chapter.source.md) | - | [code](analysis_project/chapters/49_changelog/chapter.py) | _config |

## 周次使用建议

- Week 13: dimensionality reduction、clustering、PCA/UMAP 参数解释。
- Week 14: scRNA-seq raw data processing、AnnData/Scanpy 数据结构和互操作。
- Week 15: differential gene expression、compositional analysis、GSEA/pathway。
- Week 16: QC、normalization、feature selection、annotation、integration、trajectory。

正式进入 PPT 前仍需回查 upstream 章节、数据许可和课程主线，不能把 notebook 输出直接当作医学或统计结论。
