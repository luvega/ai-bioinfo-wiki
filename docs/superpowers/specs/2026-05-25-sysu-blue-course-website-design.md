# 中山大学蓝色 Beamer 风格课程网站设计 Spec

> 项目：医药数据处理与可视化课程网站  
> 日期：2026-05-25  
> 当前阶段：设计确认，不进入搭建  
> 参考来源：`https://ai.lingnan.top/`、`luvega/codex_ppt_skill`、本项目 `course/` 与 `knowledge/`

## 1. 目标

为《医药数据处理与可视化（36 课时 · AI 前置版）》建设一个课程网站。网站要同时承担两类任务：

1. **课堂门户**：从正式课程大纲出发，清楚呈现首页、课程大纲、18 周页面、资源索引、AI 协作规范。
2. **Coursebook**：不受 36 课时限制，吸收本项目已整理的参考书、AIDD 字幕、知识页、概念页和编程案例，形成可持续扩展的课程教材。

网站不只是静态资源列表，而应成为课程组织、学生自学、AI 协作记录和后续课件生成的统一入口。

## 2. 设计原则

### 2.1 课程主线优先

`course/syllabus/36课时-AI前置调整版.docx` 和 `course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md` 是事实主线。18 周页面的标题、顺序、教学重点和 AI 使用边界以它们为准。

### 2.2 Coursebook 可超出课堂

课堂 36 学时只决定授课节奏，不限制网站教材内容。Coursebook 应纳入：

- `course/weeks/week_01` 到 `week_18` 的大纲、讲稿和材料。
- `course/first_round_content.md` 中已形成的 Week 03、14、15、16 首轮内容。
- `materials/markdown/pdf_library_mineru/` 中的 ISLP、ISLR、AI assisted Python、Generative AI analytics、嵩天 Python 课件转换内容。
- `materials/markdown/aidd_bioinformatics/` 中的 AIDD 生物信息学章节素材。
- `knowledge/entities/`、`knowledge/concepts/`、`knowledge/synthesis/` 中沉淀的工具、概念和素材映射。
- 后续新增的编程案例、图表案例、AI prompt 案例和项目 rubric。

### 2.3 设计服务学习，不做宣传站

参考 `ai.lingnan.top` 的信息架构，但不复刻其品牌和内容。首页第一屏应直接进入课程学习场景，避免营销式 hero。视觉上采用中山大学蓝色 Beamer 风格，保持学术、克制、清晰。

### 2.4 资产可追溯

中山大学校徽、字标、校区照片、建筑剪影等素材来自 `luvega/codex_ppt_skill` 提供的模板资产清单。后续实现时应保留素材来源记录和 manifest，不直接散落复制。

## 3. 已提取参考信息

### 3.1 `ai.lingnan.top` 信息架构

参考站点的可借鉴结构：

- 顶部导航：首页、课程大纲、课程教材、教学平台、关于、搜索。
- 首页：课程定位、教学方法、入口卡片、实时指标。
- 课程大纲页：课程目标、章节或周次、评估方式、学习路径。
- 课程教材页：独立 book 子站，左侧目录，章节导航，全文搜索。
- 平台页：教师端、学生端、作业流程、AI 批改流程。
- 资源页：可作为后续教学平台或工具入口。

本项目采用其“课程门户 + 课程书 + 平台/规范”的骨架，但首期 MVP 不开发作业平台。

### 3.2 SYSU Beamer Blue 视觉基础

外部 skill：`luvega/codex_ppt_skill`  
参考风格：`beamer-sysu-blue`

已提取的视觉 token：

| Token | 值 | 用途 |
|---|---:|---|
| 主蓝 accent | `#0B4F6C` | 顶部栏、主按钮、章节标识 |
| 中蓝 secondary | `#3494BA` | 链接、辅助强调、图表辅助色 |
| 绿色 emphasis | `#029E73` | 成功状态、实践任务、通过核验 |
| 橙色 warning | `#DE8F05` | 风险提示、AI 边界提醒 |
| 背景 bg | `#FFFFFF` | 页面主体 |
| 浅蓝 surface | `#F3F8FB` | 信息区块背景 |
| 浅蓝 surface2 | `#E6F1F6` | 次级区块、表头 |
| 边框 border | `#D8E5EC` | 分隔线、表格线 |
| 正文 text | `#1D2733` | 主文本 |
| 弱文本 muted | `#667085` | 元信息、说明文字 |

字体策略：

- 中文主字体：`思源黑体 CN Medium`。
- 中文加重：`思源黑体 CN Heavy`。
- Windows 回退：`微软雅黑`、`等线`。
- 英文与代码：系统 sans + monospace；代码块使用稳定等宽字体。

页面风格转换规则：

