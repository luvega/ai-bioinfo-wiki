lapply
(
names
(
ws
)
, \
(
.
)
 


    
plotCoords
(
.vhd16
, annotate
=
.
, point_size
=
0.3
, point_shape
=
15
)
)
 
|>


    
wrap_plots
(
nrow
=
2
, guides
=
"collect"
)
 
&
 
theme
(


    legend.key.width
=
unit
(
0.5
, 
"lines"
)
,


    legend.key.height
=
unit
(
1
, 
"lines"
)
)
 
&


    
scale_color_gradientn
(
colors
=
rev
(
hcl.colors
(
9
, 
"Rocket"
)
)
)
