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
