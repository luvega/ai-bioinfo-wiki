# select QC thresholds for library size, 


# detected features & mito. proportion


spe
$
qc_lib_size
 
<-
 
spe
$
sum
 
<
 
600


spe
$
qc_detected
 
<-
 
spe
$
detected
 
<
 
400


spe
$
qc_mito_prop
 
<-
 
spe
$
subsets_mito_percent
 
>
 
30




# tabulate number of cells kept/flagged by each


qc
 
<-
 
grep
(
"^qc"
, 
names
(
colData
(
spe
)
)
)


sapply
(
colData
(
spe
)
[
qc
]
, 
table
)
