set.seed
(
10001
)


hs_pairs <-
 
readRDS
(
system.file
(
"exdata"
, 
"human_cycle_markers.rds"
, 
package=
"scran"
))


assigned <-
 
cyclone
(sce.mess, 
pairs=
hs_pairs, 


    
gene.names=
rownames
(sce.mess),


    
BPPARAM=
BiocParallel
::
MulticoreParam
(
10
))


sce.mess
$
phase <-
 
assigned
$
phases
