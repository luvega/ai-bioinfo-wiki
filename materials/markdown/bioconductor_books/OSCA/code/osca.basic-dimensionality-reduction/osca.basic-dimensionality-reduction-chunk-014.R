set.seed
(
100
)


sce.zeisel <-
 
runTSNE
(sce.zeisel, 
dimred=
"PCA"
, 
perplexity=
5
)


out5 <-
 
plotReducedDim
(sce.zeisel, 
dimred=
"TSNE"
,


    
colour_by=
"level1class"
) 
+
 
ggtitle
(
"perplexity = 5"
)




set.seed
(
100
)


sce.zeisel <-
 
runTSNE
(sce.zeisel, 
dimred=
"PCA"
, 
perplexity=
20
)


out20 <-
 
plotReducedDim
(sce.zeisel, 
dimred=
"TSNE"
,


    
colour_by=
"level1class"
) 
+
 
ggtitle
(
"perplexity = 20"
)




set.seed
(
100
)


sce.zeisel <-
 
runTSNE
(sce.zeisel, 
dimred=
"PCA"
, 
perplexity=
80
)


out80 <-
 
plotReducedDim
(sce.zeisel, 
dimred=
"TSNE"
, 


    
colour_by=
"level1class"
) 
+
 
ggtitle
(
"perplexity = 80"
)




gridExtra
::
grid.arrange
(out5, out20, out80, 
ncol=
3
)
