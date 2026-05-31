---
name: marp-slides-lingnan
description: 中山大学岭南学院专用Marp演示文稿制作助手。基于岭院PPT模板风格（深红配色、院徽页脚），提供完整工作流程：工作空间初始化、内容分析、slides制作、多维度审阅、中文语言规范审阅、PNG转换检查、终稿确定。所有产出物集中管理在项目工作文件夹中。当用户提到"岭院slides"、"岭南学院PPT"、"岭院演示"、"中大岭院"等关键词时自动启用。
allowed-tools: Read, Write, Edit, Bash, Task, Glob
---

# 中山大学岭南学院 Marp Slides 制作助手

## 技能概述

本技能是专为**中山大学岭南学院**定制的Marp演示文稿制作工具。内置岭院官方PPT模板风格——深红配色（`#AC1B20`）、院徽页脚品牌标识、AACSB国际认证标志。提供系统性七阶段制作流程，支持16:9和4:3两种宽高比，所有产出物集中管理。

## 模板设计特色

| 元素 | 规格 |
|------|------|
| 顶部装饰线 | `#AC1B20` 深红色，4px |
| 幻灯片标题 | `#AC1B20` 深红色 |
| 页脚灰条 | `#DCDDDF`，含岭院品牌标识 |
| 页脚底线 | `#AC1B20` 深红色，4px |
| 页脚左侧 | 中大校徽 → 岭院院徽 → "中山大学岭南学院"中英文 |
| 页脚右侧 | AACSB国际认证标志 |
| 字体 | PingFang SC / Microsoft YaHei |
| 宽高比 | 16:9（默认）或 4:3 |

## 核心原则

> **重要**：在动笔前先读 `references/pitfalls-and-capacity.md`。该文档基于实战复盘，量化了画布容量、列出了 8 类高频陷阱与对策，是本 skill 的核心知识。

### 字号选择决策（强制）

岭院 16:9 画布为 `1280×720`，建议 padding `50/70/90/70`，可用内容区 `1140×580`。**默认基准字号 30px**——这是经过实测的最佳平衡点：

| 内容场景 | 推荐基准字号 | 说明 |
|---------|------------|------|
| **常规内容页**（默认） | `30px` | 6–9 行内容、列表 6–10 项、表格 ≤ 7 行 |
| 数据密集页（多列表格） | `28px` | 表格用 `0.82em` 进一步缩到 ~23px |
| 标题页 / 总结页（少字大字） | `34–36px` | 仅 3–5 行核心信息时使用 |
| 不要 | `< 26px` | 投影距离下不可读 |
| 不要 | `> 40px` | 一页放不下完整观点 |

**字号选择规则**：先按 30px 草稿写 → 若内容明显放不下且无法精简则降到 28px → 若内容稀少则升到 34px。**不要为了塞内容反复降字号**，那是密度失控的信号。

### 每页内容硬约束（强制）

下列上限通过反复溢出实测得出，**违反必然产生截断或孤字**：

| 元素类型 | 满页硬上限 | 单元素上限 |
|---------|----------|-----------|
| **正文段落** | **9 行**（含自动换行展开） | 单段 ≤ 2 行 |
| **bullet 列表** | **9 项** | 单项 ≤ 25 个汉字（避免折行） |
| **表格** | **header + 7 行** | 单格内容 ≤ 18 字 |
| **数学公式块** | 每个按 2 行计 | 公式 + 注释合计 ≤ 6 行 |
| **lead/居中页** | **6–7 行** | 居中样式放大段距，需更宽松 |
| **roadmap 4 阶段** | 每阶段 ≤ 4 项，每项 ≤ 12 字 | 否则盒子撑高错位 |

**行数估算法**：每段中文按"30 字 = 1 行"估算自动换行；写完后从头数"渲染行数"，**超过 9 行立即拆页或精简**——不要等到 PNG 自审才发现。

### 文字内容约束（强制）

- **每页一个核心观点**——若一页要讲两件事，拆成两页
- **每条 bullet 起首加粗关键词**——`**关键词**：解释`（中文全角冒号 `：`），让扫读者 0.5 秒抓重点。**不要用** `**关键词** — 解释`（带空格的英文破折号）——那是英文 PPT 的习惯，中文里读起来生硬
- **不要二级嵌套 bullet**——改用内联"主题：解释"结构（嵌套缩进会破坏视觉密度）
- **每段首句即结论**——评委只读首句也能跟上叙事
- **避免同义重复**——"大模型即LLM"这类括号注释只在第一次出现时给一次
- **总结页禁用纯 lead 类居中**——容易出孤字；改用 h1 标题 + 内联格式

### 中文标点与翻译腔反模式（强制）

为中文受众做的 slides 必须用地道中文。下列模式是英文直译的痕迹，每条都在实战中被用户当面纠正过——一旦发现立刻改：

