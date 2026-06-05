lab
 
<-
 
list
(


    tum
=
"Tumor"
,


    epi
=
"Intestinal.Epithelial"
,


    imm
=
c
(
"B.cells"
, 
"T.cells"
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
"Smooth.Muscle"
)
)


idx
 
<-
 
match
(
spe
$
RCTD
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
spe
$
Domain
 
<-
 
factor
(
lab
[
idx
]
)
)
