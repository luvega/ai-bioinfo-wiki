coldata <-
 
read.delim
(lun.sdrf, 
check.names=
FALSE
)




# Only keeping the cells involved in the count matrix in 'mat'.


coldata <-
 
coldata[coldata[,
"Derived Array Data File"
]
==
"counts_Calero_20160113.tsv"
,]




# Only keeping interesting columns, and setting the library names as the row names.


coldata <-
 
DataFrame
(


    
genotype=
coldata[,
"Characteristics[genotype]"
],


    
phenotype=
coldata[,
"Characteristics[phenotype]"
],


    
spike_in=
coldata[,
"Factor Value[spike-in addition]"
],


    
row.names=
coldata[,
"Source Name"
]


)




coldata
