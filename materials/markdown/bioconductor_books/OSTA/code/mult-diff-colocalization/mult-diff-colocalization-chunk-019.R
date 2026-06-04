# prepare 'data.frame' from 'calcMetricRes' 


# to be in the correct format for FDA


dat
 
<-
 
prepData
(
metricRes
, 
"r"
, 
"rs"
)




# create meta info of the IDs


splitData
 
<-
 
dat
$
ID
 
|>
 


    
str_replace
(
"-"
,
"_"
)
 
|>
 


    
str_split_fixed
(
"x"
, 
3
)
 
|>
 


    
data.frame
(
stringsAsFactors
=
TRUE
)
 
|>
 


    
setNames
(
c
(
"condition"
, 
"patient_id"
, 
"imageId"
)
)
 
|>
 


    
mutate
(
condition
=
relevel
(
condition
,
"Non_diabetic"
)
)




dat
 
<-
 
cbind
(
dat
, 
splitData
)
 
# join with results


dat
 
<-
 
drop_na
(
dat
)
          
# drop rows with NA




# calculate FPCA & visualize biplot


pca
 
<-
 
functionalPCA
(
dat
=
dat
, r
=
unique
(
metricRes
$
r
)
, pve
=
0.995
)


plotFpca
(
dat
=
dat
, res
=
pca
, colourby
=
"condition"
)
 
+
 
labs
(
color
=
"condition"
)
