---
type: synthesis
title: MinerU PDF 结构化转换方案
status: in_progress
related_sources: [PDF_Library, MinerU-Ecosystem]
tags: [mineru, pdf, markdown, course-ops, api]
---

# MinerU PDF 结构化转换方案

## 定位

本页记录 `materials/` 下 PDF 的结构化转换路线：使用 MinerU 云端 Precision API 生成更适合信息抽取的 Markdown / JSON。当前 source 页已改用 `materials/markdown/pdf_library_mineru/`，旧的轻量转换结果已退役并移除。

本项目明确不再保留本地 MinerU CLI 管线，也不维护 `.venv-mineru`。参考书 PDF 可以上传到 MinerU 云端解析；API token 只通过环境变量传入，不写入仓库。

## 为什么改为 API-only

- 本地 MinerU CLI 在 Windows 下会引入体积很大的 Python 环境、模型缓存与中间输出，不适合作为本课程知识库的长期依赖。
- MinerU Precision API 支持 token 鉴权、批量本地文件签名上传、`page_ranges`、表格/公式识别和多格式输出，足以覆盖参考书 PDF 的结构化转换需求。
- `scripts/convert/mineru_pdf_pipeline.py` 只保留 API 工作流：生成清单、提交任务、轮询结果、下载 zip、提升 Markdown。它不再调用本地 `mineru` 命令。
- 当前官方文档写明 Precision API 的文件大小上限为 200 MB、文件页数上限为 200 页；脚本先按每 200 页生成 `page_ranges` 任务。若实测发现服务端按“整份 PDF 页数”而不是“选中页数”拦截，则再增加临时 PDF 分片上传 fallback。

## 目录边界

```text
materials/raw/pdf_originals/                    # 原始 PDF，只读，不入 git
materials/raw/external_ppt/                     # 外部参考课件 PDF，例如嵩天 Python PPT
materials/markdown/pdf_library_mineru/        # MinerU API 生成层
  INDEX.md                        # PDF 清单与 API 入口
  manifest.json                   # 机器可读 PDF 清单
  api_parts.json                  # API 任务清单：page_ranges，不含 token
  api_submissions.json            # API batch_id 记录，不含 token
  api_results.json                # API 查询结果记录，不含 token
  api_zips/                       # 下载的 MinerU zip，git 忽略
  api_raw/                        # zip 解压目录，git 忽略
  <book-slug>/
    book.part_001.mineru.md       # 单个 page range 提升出的 Markdown
    book.mineru.md                # 合并后的主 Markdown，供 wiki ingest
    book.course.md                # 面向备课的课程化 Markdown
    structure_report.md           # 结构质量报告
scripts/convert/mineru_pdf_pipeline.py     # MinerU API-only 入口
```

## 标准命令

```powershell
$env:MINERU_API_TOKEN = "<token>"

python scripts/convert/mineru_pdf_pipeline.py inventory
python scripts/convert/mineru_pdf_pipeline.py prepare-parts
python scripts/convert/mineru_pdf_pipeline.py api-submit --model-version vlm
python scripts/convert/mineru_pdf_pipeline.py api-poll --wait --download
python scripts/convert/mineru_pdf_pipeline.py api-promote
```

先做单本书或少量页验证：

```powershell
python scripts/convert/mineru_pdf_pipeline.py prepare-parts --only Learn_AI --max-pages 20
python scripts/convert/mineru_pdf_pipeline.py api-submit --only Learn_AI --limit 1 --model-version vlm
python scripts/convert/mineru_pdf_pipeline.py api-poll --wait --download
python scripts/convert/mineru_pdf_pipeline.py api-promote
```

> [!important] token 安全
> 用户在 chat 中贴出的旧 token 应视为已暴露。后续应在 MinerU 控制台重新生成 token，并只在本机 PowerShell 环境变量中设置；不要写入 README、脚本、JSON 或 wiki。

## API 约束记录（2026-05-24 复核）

- Precision API 需要 `Authorization: Bearer <token>`。
- 本地文件批量上传接口是 `POST https://mineru.net/api/v4/file-urls/batch`，返回 `batch_id` 与签名上传 URL；客户端随后用 `PUT` 上传文件。
- 结果查询接口是 `GET https://mineru.net/api/v4/extract-results/batch/{batch_id}`。
- Precision API 支持 `pipeline`、`vlm`、`MinerU-HTML` 三种 `model_version`；非 HTML 参考书优先用 `vlm`。
- 官方文档的模式对比表写“批量支持≤200 个”，但本地文件批量上传接口详细说明写“单次申请链接不能超过 50 个”。实际脚本按更保守的 50 个限制处理。
- 官方文档给出的 Precision API 限制包括文件大小不超过 200 MB、页数不超过 200 页；当前脚本默认 `--max-pages 200`。
- `vlm` 模型下 `enable_formula` 对行内公式解析有明确影响；因此课程参考书默认保持 `--enable-formula true --enable-table true`。
- Agent 轻量解析 API 不适合本项目批量转换：它免 token，但限制约为 10 MB / 20 页，且只返回 Markdown 链接；本项目 PDF 全部超过 20 页。

