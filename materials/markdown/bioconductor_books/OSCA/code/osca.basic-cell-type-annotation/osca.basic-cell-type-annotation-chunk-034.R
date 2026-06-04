# goana() requires Entrez IDs, some of which map to multiple


# symbols - hence the unique() in the call below.


library
(org.Mm.eg.db)


entrez.ids <-
 
mapIds
(org.Mm.eg.db, 
keys=
rownames
(cur.markers), 


    
column=
"ENTREZID"
, 
keytype=
"SYMBOL"
)




library
(limma)


go.out <-
 
goana
(
unique
(entrez.ids[is.de]), 
species=
"Mm"
, 


    
universe=
unique
(entrez.ids))




# Only keeping biological process terms that are not overly general.


go.out <-
 
go.out[
order
(go.out
$
P.DE),]


go.useful <-
 
go.out[go.out
$
Ont
==
"BP"
 
&
 
go.out
$
N 
<=
 
200
,]


head
(go.useful[,
c
(
1
,
3
,
4
)], 
30
)
