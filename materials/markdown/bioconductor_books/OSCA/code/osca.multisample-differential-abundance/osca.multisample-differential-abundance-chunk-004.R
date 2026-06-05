library
(edgeR)


library
(scater)


# Attaching some column metadata.


extra.info <-
 
colData
(merged)[
match
(
colnames
(abundances), merged
$
sample),]


y.ab <-
 
DGEList
(abundances, 
samples=
extra.info)


y.ab
