stats <-
 
cbind
(
log10
(df
$
sum), 
log10
(df
$
detected),


    df
$
subsets_Mito_percent, df
$
altexps_ERCC_percent)




library
(robustbase)


outlying <-
 
adjOutlyingness
(stats, 
only.outlyingness =
 
TRUE
)


multi.outlier <-
 
isOutlier
(outlying, 
type =
 
"higher"
)


summary
(multi.outlier)
