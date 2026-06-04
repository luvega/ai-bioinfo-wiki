# retrieve dataset from OSF repo


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


# read into 'SpatialExperiment'


xen
 
<-
 
readXeniumSXE
(
td
, addTx
=
FALSE
)


xen
$
sample_id
 
<-
 
"Xenium"


xen
