inter.res <-
 
pseudoBulkDGE
(summed.sub,


    
label=
rep
(
"dummy"
, 
ncol
(summed.sub)),


    
design=
function
(df) {


        combined <-
 
with
(df, 
paste0
(tomato, 
"."
, celltype.mapped))


        combined <-
 
make.names
(combined)


        design <-
 
model.matrix
(
~
0
 
+
 
factor
(sample) 
+
 
combined, df)


        design[,
!
grepl
(
"Notochord"
, 
colnames
(design))]


    },


    
coef=
"combinedTRUE.Neural.crest"


)[[
1
]]




table
(
Sig=
inter.res
$
FDR 
<=
 
0.05
, 
Sign=
sign
(inter.res
$
logFC))
