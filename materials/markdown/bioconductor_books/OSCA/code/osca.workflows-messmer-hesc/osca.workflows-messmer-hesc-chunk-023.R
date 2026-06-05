cN <-
 
approxSilhouette
(
reducedDim
(naive, 
"cPCA"
), naive
$
phase)


cP <-
 
approxSilhouette
(
reducedDim
(primed, 
"cPCA"
), primed
$
phase)


c
(
naive=
mean
(cN
$
width), 
primed=
mean
(cP
$
width))
