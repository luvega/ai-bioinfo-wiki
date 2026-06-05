library
(HCAData)


sce.bone <-
 
HCAData
(
'ica_bone_marrow'
, 
as.sparse=
TRUE
)


sce.bone
$
Donor <-
 
sub
(
"_.*"
, 
""
, sce.bone
$
Barcode)
