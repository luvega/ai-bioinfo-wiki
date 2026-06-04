rescaled <-
 
runTSNE
(rescaled, 
dimred=
"PCA"
)


rescaled
$
batch <-
 
factor
(rescaled
$
batch)


plotTSNE
(rescaled, 
colour_by=
"batch"
)
