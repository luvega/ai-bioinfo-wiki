resCross
 
<-
 
calcCrossMetricPerFov
(


    
sfe
,


    selection
=
c
(
"DCIS_1"
, 
"DCIS_2"
, 
"Invasive_Tumor"
)
,


    subsetby
=
"sample_id"
,


    fun
=
"Kcross"
,


    marks
=
"Cluster"
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
)