- 保留 Beamer 的“顶部栏 + 小节标签 + 页脚进度”结构感。
- 网页上不模拟幻灯片边框，而是转为全宽学术门户布局。
- 大页面标题控制在稳重尺寸，避免过大营销字体。
- 每个屏幕只突出一个主要学习任务，避免堆叠太多卡片。
- 图像使用真实校区照片或课程相关图表，不使用抽象渐变装饰。

### 3.3 SYSU 素材类型

从 `strict-sysu-official-blue` asset manifest 提取到：

| 类别 | 数量 | 站点用途 |
|---|---:|---|
| `logo-wordmark-emblem` | 13 | 顶部品牌、页脚、关于区 |
| `campus-photo-or-background` | 11 | 首页首屏、周次页横幅、关于区 |
| `cutout-building-or-decorative` | 9 | 页脚或分区收束，谨慎使用 |
| `diagram-icon-or-small-photo` | 4 | 资源索引、案例入口 |
| `svg-mark-or-diagram` | 1 | 可作为辅助标识 |
| `unsupported-wdp-photo` | 8 | 首期不使用，除非转换验证 |

首期建议资产选择：

- 顶部栏：透明底中山大学校徽 + 中英文校名字标。
- 首页首屏：一张横向校区照片，叠加深蓝透明遮罩和课程标题。
- 资源索引或页脚：建筑剪影作为低调背景，不作为主体装饰。
- 不在网页中使用来源不明、无法压缩或无法渲染的 WDP 资源。

### 3.4 校训与校风文本

官方来源核验到中山大学校训：

> 博学 审问 慎思 明辨 笃行

站点中建议使用方式：

- 首页作为小号 institutional line，不抢课程标题。
- AI 协作规范页可把校训映射为学习方法：广泛学习、审慎提问、谨慎思考、明辨输出、笃行验证。
- 不写成大段校史宣传，避免偏离课程目标。

## 4. 网站信息架构

### 4.1 MVP 路由

```text
/
/syllabus
/weeks
/weeks/week-01
/weeks/week-02
...
/weeks/week-18
/resources
/ai-collaboration
```

### 4.2 建议预留路由

```text
/coursebook
/coursebook/concepts
/coursebook/programming-cases
/coursebook/visualization
/coursebook/omics
/coursebook/ai-assisted-analysis
/about
/search
```

预留路由首期可以不全部完成，但首页和资源索引中应体现 coursebook 的长期方向。

### 4.3 站点导航

顶部导航：

- 首页
- 课程大纲
- 18 周
- Coursebook
- 资源索引
- AI 协作规范

移动端导航：

- 抽屉菜单或底部简洁导航。
- 当前周次页面应有上一周/下一周跳转。

全站搜索：

- MVP 可先预留搜索入口。
- 若选 Astro，后续用 Pagefind 生成静态搜索。

## 5. 页面规格

### 5.1 首页 `/`

目标：让学生第一眼知道这是什么课、怎么学、从哪里进入。

内容模块：

1. SYSU 蓝色顶部栏：校徽/字标、课程名、主导航。
2. 首屏：课程名《医药数据处理与可视化》、副标题“AI 前置 · 36 课时 · 面向药学本科生”、校区照片背景。
3. 课程主线：医药问题 -> 数据结构 -> 统计方法 -> 可视化表达 -> AI 协作核验。
4. 三阶段学习路径：
   - Week 1-2：AI 边界、流程、复现。
   - Week 3-11：Python、R、清洗、统计、图表。
   - Week 12-18：高维数据、组学、综合项目。
5. 快速入口：
   - 课程大纲
   - 18 周页面
   - Coursebook
   - AI 协作规范
6. 本周学习卡片：可由后续配置指定当前周。
7. 页脚：校训、课程归属、素材与维护说明。

### 5.2 课程大纲 `/syllabus`

目标：呈现正式课程结构和评价逻辑。

内容模块：

- 课程基本信息：36 课时、18 周、对象、先修要求。
- 课程目标：数据处理、统计判断、图表表达、AI 协作核验。
- 18 周总表：周次、主题、核心能力、AI 使用边界。
- 三阶段结构图。
- 考核建议和项目产出。
- 与 Coursebook 的关系说明：课堂按 36 学时组织，Coursebook 提供扩展阅读和案例。

### 5.3 18 周总览 `/weeks`

目标：形成课程地图。

内容模块：

- 按阶段分组的周次网格。
- 每周卡片包含：周次、标题、关键词、课堂任务、AI 协作要求。
- 筛选维度：Python/R/统计/可视化/组学/项目/AI 协作。
- 进入单周页面。

### 5.4 周次页面 `/weeks/week-xx`

目标：把 `course/weeks/week_xx` 变成学生可读页面。

