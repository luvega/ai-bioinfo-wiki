u <-
 
uwot
::
umap
(
t
(
logcounts
(sce)), 
n_neighbors =
 
2
)


reducedDim
(sce, 
"UMAP_uwot"
) <-
 
u


reducedDims
(sce) 
# Now stored in the object.
