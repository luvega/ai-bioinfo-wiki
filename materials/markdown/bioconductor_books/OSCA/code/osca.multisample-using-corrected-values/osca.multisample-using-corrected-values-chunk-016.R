library
(scater)


sce.beta <-
 
sce.seger[,sce.seger
$
CellType
==
"Beta"
]


by.cell <-
 
plotExpression
(sce.beta, 
features=
"INS"
, 
swap_rownames=
"symbol"
, 
colour_by=
"Disease"
,


    
# Arrange donors by disease status, for a prettier plot.


    
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
unique)))




ave.beta <-
 
aggregateAcrossCells
(sce.beta, 
statistics=
"mean"
,


    
use.assay.type=
"logcounts"
, 
ids=
sce.beta
$
Donor, 
use.altexps=
FALSE
)


by.sample <-
 
plotExpression
(ave.beta, 
features=
"INS"
, 
swap_rownames=
"symbol"
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
