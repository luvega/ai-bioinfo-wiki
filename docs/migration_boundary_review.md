# AI_Course 迁移边界核对清单

日期：2026-05-31

当前唯一有效根目录：`E:\Codex_Projects\AI_Course`

`F:\AI_Course` 已清空并删除，不再作为回退目录。后续 Codex、Obsidian、Git 和脚本操作均以 E 盘目录为准。

## 结构映射

| 旧路径/旧角色 | 当前路径/当前角色 | 是否保留 | 是否入 Git | 人工复核 |
|---|---|---:|---:|---|
| `doc/` 正式大纲和主讲稿 | `course/syllabus/` | 是 | 是 | 复核 docx 与 Markdown 主讲稿是否同版 |
| `raw/AIDD_Bioinformatics/` | `materials/raw/aidd_bioinformatics/` | 是 | 是 | 抽查字幕清理后是否缺章节 |
| `sources/AIDD_Bioinformatics/` | `materials/markdown/aidd_bioinformatics/` | 是 | 是 | 复核 AIDD 镜像索引和章节映射 |
| `sources/PDF_Library/` | `materials/markdown/pdf_library_mineru/` | 是 | 是 | 保留 MinerU 完整转换；旧版轻量转换已移除 |
| `wiki/sources/` | `knowledge/sources/` | 是 | 是 | 检查来源页链接和摘要是否仍准确 |
| `wiki/entities/` | `knowledge/entities/` | 是 | 是 | 清理孤岛实体页 |
| `wiki/concepts/` | `knowledge/concepts/` | 是 | 是 | 检查 Week 11/15 历史错位 |
| `wiki/topics/` | `knowledge/topics/` | 是 | 是 | 只作为主题背景，不替代课程事实 |
| `wiki/synthesis/` | `knowledge/synthesis/` | 是 | 是 | 复核跨素材判断是否仍服务课程 |
| 旧 `scripts/*.py` | `scripts/convert/`、`scripts/courseware/`、`scripts/maintenance/` | 是 | 是 | 确保脚本从仓库根推导路径 |
| 原始商业 PDF | `materials/raw/pdf_originals/` | 本地保留 | 否 | 版权和体积原因，不入 Git |
| 外部 PPT/PDF | `materials/raw/external_ppt/` | 本地保留 | 否 | 只抽取可教学内容到 Markdown |
| 导出物 | `outputs/` | 本地保留 | 否 | PPT 试点后人工视觉复核 |
| 网站依赖/构建产物 | `site/node_modules/`、`site/dist/` | 可重建 | 否 | 由网站工具链重建 |
| 临时文件 | `tmp/`、缓存、日志 | 可删除 | 否 | 不作为课程来源 |

## 当前提交前检查

- `python scripts/maintenance/course_km_index.py --write`
- `python scripts/maintenance/course_km_index.py --check`
- `python scripts/maintenance/course_quality_check.py --check`
- `python -m pytest -q`

## PPT 试点边界

暂不全量生成 18 周 PPT。先生成并检查：

| 试点 | 主题 | 检查重点 |
|---|---|---|
| Week 03 | AI 辅助编程与 Python 快速入门 | 代码可手算核验、AI 协作边界、Python 课堂任务 |
| Week 15 | 差异表达分析与功能解读 | 火山图/热图解释、padj/log2FC、功能解释核验 |
| Week 16 | 单细胞转录组可视化 | QC/UMAP/marker 图、参数敏感性、细胞注释边界 |
