library
(org.Hs.eg.db)


gene.ids <-
 
mapIds
(org.Hs.eg.db, 
keys=
rowData
(sce.grun)
$
symbol,


    
keytype=
"SYMBOL"
, 
column=
"ENSEMBL"
)




keep <-
 
!
is.na
(gene.ids) 
&
 
!
duplicated
(gene.ids)


sce.grun <-
 
sce.grun[keep,]


rownames
(sce.grun) <-
 
gene.ids[keep]
