set.seed
(
1101001
)


target <-
 
runTSNE
(target, 
dimred =
 
"cPCA"
, 
perplexity =
 
40
, 
name=
"cPCA+TSNE"
)


target <-
 
runTSNE
(target, 
dimred =
 
"scPCA"
, 
perplexity =
 
40
, 
name=
"scPCA+TSNE"
)
