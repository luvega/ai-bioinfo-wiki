ggplot
(
gg
, 
aes
(
date
, 
n
, col
=
biocViews
)
)
 
+
 


    
geom_line
(
linewidth
=
0.8
)
 
+


    
geom_smooth
(
data
=
filter
(
gg
, 
n
 
>=
 
5
)
, 


        method
=
"lm"
, se
=
FALSE
, linewidth
=
1
)
 
+


    
scale_x_date
(
date_breaks 
=
 
"1 year"
, date_labels 
=
 
"%Y"
)
 
+


    
labs
(
x
=
NULL
, y
=
"# packages"
)
 
+


    
theme_bw
(
)
 
+
 
theme
(


        aspect.ratio
=
1
, 


        panel.grid.minor
=
element_blank
(
)
,


        axis.text.x
=
element_text
(
angle
=
45
, hjust
=
1
)
)
