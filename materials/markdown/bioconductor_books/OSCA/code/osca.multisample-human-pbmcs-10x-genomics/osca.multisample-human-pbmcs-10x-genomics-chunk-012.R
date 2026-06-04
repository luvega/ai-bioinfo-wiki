library
(BiocSingular)


set.seed
(
10000
)


all.sce <-
 
mapply
(
FUN=
runPCA, 
x=
all.sce, 
subset_row=
all.hvgs, 


    
MoreArgs=
list
(
ncomponents=
25
, 
BSPARAM=
RandomParam
()), 


    
SIMPLIFY=
FALSE
)




set.seed
(
100000
)


all.sce <-
 
lapply
(all.sce, runTSNE, 
dimred=
"PCA"
)




set.seed
(
1000000
)


all.sce <-
 
lapply
(all.sce, runUMAP, 
dimred=
"PCA"
)
