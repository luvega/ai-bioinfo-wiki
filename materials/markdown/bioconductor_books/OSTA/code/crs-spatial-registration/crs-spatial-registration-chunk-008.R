# plot DAPI image


p
 
<-
 
plotVisium
(
xen
, spots
=
FALSE
, image_id
=
"DAPI"
)


# overlay cells with image


img
 
<-
 
imgRaster
(
xen
)


sf
 
<-
 
scaleFactors
(
xen
)


xy
 
<-
 
spatialCoords
(
xen
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
