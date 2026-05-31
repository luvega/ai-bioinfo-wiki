# AI_Course · 医药数据处理与可视化 · 课程课件生产工作区

本项目服务于“医药数据处理与可视化（36 课时 · AI 前置版）”的备课、素材整理、PPT 大纲、授课脚本和后续课件生成。当前唯一有效工作区是：

```text
E:\Codex_Projects\AI_Course
```

`F:\AI_Course` 已完成迁移并删除，不再作为 Codex、Obsidian、Git 或脚本入口。

## 目录角色

```text
AI_Course\
├── AGENTS.md            # AI 协作规则和项目边界
├── memory.md            # 跨会话决策、偏好和当前状态
├── README.md            # 项目使用说明
├── materials\           # 素材层：原始素材与转换 Markdown
├── knowledge\           # 知识层：来源、概念、实体、综合映射
├── course\              # 课程层：正式大纲、周次产物、模板、考核
├── scripts\             # 转换、课件和维护脚本
├── skills\              # 项目本地 Codex skills
├── docs\                # 计划、迁移边界、维护文档
├── outputs\             # 最终导出的 PPT、讲义和脚本
└── site\                # 课程网站实验区
```

核心边界：

- `course/syllabus/` 是课程事实主线。
- `course/weeks/week_01` 到 `week_18` 是课件生产主工作区。
- `knowledge/` 是备课辅助层，不替代课程大纲。
- `materials/raw/` 默认只读；原始 PDF 和外部课件不进入 Git。
- `outputs/`、`site/node_modules/`、`site/dist/`、缓存和临时文件不进入 Git。

## 课程产物标准

每个周次至少包含：

- `materials.md`：素材来源、可用程度、待核验点。
- `outline.md`：PPT 页级大纲，含药学问题入口。
- `script.md`：可直接授课的讲稿，不只是提纲。

样板周为 `week_03`、`week_14`、`week_15`、`week_16`。样板周固定包含：

- 教学目标
- 药学场景或药学问题入口
- 核心数据结构
- 课堂任务
- AI协作边界
- 课后练习
- 素材来源
- 待核验

## 维护命令

每次 meaningful ingest、courseware draft 或结构调整后运行：

```powershell
python scripts/maintenance/course_km_index.py --write
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python -m pytest -q
```

通过标准：

- `course_km_index.py --check` 输出 `OK`。
- `course_quality_check.py --check` 输出 `OK`。
- `pytest` 全部通过。
- 样板周通过质量区块检查；非样板周允许保持 draft，但必须有三件套。

## 当前节奏

下一步不是继续堆素材，而是先稳定产出链：

1. 维护 E 盘唯一真源。
2. 完成迁移边界核对清单。
3. 打磨 `week_03`、`week_14`、`week_15`、`week_16` 样板周。
4. 用维护脚本检查周次三件套、断链、索引和 Week 11/15 历史错位。
5. 再进入三套 PPT 试点：Week 03、Week 15、Week 16。

下一轮执行计划见 [AI_Course 下一轮工作计划](docs/next_round_work_plan_2026-05-31.md)。

暂不全量生成 18 周 PPT，不 push，不修改远端。
