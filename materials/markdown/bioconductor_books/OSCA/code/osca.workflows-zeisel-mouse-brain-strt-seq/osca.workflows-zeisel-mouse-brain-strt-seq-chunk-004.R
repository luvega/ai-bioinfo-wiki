stats <-
 
perCellQCMetrics
(sce.zeisel, 
subsets=
list
(


    
Mt=
rowData
(sce.zeisel)
$
featureType
==
"mito"
))


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
c
(
"altexps_ERCC_percent"
, 


    
"subsets_Mt_percent"
))


sce.zeisel <-
 
sce.zeisel[,
!
qc
$
discard]
