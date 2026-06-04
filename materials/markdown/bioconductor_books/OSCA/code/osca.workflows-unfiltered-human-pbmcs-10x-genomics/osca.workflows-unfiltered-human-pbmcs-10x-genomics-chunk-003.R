set.seed
(
100
)


e.out <-
 
emptyDrops
(
counts
(sce.pbmc))


sce.pbmc <-
 
sce.pbmc[,
which
(e.out
$
FDR 
<=
 
0.001
)]
