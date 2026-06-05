# select QC threshold for number of cells per spot


spe
$
qc_cell_count
 
<-
 
spe
$
cell_count
 
>
 
10


table
(
spe
$
qc_cell_count
)
