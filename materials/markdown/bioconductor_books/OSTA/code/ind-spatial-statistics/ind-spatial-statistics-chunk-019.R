df
 
<-
 
data.frame
(
xy
, 
colData
(
sfe
)
)


ggplot
(
df
, 
aes
(
x_centroid
, 
y_centroid
, col
=
Cluster
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
 
+


    
theme_xy
 
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


    
geom_point
(
shape
=
16
, size
=
0.1
)
