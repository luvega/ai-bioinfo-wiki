plotVisium
(
.vhd8
, 


    annotate
=
".DeconLabel1"
, zoom
=
TRUE
, 


    point_size
=
0.8
, point_shape
=
22
)
 
+
 


    
ggtitle
(
"8 µm"
)
 
+
 


plot_spacer
(
)
 
+


plotVisium
(
.vhd16
, 


    annotate
=
".DeconLabel1"
, zoom
=
TRUE
, 


    point_size
=
1.6
, point_shape
=
22
)
 
+
 


    
ggtitle
(
"16 µm"
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
, widths
=
c
(
1
, 
0.05
, 
1
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
2
)
)
)
 
&


    
scale_fill_manual
(
values
=
unname
(
pals
::
trubetskoy
(
)
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
