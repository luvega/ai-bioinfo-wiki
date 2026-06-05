library
(scater)


g <-
 
buildSNNGraph
(multiout, 
use.dimred=
1
, 
k=
50
)


clusters <-
 
igraph
::
cluster_walktrap
(g)
$
membership


tab <-
 
table
(clusters, multiout
$
dataset)


tab
