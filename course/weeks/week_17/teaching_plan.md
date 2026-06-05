---
type: course-teaching-plan
week: 17
title: 综合项目工作坊：AI 协作分析与结果核验
duration_minutes: 90
teaching_plan_status: teaching_plan_ready
storyboard_source: course/weeks/week_17/ppt_storyboard.md
chapter_source: course/textbook/chapters/chapter_17.md
source: [materials.md, outline.md, script.md, ppt_storyboard.md, course/textbook/chapters/chapter_17.md]
---

# Week 17 Teaching Plan：综合项目工作坊：AI 协作分析与结果核验

## 本周定位

本教学计划回答“90 分钟怎么教”，不替代教材章节，也不替代 PPT storyboard。教材章节负责组织 `README、data_sources、AI 使用声明、storyboard` 等知识体系；PPT storyboard 负责把这些内容拆成 40 页可审查投屏源稿；本文件负责把教师活动、学生动作、课堂产物和评价证据串成 2 课时课堂流程。

本周位于“项目交付、汇报答辩与课程闭环”阶段，导入问题是：一个项目包怎样让同学和教师追溯问题、数据、代码、图表和 AI 使用？ 课堂目标不是把学生训练成完整 workflow 操作者，而是让学生能在药学本科背景下说清楚输入、处理、输出和证据边界。

## 学习目标

- 整理 README、data_sources、AI statement 和 storyboard。
- 完成图表证据边界自查。
- 用 Git/GitHub 或等价记录保留关键版本。

## 90 分钟时间切分

| Block | Minutes | Storyboard slides | Teaching focus | Teacher activity | Student action | Classroom product | Assessment evidence | Materials |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| 课程定位与导入 | 8 min | 1-4 | 校准本周问题、上一周衔接和常见误区。 | 用导入问题和反例表达建立本周证据边界。 | 学生完成问题拆解或过度结论降级。 | 问题拆解表和过度结论降级句 | 能把本周导入问题拆成数据、方法、边界三栏 | course/textbook/chapters/chapter_17.md |
| 核心概念展开 | 16 min | 5-12 | 把术语放回输入、输出和药学解释场景。 | 逐个概念追问字段、前提和不能支持的结论。 | 学生标注概念对应的数据字段或图形元素。 | 概念输入输出表和不能支持的结论清单 | 能把术语放回字段、图形或方法前提中解释 | course/textbook/assets/diagrams/week17_project_workflow.mmd |
| 数据结构与案例 | 20 min | 13-20 | 用小数据表建立字段、观测单位和 metadata 直觉。 | 带学生阅读字段字典、来源说明和质量风险。 | 学生标出主键、分组、单位和进入代码前的风险。 | 字段字典、观测单位判断和质量风险清单 | 能准确说出关键字段、单位、来源和进入代码前的核验点 | course/textbook/assets/datasets/week17_project_package_check.csv |
| 方法流程与代码 | 24 min | 21-30 | 把方法路线、代码输入、处理逻辑和输出连成可复核链条。 | 逐段解释代码意图，只讲本周需要的最小结构。 | 学生运行或阅读代码，并手工复核一处输出。 | 代码运行记录、手工复核结果和参数说明 | 能把代码输入、处理逻辑和输出结果逐项对应 | course/textbook/assets/code/week17_project_package_audit.py |
| 图表与结果解释 | 14 min | 31-36 | 训练图表视觉编码、结果表字段和图注证据边界。 | 用同一张图或表反复追问看到什么、支持什么、还需核验什么。 | 学生改写图注或执行 Claim-Evidence Gate。 | 图注草稿、结果解释句和 Claim-Evidence Gate | 能区分图上观察、统计关联、候选解释和待核验事实 | course/textbook/assets/diagrams/week17_project_workflow.mmd |
| AI 协作与核验收束 | 8 min | 37-40 | 把 AI 使用限定为解释、检查、重构和边界改写。 | 示范把 AI 输出拆成保留、修改、删除三类。 | 学生写出限定任务边界的 prompt 和克制总结句。 | 限定边界的 prompt、AI 输出审计和克制总结句 | 能指出 AI 输出中可保留、需修改和必须删除的内容 | course/textbook/chapters/chapter_17.md |

## 课堂产物与评价证据

- 学生至少完成一个可提交产物：`检查一个项目包是否包含五件最低交付物。`。
- 评价证据以“能否解释字段、代码、图表和证据边界”为准，不以是否复现完整高级 workflow 为准。
- 参考答案要点：答案应指出缺少数据来源、AI 使用声明或图表边界时不得进入最终汇报。
- 教师巡查时优先看学生是否记录输入文件、处理规则、输出解释、AI 使用和人工修订理由。

## 所需素材

- 教材章节：`course/textbook/chapters/chapter_17.md`
- PPT storyboard：`course/weeks/week_17/ppt_storyboard.md`
- 小数据：`course/textbook/assets/datasets/week17_project_package_check.csv`
- 代码或伪代码：`course/textbook/assets/code/week17_project_package_audit.py`
- Mermaid 示意图：`course/textbook/assets/diagrams/week17_project_workflow.mmd`

## AI 协作边界

AI 可以帮助解释概念、定位报错、改写图注和生成核验清单；不能替代医学判断、统计判断、真实数据核验、基因功能核验、细胞注释或临床建议。教师应要求学生把 AI 输出写入审计记录，并标出可保留、需修改和必须删除的句子。

## 与教材和 storyboard 的关系

- 教材章节用于课前预习、课后复习和知识体系整理。
- 教学计划用于组织 90 分钟课堂节奏、学生动作和评价证据。
- PPT storyboard 用于后续裁剪成正式投屏页；40 页源稿不等于最终课件页数，也不表示 PPTX 或视觉 QA 完成。
- 本周 storyboard 的每一页 `Timing` 必须落入上方 6 个教学块；若后续改 storyboard，应同步调整本教学计划。

## 来源与待核验点

- `knowledge/entities/GitHub.md`
- `knowledge/concepts/AI协作边界.md`
- `course/weeks/week_17/teaching_pack_v1.md`

- 若替换外部图、真实数据或公开图形，必须重新核对来源、授权和参数记录。
- 若 AI 输出涉及机制、疗效、统计显著性、基因功能、通路或细胞类型，必须回到课程数据、数据库或人工审查记录核验。
