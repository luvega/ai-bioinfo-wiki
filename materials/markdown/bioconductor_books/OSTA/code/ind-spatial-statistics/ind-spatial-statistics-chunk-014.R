# code adapted from 


# https://robinsonlabuzh.github.io/


# pasta/04-imaging-multivar-latSOD.html




# dependencies


library
(
BiocNeighbors
)


library
(
BiocSingular
)


library
(
bluster
)


library
(
scater
)




# log-library size normalization


sfe
 
<-
 
logNormCounts
(
sfe
)
