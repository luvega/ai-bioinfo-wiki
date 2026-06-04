# Setting the seed due to the randomness of k-means.


set.seed
(
1111
)


khclust.info <-
 
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
HclustParam
(
method=
"ward.D2"
, 
cut.dynamic=
TRUE
,


            
cut.param=
list
(
deepSplit=
3
)) 
# for higher resolution.


    ),


    
full=
TRUE


)


table
(khclust.info
$
clusters)
