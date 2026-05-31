---
type: source
title: Pythonppt
format: mineru-api-markdown
raw_path: materials/raw/external_ppt/嵩天Python/Pythonppt.pdf
mineru_raw_markdown: materials/markdown/pdf_library_mineru/api_raw/Pythonppt/part_007/full.md
source_pages: 1287
page_range: 1201-1287
generated: 2026-05-24 12:20:18
status: generated_part
---

(略)

angles = np.linspace(0, 2\*np.pi, 6, endpoint=False)

data = np.concatenate((data, [data[0]]))

angles = np.concatenate((angles, [angles[0]]))

fig = plt.figure(facecolor="white")

plt.subplot(111, polar=True)

plt.plot(angles,data,'o-', linewidth=1, alpha=0.2)

plt.fill(angles,data, alpha=0.25)

plt.thetagrids(angles\*180/np.pi, radar\_labels,frac = 1.2)

(略)

![](images/da622ef5bfb73036246c64cf5a39c228c0ed115addd32cd19ce323f10253714a.jpg)

<details>
<summary>radar</summary>

| 类别 | 实验员 | 工程师 | 推销员 | 社会工作者 | 记事员 |
|---|---|---|---|---|---|
| 研究型 (I) | 0.35 | 0.25 | 0.30 | 0.40 | 0.60 |
| 研究型 (R) | 0.30 | 0.35 | 0.25 | 0.70 | 0.30 |
| 技术型 (A) | 0.45 | 0.20 | 0.45 | 0.85 | 0.35 |
| 社会型 (S) | 0.90 | 0.25 | 0.15 | 0.35 | 0.30 |
| 企业型 (E) | 0.35 | 0.40 | 0.85 | 0.30 | 0.35 |
</details>

(略)

```python
plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='large')
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show() 
```

# 霍兰德人格分析雷达图"举一反三

