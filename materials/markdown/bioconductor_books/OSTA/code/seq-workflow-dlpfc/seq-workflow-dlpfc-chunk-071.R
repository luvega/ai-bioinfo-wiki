# identify interesting markers for each cluster


interesting
 
<-
 
sapply
(
mgs
, 
function
(
x
)
 
x
$
Top
 
<=
 
5
)


colnames
(
interesting
)
 
<-
 
paste0
(
"gene_interest_"
, 
seq_len
(
length
(
mgs
)
)
)


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
