# retrieve CosMx dataset from OSF repo


id
 
<-
 
"CosMx1k_MouseBrain2"


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


cos
 
<-
 
readCosmxSXE
(
td
, addTx
=
FALSE
)


# prepare data for 'SpaceTrooper'


cos
 
<-
 
updateCosmxSPE
(
cos
, 
td
, sampleName
=
"CosMx"
)


cos
 
<-
 
readAndAddPolygonsToSPE
(
cos
)


cos
$
in_tissue
 
<-
 
TRUE


cos
