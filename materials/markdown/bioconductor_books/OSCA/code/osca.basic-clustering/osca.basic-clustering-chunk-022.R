clust.walktrap <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
cluster.fun=
"walktrap"
))




clust.louvain <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
cluster.fun=
"louvain"
))




clust.infomap <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
cluster.fun=
"infomap"
))




clust.fast <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
cluster.fun=
"fast_greedy"
))




clust.labprop <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
cluster.fun=
"label_prop"
))




clust.eigen <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
cluster.fun=
"leading_eigen"
))
