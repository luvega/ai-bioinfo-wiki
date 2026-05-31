# 岭院 Marp 制作：容量量化与常见陷阱

本文档基于一次完整的"申报书答辩 PPT"制作复盘，沉淀了 Marp + 岭院主题在中文长内容场景下踩到的坑与可量化的容量规则。**制作 slides 时优先读这份文档**。

---

## 一、画布与容量量化

### 画布参数（16:9）

- 物理画布：`1280 × 720 px`（Marp 默认）
- 推荐 padding：`50px 70px 90px 70px`（上 / 右 / 下 / 左）
  - 下边距设为 `90px` 是为了避让岭院页脚红线和品牌灰条
- 可用内容区：`1140 × 580 px`
- 标题（h1，1.55em）实际占用约 `70 px`（含下方间距）
- **真正可摆放正文/列表的纵向空间 ≈ 490 px**

### 字号-容量对照表（基准字号 30px、line-height 1.55）

| 元素 | 字号 | 单行高度 | 段落间距 | 满页可摆放上限 |
|------|------|---------|---------|---------------|
| 正文 `<p>` | 30px | 46.5 px | ~16 px | **9–10 行** |
| 列表项 `<li>` | 30px | 46.5 px | ~10 px | **9–10 项** |
| blockquote | 30px | 46.5 px | 较大边距 | 7–8 行 |
| 数学公式块 | 30px+ | ~80 px | 大 | 单独占 ≈ 2 行 |
| 表格行（含 thead） | 24.6px (0.82em) | ~42 px | 0 | header + 9 行 ≈ 极限 |

### 安全行数硬上限（必须遵守）

- **纯正文页**：**安全上限 9 行**，超过 9 行 → 100% 溢出
- **带表格页**：标题 1 + 引言 1 + 表头 1 + 5–6 数据行 + 表后总结 1–2 = 极限
- **带数学公式页**：每个公式块按 2 行计；公式后段落需缩减到 6 行内
- **lead/居中页**：居中样式会放大段落间距，按 6–7 行设计

> **判断方法**：写完一页后数一下"换行次数"。每段 25 个汉字算 1 行（30px 字号下中文行宽 ≈ 30 字），超长会自动换 2 行——记得把换行也算进去。

---

## 二、必须使用的默认 style 块

复制粘贴到每份 slides 的 frontmatter 中，**不要删减**。这一块吸收了所有已知坑的修复：

```yaml
style: |
  /* 图片居中 */
  img {
    display: block !important;
    margin: 0 auto !important;
  }
  /* 内容区与基准字号 */
  section {
    font-size: 30px;
    padding: 50px 70px 90px 70px;
  }
  section h1 { font-size: 1.55em; }
  section h2 { font-size: 1.35em; }

  /* 表格：保住红头白字 */
  section table {
    display: table !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    font-size: 0.82em;
    border-collapse: collapse;
  }
  section table thead {
    background-color: #AC1B20 !important;
  }
  section table thead th {
    color: #ffffff !important;
    background-color: #AC1B20 !important;
    padding: 0.5em 0.8em !important;
    font-weight: 700 !important;
    text-align: left !important;
    border: none !important;
  }
  section table tbody td {
    padding: 0.45em 0.8em !important;
  }

  /* 列表节奏 */
  section ul, section ol { font-size: 1em; line-height: 1.55; }
  section blockquote { font-size: 1em; }

  /* 4阶段技术路线图组件 */
  .roadmap { display: flex; gap: 12px; margin-top: 18px; }
  .roadmap-phase {
    flex: 1;
    border: 2px solid #AC1B20;
    border-radius: 8px;
    padding: 14px 12px;
    background: #FBF3F3;
  }
  .roadmap-phase h4 {
    color: #AC1B20;
    margin: 0 0 8px 0;
    font-size: 0.95em;
    border-bottom: 1px solid #AC1B20;
    padding-bottom: 4px;
  }
  .roadmap-phase ul {
    margin: 0;
    padding-left: 18px;
    font-size: 0.78em;
    line-height: 1.5;
  }
  .roadmap-phase .date {
    font-size: 0.72em;
    color: #666;
    margin-bottom: 6px;
  }

  /* 联系页/二维码页组件（左栏联系信息 + 右栏二维码） */
  .contact-row { display: flex; gap: 60px; align-items: center; margin-top: 30px; }
  .contact-left { flex: 1.2; }
  .contact-left h1 { font-size: 52px; margin: 0 0 24px 0; }
  .contact-left p { font-size: 28px; line-height: 1.8; }
  .contact-right { flex: 1; text-align: center; display: flex; flex-direction: column; gap: 16px; align-items: center; }
  .contact-right img { display: inline !important; margin: 0 !important; height: 200px; }
  .contact-right p { font-size: 18px; margin-top: 4px; }
```

---

## 三、八大常见陷阱与对策

### 陷阱 1：表头渲染成空白

