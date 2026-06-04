gene.data <-
 
rtracklayer
::
import
(mm10.gtf)




# Cleaning up the object.


gene.data <-
 
gene.data[gene.data
$
type
==
"gene"
]


names
(gene.data) <-
 
gene.data
$
gene_id


is.gene.related <-
 
grep
(
"gene_"
, 
colnames
(
mcols
(gene.data)))


mcols
(gene.data) <-
 
mcols
(gene.data)[,is.gene.related]




rowRanges
(sce) <-
 
gene.data[
rownames
(sce)]


rowRanges
(sce)[
1
:
10
,]