#### 1. 标签—解释分隔符：用 `：` 不用 `—`

| 情况 | 写法 | 说明 |
|------|------|------|
| Bullet 标签 + 解释 | `**关键词**：解释内容` | ✅ 中文全角冒号 |
| Bullet 标签 + 解释 | `**关键词** — 解释内容` | ❌ 英文破折号是英文 PPT 习惯 |
| 句中"即"/"也就是"语气 | `**核心创新**：把 X 转化为 Y` | ✅ 直接用冒号 |
| 句中"即"/"也就是"语气 | `**核心创新**——把 X 转化为 Y` | ⚠️ 双破折号 `——` 是中文标准强调用法，**仅在句子级**使用，不要在 bullet 标签后用 |

#### 2. 动词后置作定语 / 动名词宾语前置

英文 V-ing 短语逐字翻译成中文是经典翻译腔。中文动作要"动词在前 + 宾语在后"。

| ❌ 翻译腔 | ✅ 地道中文 | 对应英文 |
|----------|-------------|----------|
| 人机差异**识别** | **识别**人机差异 | identify human-AI differences |
| 行为模式**扫描** | **扫描**行为模式 | scan behavior patterns |
| 数据特征**提取** | **提取**数据特征 | extract data features |

**例外**：技术领域的固定搭配（数据备份、版本回滚、模块化开发、随机种子归档、参数调优）属于已建立的中文术语，不算翻译腔。判断标准：在中文社区里有没有人长期这么说？没有就要倒过来。

#### 3. 直译英文学术术语

英文术语字面直译成中文造词，跨学科评审听不懂。换成功能描述。

| ❌ 直译造词 | ✅ 描述性中文 | 原英文 |
|------------|--------------|--------|
| 行为楔子 | 人机系统性差异 | behavioral wedge |
| 心智图景 | 认知模型 | mental model |
| 政策杠杆 | 政策抓手 / 政策工具 | policy lever |

#### 4. 标点拼接陷阱：`？：` / `。：` / `！：`

bullet 标签是问句结尾时不要再接冒号——视觉上 `？：` / `。：` 都很别扭。两个解决办法：

| ❌ 别扭 | ✅ 改写 |
|---------|---------|
| `**X 是否真实存在？**：员工 Y 是否会侵蚀 Z？` | `**X 是否真实**：员工 Y 是否会侵蚀 Z？` |
| `**接下来怎么办？**：分三步走` | `**应对方案**：分三步走` |

把标签改成陈述短语（去掉问号），或者整体重写成名词短语。

#### 5. 中文引号

正文里用中文弯引号 `"…"` 和 `'…'`（U+201C/D, U+2018/9），不要用英文直引号 `"…"`。**但是 YAML frontmatter（`---` 之间的部分）必须保留英文直引号**——否则 YAML 解析器报错。如果用 chinese-quote-converter 等脚本批量转换，记得检查并还原 frontmatter 的引号。

### Slides 设计原则

| 原则 | 说明 | 要点 |
|------|------|------|
| 一页一点 | 每页只讲一个核心观点 | 避免信息过载 |
| 视觉层次 | 标题（红色）→ 要点（粗体）→ 细节 | 标题自动红色突出 |
| 留白充足 | 内容占页面 60–80% | 过满与过空都需调整 |
| 文字精简 | 每页 ≤ 9 行（硬上限） | 关键词优于完整句子 |
| 品牌一致 | 每页自动带岭院页脚 | 不要手改 footer 字段 |

### 内容密度参考

- **标题页**：主标题 + 副标题 + 演讲人信息（3–4 行）
- **内容页**：红色标题 + 3–5 个要点（每点 1 行最佳，最多 2 行）
- **对比页**：两栏对比，每栏 ≤ 4 点
- **总结页**：3–5 个核心要点，**用内联格式而非纯 lead 居中**
- **路线图页**：4 阶段并列，每阶段 ≤ 4 项

### 行距随密度自适应（重要）

**当一页内容明显偏少（≤ 5 个 bullet 或合计渲染 ≤ 5 行）时，应主动加大行距与列表项间距**——否则页面下半部分会出现大块空白，视觉上显得稀疏、缺乏分量感。这一规则尤其适用于 **目录页 / 提纲页 / 总结页 / 章节封面**。

**操作方式**——为该页加 `<!-- _class: outline -->` 指令（或自定义 class），并在 frontmatter style 块中追加：

```css
section.outline ul li { margin: 0.55em 0; line-height: 1.7; }
section.sparse ul li { margin: 0.4em 0; line-height: 1.7; }

/* 关键：稀疏页内容纵向居中（覆盖 lingnan 主题的顶对齐） */
section.outline, section.sparse {
  justify-content: center !important;
}
```

