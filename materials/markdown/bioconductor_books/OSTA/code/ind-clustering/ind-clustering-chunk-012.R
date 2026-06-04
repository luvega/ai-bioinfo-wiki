# initialize 'basilisk' environment


env
 
<-
 
BasiliskEnvironment
(


  envname
=
"CellCharter"
, pkgname
=
"OSTA"
,


  channels
=
c
(
"conda-forge"
, 
"pytorch"
)
,


  packages
=
c
(


    
"python=3.10.15"
,


    
"pytorch=1.12.1"
,


    
"torchvision=0.13.1"
,


    
"torchaudio=0.12.1"
)
,


  pip
=
c
(


    
"scvi-tools==0.20.3"
,


    
"cellcharter==0.2.0"
,


    
"anndata==0.10.9"
,


    
"scanpy==1.10.4"
)
)


# activate underlying conda environment


use_condaenv
(
obtainEnvironmentPath
(
env
)
)


counts
 
<-
 
r_to_py
(
t
(
counts
(
spe
)
)
)


coords
 
<-
 
r_to_py
(
spatialCoords
(
spe
)
)
