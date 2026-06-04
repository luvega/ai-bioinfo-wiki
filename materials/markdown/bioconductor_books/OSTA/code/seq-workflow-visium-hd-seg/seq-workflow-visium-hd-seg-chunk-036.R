# (this is done only to keep runtime/memory low)


idx
 
<-
 
split
(
seq_len
(
ncol
(
sce
)
)
, 
sce
$
Level1
)


idx
 
<-
 
lapply
(
idx
, \
(
.
)
 
sample
(
.
, 
min
(
length
(
.
)
, 
1e3
)
)
)


ncol
(
.sce
 
<-
 
sce
[
, 
unlist
(
idx
)
]
)
