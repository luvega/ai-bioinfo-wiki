# visualize histrogram of counts 


# per area, including threshold


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
0
, 
0
)
)


hist
(
log
(
nc
)
, 


    n
=
50
, col
=
"lavender"
,


    main
=
NULL
, ylab
=
"# cells"
, 


    xlab
=
"log(total_counts / cell_area)"
)


abline
(
v
=
log
(
th
)
, col
=
"blue"
)
