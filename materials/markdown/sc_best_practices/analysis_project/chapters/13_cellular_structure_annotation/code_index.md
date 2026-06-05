# Code Index · Annotation

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 12 | False | `# filter out some deprecation and performance warnings that do not affect our code` |
| 6 | python | 19 | True | `import shutil` |
| 9 | python | 1 | False | `sc.set_figure_params(figsize=(5, 5))` |
| 12 | python | 2 | True | `af = ln.Artifact.get(key="cellular_structure/s4d8_clustered.h5ad", is_latest=True)` |
| 19 | python | 81 | False | `# keys: cell types or populations, values: lists of marker genes` |
| 22 | python | 7 | False | `marker_genes_in_data = {}` |
| 25 | python | 2 | False | `adata.layers["counts"] = adata.X` |
| 27 | python | 1 | False | `adata.var["highly_variable"] = adata.var["highly_deviant"]` |
| 29 | python | 1 | False | `sc.tl.pca(adata, n_comps=50, use_highly_variable=True)` |
| 31 | python | 1 | False | `sc.pp.neighbors(adata)` |
| 33 | python | 1 | False | `sc.tl.umap(adata)` |
| 36 | python | 7 | False | `B_plasma_cts = [` |
| 38 | python | 12 | True | `for ct in B_plasma_cts:` |
| 42 | python | 1 | False | `sc.tl.leiden(adata, resolution=1, key_added="leiden_1")` |
| 43 | python | 1 | True | `sc.pl.umap(adata, color="leiden_1")` |
| 45 | python | 1 | False | `sc.tl.leiden(adata, resolution=2, key_added="leiden_2")` |
| 47 | python | 1 | True | `sc.pl.umap(adata, color="leiden_2", legend_loc="on data")` |
| 49 | python | 1 | True | `sc.pl.umap(adata, color="leiden_1", legend_loc="on data")` |
| 51 | python | 5 | False | `B_plasma_markers = {` |
| 52 | python | 6 | True | `sc.pl.dotplot(` |
| 54 | python | 4 | False | `cl_annotation = {` |
| 57 | python | 1 | False | `adata.obs["manual_celltype_annotation"] = adata.obs.leiden_1.map(cl_annotation)` |
| 58 | python | 1 | True | `sc.pl.umap(adata, color=["manual_celltype_annotation"])` |
| 62 | python | 3 | False | `sc.tl.rank_genes_groups(` |
| 64 | python | 8 | True | `sc.tl.dendrogram(` |
| 66 | python | 7 | False | `sc.tl.filter_rank_genes_groups(` |
| 68 | python | 7 | True | `sc.pl.rank_genes_groups_dotplot(` |
| 70 | python | 8 | True | `sc.pl.umap(` |
| 74 | python | 1 | False | `cl_annotation["8"] = "NK cells (?)"` |
| 75 | python | 1 | False | `adata.obs["manual_celltype_annotation"] = adata.obs.leiden_1.map(cl_annotation)` |
| 87 | python | 8 | False | `adata_celltypist = adata.copy()  # make a copy of our adata` |
| 89 | python | 3 | True | `models.download_models(` |
| 91 | python | 2 | False | `model_low = models.Model.load(model="Immune_All_Low.pkl")` |
| 93 | python | 1 | True | `model_high.cell_types` |
| 94 | python | 1 | True | `model_low.cell_types` |
| 97 | python | 3 | True | `predictions_high = celltypist.annotate(` |
| 99 | python | 1 | False | `predictions_high_adata = predictions_high.to_adata()` |
| 101 | python | 6 | False | `adata.obs["celltypist_cell_label_coarse"] = predictions_high_adata.obs.loc[` |
| 103 | python | 3 | True | `predictions_low = celltypist.annotate(` |
| 104 | python | 1 | False | `predictions_low_adata = predictions_low.to_adata()` |
| 105 | python | 6 | False | `adata.obs["celltypist_cell_label_fine"] = predictions_low_adata.obs.loc[` |
| 107 | python | 7 | True | `sc.pl.umap(` |
| 108 | python | 7 | True | `sc.pl.umap(` |
| 110 | python | 6 | True | `sc.tl.dendrogram(` |
| 119 | python | 5 | False | `adata_to_map = adata.copy()` |
| 121 | python | 4 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 123 | python | 2 | False | `adata_to_map.var["gene_names"] = adata_to_map.var.index` |
| 124 | python | 2 | False | `reference_model_features["gene_names"] = reference_model_features.index` |
| 126 | python | 1 | True | `print("Total number of genes needed for mapping:", reference_model_features.shape[0])` |
| 127 | python | 4 | True | `print(` |
| 129 | python | 5 | False | `missing_genes = [` |
| 130 | python | 6 | False | `missing_gene_adata = sc.AnnData(` |
| 132 | python | 2 | False | `if "PCs" in adata_to_map.varm.keys():` |
| 133 | python | 7 | False | `adata_to_map_augmented = sc.concat(` |
| 135 | python | 3 | False | `adata_to_map_augmented = adata_to_map_augmented[` |
| 137 | python | 1 | True | `bool((adata_to_map_augmented.var.index == reference_model_features.index).all())` |
| 139 | python | 2 | False | `adata_to_map_augmented.var["gene_ids"] = adata_to_map_augmented.var.index` |
| 141 | python | 1 | True | `adata_to_map_augmented.obs.batch.unique()` |
| 143 | python | 3 | False | `sys.modules["pandas.core.indexes.numeric"] = pandas_indexes_base` |
| 145 | python | 9 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 146 | python | 5 | True | `scarches_model = sca.models.SCVI.load_query_data(` |
| 148 | python | 1 | True | `scarches_model.train(max_epochs=500, plan_kwargs={"weight_decay": 0.0})` |
| 150 | python | 1 | False | `adata.obsm["X_scVI"] = scarches_model.get_latent_representation()` |
| 152 | python | 2 | False | `sc.pp.neighbors(adata, use_rep="X_scVI")` |
| 154 | python | 9 | True | `sc.pl.umap(` |
| 156 | python | 4 | True | `af = ln.Artifact.get(` |
| 158 | python | 1 | False | `ref_emb.obs["reference_or_query"] = "reference"` |
| 160 | python | 1 | True | `ref_emb` |
| 163 | python | 1 | False | `adata_emb = sc.AnnData(X=adata.obsm["X_scVI"], obs=adata.obs)` |
| 164 | python | 1 | False | `adata_emb.obs["reference_or_query"] = "query"` |
| 166 | python | 1 | False | `adata_emb.obs["cell_type"] = None` |
| 167 | python | 7 | False | `emb_ref_query = sc.concat(` |
| 169 | python | 2 | False | `sc.pp.neighbors(emb_ref_query)` |
| 171 | python | 6 | True | `sc.pl.umap(` |
| 175 | python | 1 | False | `sc.set_figure_params(figsize=(8, 8))` |
| 176 | python | 9 | True | `sc.pl.umap(` |
| 180 | python | 5 | True | `knn_transformer = sca.utils.knn.weighted_knn_trainer(` |
| 182 | python | 7 | True | `labels, uncert = sca.utils.knn.weighted_knn_transfer(` |
| 184 | python | 2 | False | `adata_emb.obs["transf_cell_type"] = labels.loc[adata_emb.obs.index, "cell_type"]` |
| 186 | python | 9 | False | `adata.obs.loc[adata_emb.obs.index, "transf_cell_type"] = adata_emb.obs[` |
| 189 | python | 1 | False | `sc.set_figure_params(figsize=(5, 5))` |
| 190 | python | 1 | True | `sc.pl.umap(adata, color="transf_cell_type", frameon=False)` |
| 192 | python | 1 | True | `sc.pl.umap(adata, color="transf_cell_type_unc", frameon=False)` |
| 194 | python | 15 | True | `fig, ax = plt.subplots(figsize=(8, 3))` |
| 197 | python | 4 | False | `adata.obs["transf_cell_type_certain"] = adata.obs.transf_cell_type.tolist()` |
| 199 | python | 1 | True | `sc.pl.umap(adata, color="transf_cell_type_certain", frameon=False)` |
| 201 | python | 1 | True | `sc.pl.umap(adata, color="transf_cell_type_certain", groups="Unknown")` |
| 204 | python | 9 | False | `cell_types_to_check = [` |
| 206 | python | 8 | True | `sc.pl.dotplot(` |
| 209 | python | 3 | True | `sc.pl.umap(` |
| 213 | python | 13 | True | `# formatting the 'names' column as string, to prevent problems with saving to h5ad format` |
