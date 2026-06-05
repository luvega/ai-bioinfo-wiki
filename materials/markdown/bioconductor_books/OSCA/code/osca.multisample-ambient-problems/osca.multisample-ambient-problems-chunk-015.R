okay.genes <-
 
names
(non.ambient)[
which
(non.ambient)]


tab.neural2 <-
 
tab.neural[
rownames
(tab.neural) 
%in%
 
okay.genes,]




table
(
Direction=
tab.neural2
$
logFC 
>
 
0
, 
Significant=
tab.neural2
$
FDR 
<=
 
0.05
)
