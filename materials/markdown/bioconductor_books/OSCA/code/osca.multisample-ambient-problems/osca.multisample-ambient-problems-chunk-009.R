library
(DropletUtils)


ambient <-
 
vector
(
"list"
, 
ncol
(summed.neural))




# Looping over all raw (unfiltered) count matrices and


# computing the ambient profile based on its low-count barcodes.


# Turning off rounding, as we know this is count data.


for
 (s 
in
 
seq_along
(ambient)) {


    raw.tal1 <-
 
Tal1ChimeraData
(
type=
"raw"
, 
samples=
s)[[
1
]]


    
counts
(raw.tal1) <-
 
as
(
counts
(raw.tal1), 
"CsparseMatrix"
)


    ambient[[s]] <-
 
ambientProfileEmpty
(
counts
(raw.tal1), 


        
good.turing=
FALSE
, 
round=
FALSE
)


}




# Cleaning up the output for pretty printing.


ambient <-
 
do.call
(cbind, ambient)


colnames
(ambient) <-
 
seq_len
(
ncol
(ambient))


rownames
(ambient) <-
 
uniquifyFeatureNames
(


    
rowData
(raw.tal1)
$
ENSEMBL, 


    
rowData
(raw.tal1)
$
SYMBOL


)


head
(ambient)
