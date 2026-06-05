library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


rowData
(sce
.416
b)
$
ENSEMBL <-
 
rownames
(sce
.416
b)


rowData
(sce
.416
b)
$
SYMBOL <-
 
mapIds
(ens.mm.v97, 
keys=
rownames
(sce
.416
b),


    
keytype=
"GENEID"
, 
column=
"SYMBOL"
)


rowData
(sce
.416
b)
$
SEQNAME <-
 
mapIds
(ens.mm.v97, 
keys=
rownames
(sce
.416
b),


    
keytype=
"GENEID"
, 
column=
"SEQNAME"
)




library
(scater)


rownames
(sce
.416
b) <-
 
uniquifyFeatureNames
(
rowData
(sce
.416
b)
$
ENSEMBL, 


    
rowData
(sce
.416
b)
$
SYMBOL)
