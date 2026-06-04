.rng
 
<-
 \
(
spe
)
 
{


    
xy
 
<-
 
spatialCoords
(
spe
)
*
scaleFactors
(
spe
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
; 
ys
 
<-
 
nrow
(
imgRaster
(
spe
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


    
x1
 
<-
 
xs
[
1
]
 
+
 
4
*
(
xs
[
2
]
-
xs
[
1
]
)
/
8
; 
x2
 
<-
 
xs
[
2
]
 
-
 
3
*
(
xs
[
2
]
-
xs
[
1
]
)
/
8


    
y1
 
<-
 
ys
[
1
]
 
+
 
3
*
(
ys
[
2
]
-
ys
[
1
]
)
/
8
; 
y2
 
<-
 
ys
[
2
]
 
-
 
4
*
(
ys
[
2
]
-
ys
[
1
]
)
/
8


    
list
(
box
=
c
(
x1
, 
x2
, 
y1
, 
y2
)
, cov
=
c
(
xs
, 
ys
)
)


}


vhd8r
 
<-
 
.rng
(
vhd8
)


# vhd16r <- .rng(vhd16) 


# use 8um bounding boxes to subset spes at both resolutions; 


# it is similar to 16um's box range 


.box
 
<-
 \
(
roi
, 
lty
, 
lwd
, 
col
)
 
{


    
geom_rect
(


        xmin
=
vhd8r
[[
roi
]
]
[
1
]
, xmax
=
vhd8r
[[
roi
]
]
[
2
]
, 


        ymin
=
vhd8r
[[
roi
]
]
[
3
]
, ymax
=
vhd8r
[[
roi
]
]
[
4
]
,


        col
=
col
, fill
=
NA
, linetype
=
lty
, linewidth
=
lwd
)


}


cov
 
<-
 
.box
(
roi
=
"cov"
, lty
=
2
, lwd
=
1
/
2
, col
=
"grey"
)


box
 
<-
 
.box
(
roi
=
"box"
, lty
=
4
, lwd
=
2
/
3
, col
=
"black"
)


# plotting


.lim
 
<-
 \
(
spe
)
 
list
(


    
xlim
(
spe
[[
"box"
]
]
[
c
(
1
, 
2
)
]
)
,


    
ylim
(
spe
[[
"box"
]
]
[
c
(
4
, 
3
)
]
)
)




plotVisium
(
vhd8
, spots
=
FALSE
, point_shape
=
22
)
 
+
 
cov
 
+
 
box
 
+


    
ggtitle
(
"grey: data coverage\n black: zoomed region"
)
 
+
 


plotVisium
(
vhd8
, point_size
=
0.8
, zoom
=
TRUE
, point_shape
=
22
)
 
+
 
.lim
(
vhd8r
)
 
+


    
ggtitle
(
"8 µm bins in black box"
)
 
+
 


plotVisium
(
vhd16
, point_size
=
1.6
, zoom
=
TRUE
, point_shape
=
22
)
 
+
 
.lim
(
vhd8r
)
 
+


    
ggtitle
(
"16 µm bins in black box"
)
 
+
 


plot_layout
(
nrow
=
1
, widths
=
c
(
1.5
, 
1
, 
1
)
)
 
&
 
facet_null
(
)
 
&


    
theme
(
plot.title
=
element_text
(
hjust
=
0.5
, vjust
=
0.5
)
)
