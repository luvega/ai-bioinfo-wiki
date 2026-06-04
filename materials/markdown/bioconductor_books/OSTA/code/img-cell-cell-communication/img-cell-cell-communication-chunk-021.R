# visualize scales values across clusters


for
 
(
.
 
in
 
assayNames
(
mu
)
)
 
{


    
plotHeatmap
(
mu
, exprs_values
=
.
,


        features
=
grep
(
"-"
, 
rownames
(
sce
)
)
,


        main
=
switch
(
.
, s
=
"sender"
, r
=
"receiver"
)
,


        show_colnames
=
TRUE
, center
=
TRUE
, scale
=
TRUE
)


}
