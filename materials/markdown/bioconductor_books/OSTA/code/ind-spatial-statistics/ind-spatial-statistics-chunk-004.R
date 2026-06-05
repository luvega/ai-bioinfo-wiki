# get gene probes & compute Moran's I for them


idx
 
<-
 
rowData
(
sfe
)
$
Type
 
==
 
"Gene Expression"


length
(
geneProbes
 
<-
 
rowData
(
sfe
)
[
idx
, 
"Symbol"
]
)
