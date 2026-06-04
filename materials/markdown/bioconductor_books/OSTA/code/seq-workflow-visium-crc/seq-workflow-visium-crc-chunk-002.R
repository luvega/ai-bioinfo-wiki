# retrieve dataset from OSF repo


id
 
<-
 
"Visium_HumanColon_Oliveira"


pa
 
<-
 
OSTA.data_load
(
id
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
