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
(sce.mess
$
sum, 
sizeFactors
(sce.mess), 
log =
 
"xy"
, 
pch=
16
,


     
xlab =
 
"Library size (millions)"
, 
ylab =
 
"Size factor"
,


     
col =
 
ifelse
(sce.mess
$
phenotype 
==
 "naive"
, 
"black"
, 
"grey"
))




spike.sf <-
 
librarySizeFactors
(
altExp
(sce.mess, 
"ERCC"
))


plot
(
sizeFactors
(sce.mess), spike.sf, 
log =
 
"xy"
, 
pch=
16
,


     
ylab =
 
"Spike-in size factor"
, 
xlab =
 
"Deconvolution size factor"
,


     
col =
 
ifelse
(sce.mess
$
phenotype 
==
 "naive"
, 
"black"
, 
"grey"
))
