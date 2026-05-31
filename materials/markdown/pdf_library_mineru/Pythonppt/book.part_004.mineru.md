---
type: source
title: Pythonppt
format: mineru-api-markdown
raw_path: materials/raw/external_ppt/嵩天Python/Pythonppt.pdf
mineru_raw_markdown: materials/markdown/pdf_library_mineru/api_raw/Pythonppt/part_004/full.md
source_pages: 1287
page_range: 601-800
generated: 2026-05-24 12:20:18
status: generated_part
---

# lambda函数

# lambda函数返回函数名作为结果

lambda函数是一种匿名函数，即没有名字的函数  
使用lambda保留字定义，函数名是返回结果  
lambda函数用于定义简单的、能够在一行内表示的函数

# lambda函数

<函数名> = lambda <参数>: <表达式>

def <函数名>(<参数>)

等价于

<函数体>

return <返回值>

# lambda函数

>>> f = lambda x, y : x + y

>>> f(10, 15)

25

>>> f = lambda : "lambda函数"

>>> print(f())

lambda函数

# lambda函数的应用

# 谨慎使用lambda函数

lambda函数主要用作一些特定函数或方法的参数  
lambda函数有一些固定使用方式，建议逐步掌握  
一般情况，建议使用def定义的普通函数

# 单元小结

# 函数的定义与使用

使用保留字def定义函数，lambda定义匿名函数  
可选参数(赋初值)、可变参数(\*b)、名称传递  
保留字return可以返回任意多个结果  
保留字global声明使用全局变量，一些隐式规则

