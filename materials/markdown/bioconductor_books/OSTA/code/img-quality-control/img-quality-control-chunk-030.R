# visualize quality scores & highlight flagged cells


thm
 
<-
 
list
(
theme_void
(
)
, 
ggtitle
(
""
)
, 
coord_equal
(
)
)


plotCentroids
(
cos
, colourBy
=
"QC_score"
)
 
+
 
thm
 
+


plotCentroids
(
cos
, colourBy
=
"low_qcscore"
)
 
+
 
thm
 
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
