---
type: course-source
title: 【R240】Learn AI-Assisted Python Programming With GitHub Copilot and ChatGPT (2023)【Leo Porter, Daniel Zingaro】
source_mineru: book.mineru.md
generated: 2026-05-24 12:34:06
status: generated_draft
tags: [mineru, course-material, auto-extract]
---

# 【R240】Learn AI-Assisted Python Programming With GitHub Copilot and ChatGPT (2023)【Leo Porter, Daniel Zingaro】 · 课程化整理

## 使用说明

本文件由 `book.mineru.md` 自动整理生成，服务于 36 课时课程备课。它不是原书全文，也不替代人工核验；完整解析结果请回到 `book.mineru.md`。

## 一句话定位

AI 辅助 Python 编程教材，适合作为第 3 周 AI 辅助编程和第 17 周综合项目工作流的提示词、测试、调试案例池。

## 推荐进入课程的周次

| 周次 | 课程主题 |
|---:|---|
| 3 | AI 辅助编程与 Python 快速入门 |
| 4 | R 基础语法、数据框操作与 AI 代码核验 |
| 6 | 缺失值、异常值处理与分组汇总 |
| 7 | 描述统计与分布可视化 |
| 10 | 分类问题与逻辑回归 |
| 11 | 科研图表规范与 SCI 图表表达 |
| 17 | 综合项目工作坊：AI 协作分析与结果核验 |

## 章节层级索引

- H1 L6: EA R Z AI- I-Assisted Python Programming
- H1 L48: Learn AI-Assisted Python Programming
- H1 L114: Introducing AI-assisted programming with Copilot 1
- H1 L128: Getting started with Copilot 13
- H1 L138: Designing functions 33
- H1 L147: Reading Python code: Part 1 60
- H1 L157: Reading Python code: Part 2 78
- H1 L169: Testing and prompt engineering 99
- H1 L195: Problem decomposition 124
- H1 L224: CY Debugging and better understanding your code 158
- H1 L251: Automating tedious tasks 182
- H1 L270: Making some games 216
- H1 L294: Future directions 248
- H1 L312: foreword
- H1 L330: acknowledgments
- H1 L346: introduction
- H1 L356: AI assistants change how programming is done
- H1 L364: Audience
- H1 L370: What we expect from you
- H1 L378: What you will be able to do after reading this book
- H1 L390: The challenge in working with AI assistants
- H1 L394: Why we wrote this book
- H1 L400: Warning: beware of elitism
- H1 L410: How this book is organized: a roadmap
- H1 L427: Source code downloads
- H1 L435: Software/hardware requirements
- H1 L439: liveBook discussion forum
- H1 L445: about the authors
- H1 L451: About the technical editor
- H1 L455: about the cover illustration
- H1 L461: Introducing AI-assisted 1programming with Copilot
- H1 L463: This chapter covers
- H1 L473: 1.1 How we talk to computers
- H1 L505: 1.1.1 Making it a little easier
- H1 L522: 1.1.2 Making it a lot easier
- H1 L538: 1.2 About the technology
- H1 L567: 1.2.1 Copilot, your AI Assistant
- H1 L573: 1.2.2 How Copilot works behind the scenes—in 30 seconds
- H1 L600: 1.3 How Copilot changes how we learn to program
- H1 L648: 1.4 What else can Copilot do for us?
- H1 L660: 1.5 Risks and challenges when using Copilot
- H1 L673: 1.6 The skills we need
- H1 L685: 1.7 Societal concerns about AI code assistants like Copilot
- H1 L703: Summary
- H1 L711: Getting started 2with Copilot
- H1 L713: This chapter covers
- H1 L723: 2.1 Time to set up your computer to start learning
- H1 L729: 2.1.1 Overview of the software in your programming environment
- H1 L733: GitHub account
- H1 L739: Python
- H1 L743: Visual Studio Code (VS Code)
- H1 L749: 2.2 Getting your system set up
- H1 L783: 2.3 Working with Copilot in Visual Studio Code
- H1 L822: 2.3.1 Set up your working folder
- H1 L826: File not found or file missing errors
- H1 L830: 2.3.2 Check to see if your setup is working properly
- H1 L907: output "Hello Copilot" to the screen ← The prompt
- H1 L941: 2.4 Addressing common Copilot challenges
- H1 L951: 2.5 Our first programming problem
- H1 L967: 2.5.1 Showcasing Copilot’s value in a data processing task
- H1 L993: Step 1: How many passing yards did Aaron Rodgers throw in 2019–2022
- H1 L1038: Reminder: Copilot is nondeterministic
- H1 L1055: Step 2: How well did all the quarterbacks do ov er that time period?
- H1 L1169: Step 3: Let’s plot these stats so we can compare them better
- H1 L1225: Python modules
- H1 L1289: Summary
- H1 L1298: Designing functions
- H1 L1300: This chapter covers
- H1 L1315: 3.1 Functions
- H1 L1339: 3.1.1 The components of a function
- H1 L1371: Docstrings explain function behavior
- H1 L1393: 3.1.2 Using a function
- H1 L1421: 3.2 Benefits of functions
- H1 L1440: 3.3 Roles of functions
- H1 L1608: 3.4 What’s a reasonable task for a function?
- H1 L1612: 3.4.1 Attributes of good functions
- H1 L1623: 3.4.2 Examples of good (and bad) leaf functions
- H1 L1642: 3.5 The cycle of design of functions with Copilot
- H1 L1675: 3.6 Examples of creating good functions with Copilot
- H1 L1681: 3.6.1 Dan’s stock pick
- H1 L1793: 3.6.2 Leo’s password
- H1 L1943: Importing modules
- H1 L1981: 3.6.3 Getting a strong password
- H1 L2019: 3.6.4 Scrabble scoring
- H1 L2046: Getting Copilot to suggest code may require pressing Tab or Enter
- H1 L2108: 3.6.5 The best word
- H1 L2165: Summary
- H1 L2187: Reading Python
- H1 L2189: 4code: Part 1
- H1 L2191: This chapter covers
- H1 L2205: 4.1 Why we need to read code
- H1 L2249: 4.2 Asking Copilot to explain code
- H1 L2362: Copilot Labs explanations can be wrong
- H1 L2366: Here’s what Copilot gave us the first time we asked:
- H1 L2380: 4.3 Top 10 programming features you need to know: Part 1
- H1 L2418: 4.3.1 #1. Functions
- H1 L2447: 4.3.2 #2. Variables
- H1 L2464: The = symbol is different in Python than in math
- H1 L2484: Variables persist in the Python prompt
- H1 L2521: 4.3.3 #3. Conditionals
- H1 L2677: 4.3.4 #4. Strings
- H1 L2774: 4.3.5 #5. Lists
- H1 L2901: 4.3.6 Conclusion
- H1 L2909: Summary
- H1 L2923: Reading Python 5code: Part 2
- H1 L2925: This chapter covers
- H1 L2938: 5.1 Top 10 programming features you need to know: Part 2
- H1 L2942: 5.1.1 #6. Loops
- H1 L3090: Copilot explanations can be wrong
- H1 L3094: (continued)
- H1 L3124: 5.1.2 #7. Indentation
- H1 L3157: Listing 5.6 Function to determine the larger of two values
- H1 L3406: 5.1.3 #8. Dictionaries
- H1 L3479: 5.1.4 #9. Files
- H1 L3597: More than one way to solve a programming problem
- H1 L3603: 5.1.5 #10. Modules
- H1 L3609: Modules in Python
- H1 L3674: Summary
- H1 L3685: Testing and prompt 6engineering
- H1 L3687: This chapter covers
- H1 L3696: 6.1 Why it is crucial to test code
- H1 L3706: 6.2 Closed-box and open-box testing
- H1 L3714: 6.2.1 Closed-box testing
- H1 L3724: Shorthand for expressing test cases
- H1 L3778: Incorrect input testing
- H1 L3782: (continued)
- H1 L3786: 6.2.2 How do we know which test cases to use?
- H1 L3798: 6.2.3 Open-box testing
- H1 L3836: 6.3 How to test your code
- H1 L3840: 6.3.1 Testing using the Python prompt
- H1 L3853: 6.3.2 Testing in your Python file (we won’t be doing it this way)
- H1 L3857: 6.3.3 doctest
- H1 L3996: Test cases are not automatically run by Copilot
- H1 L4002: 6.4 Revisiting the cycle of designing functions with Copilot
- H1 L4040: 6.5 Full testing example
- H1 L4044: 6.5.1 Finding the most students we can add to a row
- H1 L4170: 6.5.2 Improving the prompt to find a better solution
- H1 L4227: 6.5.3 Testing the new solution
- H1 L4302: 6.6 Another full testing example—Testing with files
- H1 L4322: 6.6.1 What tests should we run?
- H1 L4352: 6.6.2 Creating the function
- H1 L4384: 6.6.3 Testing the function
- H1 L4427: 6.6.4 Common challenges with doctest
- H1 L4497: Summary
- H1 L4504: Problem decomposition
- H1 L4506: This chapter covers
- H1 L4520: 7.1 Problem decomposition
- H1 L4528: 7.2 Small examples of top-down design
- H1 L4578: 7.3 Authorship identification
- H1 L4582: Excerpt 1
- H1 L4586: Excerpt 2
- H1 L4604: Machine Learning
- H1 L4608: 7.4 Authorship identification using top-down design
- H1 L4624: 7.5 Breaking down the process subproblem
- H1 L4652: 7.5.1 Figuring out the signature for the mystery book
- H1 L4656: Features related to the structure of the author’s sentences
- H1 L4668: Features related to the author’s word selection
- H1 L4715: Av erage word length
- H1 L4725: Different words div ided by total words
- H1 L4757: Words used exactly once div ided by total words
- H1 L4765: Av erage number of words per sentence
- H1 L4779: Av erage sentence complexity
- H1 L4819: Figuring out each known signature
- H1 L4859: Finding closest known signature
- H1 L4894: 7.6 Summary of our top-down design
- H1 L4927: 7.7 Implementing our functions
- H1 L4935: 7.7.1 clean\_word
- H1 L5019: 7.7.2 average\_word\_length
- H1 L5090: 7.7.3 different\_to\_total
- H1 L5127: 7.7.4 exactly\_once\_to\_total
- H1 L6906: Copy to clipboard
- H1 L6908: Paste from clipboard
- H1 L6928: Create a Tkinter window
- H1 L6931: Hide the window
- H1 L6934: Copy to clipboard
- H1 L6940: Paste from clipboard
- H1 L6958: Copy to clipboard
- H1 L6965: Paste from clipboard
- H1 L6985: Copy to clipboard
- H1 L6988: Paste from clipboard
- H1 L7219: Open the PDF files to be merged
- H1 L7223: Create a PDF reader object for each file
- H1 L7227: Create a PDF writer object
- H1 L7230: Loop through the pages of each PDF and add them to the writer object
- H1 L7239: Write the merged PDF to a file
- H1 L7243: Close the input and output files
- H1 L7268: Call pdftk to merge the PDF files
- H1 L7597: Merge the two PDF files
- H1 L7777: Replace the source and destination paths with your own
- H1 L7781: Copy the file
- H1 L7808: Replace these file paths with the actual file paths of the .png files
- H1 L7809: you want to compare
- H1 L7863: 9.5.2 Top-down design
- H1 L7903: 9.5.3 Writing the tool
- H1 L8002: Summary
- H1 L8010: Making some games
- H1 L8012: This chapter covers
- H1 L8022: 10.1 Game programs
- H1 L8051: 10.2 Adding randomness
- H1 L8140: 10.3 Example 1: Bulls and Cows
- H1 L8144: 10.3.1 How the game works
- H1 L8154: Wordle
- H1 L8170: 10.3.2 Top-down design
- H1 L8223: 10.3.3 Parameters and return types
- H1 L8229: Using parameters and variables to avoid magic numbers
- H1 L8270: 10.3.4 Implementing our functions
- H1 L8274: random\_string
- H1 L8356: get\_guess

## 自动抽取的教学卡片

> [!todo] 本书候选大节共有 208 个，本文件先生成前 120 个教学卡片；完整层级见上方索引。

### 1. EA R Z AI- I-Assisted Python Programming

