# AGENTS.md — AI_Course 个人课程知识库的 Schema

> 本文件是“AI_Course 知识库”的 schema/工作流定义，灵感来自
> [karpathy/LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。
>
> **AI Agent 阅读本文件后，应像一个有纪律的 wiki 维护者那样工作**：
> 由用户负责输入素材、提出问题、把握方向；
> 由 AI 负责阅读素材、抽取要点、写页面、维护交叉引用、保持一致性。
>
> 本知识库的领域：**“医药数据处理与可视化（36 课时·AI 前置版）”** 课程的备课与知识沉淀，
> 周边吸纳生信教程（AIDD Bioinformatics）、统计学习教材（ISLP/ISLR）、AI 辅助编程教材
> （GitHub Copilot、Generative AI for Data Analytics）等。

> [!important] **新会话开机三件事**（每个新会话开始时，AI 必须按顺序做完）：
>
> 1. 读本文件（`AGENTS.md`）—— 规则与工作流。
> 2. 读 [`memory.md`](memory.md) —— 用户偏好 / 项目决策 / 当前阻塞 / 共识词汇。
> 3. 扫 [`wiki/index.md`](wiki/index.md) —— 知识库现状。
>
> 跳过任何一步都会让 AI 把过去做过的决策再做一次，浪费用户时间。

---

## 1. 三层架构（务必遵守边界）

```
e:\AI_Course\
├── AGENTS.md          ← 本文件，schema（规则·稳定）
├── memory.md          ← 跨会话记忆（偏好·决策·阻塞·演化）
├── README.md          ← 顶层使用说明
├── pdf_originals\     ← Raw 层 · 不可变 · 原始 PDF
├── doc\               ← Raw 层 · 人写的课程文档（教学大纲、讲稿、docx）
├── raw\               ← Raw 层 · 字幕清理后的纯文本（AIDD）
├── sources\           ← Raw 层 · PDF→Markdown 转换、AIDD txt 镜像（脚本生成）
├── scripts\           ← 工具脚本（PDF 转 md、字幕清理等）
└── wiki\              ← ★ Wiki 层 · 由 LLM 维护的知识网络
    ├── index.md       ← 内容目录（每次 ingest 都要更新）
    ├── log.md         ← 时间线（append-only）
    ├── overview.md    ← 主页 / 知识地图
    ├── sources\       ← 每份 raw 素材的“摘要 + 出处”页
    ├── entities\      ← 具体实体：库、工具、数据库、平台、人物
    ├── concepts\      ← 抽象概念：流程、方法、原则
    ├── topics\        ← 教学单元 / 模块 / 项目
    ├── synthesis\     ← 综合页：对比、映射、思考
    └── queries\       ← 历史问答归档（值得长期保留的问答）
```

### AGENTS.md / memory.md / log.md / index.md 的角色边界

| 文件 | 装什么 | 改动频率 | 谁维护 |
|---|---|---|---|
| `AGENTS.md` | **规则**（schema、工作流、写法约束） | 低·稳定 | 用户 + AI 共定 |
| `memory.md` | **状态**（偏好、决策、跨会话待办、共识词汇） | 中·演化 | AI 写 + 用户审 |
| `wiki/log.md` | **事实时间线**（每次操作的 append-only 记录） | 每次 ingest | AI 追加 |
| `wiki/index.md` | **事实目录**（全 wiki 页面清单） | 每次 ingest | AI 同步 |
| `wiki/overview.md` | **导读**（人面向的知识地图） | 低 | AI 偶尔更新 |

### 不可逾越的硬规则

1. **Raw 层只读**：`pdf_originals/`、`raw/`、`sources/`、`doc/` 里的文件 AI 不许改写。
   如果发现错误或需要纠正，写到 `wiki/synthesis/勘误.md` 或对应 source 页“勘误”章节中。
2. **`scripts/` 慎改**：只有当用户明确说“改脚本”时才能动；正常 ingest 期间不要碰。
3. **wiki 全权由 AI 维护**：用户原则上不直接编辑 wiki 页面，最多在 chat 里指出哪里要改。
4. **wiki 必须是合法的 Obsidian / Markdown 仓库**：链接用标准 Markdown 形式
   （文本加圆括号包住相对路径），不要用 Obsidian 双中括号 `[[wiki link]]` 语法
   （保持纯 Markdown 通用性）。

---

## 2. 页面类型与写法

每个 wiki 页面顶部都要有 YAML front matter，便于 Dataview / grep 查询。

### 2.1 Source 摘要页 `wiki/sources/<slug>.md`

每个被 ingest 的原始素材对应一份。结构：

```yaml
---
type: source
title: <人类可读标题>
raw_path: <相对 e:\AI_Course\ 的原始路径，可多条>
ingested: 2026-05-21
language: zh-CN | en
kind: book | course | docx | gist | article | dataset
status: draft | in_progress | stable
tags: [python, r, rna-seq, ...]
---
```

正文章节：

- **一句话定位**：这份素材在本课程中的位置。
- **核心论点 / 主要内容**：3–10 条要点，禁止整段抄原文，必须自己组织语言。
- **可抽取到课程的素材**：明确点出能进入“36 课时讲稿”的章节、案例、提示词。
- **相关页面**：内链到 entities/concepts/topics。
- **勘误**：原文存在的疑似错误（机翻、术语错配等）。

### 2.2 Entity 页 `wiki/entities/<Name>.md`

具体的、可命名的对象：库、工具、平台、数据库、人物、公司。

```yaml
---
type: entity
name: DESeq2
aka: [Deseq2, DSEC2-机翻误识]
category: r-package
domain: [transcriptomics, rna-seq, differential-expression]
status: stable
tags: [r, rna-seq, dge]
---
```

正文模板：定位 / 主要用途 / 关键 API 或命令 / 课程中的使用位置 / 常见坑 / 相关来源（链回 sources）。

### 2.3 Concept 页 `wiki/concepts/<slug>.md`

抽象主题：流程、方法、原则、范式。

```yaml
---
type: concept
title: RNA-seq 上游流程
status: in_progress
tags: [rna-seq, pipeline, ngs]
---
```

正文模板：定义 / 关键步骤 / 涉及实体（链 entities）/ 课程位置（链 topics）/ 常见问答。

### 2.4 Topic / 教学单元页 `wiki/topics/<slug>.md`

对应课程的某一模块、某一讲、某个项目。

```yaml
---
type: topic
title: 第 11 周：差异表达分析与 DESeq2
week: 11
hours: 2
status: draft
tags: [r, deseq2, dge, teaching]
---
```

正文模板：教学目标 / 大纲定位 / 引用素材（链 sources）/ 讲稿要点 / 上机任务 / AI 提示词 / 评估方式 / 风险与坑。

### 2.5 Synthesis 综合页 `wiki/synthesis/<slug>.md`

跨多份素材的对比、映射、思考、思维导图、判断。
是 wiki 真正“升值”的地方——比单点页面更稀有，但价值最高。

```yaml
---
type: synthesis
title: AIDD 章节 → 36 课时大纲映射
status: stable
related_sources: [AIDD_Bioinformatics_Course, 36课时讲稿]
tags: [course-design, mapping]
---
```

### 2.6 Query 历史问答 `wiki/queries/<YYYY-MM-DD>_<slug>.md`

值得保留的问答归档（一次性闲聊就不要往里塞了）。

---

## 3. 操作（Ops）

四个核心操作。AI 按下面的流程执行，每一步都要在 `log.md` 中留下一条记录。

### 3.1 Ingest（吃进一份新素材）

触发：用户说“ingest 一下 xxx”、“把 xxx 加进来”、“处理 raw/yyy.txt”。

流程（**对话式**，不要一次性给完）：

1. 用户给出素材路径或名称（如果是 PDF，确认是否已转 md 到 `sources/`，没有就跑
   `scripts/pdf_to_markdown.py`）。
2. AI 读完素材，**先用一段话告诉用户它读到了什么**（一句话定位 + 5 条要点 + 你打算建/改哪些页）。
3. 用户确认或调整后，AI 执行：
   - 在 `wiki/sources/` 写或更新一份 source 摘要页。
   - 创建 / 更新相关 `entities/`、`concepts/`、`topics/`。
   - **真正去 grep 已有页面**，把新素材里相关的实体名（如 `DESeq2`、`ggplot2`、
     `Biopython`）链回旧页，避免出现孤岛页。
   - 检查是否产生与旧页的“矛盾 / 互补 / 强化”，需要的话写一段 synthesis。
   - 更新 `wiki/index.md`：在合适分类下新增条目或更新行。
   - 追加 `wiki/log.md` 一行，格式见 §5。
4. 一次 ingest 改 5–15 个 wiki 文件是正常的。

### 3.2 Query（回答用户的问题）

1. 先扫 `wiki/index.md` 找候选页面（这是 wiki 的“RAG 索引”，胜过 embedding）。
2. 读相关页面，得出答案。
3. 如果发现答案过程中产生了**值得复用的新内容**（对比表、推荐学习路径、提示词模板），
   就写到 `wiki/queries/<date>_<slug>.md` 或追加到 synthesis。
4. 长答案以 Markdown 页形式输出，并标注引用了哪些 wiki 页。

### 3.3 Lint（健康体检）

触发：用户说“lint 一下知识库”、“查重 / 找孤岛”、“健康检查”。

要检查：

- 矛盾点：不同页面对同一事实的不同陈述。
- 失效声明：被新 source 推翻的旧观点（标记为 `> [!stale] 2026-xx-xx 被 xx 修订`）。
- 孤岛页：没有入链 / 出链的页（在 `wiki/index.md` 的“孤岛区”列出）。
- 命名/链接不一致：例如同一工具在不同页用了不同写法。
- 数据缺口：被多次提到但缺失专页的实体/概念，作为“后续可 ingest”的候选写入
  `wiki/synthesis/知识缺口与后续素材.md`。

### 3.4 Refactor（结构调整）

触发：用户说“拆分这个页”、“合并这俩”、“把 xx 改成 entity”。

- 改文件名要同步改全部入链（先 grep）。
- 删页面前先把内容并入新页，并在 `log.md` 写明搬迁。
- 涉及多页改动时一次做完，避免半截状态。

### 3.5 Memorize（更新 memory.md）

memory.md 是**演化**的，不是 append-only。AI 应当在以下时机主动检查并更新它：

| 时机 | 更新内容 | 写到哪节 |
|---|---|---|
| 用户首次表达某种偏好（语言、风格、节奏） | 加一条带日期的偏好 | §1 用户偏好 |
| 做出影响目录结构 / 命名 / 流程的决定 | 写一条 mini-ADR（决定 / 备选 / 为什么） | §2 项目决策 |
| 完成一次有意义的 ingest / refactor | 更新"已完成 / 下一步" | §3 状态卡 |
| 用户提出新阻塞或新问题 | 加一条 `[ ]` 待回答项 | §3 当前阻塞 |
| 出现项目内新简写或术语映射 | 加一行 | §4 共识词汇 |
| 用户给 AI 工作方式留言（夸赞或批评） | 加一条 meta-feedback | §5 元反馈 |
| 用户明确说"别这样做" | 加一条反向规则 | §6 不要做的事 |

**重要**：用户做出"重大"决策（影响 schema 或目录结构）时，**先在 chat 里复述确认，再写入 memory.md §2**——
不要悄悄记下用户可能并未真的同意的事。

---

## 4. 索引（index.md）与日志（log.md）

### 4.1 `wiki/index.md`

形式上是“全 wiki 一张表”的目录，按分类分节。每个条目格式：

```
- [<标题>](<相对路径>) — <一句话摘要> · <status> · <tag-list>
```

ingest / refactor 时**必须**更新它。AI 答题时也可直接 grep 它来定位页面。

### 4.2 `wiki/log.md`

时间线，append-only，每条以 `## [YYYY-MM-DD] <op> | <对象>` 开头，例如：

```
## [2026-05-21] ingest | AIDD_Bioinformatics_Course
- 新增：sources/AIDD_Bioinformatics_Course.md
- 新增：concepts/RNA-seq上游流程.md，Variant_Calling流程.md
- 新增：entities/DESeq2.md, ggplot2.md, samtools.md
- 更新：index.md, overview.md
- 备注：发现“贝叶斯入门”是 bash 误识别，已写入 sources 页勘误。
```

这样后续可以 `grep "^## \[" wiki/log.md | tail -20` 查最近动态。

---

## 5. 风格约定

1. **中文为主，专业术语保留英文**：DESeq2、ggplot2、scRNA-seq、samtools、bcftools 保持原样。
2. **绝不抄原文**：source 页里给的是“你（AI）读完之后的转述”。
3. **写之前先 grep**：不要重复造页。例如要写 `DESeq2.md` 前，先确认它是否已存在。
4. **每页都要有出链与入链**：孤岛页是 wiki 的癌细胞。
5. **不要罗列“xxx 的 N 大优点”这种空洞内容**：每一条 bullet 都应该承载信息，
   带具体函数名/参数/数据集/章节定位更好。
6. **不要给一份长长的“资源链接列表”**：本 wiki 不是 awesome list，
   而是为本课程服务的、被消化过的知识网络。
7. **遇到不确定的事实**：写下来并在该处加 `> [!todo] 待核实：…`，不要瞎编。
8. **图与代码**：能用 Markdown 表达就不要外链截图；代码块用三反引号 + 语言标识；
   pipeline / 结构示意用 mermaid。

---

## 6. 与“raw 层”和 `doc/` 的关系

- `doc/` 里的 `课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md` 是**事实上的主大纲**，
  wiki 的 `topics/` 必须与它的周次保持一一对应（第 1 周 … 第 18 周）。
- `doc/AIDD_Bioinformatics_课程结构与内容整理.md` 是 AIDD 课程的人写综述，
  wiki 里的 AIDD 相关 source 页要把它作为“second-hand source”引用。
- `raw/AIDD_Bioinformatics/<chapter>/<lesson>.txt` 才是第一手字幕清理结果。
  生成 wiki/concepts/concept 页时要回到这些 txt 抽细节，而不是只从 doc/ 复制。
- `sources/PDF_Library/*.md` 是 PDF→md 转换结果，可能有版式噪声，
  ingest 时优先看每章开头与目录，必要时与 `pdf_originals/` 原 PDF 交叉确认。

---

## 7. 当前优先方向（2026-05-21 设定）

1. 把 36 课时讲稿的 18 周全部建成 `wiki/topics/week_01.md … week_18.md` 骨架。
2. 把 AIDD 11 章 71 节按“概念页 + 实体页”拆分（不要一节对一页，按主题聚合）。
3. 把 4 本 PDF 各自建一份 source 页（不展开全文，只挑能进课的章节）。
4. 关键合成页：
   - `synthesis/AIDD与36课时映射.md`
   - `synthesis/三本Python书定位对比.md`
   - `synthesis/知识缺口与后续素材.md`

后续素材可能包括：单细胞 Seurat 教程、TCGA/GEO 实战、Python pandas/scikit-learn、
AI 协作记录模板、临床数据集示例等——出现时再走 ingest 流程。
