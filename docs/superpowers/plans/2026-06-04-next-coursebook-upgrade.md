# Next Coursebook Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将本轮总纲升级转化为下一轮可交付内容：优先补强 Week 11-13 与 Week 17-18，并把 Week 13 推进为“现代组学过渡样章”候选，同时启动 Week 14/16 PPT storyboard。

**Architecture:** 继续以 `course/syllabus/` 与 `course/weeks/` 为事实主线，`knowledge/` 和 `materials/markdown/` 只提供来源证据。在线教材只同步目录、状态、样章和来源，不把 18 周都伪装成完整教材正文。

**Tech Stack:** Markdown course files, YAML coursebook map, Astro data modules, Python maintenance scripts, pytest, Astro/Pagefind build.

---

## File Structure

- Modify: `course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md`
  - Responsibility: keep the 18-week syllabus as the highest-priority teaching contract.
- Modify: `course/weeks/week_11/{materials,outline,script}.md`
  - Responsibility: upgrade scientific figures, evidence boundary, and omics figure reading.
- Modify: `course/weeks/week_12/{materials,outline,script}.md`
  - Responsibility: bridge clinical tables to expression matrices, PCA, clustering, heatmap literacy.
- Modify: `course/weeks/week_13/{materials,outline,script}.md`
  - Responsibility: become the next candidate sample chapter for high-dimensional and modern omics transition.
- Modify: `course/weeks/week_17/{materials,outline,script}.md`
  - Responsibility: project workshop with Git/GitHub, source provenance, AI-use statement, and storyboard handoff.
- Modify: `course/weeks/week_18/{materials,outline,script}.md`
  - Responsibility: presentation week rubric, figure-evidence defense, and reproducibility appendix.
- Create: `course/weeks/week_14/ppt_storyboard.md`
  - Responsibility: storyboard for “表达矩阵从哪里来”.
- Create: `course/weeks/week_16/ppt_storyboard.md`
  - Responsibility: storyboard for “单细胞/空间组学图形解读”.
- Modify: `course/textbook/coursebook_map.yml`
  - Responsibility: add Week 13 sample-candidate status and Week 14/16 storyboard status without claiming PPTX completion.
- Modify: `site/src/data/coursebook.ts`
  - Responsibility: expose Week 11-13 and Week 17-18 richer catalog states and optional Week 13 sample route when ready.
- Modify: `scripts/maintenance/course_online_book_check.py`
  - Responsibility: enforce Week 13 transition wording, project-week provenance checks, and PPT status boundaries.
- Test: `tests/test_course_online_book_check.py`
  - Responsibility: cover the new maintenance rules with small fixture checks if the current script is split into testable helpers.
- Update: `docs/course_script_depth_report.md`
  - Responsibility: generated depth report after week script upgrades.

---

### Task 1: Lock Next-Round Syllabus Decisions

**Files:**
- Modify: `course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md`
- Modify: `docs/course_material_week_alignment_2026-06-04.md`

- [ ] **Step 1: Add a next-round decision block to the syllabus**

Add a section named `### 下一轮内容升级边界（2026-06）` near the current material layering section with these decisions:

```markdown
### 下一轮内容升级边界（2026-06）

1. Week 11-13 负责把“科研图表表达、表达矩阵、高维降维”连成一个可教学的过渡段。
2. Week 13 可升级为第五个在线教材样章候选，但只要求学生看懂 PCA/cluster/heatmap/UMAP 的输入输出和不确定性，不要求跑完整单细胞 workflow。
3. Week 17-18 负责项目工作坊和汇报验收，必须显式包含 Git/GitHub 记录、素材溯源、AI 使用声明、PPT storyboard 和图表证据边界。
4. Week 14/16 下一轮只生成 storyboard 与 evidence checklist，不因 `script.md formal_ready` 自动宣称 PPTX 完成。
```

- [ ] **Step 2: Update the material alignment document**

Append a `## 下一轮优先级` section to `docs/course_material_week_alignment_2026-06-04.md`:

