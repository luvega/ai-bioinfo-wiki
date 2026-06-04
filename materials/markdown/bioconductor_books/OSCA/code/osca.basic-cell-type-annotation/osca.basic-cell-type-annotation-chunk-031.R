#--- loading ---#


library
(scRNAseq)


sce.mam <-
 
BachMammaryData
(
samples=
"G_1"
)




#--- gene-annotation ---#


library
(scater)


rownames
(sce.mam) <-
 
uniquifyFeatureNames
(


    
rowData
(sce.mam)
$
Ensembl, 
rowData
(sce.mam)
$
Symbol)




library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


rowData
(sce.mam)
$
SEQNAME <-
 
mapIds
(ens.mm.v97, 
keys=
rowData
(sce.mam)
$
Ensembl,


    
keytype=
"GENEID"
, 
column=
"SEQNAME"
)




#--- quality-control ---#


is.mito <-
 
rowData
(sce.mam)
$
SEQNAME 
==
 "MT"


stats <-
 
perCellQCMetrics
(sce.mam, 
subsets=
list
(
Mito=
which
(is.mito)))


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
"subsets_Mito_percent"
)


sce.mam <-
 
sce.mam[,
!
qc
$
discard]




#--- normalization ---#


library
(scran)


set.seed
(
101000110
)


clusters <-
 
quickCluster
(sce.mam)


sce.mam <-
 
computeSumFactors
(sce.mam, 
clusters=
clusters)


sce.mam <-
 
logNormCounts
(sce.mam)




#--- variance-modelling ---#


set.seed
(
00010101
)


dec.mam <-
 
modelGeneVarByPoisson
(sce.mam)


top.mam <-
 
getTopHVGs
(dec.mam, 
prop=
0.1
)




#--- dimensionality-reduction ---#


library
(BiocSingular)


set.seed
(
101010011
)


sce.mam <-
 
denoisePCA
(sce.mam, 
technical=
dec.mam, 
subset.row=
top.mam)


sce.mam <-
 
runTSNE
(sce.mam, 
dimred=
"PCA"
)




#--- clustering ---#


snn.gr <-
 
buildSNNGraph
(sce.mam, 
use.dimred=
"PCA"
, 
k=
25
)


colLabels
(sce.mam) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
