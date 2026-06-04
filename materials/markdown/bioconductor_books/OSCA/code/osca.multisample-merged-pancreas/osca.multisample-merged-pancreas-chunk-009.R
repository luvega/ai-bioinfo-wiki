set.seed
(
1011011
)


mnn.pancreas <-
 
fastMNN
(sce.grun2, sce.muraro2, 
subset.row=
chosen.genes)




snn.gr <-
 
buildSNNGraph
(mnn.pancreas, 
use.dimred=
"corrected"
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
mnn.pancreas
$
batch)


tab
