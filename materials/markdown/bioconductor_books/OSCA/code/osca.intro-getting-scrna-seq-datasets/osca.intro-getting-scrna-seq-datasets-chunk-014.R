library
(DropletTestFiles)


cached <-
 
getTestFile
(
"tenx-2.1.0-pbmc4k/1.0.0/filtered.tar.gz"
)


fpath <-
 "tenx-2.1.0-pbmc4k"


untar
(cached, 
exdir=
fpath)
