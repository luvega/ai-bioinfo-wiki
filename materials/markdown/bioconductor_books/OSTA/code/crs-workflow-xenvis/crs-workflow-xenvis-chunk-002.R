# Visium


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


    images
=
"lowres"
, 


    format
=
"h5"
)


(
vis
 
<-
 
import
(
obj
)
)
