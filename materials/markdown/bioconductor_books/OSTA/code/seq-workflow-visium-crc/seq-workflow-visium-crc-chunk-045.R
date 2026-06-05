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
 


# use ensembl identifiers as feature names


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


# build per-spot gene rankings


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


# calculate AUC for each gene set in each spot


auc
 
<-
 
AUCell_calcAUC
(
geneSets
=
gs
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


# add results as spot metadata


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
 
res
 
<-
 
t
(
assay
(
auc
)
)
