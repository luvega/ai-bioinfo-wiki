universe <-
 
intersect
(
rownames
(sce.grun), 
rownames
(sce.muraro))


sce.grun2 <-
 
sce.grun[universe,]


dec.grun2 <-
 
dec.grun[universe,]


sce.muraro2 <-
 
sce.muraro[universe,]


dec.muraro2 <-
 
dec.muraro[universe,]




library
(batchelor)


normed.pancreas <-
 
multiBatchNorm
(sce.grun2, sce.muraro2)


sce.grun2 <-
 
normed.pancreas[[
1
]]


sce.muraro2 <-
 
normed.pancreas[[
2
]]




library
(scran)


combined.pan <-
 
combineVar
(dec.grun2, dec.muraro2)


chosen.genes <-
 
rownames
(combined.pan)[combined.pan
$
bio 
>
 
0
]
