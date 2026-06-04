library
(scRNAseq)


sce.zeisel <-
 
ZeiselBrainData
()




library
(scater)


sce.zeisel <-
 
aggregateAcrossFeatures
(sce.zeisel, 


    
id=
sub
(
"_loc[0-9]+$"
, 
""
, 
rownames
(sce.zeisel)))
