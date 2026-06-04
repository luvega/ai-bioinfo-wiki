pcs
 
<-
 
reducedDim
(
spe
, 
"PCA"
)


colData
(
spe
)
[
colnames
(
pcs
)
]
 
<-
 
pcs


lapply
(
colnames
(
pcs
)
[
seq_len
(
6
)
]
, 


    \
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
 
+


    
scale_color_gradientn
(
.
, colors
=
pals
::
jet
(
)
)
)
 
|>


    
wrap_plots
(
nrow
=
2
)
 
&
 
theme
(


        plot.title
=
element_blank
(
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
