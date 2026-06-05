library
(BiocFileCache)


bfc <-
 
BiocFileCache
(
ask=
FALSE
)


exprs.data <-
 
bfcrpath
(bfc, 
file.path
(


    
"http://cf.10xgenomics.com/samples/cell-vdj/3.1.0"
,


    
"vdj_v1_hs_pbmc3"
,


    
"vdj_v1_hs_pbmc3_filtered_feature_bc_matrix.tar.gz"
))


untar
(exprs.data, 
exdir=
tempdir
())




library
(DropletUtils)


sce.pbmc <-
 
read10xCounts
(
file.path
(
tempdir
(), 
"filtered_feature_bc_matrix"
))


sce.pbmc <-
 
splitAltExps
(sce.pbmc, 
rowData
(sce.pbmc)
$
Type)
