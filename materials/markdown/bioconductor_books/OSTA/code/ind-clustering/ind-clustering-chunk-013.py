import
 cellcharter 
as
 cc


import
 anndata 
as
 ad


import
 squidpy 
as
 sq


import
 pandas 
as
 pd


import
 numpy 
as
 np


import
 random


import
 scvi




adata 
=
 ad.AnnData(X 
=
 r.counts,


                   obsm 
=
 {
"spatial"
:r.coords},


                   layers 
=
 {
"counts"
: r.counts})




seed 
=
 
2025


random.seed(seed)


scvi.settings.seed 
=
 seed




# variational autoencoder for feature extraction


scvi.model.SCVI.setup_anndata(adata, layer
=
"counts"
)


model 
=
 scvi.model.SCVI(adata, n_hidden
=
64
)


model.train(early_stopping
=
True
,


    
# the parameters below aim to reduce runtime; 


    
# in reality, it'd be better to use defaults


    max_epochs
=
70
, batch_size
=
512
, train_size
=
0.5
, validation_size
=
0.2
)




adata.obsm[
"X_scVI"
] 
=
 model.get_latent_representation(adata).astype(np.float32)




# Getting neighborhood aggregation


sq.gr.spatial_neighbors(adata, coord_type
=
"generic"
, delaunay
=
True
, spatial_key
=
"spatial"
, percentile
=
99
)


cc.gr.aggregate_neighbors(adata, n_layers
=
3
, use_rep
=
"X_scVI"
, out_key
=
"X_cellcharter"
)




# clustering by scanning a range of data number


mod 
=
 cc.tl.Cluster(n_clusters
=
14
, random_state
=
seed)


mod.fit(adata, use_rep
=
"X_cellcharter"
)




label_df 
=
 pd.DataFrame({
"label"
: mod.predict(adata, use_rep
=
"X_cellcharter"
)}) 


label_df[[
"label"
]].value_counts()
