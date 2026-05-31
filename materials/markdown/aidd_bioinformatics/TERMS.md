# AIDD 字幕术语校正词典

| 模式 | 替换为 | 说明 |
|---|---|---|
| DSEC / DSEC2 / Deseq2 | DESeq2 | 差异表达常用 R 包 |
| RNA SEC / RNA 测序 / RNA-Seq | RNA-seq | 转录组测序 |
| FASCQ | FASTQ | 下机测序数据格式 |
| FASTA-A / pasta 文件 | FASTA / FASTA 文件 | 序列文件格式 |
| 氧化铝平台 / LuminaSec | Illumina 平台 / Illumina | Illumina 测序平台 |
| PECBio | PacBio | PacBio 长读测序平台 |
| Elad / Bota / Mr.Fast / Shreem | Eland / Bowtie / MrFAST / SHRiMP | 比对工具 |
| boros wheeler | Burrows-Wheeler | 算法/工具 |
| SAM 工具 / BCF 工具 | samtools / bcftools | 命令行工具 |
| sec.io / biosec.utils / biosec | SeqIO / Bio.SeqUtils / Bio.Seq | Biopython 模块 |
| Sketelearn | scikit-learn | 机器学习库 |
| 集合基因 / 集合基因 ID | Ensembl 基因 / Ensembl 基因 ID | 基因 ID 数据库 |
| 地理数据库 / 地理数据集 | GEO 数据库 / GEO 数据集 | GEO 公共数据库 |
| 近谷氨酸 | 核苷酸 | DNA/RNA 单体 |
| 变异比对 | 序列比对 | alignment |
| 线点 SAM / 线点 BAM / sort dot BAM | .sam / .bam / sort.bam | 文件名口语化错误 |
| 贝叶斯入门 / 贝叶斯 shell / 贝叶斯脚本 | bash 入门 / bash shell / bash 脚本 | bash 误识别为 Bayesian |

术语规则在 `scripts/convert/clean_aidd_subtitles.py` 中维护，更新规则后请重新运行脚本以再生成全部讲稿。