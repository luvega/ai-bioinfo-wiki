residuals <-
 
runTSNE
(residuals, 
dimred=
"corrected"
)


residuals
$
batch <-
 
factor
(residuals
$
batch)


plotTSNE
(residuals, 
colour_by=
"batch"
)
