# calculate log-CPM


log_cpm
 
<-
 
edgeR
::
cpm
(
dsp
$
estimated_y
, log
=
TRUE
)


nms
 
<-
 
colnames
(
log_cpm
)


# wrangling


dat
 
<-
 
data.frame
(


    log_cpm
=
log_cpm
[
top_dsp
, 
]
,


    Banksy
=
factor
(
sub
(
".*_"
, 
""
, 
nms
)
)
, 


    sample_id
=
sub
(
"(_[0-9]+)$"
, 
""
, 
nms
)
,


    day
=
as.numeric
(
sub
(
"([0-9]+)DPI.*"
, 
"\\1"
, 
nms
)
)
)


# visualization


ggplot
(
dat
, 
aes
(
factor
(
day
)
, 
log_cpm
)
)
 
+
 


    
geom_jitter
(
aes
(
col
=
Banksy
)
, size
=
2
, width
=
0.1
)
 
+
 


    
geom_boxplot
(
aes
(
fill
=
ifelse
(
Banksy
 
==
 
"2"
, 
"cluster 2"
, 
"other"
)
)
)
 
+
 


    
scale_x_discrete
(
"Days post injury"
, breaks
=
unique
(
dat
$
day
)
)
 
+
 


    
scale_fill_manual
(
NULL
, values
=
c
(
"limegreen"
, 
"gray"
)
)
 
+
 


    
labs
(
title
=
.gs
, y
=
"log2 counts per million (logCPM)"
)
 
+
 


    
theme
(
legend.position
=
"right"
)
