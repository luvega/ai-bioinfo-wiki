---
type: trial-teaching-pack
week: 4
title: R 基础语法、数据框操作与 AI 代码核验 · 试讲包 v1
status: trial_ready_pack_v1
updated: 2026-06-04
audience: 药学本科生
duration: 2 学时
---

# Week 04 试讲包 v1

## 2 学时时间切分

| 时间 | 活动 | 教师动作 | 学生可提交产物 |
|---:|---|---|---|
| 0-10 min | Python 到 R 迁移 | 对照 list/data.frame 的直觉 | R 对象标注 |
| 10-35 min | 小表读码 | 解释 `data.frame`、列名、factor | 代码注释 |
| 35-60 min | 运行与核验 | 检查 summary 输出和字段含义 | 输出解释 |
| 60-80 min | AI 报错审计 | 让 AI 只解释错误，不重写大段代码 | 报错记录 |
| 80-90 min | 小结 | 连接 Week 05 数据读取 | 核验点 3 条 |

## 课堂小数据与代码

```r
drug <- data.frame(
  patient_id = c("P01", "P02", "P03", "P04"),
  group = factor(c("Control", "Control", "Drug", "Drug")),
  concentration = c(2.1, 2.4, 3.8, 4.0),
  adverse_event = c(FALSE, TRUE, FALSE, TRUE)
)
summary(drug)
```

## 预期输出与参考答案

- `patient_id` 是标识符，不应求均值。
- `group` 是分组因子，服务后续分组统计和作图。
- `concentration` 是数值列，可以描述分布。
- `adverse_event` 是布尔变量，不能和浓度直接混为同一量纲。

评分点：对象识别 25%，代码注释 25%，输出解释 25%，AI 报错核验 25%。

## 常见误区

- 把 `patient_id` 当数值变量。
- 复制 AI 生成代码但不运行。
- 没有说明 factor 水平和分组含义。

## AI 审计提示

```text
请解释这段 R 代码每一列的数据类型和 summary 输出。
不要新增列，不要改写完整代码，不要判断药物安全性。
```