![](images/4f17f4cb096b1803c288a70dc7d927837669c9b1b817ef6d44b13ef7cbc21d9f.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/3c330c324d083b0c922e3712333603b538837e958d3b65ce63f1accaecc2bdb2.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# 举一反三

目标 + 沉浸 + 熟练

编程的目标感：寻找感兴趣的目标，寻(wa)觅(jue)之   
编程的沉浸感：寻找可实现的方法，思(zuo)考(mo)之  
编程的熟练度：练习、练习、再练习，熟练之

# 从Web解析到网络空间

![](images/6807374edb5430b6cfd0d8fb469559eac76a43da1e4b8d772a17d6db0e5dea58.jpg)

python

嵩 天

北京理工大学

pythom

# 单元开篇

# 从Web解析到网络空间

![](images/77c46244fe6935883b913648d496c6680441a16b3cfe054953ee5bdeccc76c31.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

Python库之网络爬虫  
Python库之Web信息提取  
Python库之Web网站开发  
Python库之网络应用开发

![](images/c4db9d471acce91cea69e2751da5879de74b097d808dbbd197dbb4a3c4c199bc.jpg)

<details>
<summary>natural_image</summary>

Silhouette of a person riding a bicycle with a checkered board in the background (no text or symbols)
</details>

# Python库之网络爬虫

![](images/1564cb7d108a3c53451a0c0c18bd514d78d12f0057249902ee96c4f9e354d439.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/3d7a12ccb31fe9bf0d0cf1a6f2682b307b17800d6eaf516b9a3c7f59bdc21196.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之网络爬虫

# Requests: 最友好的网络爬虫功能库

提供了简单易用的类HTTP协议网络爬虫功能  
- 支持连接池、SSL、Cookies、HTTP(S)代理等  
Python最主要的页面级网络爬虫功能库

# Python库之网络爬虫

# Requests: 最友好的网络爬虫功能库

import requests   
```python
r = requests.get('https://api.github.com/user', \
auth=('user', 'pass')) 
```

r.status\_code   
```txt
r.headers['content-type'] 
```  
r.encoding   
r.text

![](images/f3daaab0b619a1df54895659f480327480a3a2835cae832d5550c79a157d0d1d.jpg)

<details>
<summary>text_image</summary>

Requests
http for humans
</details>

# Python库之网络爬虫

# Scrapy: 优秀的网络爬虫框架

- 提供了构建网络爬虫系统的框架功能，功能半成品  
支持批量和定时网页爬取、提供数据处理流程等  
Python最主要且最专业的网络爬虫框架

# Python库之网络爬虫

# Scrapy: Python数据分析高层次应用库

![](images/575df8e4b15601a9459359d37c676ac2fc5ab9d67e9b0bd9f4f51c22a9bb0ff0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["SPIDERS"] -->|1| B["ENGINE"]
    B -->|2| C["SCHEDULER"]
    C -->|3| D["ITEMS/REQUESTS"]
    D -->|4| E["DOWNLOADER"]
    E -->|5| F["RESPONSE REQUESTS"]
    F -->|6| G["ITEMS"]
    G -->|7| H["MIDDLEWARE"]
    H -->|8| I["ITEMI PIPELINES"]
    I -->|ITEMS| J["RESPONSE"]
    J -->|REQUESTS| K["REQUESTS"]
    K -->|REQUESTS| L["RESPONSE"]
    L -->|INTERNET| M["INTERNET"]
```
</details>

https://scrapy.org

# Python库之网络爬虫

# pyspider: 强大的Web页面爬取系统

提供了完整的网页爬取系统构建功能  
支持数据库后端、消息队列、优先级、分布式架构等  
Python重要的网络爬虫类第三方库

# Python库之网络爬虫

# pyspider: 强大的Web页面爬取系统

![](images/7bf0d72705b09385071d076091f144b0f396b754a4c83e02fee0fd42b99fd8ce.jpg)

<details>
<summary>text_image</summary>

pyspider >js_test_sciencedirect
Quickstart 脚本编写指南
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Created on 2014-10-31 13:05:52
import re
from libs.base_handler import *
class Handler(BaseHandler):
    this is a sample handler
    def on_start(self):
    self.crawl('http://www.sciencedirect.com/science/article/pii/S1568494612005741',
    callback=self.detail_page)
    def index_page(self, response):
        for each in response.doc('a').items():
            if re.match('http://www.sciencedirect.com/science/article/pii/\w+$',
    each.attr.href):
        self.crawl(each.attr.href, callback=self.detail_page)
    @config(fetch_type="js")
    def detail_page(self, response):
        self.index_page(response)
        self.crawl(response.doc('HTML>BODY>DIV#page-
area>DIV#rightPane>DIV#rightOuter>DIV#rightInner>DIV.innerPadding>DIV#recommend_rela
ted_articles>OL#relArtist>LI>A.viewMoreArticles.cLink').attr.href,
    callback=self.index_page)
    return {
        "url": response.url,
        "title": response.doc('HTML>BODY>DIV#page-
area>DIV#centerPane>DIV#centerContent>DIV#centerInner>DIV#frag_1>H1.svTitle').text(),
        "authors": ["name": x.text(), "url": x.attr.href} for x in
response.doc('HTML>BODY>DIV#page-
area>DIV#centerPane>DIV#centerContent>DIV#centerInner>DIV#frag_1>UL.authorGroup.noCo
lab>LI.smh5>A.authorName').items"),
        "abstract": response.doc('HTML>BODY>DIV#page-
area>DIV#centerPane>DIV#centerContent>DIV#centerInner>DIV#frag_2>DIV.abstract.svAbst
FactSP").text(),
    "abstract": "keywords": [x.text() for x in response.doc('HTML>BODY>DIV#page-
author#: [][name': J.R Lothian],
        "url": http://www.sciencedirect.com/science/article/pii/S02615606020004
'keywords: [],
    'title': 'Editorial',
    'url': u:http://www.sciencedirect.com/science/article/pii/S0261560602000463'}
</details>

http://docs.pyspider.org

# Python库之Web信息提取

![](images/afa078c1097a97e0d0064fa20d5552b30cb033f8e36bac086521869cf8d67b66.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/4d722cea034d3f86d48afa57a2b3514912ae3cb3b254726fccf7e893d4e24ca1.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之Web信息提取

# Beautiful Soup: HTML和XML的解析库

提供了解析HTML和XML等Web信息的功能  
又名beautifulsoup4或bs4，可以加载多种解析引擎  
常与网络爬虫库搭配使用，如Scrapy、requests等

# Python库之Web信息提取

# Beautiful Soup: HTML和XML的解析库

![](images/724ca4f57bd10f82aa462ea678271605d87f8636c3aafbb90b02dd7e6482bfef.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["下行遍历"] --> B["上行遍历"]
    B --> C["下行遍历"]
    C --> D["下行遍历"]
    D --> E["下行遍历"]
    E --> F["下行遍历"]
    F --> G["下行遍历"]
    G --> H["下行遍历"]
    H --> I["下行遍历"]
    I --> J["下行遍历"]
    J --> K["下行遍历"]
    K --> L["下行遍历"]
    L --> M["下行遍历"]
    M --> N["下行遍历"]
    N --> O["下行遍历"]
    O --> P["下行遍历"]
    P --> Q["下行遍历"]
    Q --> R["下行遍历"]
    R --> S["下行遍历"]
    S --> T["下行遍历"]
    T --> U["下行遍历"]
    U --> V["下行遍历"]
    V --> W["下行遍历"]
    W --> X["下行遍历"]
    X --> Y["下行遍历"]
    Y --> Z["下行遍历"]
    Z --> AA["下行遍历"]
    AA --> AB["下行遍历"]
    AB --> AC["下行遍历"]
    AC --> AD["下行遍历"]
    AD --> AE["下行遍历"]
    AE --> AF["下行遍历"]
    AF --> AG["下行遍历"]
    AG --> AH["下行遍历"]
    AH --> AI["下行遍历"]
    AI --> AJ["下行遍历"]
    AJ --> AK["下行遍历"]
    AK --> AL["下行遍历"]
    AL --> AM["下行遍历"]
    AM --> AN["下行遍历"]
    AN --> AO["下行遍历"]
    AO --> AP["下行遍历"]
    AP --> AQ["下行遍历"]
    AQ --> AR["下行遍历"]
    AR --> AS["下行遍历"]
    AS --> AT["下行遍历"]
    AT --> AU["下行遍历"]
    AU --> AV["下行遍历"]
    AV --> AW["下行遍历"]
    AW --> AX["下行遍历"]
    AX --> AY["下行遍历"]
```
</details>

# Python库之Web信息提取

# Re: 正则表达式解析和处理功能库

提供了定义和解析正则表达式的一批通用功能  
可用于各类场景，包括定点的Web信息提取  
Python最主要的标准库之一，无需安装

# Python库之Web信息提取

# Re: 正则表达式解析和处理功能库

re.search()

re.match()

re.findall()

re.split()

r'\d{3}-\d{8}|\d{4}-\d{7}

re.finditer()

re.sub()

# Python库之Web信息提取

# Python-Goose: 提取文章类型Web页面的功能库

- 提供了对Web页面中文章信息/视频等元数据的提取功能  
- 针对特定类型Web页面，应用覆盖面较广  
Python最主要的Web信息提取库

# Python库之Web信息提取

# Python-Goose: 提取文章类型Web页面的功能库

from goose import Goose

url = 'http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html'

g = Goose({'use\_meta\_language': False, 'target\_language':'es'})

article = g.extract(url=url)

article.cleaned\_text[:150]

# Python库之Web网站开发

# Python库之Web网站开发

# Django: 最流行的Web应用框架

提供了构建Web系统的基本应用框架  
MTV模式：模型(model)、模板(Template)、视图(Views)  
Python最重要的Web应用框架，略微复杂的应用框架

# Python库之Web网站开发

Django: 最流行的Web应用框架  
![](images/89f79c19de537e8cc8c8548441fd756ac67367155983e1c8457a589ed1161745.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["浏览器"] -->|HTTP| B["WSGI"]
    B <-->|URLs| C["路由"]
    C <--> D["功能处理逻辑"]
    D <--> E["数据库"]
    F["HTML/CSS/JS 等文件"] --> D
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#bfb,stroke:#333
    style D fill:#ffb,stroke:#333
    style E fill:#cfc,stroke:#333
```
</details>

# Python库之Web网站开发

# Pyramid: 规模适中的Web应用框架

- 提供了简单方便构建Web系统的应用框架  
不大不小，规模适中，适合快速构建并适度扩展类应用  
Python产品级Web应用框架，起步简单可扩展性好

# Python库之Web网站开发

# Pyramid: 规模适中的Web应用框架

```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
def hello_world(request): 
```

```lua
return Response('Hello World!') 
```

```python
if __name__ == '__main__': 
```

```python
with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app() 
```

```txt
server = make_server('0.0.0.0', 6543, app)
server.serve_forever() 
```

# 10行左右Hello Word程序

https://trypyramid.com/

# Python库之Web网站开发

# Flask: Web应用开发微框架

提供了最简单构建Web系统的应用框架  
特点是：简单、规模小、快速   
Django > Pyramid > Flask

# Python库之Web网站开发

# Flask: Web应用开发微框架

from flask import Flask

app = Flask(\_\_name\_\_)

@app.route('/')

def hello\_world():

return 'Hello, World!'

![](images/513dcbb7c8f62de0cace76bf204d23f4ac55950a5d25745152c26c4280196f4e.jpg)

<details>
<summary>text_image</summary>

F
</details>

# lask

web development, one drop at a time

# Python库之网络应用开发

![](images/f26f42236c41abe69dc2309fa3a500b4592efbe4b2052b312f47df2581ee3bff.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/71eec9a8475b625fce8b3d5c376a6f617e22cfc1a265679260505192bf6e2f3f.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之网络应用开发

# WeRoBot: 微信公众号开发框架

提供了解析微信服务器消息及反馈消息的功能  
建立微信机器人的重要技术手段

# Python库之Web网站开发

# WeRoBot: 微信公众号开发框架

import werobot

robot = werobot.WeRoBot(token='tokenhere')

@robot.handler

def hello(message):

return 'Hello World!'

\- 对微信每个消息反馈一个Hello World

# Python库之网络应用开发

aip: 百度AI开放平台接口

- 提供了访问百度AI服务的Python功能接口  
语音、人脸、OCR、NLP、知识图谱、图像搜索等领域  
Python百度AI应用的最主要方式

# Python库之Web网站开发

# aip: 百度AI开放平台接口

![](images/c94ed8ed235909fcfa2b52b2a34ef1ccbf7c5456620ccb075a95dbc81340188f.jpg)

![](images/131c5b75ee3a37a86870118d0b65e6966dac10eb3b0a4807e329cb624016cd3e.jpg)

![](images/30cfce88fabe03bffb80cf484ababd493b4462a77042cc656647e3ea4be65cfd.jpg)

AR

![](images/7d36e51a58979868014dfd402ad433595552d98cba3eab2b90af09f6d5f97443.jpg)

![](images/b3c2767fb9b87f04335f201ed8291b703160ba05c8c645c0d4415977c4094459.jpg)

![](images/bf4b8823c7f8f4a5b9141d7356bf7c768fe79b65d8dcf7ab9d7f9c5893e3077d.jpg)

# Python库之网络应用开发

# MyQR: 二维码生成第三方库

提供了生成二维码的系列功能  
基本二维码、艺术二维码和动态二维码

# Python库之Web网站开发

MyQR: 二维码生成第三方库

![](images/12b94e57f95d247de0b7e2ba6303f507616c5e29513bd917a6932decf90b808a.jpg)

<details>
<summary>text_image</summary>

QR code with a purple cat face logo in the center, likely linking to a digital resource or webpage.
</details>

![](images/ade735f16016f3586a23c81b72a39aa966e315e74b0f9efd3c5b3d42a5c9f8fa.jpg)

<details>
<summary>text_image</summary>

QR code image with pixelated graphic of a vehicle silhouette and trees, likely for digital scanning or web-based content.
</details>

![](images/324db1a8005ecf3033db0a2a66a28afbf9c3f3d8156699abb926d092337d463c.jpg)

<details>
<summary>natural_image</summary>

Colorful cartoon character with a large red head and gray body, surrounded by a QR code (no text or symbols)
</details>

# 单元小结

# 从Web解析到网络空间

- Requests、Scrapy、pyspider  
- Beautiful Soup、Re、Python-Goose  
- Django、Pyramid、Flask   
WeRobot、aip、MyQR

# 从人机交互到艺术设计

![](images/3df5ef967a0ce6c141c6a7df34ce6f3d5b96cc481476e93d3b45d897bdf9b723.jpg)

python

嵩 天

北京理工大学

pythom

# 单元开篇

# 从人机交互到艺术设计

![](images/45ad915c690b215e3e0be81edee04a606aa97ece8ca25222bc818262121f1f42.jpg)

<details>
<summary>natural_image</summary>

Generic male avatar icon with beard and mustache (no text or symbols)
</details>

- Python库之图形用户界面  
Python库之游戏开发  
Python库之虚拟现实   
Python库之图形艺术

![](images/2174884e92f3a4340f46fab7119832e8622849471516d9344bf1355e94d61321.jpg)

<details>
<summary>natural_image</summary>

Illustration of a person riding a bicycle with a checkered board in the background (no text or symbols)
</details>

# Python库之图形用户界面

![](images/ba35298483c8b7cd8d2cbaeb53e69f45dac6993cba1407d887022c3e78437f87.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/fe33ff676b443b5f41484e475acecbba8fd23f73c62d1f497024443730871148.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之图形用户界面

# PyQt5: Qt开发框架的Python接口

提供了创建Qt5程序的Python API接口  
Qt是非常成熟的跨平台桌面应用开发系统，完备GUI  
推荐的Python GUI开发第三方库

# Python库之图形用户界面

# PyQt5: Qt开发框架的Python接口

![](images/a83febe7cd8e80723501721df323527aa92a88e23dece0c56c9461edcf6fabd2.jpg)

<details>
<summary>text_image</summary>

网格布局
1	2	3
4	5	6
7	8	9
</details>

![](images/c2ad06d1b21fe6c2da62ac8223febee02e6ad17f907e2d49e30ba40454f601e4.jpg)

<details>
<summary>text_image</summary>

与Python对话中
Me : 2016-10-02 18:03:39
Python语言程序设计(第2版)
发送	取消	历史记录
</details>

# Python库之图形用户界面

wxPython: 跨平台GUI开发框架

提供了专用于Python的跨平台GUI开发框架  
理解数据类型与索引的关系，操作索引即操作数据  
Python最主要的数据分析功能库，基于Numpy开发

# Python库之图形用户界面

# wxPython: 跨平台GUI开发框架

import wx   
```python
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop() 
```

![](images/f9ffb37e2a18a45f8e86a7ec0d4232a6fdde36afb627a77a548678c8d6d03a69.jpg)

<details>
<summary>text_image</summary>

wxPython
http://wxPython.org/
Cross-Platform GUI Library
</details>

# Python库之图形用户界面

# PyGObject: 使用GTK+开发GUI的功能库

提供了整合GTK+、WebKitGTK+等库的功能  
GTK+：跨平台的一种用户图形界面GUI框架  
- 实例：Anaconda采用该库构建GUI

# Python库之图形用户界面

# PyGObject: 使用GTK+开发GUI的功能库

import gi

gi.require\_version("Gtk", "3.0")

from gi.repository import Gtk

window = Gtk.Window(title="Hello World")

window.show()

window.connect("destroy", Gtk.main\_quit)

Gtk.main()

![](images/c894eba039892adc46116762775fe15799101d0be5ad6436ae9326a799bd8546.jpg)

PyGObject

# Python库之游戏开发

![](images/28023a9de9f1247c2220c3bd0f05fcb1b9ae9682a4f236835a152f239744c941.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/a94d114572cf3b8b6fc40ed7ad2bd83c8f3167bef6b21490aa56f6c03c9b9ed8.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之游戏开发

# PyGame: 简单的游戏开发功能库

- 提供了基于SDL的简单游戏开发功能及实现引擎  
理解游戏对外部输入的响应机制及角色构建和交互机制  
Python游戏入门最主要的第三方库

# Python库之游戏开发

# PyGame: 简单的游戏开发功能库

![](images/1ead7764a5ad0ab9e28a42e4867c4489c7cc8b4b0a544fcb66acc33ee2a8c4f8.jpg)

<details>
<summary>text_image</summary>

SCORE 2000
+10%
-10%
</details>

![](images/993a8c93ddac5efb84ebc6946d10377e45e3dfb33978644f69325fab567c8aa0.jpg)

<details>
<summary>text_image</summary>

Level: 4
 launch Time
Outward Time
Outward Time
Outward Time
Level 4
</details>

![](images/307d1aaf47031c015d586a132f5b83122c1164ca6def581cca22efd1ad2182e5.jpg)

<details>
<summary>text_image</summary>

pygame
</details>

# Python库之游戏开发

# Panda3D: 开源、跨平台的3D渲染和游戏开发库

一个3D游戏引擎，提供Python和C++两种接口  
支持很多先进特性：法线贴图、光泽贴图、卡通渲染等  
由迪士尼和卡尼基梅隆大学共同开发

# Python库之游戏开发

# Panda3D: 开源、跨平台的3D渲染和游戏开发库

![](images/19fac6751fb44a2764154d0abade2de1148bf1e3685c67b131cdb7511bc3bf41.jpg)

<details>
<summary>natural_image</summary>

Animated character with red hat and green eyes, no visible text or symbols in the scene
</details>

![](images/6dc755bd4b29e9916a6e02b137737ee21c487c7e3d0c369dd6c5a8a13d807fc7.jpg)

<details>
<summary>natural_image</summary>

Illustration of the Caribbean online cruise ship at sea, featuring multiple sailing ships and a distant skyline under a cloudy sky (no text or symbols on the scene itself)
</details>

![](images/135c738ae8fe79896bcae0a545118e38e1711704b3e68cddbbf25f63a09d0624.jpg)

<details>
<summary>text_image</summary>

PANDA3D
</details>

# Python库之游戏开发

cocos2d: 构建2D游戏和图形界面交互式应用的框架

提供了基于OpenGL的游戏开发图形渲染功能  
支持GPU加速，采用树形结构分层管理游戏对象类型  
适用于2D专业级游戏开发

# Python库之游戏开发

# cocos2d: 构建2D游戏和图形界面交互式应用的框架

![](images/c10f3f56871b0b6735bf68e5c2b93d9df698ee47c3c974711164da1c93928541.jpg)

<details>
<summary>natural_image</summary>

Illustration of a cartoon character surrounded by multiple robotic characters and sound equipment (no text or symbols)
</details>

![](images/ba9ce39f1a2b47a61b7bff78fd79179fc0032b12de5f841a4393e5769ca766ab.jpg)

<details>
<summary>text_image</summary>

For one WIS.COMS our new robot overKinds.
</details>

cocos2d

# Python库之虚拟现实

![](images/8be33c8b74e0c30ddcebf567c2bf9c2987ad01c9a73196406757f57a6ab99c51.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/a1be706d9bd6154e057053734d216b372199737bec7efccc77c0eb30f3cf8939.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之虚拟现实

# VR Zero: 在树莓派上开发VR应用的Python库

提供大量与VR开发相关的功能  
针对树莓派的VR开发库，支持设备小型化，配置简单化  
非常适合初学者实践VR开发及应用

# Python库之虚拟现实

# VR Zero: 在树莓派上开发VR应用的Python库

![](images/dfc6c783ffed2b0278e0c0c5d2a6f9acf02f581d9693b6ba66a22d5eed047ed2.jpg)

<details>
<summary>natural_image</summary>

Two-panel image showing Earth from space, with a small planet visible in the sky (no text or symbols)
</details>

![](images/3d361c41d296819b421795efdc1c24fcd8fef14c318115efc1528d6877480206.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a Gothic-style cathedral at dusk, showing its stone facade and spire (no signage or text visible)
</details>

https://github.com/WayneKeenan/python-vrzero

# Python库之虚拟现实

# pyovr: Oculus Rift的Python开发接口

针对Oculus VR设备的Python开发库  
- 基于成熟的VR设备，提供全套文档，工业级应用设备  
Python+虚拟现实领域探索的一种思路

# Python库之虚拟现实

# pyovr: 开发Oculus Rift的Python库

![](images/0ec843791237d38b2f8569721619dca291f22cd0f0e517c789253e0a473048d8.jpg)

<details>
<summary>text_image</summary>

oculus Go
</details>

![](images/0bbe0dc8fba863f64b70555cb6c854875c3685a75afda9d6f592ec705960238c.jpg)

<details>
<summary>natural_image</summary>

Two 3D geometric shapes, one red and one blue, displayed against a black background (no text or symbols)
</details>

# Python库之虚拟现实

# Vizard: 基于Python的通用VR开发引擎

专业的企业级虚拟现实开发引擎  
提供详细的官方文档  
支持多种主流的VR硬件设备，具有一定通用性

# Python库之虚拟现实

# Vizard: 基于Python的通用VR开发引擎

![](images/ae2a978f976bbf1c4825a1dd0b5f116d71ccf4d47d3b320f5160a1550d66f818.jpg)

<details>
<summary>natural_image</summary>

Industrial facility exterior with steel frameworks and concrete pillars under a cloudy sky (no visible text or symbols)
</details>

![](images/64134cf9bd7dbfe35d8f999f7f76cd13f14daffd7b38267c61bb1fed9376b3a2.jpg)

<details>
<summary>text_image</summary>

The object is configured
to be rotated, bigger,
and floated up when the
presenter enters the
sensor
</details>

![](images/1cbff2890291576168aa95f86b33c1301c438041c66d988534503c75293251d8.jpg)

<details>
<summary>text_image</summary>

Screenshot of a 3D modeling software interface displaying a virtual room interior with tool panels and property settings.
</details>

# Python库之图形艺术

![](images/3275fe39bc19c27cfb67d2b249f500039ff6964e4d745a0224cedce2a41804d8.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric line drawing with interconnected nodes and lines (no text or symbols)
</details>

![](images/3f8387d34f48454d7c327b3eda985a2b799c54a35aa5d7b809a043b209410966.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric network diagram with interconnected nodes and lines (no text or symbols)
</details>

# Python库之图形艺术

# Quads: 迭代的艺术

对图片进行四分迭代，形成像素风  
可以生成动图或静图图像  
简单易用，具有很高展示度

# Python库之虚拟现实

# Quads: 迭代的艺术

![](images/6271c4118e43eea664ed5803ded5dae7bdd773ee50ad23da591949f59dfcb403.jpg)

<details>
<summary>natural_image</summary>

Abstract pattern with zebra and dot textures in shades of blue and beige (no text or symbols)
</details>

![](images/4e9574e308eff6f060572c7b78c9a99bb14165ce0aa944fe8e9c17bd59f22cc5.jpg)

<details>
<summary>natural_image</summary>

Pixelated abstract pattern with red, yellow, and olive squares on a grid background (no text or symbols)
</details>

![](images/0973732ad3d8bb4a5a71b3b5e47b6f3b7c8f117373623ef6edadfdadc5f03967.jpg)

<details>
<summary>natural_image</summary>

Pixelated image of an owl with large eyes and brown feathers, set against a grid background (no text or symbols)
</details>

# Python库之图形艺术

ascii\_art: ASCII艺术库

将普通图片转为ASCII艺术风格  
输出可以是纯文本或彩色文本  
可采用图片格式输出

# Python库之虚拟现实 sat\*\*\*\*\*+\*\*\*\*@@000\*xx\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*##\*@@ \*\*##\*\*\*+++\*##\*\*\*@@@@@\*\*###\*+++

ascii\_art: ASCII艺术库

![](images/51e7e9d5bbe3c6f6ba24c4641f400e22bfdee78b65d59347e095029d8e6a401d.jpg)

<details>
<summary>natural_image</summary>

A young tabby kitten peeking over a wooden deck, looking upward with blue eyes (no text or symbols visible)
</details>

![](images/ef7997c0b67de36c1f4464f80081ea3741a99f82976d44179c2ba97b5668928a.jpg)

<details>
<summary>natural_image</summary>

Close-up grayscale image of a tabby cat with a red circle highlighting the eye area (no text or symbols)
</details>

黑白

![](images/9bba045f567d04dbca48f63d0c5b255582913e03690fd8536c9cb784ff7ce852.jpg)

<details>
<summary>natural_image</summary>

Black-and-white photo of a fluffy kitten standing on a wooden surface, looking upward (no text or symbols visible)
</details>

彩色

\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*#\*\*\* \*###\*\*\*\*#####\*\*\*\*% \*\*+\*+\*\*@\*\*\*\*\*\*\*#\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*#\*\*\*\*\*\*\*\*\*\*\*@@@@@@\*\*\*\*\*\*\*\*\*\*\*\*##\*##\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\* \*@\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*#\*\*\*@\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*###\*\*\*\*\*\*#\*\*\*\*#\*\*\*\*\*#\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*+\*\*\*\*\* \*\*\*\*\*\*\*## \*\*\*\*\*\*\*++\*\*\* \*\*\*\*\*\*\*\*\*\* ###\*\*\*\*##\*\*\*\*\*\*####\*\*\*\*+\*\*+\*\*\*++++++\*\*\*\*++\*\*\*\*++++++\*\*\*\*+\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\* === \*+\*\*\*\*\*\*\*\*\*+\*+\*+===\*+++\*\*\*\* \*\*\*\*\*\*\*+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*+ \*+\*\*\*\*\*\*\* ##\*@@@\*\* ##\*\*\*@####\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*#\*\*\*\*\*\*\*\*\*\*\*\* ####\*#\*++++++++\*#\*@@@@@\*\*\*\*###\*@\*\*####\*+ \*\*\*\*\*\*+\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\* \*#\*\*\*\*++\*\*\*\*+\*\*+\*\*\*\*\*\*##\* t\*##\*\*+++++++\*#\*@@@@t##\*\*#\*\*@@@@\*\*##\*+==- -#\*#\*++++\*\*\*\*\*t@@@@@ccccc@@\*\*#######\* ###\*++++++++\*\*x@@@@@\*###\*\*#\*x@@@@\*#\*++== -\*\*#\*+===++\*\*###\*\*z@@@@@@@\*\*#####\*\*\* #\*++++#@@##\*#\*#@@@\*+++\*\*+\*\*\*\*@@@@@####\* \*\*\*\*\*\*@@\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*##\*\*\* \*\*\*\*\*\*\*\*@@\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*+\*\*\*\*\*\*\*#\*\* \*\*\*\*\*+\*#@@@@@@@\*\*#\*\*\*\*##@\*\*+\*\*\*\*\*\*\*\*\*###x@@x##\* ##\*\*++++\*\*@@@@@@@@@\*###\*\*\*\*\*#\*@@\*\*+++\*\*\*\*\*\*\*\*\*###\*\*+ \*\*x@@@@@@@@\*\*+\*###\*#\*\*#+ \*#\*\*\*\*#\*@@@@@@∞###\*#\*####\*\*\*+\*\*+

##\*\*\*+ +\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*#\*\*\*\*\*##\*\*\*+ \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*jjj\*\*\*\*\*\*\*\*\*\* x\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

# Python库之图形艺术

# turtle: 海龟绘图体系

![](images/504567fdad53a8094f9116dd3bf80af85f0277885f10dfec5479671b96023433.jpg)

<details>
<summary>natural_image</summary>

Illustration of two starfish with flying birds against a yellow background (no text or symbols)
</details>

![](images/77ac2da8ffc497d19a32b84a1c2f31bef520c25c938142ea73b05ea3a2233c63.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric pattern with interlocking black, orange, and red shapes (no text or symbols)
</details>

![](images/b81f53c9c0a9f76228a8267ac11b6ac3993016c58213d5427d8aeb9c6a9c73f4.jpg)

<details>
<summary>natural_image</summary>

Stylized illustration of a sunset over blue water with birds flying around (no text or symbols)
</details>

![](images/74c5207536ddbdd7d4b27618d919b45b619273b60dbe6bb9088f0c2046a4f042.jpg)

<details>
<summary>natural_image</summary>

Colorful abstract floral pattern with interlocking leaves (no text or symbols)
</details>

![](images/592428de833d17e4f791fb9d3dd7f2b1b3d1ac174f36a118225a24f02bf3403a.jpg)

<details>
<summary>natural_image</summary>

Abstract black-and-white pattern with scattered colorful star-like shapes and a reflective surface (no text or symbols)
</details>

![](images/9625299a2eb4a0cf07cf80d84fad73401b9437c5b6c05dab00a795e5c330f886.jpg)

<details>
<summary>text_image</summary>

Rainbow
</details>

# Python库之图形艺术

# turtle: 海龟绘图体系

![](images/22399b1d1a4dfac538869a822b3f466ce6afa7ad434da26bfd8bea98f9b728dd.jpg)

<details>
<summary>natural_image</summary>

Illustration of colorful flower-like patterns scattered above a dark water surface with white wavy lines at the bottom (no text or symbols)
</details>

Random Art

# 单元小结

# 从人机交互到艺术设计

- PyQt5、wxPython、PyGObject  
- PyGame、Panda3D、cocos2d  
VR Zero、pyovr、Vizard   
Quads、ascii\_art、turtle

# 实例16: 玫瑰花绘制

![](images/262551b1e79e13db4958245f7d2266c96ba12bbe0f457145614fade6f37195f0.jpg)

python

嵩 天

北京理工大学

pythom

![](images/991b2fd83c0871359a7c880e740a589d22237ddf73b1bb23c50d870ce5a225c1.jpg)

<details>
<summary>text_image</summary>

"玫瑰花绘制"问题分析
</details>

# 问题分析

# 玫瑰花绘制

![](images/61779ad8e87dfb87b76312412cda7d971bab7cb28a6865626a9bac2a08b12ef3.jpg)

<details>
<summary>natural_image</summary>

Close-up of a vibrant red rose with green leaves against a white background (no text or symbols)
</details>

![](images/128a0ab5bab150e43f55e136a5e871af498ac41128e500dbc5ed80867f4e446e.jpg)

<details>
<summary>natural_image</summary>

Close-up of a vibrant red rose with a spiral, no text or symbols visible
</details>

![](images/4b99c81f864477728866f11799cf88e5d99c90cfc075b16c56c4f1faa402a894.jpg)

<details>
<summary>natural_image</summary>

Close-up of a single red rose with green leaves against a white background (no text or symbols)
</details>

# 问题分析

# 玫瑰花绘制

- 需求：用Python绘制一朵玫瑰花，献给所思所念   
输入：你的想象力！  
输出：玫瑰花

# 问题分析

# 玫瑰花绘制

绘制机理：turtle基本图形绘制  
绘制思想：因人而异   
思想有多大、 世界就有多大

![](images/2b4543be82af55c58dd174ed332b6817ae0d3103144a5b1b4d4b60b609592155.jpg)

<details>
<summary>text_image</summary>

"玫瑰花绘制"实例展示
</details>

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1): for i in range(n): t.left(d) t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

\# 绘制一个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/357621779e6022f39d7279daa5aaf894b1058d278f6a5d5b0e77f2dd07b7a66b.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves and stem (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1): for i in range(n): t.left(d) t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

\# 绘制一个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/def9e88c2250b14564e068005b2e9f435de85459b90076a9f6aa6bc54acb34e0.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves and stem (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1):

for i in range(n):

t.left(d)

t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

\# 绘制一个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/dc5e4b10d0052e9ee4eaa570eaa90eebcf131e41143590351808364b968d4af9.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1): for i in range(n): t.left(d) t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

\# 绘制一个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/4d04444b712c1e6e5c9b56845269d37042c43dc449d849fd4af34f333e195a50.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1): for i in range(n): t.left(d) t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

绘制 个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/ec5deb2794b444bf87ecc8ce9e253865205801c1011d584ffdfbc6454d29899b.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1): for i in range(n): t.left(d) t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

\# 绘制一个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/7da51aa759fa13d56b4e983719a93ff20c1b330a6e9cf90f5865902364fccc1d.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

\# RoseDraw.py

import turtle as t

\# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1): for i in range(n): t.left(d) t.circle(r, abs(d))

\# 初始位置设定

s = 0.2 # size

t.setup(450\*5\*s, 750\*5\*s)

t.pencolor("black")

t.fillcolor("red")

t.speed(100)

t.penup()

t.goto(0, 900\*s)

t.pendown()

\# 绘制花朵形状

t.begin\_fill()

t.circle(200\*s,30)

DegreeCurve(60, 50\*s)

t.circle(200\*s,30)

DegreeCurve(4, 100\*s)

t.circle(200\*s,50)

DegreeCurve(50, 50\*s)

t.circle(350\*s,65)

DegreeCurve(40, 70\*s)

t.circle(150\*s,50)

DegreeCurve(20, 50\*s, -1)

t.circle(400\*s,60)

DegreeCurve(18, 50\*s)

t.fd(250\*s)

t.right(150)

# 玫瑰花绘制

t.circle(-500\*s,12)

t.left(140)

t.circle(550\*s,110)

t.left(27)

t.circle(650\*s,100)

t.left(130)

t.circle(-300\*s,20)

t.right(123)

t.circle(220\*s,57)

t.end\_fill()

\# 绘制花枝形状

t.left(120)

t.fd(280\*s)

t.left(115)

t.circle(300\*s,33)

t.left(180)

t.circle(-300\*s,33)

DegreeCurve(70, 225\*s, -1)

t.circle(350\*s,104)

t.left(90)

t.circle(200\*s,105)

t.circle(-500\*s,63)

t.penup()

t.goto(170\*s,-30\*s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500\*s)

DegreeCurve(220, 250\*s, -1)

\# 绘制一个绿色叶子

t.fillcolor('green')

t.penup()

t.goto(670\*s,-180\*s)

t.pendown()

t.right(140)

t.begin\_fill()

t.circle(300\*s,120)

t.left(60)

t.circle(300\*s,120)

t.end\_fill()

t.penup()

t.goto(180\*s,-550\*s)

t.pendown()

t.right(85)

t.circle(600\*s,40)

\# 绘制另一个绿色叶子

t.penup()

t.goto(-150\*s,-1000\*s)

t.pendown()

t.begin\_fill()

t.rt(120)

t.circle(300\*s,115)

t.left(75)

![](images/692a34ad76aba21ce4c3835f0850ae2b5014b477d498b6c831d6f3e13cc80dca.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a red rose with green leaves (no text or symbols)
</details>

t.circle(300\*s,100)

t.end\_fill()

t.penup()

t.goto(430\*s,-1070\*s)

t.pendown()

t.right(30)

t.circle(-600\*s,35)

t.done()

![](images/1b98199af91011c67039029979b17da41eabbb19f32e1f0db5adac261eb93459.jpg)

<details>
<summary>text_image</summary>

"玫瑰花绘制"举一反三
</details>

# 举一反三

# 艺术之于编程， 设计之于编程

艺术：思想优先，编程是手段  
设计：想法和编程同等重要  
工程：编程优先，思想次之

# 举一反三

# 编程不重要， 思想才重要！

认识自己：明确自己的目标，有自己的思想(想法)  
方式方法：编程只是手段，熟练之，未雨绸缪为思想服务  
为谁编程：将自身发展与祖国发展相结合，创造真正价值

![](images/5faf54e0bd0c437751355f72ca68efd64807d293c18caeef7c85a518db9fdb86.jpg)

<details>
<summary>natural_image</summary>

Field of yellow rapeseed flowers with a dirt path, under a vibrant orange sunset sky with trees and distant hills (no text or symbols)
</details>