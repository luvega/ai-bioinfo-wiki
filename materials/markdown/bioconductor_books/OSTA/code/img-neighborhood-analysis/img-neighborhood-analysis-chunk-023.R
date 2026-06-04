# dependencies


library
(
scider
)


library
(
OSTA.data
)


library
(
SpatialExperimentIO
)


# retrieve data from OSF repo &


# read into 'SpatialExperiment'


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
