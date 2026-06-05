set.seed
(
00101001101
)




# runTSNE() stores the t-SNE coordinates in the reducedDims


# for re-use across multiple plotReducedDim() calls.


sce.zeisel <-
 
runTSNE
(sce.zeisel, 
dimred=
"PCA"
)


plotReducedDim
(sce.zeisel, 
dimred=
"TSNE"
, 
colour_by=
"level1class"
)
