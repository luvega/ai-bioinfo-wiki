# add information used by spatialLIBD


rowData
(
spe
)
$
gene_search
 
<-
 
with
(
rowData
(
spe
)
, 


    
paste
(
gene_name
, 
gene_id
, sep
=
"; "
)
)




# compute chrM expression and chrM expression ratio


is_mito
 
<-
 
which
(
seqnames
(
spe
)
 
==
 
"chrM"
)


spe
$
expr_chrM
 
<-
 
colSums
(
counts
(
spe
)
[
is_mito
, , drop
=
FALSE
]
)


spe
$
expr_chrM_ratio
 
<-
 
spe
$
expr_chrM
 
/
 
spe
$
sum_umi
