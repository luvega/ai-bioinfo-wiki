pal_lv1
 
<-
 
unname
(
pals
::
trubetskoy
(
)
)


pal_lv0
 
<-
 
c
(
"gold"
, 
"turquoise"
, 
"deeppink"
, 
"navy"
)


plotSpatialFeature
(
sfe
[
, 
sfe
$
roi
]
, 


    features
=
"Level1"
, colGeometryName
=
"cellseg"
)
 
+
 


    
scale_fill_manual
(
values
=
pal_lv1
)
 
+


plotSpatialFeature
(
sfe
[
, 
sfe
$
roi
]
, 


    features
=
"Level0"
, colGeometryName
=
"cellseg"
)
 
+
 


    
scale_fill_manual
(
values
=
pal_lv0
)
 
+


plot_layout
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
ggplot2
::
unit
(
.5
, 
"lines"
)
)
