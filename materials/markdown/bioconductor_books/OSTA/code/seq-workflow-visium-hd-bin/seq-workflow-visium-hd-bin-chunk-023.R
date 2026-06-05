plotCoords
(
.vhd16
, annotate
=
"sum_log"
, point_size
=
0.2
, point_shape
=
15
)
 
+
 


  
ggtitle
(
"log-library size"
)
 
+


  
plotCoords
(
.vhd16
, annotate
=
"subsets_mt_percent"
, point_size
=
0.2
, point_shape
=
15
)
 
+
 


  
ggtitle
(
"% mitochondrial"
)
 
+


  
plot_layout
(
nrow
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
pals
::
jet
(
)
)
