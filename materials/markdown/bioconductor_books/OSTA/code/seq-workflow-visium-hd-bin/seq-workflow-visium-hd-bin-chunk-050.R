sce
$
Level1
 
<-
 
ifelse
(
grepl
(
"Prolif"
, 
sce
$
Level2
)
, 
"Prolif. Immune"
, 
sce
$
Level1
)


table
(
sce
$
Level1
)
 
# tabulate low-res. labels
