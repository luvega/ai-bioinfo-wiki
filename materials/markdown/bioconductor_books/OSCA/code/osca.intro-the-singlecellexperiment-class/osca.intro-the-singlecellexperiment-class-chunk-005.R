mat <-
 
read.delim
(calero.counts, 
header=
TRUE
, 
row.names=
1
, 
check.names=
FALSE
)




# Only considering endogenous genes for now.


spike.mat <-
 
mat[
grepl
(
"^ERCC-"
, 
rownames
(mat)),] 


mat <-
 
mat[
grepl
(
"^ENSMUSG"
, 
rownames
(mat)),] 




# Splitting off the gene length column.


gene.length <-
 
mat[,
1
]


mat <-
 
as.matrix
(mat[,
-
1
]) 




dim
(mat)
