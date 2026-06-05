import
 anndata


import
 matplotlib


import
 matplotlib.pyplot 
as
 plt




ad 
=
 anndata.read_h5ad(
"spe.h5ad"
)


ad.var_names 
=
 ad.var[
"Symbol"
].astype(
str
)




xy 
=
 ad.obsm[
"spatial"
]


z 
=
 ad[:,
"ERBB2"
].layers[
"counts"
].toarray()




plt.scatter(xy[:,
0
], xy[:,
1
], c
=
z, s
=
5
, cmap
=
"turbo"
)


plt.gca().set_aspect(
"equal"
)


plt.title(
"ERBB2"
)
