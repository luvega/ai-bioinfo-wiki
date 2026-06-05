library
(pheatmap)


logFCs <-
 
getMarkerEffects
(marker.set[
1
:
50
,])


pheatmap
(logFCs, 
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
