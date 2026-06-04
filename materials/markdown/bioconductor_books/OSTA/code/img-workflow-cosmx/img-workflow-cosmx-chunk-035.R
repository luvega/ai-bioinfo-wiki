res
 
<-
 
calcMetricPerFov
(


    spe
=
sub
, fun
=
"Lest"
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
"pyramidal CA1"
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
