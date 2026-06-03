# AI_Course Skill Loading Manifest · 2026-06-03

本页记录本轮为 AI_Course 加载或确认的全局技能，以及新增的项目本地 workflow skills。原则是：全局技能提供通用能力，项目本地 `course-*` skills 负责把能力约束到本课程工作流中。

收口说明：本清单只确认技能存在、来源和用途；课程状态仍按 `script.md` 深度、`materials.md`/`outline.md` 准备度、PPT storyboard/evidence/visual QA 三层分别判断。

## 安装边界

- 全局目录：`C:\Users\xsui\.codex\skills`
- 项目目录：`E:\Codex_Projects\AI_Course\skills`
- 不全量安装外部仓库。
- 不把外部仓库完整复制进本项目。
- 未声明 license 的来源只做个人本地技能加载和项目设计参考，不作为本项目可再分发资产。

## 外部仓库快照

| Repo | Commit | 用途 | License 状态 |
|---|---|---|---|
| `K-Dense-AI/scientific-agent-skills` | `93124850ef08487e423165554c54f0b333d5631d` | 科学写作、审查、统计、可视化白名单来源 | MIT (`LICENSE.md`) |
| `luvega/codex-skills` | `e666496a06ca22ac65970c0b194d168b4feb289a` | 证据链、教学 brief、领域解释工作流 | 根目录未发现 license 文件，需复核 |
| `zLanqing/codex-claude-academic-skills` | `7ed6377f0efb6a38951b48ef03b19d996e454b1f` | 中文学术写作与 Office/PPT 工作流 | MIT (`LICENSE`) |
| `luvega/building-llm-wiki` | `6d6cf057d541968a9b9e207b8c6ab9f0ee51bb27` | AI-native 三层知识库和本地 skill 分工思想 | 根目录未发现 license 文件，需复核 |

## 全局技能白名单

| Skill | 状态 | 来源 | 是否含 scripts | 是否含 references | AI_Course 用途 |
|---|---|---|---:|---:|---|
| `building-llm-wiki` | 已确认 | `luvega/building-llm-wiki` | 是 | 是 | 三层结构、索引和维护规则 |
| `academic-chinese-style` | 已确认 | `luvega/codex-skills`/本机已有 | 否 | 否 | 中文学术表达、克制主张 |
| `scientific-critical-thinking` | 已确认 | `K-Dense-AI/scientific-agent-skills` | 否 | 是 | 证据质量、推理错误和过度解释审查 |
| `peer-review` | 已确认 | `K-Dense-AI/scientific-agent-skills` | 是 | 是 | 课程产物多维评审 |
| `scientific-writing` | 已确认 | `K-Dense-AI/scientific-agent-skills` | 是 | 是 | 科学讲义和论证结构 |
| `scientific-slides` | 已确认 | `K-Dense-AI/scientific-agent-skills` | 是 | 是 | 科学展示和 slide 结构 |
| `scientific-visualization` | 已确认 | `K-Dense-AI/scientific-agent-skills` | 是 | 是 | 图形表达和可视化风险 |
| `statistical-analysis` | 已确认 | `K-Dense-AI/scientific-agent-skills` | 是 | 是 | 统计前提、检验和解释边界 |
| `markdown-mermaid-writing` | 已确认 | 本机已有 | 否 | 是 | README、流程图和 workflow 文档 |
| `academic-presentation-teaching` | 已安装 | `luvega/codex-skills` | 否 | 是 | PPT storyboard、lesson plan、teaching brief |
| `biomedical-research-framework` | 已安装 | `luvega/codex-skills` | 否 | 是 | 生物医学 finding 到可写主张的证据门禁 |
| `office-academic-skill` | 已安装 | `zLanqing/codex-claude-academic-skills` | 否 | 是 | 中文学术 PPT/DOCX 工作流与质量检查 |
| `research-writing-skill` | 已安装 | `zLanqing/codex-claude-academic-skills` | 否 | 是 | 中文科研写作、修改、审稿回复思想 |

安装备注：`zLanqing/codex-claude-academic-skills` 使用 zip 下载时触发 Windows 长路径解压错误，已改用 `--method git` 安装指定路径。

## 项目本地 Course Skills

| Skill | 状态 | 角色 |
|---|---|---|
| `course-skill-router` | 新增 | 统一路由讲义、PPT、证据审查、素材入库和维护任务 |
| `course-lecture-expand` | 新增 | 将短讲稿扩写为 2 学时 `pilot-script` |
| `course-ppt-storyboard` | 新增 | 先生成可审查 storyboard/brief，再进入 PPTX |
| `course-evidence-review` | 新增 | 检查 claim-evidence、统计、生物学和 AI overclaim |
| `course-update-vault` | 新增 | 维护索引、断链、周次映射、技能清单和质量门禁 |

## 验证命令

```powershell
python scripts/maintenance/course_skill_inventory.py --check
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py
python -m pytest -q
```
