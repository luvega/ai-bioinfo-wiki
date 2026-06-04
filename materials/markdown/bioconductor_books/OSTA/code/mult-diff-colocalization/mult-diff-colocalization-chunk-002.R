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




# read into R & subset patient IDs (to reduce runtime)


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


ids
 
<-
 
c
(
6089
, 
6180
, 
6126
, 
6134
, 
6228
, 
6414
)


(
spe
 
<-
 
spe
[
, 
spe
$
patient_id
 
%in%
 
ids
]
)
