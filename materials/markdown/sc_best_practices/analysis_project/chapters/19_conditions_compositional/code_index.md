# Code Index · Compositional analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 7 | python | 13 | False | `import warnings` |
| 8 | python | 2 | False | `adata = pt.dt.haber_2017_regions()` |
| 9 | python | 1 | True | `adata.obs` |
| 13 | python | 9 | True | `healthy_tissue = [2000, 2000, 2000]` |
| 14 | python | 16 | True | `plot_data_global = example_data_global.melt(` |
| 16 | python | 12 | True | `rng = np.random.Generator(1234)` |
| 17 | python | 15 | True | `plot_data_sample = example_data_sample.melt(` |
| 24 | python | 10 | True | `sccoda_model = pt.tl.Sccoda()` |
| 26 | python | 9 | True | `sccoda_model.plot_boxplots(` |
| 28 | python | 4 | True | `sccoda_model.plot_stacked_barplot(` |
| 30 | python | 7 | True | `sccoda_data = sccoda_model.prepare(` |
| 31 | python | 1 | True | `sccoda_data["coda"].varm["effect_df_condition[T.Salmonella]"]` |
| 33 | python | 1 | True | `sccoda_data` |
| 35 | python | 1 | False | `sccoda_model.set_fdr(sccoda_data, 0.2)` |
| 37 | python | 1 | True | `sccoda_model.credible_effects(sccoda_data, modality_key="coda")` |
| 39 | python | 2 | True | `sccoda_model.plot_effects_barplot(sccoda_data, "coda", "condition")` |
| 43 | python | 4 | True | `import schist` |
| 45 | python | 6 | True | `# use logcounts to calculate PCA and neighbors` |
| 47 | python | 2 | True | `schist.inference.nested_model(adata, samples=100, random_seed=5678)` |
| 49 | python | 3 | True | `sc.pl.umap(` |
| 51 | python | 11 | True | `tasccoda_model = pt.tl.Tasccoda()` |
| 52 | python | 1 | True | `tasccoda_model.plot_draw_tree(tasccoda_data)` |
| 54 | python | 8 | True | `tasccoda_model.prepare(` |
| 55 | python | 3 | True | `tasccoda_model.run_nuts(` |
| 56 | python | 1 | True | `tasccoda_model.summary(tasccoda_data, modality_key="coda")` |
| 58 | python | 8 | True | `tasccoda_model.plot_draw_effects(` |
| 59 | python | 8 | True | `tasccoda_model.plot_draw_effects(` |
| 60 | python | 8 | True | `tasccoda_model.plot_draw_effects(` |
| 62 | python | 3 | True | `tasccoda_model.plot_effects_barplot(` |
| 64 | python | 14 | True | `kwargs = {"ncols": 3, "wspace": 0.25, "vcenter": 0, "vmax": 1.5, "vmin": -1.5}` |
| 70 | python | 4 | True | `milo = pt.tl.Milo()` |
| 71 | python | 12 | True | `# use logcounts to calculate PCA and neighbors` |
| 72 | python | 1 | True | `sc.pl.umap(adata, color=["condition", "batch", "cell_label"], ncols=3, wspace=0.25)` |
| 74 | python | 8 | False | `import scvi` |
| 75 | python | 2 | False | `sc.pp.neighbors(adata, use_rep="X_scVI")` |
| 76 | python | 1 | True | `sc.pl.umap(adata, color=["condition", "batch", "cell_label"], ncols=3, wspace=0.25)` |
| 80 | python | 1 | False | `milo.make_nhoods(mdata, prop=0.1)` |
| 82 | python | 1 | True | `adata.obsm["nhoods"]` |
| 84 | python | 4 | True | `nhood_size = adata.obsm["nhoods"].toarray().sum(0)` |
| 85 | python | 1 | True | `np.median(nhood_size)` |
| 87 | python | 2 | False | `sc.pp.neighbors(adata, n_neighbors=30, use_rep="X_scVI", key_added="milo")` |
| 89 | python | 4 | True | `nhood_size = adata.obsm["nhoods"].toarray().sum(0)` |
| 92 | python | 1 | True | `milo.count_nhoods(mdata, sample_col="batch")` |
| 94 | python | 1 | True | `mdata["milo"]` |
| 96 | python | 4 | True | `mean_n_cells = mdata["milo"].X.toarray().mean(0)` |
| 99 | python | 5 | True | `milo.da_nhoods(` |
| 102 | python | 53 | True | `def plot_milo_diagnostics(mdata):` |
| 105 | python | 4 | True | `milo.build_nhood_graph(mdata)` |
| 107 | python | 6 | False | `milo.annotate_nhoods(mdata, anno_col="cell_label")` |
| 108 | python | 2 | True | `milo.plot_da_beeswarm(mdata)` |
| 111 | python | 16 | False | `## Turn into continuous variable` |
| 112 | python | 1 | True | `plot_milo_diagnostics(mdata)` |
| 113 | python | 2 | True | `with matplotlib.rc_context({"figure.figsize": [10, 10]}):` |
| 114 | python | 2 | True | `milo.plot_da_beeswarm(mdata)` |
| 116 | python | 23 | True | `entero_ixs = mdata["milo"].var_names[` |
| 118 | python | 14 | True | `## Compute average Retnlb expression per neighbourhood` |
| 120 | python | 12 | False | `## Make dummy confounder for the sake of this example` |
| 121 | python | 1 | True | `mdata["milo"].var` |
| 123 | python | 20 | True | `%run ../src/lib.py` |
