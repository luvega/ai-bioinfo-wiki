# Code Index · GPU-accelerated analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 7 | python | 11 | False | `import cupy as cp` |
| 10 | python | 5 | False | `rmm.reinitialize(` |
| 12 | python | 8 | False | `import warnings` |
| 14 | python | 7 | True | `path = pooch.retrieve(` |
| 16 | python | 1 | False | `rsc.get.anndata_to_GPU(adata)` |
| 18 | python | 8 | True | `adata.var["MT"] = adata.var_names.str.startswith("MT-")` |
| 20 | python | 6 | False | `rsc.pp.normalize_total(adata, target_sum=1e4)` |
| 23 | python | 4 | False | `rsc.tl.pca(adata, n_comps=50)` |
| 26 | python | 1 | True | `sc.pl.umap(adata, color=["leiden"], legend_loc="on data")` |
| 30 | python | 10 | False | `import gc` |
| 32 | python | 8 | True | `# CuPy: what your process has allocated through the active pool.` |
| 37 | python | 12 | True | `from dask.distributed import Client` |
| 38 | python | 20 | False | `from pathlib import Path` |
| 43 | python | 38 | True | `%run ../src/lib.py` |
