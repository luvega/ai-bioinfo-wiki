---
type: textbook-logical-v2-chapter
title: 第 2 章 可复现项目与 AI 协作规范
chapter: 2
status: review_ready
review_status: review_ready
version: 2
created: 2026-06-05
core_question: 一个分析为什么必须能追溯来源、代码、Prompt 和人工核验？
source_weeks:
  - course/weeks/week_02
  - course/weeks/week_17
  - course/weeks/week_18
source_chapters:
  - course/textbook/chapters/chapter_02.md
  - course/textbook/chapters/chapter_17.md
  - course/textbook/chapters/chapter_18.md
knowledge_sources:
  - knowledge/concepts/项目目录结构与可复现.md
  - knowledge/concepts/AI协作边界.md
  - knowledge/entities/GitHub.md
  - knowledge/sources/OWF_Learn_Git.md
  - knowledge/sources/OWF_Learn_Windows_Shell.md
  - knowledge/sources/OWF_Learn_Linux_Shell.md
  - knowledge/sources/Starting_Data_Analytics_GenAI.md
material_sources:
  - materials/markdown/openwaterfoundation_learning/git/README.md
  - materials/markdown/openwaterfoundation_learning/windows_shell/README.md
  - materials/markdown/openwaterfoundation_learning/linux_shell/README.md
  - materials/markdown/aidd_bioinformatics/12_GitHub_Guide_for_Students/chapter.course.md
  - course/evaluation/student_project_rubric.md
asset_sources:
  - course/textbook/assets/datasets/week02_project_manifest.csv
  - course/textbook/assets/code/week02_project_manifest.py
  - course/textbook/assets/diagrams/week02_reproducible_workflow.mmd
learning_evidence:
  - 项目 README 草稿
  - data_sources 与 ai_use_statement 最小交付包
tags: [course, textbook, logical-v2, review-ready, reproducibility]
---

# 第 2 章 可复现项目与 AI 协作规范

## 导入问题

在医药数据课程中，学生常把“分析完成”理解成图画出来、结果表算出来、汇报页写出来。但对教师和未来读者而言，一个分析只有在能追溯来源、代码、Prompt 和人工核验时才算可审查。第 2 章把可复现项目作为全书工作流底座：不是要求学生成为软件工程师，而是要求每一次数据处理都留下足够线索，让别人知道数据从哪里来、代码做了什么、AI 参与了什么、人在哪里做了判断。

本章核心问题是：为什么不能只交一张图或一段结论？因为图和结论都可能隐藏错误。字段可能抄错，样本可能错位，AI 可能补写不存在的来源，代码可能读取了旧文件，图注可能把统计关联写成机制事实。可复现规范不是形式主义，它是在保护学生不把“能跑通”误认为“可信”。

## 本章知识链

可复现项目从目录结构开始。一个最小项目不需要复杂工程，但应至少分清 `data_sources`、`scripts`、`outputs`、`notes` 和 `ai_use_statement`。数据来源说明记录文件名称、来源、用途、是否为教学模拟、是否允许公开。脚本目录保存处理逻辑，输出目录保存生成结果，笔记或 README 解释任务目标与运行顺序。AI 使用声明记录提示词类型、AI 生成内容、人工修改和核验点。

第二个环节是版本记录。Git 和 GitHub 在本课程里不是独立技术专题，而是用来回答“什么时候改过什么、为什么改、能否回到某个版本”。学生不需要掌握所有命令，但应理解 commit 是一个可追溯检查点，README 是项目入口，文件命名和目录结构是复现的第一层证据。

第三个环节是 Shell 和运行记录。Windows Shell、Linux Shell 或 Bash 的最低目标是能定位文件、运行脚本、记录命令和查看输出。对于组学素材，命令行还承担流程日志的角色；对于本科教材，本章只保留最小能力：知道命令在哪个目录运行、输入文件是什么、输出文件写到哪里、失败时错误信息是什么。

第四个环节是 AI 协作。AI 可以解释 README、生成目录草案、检查遗漏字段、把运行记录改写成清单。但 AI 不能替学生确认数据授权、不能替教师判断统计前提、不能把未核验代码写成事实来源。可复现规范要求 AI 的参与也能被审查，而不是藏在“我问了 AI”这句话里。

## 核心概念

**可复现**在本课程里有三个层级。最低层级是“我自己明天能重新运行”；第二层级是“同学能按说明复核主要步骤”；第三层级是“教师能审查数据来源、AI 使用和人工判断”。本科课程不追求工业级自动化，但必须达到第三层级的审查要求。

