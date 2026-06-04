id
 
<-
 
"Chromium_HumanBreast_Janesick"


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


h5
 
<-
 
file.path
(
td
, 
"filtered_feature_bc_matrix.h5"
)


sce
 
<-
 
read10xCounts
(
h5
, col.names
=
TRUE
)


sce
$
sample_id
 
<-
 
"Chromium"


# set gene symbols as feature names


rownames
(
sce
)
 
<-
 
make.unique
(
rowData
(
sce
)
$
Symbol
)


# retrieve cell type labels


fs
 
<-
 
list.files
(
td
, full.names
=
TRUE
)


csv
 
<-
 
grep
(
"csv$"
, 
fs
, value
=
TRUE
)


cd
 
<-
 
read.csv
(
csv
, row.names
=
1
)


colData
(
sce
)
[
names
(
cd
)
]
 
<-
 
cd
[
colnames
(
sce
)
, 
]


dim
(
sce
)
