dec
.416
b <-
 
modelGeneVarWithSpikes
(sce
.416
b, 
"ERCC"
, 
block=
sce
.416
b
$
block)


chosen.hvgs <-
 
getTopHVGs
(dec
.416
b, 
prop=
0.1
)
