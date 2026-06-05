# retrieve dataset from OSF repository


id
 
<-
 
"Chromium_HumanColon_Oliveira"


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


# read into 'SingleCellExperiment'


sce
 
<-
 
read10xCounts
(
list.files
(
td
, 
"h5$"
, full.names
=
TRUE
)
)


cd
 
<-
 
read.csv
(
list.files
(
td
, 
"cell_meta"
, full.names
=
TRUE
)
)


colData
(
sce
)
 
<-
 
cbind
(
colData
(
sce
)
, 
cd
[
, 
-
1
]
)


table
(
sce
$
Level1
)
 
# tabulate low-res. labels


ncol
(
sce
)
 
# overall number of cells
