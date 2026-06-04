# retrieve data from OSF repo


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




# read into 'SpatialExperiment'


seg
 
<-
 
file.path
(
td
, 
"segmented_outputs"
)


spe
 
<-
 
TENxVisiumHD
(


    format
=
"h5"
, 


    images
=
"lowres"
,


    segmented_outputs
=
seg
)
 
|>


    
import
(
)




# make gene symbols unique


gs
 
<-
 
rowData
(
spe
)
$
Symbol


rownames
(
spe
)
 
<-
 
make.unique
(
gs
)




# needed for 'ggspavis'


spe
$
in_tissue
 
<-
 
TRUE
