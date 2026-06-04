y.ab2 <-
 
estimateDisp
(y.ab2, design, 
trend=
"none"
)


# We use `legacy=TRUE` to ensure consistency with previous versions of OSCA.


fit.ab2 <-
 
glmQLFit
(y.ab2, design, 
robust=
TRUE
, 
abundance.trend=
FALSE
, 
legacy=
TRUE
)


res2 <-
 
glmQLFTest
(fit.ab2, 
coef=
ncol
(design))


topTags
(res2, 
n=
10
)
