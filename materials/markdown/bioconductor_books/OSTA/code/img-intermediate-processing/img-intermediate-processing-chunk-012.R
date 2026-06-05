spe
$
in_tissue
 
<-
 
1
; 
spe
$
x_centroid
 
<-
 
spe
$
y_centroid
 
<-
 
NULL


lapply
(
c
(
"Label"
, 
"Leiden"
, 
"Banksy"
)
, \
(
.
)
 
{


    
plotCoords
(
spe
, annotate
=
.
, point_size 
=
 
0.1
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