## 当前 PDF 清单与任务拆分

| PDF | 页数 | 大小 | 建议任务数（200 页/任务） | 用途 |
|---|---:|---:|---:|---|
| ISLP Python | 613 | 19.12 MB | 4 | Python 统计学习案例 |
| ISLR R | 436 | 10.35 MB | 3 | R 统计学习案例 |
| Starting Data Analytics with GenAI | 362 | 15.49 MB | 2 | GenAI 数据分析工作流 |
| Learn AI-Assisted Python Programming | 298 | 8.83 MB | 2 | Copilot / ChatGPT 编程教学 |
| 嵩天 Python PPT | 1287 | 32.90 MB | 7 | 中文 Python 教学表达和课堂节奏 |

全部文件大小低于 200 MB；主要风险是页数超过 200 后，服务端是否允许对同一大 PDF 通过 `page_ranges` 分段解析。建议先用 `--only Learn_AI --max-pages 20 --limit 1` 做烟测，再测试一个超过 200 页原 PDF 的第二段任务。

## 实际运行记录

### 2026-05-24 全量转换

- 先用 `Learn_AI --max-pages 20 --limit 1` 完成烟测，确认提交、轮询、下载、提升 Markdown 流程可用。
- 烟测暴露上传实现问题：`urllib.request` 会自动带 `Content-Type: application/x-www-form-urlencoded`，导致 OSS 签名 URL 返回 `SignatureDoesNotMatch`。已改为 `http.client` 直接 PUT，仅发送 `Content-Length`。
- 全量按 200 页分段提交 18 个任务，全部完成，状态均为 `done`。
- 已生成 5 个合并版 `book.mineru.md`：
  - `An_Introduction_to_Statistical_Learning_with_Applications_Python/book.mineru.md`
  - `An_Introduction_to_Statistical_Learning_with_Applications_R/book.mineru.md`
  - `Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/book.mineru.md`
  - `R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro/book.mineru.md`
  - `Pythonppt/book.mineru.md`
- 初步质量观察：章节标题、图片、部分流程图和代码结构可被保留；个别复杂流程图会生成噪声较重的 Mermaid 或 OCR 文本，后续应在 `book.course.md` 阶段人工/AI 清理。

### 2026-05-24 课程化 Markdown 与 AIDD 讲义索引

- 新增 `scripts/courseware/mineru_course_markdown.py`，从 5 个 `book.mineru.md` 生成面向备课的 `book.course.md` 与 `structure_report.md`。
- PDF 课程化输出保留章节层级索引、推荐周次、教学卡片、公式/代码/图表/表格线索和结构警告；不改写 `book.mineru.md`。
- AIDD txt 讲义同步纳入素材层：从 `materials/markdown/aidd_bioinformatics/` 的 71 个 txt 生成 `aidd.course_index.md`、`aidd.structure_report.md` 和 11 个章节目录下的 `chapter.course.md`。
- 后续写 PPT 大纲时应同时查看：PDF 侧 `<book-slug>/book.course.md` 与 AIDD 侧 `aidd.course_index.md` / `chapter.course.md`，再把确认可用的素材写入对应 `course/weeks/week_xx/materials.md`。

## 课程化 Markdown 目标

MinerU 的 `full.md` 是“解析 Markdown”，还不是课程备课 Markdown。为服务 PPT 大纲和讲稿，需要在 `api-promote` 后增加二次整理：

- `book.mineru.md`：保留 MinerU 原始标题、公式、表格和图片引用，不手工改写。
- `book.course.md`：面向课程的整理版，保留章节层级，抽取重点、公式、例子、代码块和可进入哪一周。
- `structure_report.md`：质量报告，记录标题层级是否错乱、公式是否变成图片/乱码、例子和代码是否可定位。

建议 `book.course.md` 的章节模板：

```markdown
## Chapter N. 标题

### 章节定位

### 可进入课程的位置

### 核心重点

### 公式与符号

### 例子 / 代码 / 图表

### 备课摘取建议
```

## 质量检查

每本书转换后至少检查：

- 是否生成 `<book-slug>/book.mineru.md`。
- 目录、章标题和小节标题是否比旧版 Markdown 更稳定。
- 表格是否保留为 Markdown / HTML，而不是被打散成无序文本。
- 公式是否以 LaTeX 或可读文本保留。
- 页眉、页脚、页码是否明显减少。
- Python / R / shell 代码块是否仍可识别。

## 后续进入 knowledge / course 的方式

MinerU 产物不直接等同于知识页或讲稿。它仍属于 `materials/markdown/` 生成层。后续 ingest 时，应从 `book.course.md` 抽取可进入课程的章节、案例、提示词和代码片段，再更新：

- [ISLP](../sources/ISLP.md)
- [ISLR](../sources/ISLR.md)
- [Starting_Data_Analytics_GenAI](../sources/Starting_Data_Analytics_GenAI.md)
- [Learn_AI_Assisted_Python_Programming](../sources/Learn_AI_Assisted_Python_Programming.md)
- [三本 Python 书定位对比](三本Python书定位对比.md)
- [知识缺口与后续素材](知识缺口与后续素材.md)
