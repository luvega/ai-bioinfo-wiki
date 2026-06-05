# combine local and global outliers &


# remove combined set of low-quality spots


spe
$
discard
 
<-
 


    
spe
$
global_outliers
 
|
 


    
spe
$
local_outliers


spe
 
<-
 
spe
[
, 
!
spe
$
discard
]




# remove features with all 0 counts


spe
 
<-
 
spe
[
rowSums
(
counts
(
spe
)
)
 
>
 
0
, 
]


dim
(
spe
)