```markdown
## 下一轮优先级

| 优先级 | 周次 | 交付物 | 验收点 |
| --- | --- | --- | --- |
| P0 | Week 13 | outline/script + Coursebook 样章候选 | 清楚区分表格矩阵、bulk expression matrix、single-cell matrix 与 spatial matrix |
| P0 | Week 17-18 | 项目工作坊与汇报 rubric | 有 Git/GitHub、素材溯源、AI 使用声明和图表证据边界 |
| P1 | Week 11-12 | 图表证据边界与表达矩阵桥接 | 能承接 Week 13，不默认生信或统计背景 |
| P1 | Week 14/16 | PPT storyboard | 只标记 storyboard/review，不标记 PPTX 完成 |
```

- [ ] **Step 3: Verify no raw paths leaked into course-facing files**

Run:

```powershell
rg -n "materials/raw" course/syllabus course/weeks course/textbook site/src
```

Expected: no output.

---

### Task 2: Upgrade Week 11-13 Teaching Scripts

**Files:**
- Modify: `course/weeks/week_11/materials.md`
- Modify: `course/weeks/week_11/outline.md`
- Modify: `course/weeks/week_11/script.md`
- Modify: `course/weeks/week_12/materials.md`
- Modify: `course/weeks/week_12/outline.md`
- Modify: `course/weeks/week_12/script.md`
- Modify: `course/weeks/week_13/materials.md`
- Modify: `course/weeks/week_13/outline.md`
- Modify: `course/weeks/week_13/script.md`

- [ ] **Step 1: Add Week 11 figure-evidence teaching blocks**

Ensure `week_11/script.md` contains these headings:

```markdown
## 科研图表的四层阅读
## 图表证据边界与 AI 图注改写
## 药学图表课堂任务
## 素材来源与待核验点
```

Required teaching stance:

```markdown
- ggplot2 和组学图形只作为表达工具，不能替代统计判断。
- 微阵列、转录组和单细胞图形用于训练图形阅读，不要求学生完整复现高级流程。
- AI 可以改写图注、检查轴标签和生成待核验清单，不能编造数据来源或机制解释。
```

- [ ] **Step 2: Add Week 12 expression-matrix bridge**

Ensure `week_12/script.md` teaches this sequence:

```markdown
临床表格数据 -> 样本 x 指标矩阵 -> 表达矩阵 -> PCA/cluster/heatmap
```

Add a classroom task:

```markdown
学生用一个 6 samples x 5 genes 的教学矩阵，手工识别行、列、分组变量、缺失值、尺度差异，再解释为什么热图颜色不是原始医学结论。
```

- [ ] **Step 3: Promote Week 13 to sample-candidate depth**

Ensure `week_13/script.md` contains these headings:

```markdown
## 高维数据为什么需要降维
## PCA、聚类和热图的输入输出
## 从 bulk 到 single-cell 的数据结构差异
## 现代组学拓展：SCBP/OSCA/OSTA 只作为图形和流程阅读
## AI 协作边界与待核验点
```

Acceptance wording:

```markdown
Week 13 的目标是看懂高维图形和流程边界，不是训练学生独立完成单细胞或空间组学分析。
```

- [ ] **Step 4: Run depth and quality checks**

Run:

```powershell
$env:PYTHONUTF8='1'
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
```

Expected: both commands exit 0.

---

### Task 3: Upgrade Week 17-18 Project Workshop

**Files:**
- Modify: `course/weeks/week_17/materials.md`
- Modify: `course/weeks/week_17/outline.md`
- Modify: `course/weeks/week_17/script.md`
- Modify: `course/weeks/week_18/materials.md`
- Modify: `course/weeks/week_18/outline.md`
- Modify: `course/weeks/week_18/script.md`

- [ ] **Step 1: Add Week 17 reproducible project workflow**

Required blocks in `week_17/script.md`:

```markdown
## 项目文件夹与 Git/GitHub 记录
## 素材溯源表
## AI 使用声明
## PPT storyboard 交付
## 图表证据边界自查
```

Required student deliverable:

```markdown
每组提交 `README.md`、`data_sources.md`、`ai_use_statement.md`、`ppt_storyboard.md` 和至少一张可解释图表。
```

