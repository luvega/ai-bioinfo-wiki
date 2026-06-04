ggplot
(
df
, 
aes
(
sizeFactor
, 
library_size
)
)
 
+
 


    
geom_point
(
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
 
+


    
geom_abline
(
linewidth
=
0.4
, col
=
"blue"
)
 
+
 


    
facet_wrap
(
~
Label
)
 
+


    
labs
(
x
=
"Area-derived factor"
, y
=
"Library size factor"
)
 
+
 


    
ggtitle
(
"Relation between area-derived and library size factors"
)
 
+


    
coord_equal
(
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


        plot.title
=
element_text
(
hjust
=
0.5
)
)
