# downsample to at most 4,000 cells per cluster for 'sce'


# (this is done only to keep runtime/memory low)


cs
 
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


cs
 
<-
 
lapply
(
cs
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
4e3
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
cs
)
]
)


rctd_data
 
<-
 
createRctd
(
.vhd16
, 
.sce
, cell_type_col
=
"Level1"
)


(
res
 
<-
 
runRctd
(
rctd_data
, max_cores
=
4
, rctd_mode
=
"doublet"
)
)
