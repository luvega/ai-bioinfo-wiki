markers <-
 
findMarkers
(sce.grun.hsc, 
test.type=
"wilcox"
, 
direction=
"up"
,


    
row.data=
rowData
(sce.grun.hsc)[,
"SYMBOL"
,
drop=
FALSE
])
