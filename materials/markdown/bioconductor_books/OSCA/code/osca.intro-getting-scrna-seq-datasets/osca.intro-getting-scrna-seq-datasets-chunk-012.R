library
(readxl)


all.counts <-
 
read_excel
(
"GSE61533_HTSEQ_count_results.xls"
)


gene.names <-
 
all.counts
$
ID


all.counts <-
 
as.matrix
(all.counts[,
-
1
])


rownames
(all.counts) <-
 
gene.names


dim
(all.counts)
