all.sce <-
 
list
(
Grun=
sce.grun, 
Muraro=
sce.muraro, 


    
Lawlor=
sce.lawlor, 
Seger=
sce.seger)


all.dec <-
 
list
(
Grun=
dec.grun, 
Muraro=
dec.muraro, 


    
Lawlor=
dec.lawlor, 
Seger=
dec.seger)




universe <-
 
Reduce
(intersect, 
lapply
(all.sce, rownames))


all.sce <-
 
lapply
(all.sce, 
"["
, 
i=
universe,)


all.dec <-
 
lapply
(all.dec, 
"["
, 
i=
universe,)




normed.pancreas <-
 
do.call
(multiBatchNorm, all.sce)


combined.pan <-
 
do.call
(combineVar, all.dec)


chosen.genes <-
 
rownames
(combined.pan)[combined.pan
$
bio 
>
 
0
]
