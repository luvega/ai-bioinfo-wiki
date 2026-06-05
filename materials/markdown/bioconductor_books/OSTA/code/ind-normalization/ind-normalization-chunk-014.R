mean_libs
 
<-
 
rowMeans
(
assays
(
spe
)
$
logcounts
)


mean_area
 
<-
 
rowMeans
(
assays
(
spe
)
$
normalized_by_area
)


diff
 
<-
 
abs
(
mean_libs
 
-
 
mean_area
)


ord
 
<-
 
order
(
diff
, decreasing
=
TRUE
)


top_diff
 
<-
 
diff
[
ord
[
1
:
10
]
]


names
(
top_diff
)
