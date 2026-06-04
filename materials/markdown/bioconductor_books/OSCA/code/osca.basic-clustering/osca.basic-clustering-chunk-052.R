g.memory <-
 
buildSNNGraph
(sce.memory, 
use.dimred=
"PCA"
)


clust.memory <-
 
igraph
::
cluster_walktrap
(g.memory)
$
membership


plotExpression
(sce.memory, 
features=
c
(
"CD8A"
, 
"CD4"
),


    
x=
I
(
factor
(clust.memory)))
