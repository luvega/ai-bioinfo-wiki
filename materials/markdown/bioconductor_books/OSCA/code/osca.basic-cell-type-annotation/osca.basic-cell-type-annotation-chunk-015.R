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
