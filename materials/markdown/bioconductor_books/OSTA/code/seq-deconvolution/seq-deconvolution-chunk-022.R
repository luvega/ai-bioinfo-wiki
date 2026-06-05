set.seed
(
2025
)


CARD_obj
 
<-
 
CARD_deconvolution
(


    spe
=
vis
,


    sce
=
sce
,


    sc_count
=
NULL
,


    sc_meta
=
NULL
,


    spatial_count
=
NULL
,


    spatial_location
=
NULL
,


    ct_varname
=
"Annogrp"
,


    ct_select
=
NULL
,      
# use all 'sce$Annogrp' cell types


    sample_varname
=
NULL
, 
# use all 'sce' as one 'ref' sample 


    mincountgene
=
100
,


    mincountspot
=
5
)


ws_card
 
<-
 
CARD_obj
$
Proportion_CARD




# order cell type names alphabetically, as for RCTD


ws_card
 
<-
 
data.frame
(
ws_card
[
, 
colnames
(
ws_rctd
)
]
)


round
(
ws_card
[
1
:
5
, 
1
:
5
]
, 
2
)
