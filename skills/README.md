# 🛠️ Skills 技能库

本目录包含 **23 个 Claude Code 自定义技能**，覆盖学术研究、文档处理、演示制作、前端设计、文本处理和 AI 代理等场景。每个技能均可通过对应的斜杠命令（`/command`）在 Claude Code 中调用。

---

## 📚 学术研究（6 个）

### 1. Academic Paper Search `/academic-paper-search`

统一的学术论文搜索工具，支持跨 arXiv、NBER、SSRN、CrossRef、OpenAlex、Unpaywall、Semantic Scholar 等多个数据源检索论文、获取元数据和下载 PDF。覆盖经济学、金融学、社会科学、计算机科学等所有学科领域。

### 2. arXiv Research `/arxiv`

通过 arXiv 免费 REST API 搜索和获取学术预印本论文，无需 API 密钥。支持按关键词、作者、分类或论文 ID 检索，可直接获取摘要和全文 PDF 链接。

### 3. Lecture Writing `/lecture-writing`

经济学讲义写作技能，协调三个专业 Agent（内容分析、讲义撰写、讲义审阅）完成从课堂录音转写到完整讲义的全流程。强调录音线索保真、议论文体裁格式和 Human-in-the-Loop 原则。

### 4. Literature Survey Generator `/literature-survey-generator`

多代理自动化文献综述生成流水线。从学术数据库（OpenAlex、CrossRef、Unpaywall）搜索论文、下载 PDF、构建 BibTeX、撰写 LaTeX 综述、编译、质量审阅到修订，全流程自动完成。针对经济学期刊优化。

### 5. NBER Working Papers API `/nber-working-papers-api`

访问 NBER（美国国家经济研究局）工作论文和经济研究数据集的 API 工具。支持按关键词搜索、按项目筛选、获取最新论文，以及访问 NBER 宏观经济数据集（商业周期日期、制造业指数等）。

### 6. Unpaywall API `/unpaywall-api`

通过 Unpaywall 免费开放数据库查找学术文章的合法免费全文版本。支持按 DOI 查询开放获取状态，索引超过 4000 万篇免费学术文章，涵盖金色、绿色、混合、铜色等 OA 类型。

---

## 📄 文档处理（5 个）

### 7. DOCX Document Processor `/docx`

Word 文档（.docx）的创建、阅读、编辑和操作工具。支持表格目录、页眉页脚、图片插入、查找替换、修订标记等功能，可通过 pandoc 或直接操作 XML 实现文档处理。

### 8. MarkItDown `/markitdown`

多格式文档转 Markdown 工具，支持 20 多种文件格式（PDF、DOCX、XLSX、PPTX、HTML、EPUB、CSV、JSON、图片 OCR、音频转写等），输出针对大语言模型处理优化的结构化 Markdown 文本。

### 9. Markdown to DOCX Converter `/md-to-docx`

通过 pandoc 将 Markdown 文件转换为格式规范的 Word 文档。默认使用仿宋字体、黑色字体、1.5 倍行距、24pt 首行缩进，支持引用数字自动转上标，适合中文公文和学术文档格式要求。

### 10. PDF Processor `/pdf`

PDF 文件全方位处理工具。支持读取/提取文本和表格、合并/拆分 PDF、旋转页面、添加水印、创建新 PDF、填写表单、加密/解密、提取图片以及扫描件 OCR 识别等操作。

### 11. XLSX Spreadsheet Processor `/xlsx`

Excel 电子表格（.xlsx/.xlsm/.csv/.tsv）的创建、阅读、编辑和修复工具。支持添加列、公式计算、格式设置、图表制作、数据清洗等操作，遵循行业标准的颜色编码和数字格式规范，确保零公式错误输出。

---

## 🎞️ 演示制作（4 个）

### 12. Marp Slides Creator `/marp-slides-creator`

专业 Marp 演示文稿制作助手，提供七阶段完整工作流：工作空间初始化、内容分析、Slides 制作、多维度审阅、中文语言规范审阅、PNG 转换检查、终稿确定。内置 14 款精选主题，涵盖学术、商务、创意等场景。

