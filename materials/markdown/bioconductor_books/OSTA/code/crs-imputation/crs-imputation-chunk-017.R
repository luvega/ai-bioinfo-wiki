# plot R2 before vs. after


ggplot
(
df
, 
aes
(
pc
, 
r2
, col
=
x
)
)
 
+
 


    
facet_wrap
(
~
id
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
NA
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
"predictor"
, override.aes
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
20
)
)
 
+


    
theme_bw
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