- [ ] **Step 2: Add Week 18 presentation and defense rubric**

Required rubric in `week_18/script.md`:

```markdown
| 维度 | 通过标准 | 需要修改 |
| --- | --- | --- |
| 数据来源 | 能说明来源、字段、限制和授权边界 | 只写“网上数据”或无来源 |
| 图表表达 | 轴、单位、分组、图注清楚 | 图形漂亮但读不出结论 |
| 证据边界 | 区分观察、统计关联和机制假设 | 把候选结果写成医学事实 |
| AI 使用 | 写明提示词用途和人工核验 | 用 AI 生成结论但不说明 |
| 可复现记录 | 有文件结构、版本和运行记录 | 只有最终 PPT |
```

- [ ] **Step 3: Verify project-week source layering**

Run:

```powershell
rg -n "GitHub|素材溯源|AI 使用声明|storyboard|证据边界" course/weeks/week_17 course/weeks/week_18
```

Expected: each required phrase appears in either outline or script for the relevant week.

---

### Task 4: Add Week 14 and Week 16 PPT Storyboards

**Files:**
- Create: `course/weeks/week_14/ppt_storyboard.md`
- Create: `course/weeks/week_16/ppt_storyboard.md`
- Modify: `course/textbook/coursebook_map.yml`
- Modify: `site/src/data/coursebook.ts`

- [ ] **Step 1: Create Week 14 storyboard**

Create `course/weeks/week_14/ppt_storyboard.md` with this structure:

```markdown
---
week: 14
title: 表达矩阵从哪里来
ppt_status: storyboard
review_status: evidence_review_pending
---

# Week 14 PPT Storyboard

## Slide 1: 本周问题
## Slide 2: 从样本表到表达矩阵
## Slide 3: FASTQ / alignment / count 的概念边界
## Slide 4: count matrix 与 metadata
## Slide 5: QC 和 normalization 为什么需要谨慎
## Slide 6: bulk / single-cell / spatial 的输入差异
## Slide 7: AI 协作边界
## Slide 8: 课堂任务与待核验点
```

- [ ] **Step 2: Create Week 16 storyboard**

Create `course/weeks/week_16/ppt_storyboard.md` with this structure:

```markdown
---
week: 16
title: 单细胞与空间组学图形解读
ppt_status: storyboard
review_status: evidence_review_pending
---

# Week 16 PPT Storyboard

## Slide 1: 图形不是结论
## Slide 2: cell x gene matrix
## Slide 3: QC 图
## Slide 4: PCA / UMAP / t-SNE
## Slide 5: cluster 与 marker gene
## Slide 6: spatial spot / spatial domain
## Slide 7: 参数敏感性
## Slide 8: AI 协作边界与核验清单
```

- [ ] **Step 3: Update Coursebook status without claiming PPTX completion**

In `course/textbook/coursebook_map.yml` and `site/src/data/coursebook.ts`, set:

```yaml
ppt_status: storyboard
review_status: evidence_review_pending
```

for Week 14 and Week 16 if the storyboard exists but PPTX/visual QA has not been run.

- [ ] **Step 4: Verify PPT status boundaries**

Run:

```powershell
$env:PYTHONUTF8='1'
python scripts/maintenance/course_online_book_check.py
```

Expected: exit 0, and no check infers PPT completion from `script.md` status.

---

### Task 5: Sync Coursebook and Optional Week 13 Sample Route

**Files:**
- Modify: `course/textbook/coursebook_map.yml`
- Modify: `site/src/data/coursebook.ts`
- Modify: `site/src/pages/coursebook.astro`
- Modify: `site/src/pages/coursebook/[slug].astro`

- [ ] **Step 1: Add Week 13 sample-candidate metadata**

Add these values to Week 13 in the map and data layer:

```yaml
ppt_status: not_started
review_status: sample_candidate
```

In `site/src/data/coursebook.ts`, add badges:

```ts
badges: ['现代组学拓展', '样章候选']
```

- [ ] **Step 2: Add Week 13 sample content only after Task 2 passes**

