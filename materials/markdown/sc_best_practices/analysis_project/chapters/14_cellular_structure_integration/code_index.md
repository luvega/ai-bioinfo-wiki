# Code Index · Data integration

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 11 | python | 9 | False | `import warnings` |
| 13 | python | 19 | True | `# Python packages` |
| 15 | r | 3 | False | `%%R` |
| 17 | python | 7 | True | `af = ln.Artifact.get(` |
| 19 | python | 2 | False | `label_key = "cell_type"` |
| 21 | python | 1 | True | `adata_raw.obs[batch_key].value_counts()` |
| 23 | python | 3 | True | `keep_batches = ["s1d3", "s2d1", "s3d7"]` |
| 25 | python | 1 | True | `adata.var["feature_types"].value_counts()` |
| 27 | python | 3 | True | `adata = adata[:, adata.var["feature_types"] == "GEX"].copy()` |
| 29 | python | 4 | False | `adata.X = adata.layers["counts"].copy()` |
| 32 | python | 5 | True | `sc.pp.highly_variable_genes(adata)` |
| 34 | python | 6 | True | `adata.uns[batch_key + "_colors"] = [` |
| 38 | python | 4 | True | `sc.pp.highly_variable_genes(` |
| 40 | python | 3 | True | `n_batches = adata.var["highly_variable_nbatches"].value_counts()` |
| 42 | python | 2 | True | `adata_hvg = adata[:, adata.var["highly_variable"]].copy()` |
| 45 | python | 1 | False | `adata_scvi = adata_hvg.copy()` |
| 48 | python | 2 | True | `scvi.model.SCVI.setup_anndata(adata_scvi, layer="counts", batch_key=batch_key)` |
| 52 | python | 2 | True | `model_scvi = scvi.model.SCVI(adata_scvi)` |
| 54 | python | 1 | True | `model_scvi.view_anndata_setup()` |
| 58 | python | 2 | True | `max_epochs_scvi = np.min([round((20000 / adata.n_obs) * 400), 400])` |
| 60 | python | 1 | True | `model_scvi.train()` |
| 64 | python | 1 | False | `adata_scvi.obsm["X_scVI"] = model_scvi.get_latent_representation()` |
| 67 | python | 3 | True | `sc.pp.neighbors(adata_scvi, use_rep="X_scVI")` |
| 69 | python | 1 | True | `sc.pl.umap(adata_scvi, color=[label_key, batch_key], wspace=1)` |
| 73 | python | 7 | True | `# Normally we would need to run scVI first but we have already done that here` |
| 75 | python | 2 | True | `max_epochs_scanvi = int(np.min([10, np.max([2, round(max_epochs_scvi / 3.0)])]))` |
| 77 | python | 5 | True | `adata_scanvi = adata_scvi.copy()` |
| 81 | python | 2 | True | `neighbors_within_batch = 25 if adata_hvg.n_obs > 100000 else 3` |
| 83 | python | 3 | False | `adata_bbknn = adata_hvg.copy()` |
| 85 | python | 4 | True | `bbknn.bbknn(` |
| 87 | python | 2 | True | `sc.tl.umap(adata_bbknn)` |
| 91 | python | 7 | True | `adata_seurat = adata_hvg.copy()` |
| 93 | r | 2 | True | `%%R -i adata_seurat` |
| 95 | r | 3 | True | `%%R -i adata_seurat` |
| 97 | r | 3 | True | `%%R -i batch_key` |
| 99 | r | 3 | True | `%%R` |
| 101 | r | 3 | True | `%%R` |
| 103 | r | 8 | True | `%%R -o integrated_expr` |
| 105 | python | 4 | True | `adata_seurat.X = integrated_expr` |
| 107 | python | 10 | True | `# Reset the batch colours because we deleted them earlier` |
| 111 | python | 9 | True | `metrics_scvi = scib.metrics.metrics_fast(` |
| 113 | python | 1 | True | `metrics_hvg` |
| 115 | python | 26 | True | `# Concatenate metrics results` |
| 117 | python | 1 | True | `metrics.style.background_gradient(cmap="Blues")` |
| 119 | python | 2 | True | `metrics_scaled = (metrics - metrics.min()) / (metrics.max() - metrics.min())` |
| 121 | python | 7 | True | `metrics_scaled["Batch"] = metrics_scaled[` |
| 123 | python | 19 | True | `fig, ax = plt.subplots()` |
| 125 | python | 2 | True | `metrics_scaled["Overall"] = 0.4 * metrics_scaled["Batch"] + 0.6 * metrics_scaled["Bio"]` |
| 127 | python | 1 | True | `metrics_scaled.plot.bar(y="Overall")` |
| 130 | python | 19 | True | `%run ../src/lib.py` |
| 133 | python | 3 | True | `import session_info` |
| 135 | r | 2 | True | `%%R` |
