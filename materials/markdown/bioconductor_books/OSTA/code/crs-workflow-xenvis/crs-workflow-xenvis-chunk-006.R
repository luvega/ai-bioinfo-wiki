# also retrieve cell subpopulation labels


df
 
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


xen
$
anno
 
<-
 
df
$
Annotation
[
match
(
xen
$
cell_id
, 
df
$
Barcode
)
]
