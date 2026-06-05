corr.beta <-
 
corrected[,sce.seger
$
CellType
==
"Beta"
]


corr.beta
$
Donor <-
 
sce.beta
$
Donor


corr.beta
$
Disease <-
 
sce.beta
$
Disease


by.cell <-
 
plotExpression
(corr.beta, 
features=
"ENSG00000254647"
, 


    
x=
I
(
reorder
(sce.beta
$
Donor, sce.beta
$
Disease, 
FUN=
unique)),


    
exprs_values=
"reconstructed"
, 
colour_by=
"Disease"
)




ave.beta <-
 
aggregateAcrossCells
(corr.beta, 
statistics=
"mean"
,


    
use.assay.type=
"reconstructed"
, 
ids=
sce.beta
$
Donor)


by.sample <-
 
plotExpression
(ave.beta, 
features=
"ENSG00000254647"
, 


    
exprs_values=
"reconstructed"
, 
x=
"Disease"
, 
colour_by=
"Disease"
)




gridExtra
::
grid.arrange
(by.cell, by.sample, 
ncol=
2
)
