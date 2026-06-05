# Installing CRAN packages as of 29th April, 2020;


# see https://packagemanager.rstudio.com/client/#/repos/1/overview for available dates.


options
(
repos =
 
c
(
CRAN =
 
"https://packagemanager.rstudio.com/all/277"
))




# Using packages from Bioconductor version 3.10, see below. 


BiocManager
::
install
(
version=
"3.10"
)
