library
(scater)


rownames
(sce.pbmc) <-
 
uniquifyFeatureNames
(


    
rowData
(sce.pbmc)
$
ID, 
rowData
(sce.pbmc)
$
Symbol)




library
(EnsDb.Hsapiens.v86)


location <-
 
mapIds
(EnsDb.Hsapiens.v86, 
keys=
rowData
(sce.pbmc)
$
ID, 


    
column=
"SEQNAME"
, 
keytype=
"GENEID"
)
