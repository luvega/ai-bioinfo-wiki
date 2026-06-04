Y <-
 
assay
(
altExp
(sce.nest, 
"FACS"
))


keep <-
 
colSums
(
is.na
(Y))
==
0
 
# Removing NA intensities.




se.averaged <-
 
sumCountsAcrossCells
(Y[,keep], 


    
colLabels
(sce.nest)[keep], 
average=
TRUE
)


averaged <-
 
assay
(se.averaged)




log.intensities <-
 
log2
(averaged
+
1
)


centered <-
 
log.intensities 
-
 
rowMeans
(log.intensities)


pheatmap
(centered, 
breaks=
seq
(
-
1
, 
1
, 
length.out=
101
))
