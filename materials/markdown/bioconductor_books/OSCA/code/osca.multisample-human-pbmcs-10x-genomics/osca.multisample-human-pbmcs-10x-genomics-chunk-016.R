all.tsne <-
 
list
()


for
 (n 
in
 
names
(all.sce)) {


    all.tsne[[n]] <-
 
plotTSNE
(all.sce[[n]], 
colour_by=
"label"
) 
+
 
ggtitle
(n)


}


do.call
(gridExtra
::
grid.arrange, 
c
(all.tsne, 
list
(
ncol=
2
)))
