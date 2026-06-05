# To ensure reproducibility of the randomized PCA.


set.seed
(
1010101010
) 


rescaled <-
 
runPCA
(rescaled, 
subset_row=
chosen.hvgs, 


    
exprs_values=
"corrected"
,


    
BSPARAM=
BiocSingular
::
RandomParam
())




snn.gr <-
 
buildSNNGraph
(rescaled, 
use.dimred=
"PCA"
)


clusters.resc <-
 
igraph
::
cluster_walktrap
(snn.gr)
$
membership


tab.resc <-
 
table
(
Cluster=
clusters.resc, 
Batch=
rescaled
$
batch)


tab.resc