**症状**：表格首行显示为白底无文字（看似 thead 被吃掉）。

**根因**：自定义 `section table { ... }` 覆盖了主题的 thead 样式，CSS 特异性不够。

**对策**：上面默认 style 块中的 `section table thead th { ... !important }` 链已修复。**不要删除 `!important`**——主题 CSS 优先级与用户 style 在 Marp 中存在竞争。

### 陷阱 2：所有标题都用 h2 导致非红色

**症状**：目录页/小章节页标题渲染为黑色，与其他页红色标题不一致。

**根因**：lingnan 主题仅对 `h1` 染红色 `#AC1B20`，h2/h3 保持默认深色。

**对策**：**所有幻灯片标题统一使用 `# 标题` (h1)**。即使是"目录"也应写 `# 汇报提纲` 或 `# 目录`。h2/h3 留给页内分级标题。

### 陷阱 3：lead 居中页出现孤字

**症状**：`<!-- _class: lead -->` 页中段落最后一行只剩 1–2 个字符，视觉非常突兀。

**根因**：lead 类把所有段落居中，长段被自动换行后末行字数随机，容易出现"破。"这种孤儿。

**对策**：

- 总结页避免使用纯 lead 类，改用普通 h1 标题 + **内联格式**（小标题 — 内容同行）
- 若必须用 lead，把每段控制在 25 字内（单行不换行）
- 在末尾加一个 blockquote 引语作为视觉收束，避免段落孤悬

### 陷阱 4：列表项一项跨两行造成行数误判

**症状**：`<ul>` 看似只有 5 项，实际渲染占 8 行（每项约 30 字处自动换行）。

**对策**：每条 bullet 控制在 **25 个汉字以内**；信息密集的项用"X — Y"短语结构，关键词加粗在前。

### 陷阱 5：PNG 导出命令文件名错位

**症状**：执行 `marp-cli --images png -o dir/` 后输出文件落在 `dir.001.png`、`dir.002.png` 形式，而非 `dir/slide.001.png`。

**根因**：marp-cli 的 `-o` 把末尾不带扩展名的路径当作"前缀"。

**对策**：必须显式指定文件名：

```bash
npx @marp-team/marp-cli <md> --images png -o <output-dir>/slide.png \
  --theme-set <theme-dir>/ --allow-local-files
```

末尾的 `slide.png` 是必需的，会被自动展开成 `slide.001.png`、`slide.002.png` ……

### 陷阱 6：表格之后的小结被挤出页面

**症状**：表格本身渲染正常，但表格下方的"经费结构紧扣……"这类总结性文字被页脚挡住或截断。

**对策**：

- 表格行数控制在 **5–7 行**（含 header）
- 表后总结控制在 **1 句、最多 2 行**
- 必要时合并相似行（例：将 3 项 5 万元的人员费合并为"人员费 15 万"）

### 陷阱 7：footer 字段误用

**症状**：自行设置 `footer: '中山大学岭南学院'` 后，发现页脚变成纯文字，丢失了校徽 + 院徽 + AACSB 标志。

**根因**：岭院主题通过 CSS 把 `footer` 元素位置渲染为图片背景，文字 footer 会覆盖品牌图。

**对策**：**永远保持 `footer: ' '`（一个空格）**，品牌信息由主题 CSS 自动加载，不要手动改。

### 陷阱 8：bullet 嵌套两层导致密度失衡

**症状**：`- 一级\n  - 二级` 这种两层嵌套，二级文字会显著缩进且字号视觉变小，与主信息流割裂。

**对策**：尽量保持单层 bullet。需要细分时改用"加粗主题 + 破折号 + 解释"的内联结构：

```markdown
- **要点 A** — 简短说明 X、Y、Z
- **要点 B** — 简短说明
```

### 陷阱 9：HTML `<div>` 的行内 style 被 Marp 忽略

**症状**：写了 `<div style="display: flex; gap: 60px;">` 做左右分栏，渲染出来却是垂直堆叠，flex 完全不生效。图片挤满全宽。

**根因**：Marp (Marpit) 在解析 HTML 块时，**行内 `style=""` 属性中的布局属性（display/flex/gap 等）会被忽略或被主题 CSS 覆盖**。这与 `.roadmap` 组件能正常 flex 形成对比——因为 `.roadmap` 是通过 YAML `style:` 块中的 CSS class 定义的，Marp 正常处理 class 选择器。

**对策**：**所有自定义 flex/grid 布局必须通过 YAML `style:` 块中的 CSS class 实现，不要用行内 `style=""`**。

```markdown
<!-- ❌ 错误：行内 style 不生效 -->
<div style="display: flex; gap: 40px;">
  <div style="flex: 1;">LEFT</div>
  <div style="flex: 1;">RIGHT</div>
</div>

<!-- ✅ 正确：在 YAML style 块定义 class -->
<!-- YAML style 块加入：.my-row { display: flex; gap: 40px; } .my-col { flex: 1; } -->
<div class="my-row">
  <div class="my-col">LEFT</div>
  <div class="my-col">RIGHT</div>
</div>
```

