# set seed for random number generation


# in order to make results reproducible


set.seed
(
112358
)


# 'Banksy' parameter settings


k
 
<-
 
8
   
# consider first order neighbors


l
 
<-
 
0.2
 
# use little spatial information


a
 
<-
 
"logcounts"


xy
 
<-
 
c
(
"array_row"
, 
"array_col"
)


# restrict to selected features


tmp
 
<-
 
.vhd16
[
hvg
, 
]


# compute spatially aware 'Banksy' PCs


tmp
 
<-
 
computeBanksy
(
tmp
, assay_name
=
a
, coord_names
=
xy
, k_geom
=
k
)


tmp
 
<-
 
runBanksyPCA
(
tmp
, lambda
=
l
, npcs
=
20
)


reducedDim
(
.vhd16
, 
"PCA"
)
 
<-
 
reducedDim
(
tmp
)


## run UMAP (for visualization purposes only)


# .vhd16 <- runUMAP(.vhd16, dimred="PCA")


# build cellular shared nearest-neighbor (SNN) graph


g
 
<-
 
buildSNNGraph
(
.vhd16
, use.dimred
=
"PCA"
, type
=
"jaccard"
, k
=
20
)
