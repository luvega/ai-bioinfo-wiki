# Code Index · Paired integration

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 26 | True | `import logging` |
| 6 | r | 5 | True | `%%R` |
| 9 | python | 4 | True | `adt = sc.read(` |
| 10 | python | 4 | True | `rna = sc.read(` |
| 12 | python | 3 | False | `batches_to_keep = ["s1d1", "s1d2", "s1d3"]` |
| 14 | python | 1 | True | `adt.obs_names` |
| 15 | python | 1 | True | `rna.obs_names` |
| 16 | python | 4 | False | `adt.obs_names = [` |
| 17 | python | 3 | False | `common_idx = list(set(rna.obs_names).intersection(set(adt.obs_names)))` |
| 19 | python | 1 | False | `adt.var_names = ["PROT_" + name for name in adt.var_names]` |
| 21 | python | 2 | True | `mdata = mu.MuData({"rna": rna, "adt": adt})` |
| 23 | python | 2 | False | `mdata.obs["batch"] = rna.obs["batch"].copy()` |
| 26 | python | 5 | False | `adata_ = ad.AnnData(adt.X.copy())` |
| 27 | r | 6 | True | `%%R -i adata_` |
| 29 | python | 5 | False | `adata_ = ad.AnnData(rna.X.copy())` |
| 30 | r | 3 | True | `%%R -i adata_` |
| 32 | r | 3 | False | `%%R` |
| 33 | r | 2 | False | `%%R` |
| 35 | r | 6 | False | `%%R` |
| 36 | r | 3 | True | `%%R` |
| 38 | r | 8 | False | `%%R` |
| 40 | r | 3 | False | `%%R` |
| 41 | r | 2 | True | `%%R` |
| 43 | r | 2 | False | `%%R` |
| 45 | r | 2 | False | `%%R -o spca` |
| 46 | python | 1 | False | `mdata.obsm["X_spca"] = spca` |
| 48 | r | 2 | False | `%%R -o wnn` |
| 50 | python | 1 | True | `wnn[:5]` |
| 51 | python | 3 | True | `wnn["i"] = wnn["i"] - 1` |
| 53 | python | 3 | False | `mdata.obsp["wnn_connectivities"] = scipy.sparse.coo_matrix(` |
| 55 | python | 7 | False | `# we won't actually need the neighbors` |
| 56 | python | 1 | False | `mdata.obsm["X_umap_wnn"] = mdata.obsm["X_umap"].copy()` |
| 58 | python | 3 | True | `mu.pl.embedding(` |
| 60 | python | 4 | False | `scib_anndata = sc.AnnData(mdata.obsm["X_spca"]).copy()` |
| 61 | python | 13 | True | `metrics_wnn = scib.metrics.metrics(` |
| 65 | python | 1 | True | `mu.tl.mofa(mdata, groups_label="batch", gpu_mode=True)` |
| 67 | python | 3 | False | `sc.pp.neighbors(mdata, use_rep="X_mofa")` |
| 69 | python | 3 | True | `mu.pl.embedding(` |
| 71 | python | 4 | False | `scib_anndata = sc.AnnData(mdata.obsm["X_mofa"]).copy()` |
| 72 | python | 13 | True | `metrics_mofa = scib.metrics.metrics(` |
| 75 | python | 2 | False | `adata = mdata["rna"].copy()` |
| 77 | python | 6 | True | `scvi.model.TOTALVI.setup_anndata(` |
| 79 | python | 1 | True | `vae = scvi.model.TOTALVI(adata)` |
| 81 | python | 1 | True | `vae.train()` |
| 83 | python | 1 | False | `mdata.obsm["X_totalVI"] = vae.get_latent_representation()` |
| 84 | python | 2 | False | `sc.pp.neighbors(mdata, use_rep="X_totalVI")` |
| 85 | python | 1 | False | `mdata.obsm["X_umap_totalVI"] = mdata.obsm["X_umap"].copy()` |
| 87 | python | 3 | True | `mu.pl.embedding(` |
| 89 | python | 4 | False | `scib_anndata = sc.AnnData(mdata.obsm["X_totalVI"]).copy()` |
| 90 | python | 13 | True | `metrics_totalvi = scib.metrics.metrics(` |
| 93 | python | 4 | True | `metrics = pd.DataFrame([metrics_wnn[0], metrics_mofa[0], metrics_totalvi[0]])` |
| 94 | python | 12 | True | `metrics["overall"] = (` |
| 95 | python | 2 | True | `sns.scatterplot(data=metrics)` |
| 99 | python | 4 | True | `atac = sc.read(` |
| 100 | python | 4 | True | `rna = sc.read(` |
| 102 | python | 3 | False | `batches_to_keep = ["s1d1", "s1d2", "s1d3"]` |
| 103 | python | 2 | True | `mdata_multiome = mu.MuData({"rna": rna, "atac": atac})` |
| 104 | python | 2 | False | `mdata_multiome.obs["batch"] = mdata_multiome["rna"].obs["batch"].copy()` |
| 107 | python | 2 | False | `n_genes = len(rna.var_names)` |
| 109 | python | 4 | True | `adata_paired = ad.concat([rna.copy().T, atac.copy().T]).T` |
| 110 | python | 1 | False | `adata_mvi = scvi.data.organize_multiome_anndatas(adata_paired)` |
| 112 | python | 6 | False | `scvi.model.MULTIVI.setup_anndata(` |
| 114 | python | 5 | False | `mvi = scvi.model.MULTIVI(` |
| 116 | python | 1 | True | `mvi.train()` |
| 118 | python | 1 | False | `mdata_multiome.obsm["X_multiVI"] = mvi.get_latent_representation()` |
| 119 | python | 2 | False | `sc.pp.neighbors(mdata_multiome, use_rep="X_multiVI")` |
| 120 | python | 1 | False | `mdata_multiome.obsm["X_umap_multiVI"] = mdata_multiome.obsm["X_umap"].copy()` |
| 121 | python | 7 | True | `mu.pl.embedding(` |
| 123 | r | 2 | True | `%%R` |
