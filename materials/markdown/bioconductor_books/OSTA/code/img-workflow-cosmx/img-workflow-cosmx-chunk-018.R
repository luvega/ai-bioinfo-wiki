# add PCs as cell metadata


pcs
 
<-
 
reducedDim
(
sub
, 
"PCA"
)


colData
(
sub
)
 
<-
 
cbind
(
colData
(
sub
)
, 
pcs
)


# visualize PCs 1 & 2 in space


plotCentroids
(
sub
, colourBy
=
"PC1"
)
 
+


plotCentroids
(
sub
, colourBy
=
"PC2"
)
