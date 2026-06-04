set.seed
(
1111001
)


uncorrected <-
 
runTSNE
(uncorrected, 
dimred=
"PCA"
)


plotTSNE
(uncorrected, 
colour_by=
"batch"
)
