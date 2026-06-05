library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


anno <-
 
select
(ens.mm.v97, 
keys=
rownames
(sce.nest), 


    
keytype=
"GENEID"
, 
columns=
c
(
"SYMBOL"
, 
"SEQNAME"
))


rowData
(sce.nest) <-
 
anno[
match
(
rownames
(sce.nest), anno
$
GENEID),]
