# AI_Course 下一轮工作计划

日期：2026-05-31  
当前根目录：`E:\Codex_Projects\AI_Course`  
依据：多视角评审结论、[迁移边界核对清单](migration_boundary_review.md)、[AGENTS.md](../AGENTS.md)、[memory.md](../memory.md)、[README.md](../README.md)

## 目标

下一轮不继续扩大资料面，先把项目从“结构可用”推进到“稳定交付课程”的状态。

核心目标：

1. 收口 E 盘唯一真源和 Git 迁移基线。
2. 将 Week 03、Week 15、Week 16 打磨到可授课试点版本。
3. 建立课程质量 rubric，使 AI 生成内容有可复核标准。
4. 标准化知识页模板，让 `knowledge/` 更直接服务 `course/`。
5. 补充教师使用手册，降低下一轮调用 AI 的操作成本。

## 当前事实基线

- 唯一有效工作区为 `E:\Codex_Projects\AI_Course`，旧 `F:\AI_Course` 不再使用。
- `course/weeks/week_01` 到 `week_18` 已具备 `materials.md`、`outline.md`、`script.md` 三件套。
- 样板周为 `week_03`、`week_14`、`week_15`、`week_16`。
- 当前维护命令已通过：
  - `python scripts/maintenance/course_km_index.py --check`
  - `python scripts/maintenance/course_quality_check.py --check`
  - `python -m pytest -q`
- Git 工作区仍处于大规模迁移未收口状态；下一轮内容编辑前应先完成迁移基线复核和本地提交。

## P0：迁移基线收口

### 目的

把旧 `doc/`、`raw/`、`sources/`、`wiki/` 到新 `course/`、`materials/`、`knowledge/` 的结构迁移变成一个可审计基线，避免后续课件更新和迁移 diff 混在一起。

### 工作项

1. 复核 [迁移边界核对清单](migration_boundary_review.md) 中每个旧路径与新路径的对应关系。
2. 检查 `.gitignore` 是否继续排除：
   - `materials/raw/pdf_originals/`
   - `materials/raw/external_ppt/`
   - `outputs/`
   - `site/node_modules/`
   - `site/dist/`
   - `tmp/`、缓存、日志和学生数据。
3. 运行维护命令：

   ```powershell
   python scripts/maintenance/course_km_index.py --write
   python scripts/maintenance/course_km_index.py --check
   python scripts/maintenance/course_quality_check.py --check
   python -m pytest -q
   ```

4. 用 `git status --short` 与 `git diff --stat` 人工复核迁移范围。
5. 本地提交迁移基线；不 push，除非用户另行确认。

### 验收证据

- `course_km_index.py --check` 输出 `OK`。
- `course_quality_check.py --check` 输出 `OK`。
- `pytest` 全部通过。
- `git status --short` 中不再混杂旧迁移和新内容编辑。
- 本地 commit message 可清楚表达“courseware-first structure baseline”。

## P1：三套可授课试点

### 目的

先完成三周可真实试讲的课程产物，不全量生成 18 周 PPT。

### 试点范围

| 周次 | 主题 | 目标状态 |
|---|---|---|
| Week 03 | AI 辅助编程与 Python 快速入门 | 可授课、可上机、可布置练习 |
| Week 15 | 差异表达分析与功能解读 | 可讲清 padj/log2FC/火山图/热图解释边界 |
| Week 16 | 单细胞转录组可视化 | 可讲清 QC/UMAP/marker 图和细胞注释不确定性 |

Week 14 作为 Week 15 的上游铺垫继续保留样板周状态，但不作为第一批 PPT 输出重点。

### 每周交付物

每个试点周至少完成：

- `materials.md`：来源、可用程度、待核验点、课堂用途。
- `outline.md`：10-12 页 PPT 页级大纲，每页有标题、核心图/表/代码意图、讲授重点。
- `script.md`：可直接授课的讲稿，不只是 bullet list。
- 课堂练习：含输入、任务、预期输出、AI 可协助部分、人工核验点。
- 课后练习：含评分要点。
- 待核验清单：列出需要人工确认的事实、图表、代码或医学解释。

