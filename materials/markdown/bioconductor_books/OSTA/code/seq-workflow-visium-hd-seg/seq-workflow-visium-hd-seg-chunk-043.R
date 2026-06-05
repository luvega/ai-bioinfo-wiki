# perform label transfer at the Visium HD cell-level,


# using pseudo-bulk Chromium profiles as reference


res
 
<-
 
SingleR
(
test
=
sfe
, ref
=
.sce
, labels
=
.sce
$
Level1
, aggr.ref
=
TRUE
)
