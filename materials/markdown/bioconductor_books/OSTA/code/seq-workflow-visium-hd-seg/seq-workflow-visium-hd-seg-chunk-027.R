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


    colGeometryName
=
"cellseg"
, 


    features
=
"log_sum"
)
 
+


    
ggtitle
(
"log-library size"
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


    colGeometryName
=
"cellseg"
, 


    features
=
"subsets_mt_percent"
)
 
+


    
ggtitle
(
"% mitochondrial"
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
plot.title
=
element_text
(
hjust
=
0.5
)
)
 
&


    
scale_fill_gradientn
(
NULL
, colors
=
pals
::
jet
(
)
)