### 验收证据

- 三个试点周通过 `course_quality_check.py --check`。
- 每周至少有一个可运行或可手算核验的小任务。
- 每周明确写出 AI 不能替代的判断边界。
- 每周的素材引用可以从 `materials.md` 回溯到 `knowledge/` 或 `materials/`。

## P1：课程质量 Rubric

### 目的

把“结构完整”升级为“教学质量可评审”。当前脚本主要检查区块是否存在，下一轮要建立人工复核标准。

### 工作项

1. 新建 `course/evaluation/courseware_rubric.md`。
2. Rubric 至少覆盖：
   - 科学与统计准确性
   - 药学场景相关性
   - 本科生可理解性
   - 课堂可执行性
   - AI 协作边界
   - 引用与素材可追溯性
   - 图表和代码核验要求
3. 给 Week 03、Week 15、Week 16 各写一份试评样例。
4. 后续再考虑把部分 rubric 项扩展进 `course_quality_check.py`。

### 验收证据

- `course/evaluation/courseware_rubric.md` 存在且可直接用于人工评分。
- 每个试点周都有一份 rubric 试评记录。
- Rubric 不把 AI 输出当作权威结论，必须保留人工核验项。

## P2：知识页模板与高价值页面重写

### 目的

让 `knowledge/` 从“可检索页面”升级为“可复用备课资产”。

### 工作项

1. 新建知识页模板，例如 `knowledge/templates/source_page_template.md`。
2. 模板固定包含：
   - 来源与版本
   - 一句话用途
   - 适用周次
   - 可直接用于课堂的内容
   - 需要改写后才能使用的内容
   - 不应直接采用的内容
   - 待核验
   - Related
3. 优先重写或补强：
   - `knowledge/sources/AIDD_Bioinformatics_Course.md`
   - `knowledge/sources/ISLP.md`
   - `knowledge/sources/ISLR.md`
   - `knowledge/entities/DESeq2.md`
   - `knowledge/synthesis/AIDD与36课时映射.md`

### 验收证据

- 高价值页面能直接回答“服务哪一周、怎么服务、哪些不能直接用”。
- 标准 Markdown 链接无断链。
- 运行 `python scripts/maintenance/course_km_index.py --check` 通过。

## P2：教师使用手册

### 目的

降低下一轮 AI 协作成本，让教师不必理解全部目录结构也能正确使用项目。

### 工作项

新建 `docs/user_guide.md`，包含 8 个场景和可复制提示词：

1. 新增外部资料。
2. 整理某个知识点。
3. 起草某周 PPT 大纲。
4. 修改某周讲稿。
5. 生成课堂练习。
6. 检查断链和索引。
7. 记录课程决策。
8. 准备 PPT 试点导出。

### 验收证据

- 每个场景都有“用户怎么说”“AI 应该读哪些文件”“产物写到哪里”“完成后跑哪些检查”。
- 手册不要求用户记住旧 `wiki/`、旧 `raw/` 或旧 `sources/` 路径。

## 暂不做

- 不全量生成 18 周 PPT。
- 不引入向量数据库或独立 RAG 服务。
- 不把项目本地 `skills/` 安装到全局。
- 不 push、不改远端可见性、不删除远端。
- 不把原始商业 PDF、外部 PPT/PDF 或生成物纳入 Git。

## 下一轮执行顺序

1. P0 迁移基线收口。
2. Week 03 可授课版本。
3. Week 15 可授课版本。
4. Week 16 可授课版本。
5. 课程质量 rubric。
6. 知识页模板和 5 个高价值页。
7. 教师使用手册。

## 完成定义

下一轮可视为完成，当且仅当：

- 迁移基线已本地提交，后续内容更新不再混入旧结构迁移 diff。
- Week 03、Week 15、Week 16 均可从 `course/weeks/` 直接进入授课准备。
- 课程质量 rubric 已能支持人工评审。
- `knowledge/` 的高价值页面能明确服务对应周次。
- `docs/user_guide.md` 能让后续会话按场景工作。
- 所有维护命令通过。
