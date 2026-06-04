library
(MouseGastrulationData)


sce.tal1 <-
 
Tal1ChimeraData
()


counts
(sce.tal1) <-
 
as
(
counts
(sce.tal1), 
"CsparseMatrix"
) 




library
(scuttle)


rownames
(sce.tal1) <-
 
uniquifyFeatureNames
(


    
rowData
(sce.tal1)
$
ENSEMBL, 


    
rowData
(sce.tal1)
$
SYMBOL


)


sce.tal1
