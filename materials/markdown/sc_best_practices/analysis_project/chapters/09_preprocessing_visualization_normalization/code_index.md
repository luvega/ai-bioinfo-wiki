# Code Index · Normalization

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 27 | True | `import logging` |
| 5 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 7 | python | 1 | True | `p1 = sns.histplot(adata.obs["total_counts"], bins=100, kde=False)` |
| 9 | python | 3 | False | `scales_counts = sc.pp.normalize_total(adata, target_sum=None, inplace=False)` |
| 11 | python | 6 | True | `fig, axes = plt.subplots(1, 2, figsize=(10, 5))` |
| 13 | python | 1 | False | `from scipy.sparse import csr_matrix` |
| 14 | r | 3 | False | `%%R` |
| 16 | python | 9 | False | `# Preliminary clustering for differentiated normalisation` |
| 18 | python | 17 | False | `# IMPORTANT: scran's computeSumFactors requires raw counts (not normalized or log-transformed).` |
| 20 | python | 1 | False | `del adata_pp` |
| 22 | r | 11 | False | `%%R -o size_factors` |
| 24 | python | 4 | False | `adata.obs["size_factors"] = size_factors` |
| 25 | python | 8 | True | `fig, axes = plt.subplots(1, 2, figsize=(10, 5))` |
| 27 | python | 2 | False | `analytic_pearson = sc.experimental.pp.normalize_pearson_residuals(adata, inplace=False)` |
| 28 | python | 8 | True | `fig, axes = plt.subplots(1, 2, figsize=(10, 5))` |
| 31 | python | 6 | True | `af = ln.Artifact.from_anndata(` |
