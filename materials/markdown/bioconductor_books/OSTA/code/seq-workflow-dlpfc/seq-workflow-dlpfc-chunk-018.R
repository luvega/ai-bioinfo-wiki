# select global QC thresholds


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
qc_mito
 
<-
 
spe
$
subsets_mito_percent
 
>
 
28




# tabulate flagged cells


cd
 
<-
 
colData
(
spe
)


qc
 
<-
 
grep
(
"^qc"
, 
names
(
cd
)
)


sapply
(
cd
[
qc
]
, 
table
)
