library
(bluster)


nn.clusters2 <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
SNNGraphParam
(
k=
10
, 
type=
"rank"
, 
cluster.fun=
"walktrap"
))


table
(nn.clusters2)
