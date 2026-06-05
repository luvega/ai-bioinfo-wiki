# memory.md · AI_Course 跨会话记忆

本文记录 AI_Course 的稳定偏好、项目决策、当前状态和反向规则。它会随项目演化更新。

## 0. 元信息

- 项目：医药数据处理与可视化（36 课时 · AI 前置版）课程课件生产工作区。
- 当前唯一有效根目录：`E:\Codex_Projects\AI_Course\`。
- 旧根目录：`F:\AI_Course\` 已在 2026-05-31 清空并删除，不再作为回退点。
- Obsidian Vault：从 `E:\Codex_Projects\AI_Course\` 打开。
- 当前范式：courseware-first；`knowledge/` 是备课辅助层，`course/` 是课程生产主线。
- 远端仓库：private GitHub；默认在完成一轮实现与本地验证后提交并推送当前分支，方便用户检查；公开、改远端可见性、删除远端或重写远端历史前必须二次确认。

## 1. 用户偏好

- 中文为主，专业术语可保留英文，如 DESeq2、ggplot2、scRNA-seq、samtools、bcftools。
- 面向药学本科生，不默认生信或统计背景。
- 解释时优先使用药效、临床指标、表达矩阵、科研图表、药物作用机制等医药案例。
- AI 用于解释、局部生成、核验、重构，不替代医学判断、统计判断或真实数据核验。
- 使用标准 Markdown 链接，不使用 Obsidian `[[wiki link]]`。
- 项目本地 skills 只保留在本项目，不写回全局 Codex skills。

## 2. 项目决策

### [2026-05-24] D-012 · 从 wiki-first 改为 courseware-first

- `knowledge/` 保留原 wiki 的 source/entity/concept/topic/synthesis 组织方式，但只作为备课辅助。
- `course/` 是正式大纲、周次产物、模板和考核主线。
- `materials/` 保存原始素材和转换 Markdown。
- `outputs/` 保存最终导出物，不进入 Git。

### [2026-05-24] D-013 · 当前课程周次基准

以 `course/syllabus/36课时-AI前置调整版.docx` 和主讲稿为准：

| 周次 | 主题 |
|---:|---|
| 01 | 课程导论与医药数据特征 |
| 02 | 数据分析流程、复现规范与人机协作规范 |
| 03 | AI 辅助编程与 Python 快速入门 |
| 04 | R 基础语法、数据框操作与 AI 代码核验 |
| 05 | 数据读取与整理 |
| 06 | 缺失值、异常值处理与分组汇总 |
| 07 | 描述统计与分布可视化 |
| 08 | 统计推断基础 |
| 09 | 相关分析与线性回归 |
| 10 | 分类问题与逻辑回归 |
| 11 | 科研图表规范与 SCI 图表表达 |
| 12 | 高维数据与数学直觉 |
| 13 | PCA、聚类与热图 |
| 14 | 转录组数据分析基础 |
| 15 | 差异表达分析与功能解读 |
| 16 | 单细胞转录组可视化 |
| 17 | 综合项目工作坊：AI 协作分析与结果核验 |
| 18 | 综合项目汇报与课程总结 |

历史注意：早期 wiki 曾把 Week 11 作为 DESeq2/富集分析主周次；当前应统一到 Week 15。

### [2026-05-21] D-007 · Git 边界

- 入 Git：`AGENTS.md`、`memory.md`、`README.md`、`.gitignore`、`course/`、`knowledge/`、`materials/markdown/`、`materials/raw/aidd_bioinformatics/`、`scripts/`、`docs/`、`.obsidian/` 中的团队配置。
- 不入 Git：`materials/raw/pdf_originals/`、`materials/raw/external_ppt/`、`outputs/`、`ai_logs/`、`projects/`、`.obsidian/workspace.json`、`site/node_modules/`、`site/dist/`、缓存和临时文件。

### [2026-05-24] D-014 · 项目本地 skills

- `skills/` 来自项目根目录 `skills.zip`，作为 AI_Course 本地能力包。
- 不复制到全局 `$CODEX_HOME/skills`，除非用户明确要求。
- 可服务 PPT、DOCX、XLSX、Marp、Markdown 转换、讲稿写作、文献检索和前端展示。

### [2026-05-31] D-018 · E 盘为唯一真源

- 当前有效工作区统一为 `E:\Codex_Projects\AI_Course\`。
- `F:\AI_Course\` 已删除，避免后续 Codex/Obsidian/Git 操作分叉。
- 后续结构提交前，先完成迁移边界核对清单和样板周质量检查。

### [2026-05-31] D-019 · Week 03/15/16 进入可授课试点

- Week 03、Week 15、Week 16 的 `materials.md`、`outline.md`、`script.md` 已统一标记为 `pilot_ready`。
- 三周均补齐试点交付清单、12 页页级大纲、2 学时授课流程、课堂预期答案和 AI 协作边界。
- 试点周仍不等于最终 PPT；进入 PPT 前还需要人工复核图表授权、文字溢出、示例图来源和课堂运行节奏。

### [2026-05-31] D-020 · 课程质量 Rubric 落地

- 新增 `course/evaluation/courseware_rubric.md`，用 8 个维度评估课程周次材料、PPT 大纲、授课脚本和后续 PPT 样稿。
- 新增 Week 03、Week 15、Week 16 三份试点评审记录，用于把 `pilot_ready` 从结构状态推进到人工质量评审状态。
- 后续进入 PPT 前，优先处理每份试评记录中的“进入 PPT 前需处理”项。

### [2026-05-31] D-021 · Week 14 进入可授课试点

- Week 14 已从 `first_round` 提升为 `pilot_ready`，定位为 Week 15 差异表达分析的上游铺垫。
- Week 14 补齐 count matrix、metadata、总 counts 核验、12 页页级大纲、2 学时授课流程和 rubric 试评。
- Week 14 进入 PPT 前仍需核对 AIDD 上游流程中的命令名、软件名和文件格式表述。

### [2026-05-31] D-022 · Week 03 PPT 试点样稿

- 新增 `scripts/courseware/build_week03_pilot_ppt.py`，可从 Week 03 试点稿生成 12 页可编辑 PPTX。
- 新增 `scripts/courseware/export_pptx_preview.ps1`，用本机 PowerPoint COM 将 PPTX 导出为 PNG 预览。
- Week 03 样稿输出到 `outputs/ppt/week_03_pilot/`，不入 Git；验证记录写入 `docs/week03_ppt_trial.md`。
- 首轮视觉检查发现第 12 页文字截断，已修复脚本并重新导出验证。

### [2026-05-31] D-023 · 讲义深度标准与 Week 03 扩写样本

- 新增 `course/evaluation/lecture_script_standard.md`，将每周讲义分为 `scaffold`、`pilot-script`、`full-lecture` 三个深度等级。
- 新增 `scripts/maintenance/course_script_depth.py`，用于报告 18 周 `script.md` 的汉字量和深度标签。
- Week 03 `script.md` 已从试讲提示扩写为 `pilot-script` 样本，补充完整讲述话术、互动追问、误区纠偏、AI 审计和评分点。

### [2026-06-03] D-024 · 双层技能体系落地

- 全局技能采用最小白名单，不全量安装外部 skill 仓库。
- 已确认或安装：`building-llm-wiki`、`academic-chinese-style`、`scientific-critical-thinking`、`peer-review`、`scientific-writing`、`scientific-slides`、`scientific-visualization`、`statistical-analysis`、`markdown-mermaid-writing`、`academic-presentation-teaching`、`biomedical-research-framework`、`office-academic-skill`、`research-writing-skill`。
- 新增项目本地 `course-skill-router`、`course-lecture-expand`、`course-ppt-storyboard`、`course-evidence-review`、`course-update-vault`。
- 新增 `docs/skill_loading_manifest_2026-06-03.md` 和 `scripts/maintenance/course_skill_inventory.py`，将全局白名单、本地 wrapper 和 README 数量纳入机器检查。

### [2026-06-03] D-025 · 18 周讲义扩写到 full-lecture

- Week 01-18 的 `script.md` 均已标记为 `formal_ready`，并达到 `full-lecture` 字数深度。
- `docs/course_script_depth_report.md` 只衡量 `script.md` frontmatter 状态和汉字量；它不自动把整周 `materials.md`、`outline.md` 或 PPT 状态提升为正式完成。
- Week 03/14/15/16 仍是当前样板周；其余周次虽然讲义深度足够，但 `materials.md` 和 `outline.md` 仍保持 `draft`，需要后续按周提升。

### [2026-06-03] D-026 · 技能与状态收口基线

- 项目采用 `course-skill-router` + `course-update-vault` 作为第一阶段技能与状态收口入口。
- 全局 13 个白名单技能和项目本地 5 个 `course-*` workflow skills 由 `docs/skill_loading_manifest_2026-06-03.md`、`skills/README.md` 和 `scripts/maintenance/course_skill_inventory.py` 三方共同约束。
- Week 15 已完成 PPT storyboard、evidence review、SYSU 官方蓝模板 PPTX、PowerPoint COM PNG 导出和 contact sheet QA；PPT 产物保留在 `outputs/`，不进入 Git。
- 本轮 Git 改动按四组审计：技能体系、18 周讲义扩写、Week 15 PPT 试点、项目说明/状态文档。

### [2026-06-04] D-027 · 18 周教材扩写稿与 40 页 storyboard 审核基线

- Week 01-18 均已生成 `course/weeks/week_XX/ppt_storyboard.md`，当前 `ppt_status: storyboard_expanded`。
- Week 01-18 均已生成 `course/textbook/chapters/chapter_XX.md`，当前 `textbook_status: expanded_draft`。
- `storyboard_expanded` 只表示 40 页主干源稿完成，不表示 PPTX、PNG、contact sheet 或视觉 QA 完成。
- 下一阶段 Coursebook 用作人工精修审核入口，重点检查 `Student action`、`Timing`、教师讲解重复度、证据 note 具体性和去模板化质量。
- Week 03/05/08/11/12/13/15/16/18 是 storyboard 去模板化重点精修周。

### [2026-06-05] D-028 · 教材与课件双主线入口

- Coursebook 只作为教材章节、知识体系、知识图谱和素材资产入口。
- Courseware / Teaching Plan 作为周次教学计划、90 分钟时间切分、PPT storyboard 和审核指标入口。
- `outline.md` 回答“本周教什么”，`teaching_plan.md` 回答“90 分钟怎么教”，`ppt_storyboard.md` 回答“每页投屏源稿怎么呈现”，`chapter_XX.md` 回答“知识体系如何组织”。
- 18 周均新增 `course/weeks/week_XX/teaching_plan.md`，并由 `course/textbook/coursebook_map.yml` 的 `teaching_plan_source` 字段显式引用。
- 教材章节不再逐页复述 40 张 storyboard；`Storyboard 对应表` 只作为索引，不作为正文展开顺序。

### [2026-06-05] D-029 · 默认提交并推送

- 用户确认后续每轮实现默认提交并推送当前分支，便于线上检查和 PR 审阅。
- 该默认规则只覆盖普通 commit/push；公开仓库、改变远端可见性、删除远端、强推或重写远端历史仍需再次明确确认。

### [2026-06-05] D-030 · 中文 PDF 教材全文入库

- 新增 `scripts/convert/ingest_local_pdf_textbooks.py`，用于本地 PDF 文本层抽取与 Tesseract OCR。
- `生物医药大数据与智能分析.pdf` 已完成文本层全文入库：`materials/markdown/pdf_library_local_text/Biomedical_Big_Data_Intelligent_Analysis/book.fulltext.md`。
- `Python程序设计-以医药数据为例.pdf` 无可用文本层，已用 Tesseract `chi_sim+eng`、220 DPI、PSM 3 完成 335 页 OCR：`materials/markdown/pdf_library_local_text/Python_Programming_Medical_Data/book.fulltext.md`。
- 页级缓存保留在 `outputs/pdf_library_local_text_cache/`，不入 Git；原始 PDF 仍保持只读且由 `.gitignore` 排除。
- OCR 全文只用于检索和备课定位；代码、表格、函数名和原文引用进入课件前必须回原始 PDF 人工核验。

## 3. 当前状态

- `course/weeks/week_01` 到 `week_18` 已有 `materials.md`、`outline.md`、`script.md`、`teaching_plan.md` 和 40 页主干 `ppt_storyboard.md`。
- `course/textbook/chapters/chapter_01.md` 到 `chapter_18.md` 已进入 `expanded_draft`，并改为知识体系正文；与 40 页 storyboard 的关系只保留为索引表。
- 两本中文 PDF 教材已进入 `materials/markdown/pdf_library_local_text/`：`生物医药大数据与智能分析` 为文本层抽取，`Python程序设计-以医药数据为例` 为 Tesseract OCR。
- 样板周优先级：Week 03、Week 14、Week 15、Week 16 已进入可授课试点；Week 13 已进入试讲就绪样章。
- 课程质量 rubric 已新增，位置为 `course/evaluation/courseware_rubric.md`。
- Week 03 已有 PPT 试点样稿生成脚本和真实 PNG 页面验证记录。
- Week 01-18 的 `script.md` 均已达到 `formal_ready/full-lecture`；其中非样板周的 `materials.md` 与 `outline.md` 仍为 `draft`，不能据此直接进入 PPT。
- Week 15 已有官方蓝模板 PPT 试点：storyboard 和 evidence review 入 Git，PPTX/PNG/contact sheet 输出保留在 `outputs/ppt/sysu_official_blue/week_15/`。
- 项目本地 `skills/` 已新增 course workflow 入口；全局技能白名单记录在 `docs/skill_loading_manifest_2026-06-03.md`。
- 新增维护目标：索引/断链/Week 11-15 对齐检查，以及样板周质量区块检查。
- 暂不批量生成 18 周 PPTX；当前 18 周仅推进到 40 页主干 storyboard 和教材扩写稿。
- Courseware 下一步作为人工精修审核台，重点处理 Student action、Timing、重复讲解、过短页和证据 note 泛化问题。
- Coursebook 下一步作为教材审读入口，重点检查概念体系、跨章衔接、案例支撑和知识图谱一致性。

## 4. 下一步

1. 维护 `course/weeks/_index.md`、`materials/markdown/_index.md` 和 `knowledge/*/_index.md`。
2. 通过 `course_quality_check.py` 检查所有周次三件套和样板周必备区块。
3. 保持三层状态语义：讲义深度、周次 `materials/outline` 状态、PPT 生产线状态分开判断。
4. 使用 Courseware / Teaching Plan 审核视图逐周精修 40 页 storyboard，先处理 Week 03/05/08/11/12/13/15/16/18。
5. 按 `course/evaluation/` 中的试评记录逐项处理 PPT 前置问题。
6. 进入 PPTX 试点前，先人工复核文字溢出、空页、乱码、页码、图表引用、学生动作和讲稿备注。

## 5. 不要做的事

- 不把 `knowledge/` 当作课程事实主线。
- 不把 AI 输出当作权威结论直接写进讲稿。
- 不写 awesome list 式资源堆砌。
- 不在未确认前公开、删除远端仓库、改变远端可见性、强推或重写远端历史；普通实现轮默认提交并推送当前分支。
- 不再引用或恢复 `F:\AI_Course\`。
