# Code Index · Spatial domains

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 3 | python | 5 | False | `import scanpy as sc` |
| 5 | python | 2 | True | `adata = sq.datasets.visium_hne_adata()` |
| 6 | python | 1 | True | `sq.pl.spatial_scatter(adata, color="cluster", figsize=(10, 10))` |
| 8 | python | 6 | True | `# nearest neighbor graph` |
| 10 | python | 4 | True | `alpha = 0.2` |
| 12 | python | 1 | True | `sq.pl.spatial_scatter(adata, color=["cluster", "squidpy_domains"], wspace=0.9)` |
| 15 | python | 4 | False | `import numpy as np` |
| 17 | python | 8 | True | `img = np.asarray(` |
| 19 | python | 2 | False | `# requires raw data in X` |
| 22 | python | 5 | False | `# Set coordinates` |
| 24 | python | 11 | True | `# Calculate adjacent matrix` |
| 26 | python | 13 | True | `adata.var_names_make_unique()` |
| 28 | python | 3 | True | `p = 0.5` |
| 30 | python | 2 | True | `# Search for suitable resolution` |
| 32 | python | 2 | False | `model = spg.SpaGCN()` |
| 34 | python | 1 | True | `model.train(adata, adj, res=res)` |
| 36 | python | 1 | False | `y_pred, prob = model.predict()` |
| 38 | python | 2 | False | `adata.obs["spaGCN_domains"] = y_pred` |
| 40 | python | 1 | True | `sq.pl.spatial_scatter(adata, color=["spaGCN_domains", "cluster"])` |
| 43 | python | 1 | True | `adj_2d = spg.calculate_adj_matrix(x=x_array, y=y_array, histology=False)` |
| 45 | python | 5 | False | `refined_pred = spg.refine(` |
| 47 | python | 4 | False | `adata.obs["refined_spaGCN_domains"] = refined_pred` |
| 49 | python | 1 | True | `sq.pl.spatial_scatter(adata, color=["refined_spaGCN_domains", "spaGCN_domains"])` |
