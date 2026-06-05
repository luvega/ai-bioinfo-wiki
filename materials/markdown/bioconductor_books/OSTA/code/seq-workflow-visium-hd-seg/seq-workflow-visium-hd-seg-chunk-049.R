plotCoords
(
sfe
, 


    annotate
=
"Level1"
, point_size
=
0.1
)
 
+


    
scale_color_manual
(
values
=
pal_lv1
)
 
+


plotCoords
(
sfe
, 


    annotate
=
"Level0"
, point_size
=
0.1
)
 
+


    
scale_color_manual
(
values
=
pal_lv0
)
 
+


plot_layout
(
)
 
&


    
theme
(
legend.key.size
=
ggplot2
::
unit
(
0
, 
"pt"
)
)