> **为什么需要 `!important`**：lingnan.css 里 `section { justify-content: flex-start !important; ... }` 强制顶对齐。不加 `!important` 你的覆盖会被忽略——content 仍然贴顶，下半页大块空白，每次都让用户失望。

**指导原则**——不要为了"显得更满"而拼命塞内容，宁可加大行距 + 纵向居中让少量信息呼吸；反之，密集页保持默认 1.55 行高，保证 9 行硬上限不被破坏。判断阈值：

| 实际渲染行数 | 推荐 `line-height` | 推荐 li `margin` |
|------------|-------------------|-----------------|
| ≤ 5 行（稀疏） | 1.7–1.8 | 0.5–0.7em |
| 6–8 行（常规） | 1.55（默认） | 默认 |
| 9 行（满页） | 1.5 | 0 |

写完后用 PNG 自审检查内容是否落在画布纵向中段 60–70%，避免上紧下空。

### 标题格式说明（强制 h1）

岭院主题**仅对 `h1` 染红色** `#AC1B20`，h2/h3 保持深色。**所有幻灯片标题必须用 `# 标题`（h1）**，否则会出现"目录页是黑色但其他页是红色"的不一致问题。

| 页面类型 | 标题格式 | 指令 |
|----------|---------|------|
| 标题页 | `# 主标题` | `<!-- _class: title -->` |
| 目录页 | `# 汇报提纲` 或 `# 目录` | **必须 h1**，不要用 h2 |
| 内容页 | `# 页面标题` | 无需指令 |
| 分隔页 | `# Part X` | `<!-- _class: divider -->` |
| 总结页 | `# 总结：……` | 不建议用 lead 类 |
| 致谢页 | `# 谢谢！` | `<!-- _class: thanks -->` |

## 七阶段工作流程

严格按照以下流程执行，每阶段结束后询问用户确认：

### 阶段零：工作空间初始化（预处理）

**触发**：用户请求制作岭院slides时立即执行

**执行步骤**：

1. **确定项目名称**：
   - 根据用户提供的主题/文件名确定项目名称
   - 使用简短的英文或拼音命名，用连字符连接
   - 示例：`python-control-structures`、`financial-analysis`

2. **询问演讲人信息和宽高比**：

   使用 AskUserQuestion 工具：

   ```
   questions:
     - question: "请选择slides的宽高比"
       header: "宽高比"
       multiSelect: false
       options:
         - label: "16:9（推荐）"
           description: "宽屏，适合投影仪和现代显示器"
         - label: "4:3"
           description: "标准比例，适合旧式投影仪和打印"
     - question: "请输入演讲人信息（可选，多个信息用逗号分隔）"
       header: "演讲人信息"
       multiSelect: false
       options:
         - label: "姓名, 职务, 日期"
           description: "例如：张三, 教授, 2026年"
         - label: "姓名, 职务"
           description: "例如：张三, 教授"
         - label: "仅姓名"
           description: "例如：张三"
         - label: "不填"
           description: "跳过演讲人信息，后续手动添加"
   ```

3. **创建工作文件夹结构**：
   ```bash
   mkdir -p slides_[项目名]/{01_analysis,02_drafts,03_reviews,04_exports,05_final}
   ```

4. **复制品牌图片到工作空间**：

   ```bash
   mkdir -p slides_[项目名]/images
   cp marp-slides-lingnan/images/logo-red5.png slides_[项目名]/images/
   cp marp-slides-lingnan/images/aacsb-logo.png slides_[项目名]/images/
   ```

   > CSS主题通过 `url('../images/logo-red5.png')` 引用图片。从 `02_drafts/` 执行 marp 时，相对路径解析为 `slides_[项目名]/images/`。

5. **文件夹结构说明**：

   ```text
   slides_[项目名]/
   ├── images/                # 品牌图片
   │   ├── logo-red5.png         # 中大校徽+岭院院徽+中英文名称
   │   └── aacsb-logo.png        # AACSB国际认证标志
   ├── 01_analysis/           # 阶段一：分析报告
   │   ├── content-analysis.md   # 内容分析报告
   │   └── outline.md            # Slides大纲
   ├── 02_drafts/             # 阶段二：初稿
   │   └── presentation.md       # Slides初稿
   ├── 03_reviews/            # 阶段三：审阅报告
   │   ├── content-review.md     # 内容审阅
   │   ├── format-review.md      # 格式审阅
   │   ├── density-review.md     # 密度审阅
   │   ├── visual-review.md      # 视觉审阅
   │   ├── chinese-review.md     # 中文规范审阅
   │   └── summary.md            # 综合审阅报告
   ├── 04_exports/            # 阶段四：PNG/HTML导出
   ├── 05_final/              # 阶段五：终稿
   │   ├── presentation.md       # 最终Markdown
   │   ├── slides.html           # HTML版本
   │   └── slides.pdf            # PDF版本
   └── README.md              # 项目说明文件
   ```

