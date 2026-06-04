plot
(
librarySizeFactors
(sce
.416
b), 
sizeFactors
(sce
.416
b), 
pch=
16
,


    
xlab=
"Library size factors"
, 
ylab=
"Deconvolution factors"
, 


    
col=
c
(
"black"
, 
"red"
)[
grepl
(
"induced"
, sce
.416
b
$
phenotype)
+
1
],


    
log=
"xy"
)
