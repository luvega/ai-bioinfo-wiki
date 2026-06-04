#--- loading ---#


library
(DropletTestFiles)


raw.path <-
 
getTestFile
(
"tenx-2.1.0-pbmc4k/1.0.0/raw.tar.gz"
)


out.path <-
 
file.path
(
tempdir
(), 
"pbmc4k"
)


untar
(raw.path, 
exdir=
out.path)




library
(DropletUtils)


fname <-
 
file.path
(out.path, 
"raw_gene_bc_matrices/GRCh38"
)


sce.pbmc <-
 
read10xCounts
(fname, 
col.names=
TRUE
)




#--- gene-annotation ---#


library
(scater)


rownames
(sce.pbmc) <-
 
uniquifyFeatureNames
(


    
rowData
(sce.pbmc)
$
ID, 
rowData
(sce.pbmc)
$
Symbol)




library
(EnsDb.Hsapiens.v86)


location <-
 
mapIds
(EnsDb.Hsapiens.v86, 
keys=
rowData
(sce.pbmc)
$
ID, 


    
column=
"SEQNAME"
, 
keytype=
"GENEID"
)




#--- cell-detection ---#


set.seed
(
100
)


e.out <-
 
emptyDrops
(
counts
(sce.pbmc))


sce.pbmc <-
 
sce.pbmc[,
which
(e.out
$
FDR 
<=
 
0.001
)]




#--- quality-control ---#


stats <-
 
perCellQCMetrics
(sce.pbmc, 
subsets=
list
(
Mito=
which
(location
==
"MT"
)))


high.mito <-
 
isOutlier
(stats
$
subsets_Mito_percent, 
type=
"higher"
)


sce.pbmc <-
 
sce.pbmc[,
!
high.mito]




#--- normalization ---#


library
(scran)


set.seed
(
1000
)


clusters <-
 
quickCluster
(sce.pbmc)


sce.pbmc <-
 
computeSumFactors
(sce.pbmc, 
cluster=
clusters)


sce.pbmc <-
 
logNormCounts
(sce.pbmc)
