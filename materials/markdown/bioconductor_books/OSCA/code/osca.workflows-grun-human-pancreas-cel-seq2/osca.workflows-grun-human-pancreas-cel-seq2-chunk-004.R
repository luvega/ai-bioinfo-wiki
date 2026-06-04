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
