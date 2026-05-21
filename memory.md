# memory.md — 跨会话记忆

> 这是 **AI 与用户在 AI_Course 项目上累积的共识 / 偏好 / 决策 / 待办**。
> 与 [`AGENTS.md`](AGENTS.md)（规则）和 [`wiki/log.md`](wiki/log.md)（事实时间线）配套。
>
> **每次新会话开始，AI 都应该先读这份文件，再开始工作。**
>
> 维护原则：
> - AI 写 / 用户审。重大决策需要用户确认后再写入。
> - 内容**会演化**（不像 log.md 只追加）：偏好可以更新，过期的决策可以划掉但保留历史。
> - 每条记录都标日期，方便追溯。

---

## 0. 元信息

- 项目：医药数据处理与可视化（36 课时·AI 前置版）课程知识库
- 知识库范式：[Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 初始化日期：2026-05-21
- 当前 wiki 规模：35 页（详见 [wiki/index.md](wiki/index.md)）
- 版本控制：已 `git init` + main 分支首次 commit（2026-05-21）；远端 `https://github.com/luvega/ai-bioinfo-wiki`（**Private**）
- Obsidian Vault：已配置，详见 [wiki/assets/obsidian_setup.md](wiki/assets/obsidian_setup.md)
- 上次更新：2026-05-21

---

## 1. 用户偏好（preferences）

> 这里记录的是**风格性、习惯性**的偏好——AI 不应反复重新发现它们。

- **[2026-05-21] 语言**：回复一律使用**中文**；专业术语保留英文原文（DESeq2、ggplot2、scRNA-seq、samtools、bcftools 等）。
- **[2026-05-21] 教学定位**：受众是**药学专业本科生**，不是生信/统计科班；解释问题时优先用医药案例（药效、临床指标、表达矩阵）。
- **[2026-05-21] AI 协作哲学**：AI 用于**辅助**——解释 / 局部生成 / 核验，**不替学生做医学/统计判断**。
- **[2026-05-21] 节奏偏好**：先把骨架搭起来 + 少量示范页，不要一次性 ingest 全部素材；用户希望先**审过结构**再决定后续 ingest 顺序。
- **[2026-05-21] 文件命名**：中文页名可以直接出现在路径里（`第N周`、`概念名`），不强求 ASCII slug。
- **[2026-05-21] 链接风格**：使用标准 Markdown 链接语法（`[文本](path)`），**不用** Obsidian 的双中括号 `[[]]`，保持跨工具通用性。
- **[2026-05-21] 浏览器**：用 **Obsidian** 作为日常 wiki 浏览器。Vault 根 = `e:\AI_Course\`（不是 wiki 子目录），以便从 wiki 跳回 raw 原文。
- **[2026-05-21] 版本控制**：项目用 **Git**，main 分支。`pdf_originals/`、`ai_logs/`、`projects/`、`.obsidian/workspace.json` 不入 git；`sources/PDF_Library/*.md` 入 git（可读、可 diff）。

---

## 2. 项目决策（mini-ADR · Decisions）

> 每条决策包括：决定 / 备选 / 为什么。**不应再被推翻**——除非用户明确说要改。

### [2026-05-21] D-001 · 三层架构 + 双 raw 入口（raw/ 与 sources/）

- **决定**：保留 `raw/`（脚本输出的字幕清理 txt）和 `sources/`（PDF→md 转换 + AIDD 镜像）两个目录，**都视为 raw 层**。
- **备选**：合并为单一 `raw/`。
- **为什么**：
  - 用户已有的 `scripts/pdf_to_markdown.py` 写死了 `llm_wiki_kb/raw/sources/PDF_Library` 路径，重构会动脚本。
  - `sources/PDF_Library/*.md` 是"PDF 衍生品"，与 `raw/AIDD_Bioinformatics/` 的"字幕清理产物"性质不同，分目录有助于理解出处。
  - 代价是新人会迷惑，已通过 README §"目录结构"图说明。

### [2026-05-21] D-002 · 不用 Obsidian 双中括号链接

- **决定**：wiki 一律用标准 Markdown 链接（文本 + 圆括号 + 相对路径），不用 `[[wiki link]]`。
- **为什么**：保持纯 Markdown 通用性（GitHub、VS Code、Hugo 等都能直接渲染）；Obsidian 也兼容标准链接。

### [2026-05-21] D-003 · 36 课时讲稿是事实主大纲

- **决定**：所有其他素材（AIDD、PDF 书库）都被定位为"可被讲稿挑选的素材池"，不另起并列课程。
- **备选**：把 AIDD 视为另一门并列课程，做平行的"AIDD 课程 wiki"。
- **为什么**：用户的目标是**备好这门 36 课时课**，而不是建一个生信百科。

### [2026-05-21] D-004 · Topic 页按"周"而不是按"节"

- **决定**：`wiki/topics/week_01_*.md` … `week_18_*.md`，一周一页。
- **备选**：按 36 课时一节一页（每周 2 节 = 36 个 topic）。
- **为什么**：36 课时讲稿本身就是按周组织的；一节一页会破坏教学连贯性。

### [2026-05-21] D-005 · 不在 Raw 层做任何修改

- **决定**：发现 raw 层错误时，写到对应 source 页的"勘误"小节，不动原始文件。
- **为什么**：保护 raw 层不可变性；脚本可能随时重跑覆盖。

### [2026-05-21] D-006 · AGENTS.md 是项目级 schema，memory.md 是项目级状态

- **决定**：两个文件并列放在项目根，不放进 `wiki/`。
- **为什么**：它们是 AI 协作的"元数据"，不是知识本身；放在 wiki/ 内会污染知识网络。

### [2026-05-21] D-007 · git 仓库范围与 .gitignore

- **决定**：
  - 项目根 `git init -b main`，整个 `e:\AI_Course\` 是一个 git 仓库。
  - **入 git**：`AGENTS.md`、`memory.md`、`README.md`、`.gitignore`、`doc/`、`raw/`、`scripts/`、`sources/`（含 PDF_Library 的 markdown）、`wiki/`、`.obsidian/`（除 workspace.json 等本机状态）。
  - **不入 git**：`pdf_originals/`（大文件 + 版权敏感）、`ai_logs/`（潜在 PII）、`projects/`（学生项目，PII）、`.obsidian/workspace.json`（本机状态）、各类缓存。
- **备选**：(a) 不加 git；(b) 只把 wiki/ 加 git；(c) 把 PDF 也入。
- **为什么**：用户希望整个目录可追溯；同时避免 PDF 商业版权风险与 PII 风险。`sources/PDF_Library/*.md` 体积约 4 MB，对 git 可接受。

### [2026-05-21] D-008 · Obsidian Vault 边界与索引排除

- **决定**：
  - Vault 根 = `e:\AI_Course\`，不是 `e:\AI_Course\wiki\`，以保证 wiki 中 `../sources/...` 类反向链接可用。
  - 通过 `.obsidian/app.json` 的 `userIgnoreFilters` 排除 raw 层重量级目录（`pdf_originals/`、`sources/PDF_Library/`、`raw/AIDD_Bioinformatics/`、`sources/AIDD_Bioinformatics/`），让 Quick Switcher / Search / Graph View 保持干净。
  - Graph View 配 5 色分组（sources/entities/concepts/topics/synthesis）。
- **为什么**：vault 太宽会被字幕和大 markdown 拖慢；但又不能把 wiki 单独切出来，否则反向链失效。
- **副作用**：搜索 AIDD 原文需临时去掉 filter，或在 VS Code/ripgrep 中搜。

### [2026-05-21] D-010 · GitHub 远端仓库 = luvega/ai-bioinfo-wiki · Private

- **决定**：远端使用 `https://github.com/luvega/ai-bioinfo-wiki`，可见性 **Private**。
- **过程**（实事记录，便于未来追溯）：
  - 用户提供仓库 URL，AI 添加 origin 并尝试 push。
  - 第一次 push 因 `github.com:443` 直连被 reset 失败（中国网络环境）。
  - 探测本机代理端口，发现 `127.0.0.1:10080` 可达 GitHub；本地仓库（`--local`）配 `http.proxy` / `https.proxy` 指向该端口。
  - 配代理后 push 成功（commit `8c971bf` + `e512bc5`，均推到 main）。
  - 用户随后说"先不要 push 了"——但 push 已完成。
  - 用户确认保留远端但改 Private，AI 用 `gh repo edit ... --visibility private` 完成切换。
- **当前状态**：远端仍持有本地两次 commit；后续 push 默认要走代理（已 `--local` 配好，不污染全局）。
- **教训**：下次涉及"推送/对外发布"动作，**先确认目标、二次确认网络配置、再执行**。不要把 push 当成普通 commit 的延续动作。

### [2026-05-21] D-009 · Week 11 必须包含富集分析（GO/KEGG/GSEA）

- **决定**：Week 11 差异表达课不止讲 DESeq2，**必须**包含富集分析下游一节（建议 30-45 分钟）。
- **备选**：富集分析挪到 Week 12 或 Week 16。
- **为什么**：差异表达基因列表常达千级，不做富集学生根本读不出生物学意义；这是 AIDD 课程缺失的内容，本课程要补。
- **已建**：[`wiki/concepts/富集分析_GO_KEGG.md`](wiki/concepts/富集分析_GO_KEGG.md)（ORA / GSEA / clusterProfiler + 解释陷阱 + 45 分钟教学路径）。
- **后续**：建 Week 11 topic 页时直接引用此 concept 页。

---

## 3. 跨会话状态卡 / 当前阻塞

> 下次会话开始时，AI 应该参考这里决定**从哪儿继续**。

### 已完成（截至 2026-05-21）

- 三层架构搭建完成。
- `AGENTS.md`、`README.md`、`memory.md` 已建。
- wiki 35 页骨架完成（含富集分析 GO/KEGG），所有内部链接已 lint 通过。
- 首次 ingest 涵盖 8 份 source，建立了核心 entity / concept 页。
- **Git 仓库已初始化**（main 分支，196 文件首次 commit）。
- **Obsidian Vault 已配置**（`.obsidian/` 含 app/appearance/core-plugins/community-plugins/graph/hotkeys；
  详见 [`wiki/assets/obsidian_setup.md`](wiki/assets/obsidian_setup.md)）。

### 下一步建议（按优先级）

1. **Week 03 - Week 18 的 topic 页**（最大宗工作，16 周 × ~150 行 ≈ 5-7 次会话）
   - 优先 Week 11（DESeq2 + 富集分析）— 教学素材已就绪，可率先完成。
2. **第 14-15 周相关展开**：scRNA-seq / Microarray 两个 concept 页（教学需求迫切）。
3. **多重检验校正 concept 页**（从 ISLP Ch.13 抽，第 8、11 周共用）。
4. **AI 协作记录模板**写到 `wiki/assets/ai_log_template.md`（学生作业要用）。
5. **pandas / scipy.stats 入门 concept 页**（第 5-8 周教学需要）。

完整待办清单见 [`wiki/synthesis/知识缺口与后续素材.md`](wiki/synthesis/知识缺口与后续素材.md)。

### 当前阻塞 / 等用户回答的问题

> 暂无未决问题。上轮三个问题已全部回答并落到决策中：
> - ~~Week 11 是否含富集分析？~~ → D-009 ✅
> - ~~是否加 git？~~ → D-007 ✅
> - ~~是否配 .obsidian？~~ → D-008 ✅

---

## 4. 共识词汇 / 项目内简写

> 我们俩在这个项目里默认的术语映射。新加成员（或下次开始的 AI）按本表理解。

| 简写 / 简称 | 全称 / 解释 |
|---|---|
| 「主大纲」 | `doc/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md` |
| 「docx 原件」 | `doc/36课时-AI前置调整版.docx`（正式报备版） |
| 「AIDD」 | AIDD Bioinformatics 课程（71 节字幕） |
| 「案例池」 | AIDD + PDF 书库的合集，作为讲稿可选素材 |
| 「ISLP / ISLR」 | An Introduction to Statistical Learning，Python / R 版 |
| 「6 字段记录」 | AI 协作记录模板：问题 / Prompt / AI 输出 / 人工核验 / 修改说明 / 反思 |
| 「三阶段边界」 | 第 1-2 / 3-11 / 12-18 周的 AI 协作三阶段 |
| 「三红线」 | AI 不可逾越的 3 条：医学结论 / 未读懂代码 / 真实临床数据 |
| 「Raw 层」 | `pdf_originals/` `doc/` `raw/` `sources/` 四目录（不可变） |
| 「Vault」 | Obsidian 视角下的工作区，本项目里 = `e:\AI_Course\` 根 |

---

## 5. 用户对 AI 的元反馈（meta-feedback）

> AI 工作过程中收到的"做得好"/"应该这样"反馈。沉淀下来供未来 AI 参考。

- **[2026-05-21]** 用户希望首次构建知识库时**先看一遍结构再做大规模 ingest**，
  AI 落地时采用了"骨架 + 少量示范"策略，规模约 33 页，用户后续如要扩展可按需 ingest。
- **[2026-05-21]** 用户主动提议补 `memory.md`，说明用户对**跨会话状态管理**有需求；
  AI 后续应主动维护本文件，不要等用户提醒。
- **[2026-05-21]** 用户在 AI 提出 3 个待决问题的当天就给了全部答案，说明用户希望
  **快速推进、不喜欢悬而未决**——AI 后续应少留空闲问题，能合理默认的就先做。
- **[2026-05-21]** push 到 GitHub 这一步用户在执行后说"先不要 push 了"——
  虽然命令已经成功，但说明用户**对"推送到外部"动作期望更高的二次确认**。
  AI 后续对**推送 / 发布 / 公开 / 删除远端**类不可逆动作，必须先复述"我接下来要做 X，是否继续？"再执行。

> [!style] 风格约束：
> - 当 AI 想做"大改动"（一次新建/删除 >5 个页面、修改 schema、删 raw 层）时，**先讲方案再动手**。
> - 当 AI 做"小改动"（追加一段、补一个链接、写一份新 source 摘要页）时，直接做就行，不必每次都征询。

---

## 6. 不要做的事

> 反向规则集。被用户明确表态过"别这样"的事，写在这里。

- ❌ 不要给 wiki 页面**抄原文大段文字**——AI 的价值是消化与组织，不是复制粘贴。
- ❌ 不要写"awesome list"风格的资源链接堆——本课程不需要外部资源墙。
- ❌ 不要把 AI 输出（包括 wiki 页本身）当作"权威结论"在讲稿里直接采用，必须经用户审过。
- ❌ 不要为了"看起来全面"而写没有信息的 bullet（如"DESeq2 的 5 大优点"这种空话）。
- ❌ **不要在未二次确认前推送到远端 / 改变远端可见性 / 删除远端仓库**（参见 §5 元反馈 2026-05-21）。

---

## 维护说明

- AI 完成一次有意义的工作（ingest、refactor、lint）后，**检查本文件 §3 是否需要更新**。
- 用户对工作方式提出新偏好时，AI 应**主动追加到 §1 或 §5**。
- 重大决策（影响目录结构、命名、流程）应**追加到 §2** 而不是埋在 chat 里。
- 本文件超过 ~500 行时，AI 可以提议归档旧条目到 `wiki/synthesis/memory_archive_<date>.md`。