**已内置组件**：
- **路线图**：`.roadmap` + `.roadmap-phase`（4 阶段并列）
- **联系页/二维码页**：`.contact-row` + `.contact-left` + `.contact-right`（左栏文字 + 右栏二维码）

### 陷阱 10：`img` 规则的 `!important` 阻止 flex 布局中图片缩放

**症状**：即使 flex 容器生效了，`<img>` 仍然占满全宽，不受 `height: 200px` 约束。

**根因**：主题 CSS 或 YAML style 中的 `img { display: block !important; margin: 0 auto !important; }` 强制图片为块级居中，覆盖了 flex 子项的尺寸约束。

**对策**：在容器 class 中用更高特异性的选择器覆盖：`.contact-right img { display: inline !important; margin: 0 !important; height: 200px; }`。lingnan.css 已将 `img` 规则的 `!important` 移除（2026-05-22），YAML style 块中保留 `!important` 以确保普通页图片居中，同时 `.contact-right img` 等 class 选择器可正常覆盖。

---

## 四、强制视觉自审流程

完成 Markdown 草稿后，**必须**执行以下流程：

1. **导出 PNG 序列**

   ```bash
   npx @marp-team/marp-cli <md-path> --images png \
     -o <workspace>/04_exports/slide.png \
     --theme-set <skill-path>/themes/ --allow-local-files
   ```

2. **逐页 Read 自审** — 用 Read 工具读取每张 PNG（multimodal），对照下列检查项：

   - [ ] 标题红色（h1 是否生效）
   - [ ] 表头红底白字（如有表格）
   - [ ] 文字未被页脚截断（最末行完整可见）
   - [ ] 无孤字（段尾不剩 1–2 字）
   - [ ] 列表项无视觉跨页换行
   - [ ] 内容占页面 60–80%（过满或过空都需调整）
   - [ ] 数学公式渲染完整
   - [ ] 中山大学岭南学院 + AACSB 页脚正常显示

3. **发现溢出立即按"陷阱 4/6"对策修复**——不要等到用户指出才改。

4. **再渲染验证** — 修复后再跑一次 PNG 导出并 Read 自审，直到所有页通过。

> 这是岭院主题在中文长内容场景下最关键的质量门槛。跳过此步骤几乎必然产生溢出页。

---

## 五、技术路线图组件用法

模板已内置 `.roadmap` / `.roadmap-phase` 4 阶段路线图组件。在 markdown 中按以下结构插入：

```markdown
# 技术路线图

<div class="roadmap">

<div class="roadmap-phase">
<h4>① 阶段一名称</h4>
<div class="date">2026.04 – 2026.10</div>
<ul>
<li>关键活动 1</li>
<li>关键活动 2</li>
<li>关键活动 3</li>
<li>关键活动 4</li>
</ul>
</div>

<!-- 重复 3 个 .roadmap-phase 块 -->

</div>

**贯穿主线**：……
```

每个 phase 块的列表项控制在 **4 项内**，每项 ≤ 12 字，否则盒子会被撑高错位。

---

## 六、联系页/二维码页组件用法

模板已内置 `.contact-row` / `.contact-left` / `.contact-right` 组件。用于演示首页或末尾的讲师信息+二维码页。

```markdown
<!-- _paginate: false -->
<!-- _header: '' -->

<div class="contact-row">
  <div class="contact-left">
    <h1>感谢各位！</h1>
    <p><b>主讲人：姓名</b></p>
    <p>机构职称</p>
    <p>邮箱：xxx@xxx.edu.cn</p>
  </div>
  <div class="contact-right">
    <div>
      <img src="images/qr1.jpg" />
      <p>扫码关注公众号<br/><b>公众号名称</b></p>
    </div>
    <div>
      <img src="images/qr2.png" />
      <p>课程网站<br/><b><a href="https://example.com">example.com</a></b></p>
    </div>
  </div>
</div>
```

注意：
- 二维码图片高度由 CSS class 控制（200px），无需在 `<img>` 上写 `style`
- `<!-- _paginate: false -->` 隐藏页码；`<!-- _header: '' -->` 清掉顶部 header
- 最多放 2 个二维码，再多会溢出

---

## 七、调试小贴士

- **快速预览**：`npx @marp-team/marp-cli -s <md> --theme-set ... --allow-local-files` 启动本地服务器，浏览器实时刷新
- **行数估算**：写完一页后用 `wc -l` 大致看 markdown 行数，但要按"换行展开"反向估算渲染行数
- **CSS 调试**：导出 HTML 后在浏览器 DevTools 中检查盒模型，比反复猜测 padding 值高效得多
- **遇到 thead 失效**：第一时间检查是否被 `section table` 通用规则破坏 CSS 特异性，加 `!important` 即可
