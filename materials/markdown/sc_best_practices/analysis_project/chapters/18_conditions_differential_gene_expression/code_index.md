# Code Index · Differential gene expression analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 9 | python | 3 | False | `import warnings` |
| 10 | python | 8 | True | `import decoupler as dc` |
| 14 | python | 4 | True | `adata = ln.Artifact.get(` |
| 16 | python | 1 | True | `adata.obs[:5]` |
| 18 | python | 2 | True | `X = adata.X.data` |
| 19 | python | 1 | False | `adata.layers["counts"] = adata.X.copy()` |
| 21 | python | 2 | True | `print(len(adata[adata.obs["label"] == "ctrl"].obs["replicate"].cat.categories))` |
| 23 | python | 3 | True | `sc.pp.filter_cells(adata, min_genes=200)` |
| 26 | python | 7 | False | `adata.obs["sample"] = pd.Categorical(` |
| 28 | python | 7 | True | `adata_pb = dc.pp.pseudobulk(` |
| 30 | python | 7 | True | `dc.pl.filter_samples(` |
| 32 | python | 1 | False | `dc.pp.filter_samples(adata_pb, min_cells=10,min_counts=1000)` |
| 34 | python | 1 | True | `dc.pl.obsbar(adata=adata_pb, y="cell_type", hue="label", figsize=(6, 3))` |
| 38 | python | 8 | False | `adata_pb.layers['counts'] = adata_pb.X.copy()` |
| 40 | python | 2 | False | `adata_pb.obs["psbulk_counts_log"] = np.log(adata_pb.obs["psbulk_counts"])` |
| 41 | python | 9 | True | `dc.tl.rankby_obsm(adata_pb, key="X_pca")` |
| 43 | python | 2 | True | `adata_pb.obs = adata_pb.obs.sort_index(axis=1)` |
| 47 | python | 2 | True | `adata_mono = adata_pb[adata_pb.obs["cell_type"] == "CD14+ Monocytes"].copy()` |
| 49 | python | 13 | True | `dc.pl.filter_by_expr(` |
| 51 | python | 14 | True | `dc.pp.filter_by_expr(` |
| 53 | python | 1 | False | `pds2 = pt.tl.PyDESeq2(adata=adata_mono,design='~ label')` |
| 54 | python | 1 | True | `pds2.fit()` |
| 55 | python | 5 | True | `res_df = pds2.test_contrasts(pds2.contrast(` |
| 56 | python | 1 | True | `res_df.head(10)` |
| 58 | python | 1 | True | `pds2.plot_volcano(res_df, log2fc_thresh=0)` |
| 60 | python | 7 | True | `pds2.plot_paired(` |
| 64 | python | 1 | False | `pds2 = pt.tl.PyDESeq2(adata=adata_pb, design="~ label")` |
| 65 | python | 1 | True | `pds2.fit()` |
| 66 | python | 6 | True | `res_df = pds2.compare_groups(` |
| 67 | python | 7 | True | `pds2.plot_paired(` |
| 69 | python | 1 | False | `pds2 = pt.tl.PyDESeq2(adata=adata_pb, design="~ cell_type * label")` |
| 70 | python | 1 | True | `pds2.fit()` |
| 71 | python | 9 | True | `interaction_contrast = (` |
| 72 | python | 1 | True | `pds2.plot_volcano(res_df, log2fc_thresh=0)` |
| 74 | python | 1 | True | `pds2.plot_fold_change(res_df[res_df["adj_p_value"] < 0.01].copy(), n_top_vars=15)` |
| 76 | python | 5 | True | `res_df = pds2.compare_groups(adata_pb,` |
| 77 | python | 1 | True | `pds2.plot_multicomparison_fc(res_df, n_top_vars=5, figsize=(12, 1.5))` |
| 81 | python | 5 | True | `%run ../src/lib.py` |
| 83 | python | 40 | True | `%run ../src/lib.py` |
