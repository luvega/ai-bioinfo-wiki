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
.vhd16
$
Banksy
 
<-
 
factor
(
k
$
membership
)
)
