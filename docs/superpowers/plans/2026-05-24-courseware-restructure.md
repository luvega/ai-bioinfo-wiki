# AI_Course Courseware Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Reorganize `F:\AI_Course` into a courseware-first workspace centered on the 36-hour syllabus and PPT/script production.

**Architecture:** Move source material into `materials/`, teaching source files into `course/`, and the former `knowledge/` into `knowledge/`. Keep root-level `AGENTS.md`, `memory.md`, and `README.md` as project collaboration metadata. Update links, scripts, ignore rules, and stale week mappings after moves.

**Tech Stack:** PowerShell, Git, Python standard library, Markdown.

---

### Task 1: Create New Directory Skeleton

**Files:**
- Create directories under `materials/`, `course/`, `scripts/convert/`, `scripts/audit/`, `scripts/courseware/`, and `outputs/`.

- [x] **Step 1: Create directories**

Run:

```powershell
$dirs = @(
  'materials/raw/pdf_originals',
  'materials/raw/aidd_bioinformatics',
  'materials/raw/external_ppt',
  'materials/markdown/pdf_library_legacy',
  'materials/markdown/pdf_library_mineru',
  'materials/markdown/aidd_bioinformatics',
  'materials/manifests',
  'course/syllabus',
  'course/weeks',
  'course/templates',
  'course/assessments',
  'scripts/convert',
  'scripts/audit',
  'scripts/courseware',
  'outputs/pptx',
  'outputs/scripts',
  'outputs/handouts'
)
foreach ($dir in $dirs) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
```

Expected: all directories exist.

### Task 2: Move Existing Files Into New Layers

**Files:**
- Move: `doc/*` -> `course/syllabus/`
- Move: `wiki/` -> `knowledge/`
- Move: `raw/AIDD_Bioinformatics/` -> `materials/raw/aidd_bioinformatics/`
- Move: `sources/PDF_Library/` -> `materials/markdown/pdf_library_legacy/`
- Move: `sources/PDF_Library_MinerU/` -> `materials/markdown/pdf_library_mineru/`
- Move: `sources/AIDD_Bioinformatics/` -> `materials/markdown/aidd_bioinformatics/`
- Move: `pdf_originals/*` -> `materials/raw/pdf_originals/`
- Move: `嵩天Python/` -> `materials/raw/external_ppt/嵩天Python/`
- Move: scripts into `scripts/convert/`

- [x] **Step 1: Move with root-boundary safety checks**

Run a PowerShell move script that resolves every source and target under `F:\AI_Course` before moving.

Expected: root contains `materials/`, `course/`, `knowledge/`, `scripts/`, `outputs/`, and no old `doc/`, `raw/`, `sources/`, `pdf_originals/`, `wiki/`, or `嵩天Python/` directories unless left empty and removed.

### Task 3: Create Week Courseware Skeletons

**Files:**
- Create: `course/weeks/week_01/outline.md`, `script.md`, `materials.md` through `week_18`

- [x] **Step 1: Generate 18 week folders**

Use the syllabus week titles from the current docx/lecture notes:

1. 课程导论与医药数据特征
2. 数据分析流程、复现规范与人机协作规范
3. AI 辅助编程与 Python 快速入门
4. R 基础语法、数据框操作与 AI 代码核验
5. 数据读取与整形
6. 缺失值、异常值处理与分组汇总
7. 描述统计与分布可视化
8. 统计推断基础
9. 相关分析与线性回归
10. 分类问题与逻辑回归
11. 科研图表规范与 SCI 图表表达
12. 高维数据与数学直觉
13. PCA、聚类与热图
14. 转录组数据分析基础
15. 差异表达分析与功能解读
16. 单细胞转录组可视化
17. 综合项目工作坊：AI 协作分析与结果核验
18. 综合项目汇报与课程总结

Expected: each week has `outline.md`, `script.md`, and `materials.md` with front matter and links back to `course/syllabus/`.

### Task 4: Update Script Paths and Script Locations

**Files:**
- Move/update: `scripts/convert/clean_aidd_subtitles.py` -> `scripts/convert/clean_aidd_subtitles.py`
- Move/update: `scripts/convert/pdf_to_markdown.py` -> `scripts/convert/pdf_to_markdown.py`
- Move/update: `scripts/convert/mineru_pdf_pipeline.py` -> `scripts/convert/mineru_pdf_pipeline.py`

