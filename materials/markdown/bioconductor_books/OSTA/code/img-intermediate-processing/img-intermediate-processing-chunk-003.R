# get annotations from 'BiocFileCache'


# (data has been retrieved already)


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
, 
"annotation.csv"
, exdir
=
td
)


df
 
<-
 
read.csv
(
list.files
(
td
, full.names
=
TRUE
)
)


# add annotations as cell metadata


cs
 
<-
 
match
(
spe
$
cell_id
, 
df
$
Barcode
)


spe
$
Label
 
<-
 
df
$
Annotation
[
cs
]
