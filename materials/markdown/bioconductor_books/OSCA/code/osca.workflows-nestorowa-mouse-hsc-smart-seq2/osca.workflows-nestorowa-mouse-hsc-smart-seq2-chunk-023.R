markers <-
 
findMarkers
(sce.nest, 
colLabels
(sce.nest), 


    
test.type=
"wilcox"
, 
direction=
"up"
, 
lfc=
0.5
,


    
row.data=
rowData
(sce.nest)[,
"SYMBOL"
,
drop=
FALSE
])
