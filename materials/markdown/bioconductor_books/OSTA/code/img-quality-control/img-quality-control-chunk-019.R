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
shape
=
16
, size
=
0
, alpha
=
0.1
)
 
+
 


        
geom_smooth
(
method
=
"lm"
, col
=
"blue"
)
 
+


        
scale_x_log10
(
)
 
+
 
scale_y_log10
(
)
 
+


        
theme_minimal
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
)


}


.p
(
df_cos
, 
"Area_um"
, 
"total"
)
 
+
 
ggtitle
(
"CosMx"
)
 
+


.p
(
df_xen
, 
"cell_area"
, 
"total_counts"
)
 
+
 
ggtitle
(
"Xenium"
)
