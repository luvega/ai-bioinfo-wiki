set.seed
(
0010101
)


dec.pois.pbmc <-
 
modelGeneVarByPoisson
(sce.pbmc)


dec.pois.pbmc <-
 
dec.pois.pbmc[
order
(dec.pois.pbmc
$
bio, 
decreasing=
TRUE
),]


head
(dec.pois.pbmc)
