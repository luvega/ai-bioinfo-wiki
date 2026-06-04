# retrieve dataset from OSF repository


id
 
<-
 
"Xenium_HumanColon_Oliveira"


pa
 
<-
 
OSTA.data_load
(
id
, mol
=
FALSE
)


dir.create
(
td
 
<-
 
tempfile
(
)
)


unzip
(
pa
, exdir
=
td
)


(
spe
 
<-
 
readXeniumSXE
(
td
, addTx
=
FALSE
)
)
