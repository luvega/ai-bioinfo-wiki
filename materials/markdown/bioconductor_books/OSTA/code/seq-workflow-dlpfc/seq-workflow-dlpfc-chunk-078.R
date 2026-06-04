# drop the few genes for which we don't have information


spe
 
<-
 
spe
[
!
is.na
(
match_genes
)
, 
]


match_genes
 
<-
 
match_genes
[
!
is.na
(
match_genes
)
]




# keep only some columns from the gtf


mcols
(
gtf
)
 
<-
 
mcols
(
gtf
)
[
, 
c
(
"source"
, 
"type"
, 
"gene_id"
, 
"gene_name"
, 
"gene_type"
)
]




# save the "interesting" columns from our original spe object


interesting
 
<-
 
rowData
(
spe
)
[
, 
grepl
(
"interest"
, 
colnames
(
rowData
(
spe
)
)
)
]




# add gene info to spe object


rowRanges
(
spe
)
 
<-
 
gtf
[
match_genes
]




# add back the "interesting" columns


rowData
(
spe
)
 
<-
 
cbind
(
rowData
(
spe
)
, 
interesting
)




# inspect the gene annotation data we added


head
(
rowRanges
(
spe
)
)
