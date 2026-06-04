gridExtra
::
grid.arrange
(


    
plotTSNE
(merged, 
colour_by=
"tomato"
, 
text_by=
"label"
),


    
plotTSNE
(merged, 
colour_by=
data.frame
(
pool=
factor
(merged
$
pool))),


    
ncol=
2


)
