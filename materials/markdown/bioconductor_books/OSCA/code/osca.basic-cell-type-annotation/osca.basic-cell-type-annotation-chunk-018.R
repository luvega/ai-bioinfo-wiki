tab <-
 
table
(pred.seger
$
pruned.labels, sce.seger
$
CellType)


library
(pheatmap)


pheatmap
(
log2
(tab
+
10
), 
color=
colorRampPalette
(
c
(
"white"
, 
"blue"
))(
101
))
