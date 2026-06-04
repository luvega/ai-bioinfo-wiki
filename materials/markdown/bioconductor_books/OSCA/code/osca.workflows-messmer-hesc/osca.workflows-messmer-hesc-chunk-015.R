set.seed
(
1101001
)


sce.mess <-
 
runPCA
(sce.mess, 
subset_row =
 top.hvgs, 
exprs_values =
 
"corrected"
)


sce.mess <-
 
runTSNE
(sce.mess, 
dimred =
 
"PCA"
, 
perplexity =
 
40
)
