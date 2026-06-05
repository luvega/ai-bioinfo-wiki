for.hvg <-
 
sce.seger[,
librarySizeFactors
(
altExp
(sce.seger)) 
>
 
0
 
&
 
sce.seger
$
Donor
!=
"H1"
]


dec.seger <-
 
modelGeneVarWithSpikes
(for.hvg, 
"ERCC"
, 
block=
for.hvg
$
Donor)


chosen.hvgs <-
 
getTopHVGs
(dec.seger, 
n=
2000
)
