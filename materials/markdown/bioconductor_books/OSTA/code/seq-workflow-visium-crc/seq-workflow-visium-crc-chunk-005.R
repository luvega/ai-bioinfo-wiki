# use gene symbols as feature names


rownames
(
spe
)
 
<-
 
make.unique
(
rowData
(
spe
)
$
Symbol
)


# add per-cell quality control metrics


sub
 
<-
 
list
(
mt
=
grep
(
"^MT-"
, 
rownames
(
spe
)
)
)


spe
 
<-
 
addPerCellQCMetrics
(
spe
, subsets
=
sub
)
