tab <-
 
table
(labels
$
labels, 
colLabels
(sce.nest))


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
