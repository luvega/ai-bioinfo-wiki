# load processed Visium dataset


vis
 
<-
 
readRDS
(
"seq-spe_cl.rds"
)


# prepare data for 'BayesSpace'


# skipping PCA (already computed)


.vis
 
<-
 
spatialPreprocess
(
vis
, skip.PCA
=
TRUE
)


# perform spatial clustering with 'BayesSpace'


# using 'd=20' PCs and targeting 'q=10' clusters


.vis
 
<-
 
spatialCluster
(
.vis
, q
=
10
, d
=
20
, nrep
=
1e3
, burn.in
=
100
)
 


table
(
vis
$
BayesSpace
 
<-
 
factor
(
.vis
$
spatial.cluster
)
)
