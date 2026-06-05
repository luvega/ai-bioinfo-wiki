summary
(
mdl
 
<-
 
res
$
mdl
)


mm
 
<-
 
res
$
designmat


lapply
(
colnames
(
mm
)
, \
(
x
)
 
{


    
i
 
<-
 
mdl
$
coefficients
[[
1
]
]
 


    
plotMdl
(
mdl
, predictor
=
x
, shift
=
i
)


}
)
 
|>
 
wrap_plots
(
nrow
=
3
, axes
=
"collect"
)
