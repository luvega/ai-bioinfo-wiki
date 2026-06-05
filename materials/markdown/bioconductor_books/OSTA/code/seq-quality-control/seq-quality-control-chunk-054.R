# filter genes: remove zeros


ex
 
<-
 
rowSums
(
counts
(
spe_save
)
)
 
!=
 
0


spe_save
 
<-
 
spe_save
[
ex
, 
]


# save object


saveRDS
(
spe_save
, 
"seq-spe_qc.rds"
)
