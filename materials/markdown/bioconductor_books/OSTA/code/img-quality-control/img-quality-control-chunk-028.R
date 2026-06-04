# compute quality scores & flag cell's that


# fall below specified percentile threshold


cos
 
<-
 
computeQCScore
(
cos
)


cos
 
<-
 
computeQCScoreFlags
(
cos
, 


    qsThreshold
=
0.5
)




# the following slots have now been 


# added to the object's cell metadata


nms
 
<-
 
names
(
colData
(
cos
)
)


sco
 
<-
 
grepv
(
"score$"
, 
nms
)


head
(
colData
(
cos
)
[
sco
]
)
