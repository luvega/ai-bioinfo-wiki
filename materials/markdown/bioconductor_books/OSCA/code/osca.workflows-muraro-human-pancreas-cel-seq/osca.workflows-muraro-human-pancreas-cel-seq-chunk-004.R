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
