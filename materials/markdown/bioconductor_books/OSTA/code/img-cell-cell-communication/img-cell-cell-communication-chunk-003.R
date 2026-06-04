# retrieve LR interaction from CellChatDB


ct
 
<-
 
import
(
"commot"
)


db
 
<-
 
ct
$
pp
$
ligand_receptor_database
(


    species
=
"human"
, 


    database
=
"CellChat"
, 


    signaling_type
=
NULL
)


names
(
db
)
 
<-
 
c
(
"ligand"
, 
"receptor"
, 
"pathway"
, 
"type"
)


head
(
db
)
