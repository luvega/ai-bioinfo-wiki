library
(DropletTestFiles)


raw.path <-
 
getTestFile
(
"tenx-2.1.0-pbmc4k/1.0.0/raw.tar.gz"
)


out.path <-
 
file.path
(
tempdir
(), 
"pbmc4k"
)


untar
(raw.path, 
exdir=
out.path)




library
(DropletUtils)


fname <-
 
file.path
(out.path, 
"raw_gene_bc_matrices/GRCh38"
)


sce.pbmc <-
 
read10xCounts
(fname, 
col.names=
TRUE
)
