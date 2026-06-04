plotCoords
(
.vhd16
, point_shape
=
15
, annotate
=
"discard"
)
 
+
 
ggtitle
(
"discard"
)
 
+


plotCoords
(
.vhd16
, point_shape
=
15
, annotate
=
"sum_outliers"
)
 
+
 
ggtitle
(
"low_lib_size"
)
 
+


plotCoords
(
.vhd16
, point_shape
=
15
, annotate
=
"detected_outliers"
)
 
+
 
ggtitle
(
"low_n_features"
)
 
+


plot_layout
(
nrow
=
1
, guides
=
"collect"
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
)
,


        legend.key.size
=
unit
(
0
, 
"lines"
)
)
 
&


    
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
3
)
)
)
 
&
 


    
scale_color_manual
(
"discard"
, values
=
c
(
"lavender"
, 
"purple"
)
)
