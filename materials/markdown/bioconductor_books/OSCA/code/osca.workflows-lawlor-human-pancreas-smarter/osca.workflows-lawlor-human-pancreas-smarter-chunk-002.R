library
(AnnotationHub)


edb <-
 
AnnotationHub
()[[
"AH73881"
]]


anno <-
 
select
(edb, 
keys=
rownames
(sce.lawlor), 
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
(sce.lawlor) <-
 
anno[
match
(
rownames
(sce.lawlor), anno[,
1
]),
-
1
]
