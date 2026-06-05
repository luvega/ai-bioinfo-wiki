#--- data-loading ---#


library
(scRNAseq)


sce.nest <-
 
NestorowaHSCData
()




#--- gene-annotation ---#


library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


anno <-
 
select
(ens.mm.v97, 
keys=
rownames
(sce.nest), 


    
keytype=
"GENEID"
, 
columns=
c
(
"SYMBOL"
, 
"SEQNAME"
))


rowData
(sce.nest) <-
 
anno[
match
(
rownames
(sce.nest), anno
$
GENEID),]




#--- quality-control ---#


library
(scater)


stats <-
 
perCellQCMetrics
(sce.nest)


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
"altexps_ERCC_percent"
)


sce.nest <-
 
sce.nest[,
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
(sce.nest)


sce.nest <-
 
computeSumFactors
(sce.nest, 
clusters=
clusters)


sce.nest <-
 
logNormCounts
(sce.nest)




#--- variance-modelling ---#


set.seed
(
00010101
)


dec.nest <-
 
modelGeneVarWithSpikes
(sce.nest, 
"ERCC"
)


top.nest <-
 
getTopHVGs
(dec.nest, 
prop=
0.1
)
