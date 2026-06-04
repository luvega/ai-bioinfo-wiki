# download Gencode v32 GTF file and cache it


nms
 
<-
 
paste0
(


  
"ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/"
,


  
"release_32/gencode.v32.annotation.gtf.gz"
)


bfc
 
<-
 
BiocFileCache
(
)


gtf_cache
 
<-
 
bfcrpath
(
bfc
, 
nms
)
