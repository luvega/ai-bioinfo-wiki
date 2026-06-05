df
 
<-
 
data.frame
(
xy
, 
colData
(
spe
)
)


p0
 
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
 


    
geom_point
(
data
=
df
, col
=
"navy"
, shape
=
16
, size
=
0
)
 
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
, col
=
"magenta"
, shape
=
16
, size
=
0
)
 


p1
 
<-
 
p0
 
+
 
geom_point
(


    data
=
df
[
which
(
j
)
[
is_k
]
, 
]
, 


    col
=
"gold"
, shape
=
16
, size
=
0
)
 
+


    
ggtitle
(
"k-nearest neighbors"
)


p2
 
<-
 
p0
 
+
 
geom_point
(


    data
=
df
[
which
(
j
)
[
is_r
]
, 
]
, 


    col
=
"gold"
, shape
=
16
, size
=
0
)
 
+


    
ggtitle
(
"fixed-radius search"
)


(
p1
 
|
 
p2
)
 
+
 
plot_layout
(
nrow
=
1
)
 
&
 
theme_xy
