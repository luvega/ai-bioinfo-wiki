pcs
 
<-
 
reducedDim
(
spe
, 
"PCA"
)


pcs
 
<-
 
pcs
[
, 
seq_len
(
4
)
]


lapply
(
colnames
(
pcs
)
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
 
pcs
[
, 
.
]


    
plotCoords
(
spe
, annotate 
=
 
.
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
 
coord_equal
(
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
, n.breaks 
=
 
3
)
 
&
 


    
theme_void
(
)
 
&
 
theme
(


        plot.title 
=
 
element_text
(
hjust 
=
 
0.5
)
, 


        legend.key.width 
=
 
unit
(
0.2
, 
"lines"
)
, 


        legend.key.height 
=
 
unit
(
0.8
, 
"lines"
)
)


##  Coordinate system already present.


##  ℹ Adding new coordinate system, which will replace the existing one.


##  Coordinate system already present.


##  ℹ Adding new coordinate system, which will replace the existing one.


##  Coordinate system already present.


##  ℹ Adding new coordinate system, which will replace the existing one.


##  Coordinate system already present.


##  ℹ Adding new coordinate system, which will replace the existing one.


##  Scale for colour is already present.


##  Adding another scale for colour, which will replace the existing scale.


##  Scale for colour is already present.


##  Adding another scale for colour, which will replace the existing scale.


##  Scale for colour is already present.


##  Adding another scale for colour, which will replace the existing scale.


##  Scale for colour is already present.


##  Adding another scale for colour, which will replace the existing scale.