每周固定结构：

1. 周次标题和课程定位。
2. 本周要回答的问题。
3. 学习目标。
4. 课堂内容提纲。
5. 上机或讨论任务。
6. AI 协作边界与推荐 prompt。
7. 本周材料：本地讲稿、知识页、参考资源。
8. Coursebook 延伸阅读。
9. 上一周/下一周。

数据来源：

- `course/weeks/week_xx/outline.md`
- `course/weeks/week_xx/script.md`
- `course/weeks/week_xx/materials.md`
- `knowledge/index.md` 中与本周相关的知识页

### 5.5 资源索引 `/resources`

目标：不是堆链接，而是按课程任务组织素材。

建议分类：

- 课程主线：大纲、讲稿、每周材料。
- 参考书：ISLP、ISLR、AI assisted Python、Generative AI analytics、嵩天 Python。
- AIDD 生物信息学素材：Python/R/Bash、pipeline、RNA-seq、DESeq2、scRNA-seq、GitHub。
- 工具与库：Python、R、ggplot2、DESeq2、samtools、BLAST、GitHub、ChatGPT、Copilot。
- 编程案例：数据清洗、统计检验、火山图、热图、UMAP、AI prompt 记录。
- 规范模板：AI 协作记录、项目目录、评分 rubric。

每个资源条目字段：

- 标题
- 类型
- 来源路径
- 对应周次
- 适合用途
- 是否已课程化

### 5.6 AI 协作规范 `/ai-collaboration`

目标：让学生知道何时能用 AI、如何记录、如何核验。

内容模块：

- AI 在本课程中的角色。
- 允许使用场景：概念解释、报错解释、代码片段、图注润色、流程复核。
- 不允许或需强约束场景：替代判断、编造结果、伪造文献、直接生成作业结论。
- 分周 AI 使用边界：
  - Week 1-2：解释概念和报错。
  - Week 3-6：局部代码和调试。
  - Week 7-11：图形脚本优化和图注润色。
  - Week 12-16：流程梳理、参数记录、结果解释边界。
  - Week 17-18：项目报告修改、核验记录和反思。
- AI 协作记录模板。
- 输出核验清单。
- 校训映射：博学、审问、慎思、明辨、笃行。

## 6. Coursebook 结构

Coursebook 是长期内容层，不等同于每周讲稿。建议结构：

```text
coursebook/
├── index.md
├── foundations/
│   ├── medical-data-types.md
│   ├── reproducible-analysis.md
│   └── ai-collaboration-boundaries.md
├── programming/
│   ├── python-basics-for-medical-data.md
│   ├── r-data-frame-and-ggplot2.md
│   └── bash-and-pipeline-intuition.md
├── statistics/
│   ├── descriptive-statistics.md
│   ├── inference.md
│   ├── correlation-regression.md
│   └── logistic-regression.md
├── visualization/
│   ├── distribution-plots.md
│   ├── sci-figure-standards.md
│   └── figure-caption-writing.md
├── omics/
│   ├── high-dimensional-data.md
│   ├── rnaseq-workflow.md
│   ├── differential-expression.md
│   └── single-cell-visualization.md
└── cases/
    ├── python-cleaning-case.md
    ├── r-volcano-plot-case.md
    ├── heatmap-case.md
    └── ai-audit-case.md
```

内容生成原则：

- 先从课程周次页面链接到 Coursebook 章节。
- Coursebook 章节可比课堂更完整，但必须保留“课堂对应周次”标识。
- 编程案例优先小而可运行，服务药学本科生理解。
- AI 生成内容必须标注人工核验状态。

## 7. 内容数据模型

建议实现时建立独立 `site/` 目录，不直接改写 `course/` 和 `knowledge/`。

```text
site/
├── src/
│   ├── content/
│   │   ├── weeks/
│   │   ├── resources/
│   │   ├── coursebook/
│   │   └── pages/
│   ├── components/
│   ├── layouts/
│   ├── styles/
│   └── data/
├── public/
│   └── assets/
│       └── sysu/
├── scripts/
│   ├── ingest-weeks.mjs
│   ├── ingest-resources.mjs
│   └── validate-content.mjs
└── package.json
```

核心 collection：

- `weeks`：18 周页面。
- `resources`：资源索引条目。
- `coursebook`：扩展教材章节。
- `aiRules`：AI 协作规范和 prompt 模板。

周次 frontmatter 示例：

```yaml
week: 1
title: 课程导论与医药数据特征
phase: AI 边界、流程与复现
tags: [医药数据, AI协作, 课程导论]
source:
  outline: course/weeks/week_01/outline.md
  script: course/weeks/week_01/script.md
  materials: course/weeks/week_01/materials.md
ai_boundary: 概念解释与边界讨论
coursebook:
  - foundations/medical-data-types
  - foundations/ai-collaboration-boundaries
```

