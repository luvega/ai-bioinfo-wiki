#--- loading ---#


library
(scRNAseq)


sce.lawlor <-
 
LawlorPancreasData
()




#--- gene-annotation ---#


library
(AnnotationHub)


edb <-
 
AnnotationHub
()[[
"AH73881"
]]


anno <-
 
select
(edb, 
keys=
rownames
(sce.lawlor), 
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
(sce.lawlor) <-
 
anno[
match
(
rownames
(sce.lawlor), anno[,
1
]),
-
1
]




#--- quality-control ---#


library
(scater)


stats <-
 
perCellQCMetrics
(sce.lawlor, 


    
subsets=
list
(
Mito=
which
(
rowData
(sce.lawlor)
$
SEQNAME
==
"MT"
)))


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
"subsets_Mito_percent"
,


    
batch=
sce.lawlor
$
`
islet unos id
`
)


sce.lawlor <-
 
sce.lawlor[,
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
(sce.lawlor)


sce.lawlor <-
 
computeSumFactors
(sce.lawlor, 
clusters=
clusters)


sce.lawlor <-
 
logNormCounts
(sce.lawlor)




#--- variance-modelling ---#


dec.lawlor <-
 
modelGeneVar
(sce.lawlor, 
block=
sce.lawlor
$
`
islet unos id
`
)


chosen.genes <-
 
getTopHVGs
(dec.lawlor, 
n=
2000
)
