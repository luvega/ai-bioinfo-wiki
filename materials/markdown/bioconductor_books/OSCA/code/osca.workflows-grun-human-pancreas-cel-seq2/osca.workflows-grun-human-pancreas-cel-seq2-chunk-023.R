gridExtra
::
grid.arrange
(


    
plotTSNE
(merged.grun, 
colour_by=
"label"
),


    
plotTSNE
(merged.grun, 
colour_by=
"batch"
),


    
ncol=
2


)
