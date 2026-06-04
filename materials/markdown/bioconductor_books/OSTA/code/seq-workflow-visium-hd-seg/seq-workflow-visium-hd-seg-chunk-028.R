# determine spatial outliers for different metrics


qc
 
<-
 
c
(
"sum"
, 
"detected"
, 
"subsets_mt_percent"
)


for
 
(
.
 
in
 
qc
)
 
{


    
sfe
 
<-
 
localOutliers
(
sfe
, 


        workers
=
4
, metric
=
.
, 


        log
=
TRUE
, direction
=
"lower"
)


}


# get cells x flags matrix


cd
 
<-
 
colData
(
sfe
)


ol
 
<-
 
grep
(
"outliers$"
, 
names
(
cd
)
)


ol
 
<-
 
as.matrix
(
cd
[
ol
]
)


# percentage of cells exluded for each 


round
(
100
*
colMeans
(
ol
)
, 
2
)
