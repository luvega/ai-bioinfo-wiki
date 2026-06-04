library
(BiocFileCache)


bfc <-
 
BiocFileCache
(
"raw_data"
, 
ask =
 
FALSE
)


calero.counts <-
 
bfcrpath
(bfc, 
file.path
(
"https://www.ebi.ac.uk/biostudies"
, 


    
"files/E-MTAB-5522/counts_Calero_20160113.tsv"
))
