set.seed
(
101010011
)


sce.grun.hsc <-
 
denoisePCA
(sce.grun.hsc, 
technical=
dec.grun.hsc, 
subset.row=
top.grun.hsc)


sce.grun.hsc <-
 
runTSNE
(sce.grun.hsc, 
dimred=
"PCA"
)
