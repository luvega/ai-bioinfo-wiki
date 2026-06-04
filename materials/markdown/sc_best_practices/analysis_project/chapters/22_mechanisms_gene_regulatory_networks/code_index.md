# Code Index · Gene regulatory networks

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 13 | False | `import warnings` |
| 8 | python | 2 | True | `adata = sc.read_h5ad("../../data/openproblems_bmmc_multiome_genes_filtered.h5ad")` |
| 10 | python | 4 | True | `rna = adata[:, adata.var.feature_types == "GEX"]` |
| 11 | python | 1 | True | `rna.shape` |
| 13 | python | 1 | False | `sc.pp.highly_variable_genes(rna, batch_key="batch", flavor="seurat")` |
| 14 | python | 1 | False | `sc.set_figure_params(facecolor="white")` |
| 16 | python | 1 | True | `sc.pl.embedding(rna, "GEX_X_umap", color=["cell_type", "batch"])` |
| 18 | python | 2 | True | `adata_batch = rna[rna.obs.batch == "s1d1", :]` |
| 21 | python | 2 | True | `## this file has to be downloaded if not found` |
| 22 | python | 1 | False | `tfs_path = "allTFs_hg38.txt"` |
| 23 | python | 3 | False | `loom_path = "data/neurips_processed_input.loom"` |
| 25 | python | 4 | True | `# as a general QC. We inspect that our object has transcription factors listed in our main annotations.` |
| 27 | python | 6 | False | `use_hvg = True` |
| 29 | python | 10 | False | `row_attributes = {` |
| 32 | python | 1 | False | `num_workers = 3` |
| 33 | python | 3 | False | `outpath_adj = "adj.csv"` |
| 35 | python | 3 | True | `results_adjacencies = pd.read_csv("adj.csv", index_col=False, sep=",")` |
| 37 | python | 2 | True | `plt.hist(np.log10(results_adjacencies["importance"]), bins=50)` |
| 40 | bash | 1 | True | `!wget -nc https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg38/refseq_r80/mc9nr/gene_based/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs` |
| 41 | python | 3 | False | `# ranking databases` |
| 43 | bash | 1 | True | `!wget -nc https://resources.aertslab.org/cistarget/motif2tf/motifs-v9-nr.hgnc-m0.001-o0.0.tbl` |
| 44 | python | 2 | False | `# motif databases` |
| 46 | python | 8 | False | `if not Path("reg.csv").exists():` |
| 49 | python | 7 | True | `import numpy as np` |
| 51 | python | 16 | True | `fig, ax = plt.subplots(1, 1, figsize=(8, 5), dpi=100)` |
| 54 | python | 5 | False | `if not Path(loom_path_output).exists():` |
| 55 | python | 4 | False | `# collect SCENIC AUCell output` |
| 56 | python | 6 | True | `import anndata as ad` |
| 58 | python | 2 | False | `adata_batch.obsm["X_umap_aucell"] = ad_auc_mtx.obsm["X_umap"]` |
| 60 | python | 1 | True | `sc.pl.embedding(adata_batch, basis="X_umap_aucell", color="cell_type")` |
| 62 | python | 1 | True | `sc.pl.embedding(adata_batch, basis="X_tsne_aucell", color="cell_type")` |
| 64 | python | 1 | False | `import seaborn as sns` |
| 65 | python | 2 | False | `auc_mtx["cell_type"] = adata_batch.obs["cell_type"]` |
| 67 | python | 5 | False | `top_n = 50` |
| 69 | python | 7 | True | `sns.clustermap(` |
| 71 | python | 2 | False | `tf_names = top_tfs.index.str.replace(r"\(\+\)", "")` |
| 72 | python | 9 | True | `sc.pl.matrixplot(` |
| 76 | python | 25 | True | `%run ../src/lib.py` |
| 78 | python | 19 | True | `%run ../src/lib.py` |
