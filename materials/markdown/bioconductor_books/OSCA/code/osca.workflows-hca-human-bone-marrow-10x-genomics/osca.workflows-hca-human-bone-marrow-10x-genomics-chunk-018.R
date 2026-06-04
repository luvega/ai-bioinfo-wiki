# 
TODO
: add scrambling option in scater's plotting functions.


scrambled <-
 
sample
(
ncol
(sce.bone))




gridExtra
::
grid.arrange
(


    
plotUMAP
(sce.bone, 
colour_by=
"label"
, 
text_by=
"label"
),


    
plotUMAP
(sce.bone[,scrambled], 
colour_by=
"Donor"
)


)
