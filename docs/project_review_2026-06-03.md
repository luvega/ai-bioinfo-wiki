# AI_Course 技能与状态收口 Review · 2026-06-03

评审对象：`E:\Codex_Projects\AI_Course`

本页记录本轮“技能+状态收口”后的项目判断。它不是内容扩写计划，也不是 PPT 全量生产计划。

## 总体判断

项目主线已经稳定为 courseware-first：`course/` 是课程生产主线，`knowledge/` 是备课辅助层，`outputs/` 是本地导出层且不入 Git。当前结构、技能清单、索引、断链、样板周质量和测试门禁均可用。

最需要避免的误读是：18 周 `script.md` 已达到 `formal_ready/full-lecture`，但这只说明讲义深度达标；非样板周的 `materials.md` 与 `outline.md` 仍为 `draft`，不能自动进入 PPT 或公开发布。

## 1. 知识库与课程主线

优点：

- `materials/`、`knowledge/`、`course/` 三层职责清楚，且 `course/syllabus/` 优先级最高。
- `course_km_index.py` 能维护周次索引、素材索引、knowledge 分区索引、Markdown 链接和 Week 11/15 历史错位。
- `course-skill-router` 已明确先读课程主线，再回到 `knowledge/` 取素材。

待守住的边界：

- `knowledge/` 不得反向覆盖 `course/syllabus/` 或 `course/weeks/`。
- 旧 `F:\AI_Course` 只可作为历史迁移线索，不作为工作区、回退目录或 Obsidian vault。

## 2. 技能体系

当前可用技能：

- 全局白名单 13 个：`building-llm-wiki`、`academic-chinese-style`、`scientific-critical-thinking`、`peer-review`、`scientific-writing`、`scientific-slides`、`scientific-visualization`、`statistical-analysis`、`markdown-mermaid-writing`、`academic-presentation-teaching`、`biomedical-research-framework`、`office-academic-skill`、`research-writing-skill`。
- 项目本地主 workflow 5 个：`course-skill-router`、`course-lecture-expand`、`course-ppt-storyboard`、`course-evidence-review`、`course-update-vault`。
- 本地工具型 skills 仍可按需用于 PPTX、DOCX、PDF、XLSX、Marp、网页和文献检索，但不能决定课程写入位置或状态标签。

维护方式：

- `docs/skill_loading_manifest_2026-06-03.md` 记录来源、commit、license 状态和用途。
- `skills/README.md` 记录本地 32 个 skills 的分类。
- `scripts/maintenance/course_skill_inventory.py --check` 机器检查全局白名单、本地 `course-*` 和 README 数量。

## 3. 课程产物状态

当前事实：

- `course/weeks/week_01` 到 `week_18` 均有 `materials.md`、`outline.md`、`script.md`。
- 18 周 `script.md` 均为 `formal_ready/full-lecture`，深度报告见 `docs/course_script_depth_report.md`。
- Week 03/14/15/16 是样板周，`materials.md` 与 `outline.md` 为 `pilot_ready`。
- 其余周次的 `materials.md` 与 `outline.md` 仍为 `draft`；这表示整周课件准备度还没有提升到样板周水平。

状态解释：

- 讲义状态：由 `script.md` frontmatter 和 `course_script_depth.py` 判断。
- 周次状态：由 `materials.md`、`outline.md`、样板周质量区块和人工评审共同判断。
- PPT 状态：由 storyboard、evidence review、PPTX、PNG/contact sheet QA 判断。

## 4. PPT 生产线

当前成果：

- Week 03 已有 12 页 PPT 试点样稿和 PowerPoint COM PNG 预览记录。
- Week 15 已有 `course/weeks/week_15/ppt_storyboard.md`、`course/evaluation/week_15_ppt_evidence_review.md`、SYSU 官方蓝模板 PPTX、PNG 预览和 contact sheet QA。
- Week 15 QA 明确所有课堂表格和图均为教学模拟，不代表真实医学结论。

当前不做：

- 不启动 18 周全量 PPT。
- 不把 `outputs/ppt/` 中的 PPTX、PNG、contact sheet、提取文本或 QA 输出纳入 Git。
- 不把 `formal_ready/full-lecture` 自动解释为 PPT 可生成状态。

## 5. 科学与教学风险

需要持续审查：

- 基因功能、通路机制、细胞类型注释、药物疗效或临床意义必须有数据库或文献来源；没有来源时标注“需数据库或文献核验”。
- `padj`、`log2FoldChange`、UMAP、cluster、marker 等解释必须区分“图上可见”“统计候选”和“生物学结论”。
- AI 输出只可作为候选规则、候选解释、候选代码、候选图注或核验清单，不作为权威结论。

## 6. Git 与基线收口

当前本地状态：

- `main` 相对 `origin/main` 为 ahead 6 / behind 0。
- 本轮工作树改动按四组审计：技能体系、18 周讲义扩写、Week 15 PPT 试点、项目说明/状态文档。
- 不 push、不改远端可见性、不删除远端仓库，除非用户再次明确确认。

## 下一步 Backlog

| Priority | Task | 验收 |
|---:|---|---|
| P0 | 收口技能与状态文档 | README、AGENTS、memory、skill manifest、skills README 和深度报告语义一致 |
| P0 | 保持维护门禁通过 | `course_skill_inventory.py --check`、`course_km_index.py --check`、`course_quality_check.py --check`、`pytest` 全部通过 |
| P1 | Week 15 PPT 试点归档说明 | storyboard、evidence review、QA note 和输出路径边界清楚 |
| P1 | Week 16 PPT 前先做 storyboard | 每页 action title、visual intent、teacher note、student action、evidence/source、risk note 齐全 |
| P2 | 提升非样板周 materials/outline | 按周把 `draft` 推进为可审查页级大纲，不靠讲义深度自动升级 |
