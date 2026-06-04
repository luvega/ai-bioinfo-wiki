library
(SingleR)


mm.ref <-
 
MouseRNAseqData
()




# Renaming to symbols to match with reference row names.


renamed <-
 
sce.nest


rownames
(renamed) <-
 
uniquifyFeatureNames
(
rownames
(renamed),


    
rowData
(sce.nest)
$
SYMBOL)


labels <-
 
SingleR
(renamed, mm.ref, 
labels=
mm.ref
$
label.fine)
