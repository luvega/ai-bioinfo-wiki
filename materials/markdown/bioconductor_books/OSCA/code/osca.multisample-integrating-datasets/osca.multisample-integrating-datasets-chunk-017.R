library
(scran)


snn.gr <-
 
buildSNNGraph
(uncorrected, 
use.dimred=
"PCA"
)


clusters <-
 
igraph
::
cluster_walktrap
(snn.gr)
$
membership


tab <-
 
table
(
Cluster=
clusters, 
Batch=
uncorrected
$
batch)


tab
