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


# subset cells from same patient


sce
 
<-
 
sce
[
, 
grepl
(
"P2"
, 
sce
$
Patient
)
]


# realize count matrix


assay
(
sce
)
 
<-
 
as
(
assay
(
sce
)
, 
"dgCMatrix"
)


# log-library size normalization


sce
 
<-
 
logNormCounts
(
sce
)
