library
(AnnotationHub)


edb <-
 
AnnotationHub
()[[
"AH73881"
]]


symbols <-
 
rowData
(sce.seger)
$
symbol


ens.id <-
 
mapIds
(edb, 
keys=
symbols, 
keytype=
"SYMBOL"
, 
column=
"GENEID"
)


ens.id <-
 
ifelse
(
is.na
(ens.id), symbols, ens.id)




# Removing duplicated rows.


keep <-
 
!
duplicated
(ens.id)


sce.seger <-
 
sce.seger[keep,]


rownames
(sce.seger) <-
 
ens.id[keep]
