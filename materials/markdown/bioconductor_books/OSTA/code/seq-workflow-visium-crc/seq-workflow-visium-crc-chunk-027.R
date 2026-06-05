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


# tabulate subpopulations


table
(
sce
$
Level1
)
