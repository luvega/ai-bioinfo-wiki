tab <-
 
table
(
Cluster=
colLabels
(merged.muraro), 
CellType=
sce.muraro
$
label)


library
(pheatmap)


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
