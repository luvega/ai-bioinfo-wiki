library
(scuttle)


sce.grun.hsc <-
 
sce.grun.hsc[,sce.grun.hsc
$
protocol
==
"sorted hematopoietic stem cells"
]


sce.grun.hsc <-
 
logNormCounts
(sce.grun.hsc)




set.seed
(
11001
)


library
(scran)


dec.grun.hsc <-
 
modelGeneVarByPoisson
(sce.grun.hsc)
