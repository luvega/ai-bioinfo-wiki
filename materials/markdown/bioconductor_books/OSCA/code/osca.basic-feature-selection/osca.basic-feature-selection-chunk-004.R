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
