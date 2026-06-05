emtab.meta <-
 
colData
(sce.seger)[,
c
(
"cell type"
, 
"disease"
,


    
"individual"
, 
"single cell well quality"
)]


colnames
(emtab.meta) <-
 
c
(
"CellType"
, 
"Disease"
, 
"Donor"
, 
"Quality"
)


colData
(sce.seger) <-
 
emtab.meta




sce.seger
$
CellType <-
 
gsub
(
" cell"
, 
""
, sce.seger
$
CellType)


sce.seger
$
CellType <-
 
paste0
(


    
toupper
(
substr
(sce.seger
$
CellType, 
1
, 
1
)),


    
substring
(sce.seger
$
CellType, 
2
))
