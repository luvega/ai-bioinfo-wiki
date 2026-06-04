.plt_xy
 
<-
 \
(
spe
, 
col
)
 
{


    
df
 
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


    
aes
 
<-
 
if
 
(
is.numeric
(
df
[[
col
]
]
)
)
 
{


        
theme
(


            legend.key.height
=
unit
(
1
, 
"lines"
)
, 


            legend.key.width
=
unit
(
0.5
, 
"lines"
)
)


    
}
 
else
 
{


        
list
(


            
theme
(
legend.key.size
=
unit
(
0
, 
"lines"
)
)
,


            
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
alpha
=
1
, size
=
2
)
)
)
)


    
}


    
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
.data
[[
col
]
]
)
)
 
+


        
coord_equal
(
)
 
+
 
theme_void
(
)
 
+
 
aes
 
+


        
geom_point
(
stroke
=
0
, size
=
1
/
3
)


}
