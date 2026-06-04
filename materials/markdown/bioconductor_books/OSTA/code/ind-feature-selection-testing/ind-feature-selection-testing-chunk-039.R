# known SVGs for this data


known_genes
 
<-
 
c
(
"MOBP"
, 
"SNAP25"
)


# method names


method_names
 
<-
 
c
(
"nnSVG"
, 
"DESpace"
, 
"HVGs"
, 
"DEGs"
)


# convert data structure


rank_long
 
<-
 
rank_all
 
|>


    
left_join
(
data.frame
(
rowData
(
sub
)
[
, 
c
(
"gene_id"
, 
"gene_name"
)
]
)
, by 
=
 
"gene_id"
)
 
|>


    
select
(
all_of
(
c
(
"gene_name"
, 
method_names
)
)
)
 
|>


    
pivot_longer
(
cols 
=
 
c
(
nnSVG
, 
DESpace
, 
HVGs
, 
DEGs
)
, 


                 names_to 
=
 
"method"
, 


                 values_to 
=
 
"rank"
)


# all pairwise comparisons


df_pairs
 
<-
 
t
(
combn
(
method_names
, 
2
)
)
 
|>
 
as.data.frame
(
)


# function to plot each pairwise comparison


plot_pairwise_comparison
 
<-
 
function
(
m1
, 
m2
, 
df
)
 
{


  
# filter the data for the two methods being compared


  
df
 
<-
 
df
 
|>


      
filter
(
method
 
%in%
 
c
(
m1
, 
m2
)
)
 
|>


      
pivot_wider
(
names_from 
=
 
method
, values_from 
=
 
rank
)


  
# compute pearson correlation between methods


  
cor_val
 
<-
 
cor
(
df
[[
m1
]
]
, 
df
[[
m2
]
]
, method 
=
 
"spearman"
)


  
# plot


  
ggplot
(
df
, 
aes
(
x 
=
 
.data
[[
m1
]
]
, y 
=
 
.data
[[
m2
]
]
)
)
 
+


      
geom_point
(
)
 
+
 


      
geom_text_repel
(
data 
=
 
df
 
%>%
 
filter
(
gene_name
 
%in%
 
known_genes
)
, 


                      
aes
(
label 
=
 
gene_name
)
, color 
=
 
"red"
, size 
=
 
3.25
, 


                      nudge_x 
=
 
50
, nudge_y 
=
 
10
, box.padding 
=
 
0.5
)
 
+


      
labs
(
x 
=
 
paste
(
m1
, 
"rank"
)
, y 
=
 
paste
(
m2
, 
"rank"
)
,


           title 
=
 
paste
(
m2
, 
"vs."
, 
m1
, 
": Cor = "
, 
round
(
cor_val
, 
2
)
)
)
 
+


      
#scale_color_manual(values = c("darkorange", "firebrick3", "deepskyblue2")) +


      
theme_bw
(
)
 
+
 
coord_fixed
(
)
 
+
 


      
xlim
(
c
(
0
, 
120
)
)
 
+
 
ylim
(
c
(
0
, 
120
)
)


}




# generate and display all pairwise comparison plots


plots
 
<-
 
lapply
(
seq_len
(
nrow
(
df_pairs
)
)
, \
(
i
)
 
{


    
plot_pairwise_comparison
(
df_pairs
[
i
, 
2
]
, 
df_pairs
[
i
, 
1
]
,
rank_long
)


}
)




wrap_plots
(
plots
, ncol 
=
 
3
)
