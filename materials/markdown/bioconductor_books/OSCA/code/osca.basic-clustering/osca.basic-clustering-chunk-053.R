set.seed
(
1000010
)


subcluster.out <-
 
quickSubCluster
(sce.pbmc, 
groups=
clust.full,


    
prepFUN=
function
(x) { 
# Preparing the subsetted SCE for clustering.


        dec <-
 
modelGeneVar
(x)


        input <-
 
denoisePCA
(x, 
technical=
dec,


            
subset.row=
getTopHVGs
(dec, 
prop=
0.1
),


            
BSPARAM=
BiocSingular
::
IrlbaParam
())


    },


    
clusterFUN=
function
(x) { 
# Performing the subclustering in the subset.


        g <-
 
buildSNNGraph
(x, 
use.dimred=
"PCA"
, 
k=
20
)


        igraph
::
cluster_walktrap
(g)
$
membership


    }


)




# One SingleCellExperiment object per parent cluster:


names
(subcluster.out)
