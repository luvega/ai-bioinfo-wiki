library
(zellkonverter)


demo <-
 
system.file
(
"extdata"
, 
"krumsiek11.h5ad"
, 
package =
 
"zellkonverter"
)


sce <-
 
readH5AD
(demo)


sce
