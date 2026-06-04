set.seed
(
101010101
)


sparse_con_out <-
 
scPCA
(


    
target =
 mat.target,


    
background =
 mat.background,


    
penalties =
 
1e-4
,


    
n_eigen =
 
50
,


    
contrasts =
 
100
,


    
alg =
 
"rand_var_proj"
 
# for speed.


)


reducedDim
(target, 
"scPCA"
) <-
 
sparse_con_out
$
x
