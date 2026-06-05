library
(scater)


rescaled.pancreas <-
 
rescaleBatches
(sce.grun2, sce.muraro2)




set.seed
(
100101
)


rescaled.pancreas <-
 
runPCA
(rescaled.pancreas, 
subset_row=
chosen.genes,


    
exprs_values=
"corrected"
)




rescaled.pancreas <-
 
runTSNE
(rescaled.pancreas, 
dimred=
"PCA"
)


plotTSNE
(rescaled.pancreas, 
colour_by=
"batch"
)
