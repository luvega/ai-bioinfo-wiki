---
week: 14
title: 表达矩阵从哪里来
ppt_status: storyboard
review_status: evidence_review_pass
---

# Week 14 PPT Storyboard：表达矩阵从哪里来

本 storyboard 只用于审查 Week 14 的 PPT 结构和证据边界。当前状态是 `storyboard` 与 `evidence_review_pass`，尚未生成 PPTX，也尚未做 PNG/contact sheet 视觉 QA。

| Slide | Action title | Visual intent | Teacher note | Student action | Evidence/source note | Risk note |
|---:|---|---|---|---|---|---|
| 1 | 表达矩阵不是原始测序文件，而是经过流程加工后的统计输入 | 标题页，显示 FASTQ 到 count matrix 的简化链路 | 先把本周问题说清：Week 15 的 DESeq2 结果从哪里来 | 说出本周要追踪的输入和输出 | `script.md` 讲义使用说明；AIDD RNA-seq 上游流程 | 不把流程图讲成学生必跑命令 |
| 2 | 从样本表到表达矩阵要先定义观测单位 | 小表：sample_id、group、batch 与 gene counts | 让学生看到 metadata 与 count matrix 必须对齐 | 找出样本列和 metadata 行是否一一对应 | `outline.md` count matrix 核验任务 | 示例为教学模拟 |
| 3 | FASTQ / alignment / count 是三个不同层级的问题 | 三段流程卡：reads、alignment、counts | 只讲文件角色，不讲完整命令细节 | 给每个文件写一句“它服务哪一步” | AIDD Ch7；`knowledge/concepts/RNA-seq上游流程.md` | 软件名和命令进入 PPT 前需二次核对 |
| 4 | count matrix 与 metadata 对齐决定后续分析是否可信 | 3 genes x 4 samples 矩阵与 metadata 连线 | 样本名错位会让后续统计全部失效 | 手工检查 `Ctrl_1`、`Drug_1` 是否匹配 | Week 14 `script.md` classroom case | 不把模拟矩阵写成真实数据 |
| 5 | QC 和 normalization 是让比较更可信，不是让结论自动成立 | 前后对照：raw counts、library size、normalized counts | 强调总 counts 差异和标准化的必要性 | 计算一个样本总 counts 并解释风险 | Week 14 `materials.md`、SCBP/OSCA QC/normalization 备课 | 不展开高级模型或参数调优 |
| 6 | bulk、single-cell、spatial 的输入差异来自观测单位不同 | 三列表：sample x gene、cell x gene、spot x gene | 为 Week 16 做预告，只讲结构差异 | 判断三类矩阵的“行”分别是什么 | SCBP、OSCA、OSTA source pages | 不要求学生运行完整 workflow |
| 7 | AI 可以整理流程，不能替代上游质量判断 | 左侧 Prompt，右侧 AI 输出审计清单 | AI 只做流程梳理和风险提醒 | 修改 Prompt，加入“不编造结果”约束 | `knowledge/concepts/AI协作边界.md` | 不让 AI 伪造测序结果或 QC 结论 |
| 8 | 课堂出口卡检查三件事：来源、对齐、待核验 | 出口卡：数据从哪来、是否对齐、还要核验什么 | 收束到 Week 15 的差异表达输入 | 写出一条进入 Week 15 前必须核验的事项 | Week 14 `outline.md` 与 `script.md` | 不以“谢谢”页替代学习收束 |

## Evidence Checklist

- AIDD 上游流程中的软件名、命令名和文件格式进入 PPTX 脚本前需回查。
- 正式 PPT 默认使用教师自绘流程图和教学模拟矩阵；若改用外部图形，需重新进入 source review。
- 所有 count matrix、metadata、QC 和 normalization 示例必须标注“教学模拟”或给出可追溯来源。
- Week 14 只进入 storyboard review，不宣称 PPTX 完成。
