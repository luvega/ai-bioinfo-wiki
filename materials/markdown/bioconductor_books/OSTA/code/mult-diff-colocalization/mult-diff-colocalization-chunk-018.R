# extract the metric dataframe


res
 
<-
 
resLs
$
alpha_Tc


metricRes
 
<-
 
res
$
metricRes




# make unique identifiers


metricRes
$
ID
 
<-
 
with
(
metricRes
, 
paste
(
sep
=
"x"
, 


    
patient_stage
, 
patient_id
, 
image_name
)
)




# functional boxplot of spatial statistics curves


collector
 
<-
 
plotFbPlot
(
metricRes
, 
"r"
, 
"rs"
, 
"patient_stage"
)
