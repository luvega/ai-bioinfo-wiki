sce
.416
b <-
 
runPCA
(sce
.416
b, 
ncomponents=
10
, 
subset_row=
chosen.hvgs,


    
exprs_values=
"corrected"
, 
BSPARAM=
BiocSingular
::
ExactParam
())




set.seed
(
1010
)


sce
.416
b <-
 
runTSNE
(sce
.416
b, 
dimred=
"PCA"
, 
perplexity=
10
)
