# retrieve annotations


gz
 
<-
 
"binned_outputs/square_008um/deconvolution.csv.gz"


df
 
<-
 
read.csv
(
file.path
(
td
, 
gz
)
, row.names
=
2
)


head
(
df
 
<-
 
df
[
complete.cases
(
df
)
, 
-
1
]
)
