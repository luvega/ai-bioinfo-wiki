library
(scater)


stats <-
 
perCellQCMetrics
(sce.paul) 


qc <-
 
quickPerCellQC
(stats, 
batch=
sce.paul
$
Plate_ID)




# Detecting batches with unusually low threshold values.


lib.thresholds <-
 
attr
(qc
$
low_lib_size, 
"thresholds"
)[
"lower"
,]


nfeat.thresholds <-
 
attr
(qc
$
low_n_features, 
"thresholds"
)[
"lower"
,]


ignore <-
 
union
(
names
(lib.thresholds)[lib.thresholds 
<
 
100
],


    
names
(nfeat.thresholds)[nfeat.thresholds 
<
 
100
])




# Repeating the QC using only the "high-quality" batches.


qc2 <-
 
quickPerCellQC
(stats, 
batch=
sce.paul
$
Plate_ID,


    
subset=
!
sce.paul
$
Plate_ID 
%in%
 
ignore)


sce.paul <-
 
sce.paul[,
!
qc2
$
discard]
