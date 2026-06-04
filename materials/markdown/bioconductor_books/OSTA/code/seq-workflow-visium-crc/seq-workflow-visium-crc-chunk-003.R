# read into 'SpatialExperiment'


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
 
import
(
obj
)
)
