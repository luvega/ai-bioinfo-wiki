library
(scater)


set.seed
(
101010101
)


merged <-
 
runUMAP
(merged, 
dimred=
"corrected"
)


gridExtra
::
grid.arrange
(


    
plotUMAP
(merged, 
colour_by=
"label"
),


    
plotUMAP
(merged, 
colour_by=
"batch"
),


    
ncol=
2


)
