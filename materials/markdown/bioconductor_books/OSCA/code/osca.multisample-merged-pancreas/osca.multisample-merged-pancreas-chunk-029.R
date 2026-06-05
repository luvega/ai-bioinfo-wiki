multiout <-
 
runTSNE
(multiout, 
dimred=
"corrected"
)


gridExtra
::
grid.arrange
(


    
plotTSNE
(multiout, 
colour_by=
"dataset"
, 
text_by=
I
(clusters)),


    
plotTSNE
(multiout, 
colour_by=
I
(seger.donors)),


    
ncol=
2


)
