df
 
<-
 
data.frame
(
colData
(
cos
)
)


.p
 
<-
 \
(
df
, 
x
, 
y
)
 
{


    
ggplot
(
df
, 
aes
(
.data
[[
x
]
]
, 
.data
[[
y
]
]
)
)
 
+


        
geom_point
(
color
=
"grey"
, size
=
0
)
 
+


        
geom_smooth
(
)
 
+
 
theme_minimal
(
)
 
+


        
geom_vline
(
xintercept
=
r
, col
=
"red"
)
 
+


        
geom_vline
(
xintercept
=
50
, linetype
=
2
)


}


p1
 
<-
 
.p
(
df
, 
"dist_border"
, 
"total"
)
 
+
 
xlim
(
0
, 
500
)
 
+
 
ylim
(
0
, 
2000
)


p2
 
<-
 
.p
(
df
, 
"dist_border"
, 
"Area_um"
)
 
+
 
xlim
(
0
, 
500
)
 
+
 
ylim
(
0
, 
200
)


p3
 
<-
 
.p
(
df
, 
"dist_border_x"
, 
"log2AspectRatio"
)
 
+
 
xlim
(
0
, 
500
)


p4
 
<-
 
.p
(
df
, 
"dist_border_y"
, 
"log2AspectRatio"
)
 
+
 
xlim
(
0
, 
500
)


(
p1
 
+
 
p2
)
 
/
 
(
p3
 
+
 
p4
)
