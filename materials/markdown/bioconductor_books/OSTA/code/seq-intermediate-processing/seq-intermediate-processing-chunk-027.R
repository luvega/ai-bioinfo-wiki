# run BayesSpace clustering


.spe
 
<-
 
spatialPreprocess
(
spe
, skip.PCA 
=
 
TRUE
)


.spe
 
<-
 
spatialCluster
(
.spe
, nrep 
=
 
1000
, burn.in 
=
 
100
, q 
=
 
10
, d 
=
 
20
)




# cluster labels


table
(
spe
$
BayesSpace
 
<-
 
factor
(
.spe
$
spatial.cluster
)
)
