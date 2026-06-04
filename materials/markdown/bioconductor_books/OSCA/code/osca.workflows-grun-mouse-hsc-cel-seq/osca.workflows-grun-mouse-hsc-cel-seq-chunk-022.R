short <-
 
ifelse
(
grepl
(
"micro"
, sce.grun.hsc
$
protocol), 
"micro"
, 
"sorted"
)


gridExtra
:::
grid.arrange
(


    
plotTSNE
(sce.grun.hsc, 
colour_by=
"label"
),


    
plotTSNE
(sce.grun.hsc, 
colour_by=
I
(short)),


    
ncol=
2


)
