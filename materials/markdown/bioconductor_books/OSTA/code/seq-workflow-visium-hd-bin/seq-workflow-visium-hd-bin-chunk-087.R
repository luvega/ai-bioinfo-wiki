source
 
<-
 
df
$
CT
 
%in%
 
c
(
"T cells"
, 
"B cells"
, 
"Myeloid"
)


target
 
<-
 
c
(
"Tumor"
, 
"Fibroblast"
, 
"CT"
)


fd
 
<-
 
pivot_longer
(


    
df
[
source
, 
target
]
, cols
=
-
CT
,


    names_to
=
"target"
, values_to
=
"n"
)


head
(
fd
)
