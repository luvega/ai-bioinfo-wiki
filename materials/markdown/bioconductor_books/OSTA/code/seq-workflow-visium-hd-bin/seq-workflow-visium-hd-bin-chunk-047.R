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


# read into `SingleCellExperiment`


fs
 
<-
 
list.files
(
td
, full.names
=
TRUE
)


h5
 
<-
 
grep
(
"h5$"
, 
fs
, value
=
TRUE
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


# add cell metadata


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


# use gene symbols as feature names


gs
 
<-
 
rowData
(
sce
)
$
Symbol


rownames
(
sce
)
 
<-
 
make.unique
(
gs
)


# exclude cells deemed to be of low-quality


sce
 
<-
 
sce
[
, 
sce
$
QCFilter
 
==
 
"Keep"
]


# subset cells from same patient


sce
 
<-
 
sce
[
, 
grepl
(
"P2"
, 
sce
$
Patient
)
]


sce
