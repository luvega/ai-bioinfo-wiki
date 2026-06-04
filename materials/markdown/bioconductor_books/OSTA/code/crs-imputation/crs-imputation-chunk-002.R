id
 
<-
 
"Xenium_HumanBreast1_Janesick"


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


spe
 
<-
 
readXeniumSXE
(
td
, addTx
=
FALSE
)


spe
$
sample_id
 
<-
 
"Xenium"


dim
(
spe
)
