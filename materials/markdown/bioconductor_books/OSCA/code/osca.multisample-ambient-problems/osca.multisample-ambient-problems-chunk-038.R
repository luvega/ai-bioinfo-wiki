library
(edgeR)


y.ambient <-
 
DGEList
(ambient, 
samples=
colData
(summed.neural))


y.ambient <-
 
y.ambient[
filterByExpr
(y.ambient, 
group=
y.ambient
$
samples
$
tomato),]


y.ambient <-
 
calcNormFactors
(y.ambient)




design <-
 
model.matrix
(
~
factor
(block) 
+
 
tomato, y.ambient
$
samples)


y.ambient <-
 
estimateDisp
(y.ambient, design)


fit.ambient <-
 
glmQLFit
(y.ambient, design, 
robust=
TRUE
)


res.ambient <-
 
glmQLFTest
(fit.ambient, 
coef=
ncol
(design))




summary
(
decideTests
(res.ambient))
