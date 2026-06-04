# import into R (takes ~1 min)


gtf
 
<-
 
rtracklayer
::
import
(
gtf_cache
)




# subset to genes only


gtf
 
<-
 
gtf
[
gtf
$
type
 
==
 
"gene"
]




# remove the .x part of the gene IDs


gtf
$
gene_id
 
<-
 
gsub
(
"\\..*"
, 
""
, 
gtf
$
gene_id
)




# set the names to be the gene IDs


names
(
gtf
)
 
<-
 
gtf
$
gene_id




# match the genes


match_genes
 
<-
 
match
(
rowData
(
spe
)
$
gene_id
, 
gtf
$
gene_id
)


table
(
is.na
(
match_genes
)
)
