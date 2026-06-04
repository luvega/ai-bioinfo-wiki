# use 'nImages' randomly samples 


# images for parameter estimation


est
 
<-
 
estimateReconstructionParametersSPE
(


    
spe
, 


    marks
=
"cell_category"
, 


    imageCol
=
"image_name"
, 


    markSelect
=
"islet"
, 


    nImages
=
10
, 


    nCores
=
4
, 


    plotHist
=
FALSE
)


# get parameter estimates for ...


th
 
<-
 
mean
(
est
$
thres
)
 
# threshold


bw
 
<-
 
mean
(
est
$
bndw
)
  
# bandwidth
