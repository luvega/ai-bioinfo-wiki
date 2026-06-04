# Code Index · Spatially variable genes

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 7 | False | `import NaiveDE` |
| 6 | python | 1 | False | `adata = sq.datasets.visium_hne_adata()` |
| 8 | python | 2 | True | `sq.gr.spatial_neighbors(adata)` |
| 10 | python | 1 | True | `adata.uns["moranI"].head()` |
| 13 | python | 1 | True | `sq.pl.spatial_scatter(adata, color=["Nrgn", "Ttr"])` |
| 16 | python | 1 | False | `adata.var_names_make_unique()` |
| 18 | python | 1 | False | `counts = sc.get.obs_df(adata, keys=list(adata.var_names), use_raw=True)` |
| 20 | python | 1 | False | `total_counts = sc.get.obs_df(adata, keys=["total_counts"])` |
| 22 | python | 1 | True | `norm_expr = NaiveDE.stabilize(counts.T).T` |
| 24 | python | 1 | False | `resid_expr = NaiveDE.regress_out(total_counts, norm_expr.T, "np.log(total_counts)").T` |
| 26 | python | 1 | True | `results = SpatialDE.run(adata.obsm["spatial"], resid_expr)` |
| 28 | python | 1 | True | `results.head()` |
| 30 | python | 2 | True | `top10 = results.sort_values("qval").head(10)[["g", "l", "qval"]]` |
| 32 | python | 1 | True | `sq.pl.spatial_scatter(adata, color=list(top10["g"][:3]) + ["cluster"])` |
