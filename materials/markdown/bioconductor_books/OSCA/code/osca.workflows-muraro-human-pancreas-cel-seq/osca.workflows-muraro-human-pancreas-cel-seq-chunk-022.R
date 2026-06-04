gridExtra
::
grid.arrange
(


    
plotTSNE
(merged.muraro, 
colour_by=
"label"
),


    
plotTSNE
(merged.muraro, 
colour_by=
"batch"
),


    
ncol=
2


)
