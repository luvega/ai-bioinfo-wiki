lapply
(
top
, \
(
.
)
 
{


    
spe
[[
.
]
]
 
<-
 
scale
(
spe
[[
.
]
]
)
 
# scaling


    
plotCoords
(
spe
, annotate
=
.
)
 
# plotting


}
)
 
|>
 


    
# arrange & prettify


    
wrap_plots
(
nrow
=
2
, guides
=
"collect"
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
,


        oob
=
scales
::
squish
, 


        limits
=
c
(
-
2.5
, 
2.5
)
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
