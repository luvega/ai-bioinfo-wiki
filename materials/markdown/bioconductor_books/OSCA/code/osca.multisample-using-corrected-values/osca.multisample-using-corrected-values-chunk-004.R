#--- loading ---#


library
(scRNAseq)


sce.grun <-
 
GrunPancreasData
()




#--- gene-annotation ---#


library
(org.Hs.eg.db)


gene.ids <-
 
mapIds
(org.Hs.eg.db, 
keys=
rowData
(sce.grun)
$
symbol,


    
keytype=
"SYMBOL"
, 
column=
"ENSEMBL"
)




keep <-
 
!
is.na
(gene.ids) 
&
 
!
duplicated
(gene.ids)


sce.grun <-
 
sce.grun[keep,]


rownames
(sce.grun) <-
 
gene.ids[keep]




#--- quality-control ---#


library
(scater)


stats <-
 
perCellQCMetrics
(sce.grun)




qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
"altexps_ERCC_percent"
,


    
batch=
sce.grun
$
donor,


    
subset=
sce.grun
$
donor 
%in%
 
c
(
"D17"
, 
"D7"
, 
"D2"
))




sce.grun <-
 
sce.grun[,
!
qc
$
discard]




#--- normalization ---#


library
(scran)


set.seed
(
1000
) 
# for irlba. 


clusters <-
 
quickCluster
(sce.grun)


sce.grun <-
 
computeSumFactors
(sce.grun, 
clusters=
clusters)


sce.grun <-
 
logNormCounts
(sce.grun)




#--- variance-modelling ---#


block <-
 
paste0
(sce.grun
$
sample, 
"_"
, sce.grun
$
donor)


dec.grun <-
 
modelGeneVarWithSpikes
(sce.grun, 
spikes=
"ERCC"
, 
block=
block)


top.grun <-
 
getTopHVGs
(dec.grun, 
prop=
0.1
)