6. **创建README.md**：
   ```markdown
   # [项目名] Slides

   ## 项目信息
   - 创建时间：[日期]
   - 输入材料：[原始文件名]
   - 宽高比：[16:9 / 4:3]
   - **使用主题**：lingnan（中山大学岭南学院专用）

   ## 文件夹说明
   - `01_analysis/` - 内容分析和大纲
   - `02_drafts/` - Slides初稿
   - `03_reviews/` - 审阅报告
   - `04_exports/` - PNG和HTML导出
   - `05_final/` - 最终版本

   ## 制作进度
   - [ ] 阶段零：工作空间初始化
   - [ ] 阶段零B：演讲需求访谈
   - [ ] 阶段一：内容分析
   - [ ] 阶段二：初稿制作
   - [ ] 阶段三：多维度审阅
   - [ ] 阶段三B：中文语言规范审阅
   - [ ] 阶段四：PNG转换检查
   - [ ] 阶段五：问题修复与终稿
   ```

**输出**：工作文件夹路径、宽高比选择、演讲人信息，告知用户所有产出物将保存在此文件夹中

---

### 阶段零B：演讲需求访谈（强制，先于内容分析）

**触发**：工作空间初始化完成后立即执行；**只有完成本阶段，才能进入阶段一调用规划/分析子代理**。

**为什么必须先访谈**：同一份输入材料，给本科生上课、给学院同行汇报、给评审专家答辩，所要求的叙事节奏、术语密度、证据深度完全不同。若跳过访谈直接做分析，规划代理只能按"通用学术汇报"默认设定走，往往与真实场景错位，后期需要大改。让用户先回答几个关键问题，规划阶段才有明确的优化目标。

**执行步骤**：

1. **使用 AskUserQuestion 工具收集核心需求**——一次性把下列问题打包发出，避免多轮打扰：

   ```
   questions:
     - question: "本次演讲的主要受众是谁？"
       header: "受众"
       multiSelect: false
       options:
         - label: "本科生 / 研究生课堂"
           description: "教学场景，需要循序渐进、概念清晰、配合举例"
         - label: "学院同行 / 学术研讨"
           description: "同领域听众，可使用术语、强调贡献与方法"
         - label: "跨学科学者 / 校内汇报"
           description: "听众背景多元，需降低术语门槛、突出动机"
         - label: "评审专家 / 答辩委员会"
           description: "强调创新点、证据链、可行性，节奏紧凑"
         - label: "行业 / 企业 / 政府"
           description: "重应用与影响，弱化推导细节"
         - label: "其他（稍后说明）"
           description: "在后续对话中补充描述"
     - question: "演讲目的是什么？"
       header: "目的"
       multiSelect: false
       options:
         - label: "教学讲解（让听众学会）"
           description: "目标是知识传授与理解"
         - label: "成果汇报（展示已做的工作）"
           description: "目标是清晰传达进展与发现"
         - label: "课题答辩 / 项目申请"
           description: "目标是说服评审，强调创新与可行性"
         - label: "学术报告（分享研究）"
           description: "目标是引发讨论与同行反馈"
         - label: "宣讲 / 科普"
           description: "目标是激发兴趣，弱化技术细节"
     - question: "预计演讲时长？"
       header: "时长"
       multiSelect: false
       options:
         - label: "≤ 10 分钟（短报告）"
           description: "建议 8–12 页，节奏紧凑"
         - label: "15–20 分钟（标准汇报）"
           description: "建议 12–18 页"
         - label: "25–40 分钟（完整报告 / 一节课）"
           description: "建议 20–30 页"
         - label: "≥ 60 分钟（长讲座 / 多节课）"
           description: "建议分模块，每模块独立 outline"
     - question: "希望的整体风格？"
       header: "风格"
       multiSelect: false
       options:
         - label: "严谨学术（默认）"
           description: "正式书面语，重逻辑与证据"
         - label: "教学友好"
           description: "多举例、多类比，关键术语首次出现给定义"
         - label: "凝练简洁（评审/答辩）"
           description: "首句即结论、密度更高、删减背景"
         - label: "故事化叙事"
           description: "以问题—探索—答案为主线，情境引入"
   ```

2. **追问开放式补充信息**（使用普通对话，不必再走 AskUserQuestion）：

   - 是否有**必须强调的核心观点 / 卖点**？（最多 3 条）
   - 是否有**必须避开或弱化的内容**？（如尚未发表的细节、敏感数据）
   - 是否有**已知的听众背景知识水平**？（例如"听众熟悉 LLM 但不熟悉合约理论"）
   - 是否需要**预留 Q&A / 互动 / 演示 环节**？

   若用户表示"你来定"或不回答，则按受众+目的的默认组合推断，并在分析报告里明确写出"按默认假设处理"以便后续修订。

