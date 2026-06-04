# highlight border cells across 


# the tissue (using cell centroids)


cos
$
ex
 
<-
 
df
$
dist_border
 
<
 
r


plotCentroids
(
cos
, colourBy
=
"ex"
, sampleId
=
NULL
)
 
+


    
scale_color_manual
(
values
=
c
(
"lavender"
, 
"blue"
)
)
 
+


    
guides
(
col
=
guide_legend
(
override.aes
=
list
(
size
=
2
)
)
)
 
+


    
theme_void
(
)
 
+
 
theme
(
legend.key.size
=
unit
(
0
, 
"pt"
)
)


# zoom in on subset of FOVs


# visualizing cell boundaries


fs
 
<-
 
c
(
98
:
100
, 
113
:
115
, 
122
:
124
)


plotPolygons
(


    
cos
[
, 
cos
$
fov
 
%in%
 
fs
]
, 


    colourBy
=
"ex"
, sampleId
=
NULL
,


    borderCol
=
"black"
, palette
=
c
(
"lavender"
, 
"blue"
)
)
 
+


    
theme
(
legend.position
=
"none"
)
