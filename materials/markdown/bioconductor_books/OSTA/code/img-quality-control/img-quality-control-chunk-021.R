ns
 
<-
 
as.data.frame
(


    
table
(
fov
=
cos
$
fov
)
, 


    responseName
=
"n_cells"
)


ggplot
(
ns
, 
aes
(
fov
, 
n_cells
)
)
 
+
 


    
scale_x_discrete
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
max
(
cos
$
fov
)
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
1e3
)
, n.breaks
=
4
)
 
+


    
labs
(
x
=
"field of view (FOV)"
, y
=
"# cells"
)
 
+


    
geom_col
(
fill
=
"grey"
, alpha
=
2
/
3
)
 
+


    
coord_cartesian
(
expand
=
FALSE
)
 
+


    
theme_bw
(
)
