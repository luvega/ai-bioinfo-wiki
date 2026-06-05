# number of unique features


lr
 
<-
 
c
(
db
$
ligand
, 
db
$
receptor
)


ss
 
<-
 
strsplit
(
lr
, 
"-"
)


gs
 
<-
 
sapply
(
ss
, 
.subset
, 
1
)


length
(
unique
(
unlist
(
gs
)
)
)
