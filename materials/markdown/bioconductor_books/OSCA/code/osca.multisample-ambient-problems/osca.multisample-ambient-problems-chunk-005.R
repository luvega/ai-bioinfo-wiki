# Standard edgeR analysis, as described in previous chapters.


res.neural <-
 
pseudoBulkDGE
(summed.neural, 


    
label=
summed.neural
$
label,


    
design=
~
factor
(block) 
+
 
tomato,


    
coef=
"tomatoTRUE"
,


    
condition=
summed.neural
$
tomato)


summarizeTestsPerLabel
(
decideTestsPerLabel
(res.neural))
