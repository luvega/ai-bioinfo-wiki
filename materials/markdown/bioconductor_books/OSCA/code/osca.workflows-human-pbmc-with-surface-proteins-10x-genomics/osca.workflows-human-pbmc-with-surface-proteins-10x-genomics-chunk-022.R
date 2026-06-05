library
(bluster)


mod <-
 
pairwiseModularity
(g.adt, clust.adt, 
as.ratio=
TRUE
)




library
(pheatmap)


pheatmap
::
pheatmap
(
log10
(mod 
+
 
10
), 
cluster_row=
FALSE
, 
cluster_col=
FALSE
,


    
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
