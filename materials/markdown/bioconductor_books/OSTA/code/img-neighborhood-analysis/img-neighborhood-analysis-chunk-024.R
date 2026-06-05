anno
 
<-
 
read.csv
(
file.path
(
td
, 
"annotation.csv"
)
)


spe
$
cell_type
 
<-
 
anno
$
Annotation
[
match
(
spe
$
cell_id
, 
anno
$
Barcode
)
]




scider
::
plotSpatial
(
spe
, group
=
"cell_type"
, pt.alpha
=
1
)
