gridExtra
::
grid.arrange
(


    
plotTSNE
(corrected, 
colour_by=
"label"
),


    
plotTSNE
(corrected, 
colour_by=
"batch"
),


    
ncol=
2


)