If Week 13 script reaches the required sample-candidate depth, add a `sample` object with:

```ts
sample: {
  introQuestion: '为什么同一批表达数据需要 PCA、聚类和热图来辅助理解，而这些图又不能直接证明机制？',
  learningObjectives: [
    '区分样本、变量、基因、细胞和空间 spot 的观测单位。',
    '解释 PCA、聚类和热图分别压缩或重排了什么信息。',
    '说明 AI 可以帮助解释图形语言，但不能替代参数选择、数据来源和统计边界核验。'
  ],
  verificationPoints: [
    '不得把 UMAP/cluster 直接写成细胞类型事实。',
    '不得把热图颜色直接写成药效机制。',
    '必须说明 SCBP/OSCA/OSTA 是现代组学拓展来源。'
  ]
}
```

- [ ] **Step 3: Build site and verify generated pages**

Run:

```powershell
Push-Location site
npm run build
Pop-Location
```

Expected: build exits 0 and Pagefind indexes the generated pages.

---

### Task 6: Extend Maintenance Checks

**Files:**
- Modify: `scripts/maintenance/course_online_book_check.py`
- Test: `tests/test_course_online_book_check.py`

- [ ] **Step 1: Add testable helper functions**

If `course_online_book_check.py` still only has CLI-oriented checks, extract helpers with this interface:

```python
def contains_required_terms(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if term not in text]

def has_forbidden_raw_reference(text: str) -> bool:
    return "materials/raw" in text.replace("\\\\", "/")
```

- [ ] **Step 2: Add tests for raw paths and Week 13 terms**

Create `tests/test_course_online_book_check.py`:

```python
from scripts.maintenance.course_online_book_check import (
    contains_required_terms,
    has_forbidden_raw_reference,
)


def test_has_forbidden_raw_reference_detects_windows_and_posix_paths():
    assert has_forbidden_raw_reference("materials/raw/sc_best_practices")
    assert has_forbidden_raw_reference("materials\\\\raw\\\\sc_best_practices")


def test_contains_required_terms_reports_missing_terms():
    missing = contains_required_terms("Week 13 现代组学拓展", ["Week 13", "现代组学拓展", "样章候选"])
    assert missing == ["样章候选"]
```

- [ ] **Step 3: Run targeted and full tests**

Run:

```powershell
$env:PYTHONUTF8='1'
python -m pytest tests/test_course_online_book_check.py -q
python -m pytest -q
```

Expected: both commands exit 0.

---

### Task 7: Final Verification and Commit

**Files:**
- All files changed in Tasks 1-6.

- [ ] **Step 1: Run full maintenance gate**

Run:

```powershell
$env:PYTHONUTF8='1'
python scripts/maintenance/course_km_index.py --write
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
python scripts/maintenance/course_skill_inventory.py --check
python scripts/maintenance/course_online_book_check.py
python -m pytest -q
Push-Location site; npm run build; Pop-Location
```

Expected: every command exits 0.

- [ ] **Step 2: Confirm no forbidden generated artifacts are staged**

Run:

```powershell
git diff --cached --name-only | Select-String -Pattern 'site/dist|site/node_modules|materials/raw|outputs|ai_logs'
```

Expected: no output.

- [ ] **Step 3: Commit**

Run:

```powershell
git add course docs knowledge scripts site tests
git commit -m "Plan next coursebook upgrade"
```

Expected: commit succeeds.

---

## Self-Review

- Spec coverage: the plan covers syllabus decision lock, Week 11-13 content bridge, Week 17-18 project weeks, Week 14/16 PPT storyboard, Coursebook sync, maintenance checks, and final validation.
- Placeholder scan: no task uses TBD/TODO/fill-in placeholders; every content block has explicit headings, required wording, or command expectations.
- Type consistency: `ppt_status`, `review_status`, `badges`, and `sample` match the existing Coursebook data layer naming used in this repo.

Plan complete and saved to `docs/superpowers/plans/2026-06-04-next-coursebook-upgrade.md`. Recommended execution path for the next round: Subagent-Driven for Tasks 2-6, with local integration and verification after each task.
