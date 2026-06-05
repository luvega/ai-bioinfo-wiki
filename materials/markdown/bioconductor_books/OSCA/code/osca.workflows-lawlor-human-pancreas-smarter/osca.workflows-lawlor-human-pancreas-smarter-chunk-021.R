gridExtra
::
grid.arrange
(


    
plotTSNE
(sce.lawlor, 
colour_by=
"label"
),


    
plotTSNE
(sce.lawlor, 
colour_by=
"islet unos id"
),


    
ncol=
2


)
