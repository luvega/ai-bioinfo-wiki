---
type: course-week
week: 5
title: 数据读取与整理
hours: 2
status: pilot_candidate
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 05 周：数据读取与整理 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## AIDD 候选素材

- 从 [AIDD 课程索引](../../../materials/markdown/aidd_bioinformatics/aidd.course_index.md) 和相关 `chapter.course.md` 选取；字幕原文只作术语核验，不直接进入课堂。

## PDF / 外部 PPT 候选素材

- 从 `materials/markdown/pdf_library_mineru/` 和 `materials/markdown/pdf_library_skill_extract/` 选取已转换 Markdown；原始 PDF/PPT 不直接进入课程引用。

## 素材分层使用原则（2026-06-04）

- 课堂主素材：CSV/Excel/TSV 读取、列名整理、类型识别、长宽表转换。
- 支撑素材：AIDD 文件格式和 count matrix 准备内容；GenAI 数据分析参考用于数据工作流。
- 拓展素材：FASTQ/SAM/BAM 只作为文件格式有结构的类比，不讲上游 pipeline。
- 教师备课素材：PDF skill extract 和 MinerU 结果用于补充数据读入示例，进入课堂前重写为小表格。
- 教材 / PPT 边界：可进 PPT：原始表到分析表的转换流程、字段字典。

## 可进 PPT 的元素

- 概念图：原始表、字段字典、整理后分析表和长宽表选择流程。
- 示例表格：`ID/Group/Glu_pre/Glu_post/Unit` 到规范列名的转换示例。
- 代码片段：读取 CSV/Excel 后检查列名和类型的最小代码。
- AI 提示词：检查数据字典是否遗漏字段类型、单位和来源核验。

## 试点候选审查依据（2026-06-04）

- 课堂任务：把一个原始 CSV/Excel 小表整理成可分析表，补齐字段字典，并说明长表与宽表各适合回答什么问题。
- 评价证据：提交 `data_dictionary`、读取代码、整理前后表格对照和至少 3 条字段核验记录。
- AI 协作边界：允许 AI 建议字段说明、检查列名一致性和提示类型转换风险；禁止 AI 伪造数据来源、自动删除字段或替代学生判断单位含义。
- 待核验点：正式素材前需确认示例表不含真实学生或患者隐私，Excel/CSV 编码在 Windows 环境可读。
