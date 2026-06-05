lab
 
<-
 
list
(


    tum
=
c
(
"Tumor"
)
,


    epi
=
c
(
"Intestinal Epithelial"
)
,


    imm
=
c
(
"B cells"
, 
"T cells"
, 
"Myeloid"
)
,


    str
=
c
(
"Endothelial"
, 
"Fibroblast"
, 
"Smooth Muscle"
)
)


idx
 
<-
 
match
(
sub
$
Level1
, 
unlist
(
lab
)
)


lab
 
<-
 
rep.int
(
names
(
lab
)
, 
sapply
(
lab
, 
length
)
)


table
(
sub
$
Level0
 
<-
 
factor
(
lab
[
idx
]
)
)
