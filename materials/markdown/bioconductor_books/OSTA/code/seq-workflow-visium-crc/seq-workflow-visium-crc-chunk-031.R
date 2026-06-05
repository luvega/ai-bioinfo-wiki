# scale weights such that they sum to 1


ws
 
<-
 
assay
(
res
)


ws
 
<-
 
sweep
(
ws
, 
2
, 
colSums
(
ws
)
, 
`/`
)


# add proportion estimates as metadata


ws
 
<-
 
data.frame
(
t
(
as.matrix
(
ws
)
)
)


colData
(
spe
)
[
names
(
ws
)
]
 
<-
 
ws
[
colnames
(
spe
)
, 
]
