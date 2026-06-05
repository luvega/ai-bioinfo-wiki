# Code Index · Quality Control

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 7 | python | 24 | True | `# Single-cell packages` |
| 8 | python | 1 | True | `mdata = mu.read_10x_h5("cellranger_out/filtered_feature_bc_matrix.h5")` |
| 10 | python | 1 | False | `mdata.var_names_make_unique()` |
| 12 | python | 1 | True | `mdata` |
| 15 | python | 1 | True | `mdata.mod["atac"].uns` |
| 18 | python | 1 | False | `atac = mdata.mod["atac"]` |
| 23 | r | 2 | True | `%%R` |
| 25 | r | 3 | False | `%%R` |
| 28 | python | 3 | False | `# Set output paths` |
| 30 | python | 2 | False | `barcodes = list(atac.obs_names)` |
| 32 | r | 3 | True | `%R -i data_mat -o dbl_score sce <- scDblFinder(SingleCellExperiment(list(counts=data_mat)), \` |
| 34 | python | 2 | False | `scDbl_result = pd.DataFrame({"barcodes": barcodes, "scDblFinder_score": dbl_score})` |
| 35 | python | 1 | True | `scDbl_result.head()` |
| 37 | python | 1 | False | `scDbl_result = scDbl_result.set_index("barcodes")` |
| 39 | python | 1 | False | `atac.obs["scDblFinder_score"] = scDbl_result["scDblFinder_score"]` |
| 42 | r | 9 | False | `%%R` |
| 44 | python | 2 | True | `frag_path = atac.uns["files"]["fragments"]` |
| 46 | python | 5 | True | `# Run AMULET` |
| 48 | python | 1 | True | `amulet_result.head()` |
| 51 | python | 2 | False | `atac.obs["AMULET_pVal"] = amulet_result["p.value"]` |
| 52 | python | 2 | True | `# Transform q-values for nicer plotting` |
| 54 | python | 4 | True | `atac.obs.plot(x="scDblFinder_score", y="AMULET_negLog10qVal", kind="scatter")` |
| 60 | python | 14 | False | `# Calculate general qc metrics using scanpy` |
| 63 | python | 3 | True | `# Calculate the nucleosome signal across cells` |
| 65 | python | 6 | True | `sns.histplot(atac.obs, x="nucleosome_signal")` |
| 67 | python | 9 | True | `# Add group labels for above and below the nucleosome signal threshold` |
| 68 | python | 1 | True | `atac.obs["nuc_signal_filter"]  # = atac.obs["nuc_signal_filter"].astype('category')` |
| 70 | python | 8 | True | `# Plot fragment size distribution` |
| 74 | python | 1 | True | `tss = ac.tl.tss_enrichment(mdata, n_tss=3000, random_state=666)` |
| 76 | python | 17 | True | `fig, axs = plt.subplots(1, 2, figsize=(7, 3.5))` |
| 78 | python | 8 | True | `tss_threshold = 1.5` |
| 79 | python | 5 | True | `# Temporarily set different color palette` |
| 81 | python | 1 | True | `atac` |
| 83 | python | 2 | False | `# save after calculation of QC metrics` |
| 86 | python | 2 | False | `# Reload from file if needed` |
| 89 | python | 28 | True | `# Set thresholds for upper boundaries.` |
| 94 | python | 7 | False | `# upper TSS score boundary for plotting` |
| 95 | python | 18 | True | `# Scatter plot & histograms` |
| 98 | python | 24 | True | `fig, axs = plt.subplots(1, 2, figsize=(7, 3.5))` |
| 101 | python | 16 | True | `# Scatter plot total fragment count by number of features` |
| 106 | python | 9 | True | `print(f"Total number of cells: {atac.n_obs}")` |
| 107 | python | 8 | True | `mu.pp.filter_obs(` |
| 110 | python | 1 | False | `mu.pp.filter_var(atac, "n_cells_by_counts", lambda x: x >= 15)` |
| 112 | python | 1 | False | `atac.layers["counts"] = atac.X` |
| 113 | python | 1 | True | `atac` |
| 115 | python | 1 | False | `atac.write_h5ad("output/atac_qc_filtered.h5ad")` |
| 118 | python | 0 | False | `` |
