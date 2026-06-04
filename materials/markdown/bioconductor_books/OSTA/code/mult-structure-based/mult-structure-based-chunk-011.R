pca
 
<-
 
prcomp
(
t
(
isletMetrics
)
, scale.
=
TRUE
)


autoplot
(
pca
, 


    x
=
1
, y
=
2
, 


    data
=
allIslets
,


    color
=
"patient_stage"
, 


    size
=
2
, 


    loadings
=
TRUE
, 


    loadings.colour
=
"steelblue3"
, 


    loadings.label
=
TRUE
, 


    loadings.label.size
=
3
, 


    loadings.label.repel
=
TRUE
, 


    loadings.label.colour
=
"black"
)
 
+


    
theme_bw
(
)
 
+
 
coord_fixed
(
)
 
+
 


    
scale_color_manual
(
values
=
unname
(
pals
::
tol
(
n
=
3
)
)
)
