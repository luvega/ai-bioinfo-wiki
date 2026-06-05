---
source: OSCA
title: "Introduction to Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html
ingested_at: 2026-06-04T01:52:41+00:00
status: source_ingested
---

# [Introduction to Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.intro/)

# Chapter 3 Getting scRNA-seq datasets

## 3.1 Overview

Sequencing data from single-cell RNA-seq experiments must be converted into a matrix of expression values.
This is usually a count matrix containing the number of reads mapped to each gene (row) in each cell (column).
Alternatively, the counts may be that of the number of unique molecular identifiers (UMIs);
these are interpreted in the same manner as read counts but are less affected by PCR artifacts during library preparation (Islam et al. [2014](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-islam2014quantitative)).
Once this quantification is complete, we can proceed with our downstream statistical analyses in R.

Constructing a count matrix from raw scRNA-seq data requires some thought as the term “single-cell RNA-seq” encompasses a variety of different experimental protocols.
This includes droplet-based protocols like 10X Genomics, inDrop and Drop-seq;
plate-based protocols with UMIs like CEL-seq(2) and MARS-seq;
plate-based protocols with reads (mostly Smart-seq2);
and others like sciRNA-seq, to name a few.
Each approach requires a different processing pipeline to deal with cell demultiplexing and UMI deduplication (if applicable).
This chapter will briefly describe some of the methods used to generate a count matrix and read it into R.

## 3.2 Some comments on experimental design

Each scRNA-seq protocol has its own advantages and weaknesses that are discussed extensively elsewhere (Mereu et al. [2019](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-mereu2019benchmarking); Ziegenhain et al. [2017](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-ziegenhain2017comparative)).
In practical terms, droplet-based technologies are the current *de facto* standard due to their throughput and low cost per cell.
Plate-based methods can capture other phenotypic information (e.g., morphology) and are more amenable to customization.
Read-based methods provide whole-transcript coverage, which is useful in some applications (e.g., splicing, exome mutations); otherwise, UMI-based methods are more popular as they mitigate the effects of PCR amplification noise.
The choice of method is left to the reader’s circumstances - we will simply note that most of the downstream analysis is agnostic to the exact technology being used.

Another question is how many cells should be captured, and to what depth they should be sequenced.
The best trade-off between these two factors is an active topic of research (Zhang, Ntranos, and Tse [2020](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-zhang2020determining); Svensson, Veiga Beltrame, and Pachter [2019](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-svensson2019quantifying)), though ultimately, much depends on the scientific aims of the experiment.
If we are aiming to discover rare cell subpopulations, we would need more cells, whereas if we are aiming to quantify subtle differences, we would need more sequencing depth.
As of time of writing, an informal survey of the literature suggests that typical droplet-based experiments would capture anywhere from 10,000 to 100,000 cells, sequenced at anywhere from 1,000 to 10,000 UMIs per cell (usually in inverse proportion to the number of cells).
Droplet-based methods also have a trade-off between throughput and doublet rate that affects the true efficiency of sequencing.

For studies involving multiple samples or conditions, the design considerations are the same as those for bulk RNA-seq experiments.
There should be multiple biological replicates for each condition and conditions should not be confounded with batch.
Note that individual cells are not replicates; rather, we are referring to samples derived from replicate donors or cultures.
In fact, this adds another dimension into the resourcing equation - should we obtain more cells per sample at the cost of being able to sequence fewer samples?
The best answer depends on the sizes of the subpopulations involved, the ease with which they are distinguished from others, and their variability across different samples and conditions.
Such factors are rarely known ahead of time, so an informed decision on the design will often benefit from pilot experiments.

## 3.3 Creating a count matrix

As mentioned above, the exact procedure for quantifying expression depends on the technology involved:

* For 10X Genomics data, the `Cellranger` software suite (Zheng et al. [2017](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-zheng2017massively)) provides a custom pipeline to obtain a count matrix.
  This uses *STAR* to align reads to the reference genome and then counts the number of unique UMIs mapped to each gene.
* Alternatively, pseudo-alignment methods such as `alevin` (Srivastava et al. [2019](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-srivastava2019alevin)) can be used to obtain a count matrix from the same data.
  This avoids the need for explicit alignment, which reduces the compute time and memory usage.
