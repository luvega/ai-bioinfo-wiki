library
(batchelor)


quick.corrected <-
 
quickCorrect
(pbmc3k, pbmc4k, 


   
precomputed=
list
(dec3k, dec4k),


   
PARAM=
FastMnnParam
(
BSPARAM=
BiocSingular
::
RandomParam
()))




quick.sce <-
 
quick.corrected
$
corrected


quick.sce
