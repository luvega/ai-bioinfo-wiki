library
(GSEABase)


all.sets <-
 
lapply
(
names
(markers.z), 
function
(x) {


    
GeneSet
(markers.z[[x]], 
setName=
x)        


})


all.sets <-
 
GeneSetCollection
(all.sets)




library
(AUCell)


rankings <-
 
AUCell_buildRankings
(
counts
(sce.tasic),


    
plotStats=
FALSE
, 
verbose=
FALSE
)


cell.aucs <-
 
AUCell_calcAUC
(all.sets, rankings)


results <-
 
t
(
assay
(cell.aucs))


head
(results)
