library
(scPCA)


is.bg <-
 
sce.mess
$
`
experiment batch
`
==
"3"


target <-
 
sce.mess[,
!
is.bg]


background <-
 
sce.mess[,is.bg]




mat.target <-
 
t
(
assay
(target, 
"corrected"
)[top.hvgs,])


mat.background <-
 
t
(
assay
(background, 
"corrected"
)[top.hvgs,])




set.seed
(
1010101001
)


con_out <-
 
scPCA
(


    
target =
 mat.target,


    
background =
 mat.background,


    
penalties =
 
0
, 
# no penalties = non-sparse cPCA.


    
n_eigen =
 
50
,


    
contrasts =
 
100


)


reducedDim
(target, 
"cPCA"
) <-
 
con_out
$
x
