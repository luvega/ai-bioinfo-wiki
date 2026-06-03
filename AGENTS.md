# AGENTS.md · AI_Course 课程课件生产工作流

本文件定义 `E:\Codex_Projects\AI_Course` 的 AI 协作规则。当前目标是稳定产出“医药数据处理与可视化（36 课时 · AI 前置版）”课程课件，而不是维护独立百科。

`F:\AI_Course` 已迁移并删除，不再作为工作区、回退目录或 Obsidian vault。

## 新会话启动顺序

每个新会话先读：

1. `AGENTS.md`
2. `memory.md`
3. `knowledge/index.md`
4. `course/weeks/_index.md`（若不存在，先运行维护脚本生成）
5. 与任务相关的 `course/weeks/week_XX/{materials,outline,script}.md`

## 目录边界

```text
E:\Codex_Projects\AI_Course\
├── materials\           # 原始素材和转换 Markdown
├── knowledge\           # 来源、实体、概念、综合映射
├── course\              # 课程事实主线和周次产物
├── scripts\             # 转换、课件和维护脚本
├── skills\              # 项目本地 skills，不写回全局
├── docs\                # 项目计划、迁移核对、维护说明
├── outputs\             # 导出物，不入 Git
└── site\                # 网站实验区，构建产物不入 Git
```

`course/syllabus/` 优先级最高。`knowledge/` 只做备课辅助；如果和 `course/syllabus/` 冲突，以 `course/syllabus/` 为准，并修正 stale 说明。

## 技能加载与路由

本项目采用“双层技能体系”：

- 全局技能白名单提供通用科研、写作、审查和 Office/PPT 能力；来源与版本记录在 `docs/skill_loading_manifest_2026-06-03.md`。
- 项目本地 `skills/course-*` 负责把全局能力约束到 AI_Course 的课件生产闭环。

处理课程任务时优先使用：

1. `course-skill-router`：判断任务属于讲义扩写、PPT storyboard、证据审查、素材入库还是维护。
2. `course-lecture-expand`：扩写每周 `script.md`，目标是 `pilot-script` 或更高。
3. `course-ppt-storyboard`：生成 PPTX 前先产出可审查 storyboard/brief。
4. `course-evidence-review`：检查统计、生物学、图形和 AI 输出的 claim-evidence 边界。
5. `course-update-vault`：运行索引、断链、周次映射、讲义深度和技能清单维护。

全局技能可以辅助，但不能决定写入位置、状态标签或课程事实主线。若全局技能输出与 `course/syllabus/` 或 `course/weeks/` 冲突，以课程主线为准。

## 周次产物标准

每个 `course/weeks/week_XX/` 必须具备：

- `materials.md`
- `outline.md`
- `script.md`

样板周 `week_03`、`week_14`、`week_15`、`week_16` 必须包含教学目标、药学场景、核心数据结构、课堂任务、AI协作边界、课后练习、素材来源和待核验点。

状态语义必须分层判断：

- `script.md` 的 `status: formal_ready` 和 `depth: full-lecture` 只代表讲义深度达标。
- `materials.md` 与 `outline.md` 的 `status` 才代表周次素材/大纲准备度；非样板周可保持 `draft`。
- PPT 状态单独按 storyboard、evidence review、PPTX 生成和 PNG/contact sheet 视觉 QA 判断。
- 不得因为某周 `script.md` 已 `formal_ready` 就自动生成 PPT 或宣称整周已正式可发布。

## 硬规则

1. 脚本路径必须从仓库根目录推导，不把绝对根目录写死进脚本逻辑。
2. 原始素材只读；纠错写到 `knowledge/`、`course/weeks/*/materials.md` 或单独说明页。
3. 课程产物写入 `course/`；最终导出写入 `outputs/`。
4. 原始商业 PDF、外部 PPT/PDF、学生数据、日志、缓存、`site/node_modules/`、`site/dist/` 不进入 Git。
5. 项目本地 `skills/` 只服务本项目；除非用户明确要求，不复制到全局 `$CODEX_HOME/skills`。
6. 不使用 Obsidian `[[wiki link]]`；跨文件引用用标准 Markdown 链接。
7. 不 push、不改远端可见性、不删除远端仓库，除非用户再次明确确认。
8. 面向药学本科生，不默认生信或统计背景；优先用药效、临床指标、表达矩阵、科研图表解释。
9. AI 可用于解释、局部生成、核验和重构，不替代医学判断、统计判断或真实数据核验。

## 维护命令

```powershell
python scripts/maintenance/course_km_index.py --write
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
python scripts/maintenance/course_skill_inventory.py --check
python scripts/maintenance/course_online_book_check.py
python -m pytest -q
Push-Location site; npm run build; Pop-Location
```

若新增、移动、重命名课程/知识/素材 Markdown，先更新索引，再检查断链、样板周质量和在线教材映射。
