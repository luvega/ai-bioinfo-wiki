# Again, using randomized SVD here, as this is faster than IRLBA for


# file-backed matrices. We set deferred=TRUE for greater speed.


set.seed
(
1000101001
)


mnn.out <-
 
fastMNN
(pbmc3k, pbmc4k, 
d=
50
, 
k=
20
, 
subset.row=
chosen.hvgs,


    
BSPARAM=
BiocSingular
::
RandomParam
(
deferred=
TRUE
))


mnn.out
