library
(bluster)


naive <-
 
target[,target
$
phenotype
==
"naive"
]


primed <-
 
target[,target
$
phenotype
==
"primed"
]




N <-
 
approxSilhouette
(
reducedDim
(naive, 
"PCA"
), naive
$
phase)


P <-
 
approxSilhouette
(
reducedDim
(primed, 
"PCA"
), primed
$
phase)


c
(
naive=
mean
(N
$
width), 
primed=
mean
(P
$
width))
