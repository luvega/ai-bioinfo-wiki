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
