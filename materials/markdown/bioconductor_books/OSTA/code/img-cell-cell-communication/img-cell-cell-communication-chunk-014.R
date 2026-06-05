xy
 
<-
 
spatialCoords
(
spe
)


ns
 
<-
 
RANN
::
nn2
(
xy
, 
xy
, 
11
)


ds
 
<-
 
ns
$
nn.dists
[
, 
11
]


par
(
mar
=
c
(
4
,
4
,
2
,
0
)
)


hist
(
ds
, n
=
200
,


    xlim
=
c
(
0
, 
60
)
, ylim
=
c
(
0
, 
12e3
)
,


    xlab
=
"10th-NN distance"
, 


    ylab
=
"# cells"
, main
=
""
)


abline
(
v
=
d
 
<-
 
median
(
ds
)
, lw
=
2
, col
=
"red"
)


text
(
d
+
1
, 
12e3
, adj
=
c
(
0
,
1
)
, 
round
(
d
, 
2
)
, col
=
"red"
)
