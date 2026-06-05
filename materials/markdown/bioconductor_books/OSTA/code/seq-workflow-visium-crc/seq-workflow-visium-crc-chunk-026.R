# retrieve dataset from OSF repo


id
 
<-
 
"Chromium_HumanColon_Oliveira"


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
