scN <-
 
approxSilhouette
(
reducedDim
(naive, 
"scPCA"
), naive
$
phase)


scP <-
 
approxSilhouette
(
reducedDim
(primed, 
"scPCA"
), primed
$
phase)


c
(
naive=
mean
(scN
$
width), 
primed=
mean
(scP
$
width))
