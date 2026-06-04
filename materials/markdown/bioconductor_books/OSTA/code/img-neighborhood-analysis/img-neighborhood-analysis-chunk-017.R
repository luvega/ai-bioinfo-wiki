pal_k
 
<-
 
unname
(
pals
::
trubetskoy
(
nlevels
(
df
$
k
)
)
)


pal_c
 
<-
 
c
(
"blue"
, 
"cyan"
, 
"gold"
, 
"magenta"
, 
"maroon"
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
k
)
)
 
+
 


    
scale_color_manual
(
values
=
pal_k
)
 
+


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
ctx
)
)
 
+
 


    
scale_color_manual
(
values
=
pal_c
)
 
+


plot_layout
(
nrow
=
1
)
 
&


    
geom_point
(
shape
=
16
, size
=
0
)
 
&


    
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
 
&


    
theme_xy
 
&
 
theme
(
legend.key.size
=
unit
(
0.5
, 
"lines"
)
)