**项目清单**是把项目资产列出来的表格。`week02_project_manifest.csv` 可以作为课堂模板：每一行记录文件、类型、用途、来源、是否可公开、是否需要人工核验。这个清单能防止学生只记得结果图，却忘记结果图来自哪个输入表和哪个脚本。

**AI 使用声明**不是道德口号，而是证据文件。它应写清楚 AI 参与了哪些环节，例如解释代码、整理图注、生成候选核验点；也要写清楚 AI 没有替代哪些环节，例如医学阈值、统计检验选择、真实来源确认、最终结论。没有 AI 使用声明的项目，无法审查人机分工。

**README**是项目入口。它不需要很长，但必须回答四个问题：项目要解决什么课堂问题，数据来源和边界是什么，如何运行或阅读关键文件，结果能支持什么和不能支持什么。README 写不好，说明项目本身还没有形成可审查结构。

## 最小工具与流程

本章的最小工具链由三个动作组成。第一，建立目录和清单。学生创建或阅读一个项目包，列出数据、代码、输出、图表和 AI 记录。第二，写运行说明。即使不真正运行复杂流程，也要说明如果运行，命令会从哪里读入文件、向哪里写出结果。第三，做人工核验。学生至少复核一个字段含义、一个输出数字或一条图注边界。

可以使用 `week02_project_manifest.py` 演示如何读取项目清单并检查必填项。脚本不是本章重点，重点是让学生看到：文件名、用途、来源、状态、核验点可以被机器检查；而数据是否真实、阈值是否合理、结论是否越界仍需要人判断。这个分工贯穿后续章节。

本章建议课堂任务是“修复一个不可复现项目包”。教师给出一个只有图和结论、没有来源说明的项目片段，学生补写 README、data_sources 和 ai_use_statement。完成后再让 AI 检查是否遗漏输入文件、运行命令或人工核验点，但要求学生标出 AI 建议中哪些仍需人工确认。

## 案例与素材来源

本章来源于 Week 02 的数据分析流程与复现规范，也连接 Week 17 和 Week 18 的综合项目交付。OWF Git/Shell 素材提供 Git、Windows Shell 和 Linux Shell 的基础讲法；AIDD GitHub Guide 提供学生项目协作背景；GenAI 数据分析素材提供 AI 协作中的质量检查意识。它们都只服务本课程项目，不把本章变成完整 Git 教程或命令行教程。

`knowledge/concepts/项目目录结构与可复现.md` 是本章的核心知识支持层。`knowledge/entities/GitHub.md` 支持版本记录和远端协作。`course/evaluation/student_project_rubric.md` 约束最终项目交付，确保本章不是孤立规范，而是 Week 17-18 评分标准的提前铺垫。

## AI 协作与核验

AI 可以用于检查项目包是否清楚。一个合格提示词可以写成：“请检查这个 README 是否说明了数据来源、运行步骤、AI 使用和结论边界；不要补写不存在的来源。”学生应把 AI 返回结果分成三类：可以直接采纳的结构建议，需要人工确认的来源建议，必须删除的虚构内容。

AI 不能替代可复现记录。若学生让 AI 生成一个漂亮 README，但没有真实文件清单、没有运行输出、没有人工核验记录，这个 README 仍然不合格。项目自查时应优先看文件是否存在、路径是否可追踪、代码和输出是否对应，而不是只看语言是否完整。

本章还要强调隐私和公开边界。真实学生数据、患者信息、商业 PDF、外部 PPT/PDF 和输出缓存不应进入 Git。课程项目若使用教学模拟数据，应明确标注模拟；若使用公开数据，应记录来源和许可；若来源不清，应停止公开展示。

## 学习证据

本章的学习证据是一个最小项目包。它至少包含 README、data_sources、ai_use_statement 和一个项目清单。README 说明课堂问题和阅读顺序；data_sources 记录数据来源、用途和边界；ai_use_statement 记录 AI 参与内容和人工核验点；项目清单列出关键文件与状态。

评价标准不看项目复杂度，而看可追溯性。一个简单血糖表项目如果能清楚记录来源、代码、输出和边界，优于一个使用很多工具但无法复核的复杂项目。学生在课程后半段做差异表达或单细胞图形判读时，也必须沿用这套交付包。

## 证据表达与学习路径

第 2 章不是 Git、GitHub 或 Shell 的入门大全。可复现规范在本课程中是项目的服务层，重点不是命令数量，而是每一步都能留下线索。你可以接触 `git status`、`git commit`、`README`、`data_sources` 等名词，但真正要掌握的是：如何让数据、代码、输出、AI 使用和人工核验互相对应。

