# retrieve dataset from OSF repo


id
 
<-
 
"VisiumHD_HumanColon_Oliveira"


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


# read 8um bins into 'SpatialExperiment'


vhd8
 
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
"008"
)
 
|>


    
import
(
)


# use gene symbols as feature names


gs
 
<-
 
rowData
(
vhd8
)
$
Symbol


rownames
(
vhd8
)
 
<-
 
make.unique
(
gs
)


vhd8
