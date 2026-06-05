---
type: course-week
week: 3
title: AI 辅助编程与 Python 快速入门
hours: 2
status: pilot_ready
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 03 周：AI 辅助编程与 Python 快速入门 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## 本周定位

本周是课程的编程入口。目标不是系统讲完 Python，而是让药学学生建立“读懂小段代码、用小数据验证结果、用 AI 辅助解释和调试”的基本工作方式。课堂示例优先采用临床指标列表、样本分组字典和简单序列数据，避免一开始陷入复杂软件安装。

## AIDD 候选素材

- `materials/markdown/aidd_bioinformatics/aidd.course_index.md`
- `materials/markdown/aidd_bioinformatics/02_Python_Language_for_Bioinformatics_(Biopython_for_Bioinformatics)/chapter.course.md`
- `02_Python_Language_for_Bioinformatics_(Biopython_for_Bioinformatics)/01_BioPython_Introduction.txt`：可用于说明 Python 在生信中的工具属性。
- `02_Python_Language_for_Bioinformatics_(Biopython_for_Bioinformatics)/02_Setting_up_Coding_Environment.txt`：可作为开发环境与 VS Code 课堂提示。
- `02_Python_Language_for_Bioinformatics_(Biopython_for_Bioinformatics)/05_Sequence_Analysis_Using_Biopython.txt`：可抽取“读取序列、计算长度、GC 含量”的轻量案例。
- `03_Python_For_Bioinformatics_Application_Developemnt_(Tkinter_App_Development)/01_Introduction_to_Bioinformatics_Application_Developemnt.txt`：只取“把分析步骤封装为工具”的意识，不进入 GUI 细节。

## PDF / 外部 PPT 候选素材

- `materials/markdown/pdf_library_mineru/Pythonppt/book.course.md`：中文 Python 入门表达，重点回查“Python 开发环境配置”“Python 程序编写与运行”“Python 语法元素理解”“Python 程序的输入输出”。
- `materials/markdown/pdf_library_mineru/R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro/book.course.md`：AI 辅助编程主素材，重点回查“Introducing AI-assisted programming with Copilot”“Getting started with Copilot”“Reading Python code”“Testing and prompt engineering”。
- `materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/book.course.md`：补充 GenAI 数据分析工作流、提示词迭代和代码调试，不作为 Python 语法主线。

## OWF Git / Shell 参考候选

- [OWF Learn Git](../../../materials/markdown/openwaterfoundation_learning/git/README.md)：用于解释为什么 AI 生成代码后仍要保存版本、查看差异、提交小步变更。
- [OWF Learn Windows Shell](../../../materials/markdown/openwaterfoundation_learning/windows_shell/README.md)：用于 Windows 课堂环境中的命令提示符、批处理和路径问题提示。
- [OWF Learn Linux Shell](../../../materials/markdown/openwaterfoundation_learning/linux_shell/README.md)：用于说明 Bash 命令、脚本和重定向概念；本周不要求学生掌握完整 Bash。
- 使用边界：这些材料只补足 AI 辅助编程前的 Git/shell 操作背景，不替代本周 Python 小数据和人工核验主线。

## 素材分层使用原则（2026-06-04）

- 课堂主素材：Week 03 试点讲稿、PPT 大纲和血糖列表小案例。
- 支撑素材：AIDD Python/Biopython 章节、AI 编程参考书、嵩天 Python PPT 已转换 Markdown。
- 拓展素材：Biopython 只作文件和序列数据类比，不提前讲复杂生信算法。
- 教师备课素材：OWF Git/Shell 可用于解释为什么 AI 生成代码后要看 diff、保存小步版本。
- 教材 / PPT 边界：可进 PPT：`glucose` 小列表、手算核验表、AI 解释/调试边界。

## 可进 PPT 的元素

- 概念图：`问题 -> 小数据 -> Python 表达 -> AI 解释/调试 -> 人工核验`。
- 示例表格：患者 ID、分组、血糖值、是否缺失、是否高风险。
- 代码片段：列表过滤、均值计算、阈值判断、字典查找。
- AI 提示词：解释代码、定位错误、生成测试用例、检查边界情况。

## 课堂小数据

```python
glucose = [5.2, 6.1, 4.9, None, 12.8, 5.7]
groups = {
    "S01": "control",
    "S02": "treatment",
    "S03": "control",
    "S04": "treatment",
}
```

## 试点课交付清单

- 课堂核心问题：学生能否把“忽略缺失值、计算均值、标记高风险值”转成可核验的 Python 代码。
- 课堂数据：使用上方 `glucose` 列表，不引入外部包，便于手算。
- 讲授材料：12 页 PPT 大纲、2 学时授课脚本、AI 协作提示词、课堂核验表。
- 上机产物：一段 5 行以内 Python 代码、一条 AI 解释提示词、一份人工核验记录。
- 验收标准：学生能说出输入、输出、规则、边界情况，并解释为什么 `None` 不能直接参与 `sum()`。

## 课堂预期输出

```python
valid = [x for x in glucose if x is not None]
mean_glucose = sum(valid) / len(valid)
high_risk = [x for x in valid if x > 7.0]
```

| 项目 | 预期结果 | 核验方式 |
|---|---:|---|
| 有效数值 | `[5.2, 6.1, 4.9, 12.8, 5.7]` | 检查是否排除 `None` |
| 有效样本数 | `5` | 手数列表长度 |
| 均值 | `6.94` | `34.7 / 5` |
| 高风险值 | `[12.8]` | 与阈值 `> 7.0` 比较 |

## 进入 PPT 前需核验

- Python 例子必须能手算核对，避免学生只相信 AI 输出。
- AIDD 的 Biopython 例子只做“医药数据场景扩展”，不要求学生本周安装或熟练使用 Biopython。
- Copilot / ChatGPT 教材中的工具界面内容可能随版本变化，PPT 中只讲稳定原则：提示词、阅读、测试、调试。
## 样板周质量区块

### 素材来源
- 课程主线：`course/syllabus/36课时-AI前置调整版.docx`。
- 编程入口素材：AIDD Python/Biopython 字幕、中文 Python 课件、AI-assisted Python programming 参考书。

### 可用程度
- 可直接进 PPT：小型血糖列表、样本分组字典、`问题 -> 小数据 -> Python 表达 -> AI 解释/调试 -> 人工核验` 流程图。
- 需改写后进 PPT：Biopython 示例，只作为医药数据结构扩展，不作为本周安装要求。

### 待核验
- Python 示例必须能手算核对。
- AI 工具界面截图不作为稳定教学内容，只讲提示词、阅读、测试、调试原则。
