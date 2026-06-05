tab <-
 
table
(
Cluster=
colLabels
(sce.bone), 
Donor=
sce.bone
$
Donor)


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
