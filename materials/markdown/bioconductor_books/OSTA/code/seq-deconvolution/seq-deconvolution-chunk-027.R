plot_heat_ws
 
<-
 \
(
ws
, 
string
)
{


    
p
 
<-
 
pheatmap
(
ws
, 


        show_rownames
=
FALSE
, show_colnames
=
TRUE
, main
=
string
,


        cellwidth
=
12
, treeheight_row
=
5
, treeheight_col
=
5
)


    
return
(
p
)


}


plot_heat_ws
(
ws_rctd
, string
=
"RCTD"
)
 


plot_heat_ws
(
ws_card
, string
=
"CARD"
)
