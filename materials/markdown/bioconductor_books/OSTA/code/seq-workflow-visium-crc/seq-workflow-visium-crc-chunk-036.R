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
 


    
plotCoords
(
spe
, annotate
=
.
)
)
 
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
