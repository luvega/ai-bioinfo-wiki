set.seed
(
101010011
)


sce.paul <-
 
denoisePCA
(sce.paul, 
technical=
dec.paul, 
subset.row=
top.paul)


sce.paul <-
 
runTSNE
(sce.paul, 
dimred=
"PCA"
)
