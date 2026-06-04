# subset to selected FOVs


subIslets
 
<-
 
allIslets
[
allIslets
$
image_name
 
%in%
 
fov
, 
]


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
 
+


    
geom_sf
(
 
# geom for structure outlines


        data
=
subIslets
, inherit.aes
=
FALSE
, 


        color
=
"red"
, fill
=
NA
, linewidth
=
1
)
