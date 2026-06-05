# retrieve top-10 PCs


pcs
 
<-
 
reducedDim
(
vis
, 
"PCA"
)


pcs
 
<-
 
pcs
[
rownames
(
ws
)
, 
seq_len
(
10
)
]


# specify subpopulations & PCs to visualize


var
 
<-
 
c
(
"DCIS1"
, 
"T"
, 
"endo"
)


var
 
<-
 
c
(
var
, 
colnames
(
pcs
)
[
3
:
5
]
)


# visualize deconvolution weights alongside PCs


lapply
(
var
, \
(
.
)
 
{


    
.plt_xy
(


        
cbind
(
ws
, 
pcs
)
, 
vis
, col
=
.
, point_size
=
0.3
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


}
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
