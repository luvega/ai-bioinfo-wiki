# test for differentially expressed genes 


# (DEGs) to identify subpopulation markers


colLabels
(
sce
)
 
<-
 
sce
$
Annotation


mgs
 
<-
 
findMarkers
(
sce
, test
=
"wilcox"
, direction
=
"up"
, BPPARAM
=
bp
)
