top.markers <-
 
markers.bone[[cluster.choice]]


best <-
 
top.markers[top.markers
$
Top 
<=
 
10
,]


lfcs <-
 
getMarkerEffects
(best)




library
(pheatmap)


pheatmap
(lfcs, 
breaks=
seq
(
-
5
, 
5
, 
length.out=
101
))
