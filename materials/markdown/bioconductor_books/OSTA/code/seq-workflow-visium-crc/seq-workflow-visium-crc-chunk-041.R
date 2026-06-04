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


# get list of gene symbols, one element per set


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


# simplify set identifiers (drop prefix, use lower case)


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
