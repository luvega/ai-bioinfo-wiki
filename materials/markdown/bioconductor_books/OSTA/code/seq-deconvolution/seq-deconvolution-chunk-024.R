.plt_xy
 
<-
 \
(
ws
, 
vis
, 
col
, 
point_size
)
 
{


    
xy
 
<-
 
spatialCoords
(
vis
)
[
rownames
(
ws
)
, 
]


    
colnames
(
xy
)
 
<-
 
c
(
"x"
, 
"y"
)


    
df
 
<-
 
cbind
(
ws
, 
xy
)


    
ggplot
(
df
, 
aes
(
x
, 
y
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
 


        
geom_point
(
size
=
point_size
)


}




.plt_decon
 
<-
 \
(
ws
, 
vis
)
 
{


    
ps
 
<-
 
lapply
(
names
(
ws
)
, \
(
.
)
 
.plt_xy
(
ws
, 
vis
, col
=
.
, point_size
=
0.3
)
)


    
ps
 
|>
 
wrap_plots
(
nrow
=
3
)
 
&
 
theme
(


        legend.key.width
=
unit
(
0.5
, 
"lines"
)
,


        legend.key.height
=
unit
(
1
, 
"lines"
)
)
 
&


        
scale_color_gradientn
(
colors
=
pals
::
jet
(
)
)


}
