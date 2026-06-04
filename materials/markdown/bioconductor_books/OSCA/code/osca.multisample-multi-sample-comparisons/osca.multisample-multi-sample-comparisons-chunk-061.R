summed.sub <-
 
logNormCounts
(summed.sub, 
size.factors=
NULL
)


plotExpression
(summed.sub, 


    
features=
head
(
rownames
(between.res)[
order
(between.res
$
PValue)]),


    
x=
"celltype.mapped"
, 


    
colour_by=
I
(
factor
(summed.sub
$
sample)))
