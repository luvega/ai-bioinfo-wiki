# Code Index · Interoperability

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 10 | True | `import tempfile` |
| 14 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 16 | python | 4 | False | `temp_dir = tempfile.TemporaryDirectory()` |
| 24 | python | 1 | False | `h5ad_file = str(h5ad_file)` |
| 26 | r | 9 | True | `%%R -i h5ad_file` |
| 41 | r | 3 | True | `%%R` |
| 42 | r | 3 | True | `%%R` |
| 44 | r | 5 | True | `%%R` |
| 48 | python | 7 | True | `counts_mat = adata.layers["counts"].T.toarray()` |
| 50 | r | 3 | False | `%%R -i counts_mat -o magic_cpm` |
| 51 | python | 2 | True | `# Python code accessing the results` |
| 53 | python | 2 | False | `with rpy2.robjects.conversion.localconverter(anndata2ri.converter):` |
| 55 | r | 3 | True | `%%R -i r_adata` |
| 59 | r | 5 | True | `%%R` |
| 69 | python | 6 | True | `# Read file` |
| 72 | python | 11 | True | `import shutil` |
| 73 | r | 6 | True | `%%R` |
| 75 | r | 6 | True | `%%R` |
| 80 | python | 3 | True | `import session_info` |
| 82 | r | 2 | True | `%%R` |
