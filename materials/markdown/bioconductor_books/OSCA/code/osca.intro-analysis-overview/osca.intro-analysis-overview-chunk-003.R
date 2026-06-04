sce <-
 
SegerstolpePancreasData
()




# Quality control (using ERCCs).


qcstats <-
 
perCellQCMetrics
(sce)


filtered <-
 
quickPerCellQC
(qcstats, 
percent_subsets=
"altexps_ERCC_percent"
)


sce <-
 
sce[, 
!
filtered
$
discard]




# Normalization.


sce <-
 
logNormCounts
(sce)




# Feature selection, blocking on the individual of origin.


dec <-
 
modelGeneVar
(sce, 
block=
sce
$
individual)


hvg <-
 
getTopHVGs
(dec, 
prop=
0.1
)




# Batch correction.


library
(batchelor)


set.seed
(
1234
)


sce <-
 
correctExperiments
(sce, 
batch=
sce
$
individual, 


    
subset.row=
hvg, 
correct.all=
TRUE
)




# Clustering.


colLabels
(sce) <-
 
clusterCells
(sce, 
use.dimred=
'corrected'
)




# Visualization.


sce <-
 
runUMAP
(sce, 
dimred =
 
'corrected'
)


gridExtra
::
grid.arrange
(


    
plotUMAP
(sce, 
colour_by=
"label"
),


    
plotUMAP
(sce, 
colour_by=
"individual"
),


    
ncol=
2


)