3. **将访谈结果落盘**——保存到 `slides_[项目名]/01_analysis/audience-brief.md`，作为阶段一规划代理的强制输入：

   ```markdown
   # 演讲需求简报

   - 受众：……
   - 目的：……
   - 时长：……（建议页数：……）
   - 风格：……
   - 必须强调：……
   - 必须弱化 / 回避：……
   - 听众背景假设：……
   - 互动 / Q&A 安排：……

   > 上述需求由用户在阶段零B 确认，阶段一的内容分析与大纲规划必须以此为约束目标。
   ```

4. **向用户复述简报并请确认**：用 1 段话总结上述要点（不要重复列点形式），明确告知"接下来将基于这些需求调用规划代理做内容分析与大纲设计"，征得用户同意后再进入阶段一。

**输出**：`audience-brief.md` 路径 + 用户确认。**未完成本阶段不得调用阶段一的分析/规划子代理。**

---

### 阶段一：内容分析与消化

**触发**：阶段零B 的演讲需求访谈完成、`audience-brief.md` 生成并经用户确认之后；用户提供输入文件（PDF、论文、文档、笔记等）。

**前置硬约束（必读）**：在调用任何分析/规划子代理之前，**必须先 Read `slides_[项目名]/01_analysis/audience-brief.md`**，并将其中的"受众 / 目的 / 时长（含建议页数）/ 风格 / 必须强调 / 必须弱化 / 背景假设 / Q&A 安排"作为本阶段的硬约束传给子代理。子代理 prompt 中须显式包含这些字段——大纲页数贴齐时长建议、术语密度对齐受众背景、卖点对齐"必须强调"、回避点不出现在大纲。

**执行步骤**：

1. **初步阅读**：使用 Read 工具读取 `audience-brief.md` 与输入文件，了解整体结构
2. **深度分析**：
   - 提取核心论点和关键信息
   - 识别逻辑结构（问题-方案-结论 / 现状-分析-建议 等）
   - 标记重要数据、引用、案例
3. **内容分类**：
   - 核心观点（必须包含）
   - 支撑证据（选择性包含）
   - 背景信息（简化或省略）
4. **大纲生成**：
   - 确定slides数量（建议10-20页）
   - 规划每页主题和内容密度
   - 设计叙事流程

**文件保存**：
- 内容分析报告：`slides_[项目名]/01_analysis/content-analysis.md`
- Slides大纲：`slides_[项目名]/01_analysis/outline.md`

**输出模板**：

`01_analysis/content-analysis.md`:
```markdown
## 内容分析报告

### 文档概述
- 主题：[主题]
- 类型：[论文/报告/教程/...]
- 核心论点：[1-2句话]

### 关键内容提取
1. [关键点1]
2. [关键点2]
...
```

`01_analysis/outline.md`:
```markdown
## Slides大纲（预计X页）

1. 标题页
2. [内容页标题]
3. ...
```

---

### 阶段二：Slides初稿制作

**触发**：用户确认内容分析和大纲

**执行步骤**：

1. **读取模板**：使用 Read 工具读取 `marp-lingnan-template.md`

2. **配置YAML Frontmatter（强制使用完整 style 块）**：

   下面这段 style 是经过实战复盘修复的稳定配置——**不要删减**。每一项的存在都对应一个曾踩过的坑（详见 `references/pitfalls-and-capacity.md` 第三节）：

   ```yaml
   ---
   marp: true
   theme: lingnan
   paginate: true
   size: [用户选择的宽高比]
   header: ''
   footer: ' '
   style: |
     /* 图片居中 */
     img {
       display: block !important;
       margin: 0 auto !important;
     }
     /* 内容区与基准字号 */
     section {
       font-size: 30px;
       padding: 50px 70px 90px 70px;
     }
     section h1 { font-size: 1.55em; }
     section h2 { font-size: 1.35em; }

     /* 表格：保住红头白字（!important 链不可删，否则 thead 会塌成空白） */
     section table {
       display: table !important;
       width: 100% !important;
       margin-left: auto !important;
       margin-right: auto !important;
       font-size: 0.82em;
       border-collapse: collapse;
     }
     section table thead {
       background-color: #AC1B20 !important;
     }
     section table thead th {
       color: #ffffff !important;
       background-color: #AC1B20 !important;
       padding: 0.5em 0.8em !important;
       font-weight: 700 !important;
       text-align: left !important;
       border: none !important;
     }
     section table tbody td {
       padding: 0.45em 0.8em !important;
     }

     /* 列表节奏 */
     section ul, section ol { font-size: 1em; line-height: 1.55; }
     section.outline ul li { margin: 0.55em 0; line-height: 1.7; }
     section.sparse ul li { margin: 0.4em 0; line-height: 1.7; }
     section blockquote { font-size: 1em; }

     /* 稀疏页内容纵向居中（必须 !important，因为 lingnan 主题强制 flex-start） */
     section.outline, section.sparse {
       justify-content: center !important;
     }

     /* 4 阶段技术路线图组件（用 <div class="roadmap"> 调用） */
     .roadmap { display: flex; gap: 12px; margin-top: 18px; }
     .roadmap-phase {
       flex: 1;
       border: 2px solid #AC1B20;
       border-radius: 8px;
       padding: 14px 12px;
       background: #FBF3F3;
     }
     .roadmap-phase h4 {
       color: #AC1B20;
       margin: 0 0 8px 0;
       font-size: 0.95em;
       border-bottom: 1px solid #AC1B20;
       padding-bottom: 4px;
     }
     .roadmap-phase ul {
       margin: 0;
       padding-left: 18px;
       font-size: 0.78em;
       line-height: 1.5;
     }
     .roadmap-phase .date {
       font-size: 0.72em;
       color: #666;
       margin-bottom: 6px;
     }
   ---
   ```

   > **重要**：`footer: ' '`（含一个空格）必须保留。岭院品牌标识（校徽、院徽、AACSB标志）由CSS主题自动渲染在页脚，不要也不能通过 footer 字段设置。

