#--- loading ---#


library
(scRNAseq)


sce.seger <-
 
SegerstolpePancreasData
()




#--- gene-annotation ---#


library
(AnnotationHub)


edb <-
 
AnnotationHub
()[[
"AH73881"
]]


symbols <-
 
rowData
(sce.seger)
$
symbol


ens.id <-
 
mapIds
(edb, 
keys=
symbols, 
keytype=
"SYMBOL"
, 
column=
"GENEID"
)


ens.id <-
 
ifelse
(
is.na
(ens.id), symbols, ens.id)




# Removing duplicated rows.


keep <-
 
!
duplicated
(ens.id)


sce.seger <-
 
sce.seger[keep,]


rownames
(sce.seger) <-
 
ens.id[keep]




#--- sample-annotation ---#


emtab.meta <-
 
colData
(sce.seger)[,
c
(
"cell type"
, 
"disease"
,


    
"individual"
, 
"single cell well quality"
)]


colnames
(emtab.meta) <-
 
c
(
"CellType"
, 
"Disease"
, 
"Donor"
, 
"Quality"
)


colData
(sce.seger) <-
 
emtab.meta




sce.seger
$
CellType <-
 
gsub
(
" cell"
, 
""
, sce.seger
$
CellType)


sce.seger
$
CellType <-
 
paste0
(


    
toupper
(
substr
(sce.seger
$
CellType, 
1
, 
1
)),


    
substring
(sce.seger
$
CellType, 
2
))




#--- quality-control ---#


low.qual <-
 
sce.seger
$
Quality 
==
 "OK, filtered"




library
(scater)


stats <-
 
perCellQCMetrics
(sce.seger)


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
"altexps_ERCC_percent"
,


    
batch=
sce.seger
$
Donor,


    
subset=
!
sce.seger
$
Donor 
%in%
 
c
(
"H6"
, 
"H5"
))




sce.seger <-
 
sce.seger[,
!
(qc
$
discard 
|
 
low.qual)]




#--- normalization ---#


library
(scran)


clusters <-
 
quickCluster
(sce.seger)


sce.seger <-
 
computeSumFactors
(sce.seger, 
clusters=
clusters)


sce.seger <-
 
logNormCounts
(sce.seger) 




#--- variance-modelling ---#


for.hvg <-
 
sce.seger[,
librarySizeFactors
(
altExp
(sce.seger)) 
>
 
0
 
&
 
sce.seger
$
Donor
!=
"H1"
]


dec.seger <-
 
modelGeneVarWithSpikes
(for.hvg, 
"ERCC"
, 
block=
for.hvg
$
Donor)


chosen.hvgs <-
 
getTopHVGs
(dec.seger, 
n=
2000
)




#--- dimensionality-reduction ---#


library
(BiocSingular)


set.seed
(
101011001
)


sce.seger <-
 
runPCA
(sce.seger, 
subset_row=
chosen.hvgs, 
ncomponents=
25
)


sce.seger <-
 
runTSNE
(sce.seger, 
dimred=
"PCA"
)




#--- clustering ---#


library
(bluster)


clust.out <-
 
clusterRows
(
reducedDim
(sce.seger, 
"PCA"
), 
NNGraphParam
(), 
full=
TRUE
)


snn.gr <-
 
clust.out
$
objects
$
graph


colLabels
(sce.seger) <-
 
clust.out
$
clusters




#--- data-integration ---#


library
(batchelor)




set.seed
(
10001010
)


corrected <-
 
fastMNN
(sce.seger, 
batch=
sce.seger
$
Donor, 
subset.row=
chosen.hvgs)




set.seed
(
10000001
)


corrected <-
 
runTSNE
(corrected, 
dimred=
"corrected"
)




colLabels
(corrected) <-
 
clusterRows
(
reducedDim
(corrected, 
"corrected"
), 
NNGraphParam
())




tab <-
 
table
(
Cluster=
colLabels
(corrected), 
Donor=
corrected
$
batch)


tab
