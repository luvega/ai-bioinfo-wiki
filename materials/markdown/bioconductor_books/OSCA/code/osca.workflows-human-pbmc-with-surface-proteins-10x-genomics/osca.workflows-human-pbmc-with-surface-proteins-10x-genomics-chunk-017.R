par
(
mfrow=
c
(
1
,
2
))


plot
(
librarySizeFactors
(sce.pbmc), 
sizeFactors
(sce.pbmc), 
pch=
16
,


    
xlab=
"Library size factors"
, 
ylab=
"Deconvolution factors"
, 


    
main=
"Gene expression"
, 
log=
"xy"
)


plot
(
librarySizeFactors
(
altExp
(sce.pbmc)), 
sizeFactors
(
altExp
(sce.pbmc)), 
pch=
16
,


    
xlab=
"Library size factors"
, 
ylab=
"Median-based factors"
, 


    
main=
"Antibody capture"
, 
log=
"xy"
)
