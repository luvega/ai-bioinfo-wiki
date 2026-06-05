mnn.pancreas <-
 
runTSNE
(mnn.pancreas, 
dimred=
"corrected"
)


gridExtra
::
grid.arrange
(


    
plotTSNE
(mnn.pancreas, 
colour_by=
"batch"
, 
text_by=
I
(clusters)),


    
plotTSNE
(mnn.pancreas, 
colour_by=
I
(clusters), 
text_by=
I
(clusters)),


    
ncol=
2


)
