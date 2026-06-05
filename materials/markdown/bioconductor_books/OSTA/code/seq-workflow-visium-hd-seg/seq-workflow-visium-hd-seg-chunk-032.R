plotCoords
(
sfe
[
, 
order
(
sfe
$
ex
)
]
, 


    annotate
=
"ex"
, point_size
=
0.2
)
 
+


    
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
 
+


    
scale_color_manual
(
values
=
c
(
"grey90"
, 
"red"
)
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
size
=
2
)
)
)
