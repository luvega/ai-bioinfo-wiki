# Code Index · Fundamental data structures and frameworks

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 15 | python | 3 | False | `import warnings` |
| 16 | python | 7 | True | `import anndata as ad` |
| 18 | python | 5 | True | `counts = csr_matrix(` |
| 20 | python | 1 | True | `adata.X` |
| 22 | python | 3 | True | `adata.obs_names = [f"Cell_{i:d}" for i in range(adata.n_obs)]` |
| 26 | python | 3 | True | `ct = np.random.default_rng().choice(["B", "T", "Monocyte"], size=(adata.n_obs,))` |
| 28 | python | 1 | True | `adata` |
| 31 | python | 2 | True | `bdata = adata[adata.obs.cell_type == "B"]` |
| 35 | python | 3 | True | `adata.obsm["X_umap"] = np.random.default_rng().normal(0, 1, size=(adata.n_obs, 2))` |
| 37 | python | 1 | True | `adata` |
| 41 | python | 2 | True | `adata.uns["random"] = [1, 2, 3]` |
| 44 | python | 2 | True | `adata.layers["log_transformed"] = np.log1p(adata.X)` |
| 46 | python | 1 | True | `(adata.X != adata.layers["log_transformed"]).nnz == 0` |
| 49 | python | 1 | True | `adata.to_df(layer="log_transformed")` |
| 52 | python | 1 | False | `adata.write("my_results.h5ad", compression="gzip")` |
| 54 | python | 2 | True | `adata_new = ad.read_h5ad("my_results.h5ad")` |
| 58 | python | 13 | False | `obs_meta = pd.DataFrame(` |
| 60 | python | 2 | True | `adata = ad.AnnData(adata.X, obs=obs_meta, var=adata.var)` |
| 63 | python | 1 | True | `adata` |
| 65 | python | 2 | True | `adata_view = adata[:5, ["Gene_1", "Gene_3"]]` |
| 67 | python | 1 | True | `adata` |
| 69 | python | 2 | True | `adata_subset = adata[:5, ["Gene_1", "Gene_3"]].copy()` |
| 71 | python | 3 | True | `print(adata[:3, "Gene_1"].X.toarray().tolist())` |
| 73 | python | 2 | True | `adata_subset = adata[:3, ["Gene_1", "Gene_2"]]` |
| 74 | python | 1 | False | `adata_subset.obs["foo"] = range(3)` |
| 76 | python | 1 | True | `adata_subset` |
| 78 | python | 1 | True | `adata[adata.obs.time_yr.isin([2, 4])].obs.head()` |
| 81 | python | 1 | False | `adata = ad.read_h5ad("my_results.h5ad", backed="r")` |
| 82 | python | 1 | True | `adata.isbacked` |
| 84 | python | 1 | True | `adata.filename` |
| 86 | python | 1 | False | `adata.file.close()` |
| 99 | python | 4 | True | `import scanpy as sc` |
| 101 | python | 4 | True | `adata = ln.Artifact.get(` |
| 103 | python | 1 | True | `adata.var` |
| 105 | python | 1 | True | `sc.pl.highest_expr_genes(adata, n_top=20)` |
| 107 | python | 2 | False | `sc.pp.filter_cells(adata, min_genes=200)` |
| 109 | python | 1 | False | `sc.tl.pca(adata, svd_solver="arpack")` |
| 111 | python | 1 | True | `sc.pl.pca(adata, color="CST3")` |
| 113 | python | 1 | False | `sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)` |
| 115 | python | 1 | False | `sc.tl.umap(adata)` |
| 116 | python | 1 | True | `sc.pl.umap(adata, color=["CST3", "NKG7", "PPBP"])` |
| 119 | python | 19 | True | `%run ../src/lib.py` |
| 121 | python | 38 | True | `%run ../src/lib.py` |
