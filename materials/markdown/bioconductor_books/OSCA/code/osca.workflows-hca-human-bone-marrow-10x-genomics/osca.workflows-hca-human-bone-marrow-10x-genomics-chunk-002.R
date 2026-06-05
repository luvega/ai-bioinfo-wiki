library
(EnsDb.Hsapiens.v86)


rowData
(sce.bone)
$
Chr <-
 
mapIds
(EnsDb.Hsapiens.v86, 
keys=
rownames
(sce.bone),


    
column=
"SEQNAME"
, 
keytype=
"GENEID"
)




library
(scater)


rownames
(sce.bone) <-
 
uniquifyFeatureNames
(
rowData
(sce.bone)
$
ID,


    
names =
 
rowData
(sce.bone)
$
Symbol)
