gridExtra
::
grid.arrange
(


    
plotTSNE
(sce.seger, 
colour_by=
"label"
),


    
plotTSNE
(sce.seger, 
colour_by=
"Donor"
),


    
ncol=
2


)
