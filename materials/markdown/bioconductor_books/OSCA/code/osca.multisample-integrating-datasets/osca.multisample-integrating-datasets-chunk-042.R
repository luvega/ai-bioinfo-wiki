pbmc8k <-
 
all.sce
$
pbmc8k


dec8k <-
 
all.dec
$
pbmc8k




quick.corrected2 <-
 
quickCorrect
(
`
3k
`
=pbmc3k, 
`
4k
`
=pbmc4k, 
`
8k
`
=pbmc8k,


   
precomputed=
list
(dec3k, dec4k, dec8k),


   
PARAM=
FastMnnParam
(
BSPARAM=
BiocSingular
::
RandomParam
(), 
auto.merge=
TRUE
))




quick.sce2 <-
 
quick.corrected2
$
corrected




set.seed
(
00101010
)


quick.sce2 <-
 
runTSNE
(quick.sce2, 
dimred=
"corrected"
)


plotTSNE
(quick.sce2, 
colour_by=
"batch"
)
