# Averaging the ambient contribution across samples.


contamination <-
 
rowMeans
(max.ambient, 
na.rm=
TRUE
)


non.ambient <-
 
contamination 
<=
 
0.1


summary
(non.ambient)
