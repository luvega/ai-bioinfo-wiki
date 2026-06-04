library
(bluster)


clust.out <-
 
clusterRows
(
reducedDim
(sce.seger, 
"PCA"
), 
NNGraphParam
(), 
full=
TRUE
)


snn.gr <-
 
clust.out
$
objects
$
graph


colLabels
(sce.seger) <-
 
clust.out
$
clusters