3. **标题格式**：使用 `#` (h1) 作为幻灯片标题，CSS自动渲染为岭院深红色。

4. **页面类型和指令**：

   | 页面类型 | 指令 | 标题格式 |
   |----------|------|---------|
   | 标题页 | `<!-- _class: title -->` | `# 主标题` |
   | 目录页 | 无需指令 | `# 目录` |
   | 内容页 | 无需指令 | `# 页面标题` |
   | 分隔页 | `<!-- _class: divider -->` | `# Part X` |
   | 引导页 | `<!-- _class: lead -->` | `# 标题` |
   | 致谢页 | `<!-- _class: thanks -->` | `# 谢谢！` |

5. **演讲人信息**：根据阶段零收集的信息，填入标题页。

6. **逐页制作**：
   - 遵循模板中的页面类型和格式
   - 每页严格控制内容量
   - 使用适当的Markdown格式（粗体、引用、列表）

**文件保存**：
- 保存初稿：`slides_[项目名]/02_drafts/presentation.md`
- 更新README.md中的进度状态

---

### 阶段三：多维度并行审阅

**触发**：初稿完成后自动进入

**执行方式**：使用 Task 工具并行派遣4个专业agent（与通用 marp-slides-creator 相同）

并行审阅四个维度：内容审阅、格式审阅、密度审阅、视觉审阅。详细Agent配置和输出格式参考 `references/review-checklist.md`。

**岭院主题特有检查项**（增加在各审阅agent中）：

1. **内容审阅**：无特殊要求
2. **格式审阅增加**：
   - `footer: ' '` 是否正确设置？
   - `<!-- _class: -->` 指令是否与页面类型匹配？
3. **密度审阅**：无特殊要求
4. **视觉审阅增加**：
   - 顶部红线是否正确显示？
   - 页脚灰条和品牌标识是否清晰？
   - 页脚红色底线是否可见？
   - 标题是否为岭院深红色？

**文件保存**：
- 内容审阅：`slides_[项目名]/03_reviews/content-review.md`
- 格式审阅：`slides_[项目名]/03_reviews/format-review.md`
- 密度审阅：`slides_[项目名]/03_reviews/density-review.md`
- 视觉审阅：`slides_[项目名]/03_reviews/visual-review.md`
- 综合报告：`slides_[项目名]/03_reviews/summary.md`

---

### 阶段三B：中文语言规范审阅

**触发**：多维度审阅完成后执行

**执行方式**：使用 Task 工具派遣 subagent，详细流程与通用 marp-slides-creator 的"阶段三B"完全相同。

**文件保存**：`slides_[项目名]/03_reviews/chinese-review.md`

---

### 阶段四：PNG 转换与强制视觉自审

**触发**：审阅修改完成后

> **这是岭院主题在中文长内容场景下最关键的质量门槛。** 跳过此步骤几乎必然产生溢出页。LLM 自己写的 markdown 在浏览器里渲染后总会出现"看似 6 行的内容实际占 11 行"的偏差，唯一可靠的办法是把每页 PNG 读出来用多模态视觉自查。

**执行步骤**：

