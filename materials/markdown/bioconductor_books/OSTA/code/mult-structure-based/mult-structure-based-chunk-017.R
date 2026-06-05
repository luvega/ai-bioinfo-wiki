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
 
|
 
patient_id


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
)
