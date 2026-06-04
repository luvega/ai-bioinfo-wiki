# Xenium


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


(
xen
 
<-
 
readXeniumSXE
(
td
, addTx
=
FALSE
)
)
