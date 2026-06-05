#--- loading ---#


library
(TENxPBMCData)


all.sce <-
 
list
(


    
pbmc3k=
TENxPBMCData
(
'pbmc3k'
),


    
pbmc4k=
TENxPBMCData
(
'pbmc4k'
),


    
pbmc8k=
TENxPBMCData
(
'pbmc8k'
)


)




#--- quality-control ---#


library
(scater)


stats <-
 
high.mito <-
 
list
()


for
 (n 
in
 
names
(all.sce)) {


    current <-
 
all.sce[[n]]


    is.mito <-
 
grep
(
"MT"
, 
rowData
(current)
$
Symbol_TENx)


    stats[[n]] <-
 
perCellQCMetrics
(current, 
subsets=
list
(
Mito=
is.mito))


    high.mito[[n]] <-
 
isOutlier
(stats[[n]]
$
subsets_Mito_percent, 
type=
"higher"
)


    all.sce[[n]] <-
 
current[,
!
high.mito[[n]]]


}




#--- normalization ---#


all.sce <-
 
lapply
(all.sce, logNormCounts)




#--- variance-modelling ---#


library
(scran)


all.dec <-
 
lapply
(all.sce, modelGeneVar)


all.hvgs <-
 
lapply
(all.dec, getTopHVGs, 
prop=
0.1
)




#--- dimensionality-reduction ---#


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




#--- clustering ---#


for
 (n 
in
 
names
(all.sce)) {


    g <-
 
buildSNNGraph
(all.sce[[n]], 
k=
10
, 
use.dimred=
'PCA'
)


    clust <-
 
igraph
::
cluster_walktrap
(g)
$
membership


    
colLabels
(all.sce[[n]])  <-
 
factor
(clust)


}
