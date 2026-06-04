rv <-
 
clusterAbundanceVar
(tab.mnn)




# Also printing the percentage of cells in each cluster in each batch:


percent <-
 
t
(
t
(tab.mnn)
/
colSums
(tab.mnn)) 
*
 
100
 


df <-
 
DataFrame
(
Batch=
unclass
(percent), 
var=
rv)


df[
order
(df
$
var, 
decreasing=
TRUE
),]
