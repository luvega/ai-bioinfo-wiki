gridExtra
::
grid.arrange
(


    
plotTSNE
(merged, 
colour_by=
"label"
, 
text_by=
"label"
, 
text_colour=
"red"
),


    
plotTSNE
(merged, 
colour_by=
"batch"
)


)
