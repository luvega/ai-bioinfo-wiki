library
(scran)


wilcox.z <-
 
pairwiseWilcox
(sce.zeisel, sce.zeisel
$
level1class, 


    
lfc=
1
, 
direction=
"up"
)


markers.z <-
 
getTopMarkers
(wilcox.z
$
statistics, wilcox.z
$
pairs,


    
pairwise=
FALSE
, 
n=
50
)


lengths
(markers.z)
