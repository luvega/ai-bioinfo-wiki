# Finding all genes that are not remotely DE in all other labels.


remotely.de <-
 
decideTestsPerLabel
(de.results, 
threshold=
0.5
)


not.de <-
 
remotely.de
==
0
 
|
 
is.na
(remotely.de)


not.de.other <-
 
rowMeans
(not.de[,
colnames
(not.de)
!=
"Allantois"
])
==
1




# Intersecting with genes that are DE inthe allantois.


unique.degs <-
 
is.de[,
"Allantois"
]
!=
0
 
&
 
not.de.other


unique.degs <-
 
names
(
which
(unique.degs))




# Inspecting the results.


de.allantois <-
 
de.results
$
Allantois


de.allantois <-
 
de.allantois[unique.degs,]


de.allantois <-
 
de.allantois[
order
(de.allantois
$
PValue),]


de.allantois
