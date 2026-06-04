df
 
<-
 
data.frame
(
xy
, 
i
)


p
 
<-
 
ggplot
(
df
, 


    
aes
(
x_centroid
, 
y_centroid
)
)
 
+


    
coord_equal
(
)
 
+
 
theme_void
(
)
 
+
 


    
theme
(
legend.position
=
"none"
)


p
 
+
 
geom_point
(
aes
(
col
=
i
)
, stroke
=
0
, size
=
0.1
)
 
|


p
 
+
 
geom_point
(
data
=
df
[
i
, 
]
, stroke
=
0
, size
=
0.2
)
