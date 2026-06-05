cos
 
<-
 
computeQCScoreFlags
(
cos
, qsThreshold
=
0.5
)


plotCentroids
(
cos
, colourBy
=
"low_qcscore"
)
 
+
 


    
theme
(
legend.key.size
=
rel
(
0
)
)
 
+


    
guides
(
col
=
guide_legend
(
override.aes
=
list
(
size
=
2
)
)
)
