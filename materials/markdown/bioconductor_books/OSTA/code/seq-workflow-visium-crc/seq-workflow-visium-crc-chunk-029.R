# prep reference data (Chromium);


# subset cells from same patient


.sce
 
<-
 
sce
[
, 
grepl
(
"P2"
, 
sce
$
Patient
)
]


# downsample to at most 2,000 cells per cluster


cs
 
<-
 
split
(
seq_len
(
ncol
(
.sce
)
)
, 
.sce
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
2e3
)
)
)


.sce
 
<-
 
.sce
[
, 
unlist
(
cs
)
]


# run 'RCTD' deconvolution


rctd_data
 
<-
 
createRctd
(
spe
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
th
, rctd_mode
=
"full"
)
)
