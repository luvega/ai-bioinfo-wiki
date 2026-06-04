clust.full <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
)


plotExpression
(sce.pbmc, 
features=
c
(
"CD3E"
, 
"CCR7"
, 
"CD69"
, 
"CD44"
),


    
x=
I
(clust.full), 
colour_by=
I
(clust.full))
