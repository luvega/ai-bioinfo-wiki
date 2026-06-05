tab <-
 
table
(
Cluster=
colLabels
(sce.seger), 
Donor=
sce.seger
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
