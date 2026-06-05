# filer for those fully covered by the panel


keep
 
<-
 
apply
(
db
, 
1
, \
(
.
)
 
{


    
rs
 
<-
 
strsplit
(
.
[
"receptor"
]
, 
"_"
)


    
lr
 
<-
 
c
(
.
[
"ligand"
]
, 
unlist
(
rs
)
)


    
all
(
lr
 
%in%
 
rownames
(
spe
)
)


}
)


(
db
 
<-
 
db
[
keep
, 
]
)
