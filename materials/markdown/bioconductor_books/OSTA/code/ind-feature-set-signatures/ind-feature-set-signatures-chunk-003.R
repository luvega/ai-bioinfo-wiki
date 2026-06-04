# retrieve hallmark gene sets from 'MSigDB'


db
 
<-
 
msigdbr
(
species
=
"Homo sapiens"
, collection
=
"H"
)


gs
 
<-
 
split
(
db
$
ensembl_gene
, 
db
$
gs_name
)


# simplify gene set identifiers


names
(
gs
)
 
<-
 
tolower
(
gsub
(
"HALLMARK_"
, 
""
, 
names
(
gs
)
)
)


# how many sets?


length
(
gs
)
