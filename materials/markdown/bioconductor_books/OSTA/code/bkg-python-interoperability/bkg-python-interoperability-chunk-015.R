id
 
<-
 
"Visium_HumanBreast_Janesick"


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


obj
 
<-
 
TENxVisium
(


    spacerangerOut
=
file.path
(
td
, 
"outs"
)
, 


    format
=
"h5"
, 


    images
=
"lowres"
)


(
spe
 
<-
 
VisiumIO
::
import
(
obj
)
)
