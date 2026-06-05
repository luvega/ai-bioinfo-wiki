# identify mitochondrial genes


nm
 
<-
 
rowData
(
spe
)
$
gene_name


mt
 
<-
 
grepl
(
"^MT-"
, 
nm
, ignore.case 
=
 
TRUE
)


table
(
mt
)


# remove them


spe
 
<-
 
spe
[
!
mt
, 
]
