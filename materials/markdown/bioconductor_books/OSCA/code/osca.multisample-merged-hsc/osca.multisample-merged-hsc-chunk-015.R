library
(bluster)


colLabels
(merged) <-
 
clusterRows
(
reducedDim
(merged), 


    
NNGraphParam
(
cluster.fun=
"louvain"
))


table
(
Cluster=
colLabels
(merged), 
Batch=
merged
$
batch)
