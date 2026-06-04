# Code Index · Bulk deconvolution

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 13 | python | 4 | False | `import numpy as np` |
| 16 | python | 6 | True | `data_file = "/storage/groups/ml01/workspace/amit.frishberg/OriginalData/"` |
| 17 | python | 1 | True | `adata.obs["cluster_labels_res.0.8"].value_counts()` |
| 18 | python | 4 | False | `bulk = pd.read_csv(data_file + "BulkSmall.txt", sep="\t", index_col=0)` |
| 21 | python | 5 | True | `adata = adata[` |
| 23 | python | 5 | True | `# removing very rare cells` |
| 25 | python | 3 | False | `bulk_sc_genes = np.intersect1d(bulk.index, adata.var_names)` |
| 28 | python | 5 | False | `sc.pp.normalize_per_cell(adata, counts_per_cell_after=1e4, copy=False)` |
| 30 | python | 5 | True | `sc.tl.pca(adata_log)` |
| 33 | python | 7 | True | `# R interface` |
| 35 | python | 17 | True | `import itertools` |
| 37 | python | 2 | True | `adata_r = adata.copy()` |
| 39 | r | 3 | False | `%%R` |
| 41 | python | 2 | False | `cell_subsets_r = adata_r.obs["cluster_labels_res.0.8"].astype(str).copy()` |
| 43 | r | 13 | True | `%%R -i adata_r,cell_subsets_r,bulk,sc_genes -o musicRes` |
| 44 | python | 4 | False | `# Create the final output matrix` |
| 47 | python | 1 | True | `music_frac` |
| 49 | python | 9 | True | `neutCounts = metadata["Total.neutrophil.count...mm3."].astype(float)` |
| 51 | python | 11 | True | `healty_vs_covid = pd.Series(` |
| 53 | python | 4 | True | `selected_cell = healty_vs_covid.index[np.nanargmin(healty_vs_covid.to_numpy())]` |
