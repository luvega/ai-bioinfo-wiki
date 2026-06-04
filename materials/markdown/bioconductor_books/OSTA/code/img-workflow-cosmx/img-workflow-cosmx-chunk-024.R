sub
$
SingleR_label
 
<-
 
factor
(
pred
$
pruned.labels
)




nk
 
<-
 
nlevels
(
sub
$
SingleR_label
)


pal
 
<-
 
hcl.colors
(
nk
, 
"Spectral"
)




plotPolygons
(
sub
, 


    colourBy
=
"SingleR_label"
)
 
+


    
scale_fill_manual
(
values
=
pal
)
