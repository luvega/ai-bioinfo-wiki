res
 
<-
 
calcMetricPerFov
(


    spe
=
sub
, fun
=
"Lcross"
, 


    subsetby
=
"sample_id"
, 


    marks
=
"SingleR_label"
,


    selection
=
c
(
"pyramidal CA1"
, 
"oligodendrocytes"
)
,


    rSeq
=
seq
(
0
, 
500
, l
=
100
)
,


    by
=
"sample_id"
, ncores
=
1
)




plotMetricPerFov
(
res
, 


    theo
=
TRUE
, correction
=
"iso"
, 


    x
=
"r"
, imageId
=
"sample_id"
)
