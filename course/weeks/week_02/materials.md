---
type: course-week
week: 2
title: 数据分析流程、复现规范与人机协作规范
hours: 2
status: pilot_candidate
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 02 周：数据分析流程、复现规范与人机协作规范 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## AIDD 候选素材

- 从 [AIDD 课程索引](../../../materials/markdown/aidd_bioinformatics/aidd.course_index.md) 和相关 `chapter.course.md` 选取；字幕原文只作术语核验，不直接进入课堂。

## PDF / 外部 PPT 候选素材

- 从 `materials/markdown/pdf_library_mineru/` 和 `materials/markdown/pdf_library_skill_extract/` 选取已转换 Markdown；原始 PDF/PPT 不直接进入课程引用。

## OWF Git / Shell 参考候选

- [OWF Learn Git](../../../materials/markdown/openwaterfoundation_learning/git/README.md)：用于复现规范、Git 工作流、分支、提交、远端协作和常见输出消息说明。
- [OWF Learn Windows Shell](../../../materials/markdown/openwaterfoundation_learning/windows_shell/README.md)：用于 Windows 命令行、用户环境、批处理脚本和故障排查的基础参考。
- [OWF Learn Linux Shell](../../../materials/markdown/openwaterfoundation_learning/linux_shell/README.md)：用于 Linux/Bash、脚本化、重定向、日志和 cron 的基础参考。
- 使用边界：这些材料只作为“可复现工作方式”和“命令行素养”参考，不替代课程大纲，也不自动提升本周 `status`。

## 素材分层使用原则（2026-06-04）

- 课堂主素材：课程项目目录、复现规范、Prompt 记录模板和 Week 02 三件套。
- 支撑素材：AIDD Ch6 pipeline 和 Ch12 GitHub；OWF Git / Windows Shell / Linux Shell 用于版本记录、命令行和日志素养。
- 拓展素材：真实生信 pipeline 只作为输入-处理-输出的类比，不要求学生运行。
- 教师备课素材：OWF 教程用于整理 Git、shell、路径和日志讲解，不替代统计或生信事实来源。
- 教材 / PPT 边界：可进 PPT：项目目录树、AI 协作记录表、Git 小步提交示意。

## 可进 PPT 的元素

- 概念图：项目目录、Git/GitHub 记录、数据来源和 AI 日志的可复现链条。
- 示例表格：Prompt 记录表、素材溯源表和 README 最小结构。
- 代码片段：`git status`、`git add`、`git commit`、`git log --oneline`。
- AI 提示词：检查项目目录和 README 是否能支持复现，不代写结论。

## 试点候选审查依据（2026-06-04）

- 课堂任务：学生建立最小项目目录，写入 `README.md`、`data/`、`scripts/`、`outputs/`、`ai_logs/` 的用途说明，并用 Git/Shell 记录一次小步修改。
- 评价证据：提交目录截图或文本树、一次 `git status` / `git log --oneline` 记录、1 条 Prompt 记录和人工修订理由。
- AI 协作边界：允许 AI 检查目录命名、解释命令错误和整理日志；禁止 AI 替代学生决定清洗规则、隐藏失败尝试或补写未完成分析。
- 待核验点：正式演示前需核对 Windows PowerShell 命令、GitHub 隐私设置和课堂网络环境。
