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
"Gcross"
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
100
, l
=
100
)
,


    by
=
"sample_id"
)


plotCrossMetricPerFov
(


    
resCross
,


    theo
=
TRUE
,


    correction
=
"km"
,


    x
=
"r"
,


    imageId
=
"sample_id"
)
[[
1
]
]
