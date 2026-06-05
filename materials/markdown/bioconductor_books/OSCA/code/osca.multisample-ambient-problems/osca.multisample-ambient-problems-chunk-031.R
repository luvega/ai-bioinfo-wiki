par
(
mfrow=
c
(
2
,
2
))


for
 (i 
in
 
seq_len
(
ncol
(proxy.ambient))) {


    true <-
 
ambient[,i]


    proxy <-
 
assay
(proxy.ambient)[,i]


    logged <-
 
edgeR
::
cpm
(
cbind
(proxy, true), 
log=
TRUE
, 
prior.count=
2
)


    logFC <-
 
logged[,
1
] 
-
 
logged[,
2
]


    abundance <-
 
rowMeans
(logged)


    
plot
(abundance, logFC, 
main=
paste
(
"Sample"
, i))


}
