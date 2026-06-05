tab <-
 
table
(
colLabels
(sce.paul), sce.paul
$
Batch_desc)


rownames
(tab) <-
 
paste
(
"Cluster"
, 
rownames
(tab))


pheatmap
::
pheatmap
(
log10
(tab
+
10
), 
color=
viridis
::
viridis
(
100
))
