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
(sce.grun.hsc), 


    
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
(sce.grun.hsc) <-
 
anno[
match
(
rownames
(sce.grun.hsc), anno
$
GENEID),]
