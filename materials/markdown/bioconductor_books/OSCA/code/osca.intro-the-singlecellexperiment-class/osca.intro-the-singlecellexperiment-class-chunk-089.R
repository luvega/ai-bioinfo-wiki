# -1 to get rid of the first gene length column.


spike_se <-
 
SummarizedExperiment
(
list
(
counts=
spike.mat[,
-
1
]))


spike_se
