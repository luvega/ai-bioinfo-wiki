# Code Index · Quality Control

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 7 | python | 18 | True | `import lamindb as ln` |
| 9 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 11 | python | 2 | True | `adata.var_names_make_unique()` |
| 14 | python | 6 | False | `# mitochondrial genes` |
| 16 | python | 4 | True | `sc.pp.calculate_qc_metrics(` |
| 18 | python | 3 | True | `p1 = sns.displot(adata.obs["total_counts"], bins=100, kde=False)` |
| 20 | python | 6 | False | `def is_outlier(adata, metric: str, nmads: int):` |
| 22 | python | 6 | True | `adata.obs["outlier"] = (` |
| 24 | python | 4 | True | `adata.obs["mt_outlier"] = is_outlier(adata, "pct_counts_mt", 3) | (` |
| 26 | python | 4 | True | `print(f"Total number of cells: {adata.n_obs}")` |
| 27 | python | 1 | True | `p1 = sc.pl.scatter(adata, "total_counts", "n_genes_by_counts", color="pct_counts_mt")` |
| 30 | python | 10 | True | `import logging` |
| 31 | r | 2 | False | `%%R` |
| 33 | python | 3 | False | `adata_pp = adata.copy()` |
| 35 | python | 8 | False | `sc.pp.pca(adata_pp)` |
| 37 | python | 1 | False | `del adata_pp` |
| 39 | python | 3 | False | `cells = adata.obs_names` |
| 41 | python | 7 | True | `adata_raw = af.load()` |
| 42 | python | 1 | False | `del adata_raw` |
| 44 | python | 30 | False | `data_csc = data.tocsc()` |
| 46 | r | 39 | False | `%%R -o out ` |
| 48 | python | 9 | False | `with localconverter(ro.default_converter + pandas2ri.converter + numpy2ri.converter):` |
| 49 | python | 3 | False | `adata.layers["counts"] = adata.X.copy()` |
| 51 | python | 5 | True | `print(f"Total number of genes: {adata.n_vars}")` |
| 54 | r | 6 | False | `%%R` |
| 55 | python | 1 | False | `data_mat = adata.X.T` |
| 58 | python | 12 | False | `data_mat = adata.X.T.tocsc()` |
| 60 | r | 14 | False | `%%R -o doublet_score -o doublet_class` |
| 62 | python | 3 | True | `adata.obs["scDblFinder_score"] = doublet_score` |
| 64 | python | 6 | True | `af = ln.Artifact.from_anndata(` |
