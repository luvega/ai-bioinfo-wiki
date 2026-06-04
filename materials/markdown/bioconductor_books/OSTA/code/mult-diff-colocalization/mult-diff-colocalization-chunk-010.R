# this is needed due to a bug in 'spicyR' 


# (setting 'cellType' doesn't work)


.spe
$
cellType
 
<-
 
.spe
$
cell_type


lapply
(
c
(
"L29"
, 
"O02"
)
, \
(
i
)
 
{


    
plotImage
(
.spe
, 


        imageToPlot
=
i
, 


        
#cellType="cell_type",


        imageID
=
"image_name"
,


        from
=
"Tc"
, to
=
"beta"
)
 


}
)
 
|>


    
wrap_plots
(
nrow
=
1
)
 
&


    
coord_equal
(
)
