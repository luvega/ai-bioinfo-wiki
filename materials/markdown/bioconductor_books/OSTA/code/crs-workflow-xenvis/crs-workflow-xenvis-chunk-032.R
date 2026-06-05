# 'BayesSpace' clustering


res
 
<-
 
spatialCluster
(
obj
, q
=
10
, burn.in
=
100
, nrep
=
1e3
)


table
(
res
$
k
 
<-
 
factor
(
res
$
spatial.cluster
)
)