### 13. Marp Slides Lingnan `/marp-slides-lingnan`

🏫 **中山大学岭南学院专用**。内置岭院官方 PPT 模板风格（深红色 `#AC1B20` 配色、院徽页脚、AACSB 认证标志），提供七阶段系统化制作流程，支持 16:9 和 4:3 两种宽高比。

### 14. Marp Export `/marp-export`

将 Marp Markdown 演示文稿导出为 PDF（默认）、HTML、PPTX 或 PNG 格式。自动处理主题加载、Chrome/Chromium 检测和批量转换。

### 15. PPTX Processor `/pptx`

PowerPoint（.pptx）文件的创建、阅读、编辑和操作工具。支持从零创建演示文稿、读取解析现有文件、基于模板编辑修改、合并拆分幻灯片文件，以及处理布局、讲者备注和批注等。

---

## 🌐 前端设计（1 个）

### 16. Frontend Design `/frontend-design`

创建独特的、生产级前端界面，追求高设计品质。支持网站、着陆页、仪表盘、React 组件、HTML/CSS 布局等，强调创意排版、配色、动效和空间构图，避免千篇一律的 AI 风格设计。

---

## ✏️ 文本处理（2 个）

### 17. Chinese Quote Converter `/chinese-quote-converter`

将英文直引号（`"..."`）转换为中文弯引号（`"..."`），支持保留代码块内容不被转换、正确处理嵌套引号。适用于中文文档、Markdown 文件等需要规范中文排版的场景。

### 18. Fix Chinese Writing `/fix-chinese`

🔄 **主动式技能**——写作或编辑中文文本时自动激活。消除 AI 翻译腔和生硬表达，执行中英文混排格式规范（间距、标点、加粗格式），使中文文本更自然流畅，符合母语者写作习惯。

---

## 🔧 开发工具（3 个）

### 19. Agent Browser `/agent-browser`

面向 AI 代理的浏览器自动化命令行工具。支持导航网页、填写表单、点击按钮、截图、提取数据、测试 Web 应用等浏览器交互任务，通过 `agent-browser` CLI 实现程序化的网页操作。

### 20. Skill Creator `/skill-creator`

Claude Code 技能开发工具，支持从零创建新技能、修改优化现有技能、运行评估测试、进行方差分析基准测试，以及优化技能描述以提高触发准确率。提供完整的迭代式技能开发工作流。

### 21. Web Access `/web-access`

所有联网操作的统一入口技能，通过 Chrome CDP 协议实现真实浏览器环境操作。支持网页搜索、内容抓取、登录后操作、动态渲染页面读取、社交媒体内容获取等需要真实浏览器环境的网络任务。

---

## 🤖 AI 代理（2 个）

### 22. Multi-Agent Task Executor `/do-agent`

多代理多阶段复杂任务执行框架。采用 explore → think → plan → track → execute → review → revise 工作流，支持最多 10 个子代理并行执行，自动完成从规划到实施、审阅、修订的全流程，无需人工干预。

### 23. Web Research `/web-research`

多源网络研究技能，通过委派子代理搜索多个网络来源、综合发现并生成带引用的研究报告。适用于在线调研、信息查找、方案比较或生成研究报告等需求。

---

## 📊 汇总

| 类别 | 数量 | 技能 |
|:-----|:----:|:-----|
| 📚 学术研究 | 6 | academic-paper-search, arxiv, lecture-writing, literature-survey-generator, nber-working-papers-api, unpaywall-api |
| 📄 文档处理 | 5 | docx, markitdown, md-to-docx, pdf, xlsx |
| 🎞️ 演示制作 | 4 | marp-slides-creator, marp-slides-lingnan, marp-export, pptx |
| 🌐 前端设计 | 1 | frontend-design |
| ✏️ 文本处理 | 2 | chinese-quote-converter, fix-chinese |
| 🔧 开发工具 | 3 | agent-browser, skill-creator, web-access |
| 🤖 AI 代理 | 2 | do-agent, web-research |
