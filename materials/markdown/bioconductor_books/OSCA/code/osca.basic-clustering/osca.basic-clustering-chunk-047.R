# Setting the seed due to the randomness of k-means.


set.seed
(
1111
)


kaclust.info <-
 
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
AffinityParam
(
q=
0.1
) 
# larger q => more clusters


    ),


    
full=
TRUE


)


table
(kaclust.info
$
clusters)
