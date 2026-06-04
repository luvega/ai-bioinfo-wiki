library
(scater)


rownames
(sce.mam) <-
 
uniquifyFeatureNames
(


    
rowData
(sce.mam)
$
Ensembl, 
rowData
(sce.mam)
$
Symbol)




library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


rowData
(sce.mam)
$
SEQNAME <-
 
mapIds
(ens.mm.v97, 
keys=
rowData
(sce.mam)
$
Ensembl,


    
keytype=
"GENEID"
, 
column=
"SEQNAME"
)
