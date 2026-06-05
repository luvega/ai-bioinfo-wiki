top.markers <-
 
rownames
(marker.set)[marker.set
$
Top 
<=
 
10
]


plotHeatmap
(sce
.416
b, 
features=
top.markers, 
order_columns_by=
"label"
,


    
colour_columns_by=
c
(
"label"
, 
"block"
, 
"phenotype"
),


    
center=
TRUE
, 
symmetric=
TRUE
, 
zlim=
c
(
-
5
, 
5
))
