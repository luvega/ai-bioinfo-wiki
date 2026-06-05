# 
TODO
: make this process a one-liner.


all.sce2 <-
 
lapply
(all.sce2, 
function
(x) {


    
rowData
(x) <-
 
rowData
(all.sce2[[
1
]])


    x


})


combined <-
 
do.call
(cbind, all.sce2)


combined
$
batch <-
 
rep
(
c
(
"3k"
, 
"4k"
, 
"8k"
), 
vapply
(all.sce2, ncol, 0L))


clusters.mnn <-
 
colLabels
(merged.pbmc)




# Marker detection with block= set to the batch factor.


library
(scran)


m.out <-
 
findMarkers
(combined, clusters.mnn, 
block=
combined
$
batch,


    
direction=
"up"
, 
lfc=
1
, 
row.data=
rowData
(combined)[,
3
,
drop=
FALSE
])




# Seems like CD8+ T cells:


demo <-
 
m.out[[
"10"
]]


as.data.frame
(demo[
1
:
10
,
c
(
"Symbol"
, 
"Top"
, 
"p.value"
, 
"FDR"
)])
