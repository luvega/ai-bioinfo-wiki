colLabels
(sce) <-
 
scran
::
clusterCells
(sce, 
use.dimred=
"PCA"
)


table
(
colLabels
(sce))
