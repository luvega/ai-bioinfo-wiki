library
(LoomExperiment)


demo <-
 
system.file
(
"extdata"
, 
"L1_DRG_20_example.loom"
, 
package =
 
"LoomExperiment"
)


scle <-
 
import
(demo, 
type=
"SingleCellLoomExperiment"
)


scle
