# combine global/local outliers


spe
$
global_outliers
 
<-
 


    
spe
$
qc_lib_size
 
|
 


    
spe
$
qc_detected
 
|
 


    
spe
$
qc_mito


spe
$
local_outliers
 
<-
 


    
spe
$
sum_outliers
 
|
 


    
spe
$
detected_outliers
 
|
 


    
spe
$
subsets_mito_percent_outliers




rbind
(
 
# tabulate kept/flagged cells


    global
=
table
(
spe
$
global_outliers
)
,


    local
=
table
(
spe
$
local_outliers
)
)
