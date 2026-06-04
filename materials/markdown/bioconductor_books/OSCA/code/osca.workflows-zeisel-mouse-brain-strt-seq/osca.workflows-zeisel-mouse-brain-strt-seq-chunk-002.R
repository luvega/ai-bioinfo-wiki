library
(org.Mm.eg.db)


rowData
(sce.zeisel)
$
Ensembl <-
 
mapIds
(org.Mm.eg.db, 


    
keys=
rownames
(sce.zeisel), 
keytype=
"SYMBOL"
, 
column=
"ENSEMBL"
)
