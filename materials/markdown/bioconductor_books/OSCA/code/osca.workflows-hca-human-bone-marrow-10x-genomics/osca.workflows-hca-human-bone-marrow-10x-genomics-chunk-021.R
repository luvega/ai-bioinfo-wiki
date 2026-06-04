se.aggregated <-
 
sumCountsAcrossCells
(sce.bone, 
id=
colLabels
(sce.bone), 
BPPARAM=
bpp)




library
(celldex)


hpc <-
 
HumanPrimaryCellAtlasData
()




library
(SingleR)


anno.single <-
 
SingleR
(se.aggregated, 
ref =
 hpc, 
labels =
 hpc
$
label.main,


    
assay.type.test=
"sum"
)


anno.single
