lapply
(


    
c
(
"anno"
, 
"RCTD"
, 
"RCTD_no_stroma"
)
, 


    \
(
.
)
 
plotCoords
(
vis
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
1
)
 
&


    
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
 
&


    
scale_color_manual
(
values
=
unname
(
pals
::
trubetskoy
(
)
)
)
