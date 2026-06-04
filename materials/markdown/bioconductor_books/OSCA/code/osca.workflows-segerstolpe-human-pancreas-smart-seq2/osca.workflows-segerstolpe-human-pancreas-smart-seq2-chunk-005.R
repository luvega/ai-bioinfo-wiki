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
