library
(
hoodscanR
)


sqe
 
<-
 
readHoodData
(
spe
, anno_col
=
"k"
)


nbs
 
<-
 
findNearCells
(
sqe
, k
=
100
)


mtx
 
<-
 
scanHoods
(
nbs
$
distance
)
      


grp
 
<-
 
mergeByGroup
(
mtx
, 
nbs
$
cells
)
 


sqe
 
<-
 
mergeHoodSpe
(
sqe
, 
grp
)
