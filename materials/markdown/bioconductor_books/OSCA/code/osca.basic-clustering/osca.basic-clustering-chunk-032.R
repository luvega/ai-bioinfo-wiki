# Setting the seed due to the randomness of k-means.


set.seed
(
0101010
)


kgraph.clusters <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
,


    
BLUSPARAM=
TwoStepParam
(


        
first=
KmeansParam
(
centers=
1000
),


        
second=
NNGraphParam
(
k=
5
)


    )


)


table
(kgraph.clusters)
