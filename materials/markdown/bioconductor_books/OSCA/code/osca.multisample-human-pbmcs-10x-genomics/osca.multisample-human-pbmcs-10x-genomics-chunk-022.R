set.seed
(
10101010
)


merged.pbmc <-
 
runTSNE
(merged.pbmc, 
dimred=
"corrected"
)


gridExtra
::
grid.arrange
(


    
plotTSNE
(merged.pbmc, 
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
(merged.pbmc, 
colour_by=
"batch"
)


)
