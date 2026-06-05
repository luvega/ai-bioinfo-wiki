plotUMAP
(
obj
, colour_by
=
"sample_id"
, point_size
=
0.1
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
alpha
=
1
, size
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
aspect.ratio
=
1
, legend.key.size
=
unit
(
0
, 
"pt"
)
)
