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
, 


                 
reducedDim
(
spe
, 
"PCA_tx"
)
)


lapply
(
paste0
(
"PC"
, 
seq
(
3
)
)
, \
(
.
)
 
{


    
fd
 
<-
 
df
[
order
(
abs
(
df
[[
.
]
]
)
)
, 
]


    
ggplot
(
fd
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
.
]
]
)
)


}
)
 
|>


    
wrap_plots
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
, stroke
=
0
, size
=
0.2
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
 
&


    
coord_equal
(
)
 
&
 
theme_void
(
)
 
&
 
theme
(


        legend.position
=
"bottom"
,


        legend.key.width
=
unit
(
0.8
, 
"lines"
)
,


        legend.key.height
=
unit
(
0.4
, 
"lines"
)
)
