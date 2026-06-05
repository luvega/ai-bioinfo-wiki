label <-
 "Mesenchyme"


current <-
 
summed[,label
==
summed
$
celltype.mapped]




# Creating up a DGEList object for use in edgeR:


library
(edgeR)


y <-
 
DGEList
(
counts
(current), 
samples=
colData
(current))


y
