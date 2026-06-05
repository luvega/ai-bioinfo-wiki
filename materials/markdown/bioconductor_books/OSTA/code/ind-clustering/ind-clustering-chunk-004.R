# cluster using Leiden community detection algorithm


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
1.2
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
