# add some information used by spatialLIBD


spe
$
key
 
<-
 
paste0
(
spe
$
sample_id
, 
"_"
, 
colnames
(
spe
)
)


spe
$
sum_umi
 
<-
 
colSums
(
counts
(
spe
)
)


spe
$
sum_gene
 
<-
 
colSums
(
counts
(
spe
)
 
>
 
0
)
