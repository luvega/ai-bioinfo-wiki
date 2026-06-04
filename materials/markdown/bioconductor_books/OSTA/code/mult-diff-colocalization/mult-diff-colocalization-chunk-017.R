coefs
 
<-
 
c
(


    
"Onset"
=
"conditionOnset(x)"
, 


    
"Long-Duration"
=
"conditionLong_duration(x)"
)


plotCrossHeatmap
(
resLs
, 


    coefficientsToPlot
=
coefs
, QCThreshold
=
0
, QCMetric
=
"medianMinIntensity"
)
 
+
 


    
guides
(
shape
=
"none"
)
 
+
 
facet_wrap
(
~
factor
(
coefficient
, 
coefs
, 
names
(
coefs
)
)
)
