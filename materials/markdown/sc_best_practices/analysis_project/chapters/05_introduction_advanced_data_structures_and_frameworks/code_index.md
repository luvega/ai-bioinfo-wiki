# Code Index · Multimodal and spatial data structures

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 10 | python | 5 | False | `import os` |
| 13 | python | 5 | True | `import lamindb as ln` |
| 15 | python | 4 | True | `adata = ln.Artifact.get(` |
| 16 | python | 4 | True | `adata2 = ln.Artifact.get(` |
| 18 | python | 2 | True | `mdata = md.MuData({"A": adata, "B": adata2})` |
| 22 | python | 1 | True | `list(mdata.mod.keys())` |
| 24 | python | 2 | True | `print(mdata.mod["A"])` |
| 26 | python | 1 | True | `mdata.var_names` |
| 29 | python | 4 | True | `adata2.var_names = ["var_ad2_" + e.split("_")[1] for e in adata2.var_names]` |
| 31 | python | 2 | False | `# Add some unstructured data to the original object` |
| 32 | python | 2 | True | `# Access modality A via the .mod attribute` |
| 35 | python | 1 | True | `mdata.obsm["A"]` |
| 36 | python | 1 | True | `np.sum(mdata.obsm["A"]) == np.sum(mdata.obsm["B"]) == 1000` |
| 38 | python | 1 | True | `mdata.varm["A"]` |
| 41 | python | 3 | True | `view = mdata[:100, :1000]` |
| 43 | python | 2 | True | `mdata_sub = view.copy()` |
| 48 | python | 3 | True | `mdata.write("my_mudata.h5mu")` |
| 50 | python | 1 | True | `mdata_r["A"].isbacked` |
| 52 | python | 3 | True | `mdata_sub = mdata_r.copy("mdata_sub.h5mu")` |
| 55 | python | 2 | True | `x = np.hstack([mdata.mod["A"].X, mdata.mod["B"].X])` |
| 57 | python | 10 | False | `def simple_pca(mdata):` |
| 58 | python | 2 | True | `simple_pca(mdata)` |
| 71 | python | 17 | True | `import muon as mu` |
| 73 | python | 1 | False | `atac = mdata.mod["atac"]` |
| 75 | python | 3 | False | `import scanpy as sc` |
| 76 | python | 1 | True | `sc.pl.violin(atac, ["total_counts", "n_genes_by_counts"], jitter=0.4, multi_panel=True)` |
| 78 | python | 4 | False | `mu.pp.filter_var(atac, "n_cells_by_counts", lambda x: x >= 10)` |
| 80 | python | 7 | False | `mu.pp.filter_obs(atac, "n_genes_by_counts", lambda x: (x >= 2000) & (x <= 15000))` |
| 81 | python | 1 | True | `sc.pl.violin(atac, ["n_genes_by_counts", "total_counts"], jitter=0.4, multi_panel=True)` |
| 83 | python | 1 | True | `mu.pl.histogram(atac, ["n_genes_by_counts", "total_counts"])` |
| 85 | python | 1 | False | `from muon import atac as ac` |
| 86 | python | 8 | True | `# Perform rudimentary quality control with muon's ATAC module` |
| 87 | python | 6 | False | `# Save original counts, normalize data and select highly variable genes with scanpy` |
| 89 | python | 5 | True | `ac.tl.lsi(atac)` |
| 91 | python | 1 | True | `ac.pl.umap(atac, color=["KLF4"], average="peak_type")` |
| 96 | python | 2 | False | `import spatialdata as sd` |
| 98 | python | 4 | False | `# Suppress ome-zarr's "no parent found" log message which indicates a minor structural inconsistency in the Zarr store that does not affect data loading.` |
| 99 | python | 4 | True | `sdata = ln.Artifact.get(` |
| 100 | python | 2 | False | `# Reset ome-zarr logging level back to default` |
| 103 | python | 1 | True | `sdata["raw_image"]` |
| 105 | python | 1 | True | `sd.get_pyramid_levels(sdata["raw_image"], n=1)` |
| 107 | python | 1 | True | `sd.models.get_axes_names(sdata["raw_image"])` |
| 109 | python | 1 | True | `sd.models.get_channel_names(sdata["raw_image"])` |
| 111 | python | 1 | True | `sdata.pl.render_images("raw_image", cmap="gray").pl.show()` |
| 113 | python | 1 | True | `sdata["transcripts"]` |
| 115 | python | 1 | True | `sdata["transcripts"].compute()` |
| 117 | python | 4 | True | `sdata.pl.render_points("transcripts").pl.show()` |
| 119 | python | 1 | True | `sdata["nucleus_boundaries"]` |
| 120 | python | 1 | True | `sdata.pl.render_shapes("nucleus_boundaries").pl.show()` |
| 122 | python | 1 | True | `sdata["table"]` |
| 124 | python | 2 | True | `sdata.pl.render_shapes("nucleus_boundaries", color="Hal").pl.show()` |
| 130 | python | 1 | False | `import squidpy as sq` |
| 132 | python | 4 | True | `sdata = ln.Artifact.get(` |
| 135 | python | 1 | False | `sq.gr.spatial_neighbors(sdata["table"])` |
| 137 | python | 4 | True | `%%time` |
| 139 | python | 2 | True | `sq.gr.nhood_enrichment(sdata["table"], cluster_key="leiden")` |
| 141 | python | 2 | True | `%%time` |
| 143 | python | 19 | True | `%run ../src/lib.py` |
| 145 | python | 52 | True | `%run ../src/lib.py` |
