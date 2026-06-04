# Downloading the signatures and caching them locally.


library
(BiocFileCache)


bfc <-
 
BiocFileCache
(
ask=
FALSE
)


scsig.path <-
 
bfcrpath
(bfc, 
file.path
(
"http://software.broadinstitute.org"
,


    
"gsea/msigdb/supplemental/scsig.all.v1.0.symbols.gmt"
))


scsigs <-
 
getGmt
(scsig.path)
