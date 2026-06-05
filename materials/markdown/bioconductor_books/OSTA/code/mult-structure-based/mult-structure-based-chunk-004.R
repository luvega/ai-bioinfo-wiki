# subset to 4 randomly selected FOVs


fov
 
<-
 
sample
(
unique
(
spe
$
image_name
)
, 
4
)


sub
 
<-
 
spe
[
, 
spe
$
image_name
 
%in%
 
fov
]


df
 
<-
 
data.frame
(
colData
(
sub
)
, 
spatialCoords
(
sub
)
)


# visualize annotations


ggplot
(
df
, 
aes
(
cell_x
, 
cell_y
, color
=
cell_category
)
)
 
+
 


    
geom_point
(
size
=
0.4
)
 
+
 
facet_wrap
(
~
image_name
, ncol
=
2
)
 
+
 


    
scale_color_manual
(
values
=
unname
(
pals
::
okabe
(
n
=
5
)
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


    
coord_equal
(
)
 
+
 
theme_classic
(
)
