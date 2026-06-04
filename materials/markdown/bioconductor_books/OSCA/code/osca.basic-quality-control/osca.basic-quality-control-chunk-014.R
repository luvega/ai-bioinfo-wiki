qc.lib <-
 
df
$
sum 
<
 
1e5


qc.nexprs <-
 
df
$
detected 
<
 
5e3


qc.spike <-
 
df
$
altexps_ERCC_percent 
>
 
10


qc.mito <-
 
df
$
subsets_Mito_percent 
>
 
10


discard <-
 
qc.lib 
|
 
qc.nexprs 
|
 
qc.spike 
|
 
qc.mito




# Summarize the number of cells removed for each reason.


DataFrame
(
LibSize=
sum
(qc.lib), 
NExprs=
sum
(qc.nexprs),


    
SpikeProp=
sum
(qc.spike), 
MitoProp=
sum
(qc.mito), 
Total=
sum
(discard))
