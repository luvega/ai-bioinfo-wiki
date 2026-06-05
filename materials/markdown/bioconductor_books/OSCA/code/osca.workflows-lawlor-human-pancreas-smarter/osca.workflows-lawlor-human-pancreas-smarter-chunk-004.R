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
