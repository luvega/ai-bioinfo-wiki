# retrieve dataset from OSF repo


id
 
<-
 
"Chromium_HumanBreast_Janesick"


pa
 
<-
 
OSTA.data_load
(
id
)


dir.create
(
td
 
<-
 
tempfile
(
)
)


unzip
(
pa
, exdir
=
td
)




# read into 'SingleCellExperiment'


fs
 
<-
 
list.files
(
td
, full.names
=
TRUE
)


h5
 
<-
 
grep
(
"h5$"
, 
fs
, value
=
TRUE
)


sce
 
<-
 
read10xCounts
(
h5
, col.names
=
TRUE
)




# use gene symbols as feature names


rownames
(
sce
)
 
<-
 
make.unique
(
rowData
(
sce
)
$
Symbol
)




# retrieve cell type labels


csv
 
<-
 
grep
(
"csv$"
, 
fs
, value
=
TRUE
)


cd
 
<-
 
read.csv
(
csv
, row.names
=
1
)




# ignore mixtures


lab
 
<-
 
cd
$
Annotation


lab
[
grepl
(
"Hyb"
, 
lab
)
]
 
<-
 
NA
 




# simplify annotations


pat
 
<-
 
c
(


    
"B Cell"
=
"B"
, 
"T Cell"
=
"T"
, 
"Mac"
=
"macro"
, 
"Mast"
=
"mast"
, 


    
"DCs"
=
"dendritic"
, 
"Peri"
=
"perivas"
, 
"End"
=
"endo"
, 


    
"Str"
=
"stromal"
, 
"Inv"
=
"tumor"
, 
"Myo"
=
"myoepi"
)


for
 
(
.
 
in
 
names
(
pat
)
)
 


    
lab
[
grep
(
.
, 
lab
)
]
 
<-
 
pat
[
.
]


lab
 
<-
 
gsub
(
"\\s"
, 
""
, 
lab
)




# add as cell metadata


table
(
cd
$
Annogrp
 
<-
 
lab
)
