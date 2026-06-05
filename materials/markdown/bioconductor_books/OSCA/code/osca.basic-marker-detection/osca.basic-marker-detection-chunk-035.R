#--- loading ---#


library
(scRNAseq)


sce
.416
b <-
 
LunSpikeInData
(
which=
"416b"
) 


sce
.416
b
$
block <-
 
factor
(sce
.416
b
$
block)




#--- gene-annotation ---#


library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


rowData
(sce
.416
b)
$
ENSEMBL <-
 
rownames
(sce
.416
b)


rowData
(sce
.416
b)
$
SYMBOL <-
 
mapIds
(ens.mm.v97, 
keys=
rownames
(sce
.416
b),


    
keytype=
"GENEID"
, 
column=
"SYMBOL"
)


rowData
(sce
.416
b)
$
SEQNAME <-
 
mapIds
(ens.mm.v97, 
keys=
rownames
(sce
.416
b),


    
keytype=
"GENEID"
, 
column=
"SEQNAME"
)




library
(scater)


rownames
(sce
.416
b) <-
 
uniquifyFeatureNames
(
rowData
(sce
.416
b)
$
ENSEMBL, 


    
rowData
(sce
.416
b)
$
SYMBOL)




#--- quality-control ---#


mito <-
 
which
(
rowData
(sce
.416
b)
$
SEQNAME
==
"MT"
)


stats <-
 
perCellQCMetrics
(sce
.416
b, 
subsets=
list
(
Mt=
mito))


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
c
(
"subsets_Mt_percent"
,


    
"altexps_ERCC_percent"
), 
batch=
sce
.416
b
$
block)


sce
.416
b <-
 
sce
.416
b[,
!
qc
$
discard]




#--- normalization ---#


library
(scran)


sce
.416
b <-
 
computeSumFactors
(sce
.416
b)


sce
.416
b <-
 
logNormCounts
(sce
.416
b)




#--- variance-modelling ---#


dec
.416
b <-
 
modelGeneVarWithSpikes
(sce
.416
b, 
"ERCC"
, 
block=
sce
.416
b
$
block)


chosen.hvgs <-
 
getTopHVGs
(dec
.416
b, 
prop=
0.1
)




#--- batch-correction ---#


library
(limma)


assay
(sce
.416
b, 
"corrected"
) <-
 
removeBatchEffect
(
logcounts
(sce
.416
b), 


    
design=
model.matrix
(
~
sce
.416
b
$
phenotype), 
batch=
sce
.416
b
$
block)




#--- dimensionality-reduction ---#


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




#--- clustering ---#


my.dist <-
 
dist
(
reducedDim
(sce
.416
b, 
"PCA"
))


my.tree <-
 
hclust
(my.dist, 
method=
"ward.D2"
)




library
(dynamicTreeCut)


my.clusters <-
 
unname
(
cutreeDynamic
(my.tree, 
distM=
as.matrix
(my.dist),


    
minClusterSize=
10
, 
verbose=
0
))


colLabels
(sce
.416
b) <-
 
factor
(my.clusters)