“复现”在这里首先意味着自己能回到现场，也意味着同学能跟读、结果能被检查。药学本科生最先需要的是少量稳定习惯：用相对路径说明文件位置，用清单记录来源，用日志记录处理，用 AI 使用声明记录人机分工。只要这些习惯存在，后续进入图表、DE 或单细胞项目时，错误更容易被发现。

AI 协作要写得具体而不神秘。AI 不是自动分析师，而是一组可限定的辅助功能：解释错误、检查遗漏、改写说明、生成测试样例、整理核验清单。每个功能都要配一条人工责任。例如 AI 可以提示“README 缺少数据来源”，但真实来源必须由学生补；AI 可以建议“记录运行命令”，但命令是否执行过必须由学生确认。

项目规范应从第一批小案例开始使用，而不是等综合项目才引入。整理表格、解释统计结果、修改图注、审查 DE 表时，都应能回到第 2 章的最小项目包。这样，第 2 章就不是抽象规范，而是后续每章的工作台。

## 证据边界

可复现要求必须控制在本科可执行范围。复杂 Git 工作流、命令行 pipeline、分支模型和协作权限不是本章重点。最小目录、README、来源表、AI 使用声明和运行记录才是本课程需要反复使用的证据结构。

有目录、有文件名并不自动可信。项目还要说明来源是否为教学模拟、字段是否核验、代码输出是否与表格对应、AI 修改是否被人工确认。复现不是把文件放齐，而是让证据链能被检查。

隐私和 Git 边界同样属于证据边界。原始商业 PDF、外部 PPT/PDF、学生数据、日志、缓存和输出物不应进入 Git。项目本地 skills 不写入全局。若项目涉及真实数据，必须先判断是否可公开、是否需要脱敏、是否有授权来源。

综合项目最终提交的不是“分析灵感”，而是一组可检查文件。README、data_sources、ai_use_statement、图表、storyboard 和 rubric 之间应形成闭环。若项目包无法说明每张图和每段结论从哪里来，后续汇报再完整也缺少复现基础。

## 学习自查

可以用一个小项目包检查自己是否掌握本章。先故意删除来源说明、AI 使用声明或运行记录，再尝试根据本章规则指出缺了什么。若能说清“我的项目还缺哪些文件、缺这些文件会影响哪一步证据”，说明你已经理解可复现规范的作用。

AI 使用声明至少回答四个问题：AI 用在哪一步，AI 输出是否被修改，自己亲自核验了什么，哪些内容仍未核验。如果声明只写“使用 AI 辅助完成”，就不能区分人机责任；如果声明能对应 README、data_sources 和输出图表，就能进入后续项目评分。

复现记录还要能暴露错误。好的记录不仅证明学生做过什么，也能让读者看到哪里可能错。只展示成功截图，不展示输入、命令、输出和人工修改，后续无法判断图表和结论是否可信。因此，第 2 章的证据边界不是一句附加说明，而是项目包的组织原则：每个文件都要说明它支持了哪一步证据，哪些内容仍然需要人工核验，哪些内容不能由 AI 或运行结果自动推出。

本章结束时，应能把一个项目压缩成四句话：问题是什么，数据从哪里来，哪些文件支持了处理过程，哪些结论仍不能写。如果这四句话无法对应到 README、data_sources、ai_use_statement 和项目清单，就说明项目还没有达到可复现要求。

最后检查文件之间是否互相引用。README 应指向 data_sources，data_sources 应能对应输入文件，脚本或说明应能对应输出图表，ai_use_statement 应能说明哪些文字或代码经过 AI 辅助。文件之间能互相追踪，项目才不是零散材料。

所有路径都优先使用相对路径。

## 18 周反向映射

本章主要来自 Week 02，并在 Week 17-18 的综合项目中被再次使用。旧教材 `chapter_02.md` 支持流程规范，`chapter_17.md` 和 `chapter_18.md` 支持项目工作坊和汇报验收。v2 第 2 章把这些内容前置为全书工作流底座，后续每章都要回到“来源、代码、Prompt、人工核验”的交付要求。

## 待核验点

- Git/Shell 术语进入正式教材前需保持最小化，不扩展成工具百科。
- 项目模板字段应与 `course/templates/` 和学生项目 rubric 保持一致。
- AI 使用声明要覆盖提示词、AI 输出、人工修改和待核验项。
- 任何涉及公开展示的素材都要先核对来源、授权和项目 `.gitignore` 边界。
