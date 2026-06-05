# reverse y-coordinates of bounding box


.box
 
<-
 
box


.box
$
ymax
 
<-
 
-
box
$
ymin


.box
$
ymin
 
<-
 
-
box
$
ymax


aes
 
<-
 
list
(
col
=
"red"
, fill
=
NA
, linewidth
=
2
)


plotCoords
(


    
spe
[
, 
sample
(
ncol
(
spe
)
, 
5e4
)
]
)
 
+
 


    
do.call
(
geom_rect
, 
c
(
.box
, 
aes
)
)
 
+


plotCoords
(


    
sub
[
, 
sample
(
ncol
(
sub
)
, 
5e4
)
]
)