## 8. 技术路线建议

### 8.1 推荐路线：Astro + MDX + Pagefind

理由：

- 适合课程网站、文档、长文章和静态部署。
- Markdown/MDX 内容模型清晰，能从 `course/` 和 `knowledge/` 派生内容。
- 可做漂亮的自定义首页和周次页面，不被传统 docs 主题限制。
- Pagefind 支持静态全文搜索。
- React/Vue 组件可按需作为交互岛使用，不增加整体复杂度。

适用 MVP：

- 首页
- 课程大纲
- 18 周页面
- 资源索引
- AI 协作规范
- Coursebook 入口与少量样例章节

### 8.2 备选路线：VitePress

优点：

- 启动最快，Markdown 文档体验成熟。
- 适合快速做 Coursebook。

不足：

- 首页和 SYSU Beamer blue 学术门户风格定制空间较小。
- 18 周课程卡片和资源索引需要较多主题改造。

### 8.3 备选路线：Next.js

优点：

- 与参考站点技术形态相近。
- 后续如果要接作业平台、登录、动态数据更方便。

不足：

- 对当前静态课程门户偏重。
- 内容 ingestion、静态搜索和部署复杂度更高。

### 8.4 建议决策

当前最稳 MVP 选择 **Astro + MDX + Pagefind**。

实施时先做静态站，不做登录、作业提交和后端。后续如果需要教学平台，再独立评估 Next.js 或后端服务。

## 9. 实施计划

### Phase 0：确认技术路线与资产许可

需要用户确认：

- 采用 Astro + MDX + Pagefind，还是 VitePress / Next.js。
- 是否允许把 `codex_ppt_skill` 中筛选后的 SYSU 资产复制到 `site/public/assets/sysu/`。
- 是否需要首期包含 `/coursebook` 页面，还是只在首页和资源索引中预留入口。

### Phase 1：脚手架与设计系统

- 新建 `site/`。
- 建立 Astro 项目、基础布局、全局样式。
- 写入 SYSU Blue design tokens。
- 建立顶部栏、页脚、页面标题、周次卡片、资源条目组件。

### Phase 2：内容导入

- 从 `course/weeks/week_xx` 生成 18 个周次页面。
- 从 `knowledge/index.md` 和现有 source/entity/concept 页生成资源索引初稿。
- 写 `/syllabus` 和 `/ai-collaboration` 初版。
- 建立 Coursebook 入口页和 2-3 个样例章节。

### Phase 3：首页与导航

- 完成首页首屏、三阶段课程路径、快速入口和当前周模块。
- 完成 `/weeks` 总览和周次详情页互链。
- 完成资源索引筛选结构。

### Phase 4：搜索与质量检查

- 接入 Pagefind。
- 运行构建检查。
- 检查断链、缺失 frontmatter、空页面。
- 浏览器查看桌面和移动端布局。
- 校验图片尺寸、颜色对比度和文本不溢出。

## 10. 验收标准

MVP 完成时应满足：

- `site/` 可独立安装依赖、构建和本地预览。
- 首页、课程大纲、18 周页面、资源索引、AI 协作规范可访问。
- 每个周次页面至少包含标题、学习目标、课堂提纲、AI 协作边界、材料入口。
- 资源索引能按类型和周次组织现有资源。
- 视觉上符合 SYSU blue academic / Beamer-inspired 风格。
- 校徽、字标、校区照片使用路径和来源有记录。
- 不改写 `materials/raw/`。
- 不把项目本地 skills 写回全局。

## 11. 风险与处理

| 风险 | 处理 |
|---|---|
| 课程讲稿内容较长，直接塞入周次页会过重 | 周次页展示摘要和结构，完整讲稿作为折叠区或链接 |
| Coursebook 内容来源多，质量参差 | 每章标注来源、核验状态和对应周次 |
| AI 生成案例可能不可靠 | 所有案例进入 `verified / needs-review` 状态 |
| SYSU 资产版权或公开使用边界需确认 | 首期只在本地开发使用，发布前再次确认 |
| Beamer 风格网页化后可能像 PPT 截图 | 保留色彩和结构，不保留幻灯片边框和投影式排版 |

## 12. 当前待确认事项

1. 技术路线是否采用推荐的 **Astro + MDX + Pagefind**。
2. MVP 是否包含 `/coursebook` 的入口页和样例章节。
3. 是否允许在实施阶段复制经过筛选的 SYSU logo、wordmark、campus photo 到 `site/public/assets/sysu/`。
4. 首页是否显示“中山大学”完整字标，还是只在页脚/关于区显示，避免与课程归属表述冲突。

