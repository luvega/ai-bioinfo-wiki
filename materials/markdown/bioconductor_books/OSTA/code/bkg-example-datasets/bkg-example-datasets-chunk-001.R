library
(
BiocFileCache
)


bfc
 
<-
 
BiocFileCache
(
)


# specify dataset identifier


id
 
<-
 
"Xenium_HumanColon_Oliveira"
    


# query cached files for 'id'


que
 
<-
 
bfcquery
(
bfc
, 
id
)
 


# clear matching resource


bfcremove
(
bfc
, 
que
$
rid
)
   


# retrieve current dataset


OSTA.data_load
(
id
)