1. **转换为 PNG**（注意输出路径必须以 `/slide.png` 结尾，否则 marp-cli 会把目录名当前缀）：

   ```bash
   # HTML 预览
   npx @marp-team/marp-cli slides_[项目名]/02_drafts/presentation.md \
     -o slides_[项目名]/04_exports/slides.html \
     --html --theme-set <skill-path>/themes/ --allow-local-files

   # PNG 序列（关键：末尾的 slide.png 是文件名前缀，不是目录）
   npx @marp-team/marp-cli slides_[项目名]/02_drafts/presentation.md \
     --images png \
     -o slides_[项目名]/04_exports/slide.png \
     --theme-set <skill-path>/themes/ --allow-local-files
   ```

   > **常见错误**：写成 `-o slides_[项目名]/04_exports/`（没有文件名）会让输出落到 `04_exports.001.png` 等错位文件名上。**必须显式指定 `slide.png`**。
   >
   > **必带参数**：`--theme-set <skill-path>/themes/` 加载岭院主题；`--allow-local-files` 加载页脚品牌图片。缺一不可。

2. **并行子代理视觉自审（强制）**：

   **不要由主代理逐张 Read PNG**——20 张 PNG 会快速消耗主代理上下文，且串行慢。改用 Task 工具派出多个 Explore（或 general-purpose）子代理并行检查。

   **派遣策略**：

   - 按 PNG 总数划分批次：**每个子代理负责 3–5 张连续 PNG**（例如 21 张 → 派 5 个子代理，每个负责 4–5 张）
   - **在同一条消息中并行发起所有 Task 调用**（多个 tool_use 块），不要串行
   - 每个子代理拿到的 prompt 应包含：负责的 PNG 文件路径列表、检查清单、报告格式

   **子代理 prompt 模板**（每个子代理独立使用）：

   ```
   你是岭院 Marp PPT 视觉审阅员。请用 Read 工具逐张读取以下 PNG，对每页按检查表打分并报告问题：

   PNG 文件列表（按顺序读）：
   - <path>/slide.005.png
   - <path>/slide.006.png
   - <path>/slide.007.png
   - <path>/slide.008.png

   每页检查项：

   **A. 视觉布局**
   1. 标题是否为岭院红色（#AC1B20）——h1 才会红色，h2/h3 是黑色
   2. 表头是否红底白字（如有表格）——表头空白说明 thead CSS 失效
   3. 末行是否完整可见——文字被页脚灰条挡住即为溢出
   4. **是否出现孤字尾**——bullet 折行后第二行只剩 1–3 字符（如末尾"哪？"、"架"、"体并发"）独占一行；这会让 slide 显得不整齐，必须精简该 bullet
   5. 列表项是否单行——单项折成 2 行说明文字过长
   6. 内容占比是否 60–80%——过满（>90%）或过空（<40%）都需调整
   7. **稀疏页是否纵向居中**——稀疏页（≤ 5 行）应使用 `<!-- _class: sparse -->` 或 `outline` 并启用居中 CSS；如果内容贴顶、下半页大块空白，说明 `justify-content: center !important` 没生效
   8. 数学公式是否完整——溢出右边缘即为问题
   9. 页脚品牌标识是否完整——校徽 + 院徽 + AACSB 都需可见

   **B. 中文标点与翻译腔**（参考 SKILL.md 中"中文标点与翻译腔反模式"小节）
   10. **bullet 标签后是 `：` 还是 `—`**——只允许中文全角冒号 `：`；带空格的英文破折号 `—` 是英文 PPT 习惯，必须替换
   11. **是否出现 `？：` / `。：` / `！：`**——bullet 标签是问号/句号/感叹号结尾再接冒号，视觉别扭，需要把标签改成陈述短语
   12. **是否有动词后置作定语**——如 `X 识别` / `Y 扫描` / `Z 提取`（V-ing 直译模式），改成 `识别 X` / `扫描 Y` / `提取 Z`。例外是已建立的中文术语（数据备份、模块化开发等）
   13. **是否有英文术语直译造词**——如"行为楔子"（wedge）、"心智图景"（mental model），改成描述性中文
   14. **正文引号**是否为中文弯引号 `"…"`——直引号 `"…"` 是英文风格；但 YAML frontmatter 必须保留直引号

   报告格式（仅返回结构化结论，不要返回 PNG 内容）：
   ## 第 N 页（slide.NNN.png）
   - 状态：✅ 通过 / ⚠️ 有问题
   - 问题（若有）：具体描述
   - 修复建议：具体可执行的措施
   ```

   **子代理输出收敛**：所有子代理返回简短结构化报告（每页 1–3 行），主代理汇总成总问题清单。**禁止子代理把 PNG 原图返回主代理**，只返回文字结论。

3. **根据子代理报告批量修复**：

   - 收齐所有子代理报告 → 汇总问题清单（按页码升序）
   - 按问题类型批量修复（先修同类问题，避免 markdown 文件反复改动）
   - 常见问题对应措施：
     - 溢出 → 按"内容硬约束"表精简或拆页
     - 表头空白 → 确认 frontmatter style 块包含 thead `!important` 链
     - 标题不红 → 把 `##` 改回 `#`
   - 修复后重新渲染 PNG，**再次派出子代理并行复查**（仅复查曾报问题的页面），直到全部通过

