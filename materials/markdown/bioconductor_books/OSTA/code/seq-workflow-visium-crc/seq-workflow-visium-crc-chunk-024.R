# cluster via Leiden community detection algorithm


k
 
<-
 
cluster_leiden
(
g
, objective_function
=
"modularity"
, resolution
=
0.5
)


table
(
spe
$
Leiden
 
<-
 
factor
(
k
$
membership
)
)
