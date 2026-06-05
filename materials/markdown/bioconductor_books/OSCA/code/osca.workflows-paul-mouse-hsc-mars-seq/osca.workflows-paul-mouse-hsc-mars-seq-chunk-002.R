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
(sce.paul), 


    
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
(sce.paul) <-
 
anno[
match
(
rownames
(sce.paul), anno
$
GENEID),]
