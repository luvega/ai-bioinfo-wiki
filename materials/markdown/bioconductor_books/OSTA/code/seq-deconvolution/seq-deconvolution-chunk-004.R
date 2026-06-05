xy
 
<-
 
spatialCoords
(
vis
)
 
*
 
scaleFactors
(
vis
)


ys
 
<-
 
nrow
(
imgRaster
(
vis
)
)
 
-
 
range
(
xy
[
, 
2
]
)


xs
 
<-
 
range
(
xy
[
, 
1
]
)


box
 
<-
 
geom_rect
(


    xmin
=
xs
[
1
]
, xmax
=
xs
[
2
]
, ymin
=
ys
[
1
]
, ymax
=
ys
[
2
]
, 


    col
=
"black"
, fill
=
NA
, linetype
=
2
, linewidth
=
2
/
3
)


plotVisium
(
vis
, spots
=
FALSE
, point_size
=
1
)
 
+
 
box
 
+
 


    
plotVisium
(
vis
, point_size
=
1
, zoom
=
TRUE
)
 
+
 


    
plot_layout
(
nrow
=
1
)
 
&
 
facet_null
(
)
