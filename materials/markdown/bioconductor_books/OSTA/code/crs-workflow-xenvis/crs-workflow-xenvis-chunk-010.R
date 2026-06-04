df
 
<-
 
data.frame
(
spatialCoords
(
vis
)
)


fd
 
<-
 
data.frame
(
spatialCoords
(
xen
)
)


ggplot
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
 
+


    
geom_point
(
aes
(
x
, 
y
)
, 
df
, col
=
"grey"
, stroke
=
0
, size
=
1
)
 
+


    
geom_point
(
aes
(
x
, 
y
)
, 
fd
, col
=
"blue"
, stroke
=
0
, size
=
0.1
)
