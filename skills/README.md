# AI_Course 项目本地 Skills

本目录包含 **32 个** Codex/Claude 风格技能目录。它们只服务本项目，不自动写回全局 `$CODEX_HOME/skills`。全局技能加载记录见 [Skill Loading Manifest](../docs/skill_loading_manifest_2026-06-03.md)。

## 使用原则

- 先用 `course-skill-router` 判断任务类型，再调用具体项目 workflow。
- `course/` 是课件生产主线；`knowledge/` 是素材和方法支持层。
- 外部全局 skills 只提供通用能力，课程写入位置和质量门禁由本目录的 `course-*` skills 决定。
- 生成 PPTX 前先产出 storyboard/brief；生成讲义前先读周次三件套和讲义深度标准。
- AI 不替代医学、统计、生物学和来源核验。

## Courseware Workflow（5 个）

| Skill | 用途 |
|---|---|
| `course-skill-router` | 统一路由讲义扩写、PPT、证据审查、素材入库和维护任务。 |
| `course-lecture-expand` | 将 `course/weeks/week_XX/script.md` 从 placeholder/scaffold 扩写到 `pilot-script`。 |
| `course-ppt-storyboard` | 先生成可审查 slide storyboard/brief，再进入 PPTX。 |
| `course-evidence-review` | 审查统计、生物学、图形和 AI 输出的 claim-evidence 边界。 |
| `course-update-vault` | 维护索引、断链、周次映射、讲义深度和技能清单。 |

## Academic Research（6 个）

| Skill | 用途 |
|---|---|
| `academic-paper-search` | 跨数据库论文检索、元数据和开放全文线索。 |
| `arxiv` | arXiv 预印本搜索与摘要/PDF 链接获取。 |
| `lecture-writing` | 通用讲义写作流程；本项目优先由 `course-lecture-expand` 包装使用。 |
| `literature-survey-generator` | 文献综述自动化流水线，按需用于外部素材调研。 |
| `nber-working-papers-api` | NBER 工作论文和数据集 API；本课程很少触发。 |
| `unpaywall-api` | DOI 到合法开放全文版本检索。 |

## Documents And Slides（9 个）

| Skill | 用途 |
|---|---|
| `docx` | Word 文档读取、创建和编辑。 |
| `markitdown` | PDF/DOCX/PPTX/XLSX 等转 Markdown。 |
| `md-to-docx` | Markdown 转 DOCX。 |
| `pdf` | PDF 读取、抽取、合并、拆分和 OCR 相关任务。 |
| `pptx` | PPTX 读取、编辑、创建和可视化检查。 |
| `xlsx` | Excel/CSV/TSV 读取、编辑和检查。 |
| `marp-slides-creator` | 通用 Marp slide 生成。 |
| `marp-slides-lingnan` | 岭南学院风格 Marp slide 生成。 |
| `marp-export` | Marp 导出 PDF/HTML/PPTX/PNG。 |

## Web, Agents, And Dev Tools（8 个）

| Skill | 用途 |
|---|---|
| `agent-browser` | 浏览器自动化。 |
| `web-access` | 真实浏览器联网读取入口。 |
| `web-research` | 多源网络研究和带引用报告。 |
| `do-agent` | 多代理任务执行框架。 |
| `skill-creator` | 创建和评估 skill。 |
| `command-development` | 命令开发辅助。 |
| `frontend-design` | 前端界面设计。 |
| `md2website` | Markdown 打包为网站。 |

## Writing And UI Helpers（4 个）

| Skill | 用途 |
|---|---|
| `fix-chinese` | 中文表达和排版修正。 |
| `chinese-quote-converter` | 中文引号转换。 |
| `five-questions` | 经验研究问题拆解。 |
| `ui-ux-pro-max` | UI/UX 设计参考。 |

## 维护命令

```powershell
python scripts/maintenance/course_skill_inventory.py --check
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py
python -m pytest -q
```
