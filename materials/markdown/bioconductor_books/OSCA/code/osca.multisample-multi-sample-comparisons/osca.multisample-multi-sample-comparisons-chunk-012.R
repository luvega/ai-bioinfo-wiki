by.label <-
 
table
(
colLabels
(merged), merged
$
celltype.mapped)


pheatmap
::
pheatmap
(
log2
(by.label
+
1
), 
color=
viridis
::
viridis
(
101
))
