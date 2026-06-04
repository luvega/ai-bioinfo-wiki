set.seed
(
101010011
)


sce.nest <-
 
denoisePCA
(sce.nest, 
technical=
dec.nest, 
subset.row=
top.nest)


sce.nest <-
 
runTSNE
(sce.nest, 
dimred=
"PCA"
)
