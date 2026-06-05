# Code Index · Spatial deconvolution

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 10 | python | 7 | True | `import cell2location as c2l` |
| 12 | python | 5 | True | `adata_st = sc.read(` |
| 14 | python | 1 | True | `sq.pl.spatial_scatter(adata_st, library_key="patient_region_id")` |
| 17 | python | 5 | True | `adata_sc = sc.read(` |
| 19 | python | 3 | True | `adata_sc.X = adata_sc.layers["counts"]` |
| 21 | python | 1 | True | `adata_st.var.head()` |
| 23 | python | 2 | False | `adata_st.var["feature_name"] = adata_st.var_names` |
| 25 | python | 1 | True | `adata_st.var.head()` |
| 27 | python | 8 | False | `# find mitochondrial (MT) genes` |
| 29 | python | 5 | False | `shared_features = [` |
| 31 | python | 3 | True | `selected = c2l.utils.filtering.filter_genes(` |
| 34 | python | 2 | False | `adata_sc = adata_sc[:, selected].copy()` |
| 36 | python | 7 | True | `c2l.models.RegressionModel.setup_anndata(` |
| 38 | python | 4 | True | `model = c2l.models.RegressionModel(adata_sc)` |
| 40 | python | 1 | True | `model.plot_history(20)` |
| 42 | python | 4 | True | `model.export_posterior(` |
| 44 | python | 1 | True | `model.plot_QC()` |
| 46 | python | 12 | True | `# export estimated expression in each cluster` |
| 48 | python | 1 | False | `inf_aver.to_csv("inf_aver.csv")` |
| 51 | python | 4 | False | `c2l.models.Cell2location.setup_anndata(` |
| 53 | python | 6 | True | `model = c2l.models.Cell2location(` |
| 55 | python | 3 | True | `model.train(max_epochs=30000, batch_size=None, train_size=1, use_gpu=use_gpu)` |
| 57 | python | 8 | True | `adata_st = model.export_posterior(` |
| 59 | python | 1 | True | `model.plot_QC()` |
| 61 | python | 3 | False | `adata_st.obs[adata_st.uns["mod"]["factor_names"]] = adata_st.obsm[` |
| 62 | python | 15 | True | `# select one slide for visualization` |
| 64 | python | 14 | True | `clust_col = ["Mast", "Cardiomyocyte", "Endothelial"]` |
| 67 | python | 8 | False | `# Compute expected expression per cell type` |
| 69 | python | 9 | True | `slide = c2l.utils.select_slide(adata_st, "control_P1", batch_key="patient_region_id")` |
| 71 | python | 3 | True | `sc.pp.neighbors(adata_st, use_rep="q05_cell_abundance_w_sf")` |
| 73 | python | 12 | True | `sc.tl.umap(adata_st, min_dist=0.3, spread=1)` |
| 74 | python | 1 | True | `sq.pl.spatial_scatter(adata_st, color="region_cluster", library_key="patient_region_id")` |
