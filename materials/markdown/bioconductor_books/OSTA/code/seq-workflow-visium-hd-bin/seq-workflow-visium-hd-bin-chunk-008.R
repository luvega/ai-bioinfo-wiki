# read 16um bins into 'SpatialExperiment'


vhd16
 
<-
 
TENxVisiumHD
(


    spacerangerOut
=
td
,


    processing
=
"filtered"
,


    format
=
"h5"
,


    images
=
"lowres"
,


    bin_size
=
"016"
)
 
|>


    
import
(
)


# use symbols as feature names


gs
 
<-
 
rowData
(
vhd16
)
$
Symbol


rownames
(
vhd16
)
 
<-
 
make.unique
(
gs
)


vhd16
