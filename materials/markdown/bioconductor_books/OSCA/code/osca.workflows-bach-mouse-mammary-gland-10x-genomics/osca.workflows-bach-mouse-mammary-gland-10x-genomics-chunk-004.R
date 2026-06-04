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
