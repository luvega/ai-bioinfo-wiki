par
(
mfrow
=
c
(
1
, 
4
)
)


hist
(
spe
$
sum
, xlab
=
"sum"
, main
=
"UMIs per spot"
)


hist
(
spe
$
detected
, xlab
=
"detected"
, main
=
"Genes per spot"
)


hist
(
spe
$
subsets_mito_percent
, xlab
=
"pct mito"
, main
=
"Percent mito UMIs"
)


hist
(
spe
$
cell_count
, xlab
=
"no. cells"
, main
=
"No. cells per spot"
)
