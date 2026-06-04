stat <-
 
rowQuantiles
(
as.matrix
(chosen
$
full.AUC), 
p=
0.2
)


chosen[
order
(stat, 
decreasing=
TRUE
), 
1
:
4
] 
# just showing the basic stats for brevity.
