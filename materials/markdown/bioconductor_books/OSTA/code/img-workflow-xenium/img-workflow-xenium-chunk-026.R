# community detection using Leiden algorithm


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
0.7
)


table
(
sub
$
Leiden
 
<-
 
factor
(
.
 
<-
 
k
$
membership
, labels
=
letters
[
seq_along
(
unique
(
.
)
)
]
)
)
