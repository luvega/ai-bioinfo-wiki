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
rgb
)
)
 
+


    
geom_point
(
shape
=
16
, stroke
=
0
, size
=
0.4
)
 
+


    
scale_color_identity
(
)
 
+
 
coord_equal
(
)
 
+
 
theme_void
(
)
