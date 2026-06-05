y.ab3 <-
 
estimateDisp
(y.ab3, design, 
trend=
"none"
)


fit.ab3 <-
 
glmQLFit
(y.ab3, design, 
robust=
TRUE
, 
abundance.trend=
FALSE
)


res3 <-
 
glmQLFTest
(fit.ab3, 
coef=
ncol
(design))


topTags
(res3, 
n=
10
)
