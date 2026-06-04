sce.zeisel <-
 
addPerCellQC
(sce.zeisel, 


    
subsets=
list
(
Mt=
rowData
(sce.zeisel)
$
featureType
==
"mito"
))




qc <-
 
quickPerCellQC
(
colData
(sce.zeisel), 


    
sub.fields=
c
(
"altexps_ERCC_percent"
, 
"subsets_Mt_percent"
))


sce.zeisel
$
discard <-
 
qc
$
discard




plotColData
(sce.zeisel, 
x=
"sum"
, 
y=
"subsets_Mt_percent"
, 
colour_by=
"discard"
)
