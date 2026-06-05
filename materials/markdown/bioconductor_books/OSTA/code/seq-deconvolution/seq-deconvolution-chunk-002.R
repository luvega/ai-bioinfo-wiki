# retrieve dataset from OSF repository


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




# read into 'SpatialExperiment'


vis
 
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
)
 
|>
 


    
import
(
)




# retrieve spot annotations & add as metadata


df
 
<-
 
read.csv
(
file.path
(
td
, 
"annotation.csv"
)
)


cs
 
<-
 
match
(
colnames
(
vis
)
, 
df
$
Barcode
)


vis
$
anno
 
<-
 
factor
(
df
$
Annotation
[
cs
]
)




# set gene symbols as feature names


rownames
(
vis
)
 
<-
 
make.unique
(
rowData
(
vis
)
$
Symbol
)


vis
