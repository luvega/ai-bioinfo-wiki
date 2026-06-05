# locate and delete files in BiocFileCache directory


id
 
<-
 
"VisiumHD_HumanColon_Oliveira"


bfc
 
<-
 
BiocFileCache
::
BiocFileCache
(
)


qid
 
<-
 
BiocFileCache
::
bfcquery
(
bfc
, 
id
)
$
rid


BiocFileCache
::
bfcremove
(
bfc
, 
qid
)
