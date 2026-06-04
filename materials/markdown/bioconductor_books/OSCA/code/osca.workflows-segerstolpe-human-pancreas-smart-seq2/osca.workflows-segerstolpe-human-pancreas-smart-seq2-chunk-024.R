summed.beta <-
 
summed[,summed
$
CellType
==
"Beta"
]




library
(edgeR)


y.beta <-
 
DGEList
(
counts
(summed.beta), 
samples=
colData
(summed.beta),


    
genes=
rowData
(summed.beta)[,
"symbol"
,
drop=
FALSE
])


y.beta <-
 
y.beta[
filterByExpr
(y.beta, 
group=
y.beta
$
samples
$
Disease),]


y.beta <-
 
calcNormFactors
(y.beta)




design <-
 
model.matrix
(
~
Disease, y.beta
$
samples)


v.beta <-
 
voomWithQualityWeights
(y.beta, design)


fit.beta <-
 
lmFit
(v.beta)


fit.beta <-
 
eBayes
(fit.beta, 
robust=
TRUE
)




res.beta <-
 
topTable
(fit.beta, 
sort.by=
"p"
, 
n=
Inf
,


    
coef=
"Diseasetype II diabetes mellitus"
)


head
(res.beta)