![](images/33b9fc1329c33051de5b1bb335c8b2e50d2cd4110f96c2889f90043bfa0faf22.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with wheels, no text or symbols present
</details>

# 实例7: 七段数码管绘制

![](images/96c4a8b20347e8cb1fb188e0b570018e5dd081362936e0006dcab63a59439e0c.jpg)

python

嵩 天

北京理工大学

pythom

# "七段数码管绘制"问题分析

![](images/4ed9cc49237bbb0f19235a83bd744fe6a68bdb98d82d85efb1d4f3e71706297e.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/6e5feee6567123fd89f73b81e34ad910e28171fb67173cb8c5d30a5219bcfe47.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 问题分析

# 七段数码管

![](images/390404d7311e1601735ae59e6af543d66175cebb3d79eff8326534d08b478c67.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a black metal-framed digital display unit with 8888 digits, featuring hexagonal grid patterns and small connectors (no text or symbols visible)
</details>

![](images/c417dbe1ee3d9458db9da3fee1340ad5e9be7181d1f94e3229be16387243b1fc.jpg)

<details>
<summary>text_image</summary>

a
f
g
b
e
c
d
dp
</details>

![](images/9506d01fd48b84b7fc45a78dc847ccdbd8b0be238a0c10ad960068ad255ba9c9.jpg)

<details>
<summary>text_image</summary>

8.8.8.8.4.5.6.7.8.9
8.6.0.8.6.6.
</details>

# 问题分析

# 七段数码管绘制

需求：用程序绘制七段数码管，似乎很有趣  
该怎么做呢？

turtle绘图体系

![](images/07c4d5abf461fed0c5f915d3fd0755a61974453bee9d8d82a806e9bef2f2c553.jpg)

七段数码管绘制

# 问题分析

# 七段数码管绘制时间

![](images/8895d2411af55ecae09a5ebf1000fafbad019d5b3ae68edbc4bedef993450afc.jpg)

Python Turtle Graphics

![](images/723ad5d0160740ae633a40976e1f9171f0e4e5c75a7b91f51923e55c849397d5.jpg)

![](images/0f8ec0cfa9b583e5e2948e65281ba30e6ca7eaf5ed067f6b5c411383ceca4e6e.jpg)

<details>
<summary>text_image</summary>

20 18 年 10 月 10 日
</details>

# "七段数码管绘制"实例讲解(上)

![](images/d2b1f85c77f8fce06061081c90458f2828e7a484c83e0e426660916e1ca10bfb.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/d69da45d00b45455b88e04816196cdf2a5cec56b7ec0748fed521a20e101fc07.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 七段数码管绘制

# 基本思路

步骤1：绘制单个数字对应的数码管  
步骤2：获得一串数字，绘制对应的数码管  
步骤3：获得当前系统时间，绘制对应的数码管

# 七段数码管绘制

# 步骤1: 绘制单个数码管

![](images/8271072d691760cad8e71e2b3c09e05b74c620ead0aba6fbc3249476ed444477.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcf,stroke:#333
```
</details>

七段数码管由7个基本线条组成  
七段数码管可以有固定顺序  
不同数字显示不同的线条

# import turtle

def drawLine(draw): #绘制单段数码管

```txt
turtle.pendown() if draw else turtle.penup()
turtle.fd(40)
turtle.right(90) 
```

def drawDigit(digit): #根据数字绘制七段数码管

```txt
drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
drawLine(True) if digit in [0,2,6,8] else drawLine(False)
turtle.left(90)
drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
turtle.left(180) 
```

```javascript
turtle.penup() #为绘制后续数字确定位置
turtle.fd(20) #为绘制后续数字确定位置
```

![](images/11acae19be282af43e0a5ee39735997d8210ff4196cac53fa939f0fe9104e926.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    H --> I["↓7"]
```
</details>

# 七段数码管绘制

步骤2: 获取一段数字，绘制多个数码管  
![](images/93878e8d745cc0d35f3bea6b294f24d67a1518538c52d4ca235614a468a547fd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcf,stroke:#333
```
</details>

第1个

![](images/4040c34889cfbcffe23275c5a506e7d89dd65b8b854be793e466baa3a5db4d16.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcf,stroke:#333
```
</details>

第2个

![](images/f55d8fc5d8d5bdc6408c304c45a586e4b2d5840c33ada682e41d9e4cd89dbf04.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    H --> I["↓7"]
    I --> J["↓2"]
    J --> K["3"]
    K --> L["4"]
    L --> M["5"]
```
</details>

第N个

import turtle  
```python
def drawLine(draw): #绘制单段数码管
...(略) 
```

```txt
def drawDigit(digit): #根据数字绘制七段数码管
...(略) 
```

```txt
def drawDate(date): #获得要输出的数字
for i in date: 
```

drawDigit(eval(i)) #通过eval()函数将数字变为整数

def main():   
```lua
turtle.setup(800, 350, 200, 200)
turtle.penup()
turtle.fd(-300)
turtle.pensize(5)
drawDate('20181010')
turtle.hideturtle()
turtle.done() 
```  
main()

Python Turtle Graphics

$$
2 0 1 8 1 0 1 0
$$

# 准备好电脑，与老师一起编码吧！

# "七段数码管绘制"实例讲解(下)

![](images/a848ff59cab58d6156db61cc62b6b830b33ce2b4d2bad1b79835492931048cc5.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/b21bd8278a1ed99e8e323d4094204654e421006b2635d8948220809ee6c3d8ff.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 七段数码管绘制

# 基本思路

- 步骤1：绘制单个数字对应的数码管  
- 步骤2：获得一串数字，绘制对应的数码管  
步骤3：获得当前系统时间，绘制对应的数码管

# 七段数码管绘制

# 绘制漂亮的七段数码管

![](images/272124e93a6ffd81b58fbfe42068d1a385eadb0c0cf3d2077e3d062c4eb4541f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcf,stroke:#333
```
</details>

\- 增加七段数码管之间线条间隔

import turtle  
```txt
def drawGap(): #绘制数码管间隔
turtle.penup()
turtle.fd(5) 
```  
def drawLine(draw): #绘制单段数码管

```txt
drawGap()
turtle.pendown() if draw else turtle.penup()
turtle.fd(40)
drawGap()
turtle.right(90) 
```  
def drawDigit(digit): #根据数字绘制七段数码管

```txt
drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
drawLine(True) if digit in [0,2,6,8] else drawLine(False)
...(略) 
```

# 七段数码管绘制

# 步骤3: 获取系统时间，绘制七段数码管

![](images/b1dcfdac858a13e1df07890ea9a289247e0f1124b27fca050512338c48c44c67.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["起点"] --> B["1"]
    B --> C["2"]
    C --> D["3"]
    D --> E["4"]
    E --> F["5"]
    F --> G["6"]
    G --> H["7"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcf,stroke:#333
```
</details>

使用time库获得系统当前时间  
增加年月日标记  
- 年月日颜色不同

import turtle, time  
…(略)   
def drawDate(date): #data为日期，格式为 '%Y-%m=%d+'   
turtle.pencolor("red")  
for i in date:   
```python
if i == '-':
    turtle.write('年', font = ("Arial", 18, "normal"))
    turtle.pencolor("green")
    turtle.fd(40) 
```

```python
elif i == '=':
    turtle.write('月', font = ("Arial", 18, "normal"))
    turtle.pencolor("blue")
    turtle.fd(40) 
```

```python
elif i == '+':
    turtle.write('日', font = ("Arial", 18, "normal"))
else:
    drawDigit(eval(i)) 
```  
def main():   
…(略)

import turtle, time  
…(略)   
def drawDate(date):   
…(略)   
def main():   
```lua
turtle.setup(800, 350, 200, 200)
turtle.penup()
turtle.fd(-300)
turtle.pensize(5)
```  
drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))

```lua
turtle.hideturtle()
turtle.done() 
```  
main()

Python Turtle Graphics

t

![](images/494511fa1c7452381c5856f10125ea87fa637d1d06e97ddccefbb567649ffcf0.jpg)

<details>
<summary>text_image</summary>

20 18 年
</details>

![](images/da94644e5cbe6ef7d5144de3f89413a9960553febbd1b27a73fa91491ab06506.jpg)

![](images/36727362259838f9080cf1e2cea6ca22dfb0e618a4676bfc811819a54c5c4d49.jpg)

# 准备好电脑，与老师一起编码吧！

# "七段数码管绘制"举一反三

![](images/3c7b5557bd80a527f9b4e94549a41bb328e3c2b7ec87017c253e0305914ffbb8.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/796478ace4102aeb01dc34eb50b5cca5b6a69c58fd166d6b6f5ba4572bf5bfad.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

import turtle, time

…(略)

def drawLine(draw):

drawGap()

turtle.pendown() if draw else turtle.penup()

turtle.fd(40)

drawGap()

turtle.right(90)

def drawDigit(digit):

drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)

drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)

drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)

drawLine(True) if digit in [0,2,6,8] else drawLine(False)

turtle.left(90)

drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)

drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)

drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)

…(略)

![](images/4710164208a5e8823cc887a49b0e2a5d0e05e6e9072c9bc3dd3789e74eba7b6b.jpg)

<details>
<summary>text_image</summary>

Python Turtle Graphics
20 18 年 10 月 10 日
</details>

# 举一反三

# 理解方法思维

模块化思维：确定模块接口，封装功能  
规则化思维：抽象过程为规则，计算机自动执行  
化繁为简：将大功能变为小功能组合，分而治之

# 举一反三

# 应用问题的扩展

绘制带小数点的七段数码管  
带刷新的时间倒计时效果  
绘制高级的数码管

![](images/d5594cb1b2227ca3d49b690ccc888d01ca0c3850eb4072181b41a55592afbc1a.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric pattern with red and gray shapes forming a symmetrical design (no text or symbols)
</details>

![](images/5b2baa5ae1a9d124ec7428c484fa02fc23c274e35c2af674654079d00b73221e.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric pattern with interlocking hexagonal shapes (no text or symbols)
</details>

# 代码复用与函数递归

![](images/a7006f59a33df77cc9d43686671f902090de16728c1cf1051458a0b08ab56ff3.jpg)

python

嵩 天

北京理工大学

pythom

# 单元开篇

# 代码复用与函数递归

![](images/a7e88bcd76c14bb9f54390f3eaad52cdd9ec6898d34b387618846691c491d5b3.jpg)

<details>
<summary>natural_image</summary>

Simple icon of a person with beard and mustache, wearing a collared shirt (no text or symbols)
</details>

代码复用与模块化设计  
函数递归的理解  
函数递归的调用过程  
函数递归实例解析

![](images/aa6ee7d9755720daf068e6c4414ad8423ac76392122078eaaddf9bf4725a7647.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle on a blue track (no text or symbols)
</details>

# 代码复用与模块化设计

![](images/732a9c97a09dbd900c3885dbd51ea1c47ccf7669f01a19b6b9cb2f460663bf0e.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/b7ac2672a38fdcef3ba61f58cb0636dc514d4428ab0e574e0ee7fbe5eeeace99.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 代码复用

# 把代码当成资源进行抽象

代码资源化：程序代码是一种用来表达计算的"资源"  
代码抽象化：使用函数等方法对代码赋予更高级别的定义  
代码复用：同一份代码在需要时可以被重复使用

# 代码复用

# 函数 和 对象 是代码复用的两种主要形式

函数：将代码命名

在代码层面建立了初步抽象

对象：属性和方法

<a>.<b> 和 <a>.<b>()

在函数之上再次组织进行抽象

# 模块化设计

# 分而治之

通过函数或对象封装将程序划分为模块及模块间的表达  
具体包括：主程序、子程序和子程序间关系  
分而治之：一种分而治之、分层抽象、体系化的设计思想

# 模块化设计

# 紧耦合 松耦合

紧耦合：两个部分之间交流很多，无法独立存在  
松耦合：两个部分之间交流较少，可以独立存在  
模块内部紧耦合、模块之间松耦合

# 函数递归的理解

![](images/d02a63865ba74d128a278695e0e09614b2fa839af267295c2f2d63c498ba090e.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 递归的定义

# 函数定义中调用函数自身的方式

$$
\boxed {n!} = \left\{ \begin{array}{l l} 1 & n = 0 \\ n (n - 1)! & o t h e r w i s e \end{array} \right.
$$

# 递归的定义

# 两个关键特征

$$
n! = \left\{ \begin{array}{c c} 1 & n = 0 \\ n (n - 1)! & o t h e r w i s e \end{array} \right.
$$

链条：计算过程存在递归链条  
基例：存在一个或多个不需要再次递归的基例

# 递归的定义

# 类似数学归纳法

# 数学归纳法

证明当n取第一个值 $n _ { \theta }$ 时命题成立  
假设当 $\boldsymbol { n } _ { k }$ 时命题成立，证明当 $\ n = n _ { k + 1 }$ 时命题也成立

# 递归是数学归纳法思维的编程体现

# 函数递归的调用过程

![](images/2aeebdb77ca3541900438bbf822314fc52a56aca0b3db39aeec7b23a8fbb3061.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/a267b06193a3469a6ce719c95b15f4743948444682ba6308448f1bc05143e846.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 递归的实现

$$
n! = \left\{ \begin{array}{l l} 1 & n = 0 \\ n (n - 1)! & o t h e r w i s e \end{array} \right.
$$

def fact(n):

if n == 0 :

return 1

else

return n\*fact(n-1)

# 递归的实现

# 函数 + 分支语句

递归本身是一个函数，需要函数定义方式描述  
函数内部，采用分支语句对输入参数进行判断  
基例和链条，分别编写对应代码

# 递归的调用过程

![](images/efcb90b51c45fee2bb1ccc5516286fb3496d5c4fca12e2da717cb457a89ad001.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["n=5"] --> B["def fact(n): if n == 0: return 1 else: return n*fact(n-1)"]
    B --> C["24"]
    D["n=4"] --> E["def fact(n): if n == 0: return 1 else: return n*fact(n-1)"]
    E --> F["6"]
    G["n=3"] --> H["def fact(n): if n == 0: return 1 else: return n*fact(n-1)"]
    H --> I["2"]
    J["n=2"] --> K["def fact(n): if n == 0: return 1 else: return n*fact(n-1)"]
    K --> L["1"]
    M["n=1"] --> N["def fact(n): if n == 0: return 1 else: return n*fact(n-1)"]
    N --> O["1"]
    P["n=0"] --> Q["def fact(n): if n == 0: return 1 else: return n*fact(n-1)"]
    Q --> R["120"]
    S["递归调用"] --> T["n=5"]
```
</details>

![](images/ff9ca885c74fad550c741a7b65f08b957b591eed32b672abc25c72cfc9d6d55b.jpg)

<details>
<summary>text_image</summary>

函数递归实例解析
</details>

# 字符串反转

# 将字符串s反转后输出 >>> s[::-1]

函数 + 分支结构  
def rvs(s):   
递归链条  
return s   
else   
递归基例  
return rvs(s[1:])+s[0]

$$
i f \texttt {s} = = "":
$$

# 斐波那契数列

# 一个经典数列

$$
F (n) = \left\{ \begin{array}{c l} 1 & n = 1 \\ 1 & n = 2 \\ F (n - 1) + F (n - 2) & o t h e r w i s e \end{array} \right.
$$

# 斐波那契数列

$$
F (n) = F (n - 1) + F (n - 2)
$$

函数 + 分支结构  
def f(n):   
if n == 1 or n == 2 :   
递归链条  
return 1   
else   
递归基例  
return f(n-1) + f(n-2)

# 汉诺塔

![](images/44212dd0fb08ed27f00b95226750488fd7e611443cd1cbadb82d88da6fe1505a.jpg)

<details>
<summary>natural_image</summary>

Wooden abacus with a colorful striped top (no text or symbols)
</details>

![](images/aef197c28cf864d14eb17a20a7d975341f9a2d8fe3a07acce4230836f83054ae.jpg)

<details>
<summary>text_image</summary>

N片
</details>

![](images/187bf5a8b5f18f076f595128f1e3283c4d37aee73db25c6eaf705299516fa783.jpg)

<details>
<summary>natural_image</summary>

Simple diagram of a wooden abacus with colored rods and arrows indicating motion (no text or symbols)
</details>

![](images/229c7ebd53360355f53d2c884ea2aa99440488a047c7357a8ab984d41cbce715.jpg)

<details>
<summary>text_image</summary>

2^n步
N片
N片
</details>

![](images/27243968bb8e77fe7e7d74d7cdb4ec9b4df829ebab9d4249a702f802c8c8ce6e.jpg)

<details>
<summary>text_image</summary>

A
B
C
</details>

# 汉诺塔

函数 + 分支结构  
递归链条  
递归基例

$$
\text { count } = 0
$$

def hanoi(n, src, dst, mid):

global count

if n == 1 :

print("{}:{}->{}".format(1,src,dst))

count += 1

else :

hanoi(n-1, src, mid, dst)

print("{}:{}->{}".format(n,src,dst))

count += 1

hanoi(n-1, mid, dst, src)

![](images/003d4be2f511cfbf9156f8c436ebf81f2be42eb388313e8253969635ff5d5c5d.jpg)

<details>
<summary>text_image</summary>

A
B
C
</details>

# 汉诺塔

count = 0

def hanoi(n, src, dst, mid): … (略)

hanoi(3, "A", "C", "B")

print(count)

>>>

1:A->C

2:A->B

1:C->B

3:A->C

1:B->A

2:B->C

1:A->C

7

# 单元小结

# 代码复用与函数递归

模块化设计：松耦合、紧耦合  
- 函数递归的2个特征：基例和链条  
函数递归的实现：函数 + 分支结构

![](images/cacc148e57a54f712faa24bf9185fba6719b88410264f3c5993a5a79cabd5493.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle on a blue track (no text or symbols)
</details>

# Python语言程序设计

# 模块4: PyInstaller库的使用

![](images/ca30630eb15ef87374543731fbbc7fc8748c5a178eae01697798a42cd896f08e.jpg)

python

嵩 天

北京理工大学

pythom

# PyInstaller库基本介绍

![](images/57b8e355810ce49a417c5f5fd2efcb11a51ecfa4189ed53166f667c31f5a34ad.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/46e4f2e3f5cb52149199266a3668492dcbe092038b2f3f1a667e92e2064a8008.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# PyInstaller库概述

# 将.py源代码转换成无需源代码的可执行文件

![](images/04c11dead24d9ec7825b87bd3920e200f038bcb167e6c429b69fe54f3edad8e4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A[".py文件"] --> B["PyInstaller"]
    B --> C["Windows (exe文件)"]
    B --> D["Linux"]
    B --> E["Mac OS X"]
```
</details>

# PyInstaller库概述

# PyInstaller库是第三方库

官方网站：http://www.pyinstaller.org  
第三方库：使用前需要额外安装  
安装第三方库需要使用pip工具

# PyInstaller库的安装

# (cmd命令行) pip install pyinstaller

![](images/f8df0ec1ab630f45d7c9b3f8e3a1472b83a471967685cc9f9a942cc72e74e981.jpg)

<details>
<summary>text_image</summary>

C:\Users\Tian Song>pip install pyinstaller
Collecting pyinstaller
Downloading PyInstaller-3.3.1.tar.gz (3.5MB)
0% | 10kB 93kB/s eta 0:0
0% | 20kB 65kB/s eta 0:
0% | 30kB 78kB/s eta 0:
1% | 40kB 49kB/s eta 0:
1% | 51kB 61kB/s eta 0:
1% | 61kB 74kB/s eta 0:
2% | 71kB 86kB/s eta 0:
2% | 81kB 98kB/s eta 0:
2% | 92kB 111kB/s eta 0
2% | 102kB 94kB/s eta 0
3% | 112kB 104kB/s eta
</details>

![](images/886a1ed2e1d4c412f5eafea76488b78b7b6647871c4ccdb348d51ff364055f1b.jpg)

<details>
<summary>text_image</summary>

99%
100%
8.3MB 11kB/s
Installing collected packages: pefile, altgraph, macholib, py win32, pypiwin32, pyinstaller
Running setup.py install for pefile ... done
Running setup.py install for pyinstaller ... done
Successfully installed altgraph-0.15 macholib-1.9 pefile-2017
.11.5 pyinstaller 3.3.1 pypiwin32-223 pywin32-223
C:\Users\Tian Song>
</details>

# PyInstaller库使用说明

![](images/7b9a56ed2de98b05fb4b758db5565b0150a6e81ca16f4f499cad3c44fe36d320.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/0861eb05a336acce56be504ed0c7689233966cd715e7c46c87fe0e3772aa0e46.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 简单的使用

# (cmd命令行) pyinstaller -F <文件名.py>

\- pyinstaller SevenDigitsDraw2.py

```batch
D:\PYECourse>pyinstaller -F SevenDigitsDrawV2.py
140 INFO: PyInstaller: 3.3.1
140 INFO: Python: 3.6.4
140 INFO: Platform: Windows-10-10.0.15063-SP0
156 INFO: wrote D:\PYECourse\SevenDigitsDrawV2.spec
156 INFO: UPX is not available.
172 INFO: Extending PYTHONPATH with paths
['D:\\PYECourse', 'D:\\PYECourse']
172 INFO: checking Analysis
172 INFO: Building Analysis because out00-Analysis.toc is non
    existent
172 INFO: Initializing module dependency graph...
172 INFO: Initializing module graph hooks...
172 INFO: Analyzing base_library.zip ... 
```

![](images/6c551bb418d3eab00337ef0279c3e8e0a98fdb5da56b0e63dfe7958e39c3044f.jpg)

<details>
<summary>text_image</summary>

pycache_
build
dist
SevenDigitsDrawV2
</details>

![](images/4f616ce382d098da446616220a8a9659edb9a2fa937dd1004e4a9520db3e1a1a.jpg)

![](images/6501c24ed819372d07000a10b73380ba83a00d0acf5682180f11e46c525f55d9.jpg)

# PyInstaller库常用参数

<table><tr><td>参数</td><td>描述</td></tr><tr><td>-h</td><td>查看帮助</td></tr><tr><td>--clean</td><td>清理打包过程中的临时文件</td></tr><tr><td>-D, --onedir</td><td>默认值,生成dist文件夹</td></tr><tr><td>-F, --onefile</td><td>在dist文件夹中只生成独立的打包文件</td></tr><tr><td>-i &lt;图标文件名.ico&gt;</td><td>指定打包程序使用的图标(icon)文件</td></tr></table>

# 使用举例

# pyinstaller –i curve.ico –F SevenDigitsDrawV2.py

![](images/b81cc0ee5de1ba697420f42774cff3874b93468bbfd198ac3209f203b2a8ec7c.jpg)

+   
![](images/8501fe47ce67a867b9b6efa86edbebeefc75c13bf408a37e1cf59fa13977f8be.jpg)

SevenDigitsDrawV2

![](images/09a6288861aab87c4d030368f62a97f5fed00a614d5093713fd2cc1692c490b9.jpg)

SevenDigitsDrawV2

# 实例8: 科赫雪花小包裹

![](images/46bf56c9ab6bbd1736e1e0258ffffbbb51163b035c55ebfd8957f7ff8c0cadd8.jpg)

python

嵩 天

北京理工大学

pythom

# "科赫雪花小包裹"问题分析

![](images/4f573744b4e69ab520698523b4a6938d3e602cded53fc852ddc9aa4ecdf8e2e3.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/a48c65feaf8655a00bda96840d8f5f66f8434797dc78341bfdab4c8462693c92.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 科赫雪花

# 高大上的分形几何

![](images/c77b90d01f6c4437b1313aa9d08bf495139e880fff914328dba108d61b8f79a0.jpg)

<details>
<summary>natural_image</summary>

Symmetrical abstract floral design with blue and pink petal-like petals against a dark blue background (no text or symbols)
</details>

![](images/6e261fe87d37cedeb74c604de0b25e858e207586788ab47f490db7d638264f06.jpg)

<details>
<summary>natural_image</summary>

Fractal spiral pattern with green, blue, and red hues, no text or symbols present
</details>

![](images/8cebc247fd44cc9d87bed7df43a88488c584df4df42778e3db185fae77585f6e.jpg)

<details>
<summary>natural_image</summary>

Close-up of bright green fern leaves with detailed fronds (no text or symbols)
</details>

![](images/8a3cdf5139150e2868c3d230fb9726da3bb884880848da3f550b37b814ae1be3.jpg)

<details>
<summary>natural_image</summary>

Close-up of a bright green, multi-colored ram-follet with leafy green leaves (no text or symbols visible)
</details>

\- 分形几何是一种迭代的几何图形，广泛存在于自然界中

# 科赫雪花

# 科赫曲线，也叫雪花曲线

![](images/0f76e4039506ddfa58cd0c52e8af0050b4218b0484139bee8fe97aa8abcee349.jpg)

<details>
<summary>natural_image</summary>

Fractal pattern with swirling orange and purple patterns against a dark background (no text or symbols)
</details>

![](images/3deca1df64d16dbebeee612fd6b09d02cb9f6554b03f55276354c3747596b72f.jpg)

<details>
<summary>natural_image</summary>

Symmetrical fractal snowflake pattern on dark background (no text or symbols)
</details>

![](images/27942829fb3ed7559c9ad3274a91ac9e5c808054d635c39ebc81b9d53a09ff08.jpg)

<details>
<summary>natural_image</summary>

Close-up of a frost-covered snowflake on dark, reflective surface (no text or symbols)
</details>

# 科赫雪花绘制

# 用Python绘制科赫曲线

1

2

5

![](images/7a198eb8ed0602079a3dfdf3ea2bba8514f7b8400b98ab66b08bdb226143595d.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line patterns with no text or symbols
</details>

![](images/cbd9823ca1edd2a7114a98c18f20c2503bb7ed98a7294076260d88bbd4123521.jpg)

<details>
<summary>text_image</summary>

取1/3长
60度
</details>

每分隔一次为一阶

# 科赫雪花小包裹"实例讲解(上)

![](images/6ba0c316f116355407c5974efa15eb0324f18be01fd1e5514112245f2c710838.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/3f2935ab4f1188f519cf26b70bb2c5cfdabdb247467405981da3b076c9350990.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 科赫雪花小包裹(上)

# 科赫曲线的绘制

![](images/4e1601195b52fef20787c457af2a09670fa2851f64f4b939adc28ebdf1c8e2cb.jpg)

<details>
<summary>text_image</summary>

Python Turtle Graphics
绘制n阶科赫曲线线段
</details>

# 科赫雪花小包裹(上)

#KochDrawV1.py

import turtle

def koch(size, n):

if n == 0:

turtle.fd(size)

else:

for angle in [0, 60, -120, 60]:

turtle.left(angle)

koch(size/3, n-1)

# 科赫曲线的绘制

递归思想：函数+分支  
递归链条：线段的组合  
递归基例：初识线段

#KochDrawV1.py   
```python
import turtle
def koch(size, n):
    if n == 0:
    turtle.fd(size)
    else:
    for angle in [0, 60, -120, 60]:
    turtle.left(angle)
    koch(size/3, n-1)
def main():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600, 3) # 3阶科赫曲线，阶数
    turtle.hideturtle()
main() 
```

# 科赫雪花小包裹(上)

# 科赫曲线的绘制

#KochDrawV2.py   
```python
import turtle
def koch(size, n):
    ...(略) 
```  
def main():

```lua
turtle.setup(600, 600)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.pensize(2)
level = 3 # 3阶科赫雪花，阶数
koch(400, level)
turtle.right(120)
koch(400, level)
turtle.right(120)
koch(400, level)
turtle.hideturtle()
main() 
```

# 科赫雪花小包裹(上)

# 科赫曲线的绘制

![](images/85486fdff05a0d91dc117906d95e584875b9fd62b7928feca1ee460cdca7ebdf.jpg)

# 科赫雪花的绘制

#KochDrawV2.py   
import turtle  
```txt
def koch(size, n): 
```  
…(略)

def main():   
```txt
turtle.setup(600, 600)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.pensize(2)
level = 3 # 3阶科赫雪花，阶数
koch(400, level)
turtle.right(120)
koch(400, level)
turtle.right(120)
koch(400, level)
turtle.hideturtle() 
```  
main()

# 科赫雪花小包裹(上)

![](images/d5b55039ffee1b41fb52ae8f6579be1a352c2d90ca9b5aa6beb700bcc9d5f290.jpg)

Python Turtle Graphics

![](images/2e32a1b4c840b7b4de5d8282494ffd74180514055f0d9836cf3c53e2bbe02ad4.jpg)

![](images/bd43fffaaad945c2312629afccaab3d48e33ffa2c874e173c0be8a7d4528ecf0.jpg)

![](images/cc5cf3fba7f84590c73acbfd51183367d48c722c8f9d27060abafbcf5cc3a936.jpg)

![](images/5e4f9b9c72c7089f9c1227009636d8d02b146eaaad8b4b5c63e033919cce1028.jpg)

<details>
<summary>natural_image</summary>

Geometric pattern with a central orange triangle surrounded by black zigzag lines forming a symmetrical design (no text or symbols)
</details>

# 准备好电脑，与老师一起编码吧！

# 科赫雪花小包裹"实例讲解(下)

![](images/00f08e3a0766eb7ff6ae1e9e66c08354ea1103a42964b622dd89e0ba42283d4f.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/8d7c4dbbbdea908f43ca83c069d4c66e246983d08bcb6cf2c4b1d94eb91075d5.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 科赫雪花小包裹(下)

打包才能上路…

pyinstaller –i curve.ico –F KochDrawV2.py

![](images/466c9a27c288b506c3307222cd2dc877e3e6547bc74c00247ec450f200f222a3.jpg)

![](images/f828cf1552d1fd6f664b89caecf8f46429af4b161297702e8c39497c83061d2a.jpg)

![](images/504b764aac2dbae34e673708686e4dfd8e5facd907474c4ec063acfa81f7e013.jpg)

KochDrawV2

![](images/958bb0bb164326c9e92aedc461fc62285bf1ccb77b68215a286807295e535760.jpg)

![](images/376fac4f4c46e13ffa4b8a2dd2614f84e07e42322b7fbf077137e8022e42255c.jpg)

KochDrawV2

对编写后的科赫雪花代码进行打包处理

# 科赫雪花小包裹(下)

![](images/fef80af139ff293241b79a0711e1dc79c70e46d1fe6978bc4ec572ce232731ad.jpg)

<details>
<summary>text_image</summary>

D:\PYECourse>pyinstaller -i curve.ico -F KochDrawV2.py
62 INFO: PyInstaller: 3.3.1
62 INFO: Python: 3.6.4
62 INFO: Platform: Windows-10-10.0.15063-SPO
62 INFO: wrote D:\PYECourse\KochDrawV2.spec
62 INFO: UPX is not available.
62 INFO: Extending PYTHONPATH with paths
['D:\\PYECourse', 'D:\\PYECourse']
62 INFO: checking Analysis
62 INFO: Building Analysis because out00-Analysis.toc is non
existent
62 INFO: Initializing module dependency graph...
62 INFO: Initializing module graph hooks...
62 INFO: Analyzing base_library.zip ...
</details>

![](images/d520b9fa14ca84d693dbc21987a140d67c8a02f7b9e0fb80970666766b7827b2.jpg)

<details>
<summary>natural_image</summary>

Simple icon of a green abstract node or structure inside a black square, labeled 'KochDrawV2' below (no other text or symbols)
</details>

# 准备好电脑，与老师一起编码吧！

# 科赫雪花小包裹"举一反三

![](images/e6e858fda54eec2ce02136209c75a48aceeece29bcfbec4449bb4274a216f506.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/926ffa640700d98d65ede770e466c7ae5e899fc8cf62bc54cafbeb6f9c789e07.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

#KochDrawV2.py   
import turtle  
def koch(size, n):   
```txt
if n == 0: 
```

```txt
turtle.fd(size)
```  
else:

```txt
for angle in [0, 60, -120, 60]:
turtle.left(angle)
koch(size/3, n-1) 
```

def main():   
```lua
turtle.setup(600, 600)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.pensize(2) 
```

```txt
level = 3 # 3阶科赫雪花，阶数
```

```txt
koch(400, level) 
```

```javascript
turtle.right(120) 
```

```txt
koch(400, level) 
```

```javascript
turtle.right(120) 
```

```txt
koch(400, level) 
```

```javascript
turtle.hideturtle() 
```  
main()

![](images/277ec79b645eeacb08484df54326b5789f6f76f2e11e7e9561fbd00efde08abe.jpg)

Python Turtle Graphics

![](images/1ec4fdeba6867f15b4fb6fc4cc9a52936cd2445a65878af43b2ca1cde1fa7976.jpg)

![](images/e985c44e37d1a9f96f4b0e8bad9b46159eb39d925411a6c8e9e306e39e4990d3.jpg)

![](images/8b33230563cd035278af09e0bef18d31761c1d4aa29250979959b215f6ae0f53.jpg)

![](images/4ca17c10fa611869d0e3cba8b96c933ec032821f7e4110de7800539784d9c609.jpg)

<details>
<summary>natural_image</summary>

Fractal geometric pattern composed of interlocking zigzag shapes (no text or symbols)
</details>

# 举一反三

# 绘制条件的扩展

修改分形几何绘制阶数  
修改科赫曲线的基本定义及旋转角度  
修改绘制科赫雪花的基础框架图形

![](images/b943b5b1329430794f84352f510c47be75563f2f23e40659454de753fa4cadd8.jpg)

<details>
<summary>natural_image</summary>

Pure electrical circuit lines without any symbols
</details>

90度

# 举一反三

# 分形几何千千万

康托尔集、谢尔宾斯基三角形、门格海绵…  
龙形曲线、空间填充曲线、科赫曲线…   
函数递归的深入应用…

# 第6章 辅学内容

![](images/aae74b5b7ad10d34ad8eea251823f934ce252b41677274e65e286eb43cdbc414.jpg)

python

嵩 天

北京理工大学

pythom

# 前课复习

# 数字类型及操作

整数类型的无限范围及4种进制表示  
- 浮点数类型的近似无限范围、小尾数及科学计数法  
- +、-、\*、/、//、%、\*\*、二元增强赋值操作符   
- abs()、divmod()、pow()、round()、max()、min()  
int()、float()、complex()

# 字符串类型及操作

正向递增序号、反向递减序号、<字符串>[M:N:K]   
- +、\*、len()、str()、hex()、oct()、ord()、chr()  
- .lower()、.upper()、.split()、.count()、.replace()  
- .center()、.strip()、.join(）、.format()格式化

# 程序的分支结构

单分支 if 二分支 if-else 及紧凑形式  
多分支 if-elif-else 及条件之间关系  
- not and or > >= == <= < !=   
异常处理 try-except-else-finally

![](images/bfe9a2f971e76de500531c758051e1443d83b8b922d361ba9921b2d92ff735f8.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with a blue line at the base (no text or symbols)
</details>

# 程序的循环结构

- for…in 遍历循环: 计数、字符串、列表、文件…  
while无限循环   
- continue和break保留字: 退出当前循环层次  
- 循环else的高级用法: 与break有关

# 函数的定义与使用

使用保留字def定义函数，lambda定义匿名函数  
可选参数(赋初值)、可变参数(\*b)、名称传递  
保留字return可以返回任意多个结果  
保留字global声明使用全局变量，一些隐式规则

![](images/2e112e642fabaabcb001f7cd50b74ddc507bd1ec1a319ffac3fde017df5e5a5a.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with wheels, no text or symbols present
</details>

# 代码复用与函数递归

模块化设计：松耦合、紧耦合  
- 函数递归的2个特征：基例和链条  
函数递归的实现：函数 + 分支结构

![](images/90d516bd50638499d147c945234bdf16e76fd4a6a228786a24a608a268c4d81f.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle on a blue track (no text or symbols)
</details>

# 本课概要

# 第6章 组合数据类型

3.14

从一个数据到一组数据

![](images/778912ebaba519f2505784892e74bfbf8758a6af30fbaf702c12ed76c640bac1.jpg)

3.1413

3.1404

3.1398

3.1401 3.1376

3.1349

一个数据

表达一个含义

一组数据

![](images/e917b849d8840e25a6a60de932a2bf752e85fadca21559e531d6a8130d31c715.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with a blue horizontal bar at the base (no text or symbols)
</details>

表达一个或多个含义

# 第6章 组合数据类型

![](images/e26380f8079dd6e661acc5a23ba074f9c7ac6f3a08024adc8065529cc6a4a8e7.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

- 6.1 集合类型及操作  
6.2 序列类型及操作  
元组类型  
列表类型  
- 6.3 实例9: 基本统计值计算  
6.4 字典类型及操作  
6.5 模块5: jieba库的使用  
- 6.6 实例10: 文本词频统计

![](images/d791f75ac70c17641f03bb04f7de0a5c9fb9686a9d6429b4d177e56627d195b3.jpg)

![](images/7e060c1a1fb2b4fc78d93e6f52fed42df4c846602a37be729cef2845da51ad52.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with blue lane markings (no text or symbols)
</details>

# 第6章 组合数据类型

# 方法论

![](images/50fce509deb5722e2a12db5218dff4cbb0dcf06b5517b0e665cd9566144c1132.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

\- Python三种主流组合数据类型的使用方法

# 实践能力

\- 学会编写处理一组数据的程序

![](images/89bb7c0fbe4050c9fe701ed695b5037c50f29065b31dc59fea3532196b8a9e17.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with no visible text or symbols
</details>

# 练习与作业

# 第6章 组合数据类型

![](images/5f2cf95193888e88fbc85ff16a23a68f409caaf3eb8efb3485127eca63ef4a39.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

# 练习 (可选)

5道编程题 @Python123

# 作业

15道单选题 @Python123

![](images/e3ce9f7ff5161afa78b464996f68737d49cf53620509325d54f61d55c3c175a0.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with a blue line at the base (no text or symbols)
</details>

# 集合类型及操作

![](images/66748fb44c5442ae519a9393518d1c326ad65b66f7c8d90d44d5774079da7acd.jpg)

python

嵩 天

北京理工大学

pythom

# 单元开篇

# 集合类型及操作

![](images/b08cf20d05fad38597f384f5223e308373d05547473c9aa535708e9ce2000d6c.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

集合类型定义  
集合操作符  
集合处理方法  
- 集合类型应用场景

![](images/679c1030423335f25f34a5fc0b2fd2a058f5ba1a76a8c9e060fd8627b4152f63.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with wheels and a blue horizontal bar (no text or symbols)
</details>

# 集合类型定义

![](images/aa038e74ee92193a52ace14dc289b02de2e6f90f731bb3cf9e6e98252fb85662.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 集合类型的定义

# 集合是多个元素的无序组合

集合类型与数学中的集合概念一致  
- 集合元素之间无序，每个元素唯一，不存在相同元素  
集合元素不可更改，不能是可变数据类型 为什么？

# 集合类型的定义

# 集合是多个元素的无序组合

- 集合用大括号 {} 表示，元素间用逗号分隔  
- 建立集合类型用 {} 或 set()  
建立空集合类型，必须使用set()

# 集合类型的定义

```txt
>>> A = {"python", 123, ("python", 123)} #使用{}建立集合
{123, 'python', ('python', 123)}
>>> B = set("pypy123") #使用set()建立集合
{'1', 'p', '2', '3', 'y'}
>>> C = {"python", 123, "python", 123}
{'python', 123} 
```

# 集合操作符

# 集合间操作

![](images/ef02abcb2afa22d7665d9f0f0b5eaa176b4660a93aa1b2420ebc81a825e1ef3c.jpg)

<details>
<summary>text_image</summary>

S
T
</details>

S | T 并

![](images/45fc2056020b5b31d711416f60e4fc0abee5eac7cb4adf7751632af8ed860ce0.jpg)

<details>
<summary>text_image</summary>

S
T
</details>

S - T 差

![](images/993fc2687d799a23ef37875bf82c8e16c0c723b8f8f4df374e7f0777f4bf6b29.jpg)

<details>
<summary>text_image</summary>

S
T
</details>

S & T 交

![](images/16fbf7c8e4e13a0d4e4d5c26f2ca27ada562bcf845882f8d176974da9d2c8507.jpg)

<details>
<summary>text_image</summary>

S
T
</details>

S ^ T补

# 集合操作符

# 6个操作符

<table><tr><td>操作符及应用</td><td>描述</td></tr><tr><td>S | T</td><td>返回一个新集合,包括在集合S和T中的所有元素</td></tr><tr><td>S - T</td><td>返回一个新集合,包括在集合S但不在T中的元素</td></tr><tr><td>S &amp; T</td><td>返回一个新集合,包括同时在集合S和T中的元素</td></tr><tr><td>S ^ T</td><td>返回一个新集合,包括集合S和T中的非相同元素</td></tr><tr><td>S &lt;= T 或 S &lt; T</td><td>返回True/False,判断S和T的子集关系</td></tr><tr><td>S &gt;= T 或 S &gt; T</td><td>返回True/False,判断S和T的包含关系</td></tr></table>

# 集合操作符

# 4个增强操作符

<table><tr><td>操作符及应用</td><td>描述</td></tr><tr><td>S |= T</td><td>更新集合S,包括在集合S和T中的所有元素</td></tr><tr><td>S -= T</td><td>更新集合S,包括在集合S但不在T中的元素</td></tr><tr><td>S &amp;= T</td><td>更新集合S,包括同时在集合S和T中的元素</td></tr><tr><td>S ^= T</td><td>更新集合S,包括集合S和T中的非相同元素</td></tr></table>

# 集合类型的定义

$$
\ggg A = \{\text { "p" }, \text { "y" }, 1 2 3 \}
$$

$$
\ggg B = \text { set("pypy123") }
$$

$$
\ggg A - B
$$

$$
\ggg \quad A \& B
$$

$$
\ggg \mathrm{A} ^ {\wedge} \mathrm{B}
$$

$$
\{1 2 3 \}
$$

$$
\{^ {\prime} p ^ {\prime}, ^ {\prime} y ^ {\prime} \}
$$

$$
\{^ {\prime} 2 ^ {\prime}, 1 2 3, ^ {\prime} 3 ^ {\prime}, ^ {\prime} 1 ^ {\prime} \}
$$

$$
\ggg B - A
$$

$$
\ggg A | B
$$

$$
\{^ {\prime} 3 ^ {\prime}, ^ {\prime} 1 ^ {\prime}, ^ {\prime} 2 ^ {\prime} \}
$$

$$
\{^ {\prime} 1 ^ {\prime}, ^ {\prime} p ^ {\prime}, ^ {\prime} 2 ^ {\prime}, ^ {\prime} y ^ {\prime}, ^ {\prime} 3 ^ {\prime}, 1 2 3 \}
$$

# 集合处理方法

![](images/f0057ac03d3e5f725082430b7aff844129f605574a8f91cef477107b542ef6d1.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 集合处理方法

<table><tr><td>操作函数或方法</td><td>描述</td></tr><tr><td>S.add(x)</td><td>如果x不在集合S中,将x增加到S</td></tr><tr><td>S.discard(x)</td><td>移除S中元素x,如果x不在集合S中,不报错</td></tr><tr><td>S.remove(x)</td><td>移除S中元素x,如果x不在集合S中,产生KeyError异常</td></tr><tr><td>S.clear()</td><td>移除S中所有元素</td></tr><tr><td>S.pop()</td><td>随机返回S的一个元素,更新S,若S为空产生KeyError异常</td></tr></table>

# 集合处理方法

<table><tr><td>操作函数或方法</td><td>描述</td></tr><tr><td>S.copy()</td><td>返回集合S的一个副本</td></tr><tr><td>len(S)</td><td>返回集合S的元素个数</td></tr><tr><td>x in S</td><td>判断S中元素x,x在集合S中,返回True,否则返回False</td></tr><tr><td>x not in S</td><td>判断S中元素x,x不在集合S中,返回False,否则返回True</td></tr><tr><td>set(x)</td><td>将其他类型变量x转变为集合类型</td></tr></table>

# 集合处理方法

```python
>>> try:
>>> A = {"p", "y", 123}    while True:
>>> for item in A:    print(A.pop(), end=""))
    print(item, end="") except:
p123y    pass
>>> A    p123y
{'p', 123, 'y'}    >>> A
    set() 
```

![](images/ddad635949601da60be930986f0cbc02d1c3be6d250c68a43a399d6ca1620239.jpg)

<details>
<summary>text_image</summary>

集合类型应用场景
</details>

# 集合类型应用场景

# 包含关系比较

>>> "p" in {"p", "y" , 123}

True

>>> {"p", "y"} >= {"p", "y" , 123}

False

# 集合类型应用场景

# 数据去重：集合类型所有元素无重复

>>> ls = ["p", y", "y", 123]   
>>> s = set(ls) # 利用了集合无重复元素的特点  
{'p', 'y', 123}   
>>> lt = list(s) # 还可以将集合转换为列表  
['p', 'y', 123]

# 单元小结

# 集合类型及操作

- 集合使用{}和set()函数创建  
- 集合间操作：交(&)、并(|)、差(-)、补(^)、比较(>=<)  
- 集合类型方法：.add()、.discard()、.pop()等  
- 集合类型主要应用于：包含关系比较、数据去重

![](images/fbeb5a54bfc3b2e3a0721334a33871daf56872b96a3c0c6e7dc635c8fc937145.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with blue lane line (no text or symbols)
</details>

# 序列类型及操作

![](images/1364589024aa9c91909a82aa63a6c9379cd2d7977ed0084b9a42f738a081fcf4.jpg)

python

嵩 天

北京理工大学

pythom

# 单元开篇

# 序列类型及操作

![](images/e57d1ccb4f54bb153f43a7c6aa5f7f28c3038c8a48083304ac80cd3d338ff8d9.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

序列类型定义  
序列处理函数及方法  
元组类型及操作  
列表类型及操作  
序列类型应用场景

![](images/d6ea6f9faed87c9154a0f621eea82bdfa4fc682db3e1f2d6232d0d557946ef36.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with a blue line at the base (no text or symbols)
</details>

# 序列类型定义

# 序列类型定义

# 序列是具有先后关系的一组元素

序列是一维元素向量，元素类型可以不同  
类似数学元素序列： s0, s1, … , sn-1 $s _ { \theta } , ~ s _ { 1 } , ~ . . . ~ , ~ s _ { n - 1 }$   
元素间由序号引导，通过下标访问序列的特定元素

# 序列类型定义

# 序列是一个基类类型

字符串类型

元组类型

列表类型

![](images/8c5bae82326137fae79d11acb0d14f128f60e41d5db7659dae268637a940aebe.jpg)

<details>
<summary>natural_image</summary>

Pure horizontal and vertical blue lines forming a cross shape (no text or symbols)
</details>

序列类型

# 序列类型定义

# 序号的定义

反向递减序号

<table><tr><td>-5</td><td>-4</td><td>-3</td><td>-2</td><td>-1</td></tr><tr><td>&quot;BIT&quot;</td><td>3.1415</td><td>1024</td><td>(2,3)</td><td>[&quot;中国&quot;,9]</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td colspan="5">正向递增序号</td></tr></table>

# 序列处理函数及方法

![](images/cbd4e280280030e1bedcf85c25a92cc0bc94b8b67673991f761a8987b8db75ce.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/086bb3665a4370a575777b9246fdbc4a6aea92ae46b495ecc879d17b3e456fcf.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 序列类型通用操作符

# 6个操作符

<table><tr><td>操作符及应用</td><td>描述</td></tr><tr><td>x in s</td><td>如果x是序列s的元素,返回True,否则返回False</td></tr><tr><td>x not in s</td><td>如果x是序列s的元素,返回False,否则返回True</td></tr><tr><td>s + t</td><td>连接两个序列s和t</td></tr><tr><td>s*n 或 n*s</td><td>将序列s复制n次</td></tr><tr><td>s[i]</td><td>索引,返回s中的第i个元素,i是序列的序号</td></tr><tr><td>s[i: j] 或 s[i: j: k]</td><td>切片,返回序列s中第i到j以k为步长的元素子序列</td></tr></table>

# 序列类型操作实例

>>> ls = ["python", 123, ".io"]

>>> ls[::-1]

['.io', 123, 'python']

>>> s = "python123.io"

>>> s[::-1]

'oi.321nohtyp

# 序列类型通用函数和方法

5个函数和方法

<table><tr><td>函数和方法</td><td>描述</td></tr><tr><td>len(s)</td><td>返回序列s的长度</td></tr><tr><td>min(s)</td><td>返回序列s的最小元素,s中元素需要可比较</td></tr><tr><td>max(s)</td><td>返回序列s的最大元素,s中元素需要可比较</td></tr><tr><td>s.index(x)或s.index(x,i,j)</td><td>返回序列s从i开始到j位置中第一次出现元素x的位置</td></tr><tr><td>s.count(x)</td><td>返回序列s中出现x的总次数</td></tr></table>

# 序列类型操作实例

```python
>>> ls = ["python", 123, ".io"]
>>> len(ls)
3
>>> s = "python123.io"
>>> max(s)
'y' 
```

# 元组类型及操作

![](images/844583c710ea75d723cbd5e85f105b25b9d7d0ab9af9f6d4dfa2ee550cf81fff.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 元组类型定义

# 元组是序列类型的一种扩展

元组是一种序列类型，一旦创建就不能被修改

使用小括号 () 或 tuple() 创建，元素间用逗号 , 分隔

可以使用或不使用小括号

def func():

return 1,2

# 元组类型定义

>>> creature = "cat", "dog", "tiger", "human"   
>>> creature

('cat', 'dog', 'tiger', 'human')

>>> color = (0x001100, "blue", creature)   
>>> color

(4352, 'blue', ('cat', 'dog', 'tiger', 'human'))

# 元组类型操作

# 元组继承序列类型的全部通用操作

元组继承了序列类型的全部通用操作  
元组因为创建后不能修改，因此没有特殊操作  
使用或不使用小括号

# 元组类型操作

>>> creature = "cat", "dog", "tiger", "human"

>>> creature[::-1]

('human', 'tiger', 'dog', 'cat')

>>> color = (0x001100, "blue", creature)

>>> color[-1][2]

'tiger'

# 列表类型及操作

![](images/064ea6def219fb3a320245f90e55cd16f334509f8147e7081059ff3dd93e62fb.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 列表类型定义

# 列表是序列类型的一种扩展，十分常用

列表是一种序列类型，创建后可以随意被修改  
使用方括号 [] 或list() 创建，元素间用逗号 , 分隔  
列表中各元素类型可以不同，无长度限制

# 列表类型定义

>>> ls = ["cat", "dog", "tiger", 1024]

>>> ls

['cat', 'dog', 'tiger', 1024]

>>> lt = ls

>>> lt

['cat', 'dog', 'tiger', 1024]

ls

lt

['cat','dog','tiger',1024]

方括号 [] 真正创建一个列表，赋值仅传递引用

# 列表类型操作函数和方法

<table><tr><td>函数或方法</td><td>描述</td></tr><tr><td>ls[i] = x</td><td>替换列表ls第i元素为x</td></tr><tr><td>ls[i: j: k] = lt</td><td>用列表lt替换ls切片后所对应元素子列表</td></tr><tr><td>del ls[i]</td><td>删除列表ls中第i元素</td></tr><tr><td>del ls[i: j: k]</td><td>删除列表ls中第i到第j以k为步长的元素</td></tr><tr><td>ls += lt</td><td>更新列表ls,将列表lt元素增加到列表ls中</td></tr><tr><td>ls *= n</td><td>更新列表ls,其元素重复n次</td></tr></table>

# 列表类型操作

>>> ls = ["cat", "dog", "tiger", 1024]

>>> ls[1:2] = [1, 2, 3, 4]

['cat', 1, 2, 3, 4, 'tiger', 1024]

>>> del ls[::3]

[1, 2, 4, 'tiger']

>>> ls\*2

[1, 2, 4, 'tiger', 1, 2, 4, 'tiger']

# 列表类型操作函数和方法

<table><tr><td>函数或方法</td><td>描述</td></tr><tr><td>ls.append(x)</td><td>在列表ls最后增加一个元素x</td></tr><tr><td>ls.clear()</td><td>删除列表ls中所有元素</td></tr><tr><td>ls.copy()</td><td>生成一个新列表,赋值ls中所有元素</td></tr><tr><td>ls.insert(i,x)</td><td>在列表ls的第i位置增加元素x</td></tr><tr><td>ls.pop(i)</td><td>将列表ls中第i位置元素取出并删除该元素</td></tr><tr><td>ls.remove(x)</td><td>将列表ls中出现的第一个元素x删除</td></tr><tr><td>ls.reverse()</td><td>将列表ls中的元素反转</td></tr></table>

# 列表类型操作

>>> ls = ["cat", "dog", "tiger", 1024]

>>> ls.append(1234)

['cat', 'dog', 'tiger', 1024, 1234]

>>> ls.insert(3, "human")

['cat', 'dog', 'tiger', 'human', 1024, 1234]

>>> ls.reverse()

[1234, 1024, 'human', 'tiger', 'dog', 'cat']

# 列表功能默写

定义空列表lt  
向lt新增5个元素  
修改lt中第2个元素  
向lt中第2个位置增加一个元素  
从lt中第1个位置删除一个元素  
删除lt中第1-3位置元素  
判断lt中是否包含数字0  
向lt新增数字0  
返回数字0所在lt中的索引  
lt的长度  
lt中最大元素  
清空lt

# 列表功能默写

定义空列表lt  
>>> lt = []   
向lt新增5个元素  
>>> lt += [1,2,3,4,5]   
修改lt中第2个元素  
>>> lt[2] = 6   
向lt中第2个位置增加一个元素  
>>> lt.insert(2, 7)   
从lt中第1个位置删除一个元素  
>>> del lt[1]   
删除lt中第1-3位置元素  
>>> del lt[1:4]

# 列表功能默写

>>> 0 in lt

>>> lt.append(0)

>>> lt.index(0)

>>> len(lt)

>>> max(lt)

>>> lt.clear()

判断lt中是否包含数字0

向lt新增数字0

返回数字0所在lt中的索引

lt的长度

lt中最大元素

清空lt

![](images/53dad886883e903473ecfe08e21c787974222cf612d879de018885eb9e1011c5.jpg)

<details>
<summary>text_image</summary>

序列类型应用场景
</details>

# 序列类型应用场景

# 数据表示：元组 和 列表

元组用于元素不改变的应用场景，更多用于固定搭配场景  
列表更加灵活，它是最常用的序列类型  
最主要作用：表示一组有序数据，进而操作它们

# 序列类型应用场景

# 元素遍历

for item in ls • for item in tp • • :

<语句块>

<语句块>

# 序列类型应用场景

# 数据保护

# 如果不希望数据被程序所改变，转换成元组类型

>>> ls = ["cat", "dog", "tiger", 1024]

>>> lt = tuple(ls)

>>> lt

('cat', 'dog', 'tiger', 1024)

# 单元小结

# 序列类型及操作

序列是基类类型，扩展类型包括：字符串、元组和列表  
元组用()和tuple()创建，列表用[]和set()创建  
- 元组操作与序列操作基本相同  
列表操作在序列操作基础上，增加了更多的灵活性

![](images/214464d9511c8e9a023dd59ad85f7c2b0d7b23268d50d707eede7c04a0579463.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with wheels, no text or symbols visible
</details>

# 实例9: 基本统计值计算

![](images/c1f8f945cfc816294c00c5895fcf9072ba91cf4d69bc5a54aa9bec86300e3b3d.jpg)

python

嵩 天

北京理工大学

pythom

# 基本统计值计算"问题分析

![](images/f92a0453c2613bce5a8451bb418f1e0d9c3574b58370d6877c567a8df6533630.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/bcaec475fb6adbb4e6482240906e43d49e205edd97cb0ba4725c3933b566cc0a.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 问题分析

# 基本统计值

需求：给出一组数，对它们有个概要理解  
该怎么做呢？

总个数、求和、平均值、方差、中位数…

# 问题分析

# 基本统计值

总个数：len()  
求和：for … in   
平均值：求和/总个数

方差：

各数据与平均数差的平方的和的平均数

中位数：排序，然后…

奇数找中间1个，偶数找中间2个取平均

# 基本统计值计算"实例讲解

![](images/d06970ecccce0fac235b921ef3e5a1ace1ad4325ff556a5ed438b2ec8fc76949.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/1c53d834a26302c920a0e5b4dafaee681cc02581df101c250b2b5b6461521f10.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 基本统计值计算

#CalStatisticsV1.py   
```python
def getNum():    # 获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入数字(回车退出): ")
    while iNumStr != "":
    nums.append(eval(iNumStr))
    iNumStr = input("请输入数字(回车退出): ")
    return nums 
```

def mean(numbers): #计算平均值   
```python
s = 0.0
for num in numbers:
    s = s + num
return s / len(numbers) 
```

获取多数据输入

通过函数分隔功能

def dev(numbers, mean): #计算方差   
```python
sdev = 0.0
for num in numbers:
    sdev = sdev + (num - mean)**2
return pow(sdev / (len(numbers)-1), 0.5) 
```

# 基本统计值计算

def median(numbers): #计算中位数  
```python
sorted(numbers)
size = len(numbers)
if size % 2 == 0:
    med = (numbers[size//2-1] + numbers[size//2])/2
else:
    med = numbers[size//2]
return med 
```

# 获取多数据输入

# 通过函数分隔功能

```txt
n = getNum()
m = mean(n) 
```

print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n,m),median(n)))

# 准备好电脑，与老师一起编码吧！

# 基本统计值计算"举一反三

![](images/fb054bc5d8663980f730ae1647426986c5b08b9440dca8b8f5d4d8d66536cb52.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/1dbfa3611f2297476a45a04b18ae2f20baceefb859e56ff46d05eb4870cf8825.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

def dev(numbers, mean): #计算方差   
```python
sdev = 0.0
for num in numbers:
    sdev = sdev + (num - mean)**2
return pow(sdev / (len(numbers)-1), 0.5) 
```

def median(numbers): #计算中位数  
```python
sorted(numbers)
size = len(numbers)
if size % 2 == 0:
    med = (numbers[size//2-1] + numbers[size//2])/2
else:
    med = numbers[size//2]
return med 
```

```txt
n = getNum() 
```

```lisp
m = mean(n) 
```  
print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n,m),median(n)))

```python
#CalStatisticsV1.py
def getNum():    #获取用户不定长度的输入
    nums = []
    iNumStr = input("请输入数字(回车退出): ")
    while iNumStr != "":
    nums.append(eval(iNumStr))
    iNumStr = input("请输入数字(回车退出): ")
    return nums 
```

def mean(numbers): #计算平均值   
```python
s = 0.0
for num in numbers:
    s = s + num
return s / len(numbers) 
```

# 举一反三

# 技术能力扩展

获取多个数据：从控制台获取多个不确定数据的方法  
分隔多个函数：模块化设计方法  
充分利用函数：充分利用Python提供的内容函数

# 字典类型及操作

![](images/54bb4c7a6bbbe7bbf5e4c87fd9ecb83271aab3824a17fc4ce0d0eda41a268f55.jpg)

python

嵩 天

北京理工大学

pythom

# 单元开篇

# 字典类型及操作

![](images/40153a8251b71726c53a744bca1f5b309e95eb687c08b79599d77d0b8444e076.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

字典类型定义  
字典处理函数及方法  
字典类型应用场景

![](images/580b2e2a6272977d6c44cdf76628bcfd78b8260ba1532d836b7c0cd5e66ab166.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with wheels, no text or symbols present
</details>

# 字典类型定义

![](images/f3d1b045b638456eb469753aae1a990948a522c4347eeb1dcaf381486f8e710c.jpg)

<details>
<summary>natural_image</summary>

Geometric diagram of interconnected triangles and dots forming a network (no text or symbols)
</details>

![](images/7c2fef82fbd2b147e3432b7cd9cd58974ce7bb05152b3f96d340090f0f9d4386.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 字典类型定义

# 理解“映射”

# 映射是一种键(索引)和值(数据)的对应

![](images/627d954123f1e0791b1a2711ad3dfeb359afb54ee4d573df345d7e9c09157558.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["内部颜色"] --> C["红色"]
    B["外部颜色"] --> D["黑色"]
    B --> E["蓝色"]
    B --> F["白色"]
    C --> G["内部颜色：蓝色"]
    D --> H["外部颜色：红色"]
```
</details>

# 字典类型定义

# 理解“映射”

# 映射是一种键(索引)和值(数据)的对应

内部颜色：蓝色

外部颜色：红色

![](images/7e533e5b3e0e8204810c4d314918d608637b9c11577cbecaab965b74c68cb431.jpg)

"streetAddr" "中关村南大街5号"

"city" "北京市"

"zipcode" "100081"

# 字典类型定义

# 理解“映射”

# 映射是一种键(索引)和值(数据)的对应

["python", 123, ".io"]

![](images/e0752c8ed1c345b9d281cd5136b2fe7b2ee38690dfdb50b724a20e3fbd0ef981.jpg)  
0

![](images/8b25fd02718e84b6f89e60f5933e35f3c3f17f7428202c412008675c5340cfa1.jpg)  
1

![](images/5bfb793b7d3d795314d52e6bd4e9e7648cc5c696efb4098fb82ab2da85c09784.jpg)  
2

![](images/de68e5e81e26cf8211ca0dfaa9378f5aa168a7a489bf062dbd87987babac2f54.jpg)

内部颜色：蓝色

外部颜色：红色

# 字典类型定义

# 字典类型是 “映射” 的体现

- 键值对：键是数据索引的扩展  
字典是键值对的集合，键值对之间无序   
采用大括号{}和dict()创建，键值对用冒号: 表示  
{<键1>:<值1>, <键2>:<值2>, … <键n>:<值n>}

# 字典类型的用法

# 在字典变量中，通过键获得值

<字典变量> = {<键1>:<值1>, <键n>:<值n>}

<值> = <字典变量>[<键>] <字典变量>[<键>] = <值>

[ ] 用来向字典变量中索引或增加元素

# 字典类型定义和使用

>>> d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}

>>> d

{'中国': '北京', '美国': '华盛顿', '法国': '巴黎'}

>>> d["中国"]

'北京

>>> de = {} ; type(de)

<class 'dict'>

type(x)

返回变量x的类型

# 字典处理函数及方法

![](images/a43a15138260cd7d3f480fb4a1f6356c77614ce39d69ba81f25b2952ecb32a13.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/037aacd37f5f3820b6a2949fd151f234d5639aac6452a179f34752e71ec2192e.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 字典类型操作函数和方法

<table><tr><td>函数或方法</td><td>描述</td></tr><tr><td>del d[k]</td><td>删除字典d中键k对应的数据值</td></tr><tr><td>k in d</td><td>判断键k是否在字典d中,如果在返回True,否则False</td></tr><tr><td>d.keys()</td><td>返回字典d中所有的键信息</td></tr><tr><td>d.values()</td><td>返回字典d中所有的值信息</td></tr><tr><td>d.items()</td><td>返回字典d中所有的键值对信息</td></tr></table>

# 字典类型操作

>>> d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}

>>> "中国" in d

True

>>> d.keys()

dict\_keys(['中国', '美国', '法国'])

>>> d.values()

dict\_values(['北京', '华盛顿', '巴黎'])

# 字典类型操作函数和方法

<table><tr><td>函数或方法</td><td>描述</td></tr><tr><td>d.get(k,)</td><td>键k存在,则返回相应值,不在则返回值</td></tr><tr><td>d.pop(k,)</td><td>键k存在,则取出相应值,不在则返回值</td></tr><tr><td>d.popitem()</td><td>随机从字典d中取出一个键值对,以元组形式返回</td></tr><tr><td>d.clear()</td><td>删除所有的键值对</td></tr><tr><td>len(d)</td><td>返回字典d中元素的个数</td></tr></table>

# 字典类型操作

>>> d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}

>>> d.get("中国","伊斯兰堡")

'北京

>>> d.get("巴基斯坦","伊斯兰堡")

伊斯兰堡

>>> d.popitem()

('美国', '华盛顿')

# 字典功能默写

定义空字典d  
>>> d = {}   
向d新增2个键值对元素  
>>> d["a"] = 1; d["b"] = 2   
修改第2个元素  
$> > > ~ \mathsf { d } [ " \mathsf { b } " ] ~ = ~ 3$   
判断字符"c"是否是d的键   
>>> "c" in d   
计算d的长度  
>>> len(d)   
清空d   
>>> d.clear()

![](images/d7f46bf7b90c1d1a35f8336ee82e801e1fe9da6f2fc137379072780d8f622089.jpg)

<details>
<summary>text_image</summary>

字典类型应用场景
</details>

# 字典类型应用场景

# 映射的表达

映射无处不在，键值对无处不在  
例如：统计数据出现的次数，数据是键，次数是值  
最主要作用：表达键值对数据，进而操作它们

# 字典类型应用场景

# 元素遍历

for k in d :

<语句块>

# 单元小结

# 字典类型及操作

映射关系采用键值对表达  
字典类型使用{}和dict()创建，键值对之间用:分隔  
d[key] 方式既可以索引，也可以赋值  
字典类型有一批操作方法和函数，最重要的是.get()

![](images/05e15b28502def12a70ab98c5c2aa1c9b46df2f4c64434dfab693f53aa6e5d76.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with wheels and a blue horizontal bar (no text or symbols)
</details>

# 模块5: jieba库的使用

![](images/4b88d8c6f04f0514a0d9bed3ecafb0ff3ae4762a506df4bcd5f54a0663451627.jpg)

python

嵩 天

北京理工大学

pythom

![](images/8f323493b4bc7a9ad5d66a83f50248998907daddcca7417a6ac13928d825d8dd.jpg)

<details>
<summary>text_image</summary>

jieba库基本介绍
</details>

# jieba库概述

# jieba是优秀的中文分词第三方库

中文文本需要通过分词获得单个的词语  
jieba是优秀的中文分词第三方库，需要额外安装  
jieba库提供三种分词模式，最简单只需掌握一个函数

# jieba库的安装

# (cmd命令行) pip install jieba

![](images/8e21765993463ff34e1553c9eada7e1071b808502d7b8417ebdcd7f2779d46c3.jpg)

<details>
<summary>text_image</summary>

C:\Users\Tian Song>pip install jieba
Collecting jieba
Downloading jieba-0.39.zip (7.3MB)
4% | ■ | | 327kB 94kB/s eta 0:01:14
</details>

![](images/d4d6ddce4d69e683239c0be70168c1df8d8d06e525f3fc8e68b38e707324b9a2.jpg)

<details>
<summary>text_image</summary>

命令提示符
98%
99%
99%
99%
99%
99%
99%
99%
100%
7.3MB 61kB/s
Installing collected packages: jieba
Running setup.py install for jieba ... done
Successfully installed jieba-0.39
C:\Users\Tian Song>
</details>

# jieba分词的原理

# Jieba分词依靠中文词库

利用一个中文词库，确定汉字之间的关联概率  
汉字间概率大的组成词组，形成分词结果  
除了分词，用户还可以添加自定义的词组

![](images/24f5e9814b22843d3fb8b406c059a5baca4a4143dd19deb39947577afbfd9553.jpg)

<details>
<summary>text_image</summary>

jieba库使用说明
</details>

# jieba分词的三种模式

# 精确模式、全模式、搜索引擎模式

精确模式：把文本精确的切分开，不存在冗余单词  
全模式：把文本中所有可能的词语都扫描出来，有冗余  
- 搜索引擎模式：在精确模式基础上，对长词再次切分

# jieba库常用函数

<table><tr><td>函数</td><td>描述</td></tr><tr><td>jieba.lcut(s)</td><td>精确模式,返回一个列表类型的分词结果&gt;&gt;&gt;jieba.lcut(&quot;中国是一个伟大的国家&quot;)[ &#x27;中国&#x27;, &#x27;是&#x27;, &#x27;一个&#x27;, &#x27;伟大&#x27;, &#x27;的&#x27;, &#x27;国家&#x27;]</td></tr><tr><td>jieba.lcut(s,cut_all=True)</td><td>全模式,返回一个列表类型的分词结果,存在冗余&gt;&gt;&gt;jieba.lcut(&quot;中国是一个伟大的国家&quot;,cut_all=True)[ &#x27;中国&#x27;, &#x27;国是&#x27;, &#x27;一个&#x27;, &#x27;伟大&#x27;, &#x27;的&#x27;, &#x27;国家&#x27;]</td></tr></table>

# jieba库常用函数

<table><tr><td>函数</td><td>描述</td></tr><tr><td>jieba.lcut_for_search(s)</td><td>搜索引擎模式,返回一个列表类型的分词结果,存在冗余&gt;&gt;&gt;jieba.lcut_for_search(“中华人民共和国是伟大的”)[‘中华’,‘华人’,‘人民’,‘共和’,‘共和国’,‘中华人民共和国’,‘是’,‘伟大’,‘的’]</td></tr><tr><td>jieba.add_word(w)</td><td>向分词词典增加新词w&gt;&gt;&gt;jieba.add_word(“蟒蛇语言”)</td></tr></table>

# jieba分词要点

jieba.lcut(s)

# 实例10: 文本词频统计

![](images/de62227dae47958c38daed805acdc4a440ed92f8147b14243d5274618a1850ae.jpg)

python

嵩 天

北京理工大学

pythom

# "文本词频统计"问题分析

![](images/a50c6d93ba2fc4d78197c897f45c806c9e64d0a780bc67f4d0274a425417dcbb.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/d299ba6959c4d55a52343ee696024d93ecbae071bff3fd252031b34192a712c6.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 问题分析

# 文本词频统计

需求：一篇文章，出现了哪些词？哪些词出现得最多？  
该怎么做呢？

英文文本

![](images/6e04154603f6b176c1d8687d8df3ea220f1ab03efaf1fd14f60cd3c4937baaf7.jpg)

中文文本

# 问题分析

# 文本词频统计

英文文本： 分析词频

https://python123.io/resources/pye/hamlet.txt

中文文本：《三国演义》 分析人物

https://python123.io/resources/pye/threekingdoms.txt

# Hamlet英文词频统计"实例讲解

![](images/4a8ecd12542d7b83752feaab857ed50034a55126ae67fb0164c7c0c3ecc9f553.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/c9750b7690ad3273408eda5e985f3cff7e6aecb5f680c2e0ebe0e9f3223fd1b0.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

#CalHamletV1.py   
```python
def setText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_'{}~':
    txt = txt.replace(ch, " ")
    return txt 
```

```python
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
```

```python
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count)) 
```

![](images/7758956e5a233524c2f43dd2c80d080bab15c5efffc70ca411884a01f2344e16.jpg)

<details>
<summary>text_image</summary>

HAMLET
</details>

文本去噪及归一化  
- 使用字典表达词频