- [x] **Step 1: Replace hard-coded drive paths**

Update scripts to compute:

```python
ROOT = Path(__file__).resolve().parents[2]
```

Use:

```python
OUTPUT_ROOT = ROOT / "materials" / "raw" / "aidd_bioinformatics"
INPUT_DIR = ROOT / "materials" / "raw" / "pdf_originals"
OUT_ROOT = ROOT / "materials" / "markdown" / "pdf_library_mineru"
```

Expected: no active script references to `E:/AI_Course` or `llm_wiki_kb`.

### Task 5: Update Markdown Links and Stale Week Mappings

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `memory.md`
- Modify: `knowledge/**/*.md`

- [x] **Step 1: Mechanically rewrite moved paths**

Replace:

```text
wiki/ -> knowledge/
doc/ -> course/syllabus/
raw/AIDD_Bioinformatics/ -> materials/raw/aidd_bioinformatics/
sources/AIDD_Bioinformatics/ -> materials/markdown/aidd_bioinformatics/
sources/PDF_Library/ -> materials/markdown/pdf_library_legacy/
sources/PDF_Library_MinerU/ -> materials/markdown/pdf_library_mineru/
pdf_originals/ -> materials/raw/pdf_originals/
scripts/mineru_pdf_pipeline.py -> scripts/convert/mineru_pdf_pipeline.py
scripts/clean_aidd_subtitles.py -> scripts/convert/clean_aidd_subtitles.py
scripts/pdf_to_markdown.py -> scripts/convert/pdf_to_markdown.py
```

Expected: repository docs point at the new paths.

- [x] **Step 2: Correct course-week claims**

Update current course-position text so:

```text
Week 11 = 科研图表规范与 SCI 图表表达
Week 14 = 转录组数据分析基础
Week 15 = 差异表达分析与功能解读
Week 16 = 单细胞转录组可视化
```

Expected: no current knowledge page claims DESeq2/enrichment is Week 11 except historical log or decision records clearly marked stale.

### Task 6: Update Ignore Rules and Obsidian Filters

**Files:**
- Modify: `.gitignore`
- Modify: `.obsidian/app.json`

- [x] **Step 1: Update ignored paths**

Use new paths:

```text
materials/raw/pdf_originals/
materials/markdown/pdf_library_mineru/api_upload_parts/
materials/markdown/pdf_library_mineru/api_zips/
materials/markdown/pdf_library_mineru/api_raw/
materials/markdown/pdf_library_mineru/_smoke/
materials/markdown/pdf_library_mineru/**/images/
materials/markdown/pdf_library_mineru/**/*.zip
outputs/
```

Expected: raw PDFs and heavy generated caches stay untracked.

- [x] **Step 2: Update Obsidian ignore filters**

Use new material paths in `.obsidian/app.json`.

Expected: Obsidian ignores heavy material directories but can browse `knowledge/` and `course/`.

### Task 7: Verify

**Files:**
- All moved and edited files.

- [x] **Step 1: Compile scripts**

Run:

```powershell
python -m py_compile scripts/convert/clean_aidd_subtitles.py scripts/convert/pdf_to_markdown.py scripts/convert/mineru_pdf_pipeline.py
```

Expected: exit code 0.

- [x] **Step 2: Check stale paths**

Run:

```powershell
rg -n "E:/AI_Course|E:\\AI_Course|e:\\AI_Course|llm_wiki_kb" . -g "*.md" -g "*.py" -g "!materials/markdown/pdf_library_legacy/*.md"
```

Expected: no active script paths; historical memory entries are allowed only if clearly historical.

- [x] **Step 3: Check Week 11 stale claims**

Run:

```powershell
rg -n "第 11 周.*DESeq2|Week 11.*DESeq2|第 11 周.*富集|Week 11.*enrichment" README.md AGENTS.md memory.md knowledge course -g "*.md"
```

Expected: no current course-position claims remain; historical logs may mention old decisions only if marked stale.

- [x] **Step 4: Check status**

Run:

```powershell
git status --short
```

Expected: moved files and intentional edits only; no raw PDF tracked status unless already ignored.
