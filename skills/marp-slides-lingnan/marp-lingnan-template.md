---
marp: true
theme: lingnan
paginate: true
size: 16:9
# size: 4:3     # 可选4:3比例，取消注释并注释上行即可切换
header: ''
footer: ' '
style: |
  /* 图片居中 */
  img {
    display: block !important;
    margin: 0 auto !important;
  }
  /* 内容区与基准字号（30px 是经实测的最佳投影可读字号） */
  section {
    font-size: 30px;
    padding: 50px 70px 90px 70px;
  }
  section h1 { font-size: 1.55em; }
  section h2 { font-size: 1.35em; }

  /* 表格：保住红头白字（!important 链不可删，否则 thead 塌成空白） */
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
  section.outline ul li { margin: 0.55em 0; line-height: 1.7; }
  section.sparse ul li { margin: 0.4em 0; line-height: 1.7; }
  section blockquote { font-size: 1em; }

  /* 稀疏页内容纵向居中（必须 !important，覆盖 lingnan 主题的 flex-start） */
  section.outline, section.sparse {
    justify-content: center !important;
  }

  /* 4 阶段技术路线图组件（用 <div class="roadmap"> 调用） */
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
---

<!--
  ====== 容量速查表（30px 基准字号）======
  · 正文段落：满页 ≤ 9 行（含自动换行展开）
  · bullet 列表：满页 ≤ 9 项，单项 ≤ 25 个汉字
  · 表格：header + 7 行内
  · 数学公式：每个按 2 行计
  · lead/居中页：6–7 行（更宽松）
  · 路线图：4 阶段，每阶段 ≤ 4 项 × ≤ 12 字

  ====== 标题强制 h1 ======
  · 所有幻灯片标题用 # ，不要用 ##
  · h2/h3 仅用于页内分级
-->


<!-- _class: title -->

# 演示文稿主标题

**副标题说明**

演讲人，机构，日期

---

## 目录

1. **第一部分**：简要说明
2. **第二部分**：简要说明
3. **第三部分**：简要说明
4. **第四部分**：简要说明

---

<!-- _class: divider -->

# Part 1：第一部分标题

---

# 核心观点

**关键陈述用粗体强调。**

正文内容用于解释和说明。

目标：**用一句话概括本页要点。**

---

# 要点列表

**核心要素：**

1. **第一点**：解释说明
2. **第二点**：解释说明
3. **第三点**：解释说明
4. **第四点**：解释说明

---

# 详细对比

**两种方式：**

1. **方式一**
   - 特点：描述
   - 用途：说明

2. **方式二**
   - 特点：描述
   - 用途：说明

---

# 对比展示：错误 vs 正确

**错误示例**
> 这是一个不好的例子，展示常见错误。

**正确示例**
> 这是一个好的例子，展示正确做法。

---

# 重要引用

> 重要引用使用 blockquote 格式，会显示为红色左边框。

—— 出处

---

<!-- _class: divider -->

# Part 2：第二部分标题

---

# 四步流程

1. **步骤一**：说明
2. **步骤二**：说明
3. **步骤三**：说明
4. **步骤四**：说明

---

# 练习环节

**修改前：**
> 冗长、复杂、不清晰的表述示例。

**修改后：**
> 简洁、清晰、有力的表述示例。

---

# 需要避免的问题

**问题清单：**

- 问题一 → 替代方案
- 问题二 → 替代方案
- 问题三 → 替代方案
- 问题四 → 直接删除

---

<!-- _class: divider -->

# Part 3：第三部分标题

---

# 完整修改示例

**修改前：**
> 冗长、复杂、充满问题的原始文本示例。

**修改后：**
> 简洁、清晰、有效的修改后文本。

---

# 黄金法则

**"朗读你的作品。"**

你的耳朵能发现：
- 问题一
- 问题二
- 问题三
- 问题四

---

<!-- _class: lead -->

# 总结

**句子层面：**
- 要点一
- 要点二

**段落层面：**
- 要点一
- 要点二

**整体层面：**
- 要点一
- 要点二

---

# 核心信息

**"核心理念一句话总结。"**

清晰的表达反映清晰的思考。

**首先，** 通过写作发现你的想法。

**然后，** 通过修改让读者无法误解你。

---

<!-- _class: thanks -->

# 谢谢！

**敬请批评指正**

联系方式 | 机构名称

---

<!-- 联系页/二维码页示例（可放在标题页之后或致谢页之前） -->
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
