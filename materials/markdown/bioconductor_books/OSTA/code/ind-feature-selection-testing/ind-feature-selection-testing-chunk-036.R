top_DEGs
 
<-
 
lapply
(
mgs
, \
(
df
)
 
rownames
(
df
)
[
df
$
Top
 
==
 
1
]
)


top_DEGs
 
<-
 
unique
(
unlist
(
top_DEGs
)
)
[
seq_len
(
6
)
]


top_DESpace
 
<-
 
res_DESpace
$
gene_id
[
seq_len
(
6
)
]
