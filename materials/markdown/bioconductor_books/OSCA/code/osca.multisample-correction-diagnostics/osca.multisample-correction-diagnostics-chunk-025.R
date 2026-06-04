library
(batchelor)


common <-
 
rownames
(mnn.out)


vars <-
 
mnnDeltaVariance
(pbmc3k[common,], pbmc4k[common,], 


   
pairs=
metadata
(mnn.out)
$
merge.info
$
pairs)


vars[
order
(vars
$
adjusted, 
decreasing=
TRUE
),]
