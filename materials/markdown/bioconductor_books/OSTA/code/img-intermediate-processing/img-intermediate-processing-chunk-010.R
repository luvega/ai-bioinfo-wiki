pcs
 
<-
 
c
(
Leiden
=
"PCA_tx"
, Banksy
=
"PCA_sp"
)


for
 
(
.
 
in
 
names
(
pcs
)
)
 
{


    
# build cellular shared nearest-neighbor (SNN) graph


    
g
 
<-
 
buildSNNGraph
(
spe
, use.dimred
=
pcs
[
.
]
, type
=
"jaccard"
, k
=
20
)


    
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
0.8
)


    
spe
[[
.
]
]
 
<-
 
factor
(
k
$
membership
)


}
