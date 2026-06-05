# retrieve single-cell reference from OSF repo


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




# replace problematic characters


table
(
sce
$
Level1
 
<-
 
gsub
(
"\\s"
, 
"\\."
, 
sce
$
Level1
)
)
