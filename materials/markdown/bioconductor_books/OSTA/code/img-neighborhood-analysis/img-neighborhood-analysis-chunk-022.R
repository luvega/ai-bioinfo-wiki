ggplot
(
fd
, 
aes
(
k
, 
value
, fill
=
k
)
)
 
+


    
facet_wrap
(
~
name
)
 
+
 


    
scale_fill_manual
(
values
=
pal_k
)
 
+
 


    
geom_boxplot
(
outlier.stroke
=
0
, key_glyph
=
"point"
)
 
+


    
scale_y_continuous
(
"z-scaled value"
, limits
=
c
(
-
2
, 
2
)
)
 
+


    
guides
(
fill
=
guide_legend
(
override.aes
=
list
(
shape
=
21
, size
=
2
)
)
)
 
+


    
theme_bw
(
)
 
+
 
theme
(


        axis.title.x
=
element_blank
(
)
,


        panel.grid.minor
=
element_blank
(
)
,


        legend.key.size
=
unit
(
0.5
, 
"lines"
)
)