- 原始层级：H1，源行：L6
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- With GitHub Copilot and ChatGPT
- Illustration of a historical figure wearing a dark hat and patterned garment (no text or symbols visible)
- The function design cycle with Copilot, augmented to include debugging

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- With GitHub Copilot and ChatGPT
- Illustration of a historical figure wearing a dark hat and patterned garment (no text or symbols visible)
- The function design cycle with Copilot, augmented to include debugging
- `mermaid` 代码块，源行 27：graph TD / A["Define the desired behavior of the function"] --> B["Write a prompt that describes the… / B --> C["Allow Copilot to generate the code"] / C --> D["Examine the code, is it reasonable?"]
- 图片引用：`images/352a672410a0cbec92764a2a339cf78a02c67434b7a9af74052914edaf8e1959.jpg`
- 图片引用：`images/4affca9c6dd1c4f7934c75c90f4709277a85c51534832425932b6150e002951a.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「EA R Z AI- I-Assisted Python Programming」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 2. Learn AI-Assisted Python Programming

- 原始层级：H1，源行：L48
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- With GitHub Copilot and ChatGPT
- For online information and ordering of this and other Manning books, please visit www.manning.com. The publisher offers discounts on this book when ordered in quantity.
- For more information, please contact

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- With GitHub Copilot and ChatGPT
- 图片引用：`images/f1f7e5361e8d99d1388bb13aaa79936801dbad6dba69463fbd6db6dd7e4220a0.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Learn AI-Assisted Python Programming」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 3. Introducing AI-assisted programming with Copilot 1

- 原始层级：H1，源行：L114
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 1.1 How we talk to computers 2 Making it a little easier 2 ■ Making it a lot easier 3 1.2 About the technology 3 Copilot, your AI Assistant 4 ■ How Copilot works behind the scenes—in 30 seconds 5 1.3 How Copilot changes…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 1.1 How we talk to computers 2 Making it a little easier 2 ■ Making it a lot easier 3 1.2 About the technology 3 Copilot, your AI Assistant 4 ■ How Copilot works behind the scenes—in 30 seconds 5 1.3 How Copilot changes…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Introducing AI-assisted programming with Copilot 1」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 4. Getting started with Copilot 13

- 原始层级：H1，源行：L128
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- 2.1 Time to set up your computer to start learning 14 Overview of the software in your programming environment 14 2.2 Getting your system set up 15 2.3 Working with Copilot in Visual Studio Code 16 Set up your working f…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 2.1 Time to set up your computer to start learning 14 Overview of the software in your programming environment 14 2.2 Getting your system set up 15 2.3 Working with Copilot in Visual Studio Code 16 Set up your working f…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Getting started with Copilot 13」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 5. Designing functions 33

- 原始层级：H1，源行：L138
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 3.1 Functions 34 The components of a function 35 ■ Using a function 37 3.2 Benefits of functions 38 3.3 Roles of functions 40 3.4 What’s a reasonable task for a function? 43 Attributes of good functions 43 ■ Examples of…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 3.1 Functions 34 The components of a function 35 ■ Using a function 37 3.2 Benefits of functions 38 3.3 Roles of functions 40 3.4 What’s a reasonable task for a function? 43 Attributes of good functions 43 ■ Examples of…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Designing functions 33」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 6. Reading Python code: Part 1 60

- 原始层级：H1，源行：L147
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 4.1 Why we need to read code 61 4.2 Asking Copilot to explain code 63 4.3 Top 10 programming features you need to know: Part 1 66 #1. Functions 67 ■ #2. Variables 67 ■ #3. Conditionals 69 #4. Strings 72 ■ #5. Lists 74 ■…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 4.1 Why we need to read code 61 4.2 Asking Copilot to explain code 63 4.3 Top 10 programming features you need to know: Part 1 66 #1. Functions 67 ■ #2. Variables 67 ■ #3. Conditionals 69 #4. Strings 72 ■ #5. Lists 74 ■…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Reading Python code: Part 1 60」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 7. Reading Python code: Part 2 78

- 原始层级：H1，源行：L157
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 5.1 Top 10 programming features you need to know:
- #6. Loops 79 ■ #7. Indentation 83 ■ #8. Dictionaries 90
- #9. Files 91 ■ #10. Modules 94

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Reading Python code: Part 2 78」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 8. Testing and prompt engineering 99

- 原始层级：H1，源行：L169
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 6.1 Why it is crucial to test code 99
- 6.2 Closed-box and open-box testing 100
- Closed-box testing 101 ■ How do we know which test cases to use? 103 ■ Open-box testing 103

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Testing using the Python prompt 105 ■ Testing in your Python file (we won’t be doing it this way) 105 ■ doctest 105
- Finding the most students we can add to a row 110 ■ Improving the prompt to find a better solution 113 ■ Testing the new solution 114
- 6.6 Another full testing example—Testing with files 116

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Testing and prompt engineering 99」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 9. Problem decomposition 124

- 原始层级：H1，源行：L195
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 17 周

#### 核心重点

- 7.2 Small examples of top-down design 125
- 7.3 Authorship identification 127
- 7.4 Authorship identification using top-down design 129

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Problem decomposition 124」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 10. CY Debugging and better understanding your code 158

- 原始层级：H1，源行：L224
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 8.1 What causes errors (bugs)? 159 8.2 How to find the bug 160 Using print statements to learn about the code behavior 160 Using VS Code’s debugger to learn about the code behavior 162
- 8.3 How to fix a bug (once found) 169
- Asking Copilot to fix your bug via chat 169 ■ Giving Copilot

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Asking Copilot to fix your bug via chat 169 ■ Giving Copilot
- a new prompt for the whole function 171 ■ Giving Copilot a
- targeted prompt for part of a function 171 ■ Modifying the code

#### 备课摘取建议

- 若用于 PPT，可把本节作为「CY Debugging and better understanding your code 158」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 11. Automating tedious tasks 182

- 原始层级：H1，源行：L251
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 9.1 Why programmers make tools 183 9.2 How to use Copilot to write tools 184 9.3 Example 1: Cleaning up email text 184 Conversing with Copilot 185 ■ Writing the tool to clean up email 189
- 9.4 Example 2: Adding cover pages to PDF files 192
- Conversing with Copilot 194 ■ Writing the tool 198

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 9.1 Why programmers make tools 183 9.2 How to use Copilot to write tools 184 9.3 Example 1: Cleaning up email text 184 Conversing with Copilot 185 ■ Writing the tool to clean up email 189
- 9.4 Example 2: Adding cover pages to PDF files 192
- Conversing with Copilot 194 ■ Writing the tool 198

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Automating tedious tasks 182」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 12. Making some games 216

- 原始层级：H1，源行：L270
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 10.3 Example 1: Bulls and Cows 220
- How the game works 220 ■ Top-down design 222
- Parameters and return types 224 ■ Implementing our

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 10.3 Example 1: Bulls and Cows 220

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Making some games 216」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 13. Future directions 248

- 原始层级：H1，源行：L294
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- Flipped interaction pattern 250 ■ Persona pattern 253
- 11.2 Limitations and future directions 255
- Where Copilot (currently) struggles 255 ■ Is Copilot a new

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Where Copilot (currently) struggles 255 ■ Is Copilot a new

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Future directions 248」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 14. foreword

- 原始层级：H1，源行：L312
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- It’s an awesome time to learn programming. Why? Let me use an analogy to explain.
- I like to make my own bread. I make it more frequently, and more reliably, when I use my stand mixer to knead the dough compared to kneading it by hand. Maybe you’d say that’s lazy. I’d say it makes me more productive a…
- Sadly, until recently, when learning programming, you had no equivalent of a stand mixer or grammar check to support you. And there are lots of tedious things to learn and remember when you start programming.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Good news! As of spring 2023, radically new and (we think) effective support is finally here. You are about to learn programming with one of the most exciting human task supporters so far this century: artificial intell…
- So, congratulations! Whether you have never done any programming or whether you started to learn before and got frustrated… we think you will find learning to program with Copilot transformative and will allow you to en…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「foreword」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 15. acknowledgments

- 原始层级：H1，源行：L330
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 17 周

#### 核心重点

- Writing a book about technology in flux was new for us. Each day of writing started with us reading the new articles, opinion pieces, and capabilities of LLMs. Early plans had to be scrapped or revised. New ideas presen…
- In particular, we thank our Development Editor Rebecca Johnson for her expertise, wisdom, and support.
- Rebecca provided insightful feedback, constructive criticism, and creative suggestions that have greatly improved the quality and clarity of our work. Rebecca was supportive and encouraging and helped us manage book tim…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「acknowledgments」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 16. introduction

- 原始层级：H1，源行：L346
- 推荐周次：第 3 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- Software is essential today. It’s hard to think of any industry where software isn’t changing practically everything about how work is done. Manufacturing needs software to monitor production and shipping, let alone the…
- The result has been that more people than ever want to learn how to program. We’re not just talking about the computer science, computer engineering, and data science majors at universities who have been in a perpetual…
- Despite the desire to learn programming, there are decades of research in our field (computing education) that have identified many reasons for why learning to write software is hard. Even after you figure out how to so…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Despite the desire to learn programming, there are decades of research in our field (computing education) that have identified many reasons for why learning to write software is hard. Even after you figure out how to so…
- But what if we could talk to computers in a better way? A way that doesn’t require us to know all the detailed syntax rules that trip up most novices. That era has just begun thanks to AI assistants like Copilot that of…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「introduction」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 17. AI assistants change how programming is done

- 原始层级：H1，源行：L356
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- As educators, the opportunity to help people learn to write software is instantly apparent. Why should students spend so much time fighting with syntax when writing code from scratch when the code suggested by an AI ass…
- Be warned that this doesn’t mean that writing software is now just easy and that we can entirely offload the skill of programming onto the AI. Instead, the skills to write good software are evolving. Skills like problem…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「AI assistants change how programming is done」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 18. Audience

- 原始层级：H1，源行：L364
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- The second is the student who is considering a career in software engineering or programming and wants to learn how to write software. They want to learn the basics and start creating interesting software, without the t…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Audience」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 19. What we expect from you

- 原始层级：H1，源行：L370
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- This book requires no background whatsoever in programming. If you learned some programming and forgotten or it didn’t go well the first time, we think this is a great place to resume your learning.
- This book does require basic computer literacy. This means you should be comfortable installing software, copying files between folders, and opening files on your computer. If you don’t have those skills, you could stil…
- You’ll also need a computer where you have permission to install software so you can follow along and apply the ideas we’re learning. Any Windows, Mac, or Linux personal computer or laptop will work.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「What we expect from you」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 20. What you will be able to do after reading this book

- 原始层级：H1，源行：L378
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- In this book, we’re going to teach you how to use Copilot to write Python code. We’ll teach you how to identify whether that code does what you want, and what to do when it doesn’t. We’ll teach you enough about Python t…
- We won’t, however, teach you how to program in Python entirely from scratch. You’ll be in a good position to learn to do that with other resources following this book if you like—but for many tasks, as we will show you,…
- We don’t know exactly what it will look like to be a professional programmer or software engineer in light of AI coding assistants. That role is already changing and will change further as the AI technology improves. Fo…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- In this book, we’re going to teach you how to use Copilot to write Python code. We’ll teach you how to identify whether that code does what you want, and what to do when it doesn’t. We’ll teach you enough about Python t…
- The good news is that learning how to program using Copilot will make you capable of writing basic software to address common needs. The software will be more complex than what we typically teach in an introductory cour…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「What you will be able to do after reading this book」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 21. The challenge in working with AI assistants

- 原始层级：H1，源行：L390
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「The challenge in working with AI assistants」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 22. Why we wrote this book

- 原始层级：H1，源行：L394
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- Both of us have been professors for over a decade and programmers for a decade longer than that. Our care for our students’ success led us to become researchers studying how students learn computing and how to improve t…
- We’ve also had students in our office hours who struggled to learn how to program, even when we are employing best practices in teaching computing. These are intelligent students who want to learn, but who are tripped u…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- We’ve also had students in our office hours who struggled to learn how to program, even when we are employing best practices in teaching computing. These are intelligent students who want to learn, but who are tripped u…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Why we wrote this book」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 23. Warning: beware of elitism

- 原始层级：H1，源行：L400
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- One of the saddest things we see in our classes at our universities is students intimidating other students. We’ve heard students in our introductory Python programming courses try to show off how they already learned t…
- All of this, in our opinion, is unproductive and unfortunate posturing that pushes people away from the field. A comic we both enjoy called XKCD, captured the ludicrousness of this posturing well in “Real Programmers” […
- The reason we’re talking about this unfortunate aspect of our field is we know what some people will say about learning to program with Copilot. They’ll say that to learn to write software, you have to learn how to writ…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- The reason we’re talking about this unfortunate aspect of our field is we know what some people will say about learning to program with Copilot. They’ll say that to learn to write software, you have to learn how to writ…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Warning: beware of elitism」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 24. How this book is organized: a roadmap

- 原始层级：H1，源行：L410
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- This book is divided into 11 chapters. We recommend that you read this book from beginning to end, rather than skipping around. That’s because most chapters introduce skills that will be assumed in later chapters:
- Chapter 1 describes what AI code assistants are, how they work, and why they are irrevocably changing how programming is done. It also explores the concerns we need to keep in mind when using AI coding assistants. Chapt…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Chapter 1 describes what AI code assistants are, how they work, and why they are irrevocably changing how programming is done. It also explores the concerns we need to keep in mind when using AI coding assistants. Chapt…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「How this book is organized: a roadmap」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 25. Source code downloads

- 原始层级：H1，源行：L427
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- For many books about programming, the reader types the code exactly as the author has written it in order to accomplish a task with code. Our book is different because, as described earlier, the code we get back from Co…
- This book contains many examples of source code both in numbered listings and in line with normal text. In both cases, source code is formatted in a fixed-width font like this to separate it from ordinary text. Comments…
- In many cases, the original source code has been reformatted; we’ve added line breaks and reworked indentation to accommodate the available page space in the book. In rare cases, even this was not enough, and listings i…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- For many books about programming, the reader types the code exactly as the author has written it in order to accomplish a task with code. Our book is different because, as described earlier, the code we get back from Co…
- This book contains many examples of source code both in numbered listings and in line with normal text. In both cases, source code is formatted in a fixed-width font like this to separate it from ordinary text. Comments…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Source code downloads」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 26. Software/hardware requirements

- 原始层级：H1，源行：L435
- 推荐周次：第 3 周, 第 11 周, 第 17 周

#### 核心重点

- You’ll need access to any Windows, Mac, or Linux computer on which you have permission to install software. As we discuss in further detail in chapter 2, you’ll need to install the Python software, the Visual Studio Cod…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- You’ll need access to any Windows, Mac, or Linux computer on which you have permission to install software. As we discuss in further detail in chapter 2, you’ll need to install the Python software, the Visual Studio Cod…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Software/hardware requirements」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 27. liveBook discussion forum

- 原始层级：H1，源行：L439
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Purchase of Learn AI-Assisted Python Programming with GitHub Copilot and ChatGPT includes free access to liveBook, Manning’s online reading platform. Using liveBook’s exclusive discussion features, you can attach commen…
- Manning’s commitment to our readers is to provide a venue where a meaningful dialogue between individual readers and between readers and the author can take place. It is not a commitment to any specific amount of partic…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Purchase of Learn AI-Assisted Python Programming with GitHub Copilot and ChatGPT includes free access to liveBook, Manning’s online reading platform. Using liveBook’s exclusive discussion features, you can attach commen…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「liveBook discussion forum」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 28. about the authors

- 原始层级：H1，源行：L445
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Dr. Daniel Zingaro is an Associate Teaching Professor at University of Toronto. He has taught introductory Python programming to thousands of students over the past 15 years and wrote the Python textbook that is current…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「about the authors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 29. About the technical editor

- 原始层级：H1，源行：L451
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Peter Morgan is the founder of the AI consulting company Deep Learning Partnership based in London (www.deeplp.com). He has an advanced degree in physics along with an MBA. He has been working in AI for the past ten yea…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「About the technical editor」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 30. about the cover illustration

- 原始层级：H1，源行：L455
- 推荐周次：第 3 周, 第 11 周, 第 17 周

#### 核心重点

- The figure on the cover of Learn AI-Assisted Python Programming with GitHub Copilot and ChatGPT is “Prussien de Silésie,” or “Prussian from Silesia,” taken from a collection by Jacques Grasset de Saint-Sauveur, publishe…
- In those days, it was easy to identify where people lived and what their trade or station in life was just by their dress. Manning celebrates the inventiveness and initiative of the computer business with book covers ba…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- The figure on the cover of Learn AI-Assisted Python Programming with GitHub Copilot and ChatGPT is “Prussien de Silésie,” or “Prussian from Silesia,” taken from a collection by Jacques Grasset de Saint-Sauveur, publishe…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「about the cover illustration」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 31. Introducing AI-assisted 1programming with Copilot

- 原始层级：H1，源行：L461
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Introducing AI-assisted 1programming with Copilot」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 32. This chapter covers

- 原始层级：H1，源行：L463
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- ¡ How AI assistants change how new programmers learn ¡ Why programming is never going to be the same ¡ How AI assistants like Copilot work ¡ How Copilot solves introductory programming problems ¡ Possible perils of AI-a…
- In this chapter, we’ll talk about how humans communicate with computers. We’ll introduce you to your AI assistant, GitHub Copilot, an amazing tool that uses artificial intelligence (AI) to help people write software. Mo…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- ¡ How AI assistants change how new programmers learn ¡ Why programming is never going to be the same ¡ How AI assistants like Copilot work ¡ How Copilot solves introductory programming problems ¡ Possible perils of AI-a…
- In this chapter, we’ll talk about how humans communicate with computers. We’ll introduce you to your AI assistant, GitHub Copilot, an amazing tool that uses artificial intelligence (AI) to help people write software. Mo…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This chapter covers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 33. 1.1 How we talk to computers

- 原始层级：H1，源行：L473
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Would you be happy if we started by asking you to read and understand the code below?1
- That monstrosity prints out the numbers from 0 to 9. It’s written using code in assembly language, a low-level programming language. Low-level programming languages, as you can see, are not languages that humans can eas…
- No one wants to write programs like that, but especially in the past, it was sometimes necessary. Programmers could use it to define exactly what they wanted the computer to do, down to individual instructions. This lev…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- No one wants to write programs like that, but especially in the past, it was sometimes necessary. Programmers could use it to define exactly what they wanted the computer to do, down to individual instructions. This lev…
- `asm` 代码块，源行 477：section .text / global _start / _start: / mov ecx, 10

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.1 How we talk to computers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 34. 1.1.1 Making it a little easier

- 原始层级：H1，源行：L505
- 推荐周次：第 3 周, 第 4 周, 第 17 周

#### 核心重点

- Okay, no more of that. Let’s move on. Would you be happier reading this code below?
- This code is in the Python language, which is what many programmers use these days. Unlike assembly language, which is a low-level language, Python is considered a highlevel language because it’s much closer to natural…
- 9. The second line is printing something. It’s not too hard to believe that this program, just like the assembly language monstrosity, is supposed to print the numbers from 0 to 9. Unfortunately, something is wrong with…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- The holy grail of communicating with a computer is to do so in a natural language such as English. We’ve been talking to computers using various programming languages over the past 70 years, not because we want to but b…
- `python` 代码块，源行 509：for num in range(0, 9): / print(num)

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.1.1 Making it a little easier」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 35. 1.1.2 Making it a lot easier

- 原始层级：H1，源行：L522
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Using an AI assistant, we can now ask for what we want in English and have the computer code written for us in response. To get a correct Python program that does actually print the numbers from 0 to 9, we can ask our A…
- \# Output the numbers from 0 to 9
- Copilot might respond to this prompt by generating something like this:

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Using an AI assistant, we can now ask for what we want in English and have the computer code written for us in response. To get a correct Python program that does actually print the numbers from 0 to 9, we can ask our A…
- Copilot might respond to this prompt by generating something like this:
- Unlike the example we showed you before, this piece of Python code actually works!

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.1.2 Making it a lot easier」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 36. 1.2 About the technology

- 原始层级：H1，源行：L538
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 7 周, 第 11 周, 第 17 周

#### 核心重点

- We’ll use two main technologies in this book: Python and GitHub Copilot.
- Python is a programming language. It’s a way to communicate with a computer. People use it to write all kinds of programs that do useful things, like games, interactive websites, visualizations, apps for file organizati…
- There are other programming languages, like Java, C++, Rust, and many others. Copilot works with those, too, but at the time of this writing, it works really well with Python. Python code is a lot easier to write compar…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- We’ll use two main technologies in this book: Python and GitHub Copilot.
- There are other programming languages, like Java, C++, Rust, and many others. Copilot works with those, too, but at the time of this writing, it works really well with Python. Python code is a lot easier to write compar…
- Computers don’t actually know how to read and run Python code. The only thing computers can understand is something called machine code, which looks even more ridiculous than assembly code, because it is the binary repr…
- `mermaid` 代码块，源行 553：graph TD / A["Your Python program: for i in range (10): print(i)"] --> B["The Python compiler"] / B --> C["Converts your program into an intermediate form called bytecode"] / C --> D["Python bytecode"]
- 图片引用：`images/15feb69feed24e189ef661a422ce3a77b2538ed5cca5b9e0ef4b7ff6f1733f84.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.2 About the technology」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 37. 1.2.1 Copilot, your AI Assistant

- 原始层级：H1，源行：L567
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- What is an AI assistant? An AI assistant is an artificial intelligence (AI) agent that helps you get work done. Maybe you have an Amazon Alexa device at home, or an iPhone with Siri—these are AI assistants. They help yo…
- Copilot is an AI assistant with a specific job: it converts English into computer programs. (It can also do a whole lot more, as we will soon see.) There are other AI assistants like Copilot, including CodeWhisperer, Ta…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Copilot is an AI assistant with a specific job: it converts English into computer programs. (It can also do a whole lot more, as we will soon see.) There are other AI assistants like Copilot, including CodeWhisperer, Ta…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.2.1 Copilot, your AI Assistant」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 38. 1.2.2 How Copilot works behind the scenes—in 30 seconds

- 原始层级：H1，源行：L573
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- You can think of Copilot as a layer between you and the computer program you’re writing. Instead of writing the Python directly, you simply describe the program you want in words—this is called a prompt—and Copilot gene…
- The brains behind Copilot is a fancy computer program called a large language model, or LLM. An LLM stores information about relationships between words, including which words make sense in certain contexts, and uses th…
- Imagine that we asked you what the next word should be in this sentence: “The person opened the .” There are many words that you could fill in here, like “door” or “box” or “conversation,” but there are also many words…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- You can think of Copilot as a layer between you and the computer program you’re writing. Instead of writing the Python directly, you simply describe the program you want in words—this is called a prompt—and Copilot gene…
- The brains behind Copilot is a fancy computer program called a large language model, or LLM. An LLM stores information about relationships between words, including which words make sense in certain contexts, and uses th…
- Notice that we didn’t say anything about Copilot having an understanding of what it is doing. It just uses the current context to keep writing code. Keep this in mind throughout your journey: only we know whether the co…
- `mermaid` 代码块，源行 588：graph TD / A["You type a prompt like: # Output the numbers from 0 to 9"] --> B["Copilot sends your p… / B --> C["OpenAI's GPT large language model interprets your prompt and generates some code… / C --> D["for i in range (10): print(i)"]
- 图片引用：`images/8d2b1554295a7844cc217872d4b24d01163158d4a65c7a238cf709faa0205b85.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.2.2 How Copilot works behind the scenes—in 30 seconds」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 39. 1.3 How Copilot changes how we learn to program

- 原始层级：H1，源行：L600
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- To illustrate how learning to program changes in the presence of an AI assistant, we want to show you how powerful Copilot is at solving a programming task typically given to students in the middle of a programming cour…
- When learning how to program in the past, learners often spent most of their time working with the syntax and basic structure of programs. Writing a program from scratch (line by line), like the one we’ll show you next,…
- “Write a program that will read the amount of rainfall for each day. A negative value of rainfall should be rejected since this is invalid and inadmissible. The program should print out the number of valid recorded days…

#### 公式与符号

- rainfall = 0
- total_rainfall = 0
- num_rainy_days = 0
- num_valid_days = 0
- max_rainfall = 0

#### 例子 / 代码 / 图表

- To illustrate how learning to program changes in the presence of an AI assistant, we want to show you how powerful Copilot is at solving a programming task typically given to students in the middle of a programming cour…
- If you have tried to learn to program before, this kind of problem statement may be familiar to you, and you may have struggled to solve such a problem. But now, if we give this exact prompt to Copilot, we get the follo…
- Listing 1.1 Copilot code that solves the classic rainfall problem
- `python` 代码块，源行 611：rainfall = 0 / total_rainfall = 0 / num_rainy_days = 0 / num_valid_days = 0
- `python` 代码块，源行 627：num_valid_days += 1 / total_rainfall += rainfall / if rainfall > 0: / num_rainy_days += 1

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.3 How Copilot changes how we learn to program」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 40. 1.4 What else can Copilot do for us?

- 原始层级：H1，源行：L648
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- As we’ve seen, we can use Copilot to write Python code for us starting from an English description of what we want. Programmers use the word syntax to refer to the symbols and words that are valid in a given language. S…
- Such questions abound, and let’s be honest: it’s uninteresting stuff. Who cares about this when all we want to do is write a program to make something happen? Copilot can help free us from the tedium of syntax. We see t…
- But that’s not all Copilot can do. Here are some associated—and no less important— tasks Copilot can help us with:

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- As we’ve seen, we can use Copilot to write Python code for us starting from an English description of what we want. Programmers use the word syntax to refer to the symbols and words that are valid in a given language. S…
- Such questions abound, and let’s be honest: it’s uninteresting stuff. Who cares about this when all we want to do is write a program to make something happen? Copilot can help free us from the tedium of syntax. We see t…
- But that’s not all Copilot can do. Here are some associated—and no less important— tasks Copilot can help us with:

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.4 What else can Copilot do for us?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 41. 1.5 Risks and challenges when using Copilot

- 原始层级：H1，源行：L660
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- Now that we’re all pumped up about getting Copilot to write code for us, we need to talk about the dangers inherent in using AI assistants. See references [2] and [3] for elaboration on some of these points.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Now that we’re all pumped up about getting Copilot to write code for us, we need to talk about the dangers inherent in using AI assistants. See references [2] and [3] for elaboration on some of these points.

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.5 Risks and challenges when using Copilot」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 42. 1.6 The skills we need

- 原始层级：H1，源行：L673
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- If Copilot can write our code, explain it, and fix bugs in it, are we just done? Do we just tell Copilot what to do and celebrate our pure awesomeness?
- No. It’s true that some of the skills that programmers rely upon (writing correct syntax, for example) will decrease in importance. But other skills remain critical. For example, you cannot throw a huge task at Copilot…
- Other skills, believe it or not, may take on even more importance with Copilot. Testing code has always been a critical task in writing code that works. We know a lot about testing code written by humans, because we kno…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- If Copilot can write our code, explain it, and fix bugs in it, are we just done? Do we just tell Copilot what to do and celebrate our pure awesomeness?
- No. It’s true that some of the skills that programmers rely upon (writing correct syntax, for example) will decrease in importance. But other skills remain critical. For example, you cannot throw a huge task at Copilot…
- Other skills, believe it or not, may take on even more importance with Copilot. Testing code has always been a critical task in writing code that works. We know a lot about testing code written by humans, because we kno…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.6 The skills we need」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 43. 1.7 Societal concerns about AI code assistants like Copilot

- 原始层级：H1，源行：L685
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- There’s societal uncertainty right now about AI code assistants like Copilot. We thought we’d end the chapter with a few questions and our current answers. Perhaps you’ve been wondering about some of these questions you…
- Q: Are there going to be fewer tech and programming jobs now that we have Copilot?
- A: Probably not. What we do expect to change is the nature of these jobs. For example, we see Copilot as being able to help with many tasks typically associated with entrylevel programming jobs. This doesn’t mean that e…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- There’s societal uncertainty right now about AI code assistants like Copilot. We thought we’d end the chapter with a few questions and our current answers. Perhaps you’ve been wondering about some of these questions you…
- Q: Are there going to be fewer tech and programming jobs now that we have Copilot?
- A: Probably not. What we do expect to change is the nature of these jobs. For example, we see Copilot as being able to help with many tasks typically associated with entrylevel programming jobs. This doesn’t mean that e…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1.7 Societal concerns about AI code assistants like Copilot」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 44. Summary

- 原始层级：H1，源行：L703
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- ¡ Copilot is an AI assistant, which is an artificial intelligence (AI) agent that helps you get work done. ¡ Copilot changes how humans interact with computers, and the way that we write programs. Copilot changes the fo…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- ¡ Copilot is an AI assistant, which is an artificial intelligence (AI) agent that helps you get work done. ¡ Copilot changes how humans interact with computers, and the way that we write programs. Copilot changes the fo…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Summary」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 45. Getting started 2with Copilot

- 原始层级：H1，源行：L711
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Getting started 2with Copilot」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 46. This chapter covers

- 原始层级：H1，源行：L713
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- ¡ Setting up Python, VS Code, and Copilot on your system ¡ Introducing the Copilot design process ¡ Copilot’s value for a basic data processing task
- This chapter will help you start working with Copilot on your own machine and familiarize you with how to interact with it. After you are set up with Copilot, we’ll ask that you follow along with our examples when you c…
- Once you’ve set up Copilot, we’ll walk through a fun example that showcases the power of Copilot in solving standard tasks, you’ll see how to interact with Copilot, and you’ll learn how we can write software without wri…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- ¡ Setting up Python, VS Code, and Copilot on your system ¡ Introducing the Copilot design process ¡ Copilot’s value for a basic data processing task
- This chapter will help you start working with Copilot on your own machine and familiarize you with how to interact with it. After you are set up with Copilot, we’ll ask that you follow along with our examples when you c…
- Once you’ve set up Copilot, we’ll walk through a fun example that showcases the power of Copilot in solving standard tasks, you’ll see how to interact with Copilot, and you’ll learn how we can write software without wri…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This chapter covers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 47. 2.1 Time to set up your computer to start learning

- 原始层级：H1，源行：L723
- 推荐周次：第 3 周, 第 7 周, 第 11 周, 第 17 周

#### 核心重点

- Learning how to write software requires that you perform the task of writing software, not just reading about it. If this were a book on how to play guitar, would you keep reading it without ever trying to play the guit…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1 Time to set up your computer to start learning」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 48. 2.1.1 Overview of the software in your programming environment

- 原始层级：H1，源行：L729
- 推荐周次：第 3 周, 第 11 周, 第 17 周

#### 核心重点

- To set up and use Copilot easily, we’ll install the software editing tools used by novices and software engineers alike. The tools you will use are GitHub, Copilot, Python, and Visual Studio Code. Of course, if you alre…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- To set up and use Copilot easily, we’ll install the software editing tools used by novices and software engineers alike. The tools you will use are GitHub, Copilot, Python, and Visual Studio Code. Of course, if you alre…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1.1 Overview of the software in your programming environment」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 49. GitHub account

- 原始层级：H1，源行：L733
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- GitHub is an industry-standard tool for developing, maintaining, and storing software. We won’t use GitHub in this book, however. We’re signing up for GitHub simply because you’ll need an account to access Copilot. Sign…
- You might ask why they charge for the service, and there’s a good answer. It’s expensive to build the GPT3 models (imagine thousands of computers running for a year to build the model), and GitHub incurs costs by provid…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- GitHub is an industry-standard tool for developing, maintaining, and storing software. We won’t use GitHub in this book, however. We’re signing up for GitHub simply because you’ll need an account to access Copilot. Sign…
- You might ask why they charge for the service, and there’s a good answer. It’s expensive to build the GPT3 models (imagine thousands of computers running for a year to build the model), and GitHub incurs costs by provid…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「GitHub account」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 50. Python

- 原始层级：H1，源行：L739
- 推荐周次：第 3 周, 第 4 周, 第 17 周

#### 核心重点

- Really any programming language would have worked for this book, but we picked Python because it is one of the most popular programming languages in the world and is the language we teach in our introductory courses at…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Really any programming language would have worked for this book, but we picked Python because it is one of the most popular programming languages in the world and is the language we teach in our introductory courses at…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Python」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 51. Visual Studio Code (VS Code)

- 原始层级：H1，源行：L743
- 推荐周次：第 3 周, 第 11 周, 第 17 周

#### 核心重点

- You can use any text editor to program. However, if you want a nice programming environment where you can write code, easily get suggestions from Copilot, and run your code, VS Code is our preferred tool. VS Code is use…
- For VS Code to work for this book, you’ll need to install a few extensions that enable working with Python and using Copilot, but one of the great things about VS Code is that it’s easy to install those extensions.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- You can use any text editor to program. However, if you want a nice programming environment where you can write code, easily get suggestions from Copilot, and run your code, VS Code is our preferred tool. VS Code is use…
- For VS Code to work for this book, you’ll need to install a few extensions that enable working with Python and using Copilot, but one of the great things about VS Code is that it’s easy to install those extensions.

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Visual Studio Code (VS Code)」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 52. 2.2 Getting your system set up

- 原始层级：H1，源行：L749
- 推荐周次：第 3 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- This is a four-step process. To streamline this chapter, we’re just providing the main steps for this process. However, there are more detailed instructions available in the following locations:
- Visit GitHub’s documentation at https://docs.github.com/en/copilot/getting -started-with-github-copilot. The website for this book(https://www.manning.com/books/learn-ai-assisted -python-programming) provides detailed i…
- The primary steps you’ll need to accomplish are as follows:

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Visit GitHub’s documentation at https://docs.github.com/en/copilot/getting -started-with-github-copilot. The website for this book(https://www.manning.com/books/learn-ai-assisted -python-programming) provides detailed i…
- 1 Set up your GitHub account and sign up for Copilot:
- a Go to https://github.com/signup and sign up for a GitHub account. b Go into your settings in GitHub and enable Copilot. This is the point where you’ll either need to verify you are a student or sign up for the 30-day…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.2 Getting your system set up」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 53. 2.3 Working with Copilot in Visual Studio Code

- 原始层级：H1，源行：L783
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- Now that you have your system set up, let’s get acquainted with the VS Code interface shown in figure 2.1. (You may need to click the Explorer icon in the middle/top left to have this same view.) The following regions a…
- ¡ Output and Terminal Panel—This is the area of the interface for seeing the output of your code or any errors that have occurred. It has the tabs Problems, Output, Debug Console, and Terminal. We will primarily use the…
- We highlighted the Copilot logo in the bottom right of figure 2.1 because you should see this symbol (or similar) if you set up Copilot properly in the previous section.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Now that you have your system set up, let’s get acquainted with the VS Code interface shown in figure 2.1. (You may need to click the Explorer icon in the middle/top left to have this same view.) The following regions a…
- We highlighted the Copilot logo in the bottom right of figure 2.1 because you should see this symbol (or similar) if you set up Copilot properly in the previous section.
- Activity Bar Side Bar Editor Panes EXPLORER CHAPTER 2 HelloWorld.py Welcome HelloWorld.py HelloWorld.py 1 # output "Hello World" 2 3 print("Hello World") PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL Tasks Output and Terminal…
- 图片引用：`images/bf16dd967b95a1f4a54a9d4516d701efdc22295c53318c2c5946db26608c8f6b.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3 Working with Copilot in Visual Studio Code」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 54. 2.3.1 Set up your working folder

- 原始层级：H1，源行：L822
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- In the top of the Activity Bar on the left in VS Code, you will find Explorer as the top icon. After you click Explorer, it should say “No Folder Open”. Click the button to open folder and select a folder on your comput…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.1 Set up your working folder」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 55. File not found or file missing errors

- 原始层级：H1，源行：L826
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- If you ever receive an error that says you are missing a file, take heart: these are the kinds of errors that everyone makes. They can be really annoying when writing software. It could be that you just didn’t put the f…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- If you ever receive an error that says you are missing a file, take heart: these are the kinds of errors that everyone makes. They can be really annoying when writing software. It could be that you just didn’t put the f…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「File not found or file missing errors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 56. 2.3.2 Check to see if your setup is working properly

- 原始层级：H1，源行：L830
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- Let’s check to see if we’ve set up everything properly and that Copilot is working. To do this, start by creating a new file to hold our program. You do this by going to File > New File (figure 2.2), then selecting Pyth…
- File Edit Selection View Go Run Terminal Help New Text File Ctrl+N New File... Ctrl+Alt+Windows+N New Window Ctrl+Shift+N Open File... Ctrl+O Open Folder... Ctrl+K Ctrl+O Open Workspace from File... Open Recent Add Fold…
- Figure 2.2 How to create a new file in VS Code

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Let’s check to see if we’ve set up everything properly and that Copilot is working. To do this, start by creating a new file to hold our program. You do this by going to File > New File (figure 2.2), then selecting Pyth…
- Figure 2.2 How to create a new file in VS Code
- Figure 2.3 Select to create the New File as a Python File
- 图片引用：`images/18a1be5a4e91c12db7262e965a2d4772c583ceaab8b83104132a553d99657529.jpg`
- 图片引用：`images/030b87558df4a7df17a7aaf4cc5d700e31802a16bf569f22bdc8fff5506d192f.jpg`
- 图片引用：`images/0efe35f44bdeb8bf95002aa5f831c1d44af91b761c457680d3ae597a2ef64615.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.2 Check to see if your setup is working properly」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 57. output "Hello Copilot" to the screen ← The prompt

- 原始层级：H1，源行：L907
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- print("Hello Copilot") ← The code produced by Copilot
- If you are seeing different code than this, it’s because of something we mentioned in the introduction: Copilot is nondeterministic so you may see different code than us. We mention this because sometimes Copilot makes…
- You might think this slight difference (no parentheses around "Hello Copilot") wouldn’t matter, but it does. Before Python 3, this was the correct syntax for a print statement and when Python 3 was introduced, it switch…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- print("Hello Copilot") ← The code produced by Copilot
- If you are seeing different code than this, it’s because of something we mentioned in the introduction: Copilot is nondeterministic so you may see different code than us. We mention this because sometimes Copilot makes…
- You might think this slight difference (no parentheses around "Hello Copilot") wouldn’t matter, but it does. Before Python 3, this was the correct syntax for a print statement and when Python 3 was introduced, it switch…
- `txt` 代码块，源行 920：# output "Hello Copilot" to the screen / print("Hello Copilot")
- `txt` 代码块，源行 931：> & C:/Users/YOURNAME/AppData/Local/Programs/Python/Python311/Python.exec:/Users/YOURNAME…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「output "Hello Copilot" to the screen ← The prompt」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 58. 2.4 Addressing common Copilot challenges

- 原始层级：H1，源行：L941
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- It may seem early in your experience with Copilot to start talking about common challenges with Copilot, but you may have already run into challenges when writing your first program. You’ll certainly encounter some of t…
- In our time working with Copilot, we’ve run into a few common challenges. These challenges will likely decrease with time as Copilot improves, but they were still problems at the time of this writing. Although the chall…
- Table 2.1 Common challenges working with Copilot

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- It may seem early in your experience with Copilot to start talking about common challenges with Copilot, but you may have already run into challenges when writing your first program. You’ll certainly encounter some of t…
- In our time working with Copilot, we’ve run into a few common challenges. These challenges will likely decrease with time as Copilot improves, but they were still problems at the time of this writing. Although the chall…
- Table 2.1 Common challenges working with Copilot

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.4 Addressing common Copilot challenges」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 59. 2.5 Our first programming problem

- 原始层级：H1，源行：L951
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- The goal of this next section is twofold: (1) for you to see the workflow of interacting with Copilot and (2) for you to gain an appreciation of how powerful Copilot can be by seeing it solve a complicated task fairly e…
- In our next chapter, we’ll talk through the workflow with Copilot in more detail, but you’ll generally use the following steps when authoring code with Copilot:
- 1 Write a prompt to Copilot using comments (#) or docstrings ("""). 2 Let Copilot generate code for you. 3 Check to see whether the code is correct by reading through it and by testing. a If it works, move to step 1 for…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- The goal of this next section is twofold: (1) for you to see the workflow of interacting with Copilot and (2) for you to gain an appreciation of how powerful Copilot can be by seeing it solve a complicated task fairly e…
- In our next chapter, we’ll talk through the workflow with Copilot in more detail, but you’ll generally use the following steps when authoring code with Copilot:
- 1 Write a prompt to Copilot using comments (#) or docstrings ("""). 2 Let Copilot generate code for you. 3 Check to see whether the code is correct by reading through it and by testing. a If it works, move to step 1 for…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.5 Our first programming problem」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 60. 2.5.1 Showcasing Copilot’s value in a data processing task

- 原始层级：H1，源行：L967
- 推荐周次：第 3 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- We want to start with some basic data processing as this is something that many of you have likely done in your personal or professional lives. To find a dataset, we went to a great website called Kaggle [4], which has…
- Let’s get started by downloading the dataset from www.kaggle.com/datasets/ dtrade84/nfl-offensive-stats-2019-2022.
- To download the dataset, you will have to sign up for a Kaggle account. If you don’t want to create the account, it’s okay to just read through this section without using VS Code and Copilot to generate the code yoursel…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- To download the dataset, you will have to sign up for a Kaggle account. If you don’t want to create the account, it’s okay to just read through this section without using VS Code and Copilot to generate the code yoursel…
- The nfl\_offensive\_stats.csv file is something known as a comma separated value text file (see figure 2.4 for a portion of the file). This is a standard format for storing data. It has a header row at the top that expl…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.5.1 Showcasing Copilot’s value in a data processing task」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 61. Step 1: How many passing yards did Aaron Rodgers throw in 2019–2022

- 原始层级：H1，源行：L993
- 推荐周次：第 3 周, 第 11 周, 第 17 周

#### 核心重点

- Let’s start by exploring what is stored in this file. To preview what is in the file, you can look at the Kaggle webpage for these stats under “Detail”, open it in VS Code, or open it in spreadsheet software like Micros…
- game\_id,player\_id,position ,player,team,pass\_cmp,pass\_att,pass\_yds,…
- There are more columns, but these have all we need to perform our first task. We know now that there’s a column for players and a column for passing yards. Aaron Rodgers is a player who gets passing yards in each game t…

#### 公式与符号

- reader = csv.reader(f)
- nfl_data = list(reader)
- passing_yards = 0

#### 例子 / 代码 / 图表

- Let’s start by exploring what is stored in this file. To preview what is in the file, you can look at the Kaggle webpage for these stats under “Detail”, open it in VS Code, or open it in spreadsheet software like Micros…
- The """ at the top and the bottom are surrounding something called a docstring. Docstrings are an alternative way of commenting (similar to text starting with #). They are commonly used for describing functions (see cha…
- First, for the purpose of reading this book, we want to remind you that the prompt is displayed differently than what Copilot produces. This is intentional so you can tell what we wrote (and you should write) and what C…
- `python` 代码块，源行 1003：""" / open the csv file called "nfl_offensive_stats.csv" and read in the csv data from the file / """
- `python` 代码块，源行 1011：import csv / with open('nfl_offensive_stats.csv', 'r') as f: ← Notice the file name. / reader = csv.reader(f) / nfl_data = list(reader)
- `txt` 代码块，源行 1024：In the data we just read in, the fourth column is the player and the 8th column is the pa…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Step 1: How many passing yards did Aaron Rodgers throw in 2019–2022」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 62. Reminder: Copilot is nondeterministic

- 原始层级：H1，源行：L1038
- 推荐周次：第 3 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- Remember from the Introduction that Copilot is nondeterministic, so what Copilot gives you may not match what it gives us. This is going to be a challenge for the rest of the book: What do you do if you get a wrong resu…
- When we run this code (recall how to Run Code from figure 2.1), we get the result 13852,which is the correct answer. (We double-checked the answer, but if you are familiar with football, you can likely use estimates to…
- What we want you to take from this example (and the rest of the chapter):

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Remember from the Introduction that Copilot is nondeterministic, so what Copilot gives you may not match what it gives us. This is going to be a challenge for the rest of the book: What do you do if you get a wrong resu…
- When we run this code (recall how to Run Code from figure 2.1), we get the result 13852,which is the correct answer. (We double-checked the answer, but if you are familiar with football, you can likely use estimates to…
- What we want you to take from this example (and the rest of the chapter):

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Reminder: Copilot is nondeterministic」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 63. Step 2: How well did all the quarterbacks do ov er that time period?

- 原始层级：H1，源行：L1055
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- Listing 2.1 Copilot’s code to analyze the top quarterbacks
- print the sum of the passing yards sorted by sum of passing yards in descending order
- Notice that we gave Copilot three prompts. The first was to handle the input data, the second was to process the data, and the third was to output the response. This cycle of input data, process data, provide output is…

#### 公式与符号

- data = list(csv.reader(f))
- passing_yards = {}
- for player in sorted(passing_yards, key=passing_yards.get, reverse=True):
- for player in sorted(passing_yards, key=passing_yards.get, reverse=True):
- for player in sorted(passing_yards, key=passing_yards.get, reverse=True):

#### 例子 / 代码 / 图表

- Listing 2.1 Copilot’s code to analyze the top quarterbacks
- Notice that we gave Copilot three prompts. The first was to handle the input data, the second was to process the data, and the third was to output the response. This cycle of input data, process data, provide output is…
- Looking at the results from Copilot, we have to point out that we’ve taught programming for years and this is pretty impressive. We might ask students to solve something like this on a final exam in our college-level cl…
- `python` 代码块，源行 1060：""" / open the csv file called "nfl_offensive_stats.csv" and / read in the csv data from the file / """
- `python` 代码块，源行 1100：else: / # add the player to the dictionary / passing_yards[row[3]] = int(row[7])
- `text` 代码块，源行 1108：for player in sorted(passing_yards, key=passing_yards.get, reverse=True): / print(player, passing_yards[player])

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Step 2: How well did all the quarterbacks do ov er that time period?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 64. Step 3: Let’s plot these stats so we can compare them better

- 原始层级：H1，源行：L1169
- 推荐周次：第 3 周, 第 7 周, 第 11 周, 第 17 周

#### 核心重点

- Let’s drive home our key point that Copilot is a powerful tool by asking it to go even one step farther. The printout of all the quarterback stats is likely a useful analysis for some purposes. But a visual plot might b…
- At the end of the code we just wrote, add the following comment:
- The following listing shows the code Copilot gave us in response to our prompt.

#### 公式与符号

- players = []
- yards = []
- yards = np.array(yards)
- players = np.array(players)
- players = players[np.argsort(yards)]

#### 例子 / 代码 / 图表

- Let’s drive home our key point that Copilot is a powerful tool by asking it to go even one step farther. The printout of all the quarterback stats is likely a useful analysis for some purposes. But a visual plot might b…
- The following listing shows the code Copilot gave us in response to our prompt.
- Listing 2.2 Code given by Copilot to plot our data about quarterbacks
- `python` 代码块，源行 1175：""" / plot the players by their number of passing yards only for players with more than 4000 pa… / """
- `python` 代码块，源行 1184：import matplotlib.pyplot as plt / import numpy as np / # create a list of players / players = []
- `python` 代码块，源行 1201：# create a numpy array of the passing yards / yards = np.array(yards) / # create a numpy array of the players / players = np.array(players)

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Step 3: Let’s plot these stats so we can compare them better」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 65. Python modules

- 原始层级：H1，源行：L1225
- 推荐周次：第 3 周, 第 6 周, 第 7 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- Python modules expand the capability of the programming language. There are many modules in Python, and they can help you do anything from data analysis to creating websites to writing video games. You can recognize whe…
- To fix this error, you’ll need to install matplotlib. The good news is that Python has made it easy to install new packages. Go to the Terminal at the bottom right of VS Code and type:
- NOTE For some operating systems, you may need to use pip3 rather than pip. On Windows machines, we recommend using pip if you followed our installation instructions. On Mac or Linux machines, we recommend using pip3.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- When you run this command, you’ll see that a bunch of modules are installed, including numpy (the next module this code wants to use). (matplotlib requires Python modules of its own, so it installs all the modules you n…
- Figure 2.5 The plot produced by the code in listing 2.2
- In this bar graph, we see the y-axis is the number of passing yards, and the x-axis is the player’s name. The players are sorted from fewest yards (with a minimum of 4,000) to most yards. Admittedly, it’s not perfect be…
- 图片引用：`images/cf238e7cb0610cd09bc9d960a15eb934990c4f245f15136e2e5adbe453ebad69.jpg`
- 表格行：| Category | Value |
- 表格行：|---|---|
- 表格行：| Jones | 4000 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Python modules」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 66. Summary

- 原始层级：H1，源行：L1289
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 17 周

#### 核心重点

- You installed Python and VS Code and set up Copilot so you can work along with the book and start writing code yourself! ¡ The VS Code interface has areas for file management, code editing, and running code that will be…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- You installed Python and VS Code and set up Copilot so you can work along with the book and start writing code yourself! ¡ The VS Code interface has areas for file management, code editing, and running code that will be…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Summary」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 67. Designing functions

- 原始层级：H1，源行：L1298
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Designing functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 68. This chapter covers

- 原始层级：H1，源行：L1300
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- ¡ Functions in Python and their role in designing software ¡ Reasonable tasks for Copilot to solve ¡ The standard workflow when interacting with Copilot Examples of writing good functions using Copilot
- One of the hardest challenges for programming novices is to know what a reasonable task is to give to Copilot so that it finds a good solution. If you give it too big a task, it will often fail in spectacular ways that…
- This question is important for our use of Copilot but goes far beyond it. Human programmers struggle with complexity, too. If experienced software engineers try to write code to solve a problem that’s too complex withou…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- ¡ Functions in Python and their role in designing software ¡ Reasonable tasks for Copilot to solve ¡ The standard workflow when interacting with Copilot Examples of writing good functions using Copilot
- One of the hardest challenges for programming novices is to know what a reasonable task is to give to Copilot so that it finds a good solution. If you give it too big a task, it will often fail in spectacular ways that…
- This question is important for our use of Copilot but goes far beyond it. Human programmers struggle with complexity, too. If experienced software engineers try to write code to solve a problem that’s too complex withou…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This chapter covers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 69. 3.1 Functions

- 原始层级：H1，源行：L1315
- 推荐周次：第 3 周, 第 11 周, 第 17 周

#### 核心重点

- Before we can learn about the details of writing a function, we need some insight into their purpose in software. Functions are small tasks that help accomplish larger tasks, which, in turn, help solve larger tasks, and…
- Suppose that you’ve found a word search puzzle in the newspaper that you’d like to solve (see figure 3.1 for an example puzzle). In these kinds of puzzles, you’re looking for each word in the word list. The words can be…
- R M E L L L D I L A Z K B F W H F M O Z G L Z C B D T U C N G S L S H A Y Y O F U N C T I O N T F A H S I L T A S K O C H N H J O H E L L O C A Y F M P I P W L B T R J L N S J N E Z Y Z Z I T

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Before we can learn about the details of writing a function, we need some insight into their purpose in software. Functions are small tasks that help accomplish larger tasks, which, in turn, help solve larger tasks, and…
- Suppose that you’ve found a word search puzzle in the newspaper that you’d like to solve (see figure 3.1 for an example puzzle). In these kinds of puzzles, you’re looking for each word in the word list. The words can be…
- Figure 3.1 Example word search puzzle

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1 Functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 70. 3.1.1 The components of a function

- 原始层级：H1，源行：L1339
- 推荐周次：第 3 周, 第 4 周, 第 17 周

#### 核心重点

- The origin of the name function goes back to math where functions define the output of something based on an input. For example, if $\operatorname { f } ( \mathbf { x } ) = \mathbf { X } ^ { 2 } ;$ , we can say that whe…
- As software engineers, we also like to think of functions as promises or contracts. If there is a function called “larger” and we’re told that it takes two numbers and gives us the larger of the two, we have faith that…
- Every function in Python has a function header (also called a signature), which is the first line of code of the function. Given their ubiquitous nature, we’ll want to read and write function headers. The function heade…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- The origin of the name function goes back to math where functions define the output of something based on an input. For example, if $\operatorname { f } ( \mathbf { x } ) = \mathbf { X } ^ { 2 } ;$ , we can say that whe…
- In chapter 2, we wrote # comments to tell Copilot what to do. We can continue to use that approach if we want Copilot to generate a function. For example, we can use comments to ask Copilot to write a function that tell…
- As with the code in the last chapter, we just wrote the comments to prompt Copilot to give us the code. The function header has three main components: the keyword, which tells Python that this is a function; the name of…
- `python` 代码块，源行 1349：# write a function that returns the larger of two numbers / # input is two numbers / # output is the larger of the two numbers / def larger(num1, num2):

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1.1 The components of a function」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 71. Docstrings explain function behavior

- 原始层级：H1，源行：L1371
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Docstrings are how Python functions are described by programmers. They follow the function header and begin and end with three quotation marks.
- By writing the header and docstring, you’ll make it easier for Copilot to generate the right code. In the header, you will be the one deciding on the name of the function and will provide the names of each parameter tha…
- Here’s what the alternate approach would look like when writing that same larger function:

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- By writing the header and docstring, you’ll make it easier for Copilot to generate the right code. In the header, you will be the one deciding on the name of the function and will provide the names of each parameter tha…
- Notice that we wrote the function header as well as the docstring, and Copilot supplied the body of the function.
- `python` 代码块，源行 1379：def larger(num1, num2): / """ / num1 and num2 are two numbers. / Return the larger of the two numbers.

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Docstrings explain function behavior」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 72. 3.1.2 Using a function

- 原始层级：H1，源行：L1393
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Once we have a function, how do we use it? Thinking back to our f(x) = x2 analogy, how do we give the function a value of 6 for x so that it returns 36? Let’s see how to do this with code by using that larger function w…
- The way to use a function is to call it. Calling a function means to invoke the function on specific values of parameters. These parameter values are called arguments. Each value in Python has a type, and we need to tak…
- Here, we ask Copilot to call the function, store the result in a variable, and then print the result:

#### 公式与符号

- result = larger(3, 5)

#### 例子 / 代码 / 图表

- The way to use a function is to call it. Calling a function means to invoke the function on specific values of parameters. These parameter values are called arguments. Each value in Python has a type, and we need to tak…
- Here, we ask Copilot to call the function, store the result in a variable, and then print the result:
- So, when you see those parentheses right after a name, it means there’s a function call. Calling functions as we did here will be important to our workflow with Copilot, particularly in how we test functions to see if t…
- `txt` 代码块，源行 1401：# call the larger function with the values 3 and 5 / # store the result in a variable called result / # then print result / result = larger(3, 5)

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1.2 Using a function」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 73. 3.2 Benefits of functions

- 原始层级：H1，源行：L1421
- 推荐周次：第 3 周, 第 8 周, 第 10 周, 第 17 周

#### 核心重点

- We already mentioned that functions are critical in performing problem decomposition. Beyond problem decomposition, functions are valuable in software for a number of other reasons, including
- Avoid repetition—Programmers (and, we’d argue, humans in general) aren’t very excited about solving the same problem over and over. If I write a function that can correctly compute the area of a circle once, I don’t nee…
- These benefits are huge for programmers. Programming languages haven’t always had functions. But even before they did, programmers did their best to use other features to mimic functions. They were ugly hacks (Google “g…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.2 Benefits of functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 74. 3.3 Roles of functions

- 原始层级：H1，源行：L1440
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- Functions are used in many different roles in programming. At a high level, programs are functions that (often) call other functions. Critically, all programs, including Python programs, originate with a single function…
- As an example, let’s use the code in the following listing. We wrote this code, not Copilot, because no one would ever want to write this code for anything useful outside teaching. It’s just for demonstrating how functi…
- Listing 3.1 Python code to demonstrate how Python handles function calls

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- As an example, let’s use the code in the following listing. We wrote this code, not Copilot, because no one would ever want to write this code for anything useful outside teaching. It’s just for demonstrating how functi…
- In figure 3.2, we provide a diagram of how the code in listing 3.1 would be executed by the computer. We’ve intentionally provided an example that has many function calls to tie together what we just learned. Again, thi…
- Continuing this example, the next line of the code executed will be the line that prints friend. The next line calls funct3 which prints a period (.) and then returns back to its caller.
- `python` 代码块，源行 1447：def funct1(): / print("there") / funct2() / print("friend")
- `lua` 代码块，源行 1464：print("I'm") / funct4() / funct3() / print("")
- `ignorefile` 代码块，源行 1474：Hi / there / my / friend
- 图片引用：`images/05795e433956c67fa0f422eccbf263c24feeb2cd151ddff0538b210ac907fc05.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.3 Roles of functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 75. 3.4 What’s a reasonable task for a function?

- 原始层级：H1，源行：L1608
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- There’s no clear rule for what makes a good function, but there are some intuitions and recommendations we can share. Make no mistake, though: identifying good functions is a skill that takes time and practice. To help…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.4 What’s a reasonable task for a function?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 76. 3.4.1 Attributes of good functions

- 原始层级：H1，源行：L1612
- 推荐周次：第 3 周, 第 7 周, 第 11 周, 第 17 周

#### 核心重点

- Here are some guidelines that we believe will help you see what makes a good function:

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.4.1 Attributes of good functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 77. 3.4.2 Examples of good (and bad) leaf functions

- 原始层级：H1，源行：L1623
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Here are examples of good leaf functions:
- ¡ Compute the volume of a sphere—Given the sphere’s radius, return its volume. Find the largest number in a list—Given a list, return the largest value. Check whether a list contains a specific value—Given a list and a…
- Here are examples of bad leaf functions and our reasons for why they are bad:

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.4.2 Examples of good (and bad) leaf functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 78. 3.5 The cycle of design of functions with Copilot

- 原始层级：H1，源行：L1642
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- Designing functions with Copilot involves the following cycle of steps (see figure 3.3):
- 1 Determine the desired behavior of the function. 2 Write a prompt that describes the function as clearly as possible. 3 Allow Copilot to generate the code. 4 Read through the code to see if it seems reasonable. 5 Test…
- a If the code is correct after multiple tests, move on. b If the code is incorrect, move to step 2 and edit the prompt.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Designing functions with Copilot involves the following cycle of steps (see figure 3.3):
- 1 Determine the desired behavior of the function. 2 Write a prompt that describes the function as clearly as possible. 3 Allow Copilot to generate the code. 4 Read through the code to see if it seems reasonable. 5 Test…
- a If the code is correct after multiple tests, move on. b If the code is incorrect, move to step 2 and edit the prompt.
- `mermaid` 代码块，源行 1660：graph TD / A["Define the desired behavior of the function"] --> B["Write a prompt that describes the… / B --> C["Allow Copilot to generate the code"] / C --> D["Examine the code to see if it is reasonable"]
- 图片引用：`images/1c87e14b21e8724910ec57c5a42c667aa1eb186d0fb6a47a473cfb52a6150859.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.5 The cycle of design of functions with Copilot」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 79. 3.6 Examples of creating good functions with Copilot

- 原始层级：H1，源行：L1675
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- In this section, we’re going to write a bunch of functions with Copilot. We’ll code them entirely in Copilot to help you see the cycle of function design we just described. Although our goal in this chapter isn’t to hel…
- Many of the functions we’re about to work on are unrelated to each other. For example, we’ll start with a function about stock share prices and move to functions about strong passwords. You typically wouldn’t store unre…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- In this section, we’re going to write a bunch of functions with Copilot. We’ll code them entirely in Copilot to help you see the cycle of function design we just described. Although our goal in this chapter isn’t to hel…
- Many of the functions we’re about to work on are unrelated to each other. For example, we’ll start with a function about stock share prices and move to functions about strong passwords. You typically wouldn’t store unre…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6 Examples of creating good functions with Copilot」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 80. 3.6.1 Dan’s stock pick

- 原始层级：H1，源行：L1681
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- Dan is an investor in a stock called AAAPL. He purchased 10 shares for \$15 each. Now, each of those shares is worth \$17. Dan would like to know how much money he has made on the stock.
- Remember that we want to make our function as general as possible. If the only thing our function does is calculate this exact AAAPL situation, it wouldn’t be that useful in general. Sure, it would help Dan right now, b…
- A useful general function here would take three parameters, all of which are numbers. The first parameter is the number of shares purchased, the second is the share price when the shares were purchased, and the third is…

#### 公式与符号

- price_difference = current_share_price - purchase_share_price

#### 例子 / 代码 / 图表

- Adding our docstring, here is the full prompt we provide to Copilot:
- After typing that prompt, go to the next line and press the Tab key. Copilot will fill in the code for the function. Don’t worry that the code gets indented: the code of functions is supposed to be indented, and, in fac…
- Here’s what we got from Copilot:
- `python` 代码块，源行 1695：def money_made(num_shares, purchase_share_price, current_share_price): / """ / num_shares is the number of shares of a stock that we purchased. / purchase_share_price is the price of each of those shares.
- `txt` 代码块，源行 1734：>>> money_made(10, 15, 17)
- `python` 代码块，源行 1742：PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL / Type "help", "copyright", "credits" or "license" for more information. / >>> def money_made(num_shares, purchase_share_price, current_share_price): / ... """
- 图片引用：`images/37407807bdfb4d8c6e6fae93da51249b5bf31e918ccdb0b604099c8fce93501f.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.1 Dan’s stock pick」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 81. 3.6.2 Leo’s password

- 原始层级：H1，源行：L1793
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Leo is signing up for a new social network website called ProgrammerBook. He wants to make sure that his password is strong.
- Leo starts with a modest definition of what it means for a password to be strong: it’s strong if it’s not the word password and not the word qwerty. (Those are terrible passwords, for sure, but in reality, we have to do…
- Unlike our previous functions in this chapter, we’re not dealing with numbers here. The parameter, the password to check, is text. And the return value is supposed to indicate some yes/no result. We need new types!

#### 公式与符号

- num_upper = 0
- num_num = 0
- num_special = 0

#### 例子 / 代码 / 图表

- Alright! We’re ready to prompt Copilot. For functions that return bool (True/False) values, we usually name the function as has\_x, or is\_x, or using some other verb that implies a true/false result:
- In response, here’s what Copilot wrote for us:
- Well, technically True is correct, but, wow, is Leo a bad password. We should really have done better with our definition of a strong password. Let’s change our prompt to give a more reasonable definition of what it mea…
- `python` 代码块，源行 1805：def is_strong_password(password): / """ / A strong password is not the word 'password' / and is not the word 'qwerty'.
- `txt` 代码块，源行 1817：return password != 'password' and password != 'qwerty'
- `txt` 代码块，源行 1825：>>> is_strong_password('password') / False / >>> is_strong_password('qwerty') / False

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.2 Leo’s password」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 82. Importing modules

- 原始层级：H1，源行：L1943
- 推荐周次：第 3 周, 第 7 周, 第 11 周, 第 17 周

#### 核心重点

- There are a number of useful modules available in Python. We saw how powerful matplotlib is in chapter 2. But for Python code to take advantage of a module, we have to import that module. You might ask why we don’t have…
- Let’s add import string at the top of our code:
- That last one is True—it’s a strong password!—because it has the \$ punctuation added to it.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- `python` 代码块，源行 1951：def is_strong_password(password): / """ / A strong password has at least one uppercase character, / at least one number, and at least one punctuation.
- `txt` 代码块，源行 1958：Return True if the password is a strong password, False if not. / """ / return any(char.isupper() for char in password) and \ / any(char.isdigit() for char in password) and \
- `txt` 代码块，源行 1968：>>> is_strong_password('Leo') / False / >>> is_strong_password('N3w Y0rk J375') / False

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Importing modules」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 83. 3.6.3 Getting a strong password

- 原始层级：H1，源行：L1981
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Now that we have a function that tells us whether a password is strong or not, let’s write a function that obtains a strong password from the user. It will ask again and again for a password until the user types a stron…
- What should the header for such a function look like? Well, it’s going to ask the user for a password, but we won’t have a password parameter. In fact, we won’t have any parameters at all, because the function doesn’t n…
- We get the following code from Copilot as a result:

#### 公式与符号

- password = input("Enter a strong password: ")
- password = input("Enter a strong password: ")

#### 例子 / 代码 / 图表

- What should the header for such a function look like? Well, it’s going to ask the user for a password, but we won’t have a password parameter. In fact, we won’t have any parameters at all, because the function doesn’t n…
- We get the following code from Copilot as a result:
- That while keyword creates another kind of loop, this one continuing as long as the entered password is not strong. Copilot is also smart enough to call our earlier is strong\_password function to determine what counts…
- `python` 代码块，源行 1989：def get_strong_password(): / """ / Keep asking the user for a password until it is a strong password, and return that strong… / """
- `python` 代码块，源行 1998：password = input("Enter a strong password: ") / while not is_strong_password(password): / password = input("Enter a strong password: ") / return password
- `txt` 代码块，源行 2009：>>> get_strong_password() / Enter a strong password: Leo / Enter a strong password: N3w Y0rk J375 / Enter a strong password: N3w Y0rk J375$

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.3 Getting a strong password」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 84. 3.6.4 Scrabble scoring

- 原始层级：H1，源行：L2019
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- One of Dan’s favorite board games is Scrabble. Have you played it? If not, all you need to know is that you have some tiles in your hand, each with a letter on it, and your goal is to form a word using any combination o…
- To calculate the score for a word, we add up the scores for each of its letters. For example, the score for zap would be 14. That’s because z is worth 10, a is worth 1, and p is worth 3.
- Dan would like a function that, given a word, tells him how many points that word is worth. OK, so we need a function that takes a word (which is just one parameter). Let’s try this prompt, where we’ve included the numb…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- One of Dan’s favorite board games is Scrabble. Have you played it? If not, all you need to know is that you have some tiles in your hand, each with a letter on it, and your goal is to form a word using any combination o…
- To calculate the score for a word, we add up the scores for each of its letters. For example, the score for zap would be 14. That’s because z is worth 10, a is worth 1, and p is worth 3.
- Dan would like a function that, given a word, tells him how many points that word is worth. OK, so we need a function that takes a word (which is just one parameter). Let’s try this prompt, where we’ve included the numb…
- `python` 代码块，源行 2027：def num_points(word): / """ / Each letter is worth the following points: / a, e, i, o, u, l, n, s, t, r: 1 point

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.4 Scrabble scoring」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 85. Getting Copilot to suggest code may require pressing Tab or Enter

- 原始层级：H1，源行：L2046
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- We find that Copilot will sometimes pause in giving suggestions until you press a key to help prompt it. As mentioned in table 2.1, if you are giving it comments, it will sometimes just want to give you more comments as…
- Finally, after doing that a few times, the entire code unfurls, and we get the following:
- Notice that all of the letters of the alphabet are accounted for here, and the number of points that each category is worth is on the following line. We’ll discuss this overall kind of decision structure in the next cha…

#### 公式与符号

- points = 0
- points = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1,

#### 例子 / 代码 / 图表

- We find that Copilot will sometimes pause in giving suggestions until you press a key to help prompt it. As mentioned in table 2.1, if you are giving it comments, it will sometimes just want to give you more comments as…
- Let’s try a couple more. In each case, calculate by hand what you expect the answer to be—that way you’ll know if the code is doing the right thing:
- There are many ways to write correct code for a function. If you press Ctrl–Enter and look at the Copilot suggestions, you may see different types of code. It doesn’t necessarily mean that one of these types is right an…
- `python` 代码块，源行 2052：points = 0 / for char in word: / if char in "aeioulnstr": / points += 1
- `txt` 代码块，源行 2076：>>> num_points('zap') / 14
- `erlang` 代码块，源行 2083：>>> num_points('pack') / 12 / >>> num_points('quack') / 20

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Getting Copilot to suggest code may require pressing Tab or Enter」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 86. 3.6.5 The best word

- 原始层级：H1，源行：L2108
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Let’s continue with the Scrabble theme. Suppose that Dan has a bunch of words that he can make right now, but he doesn’t know which one will give him the most points. Should he make the word zap, pack, or quack? It woul…
- How many parameters should we have in such a function? Your first instinct may be 3, one for each of the 3 words in our options. But that wouldn’t be very flexible. After all, what if we want to know the best of five wo…
- The trick is to use a function with one (yes, just one!) parameter, which is a list of words. Just like numbers and strings and dictionaries, a list is a type supported by Python. It’s incredibly useful because it allow…

#### 公式与符号

- best_word = ""
- best_points = 0
- points = num_points(word)
- best_word = word
- best_points = points

#### 例子 / 代码 / 图表

- We can prompt Copilot like this to get the function that we want:
- How will Copilot know how many points each word is worth? Well, it can call that num\_ points function that we wrote in the previous section!
- Here’s the code that Copilot gives us.
- `python` 代码块，源行 2118：def best_word(word_list): / """ / word_list is a list of words. / Return the word worth the most points.
- `python` 代码块，源行 2130：best_word = "" / best_points = 0 / for word in word_list: / points = num_points(word)
- `txt` 代码块，源行 2143：>>> best_word('zap', 'pack', 'quack')

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.5 The best word」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 87. Summary

- 原始层级：H1，源行：L2165
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Summary」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 88. Reading Python

- 原始层级：H1，源行：L2187
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Reading Python」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 89. 4code: Part 1

- 原始层级：H1，源行：L2189
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4code: Part 1」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 90. This chapter covers

- 原始层级：H1，源行：L2191
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- ¡ Why knowing how to read code is important ¡ How to ask Copilot to explain code ¡ Using functions to break a problem into smaller subproblems ¡ Using variables to hang on to values ¡ Using if-statements to make decisio…
- In chapter 3, we used Copilot to write several functions for us. What are they good for? Maybe our money\_made function could be part of a stock trading system. Maybe our is\_strong\_password function could be used as p…
- However, we believe that you need to understand at a high level what code does. Because this will require some time to learn, we’ve split this discussion over two chapters. In this chapter, we’ll explain why reading cod…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- ¡ Why knowing how to read code is important ¡ How to ask Copilot to explain code ¡ Using functions to break a problem into smaller subproblems ¡ Using variables to hang on to values ¡ Using if-statements to make decisio…
- In chapter 3, we used Copilot to write several functions for us. What are they good for? Maybe our money\_made function could be part of a stock trading system. Maybe our is\_strong\_password function could be used as p…
- However, we believe that you need to understand at a high level what code does. Because this will require some time to learn, we’ve split this discussion over two chapters. In this chapter, we’ll explain why reading cod…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This chapter covers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 91. 4.1 Why we need to read code

- 原始层级：H1，源行：L2205
- 推荐周次：第 3 周, 第 12 周, 第 17 周

#### 核心重点

- When we talk about reading code, what we mean is understanding what code does by looking at it. There are two such levels of understanding.
- The first level is being able to understand, line by line, what a program will do. This often involves tracing the values of variables as the code runs to determine exactly what the code is doing at each step.
- The second level is determining the overall purpose of a program. As professors, we often test students at this level with questions that ask them to “explain in plain English.”

#### 公式与符号

- best_word = ""
- best_points = 0
- points = num_points(word)
- best_word = word
- best_points = points

#### 例子 / 代码 / 图表

- At the end of these two chapters, we want you to do both levels of interpreting code produced by Copilot. We’ll start focusing on that line-by-line understanding, but toward the end of the chapter, you’ll start being ab…
- A tracing description of what this program does would be a description of each line. For example, we would say that we’re defining a function called best\_word. We have a variable called best\_word that we start off as…
- Before we get to it, we need to be clear about the level of depth that we’re striving for. We’re not going to teach you every nuance of every line of code. Doing so would revert us back to the traditional way programmin…
- `python` 代码块，源行 2218：def best_word(word_list): / """ / word_list is a list of words. / Return the word worth the most points.

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.1 Why we need to read code」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 92. 4.2 Asking Copilot to explain code

- 原始层级：H1，源行：L2249
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- In chapter 2, when setting up your computer to use GitHub Copilot, you installed the GitHub Copilot Labs extension to Visual Studio Code (VS Code). This experimental extension is changing rapidly and is designed to offe…
- We suspect that, soon, the Copilot Labs extension, or parts of it, will be folded into the main Copilot extension. If that happens, the specific steps we give here may vary somewhat, and in that case, we encourage you t…
- For now, with the Copilot Labs extension installed, you can highlight some code that you want Copilot to describe to you. Let’s try this with our best\_word function (figure 4.1).

#### 公式与符号

- best_word = ""
- best_points = 0
- points = num_points(word)
- best_word = word
- best_points = points

#### 例子 / 代码 / 图表

- In chapter 2, when setting up your computer to use GitHub Copilot, you installed the GitHub Copilot Labs extension to Visual Studio Code (VS Code). This experimental extension is changing rapidly and is designed to offe…
- We suspect that, soon, the Copilot Labs extension, or parts of it, will be folded into the main Copilot extension. If that happens, the specific steps we give here may vary somewhat, and in that case, we encourage you t…
- For now, with the Copilot Labs extension installed, you can highlight some code that you want Copilot to describe to you. Let’s try this with our best\_word function (figure 4.1).
- `python` 代码块，源行 2282：def best_word(word_list): / """ / word_list is a list of words. / Return the word worth the most points.
- `python` 代码块，源行 2302：GITHUB COPILOT LABS / EXPLAIN / def best_word(word_list): / """
- 图片引用：`images/e9cc7825a93aa26079e4e8bc9969c820b51ebb85ac0cdcd4cbacf2c13a3f84e2.jpg`
- 图片引用：`images/b9e0f4e20c9310f8715f24579ed8adb871dd95d750c1204c019eabd8086f79f1.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.2 Asking Copilot to explain code」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 93. Copilot Labs explanations can be wrong

- 原始层级：H1，源行：L2362
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- As with the code produced by Copilot, the explanations from Copilot Labs can be wrong, too. You might be thinking, “Wait, what’s the value of a tool to understand code if it can be wrong?!” First, let us say that we agr…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- As with the code produced by Copilot, the explanations from Copilot Labs can be wrong, too. You might be thinking, “Wait, what’s the value of a tool to understand code if it can be wrong?!” First, let us say that we agr…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Copilot Labs explanations can be wrong」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 94. Here’s what Copilot gave us the first time we asked:

- 原始层级：H1，源行：L2366
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- """ Here is the explanation for the code above: 1. We define a function called best\_word that takes one argument, word\_list. 2. We define the variables best\_word and best\_points and set them equal to the empty strin…
- 4. We define a variable called points that is equal to the result of calling num\_points with word as an argument. 5. We use an if statement to check if points is greater than best\_points. 6. If it is, we set best\_wor…
- To us, this is an excellent description of what the code does line by line. Notice, however, to make full sense of it, you need to know important Python terminology and features. The explanation from Copilot refers to f…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- To us, this is an excellent description of what the code does line by line. Notice, however, to make full sense of it, you need to know important Python terminology and features. The explanation from Copilot refers to f…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Here’s what Copilot gave us the first time we asked:」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 95. 4.3 Top 10 programming features you need to know: Part 1

- 原始层级：H1，源行：L2380
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- We’re going to give you a whirlwind tour of the 10 Python features that you’ll need for the rest of your programming journey, starting with the first five of those in this chapter.
- Python is an interactive language, which makes it easier than other languages for us to play around with and see what stuff does. We’ll take advantage of that here as we explore programming features. This is how the two…
- >REPL Python: Start REPL Replace Ctrl + H Replace with Next Value Ctrl + Shift + . Replace with Previous Value Ctrl + Shift + . Search: Replace in Files Ctrl + Shift + H

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Python is an interactive language, which makes it easier than other languages for us to play around with and see what stuff does. We’ll take advantage of that here as we explore programming features. This is how the two…
- Figure 4.5 Starting REPL from VS Code
- This will put you back at the same Python prompt as in chapter 3 (as shown in figure 4.6), except with none of your functions loaded.
- `txt` 代码块，源行 2403：PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL / PS C:\Users\leona\copilot-book> & C:/Users/leona/AppData/Local/Programs/Python/Python311/… / Python 3.11.1 (tags/v3.11.1:a7a450f, Dec 6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on… / Type "help", "copyright", "credits" or "license" for more information.
- `txt` 代码块，源行 2414：>>> 5 * 4
- 图片引用：`images/7b7d30482d22aba2d5f2008e4f076f4ba07e6efcbade450d6da810108cd7f849.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3 Top 10 programming features you need to know: Part 1」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 96. 4.3.1 #1. Functions

- 原始层级：H1，源行：L2418
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- You learned all about functions in chapter 3, so let’s just summarize what we learned. You use functions to break a large problem into smaller pieces. In retrospect, that best\_word function we wrote in chapter 3 is a p…
- We design a function to take parameters, one parameter for each piece or collection of data that the function needs to do its job. After doing their work, most functions use return to send the answer back to the line of…
- For each program we write, we’ll likely need to design a few functions, but there are also some functions that are built-in to Python that we get for free. We can call those like we call our own functions. For example,…

#### 公式与符号

- >>> name = input("What is your name? ")

#### 例子 / 代码 / 图表

- You learned all about functions in chapter 3, so let’s just summarize what we learned. You use functions to break a large problem into smaller pieces. In retrospect, that best\_word function we wrote in chapter 3 is a p…
- For each program we write, we’ll likely need to design a few functions, but there are also some functions that are built-in to Python that we get for free. We can call those like we call our own functions. For example,…
- There’s also the input function, which we used in our get\_strong\_password function from chapter 3. It takes an argument that becomes the prompt, and it returns whatever the user types at the keyboard:
- `txt` 代码块，源行 2426：>>> max(5, 2, 8, 1) / 8
- `txt` 代码块，源行 2433：>>> name = input("What is your name? ") / What is your name? Dan / >>> name / 'Dan'
- `txt` 代码块，源行 2442：>>> print('Hello', name) / Hello Dan

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.1 #1. Functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 97. 4.3.2 #2. Variables

- 原始层级：H1，源行：L2447
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- A variable is a name that refers to a value. We used variables in chapter 3 to keep track of return values from functions. We also just used a variable here to hold the user’s name. Whenever we need to remember a value…
- To assign a value to a variable, we use the = (equal sign) symbol, which is called the assignment symbol. It figures out the value of whatever is on the right and then assigns that to the variable:
- >>> age = 20 + 4 >>> age 24 The right-hand side of the equal symbol is evaluated, which means 20 + 4 is evaluated to be 24. Then the variable age is assigned the value of 24.

#### 公式与符号

- To assign a value to a variable, we use the = (equal sign) symbol, which is called the assignment symbol. It figures out the value of whatever is on the right and then assigns that to the variable:
- >>> age = 20 + 4

#### 例子 / 代码 / 图表

- 图片引用：`images/d85a66296f2d0ce87ed86e09d4982901a368fe48431c3cf3035ea10d0c612f12.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.2 #2. Variables」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 98. The = symbol is different in Python than in math

- 原始层级：H1，源行：L2464
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- The = sign is used in Python and other programming languages to denote assignment. The variable on the left side of the equal symbol is given the value of the calculation performed on the right side of the equal symbol.…
- We can use the variable in a larger context, called an expression. The value that the variable refers to gets substituted for its name:
- >>> age + 3 27 >>> age 24 Age is still available in the Python prompt and has the value 24. 24 + 3 is evaluated to be 27. The expression of age + 3 does not change age because we did not reassign age.

#### 公式与符号

- # The = symbol is different in Python than in math

#### 例子 / 代码 / 图表

- >>> age + 3 27 >>> age 24 Age is still available in the Python prompt and has the value 24. 24 + 3 is evaluated to be 27. The expression of age + 3 does not change age because we did not reassign age.
- 图片引用：`images/ac98aec4865b31351078487ee6f06b8fd5a1c174e40bfe19464a32651444740d.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「The = symbol is different in Python than in math」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 99. Variables persist in the Python prompt

- 原始层级：H1，源行：L2484
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- We assigned age in the earlier batch of code. Why can we keep referring to it? Any variable declared during a session of programming with your Python prompt will stick around until you quit. That’s just how variables wo…
- But notice that the variable age didn’t change when we said age + 3! To change it, we need another = assignment statement:
- >>> age = age + 5 >>> age 2.9 We have changed age by doing an assignment (the equal symbol).

#### 公式与符号

- But notice that the variable age didn’t change when we said age + 3! To change it, we need another = assignment statement:
- >>> age = age + 5
- equivalent to age = age + 5.
- to age = age * 2.

#### 例子 / 代码 / 图表

- We assigned age in the earlier batch of code. Why can we keep referring to it? Any variable declared during a session of programming with your Python prompt will stick around until you quit. That’s just how variables wo…
- 图片引用：`images/ea920a111e7e3a7515439c006d6857085703282fe080a3272d4615eb2179f1f4.jpg`
- 图片引用：`images/2ef5f5f629b058ee013e9aa13089cff0430174361101f2e8960ee2f2a14c2733.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Variables persist in the Python prompt」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 100. 4.3.3 #3. Conditionals

- 原始层级：H1，源行：L2521
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- Whenever our program has to make a decision, we need a conditional statement. For example, in chapter 2, we needed to make a decision about which quarterbacks to include in our data. To do so, we used if statements.
- Remember our larger function from chapter 3? We’ve reproduced it here in the following listing.
- Listing 4.2 Function to determine the larger of two values

#### 公式与符号

- >>> age = 40
- >>> age = 25
- >>> age = 25
- Suppose that you put age = 25 above this code and run it. What do you think will happen?

#### 例子 / 代码 / 图表

- Whenever our program has to make a decision, we need a conditional statement. For example, in chapter 2, we needed to make a decision about which quarterbacks to include in our data. To do so, we used if statements.
- We can play around with conditional statements at the Python prompt, too—we don’t need to be writing code inside of a function. Here’s an example:
- You’ll notice that the prompt changes from >>> to ... when you’re typing inside the if statement. The change of prompt lets you know that you’re in the middle of typing code that you need to complete. You need an extra…
- `mermaid` 代码块，源行 2533：graph TD / A["def larger(num1, num2): if num1 > num2: return num1 else: return num2"] --> B["num1 >… / A --> C["This line is executed when num1 is greater than num2."] / A --> D["else: a keyword that must be paired with an if keyword. When the if doesn't exec…
- 图片引用：`images/5958ade4b7e41fab7dc815b1d029e7cfa903cb11d1206f1c7e8a671a8ccee6a4.jpg`
- 图片引用：`images/b2bbead3e34ae8ad042dcd94175a272ee629c5f20a0cbee90b1b297edeea6b2f.jpg`
- 图片引用：`images/4048808195103ba78112a80de9d104407caabb2b9627fcbf61d4f783441d642c.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.3 #3. Conditionals」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 101. 4.3.4 #4. Strings

- 原始层级：H1，源行：L2677
- 推荐周次：第 3 周, 第 6 周, 第 17 周

#### 核心重点

- As we learned in chapter 3, a string is the type we use whenever we want to store text. Text is everywhere—stats like in chapter 2, passwords, books—so strings show up in almost every Python program.
- We use quotation marks to indicate the beginning and end of the string. You’ll see Copilot use double quotes or single quotes. It doesn’t matter which you use; just be sure to start and end the string with the same type…
- Strings come with a powerful set of methods. A method is a function that’s associated with a particular type—in this case, strings. The way you call a method is a little different than how you call a function: we need t…

#### 公式与符号

- phone_number = phone_number.replace('(', '')
- phone_number = phone_number.replace(')', '')
- phone_number = phone_number.replace('-', '')
- >>> first = 'This is a '
- >>> second = 'sentence.'

#### 例子 / 代码 / 图表

- We use quotation marks to indicate the beginning and end of the string. You’ll see Copilot use double quotes or single quotes. It doesn’t matter which you use; just be sure to start and end the string with the same type…
- Strings come with a powerful set of methods. A method is a function that’s associated with a particular type—in this case, strings. The way you call a method is a little different than how you call a function: we need t…
- In chapter 3, Copilot used some string methods to implement is\_strong\_ password. Let’s try using those methods here to gain a better understanding of how they work:
- `txt` 代码块，源行 2687：>>> 'abc'.isupper() / False / >>> 'Abc'.isupper() / False
- 图片引用：`images/9c6652d3134c648991f2c61c2b727944405ac5ab33f3a7db92536703fed9c39f.jpg`
- 图片引用：`images/c9a996153fb076146324f185f2cf373e60a99cb7704dde6eb9c2b152dd707f04.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.4 #4. Strings」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 102. 4.3.5 #5. Lists

- 原始层级：H1，源行：L2774
- 推荐周次：第 3 周, 第 6 周, 第 11 周, 第 17 周

#### 核心重点

- A string is great when we have a sequence of characters, like a password or a single Scrabble word. But sometimes we need to store many words or many numbers. For that, we need a list.
- We used a list in chapter 3 for the best\_word function, because that function needed to work with a list of individual words.
- Whereas we use quotation marks to start and end a string, we use opening and closing square brackets to start and end a list. And, as for strings, there are many methods available on lists. To give you an idea of the ki…

#### 公式与符号

- >>> books = ['The Invasion', 'The Encounter', 'The Message']
- >>> title = 'The Invasion'

#### 例子 / 代码 / 图表

- Many Python types, including strings and lists, allow you to work with particular values using an index. The index starts at 0 and goes up to, but not including, the number of values. That is, the first value has index…
- Figure 4.7 List elements can be accessed through either positive or negative indexes.
- We can also use indexing to change a specific value in a list. For example,
- `txt` 代码块，源行 2822：>>> books / ['The Predator', 'The Message', 'The Encounter', 'The Invasion'] / >>> books[0] / 'The Predator'
- `txt` 代码块，源行 2848：>>> books [1:3] / ['The Message', 'The Encounter'] / Starts at index 1, end at index 2 (not 3!)
- `txt` 代码块，源行 2858：Same as using books[0:3] / >>> books[:3] / ['The Predator', 'The Message', 'The Encounter'] / >>> books[1:]
- 图片引用：`images/d0f14d19094592909d34024c5eba25edfd7756c3eea38bcb26075ce94da2d90f.jpg`
- 图片引用：`images/45fe6f3e484ffe73467d91cf1ebf29a02230592dba72138f33c1201fe9efedf8.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.5 #5. Lists」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 103. 4.3.6 Conclusion

- 原始层级：H1，源行：L2901
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 17 周

#### 核心重点

- In this chapter, we introduced you to five of the most common code features in Python. We’ll continue with five more in the next chapter. We also showed you how you can use the Copilot explanation tool to help you under…
- Table 4.2 Summary of Python code features from this chapter

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- In this chapter, we introduced you to five of the most common code features in Python. We’ll continue with five more in the next chapter. We also showed you how you can use the Copilot explanation tool to help you under…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.6 Conclusion」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 104. Summary

- 原始层级：H1，源行：L2909
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Summary」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 105. Reading Python 5code: Part 2

- 原始层级：H1，源行：L2923
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Reading Python 5code: Part 2」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 106. This chapter covers

- 原始层级：H1，源行：L2925
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- Repeating code the required number of times using loops ¡ Using indentation to tell Python which code goes together Building dictionaries to store pairs of associated values ¡ Setting up files to read and process data ¡…
- In chapter 4, we explored five Python features that you’re going to see all the time as you continue in your programming journey: functions, variables, conditionals (if statements), strings, and lists. You need to know…
- We’re going to continue in this chapter with five more Python features, which will round out our top 10. As in chapter 4, we’ll do this through a combination of our own explanations, explanations from Copilot, and exper…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Repeating code the required number of times using loops ¡ Using indentation to tell Python which code goes together Building dictionaries to store pairs of associated values ¡ Setting up files to read and process data ¡…
- In chapter 4, we explored five Python features that you’re going to see all the time as you continue in your programming journey: functions, variables, conditionals (if statements), strings, and lists. You need to know…
- We’re going to continue in this chapter with five more Python features, which will round out our top 10. As in chapter 4, we’ll do this through a combination of our own explanations, explanations from Copilot, and exper…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This chapter covers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 107. 5.1 Top 10 programming features you need to know: Part 2

- 原始层级：H1，源行：L2938
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Let’s continue where we left off in the last chapter with feature number 6.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5.1 Top 10 programming features you need to know: Part 2」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 108. 5.1.1 #6. Loops

- 原始层级：H1，源行：L2942
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- A loop allows the computer to repeat the same block of code as many times as needed. If a single one of our top 10 programming features exemplifies why computers are so useful for helping us get work done, it’s this one…
- There are two types of loops: for loops and while loops. Generally speaking, we use a for loop whenever we know how many times we need the loop to run, and we use a while loop when we don’t. For example, in chapter 3, o…
- Listing 5.1 Best\_word function from chapter 3

#### 公式与符号

- best_word = ""
- best_points = 0
- points = num_points(word)
- best_word = word
- best_points = points

#### 例子 / 代码 / 图表

- There are two types of loops: for loops and while loops. Generally speaking, we use a for loop whenever we know how many times we need the loop to run, and we use a while loop when we don’t. For example, in chapter 3, o…
- Let’s see an example of a for loop on a list this time. We’ll also throw two lines of code into the loop to demonstrate how that works, too.
- Listing 5.2 Loop example using a for loop
- `python` 代码块，源行 2949：def best_word(word_list): / """ / word_list is a list of words. / Return the word worth the most points.
- `txt` 代码块，源行 2968：>>> s = 'vacation' / >>> for char in s: / ... print('Next letter is', char) / ...
- `python` 代码块，源行 2990：>>> lst = ['cat', 'dog', 'bird', 'fish'] / >>> for animal in lst: / ... print('Got', animal) This code runs on each iteration. / ... print('Hello', animal)

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5.1.1 #6. Loops」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 109. Copilot explanations can be wrong

- 原始层级：H1，源行：L3090
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- We chose the previous Copilot explanation because it was the best answer from Copilot after we asked it to explain the code three times. One of the answers it gave us sounded quite plausible, until it started talking ab…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- We chose the previous Copilot explanation because it was the best answer from Copilot after we asked it to explain the code three times. One of the answers it gave us sounded quite plausible, until it started talking ab…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Copilot explanations can be wrong」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 110. (continued)

- 原始层级：H1，源行：L3094
- 推荐周次：第 3 周, 第 10 周, 第 17 周

#### 核心重点

- We’ll let you use Copilot explanations going forward and, if you’re interested, we encourage you to ask Copilot to explain any code from prior chapters that you’re still curious about. We do need to caution you again th…
- As with anything related to AI coding assistants right now: they’re going to mess up. But we’ve introduced Copilot explanations here because we see them as a potentially powerful teaching resource now and that will beco…
- We’re supposed to use a while loop in these kinds of situations where we don’t know how many iterations there will be. But we can use a while loop even when we know how many iterations there are. For example, we can use…

#### 公式与符号

- >>> index = 0

#### 例子 / 代码 / 图表

- We’ll let you use Copilot explanations going forward and, if you’re interested, we encourage you to ask Copilot to explain any code from prior chapters that you’re still curious about. We do need to caution you again th…
- As with anything related to AI coding assistants right now: they’re going to mess up. But we’ve introduced Copilot explanations here because we see them as a potentially powerful teaching resource now and that will beco…
- We’re supposed to use a while loop in these kinds of situations where we don’t know how many iterations there will be. But we can use a while loop even when we know how many iterations there are. For example, we can use…
- `python` 代码块，源行 3103：>>> lst / ['cat', 'dog', 'bird', 'fish'] / >>> index = 0 / >>> while index < len(lst):

#### 备课摘取建议

- 若用于 PPT，可把本节作为「(continued)」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 111. 5.1.2 #7. Indentation

- 原始层级：H1，源行：L3124
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- Indentation is critical in Python code because Python uses it to determine which lines of code go together. That’s why, for example, we always indent all of the lines of code inside of a function, the various portions o…
- For example, let’s say that we want to ask the user for the current hour and then output some text based on whether it is morning, afternoon, or evening:
- If it is morning, we want to output “Good morning!” and “Have a nice day.” If it is afternoon, we want to output “Good afternoon!” If it is evening, we want to output “Good evening!” and “Have a good night.”

#### 公式与符号

- hour = int(input('Please enter the current hour from 0 to 23:'))

#### 例子 / 代码 / 图表

- Indentation is critical in Python code because Python uses it to determine which lines of code go together. That’s why, for example, we always indent all of the lines of code inside of a function, the various portions o…
- For example, let’s say that we want to ask the user for the current hour and then output some text based on whether it is morning, afternoon, or evening:
- Whenever we write code, we need to use multiple levels of indentation to express which pieces of code are associated with functions, if statements, loops, and so on. For example, when we write a function header, we need…
- `python` 代码块，源行 3136：hour = int(input('Please enter the current hour from 0 to 23:'))
- `python` 代码块，源行 3140：if hour < 12: / print('Good morning!') / print('Have a nice day.') / elif hour < 18:

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5.1.2 #7. Indentation」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 112. Listing 5.6 Function to determine the larger of two values

- 原始层级：H1，源行：L3157
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 11 周, 第 12 周, 第 17 周

#### 核心重点

- This shows a single indent for body of the function. def larger(num1, num2): if num1 > num2: return num1 else: return num2 This shows a double indent for body of the function and body of if statement. This shows a singl…
- Or consider our get\_strong\_password function that we looked at in listing 5.4: as usual, everything in the function is indented, but there’s further indentation for the body of the while loop.
- There are even more levels of indentation in the first version of our num\_points function (reproduced here from chapter 3 as listing 5.7). That’s because, inside of the for loop through each character of the word, we h…

#### 公式与符号

- points = 0
- points = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1,
- >>> countries = ['Canada', 'USA', 'Japan']
- >>> medals = [[2, 0, 2],

#### 例子 / 代码 / 图表

- Indentation makes a huge difference on what our programs ultimately do. For example, let’s compare putting two consecutive loops versus nesting one in the other using indentation. Here are two loops in a row:
- For example, say we had some data about the figure skating medals won at the 2018 Winter Olympics, as shown in table 5.1.
- Notice that our list of lists is just storing the numeric values, and we can find a value in the list of lists by referring to its row and column (for example, Japan’s gold medal corresponds to the row at index 2 and th…
- `python` 代码块，源行 3180：def num_points(word): / """ / Each letter is worth the following points: / a, e, i, o, u, l, n, s, t, r: 1 point
- `txt` 代码块，源行 3267：>>> countries = ['Canada', 'USA', 'Japan'] / >>> for country in countries: / ... print(country) / ...
- `txt` 代码块，源行 3328：>>> medals = [[2, 0, 2], / ... [1, 2, 0], / ... [1, 1, 0], / ... [0, 1, 0],
- 图片引用：`images/9c61f46468ee99d15b20b3d883915ec0bb4590a342de2b0c453f6e334ae2859c.jpg`
- 图片引用：`images/73cfc5b57f053f60847d58e2d0be9df62194c5cbc2ff270bbe3aae940663bb7c.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Listing 5.6 Function to determine the larger of two values」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 113. 5.1.3 #8. Dictionaries

- 原始层级：H1，源行：L3406
- 推荐周次：第 3 周, 第 6 周, 第 10 周, 第 17 周

#### 核心重点

- Remember that each value in Python has a specific type. There are a lot of different types because there are many kinds of values that we might want to use! We’ve talked about using numbers to work with numeric values,…
- There’s one more Python type that shows up often, and it’s called a dictionary. As we mentioned in chapter 2 when we talk about a dictionary in Python, we don’t mean a list of words and their definitions. In Python, a d…
- That dictionary would probably be huge, but a small version of such a dictionary might look like this:

#### 公式与符号

- >>> freq = {'DNA': 11, 'acquire': 11, 'Taxxon': 13, \

#### 例子 / 代码 / 图表

- There’s one more Python type that shows up often, and it’s called a dictionary. As we mentioned in chapter 2 when we talk about a dictionary in Python, we don’t mean a list of words and their definitions. In Python, a d…
- It worked! We have discovered that dictionaries are mutable. Our freq dictionary allows us to start from whatever word we want and find its frequency. More generally, a dictionary allows us to go from key to value. Howe…
- `txt` 代码块，源行 3414：>>> freq = {'DNA': 11, 'acquire': 11, 'Taxxon': 13, \ / ... 'Controller': 20, 'morph': 41}
- `python` 代码块，源行 3425：>>> freq.keys() / dict_keys(['DNA', 'acquire', 'Taxxon', 'Controller', 'morph']) / >>> freq.values() / dict_values([11, 11, 13, 20, 41])
- `python` 代码块，源行 3441：>>> freq['dna'] # Oops, wrong key name because it is case sensitive / Traceback (most recent call last): / File " ", line 1, in / KeyError: 'dna'
- 图片引用：`images/db01122e1cef15ea776cb6f999445498ee0738724b7960739b197af977844872.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5.1.3 #8. Dictionaries」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 114. 5.1.4 #9. Files

- 原始层级：H1，源行：L3479
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 7 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- It’s often the case that we’ll want to work with datasets that exist in files. For example, in chapter 2, we worked with a file of NFL stats to visualize the most effective quarterbacks. Using files is common of other d…
- In chapter 2, we worked with a file called nfl\_offensive\_stats.csv. Make sure that this file is in your current program directory because we’ll use that file now to further understand some of the code we used in chapt…
- The first step in working with data from a file is to use Python’s open function to open the file:

#### 公式与符号

- >>> nfl_file = open('nfl_offensive_stats.csv')
- >>> nfl_file = open('nfl_offensive_stats.csv', 'r')
- >>> line = nfl_file.readline( ) ← Reads the line from the file
- >>> lst = line.split(',')
- >>> line = nfl_file.readline()

#### 例子 / 代码 / 图表

- It’s often the case that we’ll want to work with datasets that exist in files. For example, in chapter 2, we worked with a file of NFL stats to visualize the most effective quarterbacks. Using files is common of other d…
- You’ll sometimes see Copilot add an r as a second argument here:
- Once we do that, we aren’t allowed to use the file anymore. Now that we’ve discussed how to read, process, and close a file, let’s see a full example. In listing 5.10, we provide a new version of our program from chapte…
- `python` 代码块，源行 3487：>>> nfl_file = open('nfl_offensive_stats.csv')
- `python` 代码块，源行 3493：>>> nfl_file = open('nfl_offensive_stats.csv', 'r')
- `txt` 代码块，源行 3501：>>> line = nfl_file.readline( ) ← Reads the line from the file / >>> line / 'game_id, player_id, position, player, team, pass_cmp, pass_att, pass_yds, pass_td, pass_…
- 图片引用：`images/a06509e3245a7b080605e8e3ba475829ef3c0de7ebb68a531d0e9fbbac82a8df.jpg`
- 图片引用：`images/a8fb21c41542271864744574461399ae9de49b583f92a828e7c293bf07d392be.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5.1.4 #9. Files」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 115. More than one way to solve a programming problem

- 原始层级：H1，源行：L3597
- 推荐周次：第 3 周, 第 7 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- There are always many different programs that can be written to solve the same task. Some may be easier to read than others. The most important criterion for code is that it does the correct thing. After that, we care m…
- Files are used commonly in computing tasks because they are a common source for data to be processed. This includes CSV files like the one from this section, log files that keep track of events on computers or websites,…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- There are always many different programs that can be written to solve the same task. Some may be easier to read than others. The most important criterion for code is that it does the correct thing. After that, we care m…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「More than one way to solve a programming problem」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 116. 5.1.5 #10. Modules

- 原始层级：H1，源行：L3603
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- People use Python to make all kinds of things—games, data analysis apps, websites, apps to automate repetitive tasks, apps to control robots, you name it. How can Python possibly have all of the tools for us to do all o…
- Answer: It can’t! It has only the most fundamental tools available by default. What makes Python so powerful is that we can import modules that can help us do all of that stuff.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5.1.5 #10. Modules」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 117. Modules in Python

- 原始层级：H1，源行：L3609
- 推荐周次：第 3 周, 第 4 周, 第 5 周, 第 6 周, 第 7 周, 第 10 周, 第 11 周, 第 17 周

#### 核心重点

- A module is a collection of code designed for a specific purpose. Recall that we don’t need to know how a function works to use it. It’s the same with modules: we don’t need to know how modules work to be able to use th…
- Some modules come with Python, but we still need to import them. Other modules we first have to download. Trust us, if there’s a specific kind of task you want to do with Python, someone’s probably already written a mod…
- Table 5.2 Summary of commonly used Python modules

#### 公式与符号

- >>> zf = zipfile.ZipFile('my_stuff.zip', 'w', zipfile.ZIP_DEFLATED)

#### 例子 / 代码 / 图表

- A module is a collection of code designed for a specific purpose. Recall that we don’t need to know how a function works to use it. It’s the same with modules: we don’t need to know how modules work to be able to use th…
- To try this, create a few files in your programming directory, and make them all end with .csv. You could start with your nfl\_offensive\_stats.csv file and then add a few more. For example, you could add one called act…
- There are de facto Python packages for many tasks, including matplotlib for data visualization, pandas for data science, numpy for numerical analysis, pygame for game development, django for web development, and so on.…
- `txt` 代码块，源行 3625：Actor Name, Age / Anne Hathaway, 40 / Daniel Radcliffe, 33
- `txt` 代码块，源行 3633：Chore, Finished? / Clean dishes, Yes / Read Chapter 6, No
- 图片引用：`images/1be8147fd2e146469b8c6e979edc8c6a0587944b061af2714a323204c85014f4.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Modules in Python」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 118. Summary

- 原始层级：H1，源行：L3674
- 推荐周次：第 3 周, 第 6 周, 第 7 周, 第 11 周, 第 17 周

#### 核心重点

- A loop is used to repeat code as many times as needed. We use a for loop when we know how many iterations the loop will do; we use a while loop when we don’t know how many iterations a loop will do. ¡ Python uses indent…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Summary」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 119. Testing and prompt 6engineering

- 原始层级：H1，源行：L3685
- 推荐周次：第 3 周, 第 17 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Testing and prompt 6engineering」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 120. This chapter covers

- 原始层级：H1，源行：L3687
- 推荐周次：第 3 周, 第 8 周, 第 17 周

#### 核心重点

- ¡ Understanding the importance of testing Copilot code ¡ Using closed-box versus open-box testing ¡ Addressing errors by Copilot by modifying prompts ¡ Viewing examples of testing code produced by Copilot
- In chapter 3, we first started to see the importance of testing the code produced by Copilot. Testing is an essential skill for anyone writing software because it gives you confidence that the code is functioning proper…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- ¡ Understanding the importance of testing Copilot code ¡ Using closed-box versus open-box testing ¡ Addressing errors by Copilot by modifying prompts ¡ Viewing examples of testing code produced by Copilot
- In chapter 3, we first started to see the importance of testing the code produced by Copilot. Testing is an essential skill for anyone writing software because it gives you confidence that the code is functioning proper…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This chapter covers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。
