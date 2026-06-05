# load data from OSF repository (for smaller download)


osf_repo
 
<-
 
osf_retrieve_node
(
"https://osf.io/5n4q3/"
)


osf_files
 
<-
 
osf_ls_files
(
osf_repo
, 


    path
=
"zzz"
, n_max
=
Inf
,


    pattern
=
"Damond_noAssays.rds"
)


dir.create
(
td
 
<-
 
tempfile
(
)
)


foo
 
<-
 
osf_download
(
osf_files
, path
=
td
)


spe
 
<-
 
readRDS
(
file.path
(
td
, 
list.files
(
td
, 
".rds"
)
)
)


table
(
spe
$
patient_id
, 
spe
$
patient_stage
)
