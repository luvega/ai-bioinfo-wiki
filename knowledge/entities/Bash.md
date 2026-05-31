---
type: entity
name: Bash
aka: [shell, bash shell]
category: language-shell
domain: [unix, pipeline, automation, bioinformatics]
status: stable
tags: [bash, shell, pipeline, linux, wsl]
---

# Bash

## 定位

Unix/Linux 命令行 shell，本课程的**辅助工具**——
**只在"流程思维与命令行示范"语境下出现**，不要求学生独立写复杂脚本。

## 在本课程中的使用范围

| 周 | 用 Bash 干什么 |
|---:|---|
| 2 | 演示项目目录结构、git 命令、命令行复现优势 |
| 5 | （选讲）用 awk/sed 处理大型 CSV |
| 11 / 16 | 演示 RNA-seq pipeline 的命令序列（不要求学生跑） |
| 16 | 演示 Variant Calling pipeline |

## 关键命令清单（最低要求）

| 类别 | 命令 |
|---|---|
| 导航 | `pwd`、`cd`、`ls`、`tree` |
| 文件 | `cp`、`mv`、`rm`、`mkdir`、`touch` |
| 查看 | `cat`、`less`、`head`、`tail`、`wc -l` |
| 检索 | `grep`、`find` |
| 文本 | `cut`、`sort`、`uniq`、`awk`、`sed` |
| 流程 | `|`（管道）、`>` `>>`（重定向）、`&&` `||` |
| 远程 | `ssh`、`scp`、`rsync`（生信常用） |
| 包管理 | `apt` / `conda` / `mamba` |

## WSL（Windows Subsystem for Linux）

来源：AIDD [Ch.5 Linux for Windows Users (WSL)](../sources/AIDD_Bioinformatics_Course.md)。
本课程面向药学学生，多数使用 Windows，建议第 2 周用 5-10 分钟演示
`wsl --install` 并展示一次"在 Windows 上跑 bash 命令"。

## 与 AIDD 的关系

- AIDD [Ch.4 Bash for bioinformatics](../sources/AIDD_Bioinformatics_Course.md)：bash 基础 + NCBI E-utilities + BLAST。
- AIDD [Ch.6 Bioinformatics Pipeline](../sources/AIDD_Bioinformatics_Course.md)：pipeline 思维。
- AIDD [Ch.7 / Ch.8](../sources/AIDD_Bioinformatics_Course.md)：NGS / Variant Calling 全是 Bash。

## 机翻陷阱

AIDD 字幕里 "bash" 多次被误识别为 "贝叶斯"。看到 "贝叶斯入门" / "贝叶斯脚本" 请理解为 bash。
详见 [TERMS.md](../../materials/raw/aidd_bioinformatics/TERMS.md)。

## 与 AI 协作（红线）

- **绝不直接复制粘贴 `rm -rf`**、`mv ... ../../`、`> /etc/...`。
- AI 给的命令行流程**可能版本不匹配**：例如 `samtools sort -O bam` 在不同版本参数不同。
- 推荐：先在容器或 WSL 中跑一遍，确认输入输出再放进项目脚本。

## 相关页面

- 概念：[工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md) · [RNA-seq 上游流程](../concepts/RNA-seq上游流程.md) · [Variant Calling 流程](../concepts/Variant_Calling流程.md) · [项目目录结构与可复现](../concepts/项目目录结构与可复现.md)
- 实体：[samtools](samtools.md) · [BLAST](BLAST.md)
- 来源：[AIDD Ch.4-8](../sources/AIDD_Bioinformatics_Course.md)
