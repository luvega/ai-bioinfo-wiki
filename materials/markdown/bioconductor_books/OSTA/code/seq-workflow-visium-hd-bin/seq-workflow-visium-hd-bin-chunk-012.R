csv
 
<-
 
list.files
(
td
, 
"clustering.csv.gz"
, recursive
=
TRUE
, full.names
=
TRUE
)


dfs
 
<-
 
lapply
(
csv
, 
read.csv
, row.names
=
"barcode"
)
 




colData
(
vhd8
)
$
cluster
 
<-
 
factor
(
dfs
[[
1
]
]
[
colnames
(
vhd8
)
, 
"cluster"
]
)


colData
(
vhd16
)
$
cluster
 
<-
 
factor
(
dfs
[[
2
]
]
[
colnames
(
vhd16
)
, 
"cluster"
]
)
