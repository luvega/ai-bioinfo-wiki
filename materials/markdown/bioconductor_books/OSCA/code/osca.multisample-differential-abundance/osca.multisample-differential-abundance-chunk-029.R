res.lfc <-
 
glmTreat
(fit.ab, 
coef=
ncol
(design), 
lfc=
1
)


summary
(
decideTests
(res.lfc))
