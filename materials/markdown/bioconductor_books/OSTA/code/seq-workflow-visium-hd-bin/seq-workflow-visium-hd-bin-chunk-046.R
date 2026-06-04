gs
 
<-
 
c
(
"MMP2"
, 
"PIGR"
, 
"IGHG1"
)


ps
 
<-
 
lapply
(
gs
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
, point_shape
=
15
, 


                                 point_size
=
0.8
, assay_name
=
"logcounts"
)
)


wrap_plots
(
ps
, nrow
=
1
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
