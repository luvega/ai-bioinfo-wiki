library
(scran)


snn.gr <-
 
buildSNNGraph
(mnn.out, 
use.dimred=
"corrected"
)


clusters.mnn <-
 
igraph
::
cluster_walktrap
(snn.gr)
$
membership


tab.mnn <-
 
table
(
Cluster=
clusters.mnn, 
Batch=
mnn.out
$
batch)


tab.mnn
