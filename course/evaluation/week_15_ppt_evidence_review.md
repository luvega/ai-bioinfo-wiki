---
type: course-ppt-evidence-review
week: 15
title: 差异表达分析与功能解读 PPT 证据审查
status: pass
review_target: ../weeks/week_15/ppt_storyboard.md
---

# Week 15 PPT 证据审查

## Verdict

pass

Week 15 storyboard 可以进入 SYSU 官方蓝模板 PPTX 生成。当前版本把差异表达、火山图、热图、功能解读和 AI 协作都限定为教学模拟、候选解释或需核验流程，没有把基因功能、通路机制、药物疗效或临床意义写成事实结论。

## Findings

| Severity | Location | Issue | Fix |
|---|---|---|---|
| note | Slide 4、7、9、11 | 小表、火山图和热图均为课堂模拟数据 | 幻灯片内必须显式标注“教学模拟，不代表真实医学结论” |
| note | Slide 5 | DESeq2 流程只适合本科课堂概念层讲解 | 不展开负二项模型推导；如教师扩展，需补充教材或文献来源 |
| note | Slide 8 | 多重检验解释容易被学生简化成“padj 永远更正确” | 表述为“本课堂关注校正后显著性以降低大量检验中的假阳性风险” |
| note | Slide 12、13、17 | GO、Reactome、STRING 和功能解释只提供候选证据 | 所有功能、机制、通路活性、药物作用相关说法都保留“需数据库或文献核验” |
| note | Slide 14 | AI 可能编造基因功能、通路机制或数据库结论 | Prompt 和审计清单必须明确“不要编造；未提供来源必须标注需核验” |

## Claim-Evidence Gate

| Claim | Evidence status | Action |
|---|---|---|
| `padj` 和 `log2FoldChange` 共同筛选候选基因 | 由 Week 15 讲义和课堂小表支持 | 可进入 PPT；限定为课堂筛选规则 |
| 火山图同时表达效应量和显著性 | 由 Week 15 讲义和大纲支持 | 可进入 PPT；不得延伸为机制解释 |
| 热图展示表达模式，不替代统计检验 | 由 Week 15 讲义和大纲支持 | 可进入 PPT；强调图形观察边界 |
| GO、Reactome、STRING 可用于功能候选解释 | 需数据库或文献核验 | 可作为流程页；不得写成机制事实 |
| 特定基因与疾病、药物或通路机制相关 | 当前 storyboard 未提供真实数据库或文献来源 | 不进入结论；若出现必须标注需数据库或文献核验 |
| AI 可以生成筛选规则、图注模板和审计清单 | 课程 AI 协作规则支持 | 可进入 PPT；必须称为候选输出 |

## Next Checks

- 生成 PPTX 后检查所有模拟表格、火山图、热图是否带有“教学模拟，不代表真实医学结论”。
- 检查幻灯片标题是否均为 action title，而不是 topic label。
- 扫描 `final.pptx` 文本层，确认没有出现未核验的“证明”“揭示机制”“治疗有效”“通路被激活”等过度主张；模板占位符扫描不得命中未清理的模板文字。
- 视觉 QA 时重点检查表格、火山图、热图、AI Prompt 和证据门流程是否清晰可读。
