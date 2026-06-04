set.seed
(
1010010
)


subclusters <-
 
quickSubCluster
(sce.pbmc, clust.adt,


    
prepFUN=
function
(x) {


        dec <-
 
modelGeneVarByPoisson
(x)


        top <-
 
getTopHVGs
(dec, 
prop=
0.1
)


        
denoisePCA
(x, dec, 
subset.row=
top)


    }, 


    
clusterFUN=
function
(x) {


        g.gene <-
 
buildSNNGraph
(x, 
k=
10
, 
use.dimred =
 
'PCA'
)


        igraph
::
cluster_walktrap
(g.gene)
$
membership


    }


)
