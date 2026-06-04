library
(AnnotationHub)


ens.hs.v97 <-
 
AnnotationHub
()[[
"AH73881"
]]


anno <-
 
select
(ens.hs.v97, 
keys=
rownames
(sce.mess), 


    
keytype=
"GENEID"
, 
columns=
c
(
"SYMBOL"
))


rowData
(sce.mess) <-
 
anno[
match
(
rownames
(sce.mess), anno
$
GENEID),]
