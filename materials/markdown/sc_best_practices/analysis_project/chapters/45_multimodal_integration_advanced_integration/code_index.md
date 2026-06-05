# Code Index · Advanced integration

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 24 | True | `import logging` |
| 6 | r | 6 | True | `%%R` |
| 8 | python | 8 | False | `cite_reference_batches = [` |
| 9 | python | 4 | True | `rna_multiome = sc.read(` |
| 10 | python | 4 | True | `atac_multiome = sc.read(` |
| 11 | python | 4 | True | `rna_cite = sc.read(` |
| 12 | python | 2 | True | `adt_cite = sc.read("/lustre/groups/ml01/workspace/daniel.strobl/neurips_cite_pp.h5ad")` |
| 14 | python | 1 | True | `rna_cite.obs_names` |
| 15 | python | 1 | True | `adt_cite.obs_names` |
| 16 | python | 4 | False | `adt_cite.obs_names = [` |
| 18 | python | 3 | False | `common_idx = list(set(rna_cite.obs_names).intersection(set(adt_cite.obs_names)))` |
| 20 | python | 1 | False | `adt_cite.obs = adt_cite.obs.join(rna_cite.obs[["Samplename", "cell_type"]])` |
| 22 | python | 1 | False | `assert np.sum(rna_multiome.obs_names != atac_multiome.obs_names) == 0` |
| 24 | python | 19 | False | `def update_obs_column(` |
| 25 | python | 4 | False | `rna_multiome = update_obs_column(rna_multiome, "batch", "_rna_multiome")` |
| 27 | python | 18 | False | `# query` |
| 31 | python | 5 | False | `rna_multiome.X = rna_multiome.layers["counts"].copy()` |
| 33 | python | 1 | True | `np.max(adt_cite.X)` |
| 34 | python | 1 | False | `sc.tl.pca(adt_cite, n_comps=100, svd_solver="auto")` |
| 36 | python | 52 | False | `rename_proteins = {` |
| 37 | python | 4 | False | `adt_cite.var_names = [` |
| 39 | python | 5 | False | `p = np.array(adt_cite.var_names)` |
| 41 | python | 4 | False | `rna_vars = [v + "_rna" for v in rna_multiome.var_names]` |
| 43 | python | 5 | False | `adj = pd.DataFrame(mask, index=prot_vars, columns=rna_vars)` |
| 45 | python | 6 | False | `graph = nx.Graph()` |
| 47 | python | 1 | True | `graph.number_of_nodes(), graph.number_of_edges()` |
| 49 | python | 8 | False | `scglue.models.configure_dataset(` |
| 51 | python | 7 | False | `scglue.models.configure_dataset(` |
| 53 | python | 4 | True | `glue = scglue.models.fit_SCGLUE(` |
| 55 | python | 2 | False | `rna_multiome.obsm["X_glue"] = glue.encode_data("rna", rna_multiome)` |
| 56 | python | 4 | False | `adt_cite.obs["modality"] = "ADT"` |
| 58 | python | 2 | False | `sc.pp.neighbors(combined, use_rep="X_glue", metric="cosine")` |
| 59 | python | 3 | True | `sc.pl.umap(` |
| 62 | python | 4 | True | `adata = rna_cite.copy()` |
| 64 | python | 6 | True | `TOTALVI.setup_anndata(` |
| 65 | python | 9 | True | `arches_params = {` |
| 67 | python | 1 | False | `adata.obsm["X_totalvi"] = vae.get_latent_representation()` |
| 68 | python | 2 | False | `sc.pp.neighbors(adata, use_rep="X_totalvi")` |
| 69 | python | 1 | True | `sc.pl.umap(adata, color=["cell_type", "batch"], ncols=1, frameon=False)` |
| 72 | python | 3 | False | `query = rna_cite_query.copy()` |
| 74 | python | 2 | False | `adata.obs["dataset_name"] = "Reference"` |
| 75 | python | 4 | False | `adata.obs["dataset_name_fine"] = "CITE reference"` |
| 77 | python | 7 | True | `vae_q = TOTALVI.load_query_data(` |
| 79 | python | 1 | False | `query.obsm["X_totalvi_scarches"] = vae_q.get_latent_representation(query)` |
| 80 | python | 1 | False | `adata.obsm["X_totalvi_scarches"] = adata.obsm["X_totalvi"]` |
| 81 | python | 2 | True | `full_data = adata.concatenate(query, batch_key="concat_batch")` |
| 82 | python | 2 | False | `sc.pp.neighbors(full_data, use_rep="X_totalvi_scarches")` |
| 83 | python | 6 | True | `sc.pl.umap(` |
| 85 | r | 3 | True | `%%R` |
| 86 | python | 1 | True | `rna_cite_query` |
| 88 | python | 2 | True | `sc.pp.pca(rna_cite_query)` |
| 89 | python | 1 | True | `np.max(rna_cite_query.X)` |
| 91 | python | 6 | False | `adata_ = sc.AnnData(rna_cite_query.X.copy())` |
| 92 | r | 3 | True | `%%R -i adata_` |
| 94 | r | 7 | False | `%%R` |
| 96 | r | 13 | False | `%%R` |
| 98 | r | 5 | False | `%%R` |
| 99 | r | 4 | True | `%%R` |
| 100 | r | 2 | True | `%%R` |
| 102 | python | 2 | False | `rna_cite_ref = rna_cite[rna_cite.obs["batch"] == "s1d1"].copy()` |
| 103 | python | 2 | False | `adt_cite_bridge = adt_cite_query[adt_cite_query.obs["donor"] == "s2d1"].copy()` |
| 105 | python | 4 | False | `adata_ = sc.AnnData(rna_cite_ref.layers["counts"].A.copy())` |
| 106 | r | 3 | True | `%%R -i adata_` |
| 107 | r | 5 | False | `%%R` |
| 109 | python | 4 | False | `adata_ = sc.AnnData(adt_cite_bridge.layers["counts"].A.copy())` |
| 110 | python | 1 | True | `adata_` |
| 111 | r | 2 | False | `%%R -i adata_` |
| 112 | python | 4 | False | `adata_ = sc.AnnData(rna_cite_bridge.layers["counts"].A.copy())` |
| 113 | r | 5 | False | `%%R -i adata_` |
| 114 | r | 4 | False | `%%R` |
| 115 | r | 5 | False | `%%R` |
| 117 | python | 4 | False | `adata_ = sc.AnnData(adt_cite_query_bridge.layers["counts"].A.copy())` |
| 118 | r | 7 | False | `%%R -i adata_` |
| 120 | r | 15 | True | `%%R` |
| 121 | r | 8 | True | `%%R` |
| 122 | r | 11 | False | `%%R` |
| 124 | r | 4 | True | `%%R` |
| 125 | r | 6 | True | `%%R` |
| 128 | python | 6 | True | `rna1 = sc.read(` |
| 129 | python | 6 | True | `rna2 = sc.read(` |
| 131 | python | 5 | True | `adata = mtg.data.organize_multiome_anndatas(` |
| 133 | python | 5 | False | `mtg.model.MultiVAE.setup_anndata(` |
| 135 | python | 10 | False | `model = mtg.model.MultiVAE(` |
| 136 | python | 1 | True | `model.train()` |
| 138 | python | 3 | True | `model.get_latent_representation()` |
| 139 | python | 2 | False | `sc.pp.neighbors(adata, use_rep="latent")` |
| 140 | python | 1 | True | `sc.pl.umap(adata, color=["cell_type", "Modality", "Samplename"], ncols=1, frameon=False)` |
| 142 | python | 8 | False | `query = mtg.data.organize_multiome_anndatas(` |
| 143 | python | 5 | False | `mtg.model.MultiVAE.setup_anndata(` |
| 145 | python | 12 | True | `idx_atac_query = query.obs["Samplename"] == "site2_donor4_multiome"` |
| 146 | python | 2 | False | `query[idx_atac_query, :4000].X = 0` |
| 148 | python | 1 | False | `q_model = mtg.model.MultiVAE.load_query_data(query, model)` |
| 149 | python | 1 | True | `q_model.train(weight_decay=0)` |
| 151 | python | 2 | True | `q_model.get_latent_representation(adata=query)` |
| 153 | python | 8 | False | `adata.obs["reference"] = "reference"` |
| 154 | python | 1 | False | `adata_both = anndata.concat([adata, query])` |
| 155 | python | 2 | False | `sc.pp.neighbors(adata_both, use_rep="latent")` |
| 156 | python | 6 | True | `sc.pl.umap(` |
| 157 | python | 3 | True | `sc.pl.umap(` |
| 158 | python | 3 | True | `sc.pl.umap(` |
| 159 | python | 3 | True | `sc.pl.umap(` |
| 160 | python | 3 | True | `sc.pl.umap(` |
| 163 | r | 2 | True | `%%R` |
