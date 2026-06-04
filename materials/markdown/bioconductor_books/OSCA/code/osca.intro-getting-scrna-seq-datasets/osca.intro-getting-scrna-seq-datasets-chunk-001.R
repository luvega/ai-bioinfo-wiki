library
(BiocFileCache)


bfc <-
 
BiocFileCache
(
ask=
FALSE
)


url <-
 
file.path
(
"ftp://ftp.ncbi.nlm.nih.gov/geo/series"
,


    
"GSE85nnn/GSE85241/suppl"
,


    
"GSE85241%5Fcellsystems%5Fdataset%5F4donors%5Fupdated%2Ecsv%2Egz"
)




# Making a symbolic link so that the later code can pretend


# that we downloaded the file into the local directory.


muraro.fname <-
 
bfcrpath
(bfc, url)


local.name <-
 
URLdecode
(
basename
(url))


unlink
(local.name)


if
 (.Platform
$
OS.type
==
"windows"
) {


    
file.copy
(muraro.fname, local.name)


} 
else
 {


    
file.symlink
(muraro.fname, local.name)


}
