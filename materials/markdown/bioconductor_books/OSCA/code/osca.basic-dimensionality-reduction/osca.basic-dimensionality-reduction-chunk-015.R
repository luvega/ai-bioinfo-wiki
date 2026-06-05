set.seed
(
1100101001
)


sce.zeisel <-
 
runUMAP
(sce.zeisel, 
dimred=
"PCA"
)


plotReducedDim
(sce.zeisel, 
dimred=
"UMAP"
, 
colour_by=
"level1class"
)
