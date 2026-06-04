library
(SingleCellExperiment)


# Identifying the mitochondrial transcripts in our SingleCellExperiment.


location <-
 
rowRanges
(sce
.416
b)


is.mito <-
 
any
(
seqnames
(location)
==
"MT"
)




library
(scuttle)


df <-
 
perCellQCMetrics
(sce
.416
b, 
subsets=
list
(
Mito=
is.mito))


summary
(df
$
sum)
