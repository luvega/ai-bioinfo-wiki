cd
 
<-
 
data.frame
(
colData
(
spe
)
, 
spatialCoords
(
spe
)
)




mx
 
<-
 
logcounts
(
spe
)
[
ord
[
1
:
10
]
, 
]


df_ls
 
<-
 
cbind
(
cd
, 
as.matrix
(
t
(
mx
)
)
)




mx
 
<-
 
assay
(
spe
, 
"normalized_by_area"
)
[
ord
[
1
:
10
]
, 
]


df_area
 
<-
 
cbind
(
cd
, 
as.matrix
(
t
(
mx
)
)
)




p1
 
<-
 
ggplot
(
df_ls
)
 
+
 
labs
(
title
=
"Library size normalization"
)


p2
 
<-
 
ggplot
(
df_area
)
 
+
 
labs
(
title
=
"Area normalization"
)
 




(
p1
 
+
 
p2
)
 
&
 


    
geom_point
(


        
aes
(
x_centroid
, 
y_centroid
, col
=
EPCAM
)
, 


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
 
&


    
scale_color_viridis_c
(
)
 
&
 
coord_equal
(
)
 
&
 


    
theme_void
(
)
 
&
 
theme
(
legend.position
=
"bottom"
)
