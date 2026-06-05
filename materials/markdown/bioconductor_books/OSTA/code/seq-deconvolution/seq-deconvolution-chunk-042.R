pcr
$
id
 
<-
 
factor
(
pcr
$
id
, 
ids
)


pal
 
<-
 
pals
::
trubetskoy
(
)


ggplot
(
pcr
, 
aes
(
pc
, 
r2
, col
=
id
)
)
 
+


    
geom_line
(
show.legend
=
FALSE
)
 
+
 
geom_point
(
)
 
+


    
scale_color_manual
(
"predictor"
, values
=
unname
(
pal
)
)
 
+


    
scale_x_continuous
(
breaks
=
c
(
1
, 
seq
(
5
, 
20
, 
5
)
)
)
 
+


    
scale_y_continuous
(
limits
=
c
(
0
, 
1
)
, breaks
=
seq
(
0
, 
1
, 
0.2
)
)
 
+


    
labs
(
x
=
"principal component"
, y
=
"coeff. of determination"
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


    
coord_cartesian
(
xlim
=
c
(
1
, 
10
)
)
 
+


    
theme_minimal
(
)
 
+
 
theme
(


      panel.grid.minor
=
element_blank
(
)
,


      legend.key.size
=
unit
(
0
, 
"lines"
)
)
