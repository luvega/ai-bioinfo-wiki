sce.paul <-
 
sce.paul[,sce.paul
$
Batch_desc
==
"Unsorted myeloid"
]


sce.paul <-
 
logNormCounts
(sce.paul)




set.seed
(
00010010
)


dec.paul <-
 
modelGeneVarByPoisson
(sce.paul)
