# AI_Course · 医药数据处理与可视化 · 课程知识库

> 这是一个 **LLM-Wiki 模式**的个人课程知识库（受
> [karpathy/LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 启发）。
> 用于备课、查阅、组织教学素材，**让 LLM 写 wiki，人来看 wiki**。

## 目录结构（三层架构）

```
e:\AI_Course\
├── AGENTS.md            ← Schema：LLM 维护 wiki 的规则与工作流（必读）
├── memory.md            ← 跨会话记忆：偏好 · 决策 · 当前阻塞 · 共识词汇
├── README.md            ← 本文件（顶层使用说明）
├── pdf_originals\       ← Raw 层 · 不可变 · 原始 PDF（4 本）
├── doc\                 ← Raw 层 · 人写的课程文档（教学大纲、讲稿、docx）
├── raw\                 ← Raw 层 · 字幕清理后的纯文本（AIDD）
├── sources\             ← Raw 层 · PDF→Markdown 转换、AIDD txt 镜像（脚本生成）
├── scripts\             ← 工具脚本（PDF 转 md、字幕清理）
└── wiki\                ← ★ Wiki 层 · 由 LLM 维护的知识网络
    ├── overview.md      ← 主页 / 知识地图
    ├── index.md         ← 内容目录（全 wiki 一张表）
    ├── log.md           ← 时间线
    ├── sources\         ← 每份 raw 素材的摘要 + 出处页（8 份）
    ├── entities\        ← 工具 / 库 / 平台 / 数据库（11 份，按需扩展）
    ├── concepts\        ← 流程 / 方法 / 原则（8 份，按需扩展）
    ├── topics\          ← 教学单元（已建 3 份，目标 18 周 + hub）
    ├── synthesis\       ← 综合 / 对比 / 思考（3 份）
    ├── queries\         ← 历史问答归档
    └── assets\          ← 模板 / 图表 / 共享资源
```

## 怎么用

### 我想浏览知识库

直接从 [wiki/overview.md](wiki/overview.md) 开始；或者打开 [wiki/index.md](wiki/index.md) 看全表。
推荐用 **Obsidian** 作为阅读器（仓库根设为 `e:\AI_Course\`，wiki 目录为主，附带 raw/doc 作为参考层）。

### 我想让 AI 帮我维护知识库

1. 让 AI **先读 [AGENTS.md](AGENTS.md)（规则）+ [memory.md](memory.md)（状态）+ [wiki/index.md](wiki/index.md)（现状）** —— 这是新会话开机三件事。
2. 告诉 AI 你要做的操作（见下面的"4 个核心操作"）。
3. AI 应严格按 schema 工作：**不动 raw 层、必须更新 index.md 和 log.md，有新决策同步进 memory.md**。

### 4 个核心操作（提示词示例）

#### 📥 Ingest：加入一份新素材

```
请按 AGENTS.md 的 ingest 流程处理 raw/AIDD_Bioinformatics/02_.../05_Sequence_Analysis_Using_Biopython.txt。
先用一段话告诉我你读到了什么、打算建/改哪些 wiki 页，
等我确认后再写文件。
```

#### ❓ Query：问知识库一个问题

```
我想知道第 11 周 DESeq2 课需要补哪些统计前提的讲解。
先扫 wiki/index.md 找相关页，给出页面列表，再综合答案。
```

#### 🧹 Lint：健康体检

```
请按 AGENTS.md §3.3 给 wiki 做一次 lint：
- 找孤岛页
- 找矛盾 / stale 声明
- 找命名不一致
- 把发现写到 wiki/synthesis/知识缺口与后续素材.md
```

#### 🔧 Refactor：结构调整

```
把 wiki/entities/samtools.md 拆成 samtools + bcftools 两个页，
注意同步更新所有入链。
```

## 当前已 ingest 的素材

| 素材 | 路径 | source 页 |
|---|---|---|
| 36 课时讲稿 | `doc/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md` | [36课时讲稿](wiki/sources/36课时讲稿.md) |
| 36 课时大纲 | `doc/36课时-AI前置调整版.docx` | [36课时大纲docx](wiki/sources/36课时大纲docx.md) |
| AIDD 课程字幕（71 节） | `raw/AIDD_Bioinformatics/` | [AIDD_Bioinformatics_Course](wiki/sources/AIDD_Bioinformatics_Course.md) |
| AIDD 人写综述 | `doc/AIDD_Bioinformatics_课程结构与内容整理.md` | [AIDD课程结构整理](wiki/sources/AIDD课程结构整理.md) |
| ISLP（Python 版） | `pdf_originals/ISLP*.pdf` + `sources/PDF_Library/*.md` | [ISLP](wiki/sources/ISLP.md) |
| ISLR（R 版） | `pdf_originals/ISLR*.pdf` + `sources/PDF_Library/*.md` | [ISLR](wiki/sources/ISLR.md) |
| Starting Data Analytics with GenAI | `pdf_originals/...9781633437210.pdf` | [Starting_Data_Analytics_GenAI](wiki/sources/Starting_Data_Analytics_GenAI.md) |
| Learn AI-Assisted Python Programming | `pdf_originals/【R240】...Copilot...pdf` | [Learn_AI_Assisted_Python_Programming](wiki/sources/Learn_AI_Assisted_Python_Programming.md) |

## 当前页面规模

- Sources：8
- Entities：11
- Concepts：8
- Topics：3（含课程主页）
- Synthesis：3
- **合计：33 页（实建）+ ~40 页计划中（见 [知识缺口](wiki/synthesis/知识缺口与后续素材.md)）**

## 关键脚本

- [`scripts/clean_aidd_subtitles.py`](scripts/clean_aidd_subtitles.py)：清理 AIDD 字幕、术语校正、生成 INDEX.md
- [`scripts/pdf_to_markdown.py`](scripts/pdf_to_markdown.py)：PDF → Markdown，输出到 `sources/PDF_Library/`

## 推荐外部工具

- **[Obsidian](https://obsidian.md/)**：作为 wiki 浏览器（开 Graph View 看连通性）
- **Git + GitHub Private Repo**：给本目录加版本控制
- **[qmd](https://github.com/tobi/qmd)**：当 wiki 大到 ~100 sources 时，作为本地 BM25+向量搜索引擎（可选）

## 参考

- 范式来源：[Karpathy · LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 课程主大纲：[36 课时讲稿](doc/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)
- AIDD 字幕索引：[raw/AIDD_Bioinformatics/INDEX.md](raw/AIDD_Bioinformatics/INDEX.md)

## 维护原则（一张图）

```
  人（你）              AI（我）
   │                     │
   │ 1. 提供素材 / 提问   │
   │ ──────────────────► │
   │                     │ 2. 读 AGENTS.md
   │                     │ 3. 扫 wiki/index.md
   │                     │ 4. 读 / 写 wiki/
   │                     │ 5. 更新 index.md + log.md
   │ 6. 浏览 wiki + 检查 │
   │ ◄────────────────── │
```

**Raw 层永远不动。Wiki 层由 AI 写。Schema 由两人共同进化。**
