---
type: trial-teaching-pack
week: 5
title: 数据读取与整形 · 试讲包 v1
status: trial_ready_pack_v1
updated: 2026-06-04
audience: 药学本科生
duration: 2 学时
---

# Week 05 试讲包 v1

## 2 学时时间切分

| 时间 | 活动 | 教师动作 | 学生可提交产物 |
|---:|---|---|---|
| 0-10 min | 原始表问题 | 展示列名混乱的小表 | 问题标注 |
| 10-30 min | 数据读取 | 说明 CSV/Excel/TSV 和编码风险 | 读取记录 |
| 30-55 min | 数据字典 | 逐列写字段、单位、类型、用途 | `data_dictionary` |
| 55-75 min | 长宽表判断 | 比较按样本宽表和按观测长表 | 整形计划 |
| 75-90 min | 核验 | 抽查字段和来源 | 修订清单 |

## 课堂小数据

| ID | Group | Glu_pre | Glu_post | Unit |
|---|---|---:|---:|---|
| P01 | Ctrl | 8.1 | 8.0 | mmol/L |
| P02 | Ctrl | 7.5 | 7.7 | mmol/L |
| P03 | Drug | 8.4 | 6.9 | mmol/L |
| P04 | Drug | 9.1 | 7.2 | mmol/L |

任务：把列名改写为 `patient_id`, `group`, `glucose_before`, `glucose_after`, `unit`，并写数据字典。

## 预期输出与参考答案

- 预期输出：整理后表格、字段字典、3 条来源/单位核验记录。
- 参考答案要点：`Unit` 必须保留；`Glu_pre` 和 `Glu_post` 不应只靠猜测解释；长表适合后续按 time 作图。
- 评分点：列名规范 25%，字段字典 35%，整形理由 20%，核验记录 20%。

## 常见误区

- 删除单位列。
- 把 Ctrl/Drug 的缩写含义交给 AI 猜。
- 为了作图随意改变样本编号。

## AI 审计提示

```text
请检查这个数据字典是否遗漏字段类型、单位和来源核验。
不要替我猜测缩写含义，不要删除任何字段。
```
