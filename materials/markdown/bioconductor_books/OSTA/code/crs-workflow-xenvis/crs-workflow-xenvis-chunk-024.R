# pool datasets together


gs
 
<-
 
intersect
(
rownames
(
vis
)
, 
rownames
(
xem
)
)


cs
 
<-
 
intersect
(
colnames
(
vis
)
, 
colnames
(
xem
)
)


cd
 
<-
 
intersect
(
names
(
colData
(
vis
)
)
, 
names
(
colData
(
xem
)
)
)


lys
 
<-
 
list
(
Visium
=
vis
, Xenium
=
xem
)


lys
 
<-
 
mapply
(
spe
=
lys
, sid
=
names
(
lys
)
, \
(
spe
, 
sid
)
 
{


    
spe
 
<-
 
spe
[
gs
, 
cs
]


    
spe
$
sample_id
 
<-
 
sid


    
rowData
(
spe
)
 
<-
 
NULL


    
colData
(
spe
)
 
<-
 
colData
(
spe
)
[
cd
]


    
assay
(
spe
)
 
<-
 
as
(
assay
(
spe
)
, 
"dgCMatrix"
)


    
return
(
spe
)


}
, SIMPLIFY
=
FALSE
)


(
obj
 
<-
 
do.call
(
cbind
, 
lys
)
)
