res
 
<-
 
resid
(
.
, scaled
=
TRUE
)
 
~
 
fitted
(
.
)


plot
(
mod
, 
res
, 


    pch
=
12
, abline
=
0
, 


    xlab
=
"Fitted values"
, 


    ylab
=
"Standardised residuals"
,


    col
=
allIslets
$
patient_id
)