* For other highly multiplexed protocols, the *[scPipe](https://bioconductor.org/packages/3.23/scPipe)* package provides a more general pipeline for processing scRNA-seq data.
  This uses the *[Rsubread](https://bioconductor.org/packages/3.23/Rsubread)* aligner to align reads and then counts reads or UMIs per gene.
* For CEL-seq or CEL-seq2 data, the *[scruff](https://bioconductor.org/packages/3.23/scruff)* package provides a dedicated pipeline for quantification.
* For read-based protocols, we can generally re-use the same pipelines for processing bulk RNA-seq data.
* For any data involving spike-in transcripts, the spike-in sequences should be included as part of the reference genome during alignment and quantification.

In all cases, the identity of the genes in the count matrix should be defined with standard identifiers from Ensembl or Entrez.
These provide an unambiguous mapping between each row of the matrix and the corresponding gene.
In contrast, a single gene symbol may be used by multiple loci, or the mapping between symbols and genes may change over time, e.g., if the gene is renamed.
This makes it difficult to re-use the count matrix as we cannot be confident in the meaning of the symbols.
(Of course, identifiers can be easily converted to gene symbols later on in the analysis.
This is the recommended approach as it allows us to document how the conversion was performed and to backtrack to the stable identifiers if the symbols are ambiguous.)

Depending on the process involved, there may be additional points of concern:

* Some feature-counting tools (e.g., `HTSeq`) will report mapping statistics in the count matrix, such as the number of unaligned or unassigned reads.
  While these values can be useful for quality control, they would be misleading if treated as gene expression values.
  Thus, they should be removed (or at least moved somewhere else) prior to further analyses.
* The most common spike-ins are those developed by the External RNA Controls Consortium (ERCC), which have names along the lines of ERCC-00002.
  For human data, one should be careful to distinguish these rows from an actual ERCC gene family that has gene symbols like *ERCC1*.
  This issue can be avoided altogether by using standard identifiers that are not susceptible to these naming conflicts.

## 3.4 Reading counts into R

### 3.4.1 From tabular formats

The next step is to import the count matrix into R.
Again, this depends on the output format of the aforementioned processing pipeline.
In the simplest case, the pipeline will produce a matrix in tabular format, which can be read in with standard methods like `read.delim()`.
We demonstrate below using a pancreas scRNA-seq dataset from Muraro et al. ([2016](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-muraro2016singlecell)) ([GSE85241](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE85241)):

Code to download file

```
library(BiocFileCache)
bfc <- BiocFileCache(ask=FALSE)
url <- file.path("ftp://ftp.ncbi.nlm.nih.gov/geo/series",
    "GSE85nnn/GSE85241/suppl",
    "GSE85241%5Fcellsystems%5Fdataset%5F4donors%5Fupdated%2Ecsv%2Egz")

# Making a symbolic link so that the later code can pretend
# that we downloaded the file into the local directory.
muraro.fname <- bfcrpath(bfc, url)
local.name <- URLdecode(basename(url))
unlink(local.name)
if (.Platform$OS.type=="windows") {
    file.copy(muraro.fname, local.name)
} else {
    file.symlink(muraro.fname, local.name)
}
```

```
mat <- as.matrix(read.delim("GSE85241_cellsystems_dataset_4donors_updated.csv.gz"))
dim(mat) # number of rows, number of columns
```

```
## [1] 19140  3072
```

In practice, a more efficient approach is to read in the table in sparse format using the `readSparseCounts()` function from the *[scuttle](https://bioconductor.org/packages/3.23/scuttle)* package.
This only stores the non-zero values and avoids spending memory on the majority of zeros in lowly-sequenced scRNA-seq experiments.

```
library(scuttle)
sparse.mat <- readSparseCounts("GSE85241_cellsystems_dataset_4donors_updated.csv.gz")
dim(sparse.mat)
```

```
## [1] 19140  3072
```

```
# We can see that it uses less memory compared to 'mat'.
object.size(sparse.mat)
```

```
## 150978872 bytes
```

```
object.size(mat)
```

```
## 471999152 bytes
```

On occasion, we may encounter count data stored in Excel files.
These can be extracted into a matrix using functions from the *[readxl](https://CRAN.R-project.org/package=readxl)* package,
as demonstrated for a dataset from Wilson et al. ([2015](https://bioconductor.org/books/3.23/OSCA.intro/getting-scrna-seq-datasets.html#ref-wilson2015combined)) ([GSE61533](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE61533)):

Code to download file

```
bfc <- BiocFileCache("raw_data", ask=FALSE)
wilson.fname <- bfcrpath(bfc, file.path("ftp://ftp.ncbi.nlm.nih.gov/geo/series",
    "GSE61nnn/GSE61533/suppl/GSE61533_HTSEQ_count_results.xls.gz"))
```

```
library(R.utils)
wilson.name2 <- "GSE61533_HTSEQ_count_results.xls"
gunzip(wilson.fname, destname=wilson.name2, remove=FALSE, overwrite=TRUE)
```

```
library(readxl)
all.counts <- read_excel("GSE61533_HTSEQ_count_results.xls")
gene.names <- all.counts$ID
all.counts <- as.matrix(all.counts[,-1])
rownames(all.counts) <- gene.names
dim(all.counts)
```

```
## [1] 38498    96
```

### 3.4.2 From *Cellranger* output

For 10X Genomics data, the *Cellranger* software suite will produce an output directory containing counts and feature/barcode annotations.
We can read this into R by supplying the directory path to `read10xCounts()` from the *[DropletUtils](https://bioconductor.org/packages/3.23/DropletUtils)* package,
as demonstrated below using a [4000 peripheral blood mononuclear cell dataset](https://support.10xgenomics.com/single-cell-gene-expression/datasets/2.1.0/pbmc4k).
Note that the function produces a `SingleCellExperiment` object containing the matrix, which we will discuss in more detail in the next chapter.

Code to download file

```
library(DropletTestFiles)
cached <- getTestFile("tenx-2.1.0-pbmc4k/1.0.0/filtered.tar.gz")
fpath <- "tenx-2.1.0-pbmc4k"
untar(cached, exdir=fpath)
```

```
library(DropletUtils)
sce <- read10xCounts("tenx-2.1.0-pbmc4k/filtered_gene_bc_matrices/GRCh38")
sce
```

```
## class: SingleCellExperiment 
## dim: 33694 4340 
## metadata(1): Samples
## assays(1): counts
## rownames(33694): ENSG00000243485 ENSG00000237613 ... ENSG00000277475
##   ENSG00000268674
## rowData names(2): ID Symbol
## colnames: NULL
## colData names(2): Sample Barcode
## reducedDimNames(0):
## mainExpName: NULL
## altExpNames(0):
```

We can also read in multiple count matrices by passing multiple directory paths to `read10xCounts()`.
Provided that all datasets have the same gene annotation, the function will be able to combine them into a single object.

Code to download file

```
# Making a copy and pretending it's a different sample,
# for demonstration purposes.
# TODO: actually get a different sample.
target <- paste0(fpath, '-2')
unlink(target)

if (.Platform$OS.type=="windows") {
    file.copy(fpath, target)
} else {
    file.symlink(fpath, target)
}
```

```
dirA <- "tenx-2.1.0-pbmc4k/filtered_gene_bc_matrices/GRCh38"
dirB <- "tenx-2.1.0-pbmc4k-2/filtered_gene_bc_matrices/GRCh38"
sce <- read10xCounts(c(dirA, dirB))
sce
```

```
## class: SingleCellExperiment 
## dim: 33694 8680 
## metadata(1): Samples
## assays(1): counts
## rownames(33694): ENSG00000243485 ENSG00000237613 ... ENSG00000277475
##   ENSG00000268674
## rowData names(2): ID Symbol
## colnames: NULL
## colData names(2): Sample Barcode
## reducedDimNames(0):
## mainExpName: NULL
## altExpNames(0):
```

It is worth noting that the *Cellranger* software suite is not the only approach to processing 10X Genomics data.
For example, `alevin` output can be read into R using the *[tximeta](https://bioconductor.org/packages/3.23/tximeta)* package,
while `kallisto`-`bustools` output can be read using the *[BUSpaRse](https://bioconductor.org/packages/3.23/BUSpaRse)* package.

### 3.4.3 From HDF5-based formats

A family of scRNA-seq storage formats is based around Hierarchical Data Format version 5 (HDF5).
These formats offer the ability to store, in the same file, both the expression values and associated gene and cell annotations.
One flavor of this approach is the H5AD format, which can be read into R as a `SingleCellExperiment` using the *[zellkonverter](https://bioconductor.org/packages/3.23/zellkonverter)* package.
We demonstrate below with an example dataset that is built into the package:

```
library(zellkonverter)
demo <- system.file("extdata", "krumsiek11.h5ad", package = "zellkonverter")
sce <- readH5AD(demo)
sce
```

```
## class: SingleCellExperiment 
## dim: 11 640 
## metadata(2): highlights iroot
## assays(1): X
## rownames(11): Gata2 Gata1 ... EgrNab Gfi1
## rowData names(0):
## colnames(640): 0 1 ... 158-3 159-3
## colData names(1): cell_type
## reducedDimNames(0):
## mainExpName: NULL
## altExpNames(0):
```

Another flavor is the Loom file format, which we can read into R with the *[LoomExperiment](https://bioconductor.org/packages/3.23/LoomExperiment)* package.
In this case, the procedure creates a `SingleCellLoomExperiment`, which is effectively a plug-and-play equivalent to the `SingleCellExperiment`.

```
library(LoomExperiment)
demo <- system.file("extdata", "L1_DRG_20_example.loom", package = "LoomExperiment")
scle <- import(demo, type="SingleCellLoomExperiment")
scle
```

```
## class: SingleCellLoomExperiment 
## dim: 20 20 
## metadata(4): CreatedWith LOOM_SPEC_VERSION LoomExperiment-class
##   MatrixName
## assays(1): matrix
## rownames: NULL
## rowData names(7): Accession Gene ... X_Total X_Valid
## colnames: NULL
## colData names(103): Age AnalysisPool ... cDNA_Lib_Ok ngperul_cDNA
## reducedDimNames(0):
## mainExpName: NULL
## altExpNames(0):
## rowGraphs(0): NULL
## colGraphs(2): KNN MKNN
```

The HDF5-based formats have an additional advantage in that Bioconductor-based analyses can be performed without reading all of the data into R.
This allows us to analyze very large datasets in the presence of limited computer memory, a functionality that we will discuss in more detail in [Advanced Chapter 14](http://bioconductor.org/books/3.23/OSCA.advanced/dealing-with-big-data.html#dealing-with-big-data).

## Session Info

View session info

```
R version 4.6.0 RC (2026-04-17 r89917)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /home/biocbuild/bbs-3.23-bioc/R/lib/libRblas.so 
LAPACK: /usr/lib/x86_64-linux-gnu/lapack/liblapack.so.3.12.0  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_GB              LC_COLLATE=C              
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: America/New_York
tzcode source: system (glibc)

attached base packages:
[1] stats4    stats     graphics  grDevices utils     datasets  methods  
[8] base     

other attached packages:
 [1] LoomExperiment_1.30.0       BiocIO_1.22.0              
 [3] rhdf5_2.56.0                zellkonverter_1.22.0       
 [5] DropletUtils_1.32.0         DropletTestFiles_1.21.0    
 [7] readxl_1.4.5                R.utils_2.13.0             
 [9] R.oo_1.27.1                 R.methodsS3_1.8.2          
[11] scuttle_1.22.0              SingleCellExperiment_1.34.0
[13] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[15] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[17] IRanges_2.46.0              S4Vectors_0.50.0           
[19] BiocGenerics_0.58.0         generics_0.1.4             
[21] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[23] BiocFileCache_3.2.0         dbplyr_2.5.2               
[25] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
 [1] DBI_1.3.0                 httr2_1.2.2              
 [3] CodeDepends_0.6.7         rlang_1.2.0              
 [5] magrittr_2.0.5            otel_0.2.0               
 [7] compiler_4.6.0            RSQLite_2.4.6            
 [9] dir.expiry_1.20.0         DelayedMatrixStats_1.34.0
[11] png_0.1-9                 vctrs_0.7.3              
[13] stringr_1.6.0             pkgconfig_2.0.3          
[15] crayon_1.5.3              fastmap_1.2.0            
[17] XVector_0.52.0            rmarkdown_2.31           
[19] graph_1.90.0              purrr_1.2.2              
[21] bit_4.6.0                 xfun_0.57                
[23] cachem_1.1.0              beachmat_2.28.0          
[25] jsonlite_2.0.0            blob_1.3.0               
[27] rhdf5filters_1.24.0       DelayedArray_0.38.0      
[29] Rhdf5lib_2.0.0            BiocParallel_1.46.0      
[31] parallel_4.6.0            R6_2.6.1                 
[33] stringi_1.8.7             bslib_0.10.0             
[35] reticulate_1.46.0         limma_3.68.0             
[37] jquerylib_0.1.4           cellranger_1.1.0         
[39] Rcpp_1.1.1-1.1            bookdown_0.46            
[41] knitr_1.51                Matrix_1.7-5             
[43] tidyselect_1.2.1          abind_1.4-8              
[45] yaml_2.3.12               codetools_0.2-20         
[47] curl_7.1.0                lattice_0.22-9           
[49] tibble_3.3.1              withr_3.0.2              
[51] KEGGREST_1.52.0           evaluate_1.0.5           
[53] ExperimentHub_3.2.0       Biostrings_2.80.0        
[55] pillar_1.11.1             BiocManager_1.30.27      
[57] filelock_1.0.3            BiocVersion_3.23.1       
[59] sparseMatrixStats_1.24.0  glue_1.8.1               
[61] tools_4.6.0               AnnotationHub_4.2.0      
[63] locfit_1.5-9.12           XML_3.99-0.23            
[65] grid_4.6.0                AnnotationDbi_1.74.0     
[67] edgeR_4.10.0              basilisk_1.24.0          
[69] HDF5Array_1.40.0          cli_3.6.6                
[71] rappdirs_0.3.4            S4Arrays_1.12.0          
[73] dplyr_1.2.1               sass_0.4.10              
[75] digest_0.6.39             SparseArray_1.12.0       
[77] dqrng_0.4.1               memoise_2.0.1            
[79] htmltools_0.5.9           lifecycle_1.0.5          
[81] h5mread_1.4.0             httr_1.4.8               
[83] statmod_1.5.1             bit64_4.8.0
```

### References

Islam, S., A. Zeisel, S. Joost, G. La Manno, P. Zajac, M. Kasper, P. Lonnerberg, and S. Linnarsson. 2014. “Quantitative single-cell RNA-seq with unique molecular identifiers.” *Nat. Methods* 11 (2): 163–66.

Mereu, Elisabetta, Atefeh Lafzi, Catia Moutinho, Christoph Ziegenhain, Davis J. MacCarthy, Adrian Alvarez, Eduard Batlle, et al. 2019. “Benchmarking Single-Cell Rna Sequencing Protocols for Cell Atlas Projects.” *bioRxiv*. <https://doi.org/10.1101/630087>.

Muraro, M. J., G. Dharmadhikari, D. Grun, N. Groen, T. Dielen, E. Jansen, L. van Gurp, et al. 2016. “A Single-Cell Transcriptome Atlas of the Human Pancreas.” *Cell Syst* 3 (4): 385–94.

Srivastava, A., L. Malik, T. Smith, I. Sudbery, and R. Patro. 2019. “Alevin efficiently estimates accurate gene abundances from dscRNA-seq data.” *Genome Biol* 20 (1): 65.

Svensson, V., E. da Veiga Beltrame, and L. Pachter. 2019. “Quantifying the Tradeoff Between Sequencing Depth and Cell Number in Single-Cell Rna-Seq.” *bioRxiv*, 762773.

Wilson, N. K., D. G. Kent, F. Buettner, M. Shehata, I. C. Macaulay, F. J. Calero-Nieto, M. Sanchez Castillo, et al. 2015. “Combined single-cell functional and gene expression analysis resolves heterogeneity within stem cell populations.” *Cell Stem Cell* 16 (6): 712–24.

Zhang, M. J., V. Ntranos, and D. Tse. 2020. “Determining sequencing depth in a single-cell RNA-seq experiment.” *Nat Commun* 11 (1): 774.

Zheng, G. X., J. M. Terry, P. Belgrader, P. Ryvkin, Z. W. Bent, R. Wilson, S. B. Ziraldo, et al. 2017. “Massively parallel digital transcriptional profiling of single cells.” *Nat Commun* 8 (January): 14049.

Ziegenhain, C., B. Vieth, S. Parekh, B. Reinius, A. Guillaumet-Adkins, M. Smets, H. Leonhardt, H. Heyn, I. Hellmann, and W. Enard. 2017. “Comparative Analysis of Single-Cell RNA Sequencing Methods.” *Mol. Cell* 65 (4): 631–43.
