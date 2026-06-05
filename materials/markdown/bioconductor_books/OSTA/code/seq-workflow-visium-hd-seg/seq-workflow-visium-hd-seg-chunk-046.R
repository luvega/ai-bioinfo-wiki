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
"Intestinal.Epithelial"
)
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
sfe
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
sfe
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
