# convert 'SpatialExperiment' (R) to 


# 'AnnData' (Python) using 'anndataR'


ad
 
<-
 
as_AnnData
(
sub
, 


    x_mapping
=
"logcounts"
, 


    output_class
=
"ReticulateAnnData"
)


# run CCC inference using 'COMMOT'


ct
 
<-
 
import
(
"commot"
)


ct
$
tl
$
spatial_communication
(
ad
,


    database_name
=
"CellChatDB"
,


    dis_thr
=
10
,  


    df_ligrec
=
db
,


    heteromeric
=
TRUE
,


    pathway_sum
=
TRUE
,


    heteromeric_rule
=
"min"
,


    heteromeric_delimiter
=
"_"
)


# extract 'data.frame's containing


# sender & receiver CCC estimates


ccc
 
<-
 
list
(


    s
=
ad
$
obsm
$
`commot-CellChatDB-sum-sender`
,


    r
=
ad
$
obsm
$
`commot-CellChatDB-sum-receiver`
)


# add CCC inference results as cell metadata


for
 
(
df
 
in
 
ccc
)
 
colData
(
sub
)
[
names
(
df
)
]
 
<-
 
df
