Xenium


  └── outs 


    ├── cells.parquet          
# cell metadata (e.g., area)


    ├── cell_feature_matrix.h5 
# compressed format of the below 


    └── cell_feature_matrix    
# segmentation-derived matrix files


      ├── barcodes.tsv 
# cell barcodes (i.e., sequences)


      ├── features.tsv 
# gene metadata (e.g., target type)


      └── matrix.mtx   
# (gene x cell) count matrix


    ├── transcripts.parquet        
# molecule locations


    ├── cell_boundaries.parquet    
# membrane segmentation


    ├── nucleus_boundaries.parquet 
# nuclear segmentation 


    └── experiment.xenium 
# experiment-wide metadata (in .json format)
