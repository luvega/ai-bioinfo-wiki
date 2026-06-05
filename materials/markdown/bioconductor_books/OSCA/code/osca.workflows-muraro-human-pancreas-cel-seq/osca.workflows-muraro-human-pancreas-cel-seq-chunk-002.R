library
(AnnotationHub)


edb <-
 
AnnotationHub
()[[
"AH73881"
]]


gene.symb <-
 
sub
(
"__chr.*$"
, 
""
, 
rownames
(sce.muraro))


gene.ids <-
 
mapIds
(edb, 
keys=
gene.symb, 


    
keytype=
"SYMBOL"
, 
column=
"GENEID"
)




# Removing duplicated genes or genes without Ensembl IDs.


keep <-
 
!
is.na
(gene.ids) 
&
 
!
duplicated
(gene.ids)


sce.muraro <-
 
sce.muraro[keep,]


rownames
(sce.muraro) <-
 
gene.ids[keep]
