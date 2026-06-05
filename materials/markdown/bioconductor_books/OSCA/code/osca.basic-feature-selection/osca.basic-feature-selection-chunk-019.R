# Taking the top 1000 genes here:


hvg.pbmc.var <-
 
getTopHVGs
(dec.pbmc, 
n=
1000
)


str
(hvg.pbmc.var)
