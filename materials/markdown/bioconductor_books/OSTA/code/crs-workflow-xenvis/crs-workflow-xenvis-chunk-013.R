# aggregate Xenium data into pseudo-spots


xem
 
<-
 
aggregateAcrossCells
(
xen
[
, 
c
(
t
(
idx
)
)
]
, 
rep.int
(
seq
(
ncol
(
vis
)
)
, 
vis
$
n_cells
)
)
