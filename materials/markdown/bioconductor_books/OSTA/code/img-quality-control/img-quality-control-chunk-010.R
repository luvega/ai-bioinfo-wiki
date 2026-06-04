flu
 
<-
 
grepv
(
"^Mean"
, 
names
(
colData
(
cos
)
)
)


lapply
(
flu
, \
(
.
)
 
{


    
cos
[[
.
]
]
 
<-
 
asinh
(
cos
[[
.
]
]
/
10
)


    
plotCoords
(
cos
, annotate
=
.
, point_size
=
0
, y_reverse 
=
 
FALSE
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


    
theme
(


        legend.position
=
"bottom"
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
