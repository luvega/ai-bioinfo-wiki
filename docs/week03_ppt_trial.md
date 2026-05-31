# Week 03 PPT 试点样稿验证记录

日期：2026-05-31

目标：把 Week 03 从 Markdown 试点稿推进到可真实打开、可逐页检查的 PPT 样稿，用真实页面验证当前课程生产工作流。

## 输入来源

- 周次材料：[materials.md](../course/weeks/week_03/materials.md)
- PPT 页级大纲：[outline.md](../course/weeks/week_03/outline.md)
- 授课脚本：[script.md](../course/weeks/week_03/script.md)
- 质量评审：[week_03_pilot_review.md](../course/evaluation/week_03_pilot_review.md)

## 生成方式

生成脚本：

```powershell
python scripts/courseware/build_week03_pilot_ppt.py
```

导出 PNG 预览：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/courseware/export_pptx_preview.ps1 `
  -PptxPath outputs/ppt/week_03_pilot/week_03_ai_python_pilot.pptx `
  -OutputDir outputs/ppt/week_03_pilot/preview_png `
  -Width 1600 -Height 900
```

## 输出产物

输出位于 `outputs/`，不进入 Git。

| 产物 | 路径 | 用途 |
|---|---|---|
| PPTX 样稿 | `outputs/ppt/week_03_pilot/week_03_ai_python_pilot.pptx` | 可编辑试讲稿 |
| 讲稿备注 | `outputs/ppt/week_03_pilot/week_03_speaker_notes.md` | 试讲节奏与核验提示 |
| PNG 预览 | `outputs/ppt/week_03_pilot/preview_png/` | 真实页面渲染检查 |
| 总览图 | `outputs/ppt/week_03_pilot/week_03_contact_sheet.png` | 12 页快速目检 |

## 页面结构

| 页码 | 页面主题 | 验证重点 |
|---:|---|---|
| 1 | 标题页 | 课程链路和试点目标清楚 |
| 2 | 从药学问题到判断规则 | 药学指标表、规则和核验逻辑同页可读 |
| 3 | Python 在本课程中的位置 | 数据、规则、代码、图表、结论流程清楚 |
| 4 | 五个最小语法单元 | 每个语法单元均有药学数据例子 |
| 5 | 血糖列表与缺失值 | `None` 与 `12.8` 的教学角色明确 |
| 6 | 代码阅读三问 | 输入、规则、输出三栏可读 |
| 7 | 最小 Python 实现 | 三行代码与三步规则对应 |
| 8 | 人工核验结果 | `6.94` 与 `[12.8]` 突出，便于课堂核验 |
| 9 | AI 解释代码 | 提示词和审计重点同时出现 |
| 10 | AI 调试与测试 | 错误代码和边界样本同页呈现 |
| 11 | 生信扩展 | 只讲序列数据结构直觉，不要求安装 Biopython |
| 12 | 小结 | 会读、会测、会问三步闭环 |

## 验证结果

- PPTX 生成成功，共 12 页。
- PowerPoint COM 导出 PNG 成功，共 12 张，分辨率均为 `1600 x 900`。
- 已生成 12 页总览图并人工目检。
- 小数据核验沿用 Week 03 试点稿：有效值 `[5.2, 6.1, 4.9, 12.8, 5.7]`，均值 `6.94`，高风险值 `[12.8]`。
- `python-pptx` 可提取所有页面标题与主要文本，证明 PPTX 文本层存在。

## 发现并修复的问题

首次导出 PNG 后发现第 12 页右侧总结卡文本被截断。已在 `build_week03_pilot_ppt.py` 中缩短并放宽第 12 页第三步卡片文案，重新生成并复验后不再截断。

## 当前结论

Week 03 已从 Markdown 试点稿推进到 PPT 试点样稿。当前样稿可用于真实页面密度、课堂节奏和代码演示验证，但还不是最终正式课件。

进入正式课件前建议继续处理：

1. 在 PowerPoint 中试讲一次，记录每页停留时间。
2. 补充教师备注到 PPT 原生 speaker notes，或保留当前独立 `week_03_speaker_notes.md`。
3. 根据课堂反馈决定是否加入更多练习页，而不是继续增加讲授信息。
