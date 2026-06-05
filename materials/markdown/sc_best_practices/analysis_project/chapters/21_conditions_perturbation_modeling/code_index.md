# Code Index · Perturbation modeling

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 16 | python | 9 | False | `import warnings` |
| 17 | python | 2 | False | `import pertpy as pt` |
| 19 | python | 1 | False | `adata = pt.dt.kang_2018()` |
| 21 | python | 2 | False | `adata.obs.rename({"label": "condition"}, axis=1, inplace=True)` |
| 23 | python | 1 | True | `adata.obs.cell_type.value_counts()` |
| 25 | python | 1 | False | `ag_rfc = pt.tl.Augur("random_forest_classifier")` |
| 27 | python | 2 | True | `loaded_data = ag_rfc.load(adata, label_col="condition", cell_type_col="cell_type")` |
| 30 | python | 5 | True | `v_adata, v_results = ag_rfc.predict(` |
| 32 | python | 1 | True | `lollipop = ag_rfc.plot_lollipop(v_results)` |
| 35 | python | 2 | False | `sc.pp.neighbors(v_adata)` |
| 36 | python | 1 | True | `sc.pl.umap(adata=v_adata, color=["augur_score", "cell_type", "label"])` |
| 39 | python | 1 | True | `important_features = ag_rfc.plot_important_features(v_results)` |
| 44 | python | 2 | False | `bhattacherjee_adata = pt.dt.bhattacherjee()` |
| 46 | python | 1 | False | `sc.pp.log1p(bhattacherjee_adata)` |
| 47 | python | 13 | True | `# Default mode` |
| 48 | python | 8 | True | `# Permute mode` |
| 50 | python | 14 | True | `# Default mode` |
| 51 | python | 8 | True | `# Permute mode` |
| 53 | python | 1 | True | `scatter = ag_rfc.plot_scatterplot(bhattacherjee_results_15, bhattacherjee_results_48)` |
| 55 | python | 7 | True | `pvals = ag_rfc.predict_differential_prioritization(` |
| 57 | python | 1 | True | `diff = ag_rfc.plot_dp_scatter(pvals)` |
| 64 | python | 2 | False | `import pertpy as pt` |
| 67 | python | 1 | False | `adata = pt.dt.kang_2018()` |
| 69 | python | 2 | False | `sc.pp.log1p(adata)` |
| 71 | python | 2 | False | `adata.obs.rename({"label": "condition"}, axis=1, inplace=True)` |
| 73 | python | 1 | True | `adata.obs.cell_type.value_counts()` |
| 75 | python | 13 | False | `adata_t = adata[` |
| 77 | python | 1 | False | `pt.tl.SCGEN.setup_anndata(adata_t, batch_key="condition", labels_key="cell_type")` |
| 80 | python | 1 | False | `model = pt.tl.SCGEN(adata_t, n_hidden=800, n_latent=100, n_layers=2)` |
| 82 | python | 3 | True | `model.train(` |
| 84 | python | 1 | False | `adata_t.obsm["scgen"] = model.get_latent_representation()` |
| 86 | python | 2 | False | `sc.pp.neighbors(adata_t, use_rep="scgen")` |
| 87 | python | 1 | True | `sc.pl.umap(adata_t, color=["condition", "cell_type"], wspace=0.4, frameon=False)` |
| 91 | python | 6 | True | `pred, delta = model.predict(` |
| 95 | python | 5 | False | `ctrl_adata = adata[` |
| 96 | python | 1 | True | `eval_adata.obs.condition.value_counts()` |
| 98 | python | 2 | True | `sc.tl.pca(eval_adata)` |
| 100 | python | 1 | False | `cd4t_adata = adata[adata.obs["cell_type"] == "CD4 T cells"]` |
| 102 | python | 3 | True | `sc.tl.rank_genes_groups(cd4t_adata, groupby="condition", method="wilcoxon")` |
| 104 | python | 10 | True | `r2_value = model.plot_reg_mean_plot(` |
| 106 | python | 1 | True | `sc.pl.violin(eval_adata, keys="ISG15", groupby="condition")` |
| 114 | python | 3 | False | `import muon as mu` |
| 116 | python | 2 | True | `mdata = pt.dt.papalexi_2021()` |
| 120 | python | 3 | False | `sc.pp.normalize_total(mdata["rna"])` |
| 121 | python | 1 | False | `mu.prot.pp.clr(mdata["adt"])` |
| 124 | python | 1 | False | `sc.pp.pca(mdata["rna"])` |
| 125 | python | 2 | False | `# We calculate neighbors with the cosine distance similarly to the original Seurat implementation` |
| 126 | python | 1 | False | `sc.tl.umap(mdata["rna"])` |
| 127 | python | 1 | True | `sc.pl.umap(mdata["rna"], color=["replicate", "Phase", "perturbation"])` |
| 131 | python | 9 | False | `ms = pt.tl.Mixscape()` |
| 132 | python | 8 | True | `# We create a copy of the object to recalculate the PCA.` |
| 136 | python | 1 | False | `ms.mixscape(adata=mdata["rna"], control="NT", labels="gene_target", layer="X_pert")` |
| 138 | python | 1 | True | `ms.plot_barplot(mdata["rna"], guide_rna_column="guide_ID")` |
| 141 | python | 3 | True | `ms.plot_perturbscore(` |
| 143 | python | 6 | True | `sc.settings.set_figure_params(figsize=(10, 10))` |
| 145 | python | 7 | True | `ms.plot_heatmap(` |
| 147 | python | 8 | True | `mdata["adt"].obs["mixscape_class_global"] = mdata["rna"].obs["mixscape_class_global"]` |
| 150 | python | 1 | False | `ms.lda(adata=mdata["rna"], control="NT", labels="gene_target", layer="X_pert")` |
| 151 | python | 1 | True | `ms.plot_lda(adata=mdata["rna"], control="NT")` |
| 154 | python | 21 | True | `%run ../src/lib.py` |
