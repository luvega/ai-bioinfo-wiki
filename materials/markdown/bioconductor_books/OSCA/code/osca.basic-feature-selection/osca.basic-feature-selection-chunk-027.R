rowSubset
(sce.pbmc) <-
 
chosen 
# stored in the default 'subset'.


rowSubset
(sce.pbmc, 
"HVGs.more"
) <-
 
getTopHVGs
(dec.pbmc, 
prop=
0.2
)


rowSubset
(sce.pbmc, 
"HVGs.less"
) <-
 
getTopHVGs
(dec.pbmc, 
prop=
0.3
)


colnames
(
rowData
(sce.pbmc))
