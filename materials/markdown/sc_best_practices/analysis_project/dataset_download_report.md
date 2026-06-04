# SCBP Dataset Download Report

- Downloaded: 2
- Blocked/manual: 52
- Output root: `E:/Codex_Projects/AI_Course/outputs/sc_best_practices/datasets`

| Status | Source | Value | Reason / Local path |
|---|---|---|---|
| downloaded | `introduction/raw_data_processing` | `https://teichlab.github.io/scg_lib_structs/data/10X-Genomics/3M-february-2018.txt.gz` | URL path looks like a data file. |
| manual_required | `introduction/raw_data_processing` | `https://www.10xgenomics.com/resources/datasets/200-sorted-cells-from-human-glioblastoma-multiforme-3-lt-v-3-1-3-1-low-6-0-0` | 10x dataset page is not a direct file endpoint. |
| failed | `introduction/raw_data_processing` | `https://umd.box.com/shared/static/lx2xownlrhz3us8496tyu9c4dgade814.gz` | HTTP 400: Bad Request |
| downloaded | `introduction/raw_data_processing` | `https://github.com/f0t1h/3M-february-2018/raw/master/3M-february-2018.txt.gz` | URL path looks like a data file. |
| manual_required | `introduction/raw_data_processing` | `wget -qO- https://umd.box.com/shared/static/lx2xownlrhz3us8496tyu9c4dgade814.gz \| tar xzf - --strip-components=1 -C .` |  |
| manual_required | `introduction/raw_data_processing` | `wget -qO- https://github.com/f0t1h/3M-february-2018/raw/master/3M-february-2018.txt.gz \| gunzip - > 3M-february-2018.txt` |  |
| failed | `introduction/advanced_data_structures_and_frameworks` | `https://s3.embl.de/spatialdata/spatialdata-sandbox/mouse_liver.zip` | [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1032) |
| manual_required | `introduction/interoperability` | `key="introduction/interoperability_adata.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `introduction/interoperability` | `key="introduction/interoperability_mdata.h5mu", is_latest=True` | Requires lamindb connection and artifact lookup. |
| blocked_oversize | `introduction/rapids_singlecell` | `https://exampledata.scverse.org/rapids-singlecell/dli_census.h5ad` | Content-Length 885572153 exceeds limit 209715200. |
| manual_required | `preprocessing_visualization/quality_control` | `key="preprocessing_visualization/quality_control_adata.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `preprocessing_visualization/normalization` | `key="preprocessing_visualization/s4d8_quality_control.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `preprocessing_visualization/feature_selection` | `key="preprocessing_visualization/s4d8_normalization.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `preprocessing_visualization/dimensionality_reduction` | `key="preprocessing_visualization/s4d8_feature_selection.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `cellular_structure/annotation` | `key="cellular_structure/annotation_reference_features.csv", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `cellular_structure/annotation` | `key="cellular_structure/annotation_reference_model.pt", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `trajectories/pseudotemporal` | `key="trajectory/pseudotemporal.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `trajectories/rna_velocity` | `key="trajectory/rna_velocity.h5ad", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `trajectories/lineage_tracing` | `https://zenodo.org/record/5847462#.YrFDKuzMI6A` | Zenodo record requires file selection or license review. |
| manual_required | `trajectories/lineage_tracing` | `https://zenodo.org/record/5847462/files/KPTracer-Data.tar.gz?download=1` | Zenodo record requires file selection or license review. |
| manual_required | `trajectories/lineage_tracing` | `!wget "https://zenodo.org/record/5847462/files/KPTracer-Data.tar.gz?download=1"` |  |
| failed_empty | `conditions/gsea_pathway` | `https://figshare.com/ndownloader/files/34464122` | Downloaded zero bytes. |
| failed_empty | `conditions/gsea_pathway` | `https://figshare.com/ndownloader/files/35233771` | Downloaded zero bytes. |
| manual_required | `conditions/gsea_pathway` | `!wget -O 'c2.cp.reactome.v7.5.1.symbols.gmt' https://figshare.com/ndownloader/files/35233771` |  |
| manual_required | `mechanisms/gene_regulatory_networks` | `!wget -nc https://raw.githubusercontent.com/aertslab/SCENICprotocol/master/example/allTFs_hg38.txt` |  |
| manual_required | `mechanisms/gene_regulatory_networks` | `!wget -nc https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg38/refseq_r80/mc9nr/gene_based/hg38__refseq-r80__10kb_up_and_dow` |  |
| manual_required | `mechanisms/gene_regulatory_networks` | `!wget -nc https://resources.aertslab.org/cistarget/motif2tf/motifs-v9-nr.hgnc-m0.001-o0.0.tbl` |  |
| failed_empty | `mechanisms/cell_cell_communication` | `https://figshare.com/ndownloader/files/34464122` | Downloaded zero bytes. |
| manual_required | `mechanisms/cell_cell_communication` | `https://zenodo.org/badge/DOI/10.5281/zenodo.7074291.svg` | Zenodo record requires file selection or license review. |
| manual_required | `mechanisms/cell_cell_communication` | `https://zenodo.org/record/7074291/files/ligand_target_matrix_nsga2r_final.rds` | Zenodo record requires file selection or license review. |
| manual_required | `mechanisms/cell_cell_communication` | `https://zenodo.org/record/7074291/files/lr_network_human_21122021.rds` | Zenodo record requires file selection or license review. |
| manual_required | `chromatin_accessibility/quality_control` | `https://zenodo.org/record/5189588#.ZDlrwexBxqs` | Zenodo record requires file selection or license review. |
| failed_empty | `spatial/deconvolution` | `https://figshare.com/ndownloader/files/39347357` | Downloaded zero bytes. |
| failed_empty | `spatial/deconvolution` | `https://figshare.com/ndownloader/files/39347573` | Downloaded zero bytes. |
| failed_empty | `spatial/imputation` | `https://figshare.com/ndownloader/files/39360860` | Downloaded zero bytes. |
| failed_empty | `spatial/imputation` | `https://figshare.com/ndownloader/files/39360836` | Downloaded zero bytes. |
| manual_required | `surface_protein/quality_control` | `key="surface-protein/cite_filtered.h5mu", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `surface_protein/normalization` | `key="surface-protein/cite_quality_control.h5mu",
    is_latest=True,` | Requires lamindb connection and artifact lookup. |
| manual_required | `surface_protein/normalization` | `key="surface-protein/cite_raw.h5mu",
    is_latest=True,` | Requires lamindb connection and artifact lookup. |
| manual_required | `surface_protein/doublet_detection` | `key="surface-protein/cite_normalization.h5mu", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `surface_protein/dimensionality_reduction` | `key="surface-protein/cite_doublet_detection.h5mu", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `surface_protein/batch_correction` | `key="surface-protein/cite_dimensionality_reduction.h5mu", is_latest=True` | Requires lamindb connection and artifact lookup. |
| manual_required | `surface_protein/annotation` | `key="surface-protein/cite_batch_correction.h5mu", is_latest=True` | Requires lamindb connection and artifact lookup. |
| failed_empty | `air_repertoire/ir_profiling` | `https://figshare.com/ndownloader/files/35574338` | Downloaded zero bytes. |
| failed_empty | `air_repertoire/ir_profiling` | `https://figshare.com/ndownloader/files/35574539` | Downloaded zero bytes. |
| blocked | `air_repertoire/ir_profiling` | `https://s3-eu-west-1.amazonaws.com/pfigshare-u-files/35574338/bcr_cellranger.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIYCQY` | Temporary signed URL is likely expired. |
| blocked | `air_repertoire/ir_profiling` | `https://s3-eu-west-1.amazonaws.com/pfigshare-u-files/35574539/TCR_mergedUpdated.tsv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIY` | Temporary signed URL is likely expired. |
| manual_required | `air_repertoire/ir_profiling` | `! wget -O $path_bcr_input -nc https://figshare.com/ndownloader/files/35574338` |  |
| manual_required | `air_repertoire/ir_profiling` | `! wget -O $path_tcr_input -nc https://figshare.com/ndownloader/files/35574539` |  |
| failed | `air_repertoire/specificity` | `http://opig.stats.ox.ac.uk/webapps/covabdab/static/downloads/CoV-AbDab_200422.csv` | HTTP 404: NOT FOUND |
| manual_required | `air_repertoire/specificity` | `!wget -O tmp/CoV-AbDab.csv http://opig.stats.ox.ac.uk/webapps/covabdab/static/downloads/CoV-AbDab_200422.csv` |  |
| failed_empty | `air_repertoire/multimodal_integration` | `https://www.ebi.ac.uk/arrayexpress/files/E-MTAB-10026/E-MTAB-10026.processed.4.zip` | Downloaded zero bytes. |
| failed_empty | `air_repertoire/multimodal_integration` | `https://figshare.com/ndownloader/files/35574338` | Downloaded zero bytes. |
| manual_required | `air_repertoire/multimodal_integration` | `! wget -O $path_bcr_input -nc https://figshare.com/ndownloader/files/35574338` |  |
