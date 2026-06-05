# realize (sparse) gene expression matrix


mtx
 
<-
 
as
(
logcounts
(
spe
)
, 
"dgCMatrix"
)
 


# use ensembl identifiers as rownames


rownames
(
mtx
)
 
<-
 
rowData
(
spe
)
$
ID


# filter for genes represented in panel


.gs
 
<-
 
lapply
(
gs
, 
intersect
, 
rownames
(
mtx
)
)


# keep only those with at least 5 genes


.gs
 
<-
 
.gs
[
sapply
(
.gs
, 
length
)
 
>=
 
5
]


# build per-cell gene rankings


rnk
 
<-
 
AUCell_buildRankings
(
mtx
, BPPARAM
=
bp
, plotStats
=
FALSE
, verbose
=
FALSE
)


# calculate AUC for each gene set in each cell


auc
 
<-
 
AUCell_calcAUC
(
geneSets
=
.gs
, rankings
=
rnk
, nCores
=
th
, verbose
=
FALSE
)


# add results as cell metadata


colData
(
spe
)
[
rownames
(
auc
)
]
 
<-
 
t
(
assay
(
auc
)
)
