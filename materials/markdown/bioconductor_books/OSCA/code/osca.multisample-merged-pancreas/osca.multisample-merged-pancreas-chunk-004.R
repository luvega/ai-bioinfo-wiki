#--- loading ---#


library
(scRNAseq)


sce.muraro <-
 
MuraroPancreasData
()




#--- gene-annotation ---#


library
(AnnotationHub)


edb <-
 
AnnotationHub
()[[
"AH73881"
]]


gene.symb <-
 
sub
(
"__chr.*$"
, 
""
, 
rownames
(sce.muraro))


gene.ids <-
 
mapIds
(edb, 
keys=
gene.symb, 


    
keytype=
"SYMBOL"
, 
column=
"GENEID"
)




# Removing duplicated genes or genes without Ensembl IDs.


keep <-
 
!
is.na
(gene.ids) 
&
 
!
duplicated
(gene.ids)


sce.muraro <-
 
sce.muraro[keep,]


rownames
(sce.muraro) <-
 
gene.ids[keep]




#--- quality-control ---#


library
(scater)


stats <-
 
perCellQCMetrics
(sce.muraro)


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
"altexps_ERCC_percent"
,


    
batch=
sce.muraro
$
donor, 
subset=
sce.muraro
$
donor
!=
"D28"
)


sce.muraro <-
 
sce.muraro[,
!
qc
$
discard]




#--- normalization ---#


library
(scran)


set.seed
(
1000
)


clusters <-
 
quickCluster
(sce.muraro)


sce.muraro <-
 
computeSumFactors
(sce.muraro, 
clusters=
clusters)


sce.muraro <-
 
logNormCounts
(sce.muraro)




#--- variance-modelling ---#


block <-
 
paste0
(sce.muraro
$
plate, 
"_"
, sce.muraro
$
donor)


dec.muraro <-
 
modelGeneVarWithSpikes
(sce.muraro, 
"ERCC"
, 
block=
block)


top.muraro <-
 
getTopHVGs
(dec.muraro, 
prop=
0.1
)
