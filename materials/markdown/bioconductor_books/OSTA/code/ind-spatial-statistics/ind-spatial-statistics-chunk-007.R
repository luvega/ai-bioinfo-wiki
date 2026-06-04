I
 
<-
 
rowData
(
sfe
)
$
moran_sample01


o
 
<-
 
order
(
I
, decreasing
=
TRUE
)


topGenes
 
<-
 
rownames
(
sfe
)
[
head
(
o
, 
3
)
]


plotSpatialFeature
(
sfe
, 
topGenes
, ncol
=
3
)