4. **可选：并行部署多维审阅 Agents**：内容、格式、密度、视觉四维（参考 `references/review-checklist.md`）。在通过视觉自审之后再做，作为额外质检。

**文件保存**：
- HTML 预览：`slides_[项目名]/04_exports/slides.html`
- PNG 图片：`slides_[项目名]/04_exports/slide.001.png`, `.002.png`, ...

---

### 阶段五：问题修复与终稿确定

**触发**：收到所有页面检查报告

**执行步骤**：

1. **问题分类**：
   - **溢出问题**：文字超出页面 → 拆分页面或精简内容
   - **密度问题**：内容过多 → 删减或重组
   - **格式问题**：排版错误 → 修正Markdown
   - **品牌问题**：页脚品牌标识不清晰 → 检查CSS和图片路径

2. **逐一修复**并重新验证

3. **生成终稿**：

   ```bash
   cp slides_[项目名]/02_drafts/presentation.md slides_[项目名]/05_final/presentation.md

   # 导出HTML
   npx @marp-team/marp-cli slides_[项目名]/05_final/presentation.md -o slides_[项目名]/05_final/slides.html --html --theme-set marp-slides-lingnan/themes/ --allow-local-files

   # 导出PDF
   npx @marp-team/marp-cli slides_[项目名]/05_final/presentation.md -o slides_[项目名]/05_final/slides.pdf --theme-set marp-slides-lingnan/themes/ --allow-local-files

   # 导出可编辑PPTX（需LibreOffice）
   npx @marp-team/marp-cli slides_[项目名]/05_final/presentation.md -o slides_[项目名]/05_final/slides.pptx --pptx-editable --theme-set marp-slides-lingnan/themes/ --allow-local-files
   ```

4. **更新项目README**，标记所有阶段完成。

**终稿文件位置**：
- 最终Markdown：`slides_[项目名]/05_final/presentation.md`
- HTML版本：`slides_[项目名]/05_final/slides.html`
- PDF版本：`slides_[项目名]/05_final/slides.pdf`
- PowerPoint版本：`slides_[项目名]/05_final/slides.pptx`

---

## Marp-CLI 命令参考

```bash
# 预览初稿（启动本地服务器）
npx @marp-team/marp-cli -s slides_[项目名]/02_drafts/presentation.md --theme-set marp-slides-lingnan/themes/ --allow-local-files

# 导出HTML
npx @marp-team/marp-cli slides_[项目名]/02_drafts/presentation.md -o slides_[项目名]/04_exports/slides.html --html --theme-set marp-slides-lingnan/themes/ --allow-local-files

# 导出PNG
npx @marp-team/marp-cli slides_[项目名]/02_drafts/presentation.md --images png -o slides_[项目名]/04_exports/ --theme-set marp-slides-lingnan/themes/ --allow-local-files

# 导出终稿PDF
npx @marp-team/marp-cli slides_[项目名]/05_final/presentation.md -o slides_[项目名]/05_final/slides.pdf --theme-set marp-slides-lingnan/themes/ --allow-local-files

# 导出终稿PPTX
npx @marp-team/marp-cli slides_[项目名]/05_final/presentation.md -o slides_[项目名]/05_final/slides.pptx --pptx-editable --theme-set marp-slides-lingnan/themes/ --allow-local-files
```

**参数说明**：

| 参数 | 说明 |
|------|------|
| `--theme-set marp-slides-lingnan/themes/` | **必需**。加载岭院CSS主题 |
| `--allow-local-files` | **必需**。允许加载本地品牌图片（院徽、认证标志） |
| `--html` | 启用HTML标签支持 |
| `-s` | 启动预览服务器 |
| `--images png` | 导出PNG图片序列 |

---

## 交互规范

1. 每阶段结束后询问用户是否继续
2. 内容分析后让用户确认大纲再继续
3. 检查发现问题时，说明问题和建议的修复方案
4. 岭院品牌元素由CSS主题自动处理，无需用户干预

## 禁止事项

- 不跳过内容分析直接制作slides
- 不在单页放置过多内容
- 不使用过小的字体或过密的排版
- 不忽略PNG检查结果
- 不修改footer字段（品牌信息由CSS承载，`footer: ' '` 必须保留）
- 不输出未经验证的终稿

## 资源引用

### 参考文件
- **`marp-lingnan-template.md`** - 岭院Marp模板
- **`themes/lingnan.css`** - 岭院CSS主题
- **`images/logo-red5.png`** - 页脚品牌标识（中大校徽+岭院院徽+中英文名称）
- **`images/aacsb-logo.png`** - AACSB国际认证标志
- **`references/slide-types.md`** - 页面类型详解
- **`references/review-checklist.md`** - 审阅检查清单
