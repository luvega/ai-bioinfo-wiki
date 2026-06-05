# quantify proportion of cells for which


# lowly/highly correlated genes are detected


fq
 
<-
 \
(
gs
)
 
{


    
y
 
<-
 
counts
(
spe
[
gs
, 
]
)


    
round
(
rowMeans
(
y
 
>
 
0
)
, 
2
)


}


gs
 
<-
 
names
(
sort
(
diag
(
cm
)
)
)


fq
(
tail
(
gs
)
)
 
# high corr.
