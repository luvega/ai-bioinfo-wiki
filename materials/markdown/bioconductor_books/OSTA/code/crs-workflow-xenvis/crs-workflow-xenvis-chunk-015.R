# propagate Visium data's spatial coordinates, excluding empty pseudo-spots


spatialCoords
(
xem
)
 
<-
 
spatialCoords
(
vis
)
[
vis
$
n_cells
 
>
 
0
, 
]
 


colnames
(
xem
)
 
<-
 
colnames
(
vis
)
[
vis
$
n_cells
 
>
 
0
]


xem
$
in_tissue
 
<-
 
1
