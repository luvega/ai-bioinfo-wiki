# Extract symbols for each GO term; done once.


tab <-
 
select
(org.Mm.eg.db, 
keytype=
"SYMBOL"
, 
keys=
rownames
(sce.mam), 
columns=
"GOALL"
)


by.go <-
 
split
(tab[,
1
], tab[,
2
])




# Identify genes associated with an interesting term.


interesting <-
 
unique
(by.go[[
"GO:0006641"
]])


interesting.markers <-
 
cur.markers[
rownames
(cur.markers) 
%in%
 
interesting,]


head
(interesting.markers[
order
(
-
interesting.markers
$
median.logFC.cohen),
1
:
4
], 
10
)
