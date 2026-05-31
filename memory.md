# memory.md · AI_Course 跨会话记忆

本文记录 AI_Course 的稳定偏好、项目决策、当前状态和反向规则。它会随项目演化更新。

## 0. 元信息

- 项目：医药数据处理与可视化（36 课时 · AI 前置版）课程课件生产工作区。
- 当前唯一有效根目录：`E:\Codex_Projects\AI_Course\`。
- 旧根目录：`F:\AI_Course\` 已在 2026-05-31 清空并删除，不再作为回退点。
- Obsidian Vault：从 `E:\Codex_Projects\AI_Course\` 打开。
- 当前范式：courseware-first；`knowledge/` 是备课辅助层，`course/` 是课程生产主线。
- 远端仓库：private GitHub；push、公开、改远端或删除远端前必须二次确认。

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

## 3. 当前状态

- `course/weeks/week_01` 到 `week_18` 已有 `materials.md`、`outline.md`、`script.md`。
- 样板周优先级：Week 03、Week 14、Week 15、Week 16。
- 新增维护目标：索引/断链/Week 11-15 对齐检查，以及样板周质量区块检查。
- 暂不全量生成 18 周 PPT；先做 Week 03、Week 15、Week 16 三套试点。

## 4. 下一步

1. 维护 `course/weeks/_index.md`、`materials/markdown/_index.md` 和 `knowledge/*/_index.md`。
2. 通过 `course_quality_check.py` 检查所有周次三件套和样板周必备区块。
3. 继续打磨 Week 03、14、15、16 的授课脚本和 PPT 页级大纲。
4. 进入 PPT 试点前，先人工复核文字溢出、空页、乱码、页码、图表引用和讲稿备注。

## 5. 不要做的事

- 不把 `knowledge/` 当作课程事实主线。
- 不把 AI 输出当作权威结论直接写进讲稿。
- 不写 awesome list 式资源堆砌。
- 不在未确认前 push、公开、删除远端仓库。
- 不再引用或恢复 `F:\AI_Course\`。

