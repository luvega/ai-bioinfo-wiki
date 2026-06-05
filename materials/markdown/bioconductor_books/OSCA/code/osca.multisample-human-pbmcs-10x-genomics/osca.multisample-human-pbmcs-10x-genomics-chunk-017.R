# Intersecting the common genes.


universe <-
 
Reduce
(intersect, 
lapply
(all.sce, rownames))


all.sce2 <-
 
lapply
(all.sce, 
"["
, 
i=
universe,)


all.dec2 <-
 
lapply
(all.dec, 
"["
, 
i=
universe,)




# Renormalizing to adjust for differences in depth.


library
(batchelor)


normed.sce <-
 
do.call
(multiBatchNorm, all.sce2)




# Identifying a set of HVGs using stats from all batches.


combined.dec <-
 
do.call
(combineVar, all.dec2)


combined.hvg <-
 
getTopHVGs
(combined.dec, 
n=
5000
)




set.seed
(
1000101
)


merged.pbmc <-
 
do.call
(fastMNN, 
c
(normed.sce, 


    
list
(
subset.row=
combined.hvg, 
BSPARAM=
RandomParam
())))
