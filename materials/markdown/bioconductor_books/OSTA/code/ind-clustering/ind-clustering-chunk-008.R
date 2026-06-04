# perform SNN graph-based clustering on 'Banksy' PCs using


# same parameters as for 'non-spatial' clustering above


g
 
<-
 
buildSNNGraph
(
spe
, use.dimred
=
"PCA_sp"
, type
=
"jaccard"
, k
=
20
)
