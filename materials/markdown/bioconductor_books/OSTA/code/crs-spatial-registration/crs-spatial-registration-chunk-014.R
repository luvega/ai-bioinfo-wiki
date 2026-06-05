# plot H&E image


p
 
<-
 
plotVisium
(
reg
, spots
=
FALSE
, image_ids
=
"H&E"
)


# overlay cells with image


img
 
<-
 
imgRaster
(
reg
)


sf
 
<-
 
scaleFactors
(
reg
)


xy
 
<-
 
spatialCoords
(
reg
)
*
sf


xy
[
, 
2
]
 
<-
 
nrow
(
img
)
-
xy
[
, 
2
]


p
 
+
 
geom_point
(


    
aes
(
x_centroid
, 
y_centroid
)
, 
data.frame
(
xy
)
,


    shape
=
16
, stroke
=
0
, size
=
0.2
, alpha
=
0.4
, 


    col
=
"red"
, inherit.aes
=
FALSE
)
