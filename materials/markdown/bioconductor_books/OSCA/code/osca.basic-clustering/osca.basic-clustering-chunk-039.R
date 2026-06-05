hclust.dyn <-
 
clusterCells
(sce
.416
b, 
use.dimred=
"PCA"
,


    
BLUSPARAM=
HclustParam
(
method=
"ward.D2"
, 
cut.dynamic=
TRUE
,


        
cut.params=
list
(
minClusterSize=
10
, 
deepSplit=
1
)))


table
(hclust.dyn)
