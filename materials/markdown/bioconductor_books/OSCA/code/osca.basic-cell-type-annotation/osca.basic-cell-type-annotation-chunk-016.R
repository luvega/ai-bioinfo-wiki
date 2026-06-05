# Converting to FPKM for a more like-for-like comparison to UMI counts.


# However, results are often still good even when this step is skipped.


library
(AnnotationHub)


hs.db <-
 
AnnotationHub
()[[
"AH73881"
]]


hs.exons <-
 
exonsBy
(hs.db, 
by=
"gene"
)


hs.exons <-
 
reduce
(hs.exons)


hs.len <-
 
sum
(
width
(hs.exons))




library
(scuttle)


available <-
 
intersect
(
rownames
(sce.seger), 
names
(hs.len))


fpkm.seger <-
 
calculateFPKM
(sce.seger[available,], hs.len[available])




pred.seger <-
 
SingleR
(
test=
fpkm.seger, 
ref=
sce.muraro, 


    
labels=
sce.muraro
$
label, 
de.method=
"wilcox"
)


table
(pred.seger
$
labels)
