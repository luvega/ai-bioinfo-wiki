---
type: source
title: Starting Data Analytics with Generative AI and Python 9781633437210
format: mineru-api-markdown
raw_path: materials/raw/pdf_originals/Starting Data Analytics with Generative AI and Python 9781633437210.pdf
mineru_raw_markdown: materials/markdown/pdf_library_mineru/api_raw/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/part_001/full.md
source_pages: 362
page_range: 1-200
generated: 2026-05-24 12:20:18
status: generated_part
---

# Starting

# Data Anlytics with Generativ Aland Python

Artur Guja ● Marlena Siwiak ● Marian Siwiak

Foreword by Sue Tripathi

![](images/ae15b36fc0d84917a5eb19210557a43eaecb271c392ac4b3fc0f28203ba6eb97.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing a wide-brimmed hat and period attire (no visible text or symbols)
</details>

Recommended generative AI–supported data analysis flow   
![](images/2cfba93d53fcd94eb1670b65787359eb276e3b88a79b4fc7f10e3b84d148ca1e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["User activities"] --> B["Problem statement"]
    B --> C["Goals of the analysis"]
    C --> D["Guidance / suggestions"]
    D --> E["Evaluation and decision-making"]
    E --> F["Implementation details / programming"]
    F --> G["How-to / code"]
    G --> H["Analysis and results collection"]
    H --> I["Initial analysis results"]
    I --> J["Interpretive augmentation"]
    J --> K["Final synthesis and decision-making"]
    style A fill:#f9f,stroke:#333
    style K fill:#f9f,stroke:#333
```
</details>

# Starting Data Analytics with Generative AI and Python

ARTUR GUJA

MARLENA SIWIAK

MARIAN SIWIAK

FOREWORD BY SUE TRIPATHI

For online information and ordering of this and other Manning books, please visit www.manning.com. The publisher offers discounts on this book when ordered in quantity. For more information, please contact

Special Sales Department

Manning Publications Co.

20 Baldwin Road

PO Box 761

Shelter Island, NY 11964

Email: orders@manning.com

©2025 by Manning Publications Co. All rights reserved.

No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by means electronic, mechanical, photocopying, or otherwise, without prior written permission of the publisher.

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in the book, and Manning Publications was aware of a trademark claim, the designations have been printed in initial caps or all caps.

Recognizing the importance of preserving what has been written, it is Manning’s policy to have the books we publish printed on acid-free paper, and we exert our best efforts to that end. Recognizing also our responsibility to conserve the resources of our planet, Manning books are printed on paper that is at least 15 percent recycled and processed without the use of elemental chlorine.

The author and publisher have made every effort to ensure that the information in this book was correct at press time. The author and publisher do not assume and hereby disclaim any liability to any party for any loss, damage, or disruption caused by errors or omissions, whether such errors or omissions result from negligence, accident, or any other cause, or from any usage of the information herein.

![](images/1b71439f4074e242077db233495496b773c2fb5bb19ccdec9d92d80b74d13c55.jpg)

Manning Publications Co.

20 Baldwin Road

PO Box 761

Shelter Island, NY 11964

Development editor: Ian Hough

Technical editor: Mike Jensen

Review editor: Dunja Nikitović

Production editor: Kathy Rossland

Copy editor: Andy Carroll

Proofreader: Keri Hales

Technical proofreader: Tony Holdroyd

Typesetter and cover designer: Marija Tudor

To my father, for everything

—Artur Guja

# contents

foreword ix

preface xi

acknowledgments xii

about this book xiv

about the authors xix

about the cover illustration xx

# 1 Introduction to the use of generative AI in data analytics 1

1.1 Inherent limitations of generative AI models 2   
1.2 The role of generative AIs in data analytics 5

Generative AI in the data analytics flow 5 ■ The complementarity of language models and other data analytics tools 9 ■ Limits of generative AIs’ ability to automate and streamline data analytics processes 10

1.3 Getting started with generative AIs for data analytics 12

Web interface 12 ■ Beware of tokens 12 ■ Accessing and using

the API 13 ■ Third-party integrations of generative AI

models 18 ■ Running LLMs locally 19 ■ Best practices and tips

for successful generative AI implementation 20

# 2 Using generative AI to ensure sufficient data quality 23

2.1 On a whimsy of fortune 24   
2.2 A note on best practices 25

2.3 Getting started 26   
2.4 Quality assessment structure 33 Data cleaning steps 34 ■ Exploratory data analysis elements 34   
2.5 Data cleaning 35 Removing duplicates 36 ■ Handling missing values 37 Correcting data entry errors 40 ■ Data validation 41   
2.6 Exploratory data analysis 43 Reviewing score distribution 45 ■ Time series exploration 49 Mysterious variable investigation 55 ■ Harmonizing data 58

# Descriptive analysis and statistical inference supported by generative AI 62

3.1 Research questions 63   
3.2 Analysis design 66   
3.3 Descriptive data analysis 68   
Popularity of product categories 69 ■ Performance of products in their categories and regions 76 ■ Review scores distribution 84 Order status 91

3.4 Inferential analysis 97 Before you begin 97 ■ Relationship between product attributes and shipping costs 98 ■ Relationship between product, transaction, shipping attributes, and the review score 105 ■ Differences in sales performance and customer satisfaction between sellers 111

# Using generative AI for result interpretations 119

4.1 Problem definition 120   
4.2 Popularity of product categories 122   
4.3 Performance of products in their categories and regions 130   
4.4 Review scores distribution analysis 132   
4.5 Order status 138   
4.6 Relationship between product attributes and the shipping costs 142   
4.7 Relationship between product, transaction, shipping attributes, and the review score 146   
4.8 Differences in sales performance and customer satisfaction between sellers 150

# Basic text mining using generative AI 154

5.1 Text mining in the era of generative AI 155   
Generative AI is a game changer 156 ■ Beware of AI intimidation 156 ■ Unpacking the constraints 157

5.2 Preparing for analysis 159   
Data quality 159 ■ Customer feedback preparation example 160

5.3 Frequency analysis 162

What can we learn from frequency analysis of customer reviews? 162 ■ Direct frequency analysis with generative AI 163 ■ Uploading a data file to ChatGPT for frequency analysis 164 ■ Extracting the most common words 165 Extracting the most common phrases 169 ■ Understanding the output 170

5.4 Co-occurrence analysis 173

What can we learn from co-occurrence analysis? 174 ■ Cooccurrence analysis in practice 175 ■ Understanding the output 178

5.5 Keyword search 180

What can we learn from keyword search? 180 ■ Generating keywords with generative AI 181 ■ Generating keywords in practice 182 ■ Searching for keywords 186 ■ Improving keyword search 187 ■ Comparing generative AIs: Code snippets for positive review searches 194 ■ Seeking analytical inspiration 200

5.6 Dictionary-based methods 206

What can we learn from dictionary-based methods? 206 Finding resources 208 ■ Interpreting resources 211 Adapting the code to chosen resources 212 ■ Improving dictionary-based search 214

# Advanced text mining with generative AI 218

6.1 Review analysis 219

6.2 Sentiment analysis 220

What can you learn from sentiment analysis? 222 ■ Direct sentiment analysis with generative AIs 223 ■ Sentiment analysis with generative AI’s API 225 ■ Sentiment analysis with machine learning 227 ■ Sentiment analysis with a suboptimal model 231 ■ Sentiment analysis on translated inputs 234 Sentiment analysis with multilingual models 235 ■ Sentiment analysis with zero-shot learning models 236 ■ Comparing results of advanced sentiment analysis 237

# 6.3 Text summarization 238

How can you benefit from text summarization? 239 ■ How can generative AI help in text summarization? 240 ■ Summarizing text with ChatGPT 242 ■ Summarizing text with dedicated libraries 243 ■ Topic modeling 247

# Scaling and performance optimization 251

# 7.1 Performance measurement 253

Execution time 255 ■ Throughput 258 ■ Resource utilization 259

# 7.2 Improving code performance 261

Optimizing code 262 ■ Scaling code 264

# 7.3 Cloud-based deployment 271

What is cloud computing? 271 ■ Moving your code to the cloud 272

# 7.4 Code conversion 274

# 8 Risk, mitigation, and tradeoffs 280

# 8.1 The risks of GenAI, in context 282

# 8.2 General best practices 283

AI use policy 283 ■ Encouraging transparency and accountability 285 ■ Educating stakeholders 286 Validating model outputs with expert knowledge 289

# 8.3 AI delusion and hallucination risks 291

# 8.4 Mitigating misinterpretation and miscommunication risks 296

Ensuring contextual understanding 297 ■ Tailoring model prompts and iterative query refinement 297 ■ Implementing post-processing techniques 299 ■ Implementing best practices for clearly communicating results 301 ■ Establishing a feedback loop 302

# 8.5 Model bias and fairness risks 303

Recognizing and identifying bias in model outputs 304

Applying bias detection and mitigation techniques 304

Encouraging diversity and ethical use of generative AIs 306

Continuously monitoring and updating models 306

# 8.6 Privacy and security risks 306

Identifying sensitive data 307 ■ Data anonymization and pseudonymization 309 ■ Social engineering and phishing 310

Compliance with data protection regulations 311 ■ Regular security audits and assessments 311 ■ Employee training and awareness 312

# 8.7 Legal and compliance risks 312

Understanding applicable regulations 312 ■ Intellectual property and licensing 312 ■ Transparency and explainability 313 Establishing a compliance framework 313 ■ Regularly reviewing and updating compliance practices 313

# 8.8 Emergent risks 313

Rogue models 314 ■ Vulnerable crown jewels 314 Unknown unknowns 315

appendix A Specifying multiple DataFrames to ChatGPT v4 317

appendix B On debugging ChatGPT’s code 322

appendix C On laziness and human errors 329

index 333

# foreword

I am honored to contribute a foreword for Starting Data Analytics with Generative AI and Python by Artur Guja, Marlena Siwiak, and Marian Siwiak. As we navigate a global landscape increasingly shaped by the convergence of data, analytics, and artificial intelligence (AI), it becomes crucial for newcomers and transitioning professionals alike to grasp and utilize versatile tools tailored to their specific needs. This book offers a comprehensive yet meticulous exploration of why, how, and what tools should be employed, customizable to individual requirements.

In recent years, AI, particularly generative AI, has garnered considerable attention as a transformative solution for various challenges. However, while we anticipate further advancements and the fulfillment of promises, data analytics remains indispensable in uncovering insights that tools alone cannot unearth. Given the current absence of universal standards, ethical considerations, bias reduction efforts, and regulatory frameworks for AI, businesses must consider the symbiotic relationship among AI, data analytics, and tangible outcomes to inform decision-making effectively.

Understanding the foundational principles of data analytics and its intersection with AI is paramount for gaining profound insights and translating them into actionable strategies. By harnessing the synergy between data analytics and AI, individuals and organizations can fully leverage these tools to achieve superior outcomes.

Successful AI implementation hinges on a deep understanding of data preprocessing, result interpretation, and insight enhancement through AI applications. This book serves as a guide on integrating data and AI to enhance individual and organizational capabilities while mitigating associated risks.

During discussions with Artur and Marian on their podcast, “Between Data and Risk,” we highlighted the imperative of prioritizing problem-solving strategies over mere tool deployment in AI initiatives. In Starting Data Analytics with Generative AI and Python, Artur, Marlena, and Marian draw upon their vast experience spanning academia and corporate enterprises, small businesses to multinational corporations, offering practical insights applicable in real-world scenarios. This book underscores Python as a focal point while presenting methods adaptable to diverse programming environments.

For those venturing into the realm of data analytics with AI and generative AI, this book promises invaluable guidance. I am thrilled to embark on this journey alongside the authors, you, and the broader global community as we navigate the next phase of the AI and generative AI revolution through data analytics. With gratitude and best wishes to Artur, Marian, and Marlena and to you, dear readers.

—SUE TRIPATHI

THOUGHT LEADER, DATA, AI, TECHNOLOGY AND TRANSFORMATION

# preface

Put yourself in a position where you get a new analytical question from a business stakeholder. If it’s a question you’ve answered umpteen times already, you should focus on streamlining your analytics or utilizing some business intelligence tool to automate the required report generation. But what if you’re hearing the question for the first time? Where do you start?

In the constantly evolving world of data analytics, the emergence of generative AI, and especially its language-oriented incarnation of large language models (LLMs), has brought forth a new era of powerful tools and techniques we can leverage in the field. This should be no surprise, as these models have, in a very short time, found uses in practically every niche of human-computer interaction, including helping aspiring writers come up with ideas for their novels, writing new recipes for vegan dishes, summarizing books into articles, reviewing and polishing up CVs, and many more. The internet is swarming with innovative uses of language models, and new ones are uncovered daily. To the mix are added frameworks and hybrid solutions combining LLMs with omnifarious traditional software methods, such as LangChain, BabyAGI, Langdock, GradientJ, and LlamaIndex, to name a few (check the web for the current list—this one became obsolete before we finished typing this sentence).

While many everyday use cases include relatively basic text or image transformations, more and more advanced applications of language models in business and science are invented, supporting a whole range of professionals.

In this book, we aim to show how to successfully utilize generative AI to support the critical business function we have the most experience with—data analytics—from start to finish. We will show you how to turn any sufficiently developed model into a trusty advisor, offering you enormous help along the journey from raw data to business conclusions. We will also show you how to minimize the risks related to generative AI’s tendency to mislead you occasionally.

# acknowledgments

Our great appreciation goes to the exceptional team at Manning, instrumental in bringing this book to life: Marjan Bace, our supportive publisher; development editor Ian Hough, whose guidance was invaluable; and not to forget, acquisitions editor Andrew Waldron, who kindled our ambitions to transform our accumulating knowledge into a tangible manuscript. Our gratitude also extends to the diligent marketing, editorial, and production teams, who ensured this book did more than occupy space in a Manning archive.

Special thanks to our technical editor Mike Jensen. Mike is a VP of Engineering and leads Community Solar Engineering, Product, and Data Engineering at Arcadia. In previous roles at Arcadia, he worked on AI R&D and infrastructure for enterprise data platforms. He holds a BSc in computer science and has led teams supporting non-profits, political organizations, last-mile delivery services, and now renewable energy.

Many thanks also to Sue Tripathi, who wrote the foreword to this book. Having traversed the realms of AI and data science, Sue brings a unique perspective. She has been recognized by CIO Magazine as one of the Top 10 Women in AI and has contributed extensively to webinars, podcasts, and global publications on data, technology, and AI.

Furthermore, we extend our heartfelt thanks to the reviewers who believed in us, investing their precious time in evaluating this book, even during moments of uncertainty regarding its future reception: Adriaan Beiertz, Aleksandar Stanković, Ali Shakiba, Anandaganesh Balakrishnan, Ankit Virmani, Benedikt Stemmler, Cale Harrison, Clemens Baader, Daniela Orovwiroro, Darrin Bishop, David Lindelöf, Eduardo Rienzi, Joseph Ian Walker, Iyabo Sindiku, Jereme Allen, Jeremy Chen, John Williams, Joseph Chou, Karan Gupta, Kerry Koitzsch, Kevin Cheung, Laud Bentil, Mahdi Belcaid, Maxime Boillot, Mikael Dautrey, Milind Kelkar, Murugan Lakshmanan,

Najeeb Arif, Ozan Evkaya, Poorvi Shetty, Rahul Shirale, Rajat Gupta, Rambabu Posa, Ravi Tamiri, Ron Hübler, Snehil Sanyal, Sumit Bhattacharyya, Todd Cook, Tong Zhu, Vikram Shibad, Vinod Sangare, and Walter Alexander Mata López. Your suggestions helped make this a better book.

# about this book

This book can be read on three levels, so essentially you have three different books in front of you. At the highest level, it’s a book about data analytics, and you’ll find a basic introduction to the discipline, tools, algorithms, and some more advanced concepts, which together should allow you to perform analytics on your own. It will give you a high-level overview of data analytics as an initial step into the field.

Going deeper, or from a different perspective, if you prefer, it’s a book about taking advantage of the rise of generative AI, as exemplified by ChatGPT. At each step of the journey through data analytics, we’ll lead you through examples of how LLMs can support you in implementing and often also explaining data analytics concepts just through natural language prompts—this is simply a fancy way of saying that you can ask for something in plain English (or whatever language you are working in) and ChatGPT will respond. In some respects, it’s almost miraculous: you ask, and you receive, be it a solution to a problem, an algorithm, or whole pieces of custom-written code. No more going through countless posts on Stack Overflow or similar websites, trying to find people with similar problems, and hoping that some kind soul helped them. You just need to state your question, and the algorithm is chosen and the code is written for you. Moreover, LLMs can also help beyond generating code: they can explain in plain language the functioning of a code snippet you provide or provide plain language descriptions of data and results.

Finally, it’s a book about how the preceding “miracle” is illusory and how hidden traps await those lulled into a false sense of security. Generative AIs are not infallible. Despite the confident tone of their responses and their superhuman (sic!) ability to recall vast amounts of information, they still don’t “understand” as such, and we’ll show you examples of narrow focus, limited context awareness, communication mishaps, and pure AI hallucination.

It’s been said that generative AI will cause various groups of people to lose their jobs, data analysts included. We’d clarify this notion, stating that, at least at the current level of advancement of the technology, the people who should beware are the ones who trust the responses from these models uncritically, for they will, sooner or later, repeat some obvious rubbish that the model has spewed out. Don’t get us wrong: the models are brilliant and can do so much to help that it seems untrue at moments, but humans should not replace their own intelligence with artificial ones just yet. In most cases, we should use these models as tools to help humans do their jobs better.

# Who should read this book

This book caters mainly to two audiences. First, it’s tailored for individuals either embarking on a journey into data analytics or aiming to strengthen their existing skills. Our guide offers a detailed look into the analytical process, from initial planning to the practicalities of Python code-writing. Second, this book is insightful for managers and leaders. As the importance of data-driven decisions grows, having a foundational understanding of the analytics process and its associated risks becomes essential. This book provides a window into what managers can expect from their analytics teams and the challenges that might arise. In doing so, it serves as a resource for both the practitioners of analytics and those making decisions based on its outcomes.

# How to read this book

Consider the book you hold as a travelogue. We wrote it from the perspective of someone not overly burdened with experience in data analytics who has embarked on a journey from raw data to business conclusions. We will introduce and discuss data analytics concepts, testing how much help we can expect from our GPT advisor.

# Generative AI vs. LLMs vs. GPT: Decoding the trio

Throughout this book, we will be using the following sets of terms.

Generative AI refers to a subset of artificial intelligence algorithms designed to create content. These algorithms can generate various forms of data, from text and images to music and videos, often by discerning patterns in the training data they’ve been fed and applying those patterns to the inputs, or “prompts,” from the user. Their capability to produce new, original content mimicking the data they’ve learned makes them especially useful in creative and data-intensive tasks.   
LLMs (large language models) are a type of generative AI designed specifically for tasks involving human language. By training on vast amounts of textual data, these models aim to understand and generate text in a manner that’s akin to humans. The LLM category contains multiple architecture types such as GPT, BERT, MoE, GShard, GLaM.   
ChatGPT, ChatGPT 4, or our GPT/LLM/AI advisor refers to a specific LLM implementation, namely ChatGPT 4 by OpenAI.

Throughout this book, we’ve chronicled our interactions with generative AI. While we feature mainly ChatGPT 4, the scope of the book isn’t confined to just this particular implementation. Engagements and insights, along with associated risks, can be similarly derived from other LLM renditions.

# Your mileage may vary (a lot!)

When transcripts of conversations with ChatGPT are given, you should not expect to receive identical answers, even to the same prompts. There are several reasons for this:

The version of the model you use may be different, with newer optimizations, training, and overlays.   
The responses we got were usually in the flow of larger conversations, and the context may influence the response.   
The model employs a certain randomness in its responses. Hence, if you click the Regenerate button next to a response, you will get a differently worded one. Hopefully the core meaning will be the same, although we did have examples where the model hallucinated enough that it even changed the meaning of the answer. You’ll find more on AI hallucinations in chapter 8.

Let’s have a look at a typical scenario where we use ChatGPT 4 to generate posts for Facebook and Twitter announcing the launch of a certain book:

![](images/f2586c97489548ed14b45d3f3c342dc589d3932aa910d0fdc1a111d7ac655110.jpg)

Given the following Table of Contents, write a Facebook notification and a Twitter tweet advertising the launch of this book. Write it in two versions. The first one should be addressed to data scientists, while the second one should be directed at cool teens. Table of Contents: <Here the Table of Contents was supplied.>

![](images/8ce965c43857c452f7c9a5fcc560b2ea12bd59ffbbcf326e18f292c10ba6ce0f.jpg)

Sure, here is your requested social media content.

For Data Scientists:

Facebook Post:

Attention all Data Scientists! We’re excited to announce the launch of our latestbook - “Starting Data Analytics with Generative AI and Python.” This comprehensive guide dives deep into the applications of GPT models in data analysis, highlighting best practices, potential risks, and much more. Harness the power of ChatGPT and take your data analytics projects to new heights. Grab your copy today!   #DataScience #GPTModels #ChatGPT #DataAnalytics

Twitter Tweet:

Just launched: “Starting Data Analytics with Generative AI and Python”! Explore the use of GPT models in #DataAnalytics. From data cleaning with ChatGPT to scaling and performance optimization, this book has got it all. A must-read for every #Data-Scientist. Grab your copy today!  

For Cool Teens:

Facebook Post:

Hey there, tech-savvy teens! Curious about AI and data analytics? Check out our new book - “Starting Data Analytics with Generative AI and Python.” It’s packed with cool insights about AI models, data crunching, and even has some coding stuff! Dive in and discover your inner data scientist. No tech jargon, promise! $\bigotimes \square \bigsqcup$ #CoolTeens #GPTModels #ChatGPT #DataAnalytics

Twitter Tweet:

Ever wonder how AI makes sense of all that data? $\bigotimes$ Our new book “Starting Data Analytics with Generative AI and Python” is your ticket to find out! It’s all about AI, data, and coding - and it’s written for YOU. Discover your inner #DataScientist today. Check it out! $\bigotimes \square \bigsqcup$ #TeenTechies #GPTModels #ChatGPT

You can try repeating our prompts yourself. Or do even better! Try to tweak, modify, alter, adapt, reshape, customize, or correct them. We also propose a set of questions to ask your favorite LLM at the end of each chapter.

Despite the emphasis we put on the risks related to using Generative AI, throughout the book, we believe that most of the conversations you’ll have with sufficiently developed models will have great educational value. Or at least, they may provide you with interesting food for thought.

Should you expect the answers we received? Absolutely not! We’ll explain why at the very beginning of the first chapter.

# The business data used in the book

To make the examples in this book coherent and illustrative, we will be using the Brazilian e-commerce public dataset of orders made at the Olist Store. The dataset has information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow you to view orders from multiple dimensions: from order status, price, payment, and freight performance to customer location, product attributes, and, finally, reviews written by customers.

This is real commercial data. It has been anonymized, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses.

This dataset is available on Kaggle, under CC BY-NC-SA 4.0 license: https://www .kaggle.com/datasets/olistbr/brazilian-ecommerce. Access to the dataset requires creating a free account on the Kaggle platform.

# About the code

This book uses a data analysis example performed in a Python environment. If this irks you, feel free to adjust the prompts to the language or environment of your choice. A large part of chapter 7 is about utilizing generative AI to seamlessly move between programming languages.

The code is organized into Jupyter notebooks, one for each chapter, which are available in an online GitHub repository (https://github.com/mariansiwiak/Generative\_AI\_for\_Data\_Analytics) and for download from the Manning website (https:// www.manning.com/books/starting-data-analytics-with-generative-ai-and-python).

Many examples of source code are shown both in numbered listings and inline with normal text. In both cases, source code is formatted in a fixed-width font like this to separate it from ordinary text.

In many cases, the original source code has been reformatted; we’ve added line breaks and reworked indentation to accommodate the available page space in the book. In rare cases, even this was not enough, and listings include line-continuation markers (➥).

You can also get executable snippets of code from the liveBook (online) version of this book at https://livebook.manning.com/book/starting-data-analytics-with-generative-ai-and-python/welcome/v-5/.

# liveBook discussion forum

Purchase of Starting Data Analytics with Generative AI and Python includes free access to liveBook, Manning’s online reading platform. Using liveBook’s exclusive discussion features, you can attach comments to the book globally or to specific sections or paragraphs. It’s a snap to make notes for yourself, ask and answer technical questions, and receive help from the authors and other users. To access the forum, go to https://livebook.manning.com/book/starting-data-analytics-with-generative-ai-and-python/discussion. You can also learn more about Manning’s forums and the rules of conduct at https://livebook.manning.com/discussion.

Manning’s commitment to our readers is to provide a venue where a meaningful dialogue between individual readers and between readers and the authors can take place. It is not a commitment to any specific amount of participation on the part of the authors, whose contribution to the forum remains voluntary (and unpaid). We suggest you try asking the authors some challenging questions lest their interest stray! The forum and the archives of previous discussions will be accessible from the publisher’s website as long as the book is in print.

# about the authors

ARTUR GUJA is a risk manager, computer scientist, systems developer, and financial markets professional with over 20 years of experience in the banking sector, delivering safe and practical solutions across IT, risk management, and financial product trading.

MARLENA SIWIAK is a seasoned data scientist and bioinformatician with a rich scientific background. She specializes in crafting business-oriented data applications and possesses a unique blend of expertise in both quantitative analysis and natural language processing tasks.

MARIAN SIWIAK is a data scientist and strategist with a track record of using data knowledge and managerial experience to successfully deliver multimillion dollar IT, scientific, and technical projects covering various areas, from life sciences to robotics. He is the developer of the first reported Artificial Sentience.

![](images/767cb39166ab0a722581ecc2fc4a7f9eeda6a6c2ac4a59011c00080f6517e529.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in formal suit and tie against blue background (no text or symbols visible)
</details>

![](images/1faaf1127aa8ee2c6e68c46eeadb02ab59487a7bebacda5d5b8bd51466188b64.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman in a light blue striped shirt against a solid blue background (no text or symbols visible)
</details>

![](images/0629c047c27e83c5bfdb7b12b3f36e582338bf667cdf4e542ed59179b3e79e0b.jpg)

<details>
<summary>natural_image</summary>

Portrait of a bald man with glasses and beard wearing a collared shirt against a blue background (no text or symbols visible)
</details>

# about the cover illustration

The figure on the cover of Starting Data Analytics with Generative AI and Python is “Quaque,” or “Quaker,” taken from a collection by Jacques Grasset de Saint-Sauveur, published in 1788. Each illustration is finely drawn and colored by hand.

In those days, it was easy to identify where people lived and what their trade or station in life was just by their dress. Manning celebrates the inventiveness and initiative of the computer business with book covers based on the rich diversity of regional culture centuries ago, brought back to life by pictures from collections such as this one.

# Introduction to the use of generative AI in data analytics

# This chapter covers

 Introducing key limitations of generative AI models   
 The role of generative AI in data analytics   
Getting started using LLMs to support data analytics

As the dust over the generative AI hype begins to settle and the notes of disappointment mix in with the chorus of praises, it may be a good time to ask yourself a question: “If LLMs aren’t the silver bullet to all world problems, what are they really good for?” Our experience using these amazing tools to improve various processes gave us the answer. They are really good, and we mean really good in supporting improvements for different processes. Throughout this book, we will guide you through our methods for utilizing the enormous potential hidden in the matrices of generative AI to improve your analytics skills without falling victim to the risks inherent in this technology.

UNDER THE HOOD To excel in these goals, you will preferably have in the back of your mind what drives the responses you get to your prompts.

However, due to the architecture-agnostic nature of this book and the rapidly changing technology landscape, we have consciously avoided the technological nitty-gritty, focusing instead on process implementation. We encourage you, though, to get a good overview of what’s what. You can learn it from several Manning books, such as The Complete Obsolete Guide to Generative AI by David Clinton or Introduction to Generative AI by Numa Dhamani and Maggie Engler. For the technical details of GPT models, see How GPT Works by Drew Farris, Edward Raff, and Stella Biderman.

In this chapter, you will learn about three important aspects of working with generative AI. As we strongly believe that first things should indeed be first, we’ll start by presenting the inherent limitations of generative AI. We already mentioned the misalignment between the expectations and results of generative AI applications. A good understanding of the unavoidable limitations is critical to avoid disappointments at your work. The second aspect is related to embedding generative AI into the data analytics process. This part of the chapter will help you develop your first intuition about when and how to use generative AI when trying to solve an analytical problem. We will also manage expectations when it comes to automating processes involving generative AI. The last part of the chapter will provide you with knowledge about methods of accessing generative AIs. In the lion’s share of cases, browser-based access to chat would be sufficient, but history teaches us that this may not be an advisable method when working with sensitive data.

The overall goal of this chapter is not to give you encyclopedic knowledge of this technology, but to ensure you have a deep enough understanding to demystify generative AI and allow for a more critical interpretation of its abilities.

# 1.1 Inherent limitations of generative AI models

In the Middle Ages, map edges had the inscription Hic sunt dracones (Latin for “Here be dragons”). You also may find monsters depicted in areas of uncharted waters. Later, the dragons, sirens, and krakens were replaced with depictions of reefs, shoals, and ice fields. We would like you to consider our warnings as the latter, rather than the former. For any endeavor, knowing the dangers to be wary of is at least as important as knowing what benefits to hope for.

The following list outlines the inherent limitations of any generative AI system. Some of them may be reduced or even removed in the future, but reading about a potentially obsolete limitation will cost you less than being unaware of even one that remains valid. So, here are the treacherous waters we should be aware of:

 Generative AIs will always provide an answer (even if it’s a wrong one)—Like a child who finished their “why?” phase, or an overpromoted manager with heavy impostor syndrome, generative AIs, when asked a question, know everything and, as their first reaction, are unable to admit the limits of their knowledge. One of the main reasons you really want to read this book is because generative AIs can be convinced otherwise. In chapter 8, we’ll also discuss the model’s sensitivity to input phrasing. Slightly rephrasing a question may result in different answers with varying degrees of quality and relevance. It’s worth noting that, since prompts are usually supplied in natural language, this sensitivity is slightly different than for search engines. The latter only react to clusters of keywords, whereas generative AI may provide a different response based not just on the keywords, but also on the grammatical structure of the prompt, its perceived emotional tone of writing, and the context created by recent exchanges.

HE SAID, SHE SAID You can help generative AI provide correct, or at least useful, answers by providing underlying LLMs with the ability to search additional data sources and require linking answers to sources. You can learn more about that form from Generative AI in Action by Amit Bahree or AI-Powered Search by Trey Grainger, Doug Turnbull, and Max Irwin, both available from Manning Publications.

 Some of the answers might be entirely made up—There are instances where generative AI provides an answer that appears plausible but is not based on facts or directly linked to the training material. This is because the model sometimes fills in gaps in its knowledge by generating content that aligns with the patterns observed in the training data, even if the information is not accurate or complete. We will cover this problem in chapter 7, when we discuss the phenomenon of AI hallucinations.   
 Inherent sycophancy—The larger the model at the base of generative AI, the more likely it is to exercise agreeability over reliability and accuracy. If confronted or questioned about the provided answer, it’s likely to apologize and present the point of view contradicting its previous statement, even if it was correct the first time—truth be damned! Generative models can even make up numbers and falsify references to support the user’s perspective!   
 Inaccurate or outdated information—Each generative AI’s knowledge is derived from the content corpus it was trained on. The model may provide outdated or incorrect information depending on the knowledge cutoff. This will be visible in examples in this book, where the model gives answers using API calls or programming language structures from obsolete versions. This is not as severe a limitation as it might initially seem. First, the majority of the concepts covered don’t evolve that quickly, and most people will have a lot of ground to cover in the basics before they reach the need to tap the latest developments. Second, many generative AIs have access to the internet. However, mixing the timeconstrained body of knowledge used to train the model with continuous updates may lead to inaccurate results. It’s also worth remembering that some generative AIs only check the internet for the latest information when directly prompted.   
Input and output limits—When using generative AIs, you should be aware that the amount of text they can process (the amount of input they can read as a

whole and, on this basis, generate the output) is limited, although it can vary greatly between different models and implementations. The unit of text processed by generative AI is called a token, and it can be a word, part of a word, or a punctuation mark, depending on the tokenization method employed. Tokenization algorithms translate text into tokens with an average of 4 tokens per 3 words, or 0.75 words per token (this value should be relatively stable). At the time of writing this book, models have context windows ranging from several thousand up to millions of tokens, and the race to truly limitless context is fullon. For now, however, the available tools offer a limited number of input (prompt) and output (response) tokens, and you should remember that the context window covers both. You will get no warning if some data falls out of the window (no pun intended) and gets forgotten. Such truncation will usually manifest itself by the model giving responses inconsistent with previous exchanges, showing it has forgotten previous prompts or responses. In section 1.3, we present methods for estimating the number of tokens used. As a way of dealing with this limitation, you may frequently summarize the conversation and its key findings to ensure they are not left out of the context window.

 Verbosity—When you try some prompts, it will quickly become apparent that generative AIs generate overly verbose responses or overuse certain phrases (e.g., they tend to “unwaveringly delve into vast landscapes of the rich tapestry of intricacies of…” anything they encounter). This verbosity can be attributed to biases or patterns in the training data, where longer responses, or responses of a particular structure, might be more common.

A WORD TO THE WISE The prompt/response size limit and the verbosity can often lead to incomplete or cut-off responses. When designing a conversation with a generative AI, one option is to ensure that the combined length of the prompt and expected response doesn’t exceed the token limit.

 Biased or inappropriate content—Despite efforts to reduce harmful and biased content, generative AIs, especially those fine-tuned on unknown data, may still generate responses that exhibit biases or produce content that could be considered inappropriate. This can result from some biases still being present in the training data, biases that are hidden or purposefully included in the prompts, or a multitude of other overlapping factors. However, the developers of most generative AIs have gone to great lengths to balance the model’s responses. An example can be found in the GPT-4 System Card document (https://cdn.openai.com/ papers/gpt-4-system-card.pdf).

Awareness of these limitations is crucial when you are interacting with generative AIs or incorporating them into various applications. Continued research and development aim to address these limitations and improve the performance and safety of generative AIs.

# 1.2 The role of generative AIs in data analytics

On groups and forums focused on generative AIs, there are dozens of questions to the effect of “Where can I find a GenAI-based tool that does [very specific task description here]?” Even if a requested tool does not exist yet, it probably will, and soon. And it’s all good. Data warehouses, lakes, lakehouses, meshes, fabrics, and so on replace Excel files, data in emails, and napkins (if not for all intended purposes). Dashboards and self-serve business intelligence (BI) platforms replace manually created reports and PowerPoint presentations (OK, questions about using generative AI to create, modify, or improve PowerPoint slides are the most common). However, beware of silver bullets. Only 0.5% of data collected in data warehouses, lakes, and so on is ever analyzed, while the remaining 99.5% generates costs and big-data hangover to companies that over-eagerly started to collect the data without a data utilization plan. BI platforms, in turn, are filled to the brim with rogue analytics (for example, data slicing and dicing that serves no purpose other than the justification of poor business decisions).

The effectiveness of generative AI use in data analytics will depend on your, the data analyst’s, ability to harness the possibilities and overcome the limitations of this new tool. Generative AIs, like any tool or technology, cannot be expected to do all the work. Let’s look closely at what we are dealing with and at generative AI’s differences from and similarities to other elements of the data analytics flow, namely the analytical process and software.

Until now, we have leaned toward the doom-and-gloom side of things, giving you a lot of warnings about generative AI’s limitations and discouraging you from jumping onto every tool labeled as “GenAI-powered” (we have an internal betting pool regarding when the first toothbrush labeled as such will hit the market). We did this on purpose as we noticed that overinflated expectations are the main blocker to the efficient use of this amazing tool. Now let’s get out of this shadow of doubt and step into the light of the bright generative AI-supported future of data analytics.

# 1.2.1 Generative AI in the data analytics flow

Years and years of working with data has convinced us that its value does not come from the complexity of the utilized technologies. We’ve seen millions of dollars saved with a simple breakdown of costs done by process rather than by organizational unit. We’ve seen millions of dollars lost because an overcomplicated market analysis involving dozens of tools and teams poorly reflected actual customer sentiments. Data analysis is not about transforming raw data into charts. It’s about supporting business decisions using conclusions from relevant business data. Your success in this endeavor will depend on a couple of aspects, of which the available tooling is just one.

Different types of data and different business questions require different analytic pipelines. If you work in a retail company, you most likely seek insights into customer behavior. Your pipeline may begin with the collection and cleaning of data from multiple sources: transaction records, customer feedback, and website interactions. Once the data is scrubbed and standardized, you will process it through algorithms performing customer segmentation, product affinity analysis, and sales forecasting. Working with a healthcare provider, your input data would include patient electronic health records, medical imaging, and sensor data from wearable devices. Your processing would employ algorithms for disease diagnosis, treatment optimization, and patient outcome prediction. If you find yourself in a manufacturing firm, you’ll be integrating data from IoT sensors on the factory floor, quality control checks, and supply chain logistics, with the analytics focused on anomaly detection, predictive maintenance, and supply/demand forecasting.

Irrespective of what you’re analyzing and for whom, the essence of the process remains the same: collect and clean input data, process it using more or less advanced algorithms, and finally, present the results to the desired audience.

The details differ greatly depending on the business area, data sources, analytical methods applied, and expected output format. Each of these topics warrants a book (or six) on how to most effectively perform each of these steps, taking into account both cost and time, using this or that technology stack.

This book does not aim to answer all possible questions about all the possible scenarios you may encounter in your work as a data analyst. We offer you something much, much better. We propose a structured method to effectively use generative AIs’ unbelievable knowledge repository (from Wikipedia to scientific papers, to books and literature, to dialogue data, to the Pile (https://pile.eleuther.ai/), and so on) to prepare an analytical pipeline tailor-made to solve exactly your problem.

THE MISSING LINK The scale of generative AIs’ abilities is only starting to be explored. However, it’s already clear that they can be taught to respond consistently and relevantly on a wide range of topics. They have the ability to drill down into details, summarize, explain, and associate related concepts to an extraordinary degree. These abilities can be used to effectively unblock your own thinking and get you out of your rut. You no longer have to trawl through dozens of random articles trying to find inspiration or pointers. Just ask a question. Even if the answer is imperfect, it may point you to concepts you haven’t thought of before. Use this to expand your horizons.

In the preface, we identified a question you should ask yourself every time you encounter a new analytical problem: where do I start ? Searching for the right input data might not be the worst possible choice, especially if it’s accompanied by an analysis of what input data is actually relevant. Let’s assume you work in a healthcare unit and get a question like “What are the average patient waiting times on Tuesdays?”, or you work in retail and are asked to analyze, “How do our customers use loyalty cards?” Do not be fooled by the simplicity of the former question. They can, in fact, both be tricky.

The flow presented in figure 1.1 will help guide you through the crucial steps in going from the question to decision-enabling conclusions, focusing on getting the most added value from both the human and generative AI along the way, while avoiding the common pitfalls. It can be applied to any analytical task and technology stack you may have. All the examples you’ll encounter in this book will follow this general structure.

![](images/dca7e2ac5ab50bccf82d55ebb7c3923d7967d874682b90c01c0869b114b6b057.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["User activities"] --> B["Problem statement"]
    B --> C["Goals of the analysis"]
    C --> D["Guidance / suggestions"]
    D --> E["Evaluation and decision-making"]
    E --> F["Implementation details / programming"]
    F --> G["How-to / code"]
    G --> H["Analysis and results collection"]
    H --> I["Initial analysis results"]
    I --> J["Interpretive augmentation"]
    J --> K["Final synthesis and decision-making"]
    style A fill:#f9f,stroke:#333
    style K fill:#f9f,stroke:#333
```
</details>

Figure 1.1 Recommended generative AI–supported data analysis flow

You always need to start with a problem statement. Let’s look at our healthcare example. We were asked a question about waiting times on Tuesdays; however, issues around waiting times on a specific day are more likely to be the symptom of a deeper problem. The question you get asked will not often translate directly into an effective problem statement. We should ask ourselves, “What real problem are we looking at here?” While it’s the job of the final decision maker to define the scope of the requested analysis, the guided questions can get you into a much better starting position for your analysis and, ultimately, provide more value from the analyzed data.

Now, the fun part. Even if the request comes from an area of operations you don’t have experience with, generative AI can help you put the received request into a business context without bothering your stakeholders with unnecessary inquiries! Let’s try a couple of generative AI on our Tuesdays-specific question.

![](images/c5404008ba69b62bc110820bc46811846c2b6c551672bd977b8e67911ea4d02b.jpg)

I work in a healthcare unit. I’ve been asked to answer a question: “What is the average waiting time for patients on Tuesdays?” What do you think could be some actual reasons behind such a question?

The answers are too long to include here, but both OpenAI’s ChatGPTs (3.5 and 4), Google Gemini and Gemini Pro, and Meta’s Llama 2 (13B) provided lists of possible project types where such an analysis could be of importance. The answers generally involve planning and budgeting (including resource allocation and staffing optimization), patient experience and quality of care, operational efficiency, and staff training.

Depending on your knowledge of current projects in your environment, you may come back with more or less specific questions, which shouldn’t be considered a waste of time. For example, if you ask a stakeholder asking for an analysis a follow-up question like, “Is it connected to our latest focus on increasing patient satisfaction?”, you could get an answer like, “Oh yeah, we’ve often heard complaints about Tuesdays, and we want to try to do something about it.” Once you understand that patient complaints and waiting times are the root issues behind the original question about waiting times on Tuesdays, your final problem statement may look something like this: “What is the distribution of waiting times and its correlation with patient satisfaction?” This question balances specificity with scope, aiming to uncover actionable insights that can directly influence patient care protocols and satisfaction.

The level of detail you disclose about your project in conversations with your generative AI advisor should be tailored to the confidentiality requirements of your analysis and the specifics of your generative AI setup. It’s advisable to share more freely within a locally managed software environment than on public platforms. This topic, including the associated risks of employing generative AI, is explored further in chapter 8.

You can then try querying generative AI about the best ways to answer the final question.

![](images/e4997109c5c80de4e755c3ea2d442d6357745d4f1f3c8ed5b1d4ff79fdfe85f4.jpg)

And how could I approach analysis leading to answering the question: “What is the distribution of waiting times and its correlation with patient satisfaction?”

Yet again, the answers are quite lengthy and detailed. They offer you seven- to ninestep approaches, which, with additional iterative inquiries, should allow you to construct a robust pipeline. Chapter 3 provides a practical example of using generative AI to develop a detailed analysis design from an extremely vague request (unfortunately, likely to be encountered in the real world). Here, our aim is to show you that the value of generative AIs extends beyond just answering highly specific queries. Their utility isn’t really reliant on the craft of “prompt engineering.” Instead, it depends on your readiness to present the full scope of your problem and to recognize that (as in the case of any meaningful conversation with a well-informed colleague) you’re unlikely to receive a flawless answer on the first attempt. Instead, expect to engage in an iterative process, refining broad concepts to meet your particular requirements.

Inquiring into details of the analysis or code and discussing the received results are common for all the steps of your analytical process on all levels of granularity. You should use them as elements of the flow of the whole project and when going through detailed substeps, such as when cleaning the data or formatting the final charts. Generative AI can help you clarify what you want to achieve at any given moment, determine how to effectively get there, and test if what you got is what you wanted.

As we mentioned, generative AI will not replace analytical tools but help you optimize their use. Let’s have a look at the areas where they shine the brightest.

# 1.2.2 The complementarity of language models and other data analytics tools

On their own, generative AIs are particularly well-suited for tasks involving text data, such as sentiment analysis, text classification, summarization, and question-answering. However, their potential extends beyond text-based tasks. Multimodal AIs like Google’s Gemini or OpenAI’s GPT-4 allow you to upload different types of files, with the latter accepting raw data in formats such as CSV. But as we mentioned before, your success as a data analyst will depend on your ability to utilize generative AIs in a wider analytical environment. Luckily, that’s precisely where you can get excellent support from generative AI. It’s like having an expert on a speed dial!

First, all generative AIs worth their mettle have deep knowledge of most analytical frameworks available on the market. They can help you navigate through a vast array of technologies to extract, process, analyze, and visualize data. Suppose you have data in a bunch of Excel files and are tasked with creating the dashboard in Power BI. Try dropping the following question into the generative AI of your choice:

![](images/03d6e0afc1336ca4417978d99331f972b5e46eab9cc5757d4f6a019b930e8b83.jpg)

I have data in a bunch of Excel files and am tasked with creating the dashboard in Power BI. What shall I do?

You will get detailed instructions, including where to click to upload your data, basic options for modeling it, and, again, where to click to prepare a dashboard. And that’s just the first step of the iteration.

Did your company just move from WordPress plugins to Google Analytics, but Google Tag Manager–based event tracking is needed for yesterday?

![](images/e654efdf8e53b33f5d1b3f327ec4fae444e33600b218d970f89b58d0e94d648b.jpg)

I’m tasked with enhancing our website’s performance and need to leverage Google Tag Manager (GTM) for tracking various user interactions. Additionally, I must provide detailed reports in Google Analytics 4 (GA4). I’m completely new to the Google environment. Can you please help?

You’ll get a good list of options, and you will be able to choose what’s right for your specific case. Again, no “prompt engineering” is needed. Just a good, old cry for help.

Second, if you’re more invested in serious data analytics, language models can generate code in various programming languages, such as Python, R, Scala, or even, for the more adventurous, PHP, Perl, or even Cobol or Intercal. The best-known example of this concept implementation is the GitHub Copilot, with software like Bito, Tabnine, Codeium, and FauxPilot (and many more) following in its footsteps. This capability allows you to obtain ready-to-use code for data processing, analysis, and visualization tasks, saving time and effort. The generated code can vary in size and complexity, from short snippets and single functions serving as a starting point for customizing and refining analyses to whole algorithm implementations and modules, limited only by your imagination and patience to coax the model to spit it out. Unlike raw code snippets downloaded off the internet, generative AI will provide code suited exactly to your needs, and it has the invaluable ability to explain the code, as we’ll see in several examples in this book, and optimize it to your specifications.

This ability to generate and explain code will be the most helpful feature for us throughout the book, but it also comes with the biggest warning, which we’ll repeat in many places and cover in depth in chapter 7. Specifically, never trust the model to spit out entirely correct answers or perfectly working code on the first try. The higher the importance or risk of your project, the more scrupulously you should verify any output through review and testing. In subsequent chapters, you’ll find examples of model-generated code that doesn’t work as expected or that has incorrect explanations attached to it. Caveat emptor!

Finally, once the analysis is performed, language models can help interpret the results by generating natural language summaries and explanations. This feature may help you understand the intricacies of complex analytical results and communicate your findings to a broader audience.

There is an old story of a math professor complaining to his colleague about students: I explained it to them three times, I finally understood it myself, and they still had questions. With generative AI, you can allow yourself to be such a student, shamelessly pestering your advisor with questions until you’re comfortable with the answer.

If you wish to practice and feel audacious, start by pasting the following prompt into multiple generative AIs of your choice.

![](images/f1132651946e4ddaa6f1a0454b3adf65176972f983e2575f1b178d09ddb14f1d.jpg)

I got a confidence interval of 0.55-0.9 using the Wilson Score Interval (95% confidence level). How should I precisely communicate what it means for the performed test?

Statistics should be a very important part of your toolbox. Generative AI can help you avoid situations where stakeholders will evaluate your analyses on this scale: small lies, big lies, and statistics.

After reading the previous two sections, you should now feel excited about adding generative AI to your data analytics practice. We share that feeling every time we accomplish our tasks in a third or a quarter of the time they used to take. But, as always with generative AI, you need to be aware of some limitations.

# 1.2.3 Limits of generative AIs’ ability to automate and streamline data analytics processes

While you can successfully employ generative AIs in all the applications listed previously and in the subsequent sections of this book (and more), their effectiveness in automating and streamlining data analytics processes has certain limitations. You can incorporate them into the data analytics domain, but their limitations make them an amazing supplement, not a replacement, for a data analyst.

# LACK OF QUANTITATIVE ANALYSIS SKILLS

Generative AIs excel at understanding and generating natural language, but they lack the inherent ability to perform complex quantitative analysis (aka math). ChatGPT has already included an add-on running Python code on the fly (utilizing an external environment, not as a native LLM capability), and other generative AIs will probably follow suit, but the success rate of the generated analytical runs, as you’ll see in the following sections, is not something we’d wage the success of our business on. Data analytics processes often require mathematical and statistical methods, such as regression analysis, time-series forecasting, and clustering techniques. While generative AIs can suggest such methods and often offer the relevant code, the code must be thoroughly tested before it is put into the production environment.

# LIMITED UNDERSTANDING OF DOMAIN-SPECIFIC CONCEPTS

While generative AIs can generate human-like text based on the context provided, their training data may not include highly specialized domain knowledge. Consequently, their ability to accurately generate insights or recommendations in the context of specific industries or niche subjects may be limited. This problem is enhanced by the already mentioned inherent inability of generative AIs to admit their ignorance. Knowledge limitations differ between generative AI providers and can be somewhat mitigated by providing GenAI with internet access, but you really don’t want to base critical business decisions on an enthusiastic hallucination!

In the case of such specific needs, your best option is to provide the model with more general prompts and refine the answer based on your specialist knowledge.

# INABILITY TO INTERACT WITH DATABASES AND APIS

Your work in data analytics will, more often than not, involve working with databases, APIs, or other data sources to extract, clean, and process data. Generative AIs lack the built-in capability to interact directly with these sources. While it is possible to integrate generative AIs with custom-built solutions to bridge this gap, doing so can be resource-intensive and challenging to implement effectively. As in the previous cases, the model can still be effectively used to guide your analysis and provide solutions or even whole swathes of code, which you can execute independently of the model.

# UNRELIABLE INTERNET ACCESS

Some generative AIs, such as Google’s Gemini, are “internet native.” The internet connectivity is a natural part of their operations. For others, not so much. Self-hosted models, which you can download and run on your machine, such as Llama 2, need access to a search engine API and an implementation of so-called multistage reasoning, where in the first answer, the LLM decides what it needs to do to get the proper answer, and in the following steps, the architecture runs the internet search and provides the answer to the LLM, which on that basis can form the final response. ChatGPT 4 implements this in its web-based interface.

It seems complicated, and it is. The connectivity of self-hosted LLMs depends on external APIs and either a lot of code or fast-changing libraries. ChatGPT, in turn, sometimes forgets it can connect to the internet. When it was trained, it couldn’t, and this memory still lingers in its network’s deep layers. If your analysis depends on access to the latest data or news, you need to choose your tools very carefully.

In the following chapters of this book, we will show you how to apply this general-to-specific problem-solving path for the best results.

# 1.3 Getting started with generative AIs for data analytics

There is an old Chinese proverb, “In the forest of algorithms, the path to wisdom has many branches.” Actually, there isn’t—ChatGPT generated it for us. We have tried to convey that, depending on the situation, you have more than one way to access your AI advisor. To utilize generative AI’s potential, you need to get comfortable with conversing with it, as most of the tools built upon it strip its answers of relevant nuance, but you should know your options here.

# 1.3.1 Web interface

In this book, we will mainly use ChatGPT (https://chat.openai.com) and Gemini (https://gemini.google.com) as examples of generative AI. These are readily accessible (it’s more true than you’d like, as this access can be bidirectional—do not paste your confidential data there!), and the underlying language models are in constant, rapid development. There is also a chance that your company will have a self-hosted generative AI based on either of these or some other model, such as the n-th incarnation of Llama or Mixtral, but hopefully it will be accompanied by a proper web interface.

AND THE WINNER IS… At the time of writing this book, GPT 4 was by far the most useful of all the tested generative AIs for any analytics-related tasks. However, this will change (just not with GPT 4o). Keep your eyes open and don’t be shy when it comes to engaging new generative AIs and testing their usefulness. Each model has its own training dataset and an architecture influencing its interpretation of your prompts and the resulting answer. Just remember that the technicalities behind them are irrelevant from your perspective (unless they are related to cost-effectiveness, of course). What interests you, as a data analyst, is the model’s ability to support your process.

If you need specific models, you can search for one of half a million hosted on the AIdevelopment website, www.huggingface.co. Some of them require downloading, but some can be run there. You can register for free, but extensive model use will require creating your own “Space” and purchasing processing power.

The use of generative AI via web interface is as simple as writing a query and reading the answer. Sometimes, there will also be a button allowing you to upload files to be analyzed.

# 1.3.2 Beware of tokens

If you plan to connect directly to a model, you must understand the critical difference between your and GenAIs’ perceptions of text. As explained earlier, generative AIs break down input text into manageable units known as tokens. This foundational step is critical, as it transforms raw text into a structured form that an AI model can efficiently process and learn from.

Tokenization involves dissecting the input text into a sequence of tokens. This process is not a mere splitting by whitespace; it’s more nuanced, incorporating an understanding of the language’s syntax and semantics. For instance, the word “don’t” may be tokenized into “do” and “n’t” to better capture its meaning and structure. Advanced models leverage subword tokenization schemes to balance the tradeoff between representing common words as single tokens and decomposing less common words into smaller, meaningful components. This approach enables the model to handle a vast vocabulary, including neologisms, with a fixed set of tokens.

TOKENS OF BABEL The method of tokenization—how the words are split before processing—is specific for each model. This is a critical point, as using tokenization meant for one model as input for another may case the latter model to interpret the input as a meaningless, or worse, misleading, soup of semi-words misaligned with how the model’s training material has been prepared.

As we warned you in section 1.1, when the input surpasses the context window, the earliest tokens are truncated, leaving the model with only the most recent tokens within its comprehension horizon. This truncation can lead to a loss of crucial context or information necessary for generating coherent and relevant responses. Have you ever been in a situation where someone overheard just the last couple sentences of a lengthy conversation and offered unsolicited advice? Such a response rarely adds to the conversation. Exceeding the context puts generative AI in a similar position. It’s “deaf ” to parts of the conversation exceeding its context window. This is particularly dangerous if you work with a large piece of code!

Several strategies can be employed to navigate the constraints of limited context windows. One common method is chunking the input text into smaller segments that fit within the model’s context window, ensuring that each segment contains enough context to stand on its own for generation tasks. Another approach involves using techniques like sliding windows or iterative refinement, where the model progressively processes text, maintaining as much relevant context as possible across segments. For more complex interactions involving longer texts or conversations, strategies like creating a summary of previous interactions or leveraging external memory mechanisms can help maintain coherence.

# 1.3.3 Accessing and using the API

For more advanced use cases and seamless integration with your existing data analysis tools, you can access most of the popular models via their application programming interface (API). These APIs suit various programming languages, including Python, JavaScript, and more. With API access, you can create custom applications, integrate generative AIs into your existing data analysis workflows, and even build GenAIpowered analytics dashboards.

To further simplify the process of integrating generative AIs into your data analysis projects, you can use available SDKs (software development kits) and libraries created by model or third-party developers, one of the most prominent being LangChain (www.langchain.com). These resources can save you time and effort when it comes to working with the API, as they provide prebuilt functions and classes that handle common tasks. You can find popular SDKs and libraries for various programming languages on platforms like GitHub. Make sure to check the compatibility and support status before using them in your projects.

# AN EXAMPLE OF PROGRAMMATIC ACCESS TO CHATGPT

You can access different ChatGPT versions through the OpenAI API. This method allows you to programmatically send requests and receive responses, giving you greater control over the AI’s capabilities. Sign up for an API key on the OpenAI website to get started (https://platform.openai.com/signup). Then, follow the API documentation to learn how to interact with ChatGPT using your preferred programming language.

To illustrate programmatic access, let’s look at an example of accessing the ChatGPT models from Python. Similar code will be used in some of the discussions in chapter 5 on using ChatGPT directly for data analysis. If you haven’t yet set up the OpenAI API, follow the instructions to install the library and set up an API key at the OpenAI signup page.

A ROSE BY ANY OTHER NAME. . . Throughout this book, we’ll work with Python (in a Jupyter environment or any Unix environment). In chapter 7, we’ll show that generative AIs are also capable of supporting many other programming environments.

Once you have the OpenAI API, it is recommended that you assign it to the OPENAI\_API\_KEY variable in the environment, either through your shell setup (depending on your system) or, preferably, through a .env file in your project. You can then use the following simple Python code to interact with ChatGPT.

Listing 1.1 Interacting with ChatGPT through the API   
```python
from openai import OpenAI
prompt_text = """Generate a list of 20 keywords indicating positive
→sentiment to be used for searching customer reviews in
→Portuguese."""
client = OpenAI(
    api_key=<<your-API-key-here>>, 
)
chat_completion = client.chat.completions.create(
    messages=[
    {"role": "system", "content": "You are a scientific assistant, skilled
    →at explaining science to schoolchildren."},
    {"role": "user", "content": "Explain resonance to first-graders?"},
    {"role": "assistant", "content": "Alright, kids, today we're going to
    →talk about something really cool called resonance! (...)."},
    # Shortened from the full model response
    {"role": "user", "content": "Where can we use it?"}
], 
```

```txt
model="gpt-4-0125-preview", temperature=0.7,  
)  
print(chat_completion.choices[0].message.content) 
```

The preceding code sets up an example exchange to be further completed by the model. It exemplifies how the model can handle multiturn exchanges (for example, multiple question-answer iterations) with context. The main input is the messages array of message objects, where each object consists of two components:

A role, either system, user, or assistant   
 The content

A system-role message is typically included first, followed by alternating user and assistant messages. The system-role message sets up the background for the behavior of the assistant. The example in listing 1.1 modifies the assistant’s personality to reflect the style of responses we want it to take. This can be omitted, and without any specific tone or audience requirement, the model will reply in its usual helpful but flat language.

The rest of the messages should consist of alternating user and assistant content, providing the model with the exchange context. Initially, you can provide one user message to which the model should respond. In subsequent exchanges, you can build up the message array with the history of prompts and responses to provide the model with a context of the exchange so far, allowing the model to relate better to subsequent prompts. By default, the models have no memory of past requests, and all the relevant information must be supplied as part of the message array in each request.

The model parameter specifies which instance of LLM we want to access. It’s best to refer to the OpenAI models website (https://platform.openai.com/docs/models/) for the latest list of available models, as it changes quite frequently. To get started, a good choice would be to experiment with the following:

gpt-4—The latest production version of the GPT 4 model   
gpt-4o—A younger, faster, if less thoughtful brother of GPT 4   
gpt-3.5-turbo—Still a very good choice, and it can be more cost-effective in some cases   
dall-e-3—Optimized for image generation   
tts-1—Designed to generate natural-sounding speech from text   
whisper-1—Can recognize speech and transcribe it as text

New models are being developed continuously; the preceding list illustrates the breadth of capabilities already available. Obviously, for the models using images or sound as either input or output, more advanced programming techniques will be required to interact with them.

Listing 1.1 used only one of the plethora of other optional parameters: temperature. As you can guess, this controls randomness in the model responses. Increasing temperature can generate interesting results, but it has a high risk of causing the model to hallucinate. Experimenting with this is very interesting, but please use it cautiously in production environments. We’ll touch more on hallucinations and related risks in chapter 8.

Refer to the latest OpenAI documentation for other up-to-date information and additional parameters.

# PROGRAMMATIC ACCESS TO OTHER OPENAI API-COMPATIBLE MODELS

Many models are available in the market (over a million models in HuggingFace alone), each with its own interface. However, a lot of them are compatible with OpenAI API de facto standards, such as Meta’s Llama models.

To access these models, you can just replace the OpenAI API call code in the previous example.

Listing 1.2 Code to direct the client to a specific model, e.g., Llama   
```txt
client = OpenAI(
api_key = "<your_llamaapi_token>",
base_url = "https://api.llama-api.com"
) 
```

The base URL parameter specifies the server hosting the model. Obviously, you’ll need to provide a specific API key, such as the Llama API token referenced here, as each provider will require their own user authentication.

Additionally, as you probably noticed, we used the “gpt-4-0125-preview” model in listing 1.1. If you switch to Llama, you’ll need to provide a valid model, such as “llama-13b-chat” or one of the other available Llama variants. The rest of the code can remain unchanged most of the time.

# EXAMPLE OF PROGRAMMATIC ACCESS TO GOOGLE VERTEX AI

A slightly different API worth mentioning is the one defined by Google to access its powerful Gemini AI models, as well as Codey, which is optimized for code generation and completion, and Imagen, designed for image generation, editing, captioning, and visual question answering. Given the power of Google in the market, this API may also be a good contender for a standard in the future.

The quickest way to access these models is through the Cloud Shell (https:// cloud.google.com/shell/docs/launching-cloud-shell), which is a terminal, or command line, used to access cloud services. Once you activate the shell, you need to install the API.

Listing 1.3 Command to install the Google AI package on Google Cloud   
```batch
pip install "google-cloud-aiplatform>=1.38" 
```

Then you can use the following script to generate completions from the selected model.

Listing 1.4 Example code to call Vertex AI on Google Cloud   
```python
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession,
→HarmCategory, HarmBlockThreshold
# Replace PROJECT_ID with the ID of your Google Cloud project.
my_id = "PROJECT_ID"
# Replace with your Google Cloud location
my_location = "us-central1"
def generate_text(project_id: str, location: str, prompt: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    model = GenerativeModel("gemini-1.0-pro")
    # Generation config
    config = {"max_output_tokens": 2048, "temperature": 0.4, "top_p": 1, "top_k": 32}
    # Safety config
    safety_config = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:
    →HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT:
    →HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    }
    # Generate content
    responses = model.generate_content(
    [prompt],
    generation_config=config,
    stream=True,
    safety_settings=safety_config,
    )
    text_responses = []
    for response in responses:
    text_responses.append(response.text)
    return "".join(text_responses)
    prompt = "What are all the colors in a rainbow?"
    print(generate_text(my_id, my_location, prompt)) 
```

The preceding code follows a similar flow as the OpenAI example. Apart from the project ID and location, which Google uses to authenticate access to the API, we need to specify which model we want to use. In this case, we chose “gemini-1.0-pro”, the basic text-only model. Google’s API also supports multimodal requests, including sound and images both in the input and response. A range of examples is available on the API web pages. We’d need to specify the “gemini-1.0-pro-vision” model for multimodal requests.

Listing 1.4 also shows how to provide the temperature parameter, analogous to the one discussed in the OpenAI example, which is used to control the randomness in the responses.

It’s worth mentioning that Google provides an interface for explicitly setting the safety parameters of the model to block unsafe content, based on a list of defined blocking thresholds (table 1.1). The safety parameters can limit the model when it comes to generating content containing harassment, hate speech, explicit sexuality, or that may otherwise be dangerous. The full list for the newest Google models is provided on Google’s AI website (https://ai.google.dev/gemini-api/docs/safety-settings).

Table 1.1 Blocking thresholds for configuring Google’s model safety parameters 

<table><tr><td>Threshold name</td><td>Description</td></tr><tr><td>BLOCK_NONE</td><td>Always show, regardless of the probability of unsafe content.</td></tr><tr><td>BLOCK_ONLY_HIGH</td><td>Block when there is a high probability of unsafe content.</td></tr><tr><td>BLOCK_MEDIUM_AND_ABOVE (default)</td><td>Block when there is a medium or high probability of unsafe content.</td></tr><tr><td>BLOCK_LOW_AND_ABOVE</td><td>Block when there is a low, medium, or high probability of unsafe content.</td></tr><tr><td>HARM_BLOCK_THRESHOLD_UNSPECIFIED</td><td>The threshold is unspecified, so block using the default threshold.</td></tr></table>

In listing 1.4, we set very conservative parameters, safety\_config = {...}, so the model would apply quite stringent filters to the output. This may result in a lower risk while the model is used, but at the cost of returning less useful responses to some prompts. Chapter 8 will offer a broader discussion of model risk considerations.

# 1.3.4 Third-party integrations of generative AI models

In addition to the methods mentioned in previous sections, you may also find a number of generative AI models integrated into various third-party applications and plugins. These integrations typically focus on specific use cases, such as code generation and completion, data visualization, natural language processing, or predictive analytics.

These are some examples of such integrated models:

GitHub Copilot, designed to assist with code generation, completion, and explanation, with integrations available for the most common integrated development environments (IDEs), such as VSCode, Visual Studio, and the JetBrains suite of IDEs.   
Packages within the RStudio IDE, like air, provide integration of LLM models into this popular R and Python environment.

The advantage of such integrations is that they usually have direct access to the data or code inside the host environment and are able to directly insert and modify the code, which saves the user the effort of copying each code snippet from the IDE to the model chat window and back again.

# 1.3.5 Running LLMs locally

Running any downloadable model on your personal computer isn’t rocket science. You don’t need NASA-grade equipment either; a decent PC with enough RAM should suffice (with a definition of “decent” being somewhat dynamic). A solid GPU would speed things up, but that is not an absolute requirement. You will need some familiarity with the command line and a couple of libraries to bridge the gap between ambition and reality.

Let’s look at how we can use Python to connect to the Llama 2 model. Implementing it as advertised on Meta’s page is a bit daunting, so we’ll cheat a little. First, we’ll use a quantized model to save on RAM requirements. In essence, quantization of the model means “shaving off,” or rounding, the model weights, sacrificing a little accuracy in exchange for computational efficiency. We’ll also utilize models transitioned into an easy-to-use GGUF file format. If you requested and got a proper license from Meta, you can download the Llama of your choice from the HuggingFace portal.

Two libraries we propose to make your task easier are LangChain and llama-cpppython. Overall, the environment setup is as simple as presented in listings 1.1 and 1.2. It’s worth mentioning that LangChain could also be used to streamline connecting to ChatGPT or Gemini as well.

# Listing 1.5 Command to install the LangChain and Llama libraries

pip install langchain llama-cpp-python

A word of fair warning. The llama-cpp-python library has some non-negotiable requirements, especially when installed in a Windows environment. However, as it’s a fast-developing tool, check the library site for the latest details.

Now that we have our model downloaded and the proper libraries installed, all we need to do is send a prompt to a model and capture the result.

# Listing 1.6 Example of sending a prompt to Llama

from langchain\_community.llms import LlamaCpp

```python
llm = LlamaCpp(model_path='path_to_your_gguf_model_file')
response = llm.invoke('Your prompt!')
print(response) 
```

And that’s it! Depending on your hardware and the chosen model size, you should get your answer in anywhere from a few seconds to a few minutes.

CONTEXT IS NOT ONLY ABOUT TOKENS The minimalistic implementation we have presented here does not have any conversation memory. It’s a shootand-forget method of getting a specific answer to a specific question. Implementing chat memory using LangChain is, however, relatively simple, and you should not be afraid to check the website for current instructions.

Funnily enough, it even has an LLM-powered chatbot to answer your questions about the library.

There are many options for both model instantiation and prompt development, which you may find useful. You’ll find detailed instructions on the LangChain library website (www.langchain.com). We will not dig into them deeper, as this simple setup is sufficient for our purposes: asking Llama a question and getting an answer.

# 1.3.6 Best practices and tips for successful generative AI implementation

Although this book won’t cover advanced topics related to the direct integration of generative AI into applications using APIs, we encourage you to follow some best practices and consider the following tips to successfully integrate generative AIs with your data analytics solutions:

 Define clear objectives —Start by clearly identifying the goals and expectations of integrating generative AI into your data analytics solution. Determine the tasks you want generative AI to perform, such as data preprocessing, generating insights, or creating visualizations, and tailor your integration accordingly.   
 Familiarize yourself with the API or SDK you are planning to use —Thoroughly read and understand the OpenAI API documentation, including details about the API’s or SDK’s features, limitations, and best practices. This knowledge will help you design efficient and reliable interactions between generative AI and your data analytics tools.   
 Use appropriate data formats—Ensure that you are using compatible data formats when sending requests to and receiving responses from generative AI. Transform your data, if necessary, to ensure seamless integration and prevent data loss or misinterpretation.   
Monitor usage and costs—Keep track of your API usage to prevent unexpected costs, especially when working with large datasets or complex analytics tasks. Implement rate limiting, caching, or other optimizations to manage your API calls and stay within your plan’s limits.   
 Handle errors and timeouts—Implement proper error handling and retry mechanisms to deal with potential issues, such as timeouts or rate-limit errors. This will help ensure the stability and reliability of your integration.   
 Simplify and optimize your prompts—Craft your prompts carefully to obtain the most accurate and relevant results from generative AI. Use clear, concise language, and provide enough context to help the AI understand your requirements. You may need to experiment with different prompt structures to find the best approach for your specific use case.   
 Maintain the prompt cheatsheet after optimizing (and verifying the output) —Regularly update and refine your prompt notes as you continue to work with generative

AI. As your application evolves and your understanding of AI capabilities deepens, your cheatsheet should evolve to include new findings, common errors to avoid, and updated best practices.

 Provide source material and context—Alongside the problem or question, give the model context data examples or explicitly ask it to follow a certain reasoning path. You can also suggest steps in the prompt for the model to follow in its reasoning or ask it to explain certain solution steps. All of this will ensure a greater probability of a correct response and increased transparency regarding how it was generated.   
 Evaluate the AI’s output—Generative AI’s output may not always be accurate or relevant. Always double-check the results provided by the AI, and consider implementing human review or validation processes, especially for critical or high-stakes decisions.   
Test and iterate—Before fully integrating generative AI into your data analytics solution, thoroughly test its performance with various tasks and datasets. This will help you identify any issues, limitations, or inaccuracies. Continuously iterate on your prompts, data formats, and integration methods to improve the overall effectiveness of the AI in your analytics workflows.   
 Ensure data security and privacy—When working with sensitive data, make sure you comply with data protection regulations and follow security best practices. If you’re working with cloud-based generative AI, encrypt data when transmitting it to and from the provider, and consider using data anonymization techniques to protect the privacy of your users.   
Stay updated on generative AI developments—Keep track of updates and new features developed in the field, as these may impact your integration or offer additional capabilities. Regularly review the API documentation, and subscribe to relevant newsletters or forums to stay informed about any changes or improvements to generative AI.   
 Leverage community resources—Take advantage of resources provided by the AI community, such as sample code, tutorials, and forums. These resources can help you learn from others’ experiences and discover best practices for integrating generative AIs with various data analytics solutions.

By following these best practices and tips, you can successfully integrate generative AI into your data analytics workflows and harness its full potential to enhance your decision-making, automate tasks, and uncover valuable insights.

Hopefully, after this introduction, generative AI no longer appears to be a mysterious and, possibly, useless invention. Subsequent chapters will demonstrate specific exchanges between a human and a generative AI and will show us using the responses in all aspects of data analytical work. We’ll also comment on the shortcomings and pitfalls that need to be looked out for to make this cooperation between humans and AI as painless and productive as possible.

# Things to ask generative AI

 What are your limitations?   
 What is the knowledge base you’ve been built upon?   
What is the latest version of <insert favorite analytics tool> that you know about?

# Summary

 Generative AI and derivative tools have taken great strides in recent years and can be used as invaluable support in many fields, including data analytics.   
 Despite the progress, these tools won’t (yet!) replace a competent data analyst, and there are many limitations that users should be aware of.   
 At the same time, we encourage you to take full advantage of the immense possibilities of supporting your data analytical work with these language models, which can be done safely by following a few common-sense guidelines.   
 The easiest way to access generative AIs is via their web interfaces, although APIs and SDKs can be used in more advanced applications.

# Using generative AI to ensure sufficient data quality

# This chapter covers

Best practices for ensuring high quality of data   
Using generative AI to prepare a data cleaning protocol   
 Evaluating data content quality   
Dealing with data errors   
 Investigating unclear data

In MS Excel, you can calculate the trend line and standard deviation of a sample on the basis of just two data points. Clearly, such “data analysis” is meaningless. This chapter will help you focus your efforts on things you should do with data, rather than just expand on what you can do with it. It explains the necessary background for any analysis you may wish to perform. You will learn about best practices and non-negotiable rules, ensuring that your conclusions are related to the business activities you’re analyzing, rather than to flaws in the underlying data.

You’ll develop a structured approach to quality assessment and assurance, you’ll purge your data of artifacts, you’ll identify the blind spots, and you’ll learn to think about the benefits and risks of guesstimating missing pieces. Finally, you’ll learn to look at the collected data from a new perspective—the perspective of its usefulness for the process of analysis.

# 2.1 On a whimsy of fortune

Imagine you bet your business future on the flip of a coin. Let’s say you bet on tails. You threw the coin and, fortunately, got tails. Do you think it would be a good idea to do this again? And again? We most assuredly hope not. The fact that you once got the tails you bet on doesn’t mean that you will get tails again next time.

In classical logic, conclusions drawn from false assumptions can be either true or false. It’s crucial to understand that you really can draw a true conclusion from a false assumption. We will call such a conclusion an unreliable one. It doesn’t mean you’ll be right the next time you follow that false assumption.

Coming back to our example, let’s say you weigh a coin in your hand and say to yourself, “I’m going to flip this coin. If I get tails, I’ll have more customers next month than I did this month.” You throw your coin, get tails, and have more customers next month. Was the assumption that the coin has a predictive power related to the success of your business true? Probably not. We could get into psychology, the influence of self-belief on success, and so on, but even then, it’s not the coin that brought your customers. It was your self-belief and hard work. Or perhaps luck. Or weather. Or a smart marketing strategy. Or your main competitor’s mishap. Or . . . you get the idea. Nevertheless, if you believe in the predictive power of the coin, you’d draw true conclusions from a false assumption.

Similarly, business analytics performed on false assumptions (false input data) may result in true or false conclusions. Poor quality input data leads to unreliable results regardless of the sophistication of the analysis, with the critical word here being unreliable.

Let’s assume you risked performing an analysis on poor data, and it returned “good” results. You bet on tails and got more customers next month. It doesn’t sanctify the approach. Yes, it happens, but it doesn’t mean your results will be good next time. Like flipping the coin, you will get heads or tails, and your next analysis will yet again yield unreliable results.

In data analytics, this concept is often referred to as “garbage in, garbage out.” You now know that “garbage out” doesn’t mean inaccurate results. It’s much, much more dangerous. It means unreliable results. You bet 10 bucks on a flip? How about 100? Did you succeed again? How about a car or a house?

On the other hand, if you throw the coin multiple times and get your expected tails each time, the coin may not be random after all. Perhaps the quality of your data and, therefore, the following analysis is sufficient for your purpose.

Reliability of results depends heavily on the quality of the input data. In many cases, we try to avoid being too absolute about the advice we give, as there is often more than one way of solving any given problem. However, if your analysis is to be used in any decision-making process, you simply cannot accept anything less but the best possible quality of available data. We emphasized the word possible for a reason. In most realworld scenarios, you will not have the luxury of working with the quality of data you’d want. But all the compromises you make here must be conscious and taken into account when evaluating the reliability of the final result.

Unfortunately, despite some marketing claims, there is no one-size-fits-all solution ensuring data quality. The most effective way to prepare for analysis is to closely examine the data and carefully consider the meaning of each variable within the specific context of your business. There may not be any way to entirely automate this task, but there are techniques and protocols that can help you approach data evaluation and cleaning in a structured and systematic manner.

# 2.2 A note on best practices

Let’s clean our data, then! Take the first data file you have on your desktop or in your project repository, and open it. Is it “clean”? (And if you do actually keep data files on the desktop, have a hearty chat with the generative AI of your choice about data management and governance.)

TRUST, BUT VERIFY If you got your data from someone who told you that it is “clean,” ask yourself a question—do you trust this person’s data skills and (not “or”; specifically “and”!) diligence enough to hinge the success of your business on their opinion about what it means that data is “clean”? Even if you do trust them, control is the highest form of trust in the data world: better safe than sorry, look before you leap, and so on.

If you’re uncertain about whether your data is clean, we’re on a good path. Several aspects must be checked before you deem your data clean enough to be analyzed:

 Relevance—The data should be pertinent to the specific business question or problem being addressed. Irrelevant data can lead to confusion and detract from the focus of the analysis.   
 Accuracy—The data should be correct, error-free, and consistent with the realworld objects or events it represents.   
Completeness—All required data points should be present. Any missing or incomplete information should be identified and addressed. At the same time, spurious data should be avoided to maintain clarity.   
 Timeliness—Data should be up-to-date and relevant to the analyzed period. Outdated data can result in misleading or irrelevant insights.   
 Uniqueness—Duplicate data should be identified and eliminated to prevent redundancies and inaccuracies in the analysis.   
 Consistency—Data should be consistent across different sources, formats, and systems. Inconsistencies can lead to incorrect conclusions or insights.   
 Integrity—The relationships between data elements should be maintained, ensuring the data is coherent and meaningful when analyzed.

It looks like a lot of work because it is. You want to be sure that your data adequately describes the slice of reality you’re analyzing (first four points) and that its structure allows for reliable analysis (last three points).

SLOW IS SMOOTH, AND SMOOTH IS FAST Data quality is not a place to skate on thin ice. You need to get used to doing things systematically. A lot of data specialists claim that at least 80% of data work is related to data cleaning and preparation, and these are rather slow processes. Unfortunately, you may be pressed to omit it, due to a very unpleasant feedback loop. Businesses do not see the value of analysis, so they demand more of it. The more they demand, the higher the time pressure. The higher the time pressure, the more corners that are cut (usually in areas that do not get into final reports and thus are invisible or useless from the perspective of the business sponsors). The more corners that are cut, the less reliable the analysis. The less reliable the analytics, the lower the subsequent value of said analytics. The lower the value of the analytics . . . Doing things right from the start will reduce the bumps and hiccups on your analytical journey, caused by your stakeholders coming back to you, requesting repeat analyses better aligned to the reality they observe.

Ensuring data quality can be daunting—there is no silver bullet, and cutting corners can lead to unreliable data (and therefore unreliable results). But there is still hope: a good structure can guide you through this process in a finite amount of time. Knowing what to look for, and when, can help you discover the quality issues and estimate their impact on the final analysis.

# 2.3 Getting started

Do you still have your data file open? Yes, the one from your desktop. No? Open it. Have a look at it. Scroll it up and down, and if needed, left and right. Try to get to know your data.

Do you think you look silly? Not as silly as you’ll look trying to explain why you added the sales volume to the physical product volume (yes, we’ve seen it). In an ideal world, you’d have richly described metadata explaining all the columns down to the expected decimal places and the name of the person who wrote the script that parses texts scraped from the web (if applicable). But most probably, you won’t. You’ll get the file with “address”, “time”, and “sales” columns, and it will be up to you to decipher whether the addresses are of customers or brick-and-mortar shop locations; whether the sales are in USD, EUR, or metric tons; and whether the time is the time of order or purchase, or perhaps a test column left by developers.

We will repeat this again. If you work in business and are not absolutely, positively sure about the exact meaning of the variables received from your IT department, don’t assume. Ask! We happened to analyze the efficiency of a service sending tens of millions of messages to the clients of a multinational company. We discovered an anomaly that would occur very rarely, where the ratio of opened-to-received messages was higher than one. Trying to understand what was actually defined as a received message and what was actually defined as an open message, we discovered that the error in the logging system was so deep that all the previous analytics on the efficiency of messaging were worthless! We cannot overemphasize the importance of close collaboration between the business and data or IT crowds.

From clay tablets to AI, tools change, but the mess in the data doesn’t. What did change with the introduction of generative AI is your access to expert knowledge, which may save you a lot of time. It won’t replace your experience and responsibility for understanding your data, but it may help you get to know it much quicker.

If you have read the available metadata, there are still a couple of steps you should take to make this initial inspection a part of a structured analytical approach. What steps? We could tell you, but this book wouldn’t be about generative AI then, would it?

We want you to accept that your AI advisor is infinitely patient and perfectly nonjudgmental. There is no question too simple to ask. “What was the name of this curve . . . you know, this looking like the hill? How do I plot two columns from a Data-Frame?” Honestly, searching one’s own memory is sometimes more time consuming than dropping a quick question and running the provided code.

We also want you to forget about “prompt engineering.” It has its place, and some models, such as smaller Llama versions, are incredibly vulnerable to prompt structure. Changing a single word to a synonym can sometimes drastically change the model’s understanding of the prompt. We assume, however, that you will use a generative AI that understands the linguistic context sufficiently to not require more work on prompt engineering than it would take to find relevant information about actual analytics elsewhere.

NOTE As mentioned in the “about this book” section (before chapter 1), we mainly use the Python environment to process example datasets. Chapter 7 will guide you through using generative AI to adapt the code to your environment if needed.

Let’s see how generative AI (in this case, ChatGPT 4) deals with a plain language question to the effect of “I’m lost and need guidance.”

![](images/90afa34eed00ec75797de141a49f0a8fc0168cb1478a7fc4bd8331b89db8e448.jpg)

I want to perform data analysis. I imported my data into pandas DataFrames. What is the first thing I should do with it?

![](images/1d569ef57cd43d29229294f052a92daaa2d25a4701ae48d35de0c8d3916577b8.jpg)

After importing your data into pandas DataFrames, the first thing you should do is to explore and understand your data. You can start by performing the following steps:

1 Inspect the first few rows of the DataFrame: Use the head() method to display the first few rows of the DataFrame. This will give you a quick overview of the data structure, column names, and the type of data contained within each column.

df.head()

2 Check the shape of the DataFrame:

Use the shape attribute to get the dimensions of the DataFrame (rows and columns).

df.shape

3 Obtain summary statistics and data types:

Use the info() method to get a summary of the data types, number of non-null values, and memory usage of the DataFrame.

```txt
df.info() 
```

4 Generate summary statistics for numerical columns:

Use the describe() method to get summary statistics for the numerical columns in the DataFrame. This will give you a sense of the central tendency and dispersion of the numerical data.

```cmake
df.describe() 
```

5 Check for missing values:

Use the isna() method in conjunction with the sum() method to count the number of missing values in each column.

```txt
df.isna().sum()
```

6 Investigate the categorical columns:

For categorical columns, you can use the value\_counts() method to get a count of unique values and their frequencies.

```txt
df['column_name'].value_counts() 
```

Once you have a better understanding of your data, you can proceed with data cleaning, preprocessing, and analysis. This may involve handling missing values, encoding categorical variables, feature engineering, and other tasks based on the specific requirements of your analysis.

In its first sentence, our AI advisor agreed with the importance of understanding your data. A careful read of the rest of the model’s answer may reveal some less impressive components. Some steps seem redundant. For example, the df.isna().sum() method does not offer any information not previously provided by df.info() (which, in fact, also includes information returned by df.shape).

YOU NEED TO DECIDE ON YOUR PRIORITIES Efficiency versus readability is just one of the choices you’ll have to make when choosing the methods you’ll be using to reach your goals. Generative AI, when inquired, can often present you with the benefits and weaknesses of different methods. Still, you need to be conscious of these choices and sometimes explicitly request a specific method or solution, prioritizing one characteristic over the other.

Nevertheless, the overall answer is very good. Like the old carpenter’s adage says, it’s better to measure twice. We appreciate that ChatGPT errs on the side of redundancy. Provided with a wide enough toolset, you’ll soon be able to select the tools that best suit your analysis style. Equipped with insufficient tools, you may stay in the dark.

In summary, you want to check the following:

1 The overall “look” of the data.   
2 The size of the tables.

3 The types of variables in each column. The quick check should reveal whether there are mismatched data types, such as text strings in place of numerical values or vice versa.   
4 For numerical columns, the basic statistics, count, mean, extreme values, etc.   
5 The number of missing values in each column. A note of a warning here: some data is inherently sparse. Simply counting the missing values in the column will not provide a definite answer on data completeness; however, if you combine it with the knowledge of data meaning, it should.   
6 The number of unique values in each column.

This should give you a good intuition about the data you’re working with.

Let’s load our example data so we have something to analyze: the Brazilian e-commerce public dataset by Olist (www.kaggle.com/datasets/olistbr/brazilian -ecommerce). As we mentioned in the preface, you’ll need to use a free Kaggle account. The following listing shows the code we used to load our data. (All the code required to perform the analytics we present is available in our GitHub repository, https://github.com/mariansiwiak/Generative\_AI\_for\_Data\_Analytics.)

Listing 2.1 Preparing variables for further analysis later in the chapter   
```python
import pandas as pd

df_customers = pd.read_csv('olist_customers_dataset.csv')
df_order_items = pd.read_csv('olist_order_items_dataset.csv')
df_order damages = pd.read_ csv('olist_order Payments_dataset.csv')
df_order_reviews = pd.read_csv('olist_order_reviews_dataset.csv')
df_orders = pd.read_csv('olist_orders_dataset.csv')
df_products = pd.read_csv('olist_products_dataset.csv')Jupyter
df_sellers = pd.read_csv('olist_sellers_dataset.csv')
df_product_category_translation =
→pd.read_csv('product_category_name_translation.csv') 
```

As the next step, we’ll look at the properties of the DataFrames in listing 2.1. Unfortunately, that means running all of the commands proposed by our generative AI advisor for all downloaded datasets. That’s a habit you should develop for every bit of data you import.

Did you just stop reading and run all the tests on all the DataFrames? Let’s try to induce in you a healthy dose of paranoia. We’ll share some alarming findings to show you how looking at data summaries can point you to potential problems. We’ll also work on identifying the solutions.

We found two interesting points while we waded through the data structures in our example data:

 The number of customers in the df\_customers DataFrame and the number of orders in the df\_orders DataFrame are identical. There are two possibilities. One is that each customer, as identified by the system, made one and only one purchase, and the second is that we have been provided with an incomplete set of data. Both possibilities have far-reaching implications related to further analytics. (The number of 99,441 rows has arbitrarily been set by whoever generated this dataset for us. In this case, reading the metadata on a dataset would tell us this, but let’s assume it’s not available.)

 The df\_customers DataFrame contains two suspiciously similar columns: customer\_id and customer\_unique\_id. As we will probably want to analyze customer properties in other DataFrames, the column that will allow us to connect them is customer\_id. As such, this column is of great importance, so we should stop and ask if customer\_id is indeed a unique identification for customers.

As we mentioned and will keep mentioning, it’s of utmost importance not to wave away anything that doesn’t look right! You could send an email with questions to whoever provided you with the data and, depending on their workload, get the answer within minutes or months.

If you’re not fluent enough in the available analytical environment, fret not! As long as you know what you want to do, you have a generative AI advisor to help you determine how.

![](images/6fd6139980e3e50df31a3f63ee9446bd005841dae94eb5e915e5b16275202e47.jpg)

I have a pandas DataFrame with customer\_id and order\_id columns. How can I quickly check if every customer made just one order or if there are customers who made more than one order?

![](images/2b0e6bd6969d450c5d845acd56bcd1e5594522ca8b82c957a98134ff626e4452.jpg)

You can quickly check if every customer made just one order or if there are customers who made more than one order by using the value\_counts() method on the 'customer\_id' column and then checking the maximum count. Here’s an example:

```python
import pandas as pd

# Sample DataFrame
data = {'customer_id': [1, 2, 3, 4, 2],
    'order_id': [101, 102, 103, 104, 105]}

df = pd.DataFrame(data)

# Count orders per customer
order_counts = df['customer_id'].value_counts()

# Check if any customer made more than one order
if order_counts.max() > 1:
    print("There are customers with more than one order.")
else:
    print("Every customer made just one order.") 
```

In this example, df['customer\_id'].value\_counts() returns a pandas Series containing the number of orders for each unique 'customer\_id'. If the maximum value in this Series is greater than 1, it means that at least one customer has made more than one order.

Generative AI understood what we wanted to achieve and proposed code we could adapt to our needs, replacing just the name of the DataFrame to be tested with df\_orders, as we defined it when loading our datasets.

You can check the results in the files we placed in the repository. It shows that either we got the data from the online platform with the lowest customer retention rate in existence (one visit per user) or there is a problem with the customer\_id column in the df\_orders DataFrame.

We previously noted that the customer\_id column in df\_customers DataFrame is accompanied by a customer\_unique\_id column, which seems redundant if the customer\_id column was constructed correctly. The following conversation will show you that working with generative AI is indeed different from using any other software you have ever encountered. All you need to do is provide a plain language explanation of the problem you need to solve.

# MA

In my DataFrame containing customers’ data, I have two columns: customer\_id and customer\_unique\_id. How can I check how one relates to the other and which one contains actual identifiers?

![](images/2c23f7f02224155a08a74887be021152c217c107c7ee277fea797932550a32ea.jpg)

To check how the customer\_id and customer\_unique\_id columns relate to each other and which one contains actual identifiers, you can analyze the uniqueness of the values in each column and their relationship. Here’s an example of how you can do this using pandas:

```python
import pandas as pd

# Sample DataFrame
data = {'customer_id': [1, 2, 3, 4, 5],
    'customer_unique_id': [1001, 1002, 1002, 1004, 1004]}

df = pd.DataFrame(data)

# Check the number of unique values in each column
unique_customer_ids = df['customer_id'].nunique()
unique_customer_unique_ids = df['customer_unique_id'].nunique()

print(f"Unique customer_id values: {unique_customer_ids}")
print(f"Unique customer_unique_id values: {unique_customer_unique_ids}")

# Check the relationship between the two columns
relationship = df.groupby('customer_unique_id')['customer_id'].nunique()

print("\nRelationship between customer_unique_id and customer_id:")
print(relationship) 
```

In this example, df['customer\_id'].nunique() and df['customer\_unique \_id'].nunique() return the number of unique values in each column. Comparing these numbers can give you an idea of which column is more likely to contain actual identifiers.

Next, df.groupby('customer\_unique\_id')['customer\_id'].nunique() groups the DataFrame by the customer\_unique\_id column and computes the number of unique customer\_id values for each group. This will help you understand the relationship between the two columns.

Based on the results, you can determine which column contains actual identifiers and how they are related. For example, if customer\_unique\_id has fewer unique values and each customer\_unique\_id maps to multiple customer\_id values, it may indicate that customer\_unique\_id is the actual identifier, and customer\_id represents multiple records or transactions for each unique customer.

That’s an interesting response, mainly because it doesn’t suggest that the answer will be definitive! There is even a possibility that none of these columns are valid identifiers (see, this is how you get paranoia in this line of work). That point is essential. Don’t assume anything about data you received from an uncertain source, even if you firmly believe and logic dictates that some values mean one thing or another. In nine out of ten cases, it will be what you expect, but in that tenth case, you’ll thank us after reaching out to the data source and learning what this or that variable actually means.

Returning to our analysis, the resulting relationship Series is too big to analyze manually. This is another important lesson about working with generative AI. Do not settle for the answers if the result is unsatisfactory. Complain!

![](images/a702ad3333091777449cbf59a1e4de1a9172efc9f41069bf795c96be55261354.jpg)

With my data, the relationship Series produced by your previous code is too long to check manually. Can you propose a method to analyze its contents?

![](images/16177459cd28623a83e45bfba80c70512e643f77719fd6d05610ef4231e53293.jpg)

Sure! You can analyze the relationship Series by generating a summary of its contents, such as the minimum, maximum, mean, and count of unique customer\_id values per customer\_unique\_id. Here’s an example of how you can do this:

```python
import pandas as pd

# Sample DataFrame
data = {'customer_id': [1, 2, 3, 4, 5, 6, 7],
    'customer_unique_id': [1001, 1002, 1002, 1004, 1004, 1001, 1004]}

df = pd.DataFrame(data)

# Check the number of unique values in each column
unique_customer_ids = df['customer_id'].nunique()
unique_customer_unique_ids = df['customer_unique_id'].nunique()

print(f"Unique customer_id values: {unique_customer_ids}")
print(f"Unique customer_unique_id values: {unique_customer_unique_ids}")

# Check the relationship between the two columns
relationship = df.groupby('customer_unique_id')['customer_id'].nunique()

print("\nSummary of the relationship between customer_unique_id and customer_id:")
print(f"Min: {relationship.min()}")
print(f"Max: {relationship.max()}")
print(f"Mean: {relationship.mean()}")
print(f"Count of unique customer_id values per customer_unique_id:\n{relationship.value_counts().sort_index()}") 
```

In this example, the summary of the relationship between the customer\_unique\_id and customer\_id columns includes the minimum, maximum, and mean number of unique customer\_id values per customer\_unique\_id. Additionally, the relationship.value\_counts().sort\_index() method returns a count of unique customer\_id values per customer\_unique\_id, sorted by the index (i.e., the number of unique customer\_id values).

This summary will give you a better understanding of the relationship between the two columns without having to manually check the entire relationship Series.

After we run the code suggested by our generative AI advisor, the results are indeed easier to digest:

```csv
Unique customer_id values: 99441
Unique customer_unique_id values: 96096

Summary of the relationship between customer_unique_id and customer_id:
Min: 1
Max: 17
Mean: 1.0348089410589412
Count of unique customer_id values per customer_unique_id:
1    93099
2    2745
3    203
4    30
5    8
6    6
7    3
9    1
17    1
Name: customer_id, dtype: int64 
```

It looks like customer\_id values uniquely identify records in the dataset rather than uniquely identifying customers. Therefore, customer\_unique\_id is more likely to serve as a customer identifier. In the actual business environment, our next step would be to check with the IT or other relevant departments whether over 93% of our clients really make only a single order in their lifetime, or whether this is indeed a data quality issue. For now, we’ll take the data at face value and continue our analysis.

The key takeaway here is that generative AI can help us choose suitable analytical methods. Still, it is up to us to ask the right questions and understand the meaning of the data in the context of our business domain.

# 2.4 Quality assessment structure

We should now know what information is encoded in the data at hand, and we should have an overview of its completeness.

We mentioned previously that you will need a structured approach to ensure sufficient data quality. In the introduction to this chapter, we also emphasized that even “successful” results from an analysis do not ensure the repeatability of this success. The following sections on data cleaning and exploratory data analysis present the main elements of such a quality assessment. This should give you a solid foundation upon which you can build a structure fit for your use case.

# 2.4.1 Data cleaning steps

You can compare data cleaning to preparing ingredients before cooking a meal. We strongly advise against dropping the contents of your fridge directly into a cooking pot. A good chef inspects ingredients to remove any spoiled parts, washes them to ensure cleanliness, and chops them to uniform sizes for even cooking. Similarly, data cleaning involves inspecting the dataset for inaccuracies or inconsistencies, removing or correcting these elements, and ensuring the data is in a uniform format. This preparatory step is essential to ensure that the final dish (or analytical result) is of high quality and free from elements that could compromise its taste (or integrity). We’ve emphasized multiple times that analyzing unclean data can lead to unreliable conclusions. The comparison with cooking serves this point. By cooking with unprepared ingredients, you can get something edible; we just wouldn’t advise this approach when you’re cooking to impress your date.

To ensure your data is technically clean, you should do the following:

1 Remove duplicates.   
2 Handle missing values.   
3 Correct data entry errors.   
4 Validate the data.

These steps should ensure that your tables contain data points describing business processes rather than artifacts from the data collection and preparation processes. The next phase should give you a better understanding of the data’s meaning.

# 2.4.2 Exploratory data analysis elements

By now, your data, or dish ingredients, are filtered and cleaned. Continuing with the cooking analogy, exploratory data analysis (EDA) can be compared to tasting and seasoning the ingredients. Is your tomato fresh and sun-ripened, or did it travel half the world in a freezer and is still so hard that you could play baseball with it? Does your variable have the normal distribution required by many algorithms, or is it skewed? Just as you would taste the dish at different stages, adjusting spices and ingredients to balance flavors and textures, EDA examines the dataset through various analytical and visualization techniques to understand its characteristics, trends, and outliers. This process allows you to adjust your analysis approach, like seasoning, to ensure the outcome is well-balanced and palatable. EDA is about getting a feel for the “flavor profile” of the data, identifying which ingredients (variables) play well together, anticipating how the final dish (analysis) might turn out, and making adjustments as needed for the best possible result.

The basic EDA structure you should employ for all data you lay your hands on could look like this:

1 Variables distribution testing —What are the characteristics of the data samples, such as mean, standard deviation, range, and so on?   
2 Variables visualization—What can you read from visual representations of the data?   
3 Data meaning clarification—Does the data represent what you think it does?   
4 Data mapping and harmonization—Are all the data points sampled using the same units, and do the headings use standardized description vocabulary?

Some people add extra steps to EDA, like correlation testing or text analysis. Others also add feature engineering. Depending on your data, their approach may be more suitable to your needs.

# One way from Sunday

We do not think a one-size-fits-all, silver-bullet, cure-all data preparation protocol exists. The general framework we believe will lead to high quality data is as follows:

Understand the relation of your data with reality (what each variable means and how it was generated).   
Ensure the data meets some basic technical standards (that you are working on all available relevant data points and can cross-relate them between data sources if needed).   
Before you analyze reality using your data, analyze the data itself (ensure it adheres to either expertise- or common-sense-based expectations).

In the following sections, we will walk through an example and ensure the data describes phenomena rooted in reality.

# 2.5 Data cleaning

Data cleaning must be done as early as possible, as errors resulting from poor data representation, consistency, or integrity are persistent and stack up quickly. Unclean data can misguide other data preparation and evaluation steps as well as your analytics results.

Let us repeat: We don’t believe there is one best way of cleaning data or performing EDA. In your work, you may encounter data cleaning protocols, including steps we describe as a part of EDA, and vice versa. You may be given a protocol that includes steps we consider analysis. If specialists in their field prepared these protocols, there is a chance they are better for the data types they are designed for. Be flexible. Just make sure you understand what’s happening.

ORDER MATTERS Some cleaning steps may obfuscate errors, especially in preparatory work. It is of great importance to understand how things change after each step. For example, if you fill missing data with average values from a certain column, you cannot do this before removing duplicates.

We’ll assume the worst-case scenario for this exercise. That’s the scenario where you’re unsure what to expect from your data.

# 2.5.1 Removing duplicates

There are many ways duplicate records can sneak into your data. From data entry mistakes (human errors) and system glitches (software errors) to poorly designed identifiers (human error), to synchronization problems in distributed systems (software error), to errors in merging datasets, to import issues . . . the list goes on. With so many things that can go wrong, some of them most likely will. In all honesty, we’re still waiting to see a duplicate-free dataset that was not previously curated for sharing.

How do you efficiently eliminate duplicate records to avoid overrepresenting certain data points, which could skew the analysis results? It depends on your analytical environment. Do you need to memorize details? Most certainly not!

![](images/7c4786826274cb4f6ec8c2db3f556e18af3ae4cccc6f49afaf322ebab34410de.jpg)

How can I remove duplicate entries from a DataFrame?

![](images/40925353c2037e42a25cc0e2c20ad46fed0a1b3b012c863abb065bfda44d19dd.jpg)

To remove duplicate entries from a DataFrame, you can use the drop\_duplicates() method. By default, it considers all columns when identifying duplicates and keeps the first occurrence of a duplicate row. Here’s an example:

```python
import pandas as pd

# Sample DataFrame with duplicate rows
data = {'A': [1, 2, 2, 4, 5, 1],
    'B': [6, 7, 7, 9, 10, 6]}

df = pd.DataFrame(data)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

print("Original DataFrame:")
print(df)

print("\nDataFrame without duplicates:")
print(df_no_duplicates) 
```

If you want to remove duplicates based on a specific set of columns, you can use the subset parameter:

```python
# Remove duplicates based on column 'A'
df_no_duplicates = df.drop_duplicates(subset=['A'])

print("\nDataFrame without duplicates based on column 'A':")
print(df_no_duplicates) 
```

In this example, df.drop\_duplicates(subset=['A']) removes duplicate rows based on the values in column A while keeping the first occurrence of each duplicate.

This answer is technically correct and, under regular circumstances, sufficient.

EFFICIENCY MAY NOT BE THE TOP PRIORITY, OR IT MAY Depending on your generative AI’s specifics, it may consider the answer’s simplicity rather than the resource-effectiveness of the solution. Quoting Grace Hopper, it’s a feature, not a bug. Chapter 5 describes methods for using even general-knowledge generative AIs to optimize code.

In our case, the answer is sufficient (as we didn’t have any duplicates in the first place), so we can triumphantly tick this box and move on to the next step.

# 2.5.2 Handling missing values

We will repeat the warning we issued earlier: some data is sparse. However, a list of the possible causes for missing data entries would be at least as long as the one for duplicates. Data entry errors, sensor malfunctions, copying errors, integration errors, you name it. Finally, there is the unavailability of information.

Depending on the context and the amount of missing data, you can choose to either delete the incomplete data entry or variable (the row or column in tabular formats), ignore it, or somehow fill in missing values. You could fill empty fields with a default value, an estimate (such as a mean, median, or mode), or use interpolation methods. It’s critical, however, to make these decisions consciously, depending on the meaning and importance of the data. Recently there was a case of a renowned macroeconomist filling missing data for some countries by copying them from adjacent cells. In that case, the dataset was sorted alphabetically by country names, which caused this method to make completely nonsensical adjustments.

It is paramount that the decision on what to do about missing values is based on understanding why the value is missing. Was it, for example, a sensor system error causing a missed measurement? Or was it an error in the system writing down the results? Was there an error when multiple data sources were connected together? To decide what to do with the missing values, you should first have a look at the data.

In our example data, we should notice three DataFrames where the number of non-null values differs from the number of rows in some columns (meaning it’s not just an empty column). These are df\_orders, df\_order\_reviews, and df\_products.

In the df\_orders DataFrame, we noticed that some approval and delivery dates are missing. We’ll use this DataFrame in section 2.6 to analyze the underlying process described by the data and the relation of the order status with the missing dates.

In the case of df\_products, we are missing some category names, the same number of product names, description lengths, and pictures, and some product size data. Let’s see if we can say anything by looking at the products where some of the values are missing.

There are 611 rows where some of the data is missing. This would be a chore to analyze and address manually, and if we were dealing with 6,111 or 61,111 rows, it would become unfeasible. What can we do to automate the process somewhat? Let’s start with investigating whether the number of missing values in different columns is coincidental or if there is some structure to it.

There is a lesson here about working with generative AI. If you have any doubts about your data but are unsure how to voice them precisely, don’t. We mean, don’t voice them precisely. Simply voice them as best you can.

![](images/d44ad6551b7bcc12d11a1183e9c9ec6632fe2ee243025fb5acad763856dd3fb9.jpg)

In my DataFrame, I have missing values. It looks like the number of missing values in some columns is correlated. How can I check if the missing values form a pattern?

![](images/6bea56f946a640e6c1f45db0b74b55479e18d62584a1445dea47a3ec57b89156.jpg)

You can check if the missing values form a pattern by analyzing the co-occurrence of missing values across different columns. To do this, you can use pandas to create a DataFrame indicating which values are missing and then compute the correlation between these binary indicators. Here’s an example:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame with missing values
data = {'A': [1, None, 3, 4, None],
    'B': [1, 2, None, 4, None],
    'C': [None, 2, 3, None, 5],
    'D': [1, 2, 3, 4, 5]}

vdf = pd.DataFrame(data)

# Create a DataFrame indicating which values are missing
missing_indicator = df.isna()

# Compute the correlation between the missing value indicators
missing_corr = missing_indicator.corr()

# Visualize the correlation matrix using a heatmap
sns.heatmap(missing_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation of Missing Value Indicators")
plt.show() 
```

In this example, df.isna() returns a DataFrame of the same shape as df, where each element is a boolean value indicating if the corresponding element in df is missing (True) or not (False).

missing\_indicator.corr() computes the pairwise correlation between the columns of the missing value indicators. The resulting correlation matrix represents the correlation between the missing values across different columns. High positive correlation values indicate that the missing values in the corresponding columns tend to co-occur.

Finally, the correlation matrix is visualized using a heatmap from the Seaborn library. This heatmap can help you quickly identify patterns in missing values, such as whether missing values in certain columns tend to coincide with missing values in other columns.

This time, we got some really heavy artillery, including visualization libraries. Skillful visualization is one of the most important skills in data analysis, and you shouldn’t be shy about leaning on your generative AI advisor to provide you with the tools you need.

A PICTURE IS WORTH A THOUSAND WORDS If you’d like to learn more about the importance of proper visualization for statistical analysis, we can’t recommend timeless books by Professor Edward Tufte enough. His Visual Explanations: Images and Quantities, Evidence and Narrative (Graphics Press, 1997) and The Visual Display of Quantitative Information (Graphics Press, 1997) are technology-agnostic bibles of excellent visual communication.

Figure 2.1 shows the results of one of the analyses proposed by generative AI. While there are many types of analysis that can be performed, most of the steps would be similar, so we’ll just use this one as an example.

![](images/3d93505d704cd9fbdc38a376df5bb294076459f72de1d43f7e685b77b649bdf5.jpg)

<details>
<summary>heatmap</summary>

Correlation of Missing Value Indicators
| product_id | product_category_name | product_name_lenght | product_description_lenght | product_photos_qty | product_weight_g | product_length_cm | product_height_cm | product_width_cm |
|---|---|---|---|---|---|---|---|---|
| product_id - | 1 | 1 | 1 | 0.028 | 0.028 | 0.028 | 0.028 | 0.028 |
| product_category_name - | 1 | 1 | 1 | 0.028 | 0.028 | 0.028 | 0.028 | 0.028 |
| product_name_lenght - | 1 | 1 | 1 | 0.028 | 0.028 | 0.028 | 0.028 | 0.028 |
| product_description_lenght - | 1 | 1 | 1 | 0.028 | 0.028 | 0.028 | 0.028 | 0.028 |
| product_photos_qty - | 1 | 1 | 1 | 0.028 | 0.028 | 0.028 | 0.028 | 0.028 |
| product_weight_g - | 0.028 | 0.028 | 0.028 | 0.028 | 1 | 1 | 1 | 1 |
| product_length_cm - | 0.028 | 0.028 | 0.028 | 0.028 | 1 | 1 | 1 | 1 |
| product_height_cm - | 0.028 | 0.028 | 0.028 | 0.028 | 1 | 1 | 1 | 1 |
| product_width_cm - | 0.028 | 0.028 | 0.028 | 0.028 | 1 | 1 | 1 | 1 |
</details>

Figure 2.1 The correlation between missing values in different columns

We can see that some products have missing values in all of the product\_category \_name, product\_name\_lenght, and product\_photos\_qty columns, or in all of the product\_weight\_g, product\_length\_cm, product\_height\_cm, and product\_width\_cm columns. This means that some products could either be weightless and dimensionless (services, perhaps?) or they don’t have any category, product name, or photos (a mystery box comes to mind).

NOTE The typo in the variable name product\_name\_lenght is preserved here to conform to the naming in the original dataset.

When we looked for rows in the dataset where every column except for the product\_id was empty, we found just one: product\_id 5eb564652db742ff8f28759cd8 d2652a. As we discussed earlier, before deciding whether to remove or keep such an item, we should check the business or data collection process behind such an oddity.

Fraud detection and forensic analysis are outside the scope of this book, but following our attempt to instill in you a bit of professional paranoia, we can’t completely ignore the fact that this case begs for an investigation. If we were to investigate such a case, we would first check the simplest explanation: someone was playing with the database and didn’t clean up after themselves. In such a case, this product\_id should be present only in this single table. The product\_id in question, however, seems to be connected to an order. If possible, we’d try to find the product’s website and see if it is a service (unlikely, as there is just one such case). If we felt especially inquisitive, we’d move to check this seller’s other transactions, particularly with the same buyer. In short, we would try to understand the actual event and the expected shape of the data describing it. From there, we would try to identify how the error could occur in the data (if it is, in fact, an error instead of a non-typical but a legitimate situation).

Unfortunately, we now need to take off our Sherlock Holmes caps and get back to dealing with a much more prevalent, if not so exciting, category of problem.

# 2.5.3 Correcting data entry errors

Is “Washington” the same thing as “Washington D.C.”? Or did an employee who was saving their precious time by typing just “SD” have in mind “Shipment Delayed” or “Standard Delivery”? You’ll encounter multiple data entry error types in your work, such as typos, mislabeling, or inconsistent formats, all of which negatively affect the dataset’s quality. You need to identify and correct these errors to ensure accurate and consistent data.

This is one of the most strenuous and least automatable parts of data preparation. Unfortunately, the best tool you can use to search for such errors is biological rather than digital. As of the time we’re writing this book, nothing beats a good oldfashioned eyeball. Some of the methods described in section 2.1 can help identify the oddities. For example, df['column\_name'].value\_counts() can help you spot values that occur only once, which may be suspicious if you expect uniform distribution. However, detecting and correcting data entry errors requires a combination of these techniques, along with domain knowledge and manual inspection.

The specific type of data entry error analysis we want to point out is outlier detection and treatment. Outliers are data points that deviate significantly from the rest of the dataset (for example, when almost all transactions in a set are from NY, and suddenly one is from LA). Identifying and handling outliers is very important, as they can disproportionately impact the analysis results. Alternatively, they can indicate data points of extreme importance. Outliers can be accepted, removed, capped, or transformed, depending on the context.

# 2.5.4 Data validation

You’d really rather not find entries like “last Tuesday, around noon” or “it was a beautiful spring morning” in the date column of your table. Validating the data ensures that the data adheres to specific rules or constraints, such as data types, value ranges, or relationships between columns. This is crucial for maintaining data integrity and avoiding inconsistencies that could lead to erroneous conclusions.

If this seems like a lot of work, that’s because it is. The good news is that this is yet another opportunity for you to get intimately familiar with analyzed data, and that’s something you can’t fake.

These are the four steps for validating your data:

1 Define expected values for your data.   
2 Check if any bits of data fall outside your expectations.   
3 If any do, do something about it.   
4 Check the consistency of the data coming from multiple tables.

The specifics of what values are expected will vary, depending on your dataset. There are no universal rules for determining expected versus unexpected values; that’s where your domain knowledge kicks in. You must remember, however, that data points deviating from expectations might signal either errors in data collection (worth investigating) or events of significant importance to your business (definitely worth investigating). To give you a starting point, we’ll outline three basic areas you should consider when validating your data.

# UPFRONT VALIDATION RULES AND CONSTRAINTS DEFINITION

We mentioned that the whole analytical protocol should be defined before running an analysis, to avoid having to “tweak” the analysis to fit expectations better.

Validation rules and constraints, indeed, must be defined upfront. If you scrolled through the files, as we advised you to do at the beginning of section 2.3, you should have a more or less solid intuition about the structure and distribution of variables in your data. You should also study your domain and related data enough to know what values are typical and expected. Suppose you don’t know the exact acceptable border values for your variables. In that case, you should be able to state your expectations in terms of deviations from the mean, percentiles, cicada chirps, horse’s lengths, or whatever applies to your data.

Now, let’s get off our high horse for a minute. Data quality assurance is an iterative process. We will perform an EDA, and we may learn that some of the assumptions we made after our initial analysis were not sufficiently grounded and that our intuition led us astray. In that case, we’ll go back and correct our validation rules to better discriminate between valuable data and potential artifacts.

# DATA TYPES

Assigning correct data types to your variables will make your life much easier down the line, as many libraries make operations on columns with well defined types (especially numerical ones) easy and efficient. In general, if you want to perform an operation like 111-11, you’d like to get 100, not 1 or a system error (where, as we will repeat throughout this book, the latter would be preferable).

When looking at the properties of our example DataFrames revealed by df\_name.dtype, or by calling the df\_name.info() method, you should notice that pandas successfully derived the types of numerical columns. However, it assigned general object types to columns containing dates.

Time representation in programming is far from straightforward. There are myriad methods and formats for noting something as seemingly simple as a timestamp, reflecting the complexity of time zones, calendar systems, and coding standards. In Python, there is no singular “date” type due to these complexities. Instead, for our datasets, we have found that the most suitable format is datetime64ns, which offers a precise timestamp down to the nanosecond:

```python
df_name['column_name'] = df_name.column_name.astype('datetime64[ns]') 
```

Analyzing methods for reading different time formats from text may be beyond the scope of this book, but it’s surely not beyond the scope of knowledge of your GenAI advisor! When in doubt, provide an example of your data, and ask the generative AI how to transform it into the format you’ll be using in your pipeline.

# RELATIONSHIPS BETWEEN COLUMNS

We mentioned that we’d seen sales volumes added to physical volumes. How do you think that happened? This point is critical if you work with multiple DataFrames from different data sources. Blind trust that identical column names mean that the two columns describe the same thing may very easily deprive your analysis of any functional value.

Before you start coding (or copying) a cross-reference function, you should have a good understanding of which of your DataFrames will serve as the reference—the source of so-called primary keys—and which DataFrames will have foreign keys— meaning the values reference existing primary keys. This way, you’ll create a lineage of DataFrames.

If you have a DataFrame containing the data on all your customers, their identifiers become primary keys. Suppose you have another DataFrame describing orders from some range of time, and it has information on which customer made an order; all these customers’ identifiers will exist in the DataFrame of customers. However, there is a possibility that some of the customers in the reference dataset didn’t order anything in the timeframe in question, so they don’t need to all be in the orders DataFrame.

You can use the following code to identify problems with keys within df\_orders and df\_order\_payments.

# Listing 2.2 Identifying foreign key violations

```python
foreign_key_violations =
df_orders[~df_orders['order_id'].isin(df_order Intentions['order_id'])]
if not foreign_key_violations.empty:
    print("Foreign key violations found:") 
```

```python
print(foreign_key_violations)
# Handle violations (e.g., drop rows or correct the foreign key values) 
```

In the course of our work with this example dataset, we’ve already discovered that there is a problem with customer\_id, so the relation between df\_orders and df\_ customers here is unexpectedly 1:1, but when checking df\_orders against df\_order\_payments, we can see the expected behavior of order\_id being a primary key in df\_orders and a foreign key in df\_order\_payments. There is one violation, but we’ll leave dealing with it as an exercise for you.

Yet again, there is an issue of causality, which you should identify as an analyst. By that, we mean identifying the actual cause of an unexpected data structure. Any explanation you can come up with should be confirmed with the data creators. Of course, sometimes, your ability to confirm things may be limited, and you may need to rely on cross-referencing all the DataFrames and checking if there is a logical pattern in identifier columns. Still, in cases where you work without 100% certainty on the data’s meaning, you should clearly communicate to your stakeholders the risk of analysis being performed on an unconfirmed dataset.

We now should have our data adequately cleaned. By performing a thorough data cleaning, you increase the likelihood of obtaining reliable and accurate insights from your data analysis. A clean dataset serves as a strong foundation for the subsequent stages of data preprocessing, EDA, and modeling.

The dataset we use in this book is provided in a modeling-ready state, and as such does not require additional cleaning or preprocessing, so we will move directly to EDA. In your work, you shouldn’t be so hasty!

# 2.6 Exploratory data analysis

Now that the data has been sliced and diced, it’s time for some seasoning, mainly of you as a data analyst. In most cases, your stakeholders will require simple analyses, and they’ll have strong opinions about the visualizations they want. You’ll be surprised how often they refuse bleeding-edge interactive, flashy, blinking, and sparkling tools and demand good old static charts. And there is nothing wrong with that. Your role is to make sure their decisions are informed. If their preferred way of acquiring the required information is through one type of chart or another, you should respect that in most cases. You’ll need to stomp down your foot, however, when you realize that some other data presentation introduces new and required information. Pick your battles.

Why do we talk about visualization types here? Because you will get many useful charts as a side-effect of your EDA. Doing them right at this stage (which means they’re useful to your stakeholders) can save you time and effort later. In this section you will find some examples of such useful charts.

In our opinion, EDA is the process that distinguishes great analysts. It’s a form of art, linking the meaning of data with its structure. In EDA, you will combine statistics, domain knowledge, and visualizations. (You may use your new visualization toys, but if you want your stakeholders to adopt them, make sure you sometimes show them what you use—luring them generally works better than forcing things down their throats.)

This mix of required knowledge may seem intimidating, but you now have access to a fantastic source of multidisciplinary know-how. Let’s ask generative AI about the DataFrame containing order reviews, aptly named df\_order\_reviews, as it has an interesting combination of numbers, text, and dates.

![](images/9793195734066939a5d2b31a9077864f4d999e00835b33fde10386559425e182.jpg)

# Please suggest EDA techniques for the following DataFrame:

DataFrame name: df\_order\_reviews

Columns:

- review\_id (object):   
➥Unique identifier of each review.   
- order\_id (object):   
➥Identifier of the order being reviewed.   
- review\_score (int64):   
➥Note ranging from 1 to 5 given by the customer on a satisfaction survey.   
- review\_comment\_title (object):   
➥Comment title from the review left by the customer in Portuguese.   
- review\_comment\_message (object):   
➥Comment message from the review left by the customer in Portuguese.   
- review\_creation\_date (datetime64[ns]):   
➥The timestamp of the review creation.   
- review\_answer\_timestamp (datetime64[ns]):   
➥I am not sure what this one actually is.

![](images/228d90c26d16b310f447f5d7895d371c0af4ac3bf185b6ace99f232e887f6dd9.jpg)

Based on the provided DataFrame structure and content, here are some EDA techniques to better understand and analyze your df\_order\_reviews DataFrame:

1 Basic data overview: Use .head(), .tail(), .info(), and .describe() to get an initial understanding of the DataFrame content and structure.   
2 Missing values analysis: Check for missing values in each column using .isna().sum() and decide how to handle them (drop, fill, or impute).   
3 Review scores distribution: Use .value\_counts() or a histogram to visualize the distribution of review scores.   
df\_order\_reviews['review\_score'].value\_counts().sort\_index()   
➥.plot(kind='bar')  
4 Reviews over time: Plot the number of reviews created over time using the review\_creation\_date column. This can help you identify trends and patterns in the review data.   
df\_order\_reviews['review\_creation\_date'].dt.to\_period('M').   
value\_counts().sort\_index().plot(kind='bar')  
5 Review response time: Calculate the response time for each review by subtracting the review\_creation\_date from the review\_answer\_timestamp. Analyze the distribution of response times and investigate if there is a relationship between response time and review scores.

df\_order\_reviews['response\_time'] =

➥df\_order\_reviews['review\_answer\_timestamp'] -

➥df\_order\_reviews['review\_creation\_date']

6 Text analysis: Explore the text data in the review\_comment\_title and review\_comment\_message columns. You can perform sentiment analysis, topic modeling, or word frequency analysis to identify common themes, patterns, or issues mentioned in the reviews.   
7 Investigate the unclear column: To understand the review\_answer\_timestamp column, you can analyze its relationship with other columns, like review\_creation\_date or review\_score. Plotting scatter plots, calculating correlations, or performing other statistical tests can help you identify the purpose of this column.   
8 Orders with multiple reviews: Check if there are any orders with multiple reviews. This could indicate data entry errors or provide insight into the review process.

```python
order_review_counts = df_order_reviews['order_id'].value_counts()
multiple_review_orders = order_review_counts[order_review_counts > 1] 
```

These EDA techniques can help you gain a better understanding of the df\_order\_reviews DataFrame and identify patterns, trends, and potential issues in the data. Depending on your specific objectives and domain knowledge, you may need to adapt or extend these techniques to suit your needs.

The preceding answer comes from ChatGPT-v4, as it was the most comprehensive. It developed one solid EDA plan, touching upon multiple topics at once. It shows how different levels of analysis overlap with each other. You shouldn’t be surprised to see some of the steps we performed in the data-cleaning phase included here. Other steps, in our opinion, are elements of the data analysis itself. As we mentioned, there is no gold standard for EDA, and generative AI often provides the broadest possible answer.

# 2.6.1 Reviewing score distribution

Let’s get back to our coin-flip gambling problem for a second. If you recall, at the beginning of this chapter, we said, “. . . if you throw the coin multiple times and get your expected tails each time, the coin may not be random after all.” Before betting on a coin, you most definitely should check what the distribution of results is. If it’s really random, you most likely should not bet on it at all, but if it’s not random, you can use it to your advantage. You can think about reviewing the score distribution as you would about testing multidimensional coins.

The importance of score distribution cannot be overemphasized, as distribution analysis can reveal potential issues that may impact the study’s validity, such as data entry errors or biases. Visualizing the distribution through histograms, box plots, or density plots can also help to determine whether the data follows a specific pattern or conforms to a known statistical distribution. This knowledge can help you select appropriate statistical tests, predictive models, or data transformation techniques to ensure accurate and reliable results.

Reviewing the distribution typically involves comparing the observed data distribution with a theoretical distribution (for example, normal, exponential, or binomial) to assess how well the data conforms to expected patterns. You have multiple distribution testing methods at your disposal, including visual inspection with histograms or Q-Q plots, or more quantitative measures like the Kolmogorov-Smirnov test, the Shapiro-Wilk test for normality, or the Anderson-Darling test. Each method has its strengths and particularities, making it more or less suitable depending on the size of the dataset and the assumptions you’re willing to make.

If this task seems complex, that’s because it used to be. Now it’s as simple as typing:

MA How can I test what distribution does my dataset fit best?

If you’re looking for a more specific answer, you can add details about your analytical environment, data source, or an intuition you want to examine (note that we didn’t use the word “confirm”). From our experience, ChatGPT-4 beats all the other tools in its statistical prowess.

Let’s look at some popular distributions and where you may expect them. The shapes of commonly encountered distributions are presented in figure 2.2.

# NORMAL DISTRIBUTION

The normal distribution is also known as Gaussian distribution or “bell curve.” It’s often the first assumption for continuous data, due to the central limit theorem, which posits that the mean of a sufficiently large number of independent random variables, each with finite mean and variance, will be approximately normally distributed, regardless of the underlying distribution. Be careful, though. Some statistical tests rely heavily on the assumption of the normality of the data distribution. If your data is skewed, your test results may get screwed as a result.

The normal distribution is particularly relevant for metrics like sales figures, heights of individuals, and errors in measurements.

# BINOMIAL DISTRIBUTION

The binomial distribution is used for binary outcomes in data, like coin flipping. This distribution is relevant when dealing with success/failure, yes/no, or 1/0 types of outcomes in data, such as conversion rates in A/B testing, pass/fail rates in quality control, or click-through rates in online advertising.

Seeing more than two bars in a binomial distribution chart often leads to confusion, so let’s try to dispel that right away. The binomial distribution describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. When you see a binomial distribution with more than two bins, it does not represent just a single trial (which would result in only two outcomes: success or failure, 1 or 0). Instead, it represents the outcomes of multiple trials, so it can have more than two bins.

For example, suppose you analyze the binomial distribution of n=10 different trials. In that case, the distribution doesn’t show just two outcomes but the probability of achieving 0, 1, 2, ..., up to 10 successes out of those 10 trials. Each “bar” in this context represents the number of successes: one bar for 0 successes, another for 1 success, and so on, up to 10 successes. So while each individual trial has a binary outcome, the

![](images/642c634dd427a3c1d6941cb87eee36c057d99fd7698628382036dbd590fbf0b7.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count | Density |
| --------- | ----- | ------- |
| -4 to -3  | 0     | 0.00    |
| -3 to -2  | 10    | 0.05    |
| -2 to -1  | 30    | 0.15    |
| -1 to 0   | 80    | 0.30    |
| 0 to 1    | 110   | 0.40    |
| 1 to 2    | 70    | 0.25    |
| 2 to 3    | 20    | 0.10    |
| 3 to 4    | 5     | 0.02    |
</details>

![](images/5d3d45a667ad10be0ec4e53e2a24d575a5d52fb659954a6ab568e924eb8c2f35.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count | Density |
| --------- | ----- | ------- |
| 0-1       | 0     | 0.00    |
| 1-2       | 10    | 0.01    |
| 2-3       | 40    | 0.05    |
| 3-4       | 130   | 0.15    |
| 4-5       | 200   | 0.20    |
| 5-6       | 250   | 0.25    |
| 6-7       | 220   | 0.20    |
| 7-8       | 120   | 0.10    |
| 8-9       | 30    | 0.05    |
| 9-10      | 10    | 0.01    |
</details>

![](images/39400cd36c30f2939d2f840c10d03d93ef1ed0774296030c79af336662740dbf.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count |
| --------- | ----- |
| -0.2 to 0.0 | 95 |
| 0.0 to 0.2 | 88 |
| 0.2 to 0.4 | 92 |
| 0.4 to 0.6 | 105 |
| 0.6 to 0.8 | 72 |
| 0.8 to 1.0 | 95 |
| 1.0 to 1.2 | 95 |
</details>

![](images/39c6a4f15408cfd340e14678c709757cc58d1e508ae22e3f1dd6ca9b102c5c9a.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count | Density |
| --------- | ----- | ------- |
| 0 - 1     | 50    | 0.05    |
| 1 - 2     | 160   | 0.15    |
| 2 - 3     | 210   | 0.20    |
| 3 - 4     | 180   | 0.18    |
| 4 - 5     | 110   | 0.12    |
| 5 - 6     | 50    | 0.05    |
| 6 - 7     | 15    | 0.02    |
| 7 - 8     | 5     | 0.01    |
| 8 - 9     | 2     | 0.005   |
| 9 - 10    | 1     | 0.002   |
</details>

![](images/4b85a759caac12c3817a9900af1099e9f461c41ec7476c15efd8dd4883300caa.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count |
| --------- | ----- |
| 0 - 0.5   | 200   |
| 0.5 - 1.0 | 160   |
| 1.0 - 1.5 | 130   |
| 1.5 - 2.0 | 90    |
| 2.0 - 2.5 | 60    |
| 2.5 - 3.0 | 40    |
| 3.0 - 3.5 | 25    |
| 3.5 - 4.0 | 15    |
| 4.0 - 4.5 | 10    |
| 4.5 - 5.0 | 5     |
| 5.0 - 5.5 | 2     |
| 5.5 - 6.0 | 1     |
</details>

![](images/ccc9f0d2652bcccae0797bae93f88ace8cea9c64b1008dab020042d9f145599e.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count | Density |
| --------- | ----- | ------- |
| 0 - 2     | 180   | 0.35    |
| 2 - 4     | 120   | 0.25    |
| 4 - 6     | 60    | 0.15    |
| 6 - 8     | 30    | 0.05    |
| 8 - 10    | 10    | 0.02    |
| 10 - 12   | 5     | 0.01    |
| 12 - 14   | 2     | 0.005   |
| 14 - 16   | 1     | 0.002   |
| 16 - 18   | 0     | 0.001   |
| 18 - 20   | 0     | 0.0005  |
| 20 - 22   | 0     | 0.0002  |
| 22 - 24   | 0     | 0.0001  |
| 24 - 26   | 0     | 0.00005 |
| 26 - 28   | 0     | 0.00002 |
| 28 - 30   | 0     | 0.00001 |
| 30 - 32   | 0     | 0.000005|
| 32 - 34   | 0     | 0.000002|
| 34 - 36   | 0     | 0.000001|
| 36 - 38   | 0     | 0.0000005|
| 38 - 40   | 0     | 0.0000002|
| 40 - 42   | 0     | 0.0000001|
| 42 - 44   | 0     | 0.00000005|
| 44 - 46   | 0     | 0.00000002|
| 46 - 48   | 0     | 0.00000001|
| 48 - 50   | 0     | 0.000000005|
| 50 - 52   | 0     | 0.000000002|
| 52 - 54   | 0     | 0.000000001|
| 54 - 56   | 0     | 0.0000000005|
| 56 - 58   | 0     | 0.0000000002|
| 58 - 60   | 0     | 0.0000000001|
</details>

![](images/5157a2ce8757bbf31474647f614abac5a351201b1224b9ae1ddc421779b6c39c.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Count |
| --------- | ----- |
| 0.0 - 0.1 | 38    |
| 0.1 - 0.2 | 72    |
| 0.2 - 0.3 | 114   |
| 0.3 - 0.4 | 78    |
| 0.4 - 0.5 | 52    |
| 0.5 - 0.6 | 36    |
| 0.6 - 0.7 | 20    |
| 0.7 - 0.8 | 10    |
| 0.8 - 0.9 | 5     |
| 0.9 - 1.0 | 2     |
</details>

![](images/18da62354f36fdb1eeb7a56e318a0bb504b0810946be583f3f992ae803ce1575.jpg)

<details>
<summary>histogram</summary>

| Gamma Range | Count | Density |
|-------------|-------|---------|
| 0 - 1       | 45    | 0.095   |
| 1 - 2       | 95    | 0.135   |
| 2 - 3       | 125   | 0.175   |
| 3 - 4       | 105   | 0.150   |
| 4 - 5       | 70    | 0.100   |
| 5 - 6       | 55    | 0.075   |
| 6 - 7       | 30    | 0.050   |
| 7 - 8       | 20    | 0.035   |
| 8 - 9       | 10    | 0.025   |
| 9 - 10      | 5     | 0.015   |
| 10 - 11     | 3     | 0.010   |
| 11 - 12     | 2     | 0.005   |
| 12 - 13     | 1     | 0.003   |
| 13 - 14     | 1     | 0.002   |
| 14 - 15     | 0     | 0.001   |
| 15 - 16     | 0     | 0.001   |
| 16 - 17     | 0     | 0.001   |
| 17 - 18     | 0     | 0.001   |
| 18 - 19     | 0     | 0.001   |
| 19 - 20     | 0     | 0.001   |
</details>

Figure 2.2 Commonly encountered data distributions

aggregate result across multiple trials can range from 0 successes (all failures) to n successes (all successes), leading to n+1 possible outcomes. Hence the number of bars in the distribution’s representation.

# UNIFORM DISTRIBUTION

A uniform distribution assumes that all outcomes are equally likely. It’s frequently a starting assumption for simulations or when modeling unbiased random variables, such as random digits, the simulation of equal-probability scenarios, or when no prior information is available.

While this distribution is less common in raw business data, it’s worth remembering.

# POISSON DISTRIBUTION

The Poisson distribution applies to count data where occurrences happen independently over a constant rate in space or time. It’s commonly used for modeling the number of times an event occurs in a fixed interval of time or space.

You may encounter this distribution when analyzing the number of customer arrivals per hour, daily demand for a product, or the number of failures of a system.

# EXPONENTIAL DISTRIBUTION

An exponential distribution is often used to model the time between events in a Poisson process, representing the time until an event occurs.

Look for this distribution when working with the lifespan of machinery before failure, the time until a customer’s next purchase, or the inter-arrival times in a queuing system.

# LOG-NORMAL DISTRIBUTION

The log-normal distribution comes into play when dealing with variables that are the product of many independent random variables. It’s used when data cannot be negative and the distribution is skewed right.

You’ll encounter this distribution in datasets concerning stock or real estate property prices or income distributions.

# BETA DISTRIBUTION

The beta distribution is useful in modeling variables that are bounded on both sides, such as proportions and percentages. It’s flexible and can assume a variety of shapes, making it suitable for modeling the behavior of random variables limited to intervals.

This distribution appears when the data represents conversion rates with values between 0 and 1.

# GAMMA DISTRIBUTION

The gamma distribution is related to the exponential distribution and is useful for modeling the wait time for the n-th event in a Poisson process.

You’ll need the gamma distribution when modeling things such as the amount of rainfall accumulated in a reservoir, service times in systems, or the reliability of systems over a continuous scale.

NOTE Can multimodal generative AI be used to identify distribution type from a chart? At the time of writing this book, no. We tried to feed parts of figure 2.2 to different generative AIs, and their answers were often as diverse as misleading. However, generative AIs can still guide you through proper testing procedures.

# 2.6.2 Time series exploration

Now we enter a grey zone. You may encounter discussions on analyzing changes over time as a part of EDA or as a part of in-depth analysis itself. On the one hand, visualizing all the time series is a part of EDA. Sometimes this will allow you to identify outliers or errors requiring cleanup. On the other hand, these outliers could encode significant issues or events in business processes.

We conclude that distinguishing between EDA and in-depth business analysis is a false dichotomy. EDA is an integral part of in-depth analysis. It’s not something you want someone else to do for you. Nor is EDA a once-off event—you will be coming back to it now and then.

From the process management perspective, it’s clearer when steps related to evaluating the data’s technical and structural properties are separate from those related to discovering business-related insights. However, the two are too closely related to be wholly compartmentalized.

There are two tests that we propose to run at the first EDA iteration. First, we’ll visualize and look at the data to search for outliers; second, we’ll perform cyclicity detection.

# CHANGES IN THE NUMBER OF RESPONSES: QUICK DATA VISUALIZATION

We’ve seen situations where the success attributed to a project was, in fact, caused by the change in the overall market or the performance of another business function. Taking a good look at how different variables change over time can be very informative indeed!

This is a very basic yet important task, which should be performed on most of your date-related variables. Most business activities have a continuous character, and analyzing their performance over time is critical for understanding those activities.

Figure 2.3 presents the number of reviews recorded in our dataset per month. We can clearly see three distinct phases. The first one lasted from October 2016 to January 2017. The almost non-existent number of reviews suggests that either the business operations or review collecting system were just getting traction. Then, from February 2017 to November 2017 (or May 2018, really), we can see a phase of rapid growth in the number of reviews collected monthly. Then, from December 2017 the system stabilized and started fluctuating, or from June 2018 it had a moment of collapse and rebounded in August 2018.

![](images/75e39c9d3439bc5419d2072fe5a1bb1ac472a7dfa5ab5c1c8f55e152c81dab16.jpg)

<details>
<summary>bar</summary>

| Date | Value |
|---|---|
| 2016-10 | 150 |
| 2016-11 | 70 |
| 2016-12 | 30 |
| 2017-01 | 250 |
| 2017-02 | 1400 |
| 2017-03 | 2500 |
| 2017-04 | 2050 |
| 2017-05 | 3700 |
| 2017-06 | 3450 |
| 2017-07 | 3500 |
| 2017-08 | 4550 |
| 2017-09 | 4200 |
| 2017-10 | 4450 |
| 2017-11 | 4800 |
| 2017-12 | 8000 |
| 2018-01 | 6200 |
| 2018-02 | 6150 |
| 2018-03 | 7850 |
| 2018-04 | 7350 |
| 2018-05 | 7500 |
| 2018-06 | 6750 |
| 2018-07 | 5650 |
| 2018-08 | 9150 |
</details>

Figure 2.3 The number of reviews over time—monthly aggregation

This information could be crucial if we were to quantitatively compare metrics involving the number of reviews between different points in time. Now that we’ve checked the number of reviews, let’s move on to checking the scores associated with reviews.

# CHANGES IN REVIEW SCORES OVER TIME

Some data is expected to be cyclic, and other data, not so much. Discovering and describing cycles in data can help you identify whether the dataset you’ve provided is relevant to explaining the related business processes.

The following recording of our conversation with the AI advisor proves our point from chapter 1, related to the limitations of embedding generative AI directly into your analytics pipeline in a shoot-and-forget manner.

![](images/14d3977d6ae847321bdfd2ae51fe265ea454e0ae4a272ef7453907ae38db376d.jpg)

How can I detect internal cyclicity in data?

![](images/dad36ee7ebc784ea8b8adc65e89264d84f9bc4ad45d2f9a5e4130fbd0778e2ef.jpg)

Detecting internal cyclicity in data involves identifying recurring patterns or periodic fluctuations over time. Time series data is a common example where cyclicity might be present. Here are some techniques to detect cyclicity in your data:

1 Visual inspection: Plot the data over time to visually inspect if there’s any noticeable cyclical pattern. This can be a quick and simple way to identify obvious patterns.

```python
import matplotlib.pyplot as plt
plt.plot(df['timestamp'], df['value'])
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Data')
plt.show() 
```

2 Seasonal decomposition: Decompose the time series data into its trend, seasonal, and residual components using methods like classical decomposition or Seasonal and Trend decomposition using Loess (STL). This can help you observe the seasonal component directly.

```txt
<Dysfunctional code was here> 
```

3 Autocorrelation and partial autocorrelation: Plot the autocorrelation function (ACF) and partial autocorrelation function (PACF) to identify any significant lags that indicate cyclical patterns.

```txt
<Dysfunctional code was here> 
```

4 Spectral analysis: Perform a spectral analysis using the Fast Fourier Transform (FFT) or Lomb-Scargle Periodogram to identify dominant frequencies in the data, which can correspond to cyclic patterns.

```txt
<Dysfunctional code was here> 
```

These techniques can help you detect internal cyclicity in your data. Depending on the characteristics of your data and the nature of the cyclicity, some methods may be more appropriate than others. It’s essential to understand the underlying assumptions and limitations of each technique and to choose the one that best fits your specific data and objectives.

The code provided by generative AI sometimes differs from expectations. Three of the four pieces of code we received are dysfunctional (and are therefore censored), and the other . . . Well, look at figure 2.4 to see the resulting visualization of the relationship between the score and the time of the review.

We believe that some people gifted with an affinity for postmodern art could find an application for the resulting chart. In business analytics, however, you aim to get something a tad more readable.

Let’s get back to the dysfunctional code, as there is a lesson to be learned here. The FFT and Lomb-Scargle methods didn’t work due to problems with data types. So far, we’ve advocated that you present your generative AI advisor with general queries to confirm your expertise or expand your horizons. However, sometimes you’ll encounter problems resulting from false assumptions that generative AI may make related to the data types available for analysis. That doesn’t mean the answer is useless. It means you’ll have to change gears.

![](images/934eb15cc81fefee711788cd85bc4e48f697605a30788211757949f535df5112.jpg)

<details>
<summary>line</summary>

| Timestamp   | Value |
| ----------- | ----- |
| 2016-10     | 1.0   |
| 2017-01     | 4.0   |
| 2017-04     | 3.0   |
| 2017-07     | 3.5   |
| 2018-01     | 2.5   |
| 2018-04     | 2.0   |
| 2018-07     | 1.5   |
| 2018-10     | 1.0   |
</details>

Figure 2.4 The relationship between the score and the time of the review

VARIABLES WON’T, CONSTANTS AREN’T Generative AIs are language models. They operate on a general set of knowledge of mind-boggling scope. Expecting them to correctly assume the alignment of data type requirements for some advanced methods with our specific data may be overly optimistic.

As the general inquiry failed, let’s try to be more specific.

![](images/1b77e0eebf71342e55e80e7649637f052e53477ea40e3ffe2d526c10fe1d036c.jpg)

Values in my data are categorical, with possible values of 1, 2, 3, 4, 5. They are review scores given to orders by customers. Can you propose a method to detect if there are any cyclical dependencies of the score in time?

![](images/c977ca15e7dedbf954939199fbba00cb3e6329bead703845386d8fff9ba945b9.jpg)

Since your data consists of categorical values (review scores), you can analyze cyclical dependencies by examining the distribution of scores over different time periods. One approach is to use aggregated bar plots to visualize the score distribution over time.

Here’s a step-by-step guide to analyze cyclical dependencies:

1 Convert the timestamp to a more suitable frequency (e.g., daily, weekly, or monthly), depending on the length and resolution of your data.

```python
# Create a new column with the timestamp at the desired frequency
→(e.g., daily)
df_order_reviews['date_daily'] =
→df_order_reviews['review_creation_date'].dt.date 
```

2 Aggregate the scores and calculate the proportions for each score in each time period.

```python
# Group by date_daily and calculate the proportion of each score
score_counts = df_order_reviews.groupby(['date_daily',
    'review_score']).size().unstack(fill_value=0)
score_proportions = score_counts.div(score_counts.sum(axis=1), axis=0) 
```

3 Create a stacked bar plot to visualize the proportions of scores over time.

```python
score_proportions.plot(kind='bar', stacked=True, figsize=(15, 6))
plt.xlabel('Date')
plt.ylabel('Proportion of Scores')
plt.title('Proportion of Review Scores Over Time')
plt.legend(title='Review Score', bbox_to_anchor=(1, 1))
plt.show() 
```

Examine the stacked bar plot for any apparent cyclical patterns. If you observe any regular fluctuations in the proportions of different scores, there might be a cyclical dependency in the data.

Please note that the choice of aggregation frequency (daily, weekly, or monthly) will impact the granularity of the analysis. You might need to experiment with different frequencies to find the most suitable one for your data.

As we used web-based generative AI, it even remembered the name of our DataFrame in the conversation context, so no code adjustment in this regard is needed. It’s equally as awesome as it may be dangerous. All of its assumptions should be taken with a pinch of salt and noted down, as they often may turn out to be a reason why some of the steps don’t work as expected.

Figure 2.5 presents the result of the proposed code. As you can see, the initially proposed frequency does not work well with our data. However, there is no obvious way of changing it. Does that mean we need to change the tools—revert to Excel and pivot tables or find something with a nice, big “change frequency” button? Or should we spend another week searching the matplotlib documentation?

![](images/3f6d83c1f5fdb7e444c3df8d7d0783a411727bcc740c8d5eb351b2bbc3b46ae1.jpg)

<details>
<summary>bar</summary>

| Date       |   Review Score 1 |   Review Score 2 |   Review Score 3 |   Review Score 4 |   Review Score 5 |
|:-----------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| 2022-01-01 |         0.176405 |          0.329248 |          0.205836 |          0.11836  |           0.655619 |
| 2022-01-02 |         0.345469 |          0.678738 |          0.399294 |          0.419195 |           0.791725 |
| 2022-01-03 |         0.595283 |          0.437429 |          0.546968 |          0.386756 |           0.539249 |
| ...        |       nan        |        nan        |        nan       |        nan       |          nan       |
| 2022-01-30 |         0.767435 |          0.592149 |          0.467563 |          0.313878 |           0.678738 |
| 2022-01-31 |         0.978738 |          0.467563 |          0.345469 |          0.539249 |           0.419195 |
| 2022-02-01 |         0.998874 |          0.386756 |          0.286756 |          0.467563 |           0.313878 |
| 2022-02-02 |         0.998874 |          0.313878 |          0.214329 |          0.345469 |           0.234569 |
| ...        |       nan        |        nan        |        nan       |        nan       |          nan       |
| 2022-03-31 |         0.998874 |          0.234569 |          0.143878 |          0.267563 |           0.165619 |
| Note: The data is randomly generated for all dates |       nan        |        nan        |        nan       |        nan       |          nan       |
</details>

Figure 2.5 Order scores distribution over time—daily aggregation

Maybe not. This is the brilliance of generative AI in action. You encounter a problem, you mention it to your AI advisor, and . . .

![](images/68df8c6b110ffdacd0e5ebb1c46156ed2944cdfd3ed9a7c995f609db5d055bd5.jpg)

How would I change the frequency to monthly?

![](images/f64ddb326f8edc46f76a880d7a549ac023541d2ce0af1b76c65282cab6ab910d.jpg)

To change the frequency to monthly, you’ll need to resample your data accordingly. Here’s how you can modify the code to aggregate the data on a monthly basis:

1 Convert the timestamp to a more suitable frequency (e.g., monthly).

```python
# Create a new column with the timestamp at the desired frequency
→(e.g., monthly)
df_order_reviews['month'] =
→df_order_reviews['review_creation_date'].dt.to_period('M') 
```

2 Aggregate the scores and calculate the proportions for each score in each time period.

```python
# Group by month and calculate the proportion of each score
score_counts = df_order_reviews.groupby(['month', 'review_score']).size().unstack(fill_value=0)
score_proportions = score_counts.div(score_counts.sum(axis=1), axis=0) 
```

3 Create a stacked bar plot to visualize the proportions of scores over time.

```python
score_proportions.plot(kind='bar', stacked=True, figsize=(15, 6))
plt.xlabel('Month')
plt.ylabel('Proportion of Scores')
plt.title('Proportion of Review Scores Over Time (Monthly)')
plt.legend(title='Review Score', bbox_to_anchor=(1, 1))
plt.show() 
```

Now, the analysis will be performed at a monthly level, which can help reveal longterm cyclical patterns in the data. Feel free to adjust the frequency according to your requirements and the granularity of your data.

. . . there is a high chance that generative AI is capable of solving it. Figure 2.6 presents the distribution of review scores over time, aggregated by month.

We can see that there was a spike in low scores in November and December 2016, and maybe, just maybe, there is a cyclic rise in low scores in the spring, but the signal is so weak that we won’t dig much deeper into it unless we want to run some precise predictive analysis.

We can safely conclude from this section that generative AIs may make mistakes, but they can still help you write and modify code, such as for time series analysis, and they are not shy of using really advanced libraries and algorithms (Lomb-Scargle is an algorithm developed by biologists to analyze biological cycles, later adopted by astronomers to search for patterns in star brightness observations). We believe that with a little patience and an iterative approach to clarifying the method requirements and your data properties, generative AI will become the greatest facilitator of your analytical processes.

![](images/e90a0812590928562beb23355b04094262956f8d7900df476de24abcb83edbd7.jpg)

<details>
<summary>bar_stacked</summary>

| Month    |   Score 1 |   Score 2 |   Score 3 |   Score 4 |   Score 5 |
|:---------|----------:|----------:|----------:|----------:|----------:|
| 2016-10  |      0.15 |      0.05 |      0.07 |      0.18 |      0.42 |
| 2016-11  |      0.35 |      0.08 |      0.09 |      0.12 |      0.38 |
| 2016-12  |      0.65 |      0.03 |      0.04 |      0.06 |      0.25 |
| 2017-01  |      0.07 |      0.06 |      0.11 |      0.15 |      0.45 |
| 2017-02  |      0.06 |      0.05 |      0.12 |      0.21 |      0.43 |
| 2017-03  |      0.14 |      0.09 |      0.13 |      0.19 |      0.41 |
| 2017-04  |      0.13 |      0.11 |      0.14 |      0.23 |      0.39 |
| 2017-05  |      0.12 |      0.12 |      0.15 |      0.24 |      0.38 |
| 2017-06  |      0.11 |      0.13 |      0.16 |      0.25 |      0.37 |
| 2017-07  |      0.1 |      0.14 |      0.17 |      0.26 |      0.36 |
| 2017-08  |      0.1 |      0.15 |      0.18 |      0.27 |      0.35 |
| 2017-09  |      0.12 |      0.16 |      0.19 |      0.28 |      0.34 |
| 2017-10  |      0.12 |      0.17 |      0.2 |      nan   |    nan    |
</details>

Figure 2.6 Order scores distribution over time—monthly aggregation

# 2.6.3 Mysterious variable investigation

If mysterious variables don’t already plague your days as a data analyst, you can expect they will. We mentioned, and will again, that nothing beats solid metadata, but things like thorough documentation data pipelines are considered a luxury in these times of ever-increasing time pressure. Therefore, some of your data may come from a poorly documented system. As much as we discourage using unconfirmed data for any reason other than warming your server room, sometimes it is possible to deduce the meaning of some variables to a satisfying level of certainty.

To show how you can deal with an example of a mysterious variable, let’s feign ignorance as to the meaning of one of the columns in our example data. Let’s try to get some insight into the review\_answer\_timestamp column. With our Sherlock cap on, let’s see if there is any other column could be connected to it. Using intuition alone, we’ll check the relation with review\_creation\_date. Both columns relate to reviews and, in some form, to a time.

But what does it mean for two columns to be related? A knee-jerk reaction could be to check for a correlation, but this could be a risky proposition in the case of time series. Correlation measures the linear relationship between two variables, assuming that this relationship is consistent across the dataset. However, this assumption often doesn’t hold in time series, data due to factors like autocorrelation, trends, seasonality, and external shocks. Autocorrelation refers to the correlation of a signal with a delayed version of itself, a common characteristic of time series data that can inflate correlation measurements between two time series. Similarly, trends and seasonality can create spurious correlations that do not reflect a true causal relationship but rather the presence of underlying patterns that both series share. Moreover, external shocks impacting both series can temporarily increase correlation without indicating a meaningful or lasting relationship.

In our case, the critical factor is that the values in both columns relate to orders, which themselves were placed as series in time, so they will be correlated. Whatever these columns mean, their values will grow in time with orders. How, then, shall we define the relationship?

Maybe we won’t? We have tested generative AI for ideas and found its ability to understand the problem and propose a solution worthwhile.

# MA

Can you propose how I can investigate the relationship between the review\_answer\_ timestamp and the review\_creation\_date columns?

![](images/fbad2d582e39a331e74dcab2750ac27701ddfd624c3265a78dade66e05a4ddce.jpg)

To investigate the relationship between review\_answer\_timestamp and review\_ creation\_date, you can calculate the time difference between these two timestamps and analyze the distribution of the time differences. This will give you insights into how long it typically takes for a review to be answered.

Here’s a step-by-step guide to analyze the relationship between these two columns:

1 Calculate the time difference between review\_answer\_timestamp and review\_ creation\_date.

```txt
df_order_reviews['time_diff'] =
→(df_order_reviews['review_answer_timestamp'] -
→df_order_reviews['review_creation_date']).dt.total_seconds() 
```

The time\_diff column now contains the time difference in seconds.

2 Calculate basic statistics on the time difference to get an overview of the distribution.

```python
time_diff_summary = df_order_reviews['time_diff'].describe()
print(time_diff_summary) 
```

3 Visualize the distribution of time differences using a histogram or a box plot.

```python
import matplotlib.pyplot as plt
# Histogram
df_order_reviews['time_diff'].plot(kind='hist', bins=50)
plt.xlabel('Time Difference (Seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Time Difference Between Review Creation and Answer')
plt.show()

# Box plot
df_order_reviews['time_diff'].plot(kind='box', vert=False)
plt.xlabel('Time Difference (Seconds)')
plt.title('Box Plot of Time Difference Between Review Creation and Answer')
plt.show() 
```

By analyzing the distribution of time differences between review\_answer\_timestamp and review\_creation\_date, you can understand the typical response time and identify any outliers or trends in the data.

Feel free to convert the time differences to a more suitable unit (e.g., hours or days) if needed. You can also further investigate the relationship by looking at how the time difference varies with other factors, such as review scores or specific time periods (e.g., days of the week or months of the year).

It makes perfect sense to check the distribution of time differences between dates in two investigated columns. Let’s apply the proposed code.

The time difference summary analysis proves that the default timeframe of seconds may not be the most useful for the analysis.

<table><tr><td>count</td><td>9.922400e+04</td></tr><tr><td>mean</td><td>2.720730e+05</td></tr><tr><td>std</td><td>8.545003e+05</td></tr><tr><td>min</td><td>7.709000e+03</td></tr><tr><td>25%</td><td>8.682075e+04</td></tr><tr><td>50%</td><td>1.447155e+05</td></tr><tr><td>75%</td><td>2.681480e+05</td></tr><tr><td>max</td><td>4.481561e+07</td></tr></table>

Name: time\_diff, dtype: float64

However, our AI advisor mentioned that seconds might not be the best units for this data analysis. Fortunately, getting it to other time units is as simple as dividing the result by a constant. Feeling lazy, we asked generative AI to amend the code. It even took care of proper axis titles. The resulting images are presented in figure 2.7.

Judging by the time distribution, where some answers are provided within a few hours and others after many months, it seems very much like some human interaction drives the difference.

![](images/5d59182126df958e9be819c920015e2971442974f2af28c0e286aded8a0e916c.jpg)

<details>
<summary>bar</summary>

| Time Difference (Hours) | Frequency |
| ----------------------- | --------- |
| 0                       | 98000     |
| 1000                    | 2000      |
</details>

![](images/02459f2785c712230b5827802b58ad3a3cf463956917024508f51c3d10812588.jpg)

<details>
<summary>boxplot</summary>

| Time Difference (Hours) | time_diff |
| ----------------------- | --------- |
| 0                       | 0         |
| 12000                   | 0         |
</details>

Figure 2.7 Distribution of the time difference between the review\_answer\_timestamp and review\_creation\_date columns represented as a histogram (a) and a box plot (b)

Let’s try to apply logic here. We have a review creation and review answer. As the data comes from an online platform, the first intuition is that the user creates the review after purchase, and the seller answers to the reviewer after some time.

This example shows that the combined might of generative AI and human expertise can easily be beaten by vague column-naming conventions and a lack of metadata. Actually, the review\_creation\_date column contains the date of sending the survey to the customer, and the review\_answer\_timestamp indicates when the customer answered it. This is yet another reason to always confirm the naming convention data creators used.

# 2.6.4 Harmonizing data

Let’s turn our attention to the structural issue of the number of reviews per . . . and here is the trick: are you actually sure what those collected reviews are concerned with? Getting multiple reviews of the same product is one thing. It’s not unusual for multiple people buy the same thing and express their, often diverse, opinions. However, getting multiple reviews of the same order would require your attention, as you would need to decide how to evaluate order satisfaction in the case of more than one score. Would you use the last review or the average?

In our dataset, 547 orders have more than one review. Now we should check if they come from the customer who ordered it, or from multiple customers, which would be worrying. To answer the question, we need to harmonize our data and connect different sources to form a coherent whole.

Let’s assume we feel lazy (that’s a reasonably safe assumption) and that we want our generative AI to do the heavy lifting.

![](images/9b6c4b915144782a14a9c94095ead9c5cf8a96ef3e3af4a9d686ae8420a7fc62.jpg)

I have another DataFrame named df\_customers. There are two columns customer \_id and customer\_unique\_id. What shall I do to create in the previously discussed df\_order\_reviews an additional column with customer\_unique\_id correctly assigned to customer\_id, which is already there?

![](images/1b4da050d333f83d414037cfdfb094f0673f645ffbec4022375428c31afa106e.jpg)

To add the customer\_unique\_id column to the df\_order\_reviews DataFrame based on the customer\_id column, you can use the merge() function in pandas. Here’s how to do it:

Merge the df\_order\_reviews and df\_customers DataFrames on the customer\_id column.

```python
merged_df = df_order_reviews.merge(df_customers, on='customer_id', how='left') 
```

This will perform a left join, meaning that all rows from df\_order\_reviews will be included in the merged\_df DataFrame, and the corresponding customer\_unique\_id values from df\_customers will be matched based on the customer\_id column.

Now, the merged\_df DataFrame contains an additional customer\_unique\_id column, with the correct values assigned to each customer\_id. If you want to update the original df\_order\_reviews DataFrame instead of creating a new one, you can simply assign merged\_df to df\_order\_reviews:

```python
df_orders_reviews = merged_df 
```

Now, that’s a nice bit of code with no right to work! It’s trying to assign customers to orders in the df\_order\_reviews DataFrame. However, no column in df\_order\_ reviews allows us to do this directly. We know that the only actual identifier we have is the order\_id column, as we did our homework and learned that customer\_id does not, in fact, identify customers.

THE CUSTOMER IS ALWAYS RIGHT Generative AIs will neither question nor correct you. If you tell them to believe in something, they will assume you have your reasons. Although, there is a limitation to their suspension of disbelief. We tried to convince generative AIs that the Earth is flat, and even though they agreed to keep this assumption for the sake of the discussion, they reminded us every now and then that the Earth is, in fact, round. However, their tolerance borders are set pretty far.

We can get the desired result in a two-step process by first connecting df\_orders and df\_customers on the customer\_id field. This will give us a DataFrame that contains the customer\_unique\_id for each order. We can then connect this DataFrame to df\_order\_reviews on the order\_id field. Alternatively, we could start by connecting df\_orders and df\_order\_reviews on the order\_id field. Then we could connect the resulting DataFrame to df\_customers on the customer\_id field. Hopefully you can now see why the initial data analysis is critical. You need to see all the DataFrames to harmonize data from multiple sources effectively.

Joining, merging, and concatenating tables may be obvious to you, but, for others, this bit of data engineering 101 may still be something to worry about. In the past, just knowing what needs to happen was a required but not sufficient condition for getting the code to perform the desired operation. We’ve seen the computer science degree requirement in many data analysts’ job descriptions. Let’s take this opportunity to check if today’s gaps in coding experience can be closed using generative AI.

![](images/958121c7c11daa3698760181dc3af4536c812cc17962e10bd22b75656de46049.jpg)

I have my df\_order\_reviews DataFrame, which has the order\_id column. I also have the df\_orders DataFrame, where I have the order\_id and the customer\_id columns. I also have the df\_customers DataFrame, where I have the customer\_id and the customer\_unique\_id columns. How do I assign a valid customer\_ unique\_id from df\_customers to each order\_id in df\_order\_reviews?

![](images/a8451e9a61097883f5fce52131baae57e740155b2e9f266b0f112da09b847831.jpg)

To assign the valid customer\_unique\_id from df\_customers to each order\_id in df\_order\_reviews, you will first need to merge df\_orders with df\_customers to create a DataFrame with order\_id and customer\_unique\_id columns. Then, merge this new DataFrame with df\_order\_reviews. Here’s how to do it step by step:

1 Merge the df\_orders and df\_customers DataFrames on the customer\_id column.

```python
orders_customers = df_orders.merge(df_customers, on='customer_id', how='left') 
```

Now, the orders\_customers DataFrame has order\_id and customer\_unique\_ id columns.

2 Merge the df\_order\_reviews and orders\_customers DataFrames on the order\_id column.

```python
merged_df = df_order_reviews.merge(orders_customers[['order_id', 'customer_unique_id']], on='order_id', how='left') 
```

This will perform a left join, meaning that all rows from df\_order\_reviews will be included in the merged\_df DataFrame, and the corresponding customer\_unique\_id values from orders\_customers will be matched based on the order\_id column.

Now, the merged\_df DataFrame contains an additional customer\_unique\_id column, with the correct values assigned to each order\_id. If you want to update the original df\_order\_reviews DataFrame instead of creating a new one, you can simply assign merged\_df to df\_order\_reviews:

```python
df_order_reviews = merged_df 
```

Now, your df\_order\_reviews DataFrame has the customer\_unique\_id column correctly assigned to each order\_id.

This time, the code works as advertised. Generative AIs indeed can supplement you with the code; they know how to do it (even if they sometimes need severe prodding to get something working). The decision about what needs to happen is still yours (even if the initial conversations provided you with suggestions).

Now, to finish this part of the exercise, let’s check if multiple reviews do come from different customers; in such a case, you should probably inform your IT department, as there would be a strong possibility of erroneous review assignments to orders. The following code should give you the required answer (and no, we didn’t write this ourselves).

```python
unique_customers_per_order =
    df_order_reviews.groupby('order_id')['customer_unique_id'].nunique()
    multiple_customers_orders =
    unique_customers_per_order[unique_customers_per_order > 1]
    if len(multiple_customers_orders) > 0:
    print(f"There are {len(multiple_customers_orders)} orders with reviews
    from multiple customers.")
    print("\nOrder IDs and the number of unique customers:")
    print(multiple_customers_orders)
else:
    print("There are no orders with reviews from multiple customers.") 
```

This code groups the df\_order\_reviews DataFrame by counting unique customer unique\_id values, checks for cases where the count of unique customer\_unique\_id values assigned to order\_id is greater than 1, and finally prints the results. All the multiple reviews came from the same customers. This saves you a trip to the IT den and even allows an analysis of how prevalent an opinion about the order is over time.

We can assume that you now either know your data well enough or know how to use sufficiently eloquent and knowledgeable generative AI models to help you get a good insight into your data structure and properties. In the next chapter, we’ll focus on the business analysis itself.

# Things to ask generative AI

What is the typical data structure for data coming from <some\_business\_ area>?   
What data quality problems should I test for in the DataFrame I have provided you?   
 What distribution should I expect in the column describing <some\_activity>?   
 How do I deal with <a\_clear\_description\_of\_the\_encountered\_problem>?

# Summary

 Be aware of the context of your conversation with your generative AI advisor. Ask it to summarize its understanding of the context (this is particularly useful if you want to start a new session on the same topic, such as to research different approaches).   
 Don’t shy away from reminding your AI adviser about the purpose of the current work or the variable names used. Remember, it aims to please, not to be precise.   
There is no better way to understand the data than by looking at it.   
 When evaluating data quality, it’s essential to check its structure, consistency, and contents.   
 Double-check your data, triple-check, and reach out to data providers for clarification when you’re still in doubt.   
It’s a good practice to keep data quality investigation separate from the actual in-depth analysis . . .   
 . . . however, data cleaning and EDA are integral parts of your data analysis, and you’ll be repeating them sooner than you hope.

# Descriptive analysis and statistical inference supported by generative AI

# This chapter covers

 Using generative AI to design analytics   
Descriptive analytics of collected data using generative AI   
Utilizing generative AI to select appropriate inference analytics methods   
Using generative AI to obtain complete code solutions for data transformation, visualization, and modeling

The work described in the previous chapter was challenging and strenuous but absolutely necessary. You ensured that the data is of acceptable quality and that you understand its meaning. Your understanding of the data may still change as analysis uncovers nuances and intricacies of the underlying process, but you should have a solid foundation by now.

In this chapter, we will walk through the first part of an in-depth business analysis, the end-to-end descriptive analysis, learning how generative AI can help us at each step. And it can help a lot, from answering questions related to available data to providing real business insights. We will start with high-level analysis planning, touch on even more data preparation (surprise!), and then describe and visualize the data, searching for business-relevant information. We will also apply more advanced statistical modeling tools to our data, hoping to infer more insight from it.

# 3.1 Research questions

In the first chapter, we explained how you can use generative AI to help specify the business goal of your analysis. As we said then, your goals should usually be determined by the business stakeholders. In the second chapter, you did a primary cleanup of your data and investigated the contents of available data sources.

Let’s now make millions for your company! That’s your role, no? Well, actually, no. At least, it shouldn’t be. Your role is to inform decisions made by business stakeholders. But to do that, you need to translate the business questions into research questions. The plural here is not by accident. Usually, you’ll discover that answering a single business question requires answering multiple research questions. Take a simple question: “How do we make more money?” To answer that, you may go down the following path: “Who spends the most money with us?”, followed by “Can they buy more of our product?”, or “Where do we find similar people?” Or, as the dollar saved is worth ten dollars earned: “What step in our production produces the most scrap?”, followed by “What production parameters could we optimize to reduce this?”

The possibilities are endless, and you’re limited only by your imagination and data availability. That’s why knowing your data is so important! Business stakeholders usually think in terms of business processes. A person managing a supply chain would love to lay their hands on a prediction of product demand across different regions to minimize overstocking and understocking issues. A person responsible for alloy casting would love to have a tool that calculates optimal ratios of different substrate materials to get the final product. They understand the supply chain or metal mixing process; they might not appreciate the complexity of integrating regional sales trends and global economic indicators, or the need for confirmed quality and trace element analysis that are crucial for creating robust models. They don’t necessarily know the limitations and possibilities inherent to your data sources.

The key point here is that you will rarely answer the business question you’ve been presented with. More often than not, you will need to break it down and translate it into a series of research questions, and only after their analysis will you synthetize the final answer. In the first chapter, we showed you an iterative way of defining the analysis scope. Even if it seems you defined your scope just a short while ago, the moment you’ve finished cleaning and assessing your data inventory is a good time to look at the problem with fresh eyes. Maybe some questions you thought were answerable aren’t, and perhaps new opportunities have arisen.

As we were writing this book, we asked generative AI what information it would want from us to help us formulate research questions about the dataset we have at hand (think of a situation when a business stakeholder drops data on your lap with a short request “do something about it”; it happens). What we got back was a handy checklist, which should help you structure your thinking about what questions are and aren’t answerable in the context of your data environment:

Data dictionary—A brief description of each variable in your dataset, including its type (e.g., continuous, ordinal, or nominal), measurement scale (e.g., interval, ratio), and any potential coding or transformation applied.   
 Data sources and context—The origin of the data, the context in which it was collected, and any relevant background information.   
 Data collection and sampling methods—How the data was collected, any sampling methods applied, and any potential biases or limitations in the data.   
Domain knowledge—Any specific domain knowledge or expertise you have about the subject matter of the dataset.   
 Goals and interests—Goals and interests for this analysis, such as identifying patterns, making predictions, evaluating a policy, understanding relationships between variables, and so on.   
 Stakeholders—Stakeholders who will benefit from the insights generated from your analysis.   
 Temporal and spatial aspects—Temporal or spatial components that may affect the research questions.   
 Previous research—Any knowledge of prior research or studies conducted using similar data or in the same domain.   
 Limitations and constraints—Any limitations or constraints in the data or the analysis process that might affect the research questions you can explore.

Collecting all this information at this stage will allow you to design an analytics process that won’t suddenly stop midway when you realize you are missing a critical bit of required data.

With all this information at hand, you may come up with a bunch of research questions, answers to which you will be able to synthesize into the answer to your business question. But are they really all relevant questions? Fortunately, you have access to a tool with hundreds of combined years of analytical experience. With its help, you can make sure you didn’t omit any relevant issues and check that all the research questions you are thinking of asking are indeed relevant to the analyzed business issue. Such help will be of exceptional value if your boss sends you an email with a pile of files and asks you to extract all possible insights from them.

Let’s see how a generative AI advisor tackles the problem of overly general business problems in the context of available data. We will use our example dataset of Brazilian e-commerce, specifically the data description, and ask generative AI about possible related research questions. Please note that, due to the size of the request, it’s presented in full as appendix A.

# MA

Propose research questions for the analysis of the following set of data:

1. Data description and dictionaries: Data is composed of 8 DataFrames described in detail below:

\# BORING DETAILS RELATED TO POINTS 1–5 (see appendix A)

6. Goals and interests: I would like to increase the business efficiency of the e-commerce shop which produced this data.

7. Temporal and spatial aspects: Data comes from Brazil and describes orders from 2016 to 2018.

8. Previous research: Unknown.

9. Limitations and constraints: We would like to focus on descriptive analytics and avoid Machine Learning methods beyond linear or logistic regression.

# 6

Based on the provided information, here are some potential research questions for your analysis:

1 What are the most popular product categories in terms of revenue, and how do their sales performance vary across different regions in Brazil?   
2 How does the average product price, freight value, and payment value differ across different product categories and regions?   
3 What is the distribution of review scores across different product categories?   
4 How does the order status (e.g., delivered, shipped, etc.) vary across different regions, product categories, and sellers?   
5 What is the relationship between product attributes (e.g., weight, dimensions) and overhead costs (e.g., shipping costs)?   
6 What factors (e.g., delivery time, price, product attributes) contribute to differences in the average review score?   
7 How do different payment methods and the number of payment installments affect order completion rates and customer satisfaction?   
8 What is the impact of delivery time (actual vs. estimated) on customer satisfaction and review scores?   
9 Are there any significant differences in sales performance and customer satisfaction between sellers from different cities or states?

These research questions focus on descriptive analytics and should help you gain insights into the factors that influence sales performance, customer satisfaction, and overall business efficiency for the e-commerce shop.

As you can see, you can identify multiple areas of interest within seconds! While our initial inquiry didn’t specify objectives beyond enhancing business value, performing the suggested analytics should provide business stakeholders with information, allowing them to make significant steps toward the overarching goal of increasing business efficiency.

I FOUND 1,000 WAYS OF NOT DOING SOMETHING It would be best to talk to the business at this stage. They should think about whether such an insight will help them and if they want to prioritize it. Most importantly, this list will hopefully spark some new ideas about what kind of analysis they could immediately use to generate value.

This list is good enough for us to use as a base for our analysis. Of course, we might expect more of a typical analysis, like the Net Promoter Score (the most common method of measuring client satisfaction), but the result is not bad, not bad at all!

# 3.2 Analysis design

Once you have a clear goal, you’ll probably feel energized and may be tempted to jump into creating pivot tables and charts . . . Sit down, sip a coffee, and wait until that feeling passes. In chapter 1, we advised you to first prepare a protocol of what your analysis will look like, what the possible results are, and what the meaning of each of these possible results would be. This element of experiment design is often overlooked, even in the academic research world, but you don’t want to learn from the worst. Getting some results and trying to fit a theory to them may result in worthless science fiction research papers (not to be mistaken with a respectable literature genre in which we’ve authored some titles ourselves); in business reality, this may lead to significant financial losses. Always plan ahead. No result should come as a surprise. Prepare a complete list of possible results and their meaning in the context of your business case. For example, if the current price is higher than the purchase price, sell; if they are equal, hold; otherwise buy.

Of course, no protocol is set in stone. You will likely revise it after preprocessing your data (you may find that not all planned analyses are possible, or new ideas might strike you while scrolling through the data). Your stakeholders may change their priorities or focus areas when you’re halfway through. Even in this book we ignore our own advice—the speed of GenAI development outpaced our typing abilities, so we had to revisit parts of this book a couple of times. Pretending that we followed the assumed path would be a straight-up lie.

Unfortunately, cases where playing analysis by ear is justified are less common than the popularity of this approach. The sad fact is that as rare as proper experiment design is in an academic environment, it’s even rarer outside of it. You won’t find many good materials to guide you through the process. Even in the data (or text) corpus on which most generative AIs are trained, the cases where analytics design includes prior result analysis are most likely rare and far between, as none of the tested AI advisors considered it worth mentioning.

![](images/c8a6918284a6d36e5325eab027304cf7cd167d742bcf1f71ca76da04c8f859f3.jpg)

Can you propose a design of the analysis that would answer all these questions based on the provided data?

![](images/b165d232f0dfb8d247496eea8697468f143c09078fdd96d7e8072727d06de7be.jpg)

To answer the proposed research questions, you can follow this general design for your analysis:

# 1 Data Preparation:

a Merge relevant DataFrames to create a comprehensive dataset:

Merge df\_product\_category\_translation with df\_products to get product category names in English.   
ii Merge df\_orders, df\_customers, and df\_order\_items using customer\_ id and order\_id.   
iii Merge the resulting DataFrame with df\_products using product\_id.   
iv Merge the DataFrame with df\_order\_payments using order\_id.   
Merge the DataFrame with df\_order\_reviews using order\_id.   
vi Merge the DataFrame with df\_sellers using seller\_id.

# b Clean the dataset:

i Handle missing values (e.g., impute, drop, or leave as is, depending on the context).   
ii Convert data types if necessary (e.g., timestamps, floats, and integers).   
iii Create new variables, such as delivery time difference (actual vs. estimated), if needed.

# 2 Descriptive Analysis:

a Compute summary statistics for key variables (e.g., sales volume, revenue, product attributes, and review scores).   
b Create visualizations to explore patterns and trends in the data (e.g., bar charts, line charts, scatter plots, and heatmaps).   
c Conduct cross-tabulations and comparisons across different categories (e.g., regions, product categories, and sellers).

# 3 Inferential Analysis:

a Test for statistically significant differences between groups (e.g., using t-tests, ANOVA, or chi-square tests).   
b Perform correlation analyses to identify relationships between variables (e.g., product attributes and sales performance).   
c Conduct linear or logistic regression analyses to identify predictors of key outcomes (e.g., sales volume, revenue, and customer satisfaction).

# 4 Interpretation and Discussion:

a Summarize key findings from the descriptive and inferential analyses.   
b Discuss potential explanations for the observed patterns and relationships.   
c Identify potential limitations of the analysis and areas for future research.

# 5 Conclusion and Recommendations:

a Draw conclusions based on the analysis findings.   
b Provide actionable recommendations to improve the e-commerce shop’s business efficiency.

Following this general design for your analysis will help you systematically answer the proposed research questions using the provided data.

Let us share a little story, or actually more than a dozen we encountered, fitting the same scenario: The analyst performs a regression analysis to explore the relationship between social media advertising spend and sales. The results indicate a statistically significant correlation between the amount spent on social media ads and increased sales. The company decides to increase social media spending, only to find out their return on investment (RoI) is in the negative. To make things worse, the budget diverted to social media campaigns weakened other business functions. That is a typical example of a poor analytics design with a perfectly avoidable outcome.

It is not our goal to follow in the footsteps of Don Quixote, pursuing lofty ideals that we will never obtain, but you should spend some time inquiring about the possible results of different types of analytics and their meanings. In some cases, predicting all possible outcomes is not feasible. For example, you don’t want to come up with all possible variants of a chart you’re expected to generate. But you should have a general idea of expected shapes or traces. We touched upon this previously when we discussed data cleaning. You need to understand what’s expected to notice what’s relevant that’s unexpected. In some analyses, you should spend more time thinking about the meaning of the results. A good example here would be correlation analysis.

What does correlation mean from the business perspective? How big a correlation is actually meaningful ? (Do not mistake this for statistical significance, as did the protagonists of the earlier story.) When calculating regression, what is the predictive power you require? There are no ready-to-use templates to be filled out. Your domain knowledge and understanding of the business will allow you to distinguish between valuable and misleading insights. Generative AI can help you, but don’t expect it to do all the heavy lifting for you. You need to talk to your business people to be able to deeply integrate domain knowledge into your analytical pipeline.

In the generative AI’s proposed design, there is one popularity-bias-driven element—the content of point 3.a, the methods for statistical testing. We’ll explain our gripe with that particular point in the introduction to section 3.5.

Other than that, the execution of this plan may indeed extract some insight from the data we meticulously cleaned.

# 3.3 Descriptive data analysis

Many people approach data analysis (both stakeholders and naive newcomers to the job), with quite high expectations. Wouldn’t it be great to just drop all your company’s data into a magical box and receive back a set of simple instructions, like “Fire Sue from the third floor, as her micromanagement style kills the soul and effectiveness of her team. While you’re firing people, don’t forget Joe from packaging, as he’s the reason behind 20% of your returns”? Or, “Add the pink Buy now! button in the left-right corner of your landing page, and you’ll get 61.73% more sales in the first week”?

Going from data to information to insight is a process. It can be somewhat automated or sped up by the tools, but a lot of data analysis is just that—analyzing : a detailed examination of the elements or structure of the data. Despite the best efforts of AIfocused companies, the part where someone needs to describe data elements and structure is not going anywhere, primarily because it offers an overview of business performance. Various statistical measures and visualization techniques enable you to identify patterns, relationships, and anomalies within datasets. You can use descriptive analytics to understand your business operations, customer behavior, and market dynamics better, laying a solid foundation for informed decision-making and future analysis.

It doesn’t matter if you work for an organization, big or small. Analyzing data from a restaurant, you may use this approach to identify the most ordered items versus those rarely ordered. While working in the corporate office of the restaurant chain, you may use it to determine the most popular items by location and time of day. This insight could then guide decisions around stock management, staff scheduling, and targeted promotions, ultimately enhancing operational efficiency and customer satisfaction. Despite its simplicity, descriptive analytics is crucial in paving your way toward more advanced analytics methods, such as predictive and prescriptive analytics.

You should describe your data using nomen omen descriptive statistics, including mean, median, mode, standard deviation, and percentile values. You should also prepare visualizations like bar charts, histograms, and scatter plots to further enhance your ability to identify and examine patterns and trends within the data.

Four of the nine research questions initially proposed by generative AI can be addressed using these methods. We will do just that in the following subsections. The other five will require a somewhat different toolbox, presented in section 3.4.

# 3.3.1 Popularity of product categories

Recall the question provided by ChatGPT: “What are the most popular product categories in terms of revenue, and how do their sales performance vary across different regions in Brazil?” If working with e-commerce data makes you stifle your yawn, don’t worry. The same methodology is helpful in many business areas. Let’s explore some examples where this approach can provide you with valuable insights:

 Retail, e-commerce, and manufacturing—Beyond product categories, this method can be applied to understand customer segments’ buying behavior across different regions or time periods, such as analyzing seasonal trends in purchasing or the effect of marketing campaigns on various demographics.   
 Healthcare—In healthcare, similar techniques can be used to analyze the distribution of disease incidence or treatment outcomes across different geographical areas and demographic groups. This can help in resource allocation, understanding disease spread patterns, and tailoring public health interventions.   
 Financial services—For banks and financial institutions, analyzing the distribution of loan or credit card defaults by product type and geographic region can help in risk management and in designing targeted financial products.   
 Supply chain and logistics—Here, the method can be used to analyze the performance of different logistics routes or transportation methods, categorizing them by cost, efficiency, or environmental impact across various regions. This can aid in optimizing routes, reducing costs, and improving sustainability.   
 Telecommunications—Analyzing the usage patterns of different service plans or products (e.g., data plans, voice plans) across regions can help in tailoring

offerings, improving network infrastructure, and identifying new market opportunities.

Utilities and energy—In this sector, analyzing consumption patterns of different energy sources (e.g., electricity, gas) across regions can inform infrastructure development, energy conservation efforts, and pricing strategies.   
 Tourism and hospitality—Understanding the preferences for different types of accommodations or travel experiences across various tourist demographics can help businesses tailor their services, optimize pricing strategies, and improve customer satisfaction.   
 Real estate—Analyzing the performance of different types of properties (e.g., residential versus commercial) across regions can inform investment strategies, property development, and marketing efforts.   
 Education—Evaluating the performance of different educational programs or courses across demographic groups can help educational institutions tailor their offerings, improve student outcomes, and optimize resource allocations.   
 Government and public policy—Governments can use this method to analyze various policy impacts across regions, such as the effectiveness of economic incentives, public health initiatives, or infrastructure projects, enabling more informed decision-making.

For each of these examples, the method we’ll look at next can help you uncover patterns and insights that might not be immediately apparent. You can really support your businesses by categorizing data across meaningful dimensions (like product categories, service types, or demographic segments) and analyzing their performance across different regions or groups.

Let’s get back to work. We will start with the simple task of testing which product categories bring the most revenue. It’s a fundamental analysis required for product portfolio optimization. We can apply the same methodology to evaluate the performance of different groups quickly.

![](images/cced14755fa297cfc81fff0fb2fa472245ca325b7e4d2764d54ef10174b8782d.jpg)

Provide me with a complete Python code solution required to answer this question on the most common product categories in the dataset.

![](images/eb682c184a419dc4a11f8a9af3399a229f58ce2b32e3fc0f4be7f51f822d1641.jpg)

To answer the question about the most common product categories in the dataset, you can follow these steps in Python:

1 Import necessary libraries   
2 Read and merge the required DataFrames   
3 Perform the analysis to find the most common product categories   
4 Display the results

Here’s the complete Python code solution:

import pandas as pd

```python
# Read DataFrames
df_products = pd.read_csv('df_products.csv')
df_product_category_translation =
pd.read_csv('df_product_category_translation.csv')

# Merge DataFrames
df_products_merged = df_products.merge(
df_product_category_translation, on='product_category_name',
how='left')

# Analyze the most common product categories
category_counts =
df_products_merged['product_category_name_english'].value_counts()

# Display the results
print("The most common product categories are:")
print(category_counts.head(10)) 
```

This code will read the data, merge the DataFrames, count the occurrences of each product category, and display the top 10 most common categories.

Generative AI failed to understand what question we were referring to. We hoped it would recall the question it itself proposed just two prompts earlier: “What are the most popular product categories in terms of sales volume and revenue, and how do their sales performance vary across different regions in Brazil?” Instead, it provided us with unhelpful output related to identifying the most common product categories instead of their sales performance. Let this be a warning that you shouldn’t always rely on generative AI to recall your conversation correctly if your prompt is vague.

TOMAYTO, TOMAHTO Sometimes, the difference between the question you asked and the question generative AI answered might be minute and hard to spot, but inferring any insight from the answer to a question that’s different than you asked may have far-reaching implications.

Let’s try to be more specific.

![](images/e76aae09c4e76d9d288a229224c0033212e24e84a0b9dfd10bd89f5061c8a07f.jpg)

Provide me with a complete Python code solution required to answer the question, “What are the most popular product categories in terms of sales volume and revenue, and how do their sales performance vary across different regions in Brazil?”

![](images/15789c9dff4a52df092377bd264cd7ddd05e4638f9d6297eafb0fffb0aecb3d7.jpg)

To answer this question, you need to follow these steps in Python:

1 Import necessary libraries   
2 Read and merge the required DataFrames   
3 Perform the analysis to find the most popular product categories in terms of sales volume and revenue and how their sales performance varies across different regions in Brazil   
4 Display the results

Here’s the complete Python code solution:   
```python
import pandas as pd

# Read DataFrames
df_products = pd.read_csv('df_products.csv')
df_product_category_translation =
→pd.read_csv('df_product_category_translation.csv')
df_order_items = pd.read_csv('df_order_items.csv')
df_orders = pd.read_csv('df_orders.csv')
df_customers = pd.read_csv('df_customers.csv')

# Merge DataFrames
df_products_merged = df_products.merge(
→df_product_category_translation, on='product_category_name',
→how='left')
df_order_items_merged = df_order_items.merge(
→df_products_merged, on='product_id', how='left')
df_orders_merged = df_orders.merge(
→df_customers, on='customer_id', how='left')
df_merged = df_order_items_merged.merge(
→df_orders_merged, on='order_id', how='left')

# Calculate sales volume and revenue per category
category_sales = df_merged.groupby(
→['product_category_name_english', 'customer_state']).agg(
→{'order_id': 'count', 'price': 'sum'}).reset_index()
category_sales.columns =
→['product_category', 'customer_state', 'sales_volume', 'revenue']

# Sort by sales_volume and revenue
category_sales_sorted = category_sales.sort_values(
→by=['sales_volume', 'revenue'], ascending=False)

# Display the results
print("The most popular product categories
→in terms of sales volume and revenue are:")
print(category_sales_sorted.head(10))

print("\nSales performance across different regions in Brazil:")
sales_by_region =
→category_sales_sorted.pivot_table(
→index='product_category',
→columns='customer_state',
→values=['sales_volume', 'revenue'], fill_value=0)
print(sales_by_region) 
```

Replace the file names df\_products.csv, df\_product\_category\_translation .csv, df\_order\_items.csv, df\_orders.csv, and df\_customers.csv with the appropriate file names for your dataset. This code will read the data, merge the Data-Frames, analyze the sales volume and revenue for each product category across different regions in Brazil, and display the results.

The interesting fact is that, following the language of the conversation, ChatGPT assumed we would be interested in English names of categories rather than Portuguese, even though it itself is fluent in both languages.

The resulting DataFrame has 54 columns. If only generative AI would suggest a way to make interpreting the results easier, right? Well, yes and no. It is important to remember that we don’t leave our own analytical skills at the front door when we let generative AI help us out. Any experienced data analyst could tell you that a large DataFrame such as this will benefit from the visualization of the results. So before we go further with the steps proposed by generative AI, we’ll take a moment to get some visuals.

![](images/519add543083bc147919708f22666ecc4536943c5d9dd3d904ab7ffa113cd482.jpg)

Can you propose visualization methods for sales\_by\_region DataFrame, which would allow answering the posed research question?

![](images/ad0a5542a4b3bc97791f22fd5e74c209432c579f57e92fe1a89f6860d9815fec.jpg)

Certainly! To visualize the sales\_by\_region DataFrame and answer the research question effectively, you can use the following visualization methods:

1 Bar plot: You can create a grouped bar plot to compare sales volume and revenue for each product category across different regions in Brazil. The x-axis will represent the regions, and the y-axis will represent the sales volume and revenue. You can use different colors for each product category to distinguish them.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.barplot(data=sales_by_region, x='customer_state', y='revenue',
    hue='product_category_name_english', ci=None)
plt.title('Revenue by Product Category and Region')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(data=sales_by_region, x='customer_state', y='sales_volume',
    hue='product_category_name_english', ci=None)
plt.title('Sales Volume by Product Category and Region')
plt.show() 
```

2 Heatmap: Another way to visualize the sales performance across different regions in Brazil is by using a heatmap. You can create a pivot table with regions as rows, product categories as columns, and sales volume and revenue as values. Then, you can use a heatmap to represent the sales performance using a color gradient.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Create pivot tables for sales_volume and revenue
sales_volume_pivot = sales_by_region.pivot_table(
→values='sales_volume', index='customer_state',
→columns='product_category_name_english')
revenue_pivot = sales_by_region.pivot_table(
→values='revenue', index='customer_state',
→columns='product_category_name_english') 
```

```python
# Plot heatmaps
plt.figure(figsize=(12, 8))
sns.heatmap(sales_volume_pivot, annot=True, cmap='viridis', fmt='.0f')
plt.title('Sales Volume by Product Category and Region')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(revenue_pivot, annot=True, cmap='viridis', fmt='.0f')
plt.title('Revenue by Product Category and Region')
plt.show() 
```

These visualization methods will help you better understand the sales performance of different product categories across various regions in Brazil.

This code, instead of producing graphs, resulted in a warning and the following error message:

```txt
FutureWarning: The `ci` parameter is deprecated.
→ Use `errorbar=None` for the same effect.
ValueError: Could not interpret input 'customer_state' 
```

We present this transcript as a warning. Bugs and problems are to be expected. Getting generative AI to debug the code can take some effort, as appendix B shows. However, this exercise resulted in two conclusions worth presenting here:

 Generative AIs may provide you with incorrect code, and more than once at that. We can still use them to debug the code (with more or less success, depending on the language), as it may take less time than learning all the intricacies of syntax from the ground up yourself.   
 You should not leave the debugging process to generative AI completely, as it doesn’t have access to the results. Looking for oddities in the output and informing your AI advisor about them significantly speeds up the process.

Thanks to the provided code, we were able to generate four figures: two bar plots and two heatmaps.

The bar plots may not be suitable for adding to a presentation destined for an SD projector. In figure 3.1 you can find one of them; the second one is almost identical. To make it fit the page, we dropped the legend containing 71 categories (they are still present on the figure generated in the accompanying Jupyter notebook). It’s still unreadable, but that’s hardly generative AI’s fault. We are trying to visualize almost six thousand data points, after all!

To make this figure more consumable, we can ask our AI advisor to break it down by state or product group, but we’ll end up with dozens of charts. Let’s check if using heatmaps will save us this trouble. A visualization of the same data is presented in figure 3.2. Both heatmaps are available in the Jupyter Notebook in the book’s GitHub repository.

Unfortunately, the generated heatmap is not much more readable, is it? We printed this indecipherable image in this book as valuable learning material.

Sales Volume by Product Category and Region   
![](images/5f8545b8103b32efb50b9b5083c389bc810fe329b3dbd2bd52f65ef395869030.jpg)

<details>
<summary>bar</summary>

| customer_state | sales_volume |
| -------------- | ------------ |
| AC             | 0            |
| AL             | 0            |
| AM             | 0            |
| AP             | 0            |
| BA             | 200          |
| CE             | 100          |
| DF             | 150          |
| ES             | 100          |
| GO             | 150          |
| MA             | 50           |
| MG             | 1300         |
| MS             | 100          |
| MT             | 50           |
| PA             | 50           |
| PB             | 50           |
| PE             | 100          |
| PI             | 50           |
| PR             | 500          |
| RJ             | 1600         |
| RN             | 100          |
| RO             | 50           |
| RR             | 50           |
| RS             | 500          |
| SC             | 300          |
| SE             | 50           |
| SP             | 5200         |
| TO             | 3600         |
</details>

Figure 3.1 Bar plot of sales volume by product category and region

![](images/ec2d0a0617ad72612dca421cb2b6736e09b0cbda7732cb68603acde21966976e.jpg)  
Figure 3.2 Heatmap of sales revenue by product category and region

You will see unreadable graphics in your work every now and then. If you’re asked to prepare “something that will fit a PowerPoint slide,” it can really ruin your day. In such a case, you need to consider whether you face an inherent issue, like the number of bars in figure 3.1, or if the visual clutter can be remedied with a simple reformatting. If you’re unsure how to tweak your visualization software’s settings, generative AI is there for you! You should get the solution and an explanation to help you in your future work.

![](images/69ef837f1d82cc67d485a2ab28eb08a9b2af0f90c72b8b035cba2f86208dc0f7.jpg)

Can you modify the heatmap code so the numbers in the matrix are printed in a smaller font?

![](images/17448b2fabc7ec5bf9483c4d7c28822cecffde79e7f0ee87708055bb71a5ef5a.jpg)

Sure! You can adjust the font size of the numbers in the heatmap by using the annot\_kws parameter within the sns.heatmap function. You can set the font size to a specific value as follows:

```python
plt.figure(figsize=(12, 12))
sns.heatmap(revenue_df.set_index('product_category'),
    cmap="YlGnBu", annot=True, fmt=".0f", linewidths=0.5,
    annot_kws={"size": 6})
plt.title("Revenue by Product Category and State")
plt.show()

plt.figure(figsize=(12, 12))
sns.heatmap(sales_volume_df.set_index('product_category'),
    cmap="YlGnBu", annot=True, fmt=".0f", linewidths=0.5,
    annot_kws={"size": 6})
plt.title("Sales Volume by Product Category and State")
plt.show() 
```

In this example, I set the font size to 6. You can change this value as needed to achieve the desired appearance.

Before we proceed to present the result, we need to note that the revenue\_df Data-Frame mentioned in the code was defined in the previously mentioned appendix B, where we show a long and winding road to the correct code. This time, however, things progressed as expected. The result is presented in figure 3.3.

The overall result is now possible to analyze. Maybe not so much in terms of reading individual numbers, but that’s precisely the purpose of the heatmap. It’s meant to pinpoint outliers in the dimensional distribution.

The other visualization proposed is stacked bar plots, which are included in the book’s GitHub repository.

At this stage, we are well equipped with visualizations for drawing business conclusions on the most popular product categories. Following our AI advisor’s guidance, we will now move on to research their performance.

# 3.3.2 Performance of products in their categories and regions

As a reminder, based on our data availability, our generative AI advisor proposed the following approach to measuring performance: “How does the average product price, freight value, and payment value differ across different product categories and regions?” The information on the performance and behavior of products across categories and different locations is a trove of information for the business. Using this methodology, you may support decisions driving sales and marketing efforts. For example, best practices from best-performing regions could be used to boost the efficiency of weaker ones, or some products could be dropped and replaced by more profitable ones.

![](images/1eae4638e955a2663b93ac173feff7d6978502747e450023ea15e1bff835a7c7.jpg)  
Figure 3.3 Heatmap of sales revenue by product category by state, reformatted

However, this one application wouldn’t be worth reading about unless you’re genuinely excited by marketing. Fortunately, by applying this analytical framework, you can explore a lot of different variables to extract insights across various industries. Here are some examples:

 Customer lifetime value (CLV) and acquisition cost—In industries like e-commerce, telecommunications, or financial services, analyzing the relationship between the CLV and the cost of acquiring customers across different products or services and regions can help optimize marketing spend and target customer segments more effectively.

 Service response time and customer satisfaction —For service-oriented sectors like healthcare, logistics, or customer support, examining how response times relate to customer satisfaction across different service categories and regions can pinpoint areas for improvement and guide resource allocation.   
 Inventory turnover and sales performance —In retail and manufacturing, analyzing the relationship between inventory turnover rates and sales performance across product categories and regions can help manage inventory more efficiently, reduce holding costs, and identify demand patterns.   
Renewable energy production and consumption—In the utilities and energy sector, examining the relationship between renewable energy production (e.g., solar, wind) and consumption across different regions can inform infrastructure investments and sustainability initiatives.   
 Occupancy rates and rental yields—In real estate, particularly within the hospitality and residential sectors, analyzing the relationship between occupancy rates and rental yields across different property types and locations can aid investment decisions and pricing strategies.   
 Utilization rates and operational costs —For transportation and logistics, looking at how vehicle or asset utilization rates relate to operational costs across different regions or routes can optimize operations and improve profitability.   
 R&D spend and innovation outcomes—In technology and pharmaceutical industries, analyzing the relationship between R&D spending and outcomes such as patent filings or product launches across different categories can guide investment strategies and innovation focus.   
Digital marketing spend and engagement metrics—For businesses investing in digital marketing, examining how spending relates to engagement metrics (e.g., clickthrough rates, conversion rates) across different campaigns or regions can optimize marketing strategies and budget allocation.   
 Workforce training investment and productivity gains —In sectors with significant human capital, such as education, healthcare, or manufacturing, analyzing the relationship between investment in workforce training and productivity gains across different departments or locations can inform talent development strategies.   
Sustainability initiatives and corporate performance—Across industries, examining the relationship between investments in sustainability initiatives (e.g., carbon footprint reduction, waste management) and corporate performance metrics (e.g., profitability, brand perception) can guide corporate social responsibility efforts and investment.

Each of these examples applies the analytical approach of exploring relationships and variations across categories and regions to different variables.

Let’s look at how we can capture performance differences between categories, as they may be valuable for business decision-making.

![](images/f35d84e94b3f0a1ab7e5e517ede3c3a252d8f338fcfa549245079bd7a160a999.jpg)

Provide me with a complete Python code solution required to answer the question, “What are the most popular product categories in terms of sales volume and revenue, and how do their sales performance vary across different regions in Brazil?”

![](images/64f78dfbf038718ed078980a885eef68a7bd3088fbba1922e8c17b63e6bd567f.jpg)

To answer this question, you can use the merged DataFrame that you created earlier and perform a groupby operation on product categories and regions. You will then calculate the average product price, freight value, and payment value for each group.

Here’s the Python code to achieve this:

```python
import pandas as pd
# Assuming you have already merged the DataFrames and named it
→ 'merged_data'

# Group the data by product category and region (state)
grouped_data = merged_data.groupby(
→ ['product_category_name_english', 'customer_state'])

# Calculate the average product price, freight value,
→ and payment value for each group
average_values = grouped_data[
→ ['price', 'freight_value', 'payment_value']].mean()

# Reset the index to have a flat DataFrame
average_values = average_values.reset_index()

# Rename the columns for clarity
average_values.columns = ['product_category', 'state',
'avg_product_price',
→ 'avg_freight_value', 'avg_payment_value']

# You can now explore the 'average_values' DataFrame
→ to analyze the differences across product categories and regions 
```

The average\_values DataFrame will contain the average product price, freight value, and payment value for each product category and region (state). You can further analyze this DataFrame using various visualization techniques, such as bar charts or heatmaps, to better understand the differences across product categories and regions.

We presented the received answer in its entirety, as there are three noteworthy elements:

 The first is generative AI’s ability to predict our next steps and suggest visualization techniques.   
The second is that it considers the readability of the column names.   
 The last one is, unfortunately, that it used the wrong name of the DataFrame. We never defined a merged\_data DataFrame.

We want you to pay attention now. You could assume that the merged\_data Data-Frame is just df\_merge from the previous example. But, as we repeat over and over, cultivate your paranoia! If there is any doubt, you should double- and triple-check to make sure what you are analyzing is indeed what you intend to analyze!

![](images/dba2a99209d8df80a51a86dbf4b5cef4c8c75de8a60a0a368c4e1311cfdb1d50.jpg)

Can you write the columns that should be in the merged\_data DataFrame you used?

![](images/4fdbc9efd525c9638be052a9f2d89cbec0fb33331ab3e5aacf2756928251fc50.jpg)

Certainly! Based on the data we discussed earlier, the merged\_data DataFrame should contain the following columns:

1 product\_category\_name\_english (str) - category name in English   
2 customer\_state (str) - customer state   
3 price (float64) - item price   
4 freight\_value (float64) - item freight value (if an order has more than one item, the freight value is split between items)   
5 payment\_value (float64) - transaction value

To create the merged\_data DataFrame, you would need to merge the necessary DataFrames, as discussed earlier in the conversation. Here’s a quick recap of how to create the merged\_data DataFrame:

1 Merge df\_order\_items with df\_orders on order\_id   
2 Merge the result with df\_product\_category\_translation on product\_category\_name   
3 Merge the result with df\_customers on customer\_id   
4 Merge the result with df\_order\_payments on order\_id

The resulting merged\_data DataFrame should contain the columns listed above, which can be used to answer the question related to average product price, freight value, and payment value across different product categories and regions.

Interestingly, merged\_data, hallucinated by ChatGPT, and df\_merged, which we actually have, do differ, and significantly! You would get an error if you tried to run the original code simply by replacing merged\_data with df\_merged.

KEEPING THE BELLS RINGING The longer the conversation, the more likely generative AI is to lose track of nuances of the conversation. To ensure the proper contextual awareness of your AI advisor, when you notice it hallucinating about provided data structures, paste it a reminder with a detailed description of the data in question, or move on to a new conversation session.

Remember, that’s not the worst-case scenario. Errors that break the code are simple to spot. Errors where things go smoothly, but the results are based on wrong data, are a different kettle of fish. Consider this fair warning.

The resulting DataFrame has 1,356 rows. Yet again, we should probably think of visualizing the result.

![](images/4fd062e246a1a1068085242ab966d30e87528e25adbd14c2b2ea624fccfb3174.jpg)

Could you propose a visualization method suitable for data in the generated average\_values DataFrame?

![](images/6793b828ae09271ac587641e78d30cf650375548a79408632818ed9ee6174c89.jpg)

Given the structure of the average\_values DataFrame, you can create:

1 A scatterplot matrix (pair plot) to visualize the relationships between average\_ product\_price, average\_freight\_value, and average\_payment\_value across different product categories and states. You can use seaborn’s pairplot function for this purpose.

Here’s the code to create a scatterplot matrix:

```python
import seaborn as sns

# Create a pair plot with different colors for each state
g = sns.pairplot(data=average_values, hue='state', markers=' Process')
# Set the title and labels for each plot
g.fig.suptitle(
->"Scatterplot Matrix of Average Values by State and Product Category",
->y=1.02)
g.set_axis_labels(
->"Average Product Price", "Average Freight Value",
->"Average Payment Value")

# Adjust legend
g.add_legend(title="State")

# Show the plot
plt.show() 
```

This will give you a scatterplot matrix that shows the relationships between the average product price, average freight value, and average payment value for each product category in each state. The points in the scatterplots will be colored according to the state.

2 Three separate bar plots - one for each value of interest (average product price, average freight value, and average payment value). These bar plots will display the product categories on the x-axis and the corresponding values on the y-axis, with each bar representing a state.

Here’s Python code to create these bar plots using the seaborn library:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Function to create bar plots for the given value
def create_bar_plot(data, value_col, title, ylabel):
    plt.figure(figsize=(15, 6))
    sns.barplot(x='product_category', y=value_col, hue='state', data=data)
    plt.title(title)
    plt.xlabel('Product Category')
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.legend(title='State', bbox_to_anchor=(1, 1))
    plt.show() 
```

\# Create bar plots for average product price, average freight value,

➥and average payment value   
create\_bar\_plot(average\_values, 'avg\_product\_price',   
➥'Average Product Price by State and Product Category',   
➥'Average Product Price')   
create\_bar\_plot(average\_values, 'avg\_freight\_value',   
➥'Average Freight Value by State and Product Category',   
➥'Average Freight Value')   
create\_bar\_plot(average\_values, 'avg\_payment\_value',   
➥'Average Payment Value by State and Product Category',   
➥'Average Payment Value')

The resulting scatterplot is presented as figure 3.4, and one of the bar charts is presented as figure 3.5.

Scatterplot Matrix of Average Values by State and Product Category   
![](images/859e9ba6c9f315e60ff6153ddd0f3159f98b785b56fa404200395d43df086984.jpg)

<details>
<summary>scatter</summary>

| State | avg_product_price | avg_freight_value | avg_payment_value |
|-------|-------------------|-------------------|--------------------|
| AL    | 2500              | 300               | 200                |
| AP    | 1500              | 100               | 150                |
| BA    | 1000              | 50                | 100                |
| CE    | 800               | 30                | 80                 |
| ES    | 600               | 20                | 60                 |
| GO    | 400               | 10                | 40                 |
| MA    | 200               | 5                 | 20                 |
| MG    | 100               | 3                 | 10                 |
| MS    | 50                | 2                 | 5                  |
| MT    | 30                | 1                 | 3                  |
| PA    | 20                | 1                 | 2                  |
| PB    | 15                | 1                 | 1                  |
| PE    | 10                | 1                 | 1                  |
| PI    | 5                 | 1                 | 1                  |
| PR    | 3                 | 1                 | 1                  |
| RJ    | 2                 | 1                 | 1                  |
| RO    | 1                 | 1                 | 1                  |
| RS    | 1                 | 1                 | 1                  |
| SC    | 1                 | 1                 | 1                  |
| SP    | 1                 | 1                 | 1                  |
| AM    | 1                 | 1                 | 1                  |
| DF    | 1                 | 1                 | 1                  |
| RN    | 1                 | 1                 | 1                  |
| TO    | 1                 | 1                 | 1                  |
| AC    | 1                 | 1                 | 1                  |
| RR    | 1                 | 1                 | 1                  |
| SE    | 1                 | 1                 | 1                  |
</details>

Figure 3.4 Scatterplot of relationships between average payment values, average freight values, and average product prices

![](images/b3f5453e6157cfd3387575d0ff26ea1590568804390c7595f25860de1d02acd5.jpg)

<details>
<summary>bar</summary>

Average Product Price by State and Product Category
| Product Category | State | Average Product Price |
| :--- | :--- | :--- |
| agro_industry_and_commerce | AL | 1450 |
| air_conditioning | AP | 520 |
| art | BA | 280 |
| arts_and_craftmanship | CE | 160 |
| audio | ES | 560 |
| auto | GO | 390 |
| baby | MA | 270 |
| bed_bath_table | MG | 180 |
| books_general_interest | MS | 730 |
| books_imported | MT | 100 |
| books_technical | PA | 100 |
| cds_dvds_musicals | PS | 100 |
| christmas_supplies | AM | 100 |
| cine_photo | RF | 650 |
| computers_accessories | TO | 1680 |
| consoles_games | OC | 1250 |
| construction_tools_construction | OC | 580 |
| construction_tools_ilities | OC | 320 |
| construction_tools_safety | OC | 1050 |
| cool_stuff | OC | 230 |
| construction_tools_garden | OC | 580 |
| construction_tools_tools | OC | 320 |
| diapers_and_hygiene | OC | 100 |
| drinks | OC | 100 |
| dvds_blu_ray | OC | 100 |
| electronics | OC | 100 |
| fashion_female_clothing | OC | 100 |
| fashion_bags_accessories | OC | 100 |
| fashion_children_clothes | OC | 100 |
| fashion_male_clothing | OC | 100 |
| fashion_shoes | OC | 100 |
| fashion_sport | OC | 100 |
| fashion_underwear_beach | OC | 100 |
| fixed_telephony | OC | 820 |
| flowers | OC | 650 |
| food | PR | 120 |
| food_drink | PR | 120 |
| furniture_bedroom | PR | 320 |
| furniture décor | PR | 320 |
| furniture_living_room | PR | 320 |
| furniture_mattress_and_upholstery | PR | 320 |
| garden_tools | PR | 320 |
| health_beauty | PR | 320 |
| home_appliances_2 | PR | 1150 |
| home_appliances_2 | SP | 880 |
| homeComfort_2 | SP | 480 |
| home_confort | SP | 320 |
| home_construction | SP | 320 |
| home_houseware | SP | 320 |
| industry commerce_and_business | SP | 1100 |
| kitchen_dining_laundry_garden_furniture | SP | 480 |
| la_cuisine | SP | 480 |
| luggage_accessories | SP | 520 |
| market_place | SP | 1150 |
| music | SP | 480 |
| musical_instruments | SP | 480 |
| office_furniture | SP | 650 |
| party_supply | SP | 280 |
| perfumery | SP | 280 |
| pet_shop | SP | 730 |
| security_and_services | SP | 180 |
| signaling_and_security | SP | 180 |
| small_appliances | SP | 650 |
| small_appliances_home_oven_and_coffee | SE | 2000 |
| sports_leisure | SE | 1250 |
| stationery | SE | 280 |
| tablets_printing_image | SE | 280 |
| telephony | SE | 280 |
| toys | SE | 280 |
| watches_gifts | SE | 480 |
The chart displays a vertical bar chart comparing the average product prices across various U.S. states and regions. The data is presented in a table format with rows of product names (e.g., 'home', 'oil', 'house') and columns of state or region (e.g., 'service', 'store'). The values for each bar are explicitly labeled on the chart. The data is already in English. The table is in English. The values for all other countries are in English. There is no additional data series present in the chart.
</details>

Figure 3.5 Grouped bar plot showing the relation of average product price per category per region

The piece of code responsible for explicitly naming the chart axes didn’t work correctly. Fortunately, the DataFrame column names used by matplotlib as a default are informative enough. We left it as is to drive home a more general point: Sometimes, in your work, especially under time pressure, you’ll be tempted to “save time” on naming conventions. Quickly, all variables will become x, tmp, or var1—it’s a terrible habit. You’ll agree with us after you open a file you wrote two months ago. You’re saving seconds now to lose literally hours later. Using informative variable names is a time saver. Of course, being too verbose won’t do much for your code readability either. A variable named second\_attempt\_to\_average\_the\_sales\_in\_Joe\_Smiths\_analysis\_ of\_his\_shop may be overkill.

The resulting figure 3.5 may take some time (and a magnifying glass or two) to analyze, but it should suffice to provide some business insight into product performance. If you lack a magnifying glass of sufficient magnitude, we will discuss utilizing generative AI to cluster product categories in the next section, where we’ll analyze product perception.

# 3.3.3 Review scores distribution

The value of knowing the distribution of review scores is relatively apparent. It’s critical feedback about how the products are perceived by the people paying for them. As we mentioned before, there are certain methods and measures for representing overall client satisfaction as a single number. Still, we’ll forget about them for the time being (pretending we are working on unknown data) and try to answer the question proposed by our AI advisor: “What is the distribution of review scores across different product categories?”

If you feel like skipping this exercise because you know how to make a bar chart of a single variable in Excel, you can skip it. We’re not rediscovering the wheel here. However, if you feel like spending a minute learning how generative AI can help you work on the granularity of your results, read on!

REPETITION IS A MOTHER OF LEARNING We previously wrote about the issues with how far back generative AI can reach in its conversation context analysis. Every now and then, you should clarify whether it remembers all the details correctly. If there is a problem, you can remind it of the full data description instead of correcting one variable after another.

Let’s see if generative AI will provide any helpful twists to this simple exercise. After jogging generative AI’s memory on the structure of the involved DataFrames (as presented in appendix A), we received the following answer to our question.

![](images/4962e46788cae99d58194cda9a4505512c7f8273fc0d3fc3c14fa4e02855dbd2.jpg)

How should I extract information on the distribution of review scores, and how does it vary across different product categories and sellers?

![](images/204f1fb3a6a50fb749784164d316dd173a0fcb9ef0eff873baf1fc36443381ba.jpg)

To analyze the distribution of review scores across different product categories and sellers, you can follow these steps:

1 Merge the required DataFrames: You may need to merge the reviews, orders, order\_items, and products DataFrames to obtain a combined DataFrame containing review scores, product categories, and seller information.   
2 Group the combined DataFrame by product categories and sellers: Use the groupby() function to group the data by product\_category\_name\_english and seller\_id.   
3 Calculate the distribution of review scores: Use the value\_counts() function to compute the count of each review score within each group.

Here’s the code to perform the above steps:

```txt
# Merge the DataFrames
merged_data = (
    df_orders.merge(df_order_items, on='order_id')
    .merge(df_products, on='product_id')
    .merge(df_order_reviews, on='order_id')
    .merge(df_product_category_translation, on='product_category_name')
) 
```

\# Group by product\_category\_name\_english, seller\_id, and review\_score review\_score\_distribution =

➥merged\_data.groupby(['product\_category\_name\_english', 'seller\_id', ➥'review\_score']).size().reset\_index(name='count')

Now, the review\_score\_distribution DataFrame contains the distribution of review scores for each combination of product category and seller. To visualize this data, you could use a stacked bar chart, heatmap, or other suitable visualization method, depending on your preference.

The code worked as advertised, but the problem is that we again beat our own record, and now we have a DataFrame with 14,503 rows. We’re going to need visualizations again if we’re to make any sense of this.

# MA

How should I visualize the review\_score\_distribution DataFrame to get to meaningful conclusions?

![](images/5a05c06a69f3dedab91c01e0feeffacc87f9be96da168ca5e7e52fe2c124b0ba.jpg)

For visualizing the review\_score\_distribution DataFrame, you can use a grouped bar chart, where the x-axis represents the product categories, the y-axis represents the count of reviews, and different colors or patterns represent the different review scores. This will allow you to see how review scores are distributed across product categories and compare their performance in terms of customer satisfaction.

Here’s a code snippet using Seaborn to create a grouped bar chart:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set a larger figure size
plt.figure(figsize=(20, 10))

# Create the grouped bar chart
sns.barplot(data=review_score_distribution,
    x='product_category_name_english',
    y='count',
    hue='review_score',
    ci=None)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Set labels for the axes and the title
plt.xlabel('Product Categories')
plt.ylabel('Review Count')
plt.title('Review Score Distribution by Product Category')

# Show the plot
plt.show() 
```

This plot will give you an idea of how different product categories perform in terms of customer reviews. Keep in mind that this plot might be quite large and hard to read depending on the number of product categories in your dataset. You may want to filter or aggregate the data further to focus on specific categories or review score ranges.

It looks like generative AI was able to estimate that the size of the results will be bigger than the previous ones. Figure 3.6 shows that it wasn’t wrong. At this time, the advised course of action would be a trip to a stakeholder, who will receive this analysis and a solid heart-to-heart. They could decide to accept the oversized chart and promise never to print it, or they could propose an aggregation meaningful to them.

![](images/125a8bcd3d1366b71ccb3fac10326a2fb78db4b37fcaf7d7352bd014424288e6.jpg)  
Figure 3.6 Grouped bar plot showing review score counts by product category

For the sake of argument, we will assume that this analysis is being prepared for an elevator pitch and, as such, cannot be approved in advance. Let’s divide the reviews into positive (4 or 5 points) and negative (1, 2, 3 points), with us arbitrarily deciding what scores are considered positive (and negative). Getting the code from generative AI is straightforward.

Listing 3.1 Generating a grouped bar plot   
```python
import seaborn as sns
import matplotlib.pyplot as plt

def categorize_review_score(score):
    if score >= 4:
    return 'Positive'
    else:
    return 'Negative'

review_score_distribution['review_category'] =
→ review_score_distribution['review_score'].apply(categorize_review_score)

# Set a larger figure size
plt.figure(figsize=(20, 10))

# Create the grouped bar chart
sns.barplot(data=review_score_distribution,
    x='product_category_name_english',
    y='count',
    hue='review_category',
    ci=None)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Set labels for the axes and the title
plt.xlabel('Product Categories')
plt.ylabel('Review Count')
plt.title('Simplified Review Score Distribution by Product Category')

# Show the plot
plt.show() 
```

As shown in figure 3.7, the result is a bit more readable than figure 3.6. With “bit” being the key word.

Simplified Review Score Distribution by Product Category   
![](images/d6b29f914b324070d08a5ba7f846f28fd55c2e17ef625da5f7f0fd2c882e4114.jpg)

<details>
<summary>bar</summary>

| Product Categories | Positive | Negative |
|---|---|---|
| agro_industry_and_commerce | 4 | 1.5 |
| air_conditioning | 3.5 | 1.8 |
| art | 4 | 3.2 |
| arts_and_craftmanship | 1.2 | 1.0 |
| audio | 6 | 3.0 |
| auto | 7 | 2.8 |
| baby | 27 | 12 |
| bed_bath_table | 6 | 1.8 |
| books_general_interest | 6.5 | 1.5 |
| books_imported | 6.5 | 1.3 |
| books_technical | 6.5 | 1.5 |
| cds_dvds_musicals | 6.5 | 0.8 |
| christmas_supply | 5 | 1.5 |
| cine_photo | 3.8 | 1.2 |
| computers | 16 | 6 |
| computers_accessories | 14.8 | 6.2 |
| consoles_games | 7.8 | 3.5 |
| construction_tools_construction | 4.5 | 2.8 |
| construction_tools_lights | 5.2 | 3.2 |
| construction_tools_safety | 3.5 | 2.3 |
| cool_stuff | 8.3 | 3.0 |
| costruction_tools_garden | 4.9 | 2.5 |
| costruction_tools_tools | 2.8 | 1.5 |
| diapers_and_hygiene | 1.5 | 3.5 |
| drinks | 7.2 | 3.5 |
| dvds_blu_ray | 5.7 | 1.2 |
| electronics | 11 | 5 |
| fashion_female_clothing | 3.3 | 1.3 |
| fashion_bags_accessories | 11.7 | 3.5 |
| fashion_children_clothes | 2.3 | 0.9 |
| fashion_male_clothing | 4.9 | 2.8 |
| fashion_shoes | 13.2 | 3.5 |
| fashion_sport | 2.0 | 1.2 |
| fashion_underwear_beach | 6.5 | 1.8 |
| fixed_telephony | 3.0 | 1.8 |
| flowers | 5.5 | 0.9 |
| food | 5.4 | 2.8 |
| food_drink | 5.4 | 1.8 |
| furniture_bedroom | 2.9 | 1.8 |
| furniture_decor | 12.7 | 5.4 |
| furniture_living_room | 5.4 | 2.6 |
| furniture_mattress_and_upholstery | 4.4 | 1.7 |
| garden_tools | 10.7 | 5.5 |
| health_beauty | 10.7 | 4.4 |
| home_appliances_2 | 9.2 | 5.7 |
| home_appliances_2 | 3.4 | 0.9 |
| home_comfort_2 | 3.4 | 0.9 |
| home_confort_2 | 11.3 | 7.2 |
| home_construction_2 | 5.4 | 2.8 |
| housewares_2 | 8.1 | 3.5 |
| industry commerce_and_business_2 | 6.0 | 3.0 |
| kitchen_dining_garden_furniture_2 | 3.0 | 1.8 |
| la_cuisine_2 | 3.4 | 2.8 |
| luggage_accessories_2 | 9.3 | 3.3 |
| market_place_2 | 3.4 | 1.8 |
| music | 1.3 | 1.8 |
| musical_instruments_2 | 5.7 | 1.8 |
| office_furniture_2 | 22.4 | 17.9 |
| party_supplies_2 | 1.9 | - |
| perfumery_2 | 11.1 | - |
| pet_shop_2 | 8.0 | - |
| security_and_services_2 | 0.9 | - |
| signaling_and_security_2 | 3.0 | - |
| small_appliances_2 | 4.0 | - |
| small_appliances_2 | 3.0 | - |
| small_appliances_home_oven_and_coffee_2 | 1.0 | - |
| sports_tleisure_2 | 10   | - |
| stationery_2 | 8.4 | - |
| tablets_printing_image_2 | 7   | - |
| telephony_2 | 16   | - |
| toys_2 | 9    | - |
| watches_gifts_2 | 30   | - |
The chart displays a vertical bar chart with two categories: 'Positive' and 'Negative'. The values for each category are explicitly labeled on the chart.
</details>

Figure 3.7 Grouped bar plot showing aggregated review score counts by product category

If it’s genuinely going to serve as an elevator pitch, we need to do better. That means we’ll need to aggregate product categories. However, our dataset doesn’t have an ontology categorizing products into even broader categories. Fortunately, generative AI is really good at providing first approximations in this type of task.

![](images/2f70ec4fbc53442748c941c9a2b2a8d7c8d763c504f03939a6134c24d5c19400.jpg)

I would like to add the aggregation by product category. Propose the grouping and explanation of the grouping decision for the following list of categories:

[<HERE WE PROVIDED A FULL LIST OF CATEGORIES>]

![](images/19ac4bd22d67e0c9531ae897f21a479200f5d16ea6f73561f3f343990edf8e6e.jpg)

One way to group the product categories is by considering their main industry or area of interest. This can make the visualization more manageable and reveal trends at a higher level. Here’s a proposed grouping for the given list of categories:

1 Home & Furniture: ['bed\_bath\_table', 'furniture\_bedroom', 'furniture\_ decor', 'furniture\_living\_room', 'furniture\_mattress\_and\_upholstery', 'kitchen\_dining\_laundry\_garden\_furniture', 'home\_confort', 'home\_ comfort\_2', 'home\_construction', 'housewares']   
2 Electronics & Computers: ['audio', 'computers', 'computers\_accessories', 'electronics', 'telephony', 'tablets\_printing\_image']   
3 Fashion: ['fashio\_female\_clothing', 'fashion\_bags\_accessories', 'fashion\_childrens\_clothes', 'fashion\_male\_clothing', 'fashion\_ shoes', 'fashion\_sport', 'fashion\_underwear\_beach']   
4 Entertainment: ['art', 'arts\_and\_craftmanship', 'books\_general interest', 'books\_imported', 'books\_technical', 'cds\_dvds\_musicals', 'christmas\_supplies', 'consoles\_games', 'cool\_stuff', 'cine\_photo', 'dvds\_blu\_ray', 'music', 'musical\_instruments', 'toys', 'watches\_ gifts']   
5 Sports & Leisure: ['sports\_leisure', 'garden\_tools']   
6 Health & Beauty: ['health\_beauty', 'perfumery']   
7 Baby & Kids: ['baby', 'diapers\_and\_hygiene', 'fashion\_childrens\_ clothes']   
8 Office & Industry: ['agro\_industry\_and\_commerce', 'industry\_commerce\_ and\_business', 'office\_furniture', 'stationery']   
9 Home Appliances: ['air\_conditioning', 'home\_appliances', 'home\_ appliances\_2', 'small\_appliances', 'small\_appliances\_home\_oven\_and\_ coffee']   
10 Tools & Construction: ['construction\_tools\_construction', 'construction\_ tools\_lights', 'construction\_tools\_safety', 'costruction\_tools\_ garden', 'costruction\_tools\_tools']   
11 Auto & Accessories: ['auto', 'fixed\_telephony']   
12 Food & Drink: ['food', 'food\_drink', 'drinks']   
13 Miscellaneous: ['flowers', 'la\_cuisine', 'luggage\_accessories', 'market\_place', 'party\_supplies', 'pet\_shop', 'security\_and\_- services', 'signaling\_and\_security']

You can create a new column in the review\_score\_distribution DataFrame to represent these groupings:

```python
def categorize_product_category(category):
    category_mapping = {
    'Home & Furniture': ['bed_bath_table', 'furniture_bedroom',
    'furniture_decor', 'furniture_living_room',
    'furniture_mattress_and_upholstery',
    'kitchen_dining_laundry_garden_furniture', 'home_confort',
    'home_comfort_2', 'home_construction', 'housewares'],
    # ... Include other mappings here ...
    }
    for key, values in category_mapping.items():
    if category in values: 
```

```txt
return key
return 'Unknown'
review_score_distribution['product_category_group'] =
→ review_score_distribution['product_category_name_english'].apply(
→ categorize_product_category) 
```

Now you can visualize the aggregated review score distribution for these groupings using a grouped bar chart or a stacked bar chart, as discussed earlier.

Our generative AI advisor presented an impressive level of understanding of the task. If you are interested in our discussion with ChatGPT on placing fixed\_telephony in “Auto & Accessories” and making it a complete category\_mapping dictionary, we propose reading appendix C.

As seen in figure 3.8, the result is much more comprehensible than previous versions.

Simplified Review Score Distribution by Product Category Group   
![](images/bce6e2f596d6fb1b4f4a03fefa893b34cc6577c8be57240aa003c26e1408807a.jpg)

<details>
<summary>bar</summary>

| Product Category Groups | Positive | Negative |
| :--- | :--- | :--- |
| Office&Industry | 9.5 | 5.6 |
| HomeAppliances | 4.8 | 2.1 |
| Entertainment | 10.2 | 4.2 |
| Electronics&Computers | 13.0 | 5.6 |
| Auto&Accessories | 6.5 | 2.8 |
| Baby&Kids | 7.0 | 3.3 |
| Home&Furniture | 12.2 | 5.8 |
| Tools&Construction | 4.4 | 2.5 |
| Food&Drink | 5.9 | 2.9 |
| Fashion | 9.7 | 3.1 |
| Miscellaneous | 6.7 | 2.7 |
| Sports&Leisure | 10.2 | 4.1 |
| Health&Beauty | 10.8 | 4.3 |
</details>

Figure 3.8 Grouped bar plot showing aggregated review score counts by product categories aggregated into product groups

Having secured analyzable results of the review score distribution, we can now move on to the last of the descriptive analyses—the description of order statuses and their distributions.

# 3.3.4 Order status

There are multiple reasons to research order statuses, from identifying problems with logging systems to improving the user experience. To answer the question, “How does the order status (e.g., delivered, shipped, etc.) vary across different regions, product categories, and sellers?” we will extract information about types of order statuses across categories and regions. Later, in section 3.4, we will do a more advanced regression analysis on delivery times.

This will be a recurring theme in your work. You will take a first glance at the data when cleaning it, a second during descriptive analytics, and sometimes then decide what data is rich enough to drive data modeling. This may seem inconsistent with our previous remarks about having a strict protocol, but that’s not the case. Your protocol should be flexible enough to allow for evaluation and decisions.

Generative AI will readily provide the code needed to merge the necessary Data-Frames to get the required information in one place, and then to group and analyze the data.

Listing 3.2 Preparing DataFrame with order statuses   
```python
import pandas as pd

orders_items = pd.merge(df_orders, df_order_items, on='order_id')

# Merge orders_items with df_products on 'product_id'
orders_items_products = pd.merge(
→orders_items, df_products, on='product_id')

# Merge orders_items_products with df_product_category_translation
→on 'product_category_name'
merged_data = pd.merge(orders_items_products,
→df_product_category_translation, on='product_category_name')

# Group by 'order_status', 'product_category_name_english',
→and 'seller_id', then count the occurrences
status_distribution = merged_data.groupby(['order_status',
→'product_category_name_english', 'seller_id']).size().reset_index(
→name='count')

# Sort the result by 'order_status', 'product_category_name_english',
→and 'count' in descending order
status_distribution_sorted =
→status_distribution.sort_values(['order_status',
→'product_category_name_english', 'count'], ascending=[True, True,
→False])

print(status_distribution_sorted) 
```

The code is simple enough to work without a hitch. A glance at the resulting Data-Frame shows that some orders have the status of approved but have apparently never shipped. This could be investigated further.

However, with a result including 7,524 rows, we need something worth a thousand words to analyze these results. Fortunately, in data analytics, as we prove over and over again, the power of generative AI goes way beyond code generation.

![](images/65306e5b9bda7640a178c12e789618d8dc08c44bb7365634271271be663e820b.jpg)

What type of visualization would you propose for the previously generated status\_ distribution\_sorted DataFrame?

![](images/f1d000f2b52fa6eb296ff83c41dfc5d125deb8e50fc2809c7e59a307f4b469d7.jpg)

For the status\_distribution\_sorted DataFrame, a stacked bar chart would be an appropriate visualization. This will allow you to display the distribution of order statuses for each product category while also making it easy to compare the total number of orders among product categories.

To create a stacked bar chart, we need to use the pandas plot function with the kind='bar', vstacked=True parameters. First, we need to reshape the status\_ distribution\_sorted DataFrame into a format suitable for creating a stacked bar chart.

Here’s the code to create the stacked bar chart for the status\_distribution\_ sorted DataFrame:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Pivot the DataFrame for the stacked bar chart
status_pivot =
→status_distribution_sorted.pivot_table(
→index='product_category_name_english',
    columns='order_status',
    values='count',
    aggfunc='sum',
    fill_value=0)

# Plot the stacked bar chart
plt.figure(figsize=(20, 10))
status_pivot.plot(kind='bar', stacked=True, figsize=(20, 10))

plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=12)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Count of Orders', fontsize=12)
plt.title('Order Status Distribution by Product Category', fontsize=14)
plt.legend(title='Order Status', title_fontsize=12, fontsize=10,
→loc='upper right')

plt.tight_layout()
plt.show() 
```

This code pivots the status\_distribution\_sorted DataFrame, creating a new DataFrame with the product categories as the index and order statuses as columns.

It then creates a stacked bar chart using the plot function with kind='bar' and stacked=True parameters. The remaining lines adjust the figure size, font size, and rotation of the x-axis labels for better readability.

The result of this code is presented in figure 3.9.

![](images/5080217bb7df729d2d10ad6ad6c5131bbb28cf84f73a85d0656382f15b49e50f.jpg)  
Figure 3.9 Stacked bar plot showing order status delivery counts per product category

Though it might be challenging to discern from the chart, due to its scale, the lion’s share of statuses are marked as “delivered,” irrespective of the product category. The occurrences of other statuses are minimal in comparison.

If we were to just going to generate another bar chart, we wouldn’t bother you with reading this section. Let’s try to go beyond the obvious and add our own twist to the question proposed by our AI advisor.

![](images/1484492c50def296f55cf288b1d9315a78e6414934927887b1ca7137f2c87186.jpg)

Are there any patterns in order delivery time based on the customer’s and seller’s location?

![](images/c3f8820a45dd7b950817bd607d0c9456bed01ec51621e83efd9065dd908a256c.jpg)

To analyze patterns in order delivery time based on customer’s and seller’s location, we can first calculate the delivery time for each order and then visualize the relationship between delivery time, customer’s location, and seller’s location.

1 Calculate delivery time:

We will use the df\_orders DataFrame and calculate the delivery time as the difference between order\_delivered\_customer\_date and order\_purchase\_ timestamp.

```python
import pandas as pd

df_orders['order_purchase_timestamp'] =
→pd.to_datetime(df_orders['order_purchase_timestamp'])
df_orders['order_delivered_customer_date'] =
→pd.to_datetime(df_orders['order_delivered_customer_date'])
df_orders['delivery_time'] = (df_orders['order_delivered_customer_date'] - 
→df_orders['order_purchase_timestamp']).dt.days 
```

2 Merge necessary columns from df\_customers and df\_sellers DataFrames with df\_orders:

```python
df_orders_customers = df_orders.merge(df_customers[['customer_id', 'customer_city', 'customer_state']], on='customer_id')
df_orders_customers_sellers =
df_orders_customers.merge(df_order_items[['order_id', 'seller_id']], on='order_id')
df_orders_customers_sellers =
df_orders_customers_sellers.merge(df_sellers[['seller_id', 'seller_city', 'seller_state']], on='seller_id') 
```

3 Visualize the relationship between delivery time, customer’s location, and seller’s location:

A suitable visualization method for this purpose is a scatter plot, where we can use the customer’s state and seller’s state on the x and y axes, respectively, and color the points based on the delivery time.

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 12))
sns.scatterplot(data=df_orders_customers_sellers, x='customer_state', y='seller_state', hue='delivery_time', palette='coolwarm', alpha=0.6)
plt.xlabel("Customer State")
plt.ylabel("Seller State")
plt.title("Delivery Time by Customer and Seller State")
plt.show() 
```

This visualization will help us identify any patterns or trends in delivery time based on the customer’s and seller’s locations. Keep in mind that this is a high-level overview, and further analysis may be required to draw more specific conclusions.

Interestingly, this time we received the end-to-end solution. From merging required DataFrames, to feature engineering (creating a completely new column), to visualization! That’s impressive.

In the notebook in our GitHub repository, you’ll notice that the initial visualization is less than impressive. The data distribution is clearly skewed toward low values, while high-value outliers “hijacked” the upper part of the color range, leaving the vast majority of results barely distinguishable. In addition, the order of regions on both axes is random. However, it wasn’t much work to get code to deal with these problems.

Listing 3.3 Creating a log-scaled heatmap   
```python
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

# Sort the data by customer_state and seller_state
df_sorted = df_orders_customers_sellers.sort_values(
    by=['customer_state', 'seller_state'])

# Create the scatter plot
plt.figure(figsize=(16, 12))

# Use LogNorm for color normalization
norm = mcolors.LogNorm(
    vmin=df_orders_customers_sellers['delivery_time'].min() + 1,
    vmax=df_orders_customers_sellers['delivery_time'].max())

plt.scatter(x=df_sorted['customer_state'], y=df_sorted['seller_state'],
    c=df_sorted['delivery_time'], cmap='coolwarm', alpha=0.6, norm=norm)

plt.xlabel("Customer State")
plt.ylabel("Seller State")
plt.title("Log-scaled Delivery Time by Customer and Seller State")
plt.colorbar(label="Delivery Time (log-scaled)")

# Get the unique state values and sort them
sorted_states = sorted(df_sorted['customer_state'].unique())

# Set the same order for both x and y axes
ax = plt.gca()
ax.set_xticks(range(len(sorted_states)))
ax.set_xticklabels(sorted_states)
ax.set_yticks(range(len(sorted_states)))
ax.set_yticklabels(sorted_states)

plt.show() 
```

Applying generative AI’s suggestion to use the logarithmic scale solved the “blueiness” problem we encountered, and the alphabetical order of regions makes finding relevant pairs much easier. As you can see in figure 3.10, the result is a perfectly analyzable image; we will conduct the analysis itself in chapter 4. For now, it’s enough to see that there are indeed differences in delivery times depending on the region.

![](images/e56b84d749270e6eb6c16eeb0f74be590961bdfc55c47a30c5ce904d4513fd4c.jpg)  
Figure 3.10 Scatterplot of delivery times from one state to another, colored by a log-norm scale, with identical order of elements on both axes

# “WHEN WE TALK ABOUT TASTES AND COLORS, THERE IS NOTHING TO BE DISPUTED”

Certain elements of human perception may be hard for a computer program to notice. If done properly, things like the distribution of colors or order of elements will enhance the human ability to absorb the information presented. You can try to get some theoretical background and sound advice from generative AI, but the responsibility for the clarity and readability of the final results is on you.

In this section, you learned that generative AI can provide you with the code required to perform all the necessary elements of descriptive analytics. It’s not error-free, but you must remember that LLMs do not run actual calculations or transformations, despite being computer programs. They generate answers based on their understanding of the language patterns involved in mathematical reasoning rather than by performing a numerical calculation. The accuracy of the provided answers depends on how well-represented related mathematical patterns are in the data they were trained on. However, descriptive analysis is relatively easy. Let’s see how well our AI advisor fares when facing more demanding tasks.

# 3.4 Inferential analysis

In the previous section, you mainly visualized data, grouping it this way or another along the way. Luckily (from the business decision-making perspective), or unluckily (from your workload perspective), there is more to descriptive analysis than bar and line charts. More even than scatterplots.

Imagine that your organization has recently implemented a novel marketing strategy aimed at increasing product sales. The plan was rolled out across several regions with distinct market dynamics and consumer behaviors. To evaluate the strategy’s effectiveness, you need to determine not only whether sales have increased postimplementation but also if the observed changes can be attributed directly to the marketing efforts rather than external factors or mere chance. Furthermore, you’re tasked with identifying which specific strategy elements were most effective in different regions and among various demographic groups.

The toolbox you need to open for more advanced problems is called inferential or inference statistics. Inference analysis is a branch of statistics that focuses on drawing conclusions about a population based on data obtained from a sample (inferring things about the population based on what you find in the sample—it does what it says on the tin, really). It is grounded in probability theory and employs various statistical tests and methods to estimate population parameters, test hypotheses, and assess the strength and direction of relationships between variables.

The following sections will test generative AI’s ability to guide us through this statistics-laced minefield.

# 3.4.1 Before you begin

Unfortunately, we need to put on our Don Quixote cap (or helmet) for a moment. The methods we will show you are not very popular, and you may rightfully ask yourself, why don’t we use methods we’ll find in most textbooks or websites? There are a couple of reasons for that.

First, we perceive our role as pointing you to ways of doing things right, where right means analyzing your data in a way that allows you to draw correct conclusions.

The second reason results from the availability of generative AI. Where previously you’d need to spend a considerable amount of time learning the intricacies of statistics to even begin to do things right, you now have, at your fingertips, all the required knowledge and a tool to parse and explain it to you in a way you’ll feel comfortable with. Plus, this tool will provide the complete code to perform the analysis as a bonus.

# THE IMPORTANCE OF USING CONFIDENCE INTERVALS IN INFERENCE ANALYSIS

In section 3.1, we mentioned that we disagree with generative AI’s popularity-based approach to selecting methods for evaluating the results of statistical analyses. We realize that for the majority of our readers, the concept on which we base the following analyses may be new, so we’ll present an overview here.

We already mentioned that the role of inference analysis is to draw conclusions about the population from the sample. Imagine we wanted to know the average monthly spending of our company’s customers on some product category (one they may also buy outside of our company). Since it’s not feasible to survey all our customers, we may decide to randomly select 100 customers and calculate their average spending. Let’s assume the result turned out to be \$200.

The sample might not perfectly represent our entire customer base. We would then calculate the confidence interval (CI) to account for potential variability. A 95% confidence interval for average monthly spending might be between \$180 and \$220. This means that we can be 95% confident that the true average spending of all customers on this product category lies within that range. In other words, if we repeat the sampling and CI calculation 100 times, 95 of the calculated confidence intervals will contain the true mean.

Confidence intervals offer certain advantages over more widely used null hypothesis significance testing (NHST), or p-value, as they provide a range of plausible values for the population parameter, allowing for a more comprehensive understanding of the effect size and its uncertainty.

Therefore, confidence intervals contribute to a better interpretation of the results and more informed decision-making. This is why, despite the general, popularitydriven consensus approach proposed initially by ChatGPT, we modified the proposed analysis design for the questions we will discuss in following subsections and explicitly asked our AI advisor to focus on methods utilizing confidence intervals.

# AN IMPORTANT NOTE ON THE COMPLETENESS OF THE DATA

We use inference statistics here because we know that the data we have is a sample of a bigger set. If you work with a full dataset, such as all the customers you have and all the transactions made, there is no need to calculate confidence intervals for the purpose of historical data analysis, as your sample is your population. However, inference statistics will come in handy if you want to use your data for any kind of predictive analytics.

We are now equipped to plunge back into analyzing our e-commerce data.

# 3.4.2 Relationship between product attributes and shipping costs

The question, “What is the relationship between product attributes (e.g., weight, dimensions) and overhead costs (e.g., shipping costs)?” posed by our AI advisor may seem a little naive, but it will help us build an intuition about the power of confidenceinterval–based linear regression. The importance of this tool is impossible to overestimate. You will encounter it when working in various fields:

 Economics—Economists use linear regression to understand the relationship between economic indicators, such as GDP growth and unemployment rates, or inflation and interest rates. Confidence intervals in these regressions help policymakers assess the reliability of these relationships when making fiscal or monetary policy decisions.   
 Finance—In finance, linear regression is used to model the relationship between the risk and return of assets, as described by the capital asset pricing model (CAPM). Analysts use confidence intervals to gauge the precision of beta coefficients, which measure the sensitivity of asset returns to market movements, thereby informing investment strategies.   
 Healthcare—Researchers employ linear regression to study the relationship between various risk factors (e.g., smoking, diet, physical activity) and health outcomes (e.g., heart disease, diabetes). Confidence intervals around the regression coefficients provide insights into the significance and reliability of these factors, guiding public health recommendations and patient treatment plans.   
 Marketing—Marketing analysts use linear regression to understand how different aspects of marketing strategies (e.g., advertising spend, promotional activities) influence sales or customer behavior. Confidence intervals help in assessing the strength of these relationships, optimizing marketing budgets, and tailoring strategies to maximize ROI.   
 Real estate—Linear regression models are used to predict property prices based on features such as size, location, and amenities. Confidence intervals around the predictions provide potential buyers and sellers with a range of expected prices, aiding in negotiation and decision-making processes.   
 Environmental science—Scientists apply linear regression to model the impact of human activities on environmental indicators, such as CO2 emissions and global temperature rise, or the effect of environmental variables on biodiversity. Confidence intervals help quantify the uncertainty in these models, crucial for environmental policy and conservation strategies.   
 Manufacturing—In the manufacturing sector, linear regression is used to model the relationship between production processes (e.g., temperature, pressure, material properties) and product quality or yield. Confidence intervals allow engineers to understand the variability in these processes and to optimize them for better outcomes.   
Education—Researchers use linear regression to explore the impact of educational interventions (e.g., class size, teaching methods, technology use) on student performance. Confidence intervals provide a measure of the effectiveness and reliability of these interventions, informing educational policy and practice.   
 Sports analytics—Linear regression is applied in sports analytics to evaluate the performance of players based on various metrics (e.g., scoring, defensive actions) and their impact on game outcomes. Confidence intervals around these estimates help teams make strategic decisions about player training and game tactics.

 Technology and innovation—In technology companies, linear regression can analyze the relationship between features of a product or service and user engagement or satisfaction. Confidence intervals around these relationships guide product development, feature prioritization, and customer experience strategies.

In our opinion, quantitatively checking how much one thing depends on the other is irreplaceable in any decision-making process. Fortunately, generative AI can help you go through the whole process quickly and efficiently.

# MA

How can I check if there is a relationship between product attributes (e.g., weight, dimensions) and shipping costs?

![](images/47d33139654fcc2604fb0479c4608bb03b4e1719c24f166fc848c94b26aa7b9a.jpg)

To investigate the relationship between product attributes (e.g., weight, dimensions) and shipping costs, you can use a linear regression model with confidence intervals. First, let’s combine the necessary data from the df\_products and df\_order\_items DataFrames:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table

# Merge the DataFrames
merged_df = df_order_items.merge(df_products, on="product_id", how="left")

# Calculate product volume
merged_df["product_volume"] = merged_df["product_length_cm"] *
merged_df["product_height_cm"] * merged_df["product_width_cmalar"
# Filter out the relevant columns
analysis_df = merged_df[
["freight_value", "product_weight_g", "product_volume"]]
# Remove rows with NaN values
analysis_df = analysis_df.dropna() 
```

Next, let’s build a linear regression model for each of the product attributes (weight and volume) against the shipping cost (freight value):

```python
# Linear regression for weight
X_weight = sm.add_constant(analysis_df["product_weight_g"])
y = analysis_df["freight_value"]
model_weight = sm.OLS(y, X_weight).fit()

# Linear regression for volume
X_volume = sm.add_constant(analysis_df["product_volume"])
y = analysis_df["freight_value"]
model_volume = sm.OLS(y, X_volume).fit() 
```

Now, you can visualize the relationships and their confidence intervals:

```python
# Function to plot regression line with confidence interval
def plot_regression_with_ci(X, y, model, xlabel, ylabel):
    fig, ax = plt.subplots() 
```

```python
sns.regplot(x=X.iloc[:, 1], y=y, ax=ax, scatter_kws={'alpha': 0.3})
st, data, ss2 = summary_table(model, alpha=0.05)
predicted = data[:, 2]
upper = data[:, 4]
lower = data[:, 5]
ax.plot(X.iloc[:, 1], predicted, '-', lw=2, color='red',
    ➔label='Fitted Line')
ax.fill_between(X.iloc[:, 1], lower, upper, color='red', alpha=0.15,
    ➔label='95% CI')
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend()
plt.show() 
```

```python
# Plot the relationship between weight and freight value
plot_regression_with_ci(X_weight, y, model_weight,
    xlabel="Product Weight (g)", ylabel="Freight Value") 
```

```txt
# Plot the relationship between volume and freight value
plot_regression_with_ci(X_volume, y, model_volume,
→xlabel="Product Volume (cm³)", ylabel="Freight Value") 
```

By examining the plots and their 95% confidence intervals, you can determine whether there’s a relationship between the product attributes and shipping costs. A narrow confidence interval around the fitted line indicates a stronger relationship between the variables, while a wider interval suggests more uncertainty in the relationship.

Our AI advisor proposed a complete solution. It engineered the required DataFrame, built regression models, and proposed a visualization of results. The latter turned out to be way more cluttered than we could hope, but it is presented in figure 3.11 nevertheless.

![](images/49e1cb08281ca401eca38e9f9a1ff4a26b817c5a00bc61bdadf38c1267175a68.jpg)

<details>
<summary>scatter</summary>

| Product Weight (g) | Freight Value |
| ------------------ | ------------- |
| 0                  | 0             |
| 5000               | 50            |
| 10000              | 100           |
| 15000              | 150           |
| 20000              | 200           |
| 25000              | 250           |
| 30000              | 300           |
| 35000              | 350           |
| 40000              | 400           |
</details>

a

![](images/6bc8b5c379db8cea427f3783422b66a204d20b68dcdbe86b311cb3ee9bcf2d3d.jpg)

<details>
<summary>scatter</summary>

| Product Volume (cm³) | Freight Value |
| --------------------- | ------------- |
| 0                     | 0             |
| 50000                 | 100           |
| 100000                | 200           |
| 150000                | 300           |
| 200000                | 400           |
| 250000                | 350           |
| 300000                | 300           |
</details>

b   
Figure 3.11 Scatterplot of the relationship between (a) freight value and product weight, and (b) freight value and volume

There are interesting vertical lines of data points at 30,000 g and $2 5 { , } 0 0 0 ~ \mathrm { c m ^ { 3 } }$ in figure 3.11. We guess it’s caused by some standard package sizes used by delivery companies across Brazil.

The other thing worth discussing is that the confidence interval is so narrow that it’s not even visible in the picture. That means, from the statistical point of view, that the line most likely is where we drew it—we have so much data that we can be sure about our estimation’s precision. That doesn’t mean this regression is immediately useful, though.

The results are spread wide around the regression line. Its predictive power seems to be low, to say the least. If we have a package of 20 kg, for example, we can estimate its freight value to be anywhere between 0 and 200 BRL (it’s our assumption that that’s the monetary unit the data provider uses).

HOW MUCH WOOD WOULD THE WOODCHUCK CHUCK? The main value of regressions is their ability to predict dependent variables based on a set of independent variables. To assess the performance of a regression model, we may employ various metrics, such as mean absolute error (MAE), mean squared error (MSE), root mean squared error (RMSE), and $\mathrm { R ^ { 2 } }$ (coefficient of determination). These metrics provide insights into the model’s accuracy, the magnitude of the errors, and the proportion of the variance in the dependent variable explained by the independent variables. Additionally, residual analysis and diagnostic plots can be used to examine the model’s assumptions, such as linearity, homoscedasticity, and the normality of residuals.

We promised you a quantitative analysis of the dependency, and we’re not going to stop at drawing a chart this time. These are several commonly used metrics that you’ll want to look at when analyzing regression data (especially in the context of its predictive power):

 Mean absolute error (MAE)—The average of the absolute differences between predicted and actual values. It gives an idea of how wrong the predictions are. A smaller MAE indicates better predictive performance.   
Mean squared error (MSE)—The average of the squared differences between predicted and actual values. It tends to penalize large errors more than small ones. A smaller MSE indicates better predictive performance.   
Root mean squared error (RMSE)—The square root of the MSE. It has the same units as the dependent variable and is more interpretable than the MSE. A smaller RMSE indicates better predictive performance.   
 $R ^ { 2 } { - } R ^ { 2 }$ measures the proportion of variance in the dependent variable that can be explained by the independent variable(s). A higher $\mathrm { R ^ { 2 } }$ value indicates better predictive performance.

As usual, accepting the help of generative AI is the quickest way to get code that calculates all of these values.

Listing 3.4 Predicting product weight or volume influence on freight value   
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error,
    r2_score

# Split the data into features (X) and target (y)
X_weight = analysis_df["product_weight_g"].values.reshape(-1, 1)
X_weight = sm.add_constant(X_weight) # Add a constant for the intercept
X_volume = analysis_df["product_volume"].values.reshape(-1, 1)
X_volume = sm.add_constant(X_volume) # Add a constant for the intercept
y = analysis_df["freight_value"].values

# Predict the target variable using the models
y_pred_weight = model_weight.predict(X_weight)
y_pred_volume = model_volume.predict(X_volume)

# Calculate the evaluation metrics for both models
mae_weight = mean_absolute_error(y, y_pred_weight)
mse_weight = mean_squared_error(y, y_pred_weight)
rmse_weight = np.sqrt(mse_weight)
r2_weight = r2_score(y, y_pred_weight)

mae_volume = mean_absolute_error(y, y_pred_volume)
mse_volume = mean_squared_error(y, y_pred_volume)
rmse_volume = np.sqrt(mse_volume)
r2_volume = r2_score(y, y_pred_volume)

# Print the evaluation metrics
print(f"Product Weight Model: MAE={mae_weight:.2f}, MSE={mse_weight:.2f},
    RMSE={rmse_weight:.2f}, R2={r2_weight:.2f}")
print(f"Product Volume Model: MAE={mae_volume:.2f}, MSE={mse_volume:.2f},
    RMSE={rmse_volume:.2f}, R2={r2_volume:.2f}") 
```

The proposed code should provide us with the following result:

```txt
Product Weight Model: MAE=6.89, MSE=156.77, RMSE=12.52, R2=0.37
Product Volume Model: MAE=7.41, MSE=163.70, RMSE=12.79, R2=0.34 
```

The results show that just about 35 percent of the variability in the freight value is explained by product weight or volume. It may be interesting to see if combining the two would increase the available predictive power.

Listing 3.5 Predicting product weight and volume influence on freight value   
```python
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Merge the DataFrames
merged_df = df_order_items.merge(df_products, on="product_id", how="left")
# Calculate product volume
merged_df["product_volume"] = merged_df["product_length_cm"] *
→merged_df["product_height_cm"] * merged_df["product_width_cm"] 
```

```python
# Filter out the relevant columns
analysis_df = merged_df[["freight_value", "product_weight_g", "product_volume"]]
# Remove rows with NaN values
analysis_df = analysis_df.dropna()

# Define the independent variables (weight and volume)
and the dependent variable (freight value)
X = analysis_df[['product_weight_g', 'product_volume']]
y = analysis_df['freight_value']

# Add a constant for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Print the summary
print(model.summary()) 
```

The results may seem a bit daunting, but if you feel daring, generative AI should help you understand all of the following parameters.

OLS Regression Results 

<table><tr><td>Dep. Variable:</td><td>freight_value</td><td>R-squared:</td><td>0.399</td></tr><tr><td>Model:</td><td>OLS</td><td>Adj. R-squared:</td><td>0.399</td></tr><tr><td>Method:</td><td>Least Squares</td><td>F-statistic:</td><td>3.744e+04</td></tr><tr><td>Date:</td><td>Sun, 09 Apr 2023</td><td>Prob (F-statistic):</td><td>0.00</td></tr><tr><td>Time:</td><td>15:38:56</td><td>Log-Likelihood:</td><td>-4.4203e+05</td></tr><tr><td>No. Observations:</td><td>112632</td><td>AIC:</td><td>8.841e+05</td></tr><tr><td>Df Residuals:</td><td>112629</td><td>BIC:</td><td>8.841e+05</td></tr><tr><td>Df Model:</td><td colspan="3">2</td></tr><tr><td>Covariance Type:</td><td colspan="3">nonrobust</td></tr></table>

<table><tr><td></td><td>coef</td><td>std err</td><td>t</td><td>P&gt;|t|</td><td>[0.025</td><td>0.975]</td></tr><tr><td>const</td><td>13.7268</td><td>0.044</td><td>314.740</td><td>0.000</td><td>13.641</td><td>13.812</td></tr><tr><td>product_weight_g</td><td>0.0016</td><td>1.63e-05</td><td>101.023</td><td>0.000</td><td>0.002</td><td>0.002</td></tr><tr><td>product_volume</td><td>0.0002</td><td>2.61e-06</td><td>70.759</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Omnibus:</td><td colspan="2">105287.730</td><td colspan="2">Durbin-Watson:</td><td colspan="2">1.815</td></tr><tr><td>Prob(Omnibus):</td><td colspan="2">0.000</td><td colspan="2">Jarque-Bera (JB):</td><td colspan="2">12678300.032</td></tr><tr><td>Skew:</td><td colspan="2">4.145</td><td colspan="2">Prob(JB):</td><td colspan="2">0.00</td></tr><tr><td>Kurtosis:</td><td colspan="2">54.311</td><td colspan="2">Cond. No.</td><td colspan="2">3.37e+04</td></tr></table>

# Notes:

[1] Standard Errors assume that the covariance matrix of the errors ➥is correctly specified.   
[2] The condition number is large, 3.37e+04. This might indicate ➥that there are strong multicollinearity or other numerical problems.

NOTE You can learn a lot about the measurements and parameters used in statistics from the perspective of someone dealing with money, rather than basic science, from Mostly Harmless Econometrics by Joshua Angrist and Jörn-Steffen Pischke (Princeton University Press, 2009).

The critical information here should be $\mathbf { R } ^ { 2 } ,$ which tells you that almost 40% of the variability in freight value can be explained by product weight and volume variability. This means that by controlling and optimizing these two variables, you can impact the freight value. If the freight value is an essential factor of the overall cost of the product, this result could lead to the conclusion that it would be worth trying to reduce the weight or size of products without reducing their functionality or quality. This could lead to freight cost savings.

BEGGARS CAN’T BE CHOOSERS As we explained in chapter 2, the quality of results depends heavily on the quality and accessibility of data. Given a choice, you should avoid proposing business solutions based on data with the spread seen in figure 3.11. The observed effects are also not too significant. However, the key phrase is “given a choice.” Sometimes you will not have any better data, and your business may require any support it can get. Relying on even imperfect results like these may mean the difference between letting the business sink and giving it a fighting chance.

We will spend a bit more time drawing conclusions from this result in chapter 4. For now, we’ll turn our attention back to the review score.

# 3.4.3 Relationship between product, transaction, shipping attributes, and the review score

Your boss would be proud of you if they saw you doing what we will do in this section— merge the three research questions proposed by our AI advisor into one:

“What factors (e.g., delivery time, price, product attributes) contribute to differences in the average review score?”   
 “How do different payment methods and the number of payment installments affect order completion rates and customer satisfaction?”   
 “What is the impact of delivery time (actual vs. estimated) on customer satisfaction and review scores?”

The method of answering them is identical, so why waste time (which is money) doing the same work three times? Well, that would only work if you don’t care too much about the reliability and accuracy of the results. That’s an important lesson: even if you technically can do something, it doesn’t mean you should.

LESS IS MORE In regression analysis, you could hope that the more independent variables you drop into the model, the better the result, but that is not necessarily the case. Too many variables may muddy the water, so to speak, as they can result in either overfitting the model or causing issues related to multicollinearity. Overfitting means your model starts to fit the noise, rather than the underlying patterns, and it usually occurs when you have too many parameters in relation to the number of observations. Multicollinearity occurs when two or more predictor variables are highly correlated—the estimated coefficients may then become unstable and sensitive to minor changes in the data. This instability makes it difficult to reliably interpret which variables are genuinely impactful and how much they contribute to explaining the dependent variable.

We have only limited information on the product and transaction process. We also know already that the majority of transactions are finished when they are delivered. This should prepare us not to expect great success in finding a correlation between these factors and the level of happiness expressed by the customers in their reviews. However, we think the techniques for investigating such relationships are worth learning about.

![](images/97834e5316455a9813f38b06ccdea09333d070e28d266a2fbbdefd0b5df6b592.jpg)

What inferential statistics should I use to research how the average review score varies across different product categories, and what factors (e.g., delivery time and its difference vs. estimation, price, product, and payment attributes) contribute to these differences?

![](images/f6fa8f1f985afa801d7bf2d7f71f47481cb4c2ba7de86d0964ae96f6c9c6dca2.jpg)

To use inferential statistics to research how the average review score varies across different product categories and how factors like delivery time, price, and product attributes contribute to these differences, you can follow these steps:

1 Prepare the data:

a Create a DataFrame containing the necessary columns: product category, review score, delivery time, price, and product attributes (e.g., weight, dimensions).   
b Merge the necessary DataFrames to obtain this information.   
c Ensure there are no missing values and convert categorical variables to numerical format if required.

2 Perform ordinal logistic regression:

a Since the review score is an ordinal variable (1-5), you can use ordinal logistic regression to model the relationship between the review score and the factors of interest (product category, delivery time, price, and product attributes).   
b To do this, you can use the mord.LogisticAT model from the mord package.

3 Fit the model:

a Split the data into training and testing sets.   
b Fit the ordinal logistic regression model on the training data.

4 Evaluate the model:

a Use the model to predict the review scores on the test data.   
b Calculate the accuracy of the predictions using a confusion matrix and other metrics like precision, recall, and F1-score.   
c Analyze the model’s coefficients to determine the importance of each factor in predicting the review score.

Here’s a sample code to help you get started:   
```python
import pandas as pd
import mord
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# Prepare the data (assuming you have already merged necessary
→DataFrames into analysis_df)

# Convert categorical variables to numerical format if required
# (e.g., using pd.get_dummies() for product categories)

# Split the data into training and testing sets
X = analysis_df.drop("review_score", axis=1)
y = analysis_df["review_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
→random_state=42)

# Fit the ordinal logistic regression model
model = mord.LogisticAT(alpha=0)
model.fit(X_train, y_train)

# Predict the review scores on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the predictions
print("Accuracy:", accuracy_score(y_test, y_pred))

# Display the confusion matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Analyze the model's coefficients
print("Coefficients:\n", model.coef_) 
```

With this approach, you can explore the relationship between the average review score and various factors using ordinal logistic regression.

If the comment in the code saying “assuming you have already merged necessary DataFrames into analysis\_df,” was not a red flag for you, we’ve done a poor job so far. Whenever you see any assumptions on the part of the generative AI, you need to shiver, curse under your breath, and double-check them. We won’t include the whole conversation we had, trying to specify what generative AI hallucinated analysis\_df to be. You can see the final code in listing 3.6.

Listing 3.6 Preparation of the analysis\_df DataFrame   
```python
# Merge df_products with df_product_category_translation
products_merged = pd.merge(
    df_products, df_product_category_translation, on='product_category_name')

# Merge df_orders with df_order_items
order_items_merged = pd.merge(df_orders, df_order_items, on='order_id')

# Merge the resulting DataFrame with df_customers
order_customer_merged = pd.merge(
    order_items_merged, df_customers, on='customer_id') 
```

```python
# Merge the resulting DataFrame with products_merged
order_product_merged = pd.merge(
→order_customer_merged, products_merged, on='product_id')

# Merge the resulting DataFrame with df_sellers
order_seller_merged = pd.merge(
→order_product_merged, df_sellers, on='seller_id')

# Merge the resulting DataFrame with df_order_reviews
order_review_merged = pd.merge(
→order_seller_merged, df_order_reviews, on='order_id')

# Merge the resulting DataFrame with df_order damages
analysis_df = pd.merge(
→order_review_merged, df_order damages, on='order_id')

# Calculate delivery time in days
analysis_df['delivery_time'] =
→(analysis_df['order_delivered_customer_date'] -
→analysis_df['order_purchase_timestamp']).dt.days

# Calculate the difference between actual vs. estimated delivery time
analysis_df['delivery_time_misestimation'] =
→(pd.to_datetime-analysis_df['order_estimated_delivery_date']) -
→pd.to_datetime(analysis_df['order_delivered_customer_date']).dt.days

# Calculate product volume
analysis_df['product_volume'] = analysis_df['product_length_cm'] *
→analysis_df['product_height_cm'] * analysis_df['product_width_cm']

# Apply one-hot encoding to the payment_type column
payment_type_dummies = pd.get_dummies(
→analysis_df['payment_type'], prefix='payment_type')

# Concatenate the one-hot encoded columns with analysis_df
analysis_df = pd.concat([analysis_df, payment_type_dummies], axis=1)

# Drop unnecessary columns
analysis_df.drop(columns=['product_category_name', 'order_approved_at',
→'order_delivered_carrier_date', 'order_estimated_delivery_date',
→'shipping_limit_date', 'review_creation_date',
→'review_answer_timestamp', 'order_id', 'customer_id', 'order_status',
→'order_purchase_timestamp', 'order_delivered_customer_date',
→'order_item_id', 'product_id', 'seller_id',
→'product_category_name_english', 'seller_zip_code_prefix',
→'seller_city', 'seller_state', 'review_comment_message',
→'review_comment_title', 'review_id', 'product_length_cm',
→'product_height_cm', 'product_width_cm', 'customer_unique_id',
→'customer_zip_code_prefix', 'customer_city', 'customer_state',
→'payment_type'], inplace=True)

analysis_df = analysis_df.dropna() 
```

The DataFrame resulting from the preceding code will be devoid of all unnecessary information about identifiers, geographic locations, and timestamps, as they will not be used in this particular analysis and would be unnecessary noise. We want to focus on variables of interest and their impact on review score.

The result of the logistic regression analysis is relatively easy to read.

Accuracy: 0.43035067573535907

Confusion Matrix:

```txt
[ [ 385 70 401 1637 1302]
[ 38 13 71 563 513]
[ 55 16 109 1342 1365]
[ 49 18 100 2909 3501]
[ 54 23 208 8021 11200]]
coefficients:
[-4.92618413e-02 1.63964377e-03 3.08760598e-03 1.38901936e-02
1.93889038e-05 4.21370114e-01 -8.75650964e-06 3.59787432e-01
2.93638614e-02 -1.72296023e-03 2.82130024e-02 9.50451240e-07
1.32936583e-01 2.23209948e-01 1.31639907e-02 -5.95202359e-03]
```

This accuracy means that you can explain 43% of the variability in review scores.

RIGHT ON THE MONEY? Misinterpretation or overestimation of a model’s accuracy can be very costly. A confusion matrix is a table layout that visualizes the performance of a classification algorithm, typically used in supervised learning. In binary prediction, it displays the number of correct and incorrect predictions made by the model, comparing them to the actual outcomes. The matrix is organized into four quadrants representing true positives (TP), true negatives (TN), false positives (FP; also known as type I errors), and false negatives (FN; also known as type II errors). By assessing the matrix, we can estimate the rate of type I errors, which occur when the model incorrectly classifies a positive instance as negative, and type II errors, which occur when the model incorrectly classifies a negative instance as positive. You’ll find more information on error types in chapter 5.

In a multivariate confusion matrix, such as the preceding one, each row represents the actual class, while each column represents the predicted class. The elements on the main diagonal of the matrix correspond to the correctly classified instances for each class, while the off-diagonal elements indicate misclassifications. To get a better intuition, let’s take a look at our classification of reviews and focus on the third column in the matrix, representing predictions of score three. In 109 cases, the classifier correctly assigned the score. It also misclassified 71 actual threes as twos, 401 as ones, 100 as fours, and 208 as fives.

To make analysis easier, let’s ask generative AI for the code linking the received result with the remaining variables.

# Listing 3.7 Connecting prediction results with variable names

\# Assuming you have already fitted the model and have the \`model\` variable ➥as the instance of the fitted model, e.g., model = mord.LogisticAT().fit(X\_train, y\_train)

```python
# Get the feature names from the analysis_df DataFrame
# Replace 'X' with the actual variable name containing your
→independent variables
feature_names = X.columns

# Get the coefficients from the model
coefficients = model.coef_

# Create a dictionary to link the coefficients to the column names
coefficient_dict = dict(zip(feature_names, coefficients))

# Print the coefficients along with the corresponding column names
for feature, coef in coefficient_dict.items():
    print(f"{feature}: {coef}") 
```

The preceding code snippet should work as advertised and return us this simple answer:

```yaml
delivery_time: -0.04926184129232652
price: 0.0016396437688542174
freight_value: 0.003087605979194856
product_name_lenght: 0.013890193611842357
product_description_lenght: 1.938890383573905e-05
product_photos_qty: 0.4213701136980763
product_weight_g: -8.756509636657266e-06
payment_sequential: 0.35978743241417466
payment_installments: 0.02936386138061978
payment_value: -0.001722960231783981
delivery_time_misestimation: 0.02821300240733595
product_volume: 9.504512398147115e-07
payment_type_boleto: 0.1329365830670677
payment_type_credit_card: 0.22320994812520034
payment_type_debit_card: 0.013163990732791755
payment_type_voucher: -0.005952023594428278 
```

The interpretation of coefficients resulting from the ordinal regression is similar to the interpretation of results we obtained from the linear regression, if not so straightforward. The resulting numbers represent the change in log-odds of being in a higher category of the outcome variable for a one-unit increase in the corresponding predictor variable, holding other variables constant. In simpler terms, when we’re predicting something with a specific order, like “low,” “medium,” and “high,” the coefficients give us information about how our prediction changes with input changes.

For example, let’s say we want to predict a happiness level based on how many hours you sleep. The coefficient would tell us how much the odds of being “more happy” (moving up a level from “low” to “medium” or “medium” to “high”) change for each extra hour of sleep you get. All of this is assuming that nothing else in your environment has changed. So, if the number (coefficient) is positive, that means getting more sleep increases the odds of being “more happy.” If it’s negative, more sleep decreases the odds. The bigger the number, the stronger the effect.

From the research perspective, it’s not ideal to evaluate sleep’s influence on your happiness if the increased sleep results from holidays from stressful work. Still, we’re not always given perfect testing conditions. The method described here could allow you to identify the influence of sleep if you provide multiple conditions and your mood record as input.

We will discuss how our coefficients translate to business insights in chapter 4.

# 3.4.4 Differences in sales performance and customer satisfaction between sellers

In this section, our focus will be on the differences between groups of sellers. We’ll try to answer the question, “are there any significant differences in sales performance and customer satisfaction between sellers from different cities or states?”

As it’s later in the chapter and you may be eager to move on to the next one, let’s take a look at where this approach could be successfully applied. Who knows, maybe something here will be of interest to you:

 Healthcare performance analysis—Comparing patient outcomes (e.g., recovery rates, satisfaction scores) between different hospitals or healthcare providers to identify quality disparities and areas for improvement.   
 Educational achievement gaps—Analyzing differences in student performance (e.g., test scores, graduation rates) across schools or districts to uncover educational inequalities and target interventions.   
 Marketing campaign effectiveness—Evaluating the impact of different marketing campaigns across regions or demographics to determine which strategies are most effective in enhancing brand awareness or sales.   
 Human resource management—Comparing employee satisfaction and performance metrics across different company locations or departments to identify best practices and areas needing attention.   
Financial services comparison—Analyzing loan approval rates or default rates across different branches to assess risk management effectiveness and customer service quality.   
 Supply chain efficiency—Comparing delivery times or inventory turnover rates across different distribution centers to optimize logistics and supply chain management.   
 Product quality control—Analyzing return rates or customer complaints for products manufactured at different facilities to identify quality control issues.   
 Environmental policy impact—Comparing pollution levels or conservation outcomes across regions before and after the implementation of environmental policies to assess their effectiveness.   
 Retail chain performance—Evaluating sales volumes or customer loyalty scores across different store locations to identify high-performing stores and understand factors contributing to their success.   
 Public policy and social programs —Assessing the effectiveness of social programs (e.g., unemployment aid, public health initiatives) in different communities by comparing outcome metrics like employment rates or health indicators.

Before we jump into the analysis, we need to expose you to the method called bootstrapping.

Bootstrap methods are a powerful resampling technique you can use to estimate confidence intervals, especially when the underlying data distribution is unknown or difficult to determine analytically. The bootstrap approach involves generating multiple random samples with replacements from the original dataset, each of the same size as the original sample. This means that while constructing each sample, every data point from the original dataset can be selected multiple times, and the number of data points in each new sample matches the number in the original dataset. A statistic of interest (e.g., mean, median, or regression coefficient) is calculated for each generated sample. These calculated statistics form a bootstrap distribution for estimating the population parameter’s confidence interval. A bootstrap distribution is essentially a frequency distribution of a statistic—like the mean or a regression coefficient—computed across multiple resampled datasets.

What does this mean in practice? Imagine you work for a company manufacturing extremely expensive equipment, such as quantum electronics. They need to make destruction tests to estimate safety parameters, such as the temperature the product can withstand. Destroying too many samples would literally bankrupt them, but let’s assume they can afford to overheat 50 pieces of equipment. The engineers run the test 50 times and come to you with 50 breakpoint temperatures. The reliability of a simple average calculation isn’t sufficient to satisfy the needs of clients, who want to know exactly how critical the cooling requirements are. Remember, we’re talking about huge costs for the products, but also huge costs for ensuring safe operational requirements. Safety margins are good and nice, but widening them too much can make your product unfeasible for clients.

Enter bootstrapping. You create “new” test batches by randomly selecting 50 scores from your original test results, with replacement. In other words, some scores may be selected multiple times and others not at all, simulating a new batch of tests under identical conditions. You repeat this resampling process many times—let’s say 10,000 times—each time calculating the average score of the resampled batch. This extensive repetition produces a wide range of possible breakpoint temperatures, reflecting the natural variability in your equipment’s durability. The collection of these 10,000 breakpoint temperatures forms your bootstrap distribution. This distribution gives you a statistical model of what the average durability score for your quantum electronics equipment might look like, based on your actual testing data. Given this bootstrap distribution, you can determine the middle 95% (or 99%, or 99.9%) of the average breakpoint temperatures as your confidence interval. This interval provides a statistically sound estimate of where the true average breakpoint temperature of your equipment lies, offering insights into its performance and how it might hold up in realworld use.

The bootstrap method shines in situations where traditional assumptions (like the normal distribution of the data) may not hold, or where sample sizes are too small to rely on the asymptotic properties of estimators (e.g., the simple calculation of a mean). Here are a few examples:

 Startup performance metrics—Early-stage startups often have limited data on customer behavior, revenues, or engagement metrics. Bootstrap methods can help estimate the variability and confidence intervals of key performance indicators (KPIs) like average revenue per user (ARPU) or customer lifetime value (CLV), providing valuable insights for decision-making despite small sample sizes.   
 Drug efficacy in clinical trials—In clinical trials, especially early-phase trials with small sample sizes, the distribution of treatment effects can be skewed or multimodal due to heterogeneous responses among participants. Bootstrap methods allow for the estimation of confidence intervals around the median treatment effect or other non-normally distributed outcomes, offering a more robust understanding of the drug’s efficacy.   
 Environmental impact studies—Environmental data, such as pollution levels or species counts, often exhibit skewed distributions due to the presence of extreme values (e.g., very high pollution levels on certain days). Bootstrap methods can provide reliable confidence intervals for median pollution levels or mean species counts, which are more informative and robust for policymaking than simple means.   
 Economic policy evaluation—Evaluating the impact of economic policies on outcomes such as employment rates or GDP growth often involves dealing with complex, non-normal distributions of effects across different regions or industries. Bootstrap confidence intervals can offer a more nuanced understanding of policy impacts, helping policymakers identify the range of potential outcomes and the reliability of estimated effects.

In each of these scenarios, the bootstrap method’s ability to provide reliable confidence intervals without relying on strict assumptions about the data’s distribution is invaluable. It allows researchers and practitioners to draw more confident conclusions from their data, even in challenging analytical contexts.

Let’s move from quantum electronics and economic policies into more commonly encountered customer satisfaction issues. In the case of customer satisfaction, you will often operate on opinions collected from just a sample of the total number of customers. Only some customers will leave a review or answer a survey. Businesses should know, reliably, their customers’ opinions across different categories.

Chapters 5 and 6 will discuss analyzing the reviews’ texts. Here, we’ll ask generative AI to prepare bootstrap-based confidence intervals for two numerical values important from the business perspective: average price and average customer review.

We will limit our attention to a single category of products. From the computational perspective, it doesn’t matter if we drop in the whole DataFrame or a filtered selection. We would like, however, to point your attention to the importance of the business meaning of the analysis. In a real-life scenario, even selecting a single category—in our case, “health and beauty”—wouldn’t be granular enough. Luxury and commodity products differ greatly in both prices and expectations. Mixing them does not offer sufficient insight into the market situation. Mixing them all together with car sales would muddy the waters even more, don’t you think?

Let’s get to the code.

Listing 3.8 Calculating confidence intervals for sales and review scores by state   
```python
# Prepare datasets
# Merge df_products with df_product_category_translation
products_merged = pd.merge(
    df_products, df_product_category_translation, on='product_category_name')

# Merge df_orders with df_order_items
order_items_merged = pd.merge(df_orders, df_order_items, on='order_id')

# Merge the resulting DataFrame with df_customers
order_customer_merged = pd.merge(
    order_items_merged, df_customers, on='customer_id')

# Merge the resulting DataFrame with products_merged
order_product_merged = pd.merge(
    order_customer_merged, products_merged, on='product_id')

# Merge the resulting DataFrame with df_sellers
order_seller_merged = pd.merge(
    order_product_merged, df_sellers, on='seller_id')

# Merge the resulting DataFrame with df_order_reviews
order_review_merged = pd.merge(
    order_seller_merged, df_order_reviews, on='order_id')

# Merge the resulting DataFrame with df_order Instructions
analysis_df = pd.merge(
    order_review_merged, df_order Instructions, on='order_id')

# Choose a specific product category to analyze
product_category = "health_beauty"
filtered_df = analysis_df[
    analysis_df['product_category_name_english'] == product_category]

# Group the data by seller state or city, and calculate
the metrics of interest
grouped_data = filtered_df.groupby('seller_state')
group_metrics = grouped_data.agg(
    {'price': ['sum', 'mean', 'count'], 'review_score': 'mean'})
# Calculate the standard deviations
group_metrics['price', 'std'] = grouped_data['price'].std()
group_metrics['review_score', 'std'] = grouped_data['review_score'].std()

# Use bootstrapping to estimate the 95% confidence intervals for
the average sales revenue and average review score for each city or state 
```

```python
import numpy as np
# Bootstrap the confidence intervals
def bootstrap_CI(data, func, n_bootstraps=1000, ci=95, axis=0):
    """
    Generate a confidence interval for a given statistic using
    bootstrapping.

    Parameters:
    data (numpy.ndarray or pandas.DataFrame):
    The data to calculate the statistic from.
    func (callable): The function used to calculate the statistic.
    n_bootstraps (int): The number of bootstrap samples to generate.
    ci (float): The confidence interval percentage (e.g., 95 for a 95% CI).
    axis (int):
    The axis along which to apply the statistic function
    (0 for columns, 1 for rows).

    Returns:
    tuple: The lower and upper bounds of the confidence interval.
    """
    bootstrapped_statistics = []
    for _ in range(n_bootstraps):
    bootstrap_sample = np.random.choice(
    data, size=len(data), replace=True)
    bootstrapped_statistic = func(bootstrap_sample, axis=axis)
    bootstrapped_statistics.append(bootstrapped_statistic)

    lower_bound = np.percentile(bootstrapped_statistics, (100 - ci) / 2)
    upper_bound = np.percentile(
    bootstrapped_statistics, 100 - (100 - ci) / 2)

    return lower_bound, upper_bound

# Create a new DataFrame to store the confidence intervals
def calculate_ci(group):
    return pd.Series({
    'price_ci_lower': bootstrap_CI(group['price'], np.mean,
    n_bootstraps=1000, ci=95)[0],
    'price_ci_upper': bootstrap_CI(group['price'], np.mean,
    n_bootstraps=1000, ci=95)[1],
    'review_score_ci_lower': bootstrap_CI(group['review_score'],
    np.mean, n_bootstraps=1000, ci=95)[0],
    'review_score_ci_upper': bootstrap_CI(group['review_score'],
    np.mean, n_bootstraps=1000, ci=95)[1]
    })

ci_df = grouped_data.apply(calculate_ci)

# Create visualizations with error bars for the average sales revenue and
average review score by seller state.

def plot_error_bars_only(df, metric_name, ylabel='', title='', 
figsize=(10, 6)):
    fig, ax = plt.subplots(figsize=figsize) 
```

```python
x = np.arange(len(df.index))
y = df[metric_name + '_ci_lower'] + (df[metric_name + '_ci_upper'] - 
    df[metric_name + '_ci_lower']) / 2
yerr = (df[metric_name + '_ci_upper'] - 
    df[metric_name + '_ci_lower']) / 2

plt.errorbar(x, y, yerr=yerr, fmt='o', capsize=5, capthick=2,
    ecolor='black', elinewidth=2)

plt.xticks(x, df.index, rotation=90)
plt.xlabel('Seller State')
plt.ylabel(ylabel)
plt.title(title)
plt.grid(axis='y')

plt.show()

# Plot the confidence intervals
plot_error_bars_only(ci_df, 'price', ylabel='Average Sales')
plot_error_bars_only(ci_df, 'review_score', ylabel='Average Review Score') 
```

As you can see, going through data harmonization, statistical modeling, and visualization results in quite a substantial amount of code. Fortunately, generative AIs are capable of not only providing the code, but also commenting it in an informative way.

The confidence intervals calculated for our examples are presented in figure 3.12.

![](images/32b8092eba6634b58d69df54be3c4ae9de9d158c37a0cbe6fef8d0b3837e135d.jpg)

<details>
<summary>other</summary>

| Seller State | Average Sales |
| ------------ | ------------- |
| BA           | 120           |
| CE           | 450           |
| DF           | 110           |
| ES           | 150           |
| GO           | 120           |
| MA           | 80            |
| MG           | 140           |
| MS           | 190           |
| MT           | 90            |
| PE           | 30            |
| PR           | 200           |
| RJ           | 170           |
| RN           | -10           |
| RS           | 260           |
| SC           | 320           |
| SP           | 100           |
</details>

a

![](images/2f587f33bdb315c2dec47b1f44c71cd24ff965a3b812688af828262107ff0eae.jpg)

<details>
<summary>bar</summary>

| Seller State | Average Review Score |
| ------------ | -------------------- |
| BA           | 4.8                  |
| CE           | 4.7                  |
| DF           | 4.3                  |
| ES           | 3.2                  |
| GO           | 4.6                  |
| MA           | 4.0                  |
| MG           | 4.2                  |
| MS           | 5.0                  |
| MT           | 4.5                  |
| PE           | 3.3                  |
| PR           | 4.3                  |
| RJ           | 4.2                  |
| RN           | 5.0                  |
| RS           | 4.4                  |
| SC           | 4.1                  |
| SP           | 4.0                  |
</details>

b   
Figure 3.12 Confidence intervals of (a) the average sales price and (b) the review score, both per state

We would like to repeat that, while doing the full-scale analysis, you should prepare separate charts for each product category, or dig even deeper, to avoid comparing apples with oranges or visual clutter.

A WORD ON SOFTWARE EFFICIENCY There are two main elements of increasing program efficiency. One is to optimize code execution, and we write about that at length in chapter 7. The other one, oftentimes no less important, is the parameterization of the algorithm used. Bootstrap methods balance two main parameters: the number of resamplings and the accuracy of the confidence interval. If you analyze really big data, before you jump into the technical aspects of optimization, you should try to understand whether the parameters of the algorithm you are using don’t offer ways of getting to your goal faster. Or at least closer to your goal. That’s another bonus of learning about parameters—you can usually understand the results better if you know what the assumptions behind each of them are.

We can see some interesting differences in the results, but we’ll leave interpreting the results for chapter 4. For now, we would like to leave you with a riddle: Why, when working with our example, does it make sense to use bootstrapping and calculate confidence intervals for our prices, and why would it most likely not make sense if you worked with your business data?

Having read this section, you should now be able to use inferential statistics and its different methods in your analytical work. In this chapter, you broke down the data and identified multiple relationships between different parameters. You used different visualization tools, like heatmaps and scatter plots, as well as regression analysis, to see how some parameters correlate with others.

CORRELATION DOES NOT IMPLY CAUSATION Sleeping with shoes on correlates with headaches in the morning, ice cream sales correlate with violent crimes, hair color correlates with ice-skating skills. These examples demonstrate that seeing a correlation is just a first stop in explaining observed phenomena. Often the correlation is caused by a third factor influencing your observed parameters. Sleeping with shoes on and headaches go hand in hand with alcohol overuse, ice cream sales and violent crimes result from heat waves, while blond hair is more often found in countries where you can find ice outside every now and then. Never assume causation on the basis of observed correlation without identifying a logical link between the observations.

There are many more methods in descriptive analytics, but after reading this chapter, you should be able to use generative AI to quickly identify and implement the best analytical tools for your dataset. All you need to do is to honestly and precisely describe the data you have available, and as honestly and as precisely as you can (which could mean not at all!), describe the goal of your analytics.

You should also be aware of generative AI’s weaknesses. The most notable one is its tendency to hallucinate when asked about topics and data defined too long before the prompt. Also, the provided code always needs to be tested. Applying this “trust, but verify” approach, generative AI can substantially improve and accelerate your analysis process.

# Things to ask generative AI

 What research questions related to the provided data can be asked?   
 What analysis design would lead to answering the following question?   
 What statistical method is best to analyze <available data>?   
Provide me with code to <data transformation>.   
 How should I visualize <data structure>.   
Provide me with a solution answering the following question: . . .   
 Modify the code to change the visualization format.

# Summary

Generative AI may be excellent at suggesting proper analytical tools and providing end-to-end analytical strategies.   
 Generative AI will first suggest the most popular methods, but they can provide competent support in the implementation of more niche ones too.   
 Generative AI may supplement analysis with market-specific information.   
Feeding generative AI with results to get insights requires caution and sometimes re-engineering of the output.   
 Generative AI can offer sound business insights.   
 You need to control the context awareness of generative AIs and be wary of their hallucinations. Jog their memories from time to time.   
The code provided by generative AI needs careful testing.

# Using generative AI for result interpretations

# This chapter covers

Building analysis context for generative AI by building an analysis summary   
Ways to describe visual results to a language model   
 Using generative AI’s advice to connect analyses   
Interrogating generative AI for business conclusions of analysis results

In the previous chapter, you performed a number of descriptive analyses and ended up with quite a few charts and some statistical modeling parameters. Yay! You can now bag it all and send it to your boss, right? Maybe . . . Depends on your boss, really.

In your work, you may encounter different types of managers. Some will be really well-versed in analytics themselves, and you’ll be cooperating with them, learning a ton of useful stuff. They will accept your results and discuss assumptions and methods with you; they may ask you to do some analytics neither you nor your generative AI advisor expected in this context. All will be good. The kind of boss you need to be wary of is the type with an overinflated opinion about their analytical skills. We won’t dwell on this type, as dealing with these people is a matter of psychology, rather than data analytics.

The type relevant for this chapter are bosses who expect you not only to provide the results, but also to propose the interpretation. Some of them overlap with the first category we mentioned, and they want to help you understand the business better and grow as analysts. Others are too busy to be bothered with the trivial task of drawing business-critical conclusions. There is also a chance that you will be analyzing data for your own business (in this undoubtedly short period when your company won’t be able to hire dedicated analysts).

Regardless of the reason, you may find yourself in a situation where you’ll be scratching your head over the charts you prepared. To derive the most business value, you need to ensure that your interpretation of results is

 Holistic—When interpreting results, it’s important to look at the big picture. Make sure your conclusions from one set of data don’t clash with those from another. Consider all your findings together to get a full understanding of what the data is telling you.   
 Precise—Be careful not to stretch your interpretations beyond what the data actually shows. Stick to the facts and avoid making assumptions that the data doesn’t support. Remember, being accurate is more important than making the data seem more exciting or significant than it really is.   
 Well-communicated—Make sure you explain your findings in a way that everyone can understand, whether they’re a data expert or not. Use clear and simple language and visuals to share your insights. It’s all about making sure your audience can easily grasp and act on the information you provide.

Regarding the last point, you may be required to engage in some form of storytelling. (You can learn more about AI-powered storytelling from another excellent Manning book, aptly named Data Storytelling with Generative AI, by Angelica Lo Duca.) The narrative-building skills are beyond the scope of this book, but in the other two aspects of your interpretation, generative AI can help you. This chapter will cover how to get helpful advice, from interpreting charts to enhancing results with a meaningful business context.

# 4.1 Problem definition

In previous chapters, we asked our generative AI advisor about the structure of the analytical process and about its implementation details, including writing the code. We then put real-life business data through the pipeline we created and got a handful of results. However, there is currently one big limitation of utilizing generative AIs for interpreting results: most of our results are in graphical format, while the large language models (LLMs) discussed here are, as the name suggests, language models, and as such excel at text-oriented tasks.

Multimodal generative AIs allow you to upload your images for analysis. However, we have discovered that the precision required to register visually minute differences between bar heights, for example, isn’t there yet. We will be limited to describing the generated charts and asking for help in their interpretation. If we want to fully utilize generative AI’s power, we need to provide our AI advisor with a proper context.

![](images/cc7e438d708ae8f3959d82048ca70196ff3fa17d11429c822130ec6a4c0b361c.jpg)

I performed a series of analyses on Brazilian e-commerce portal data. These include:

1 Descriptive analysis of:

– the popularity of product categories per state, resulting in the heatmap of product categories on the y-axis, states on the x-axis, and value of sales as a value in cells);   
– performance of products in categories and regions, resulting in:

a a matrix scatterplot of average payment value, average freight value, and average product price against each other   
b grouped barplot showing the relation of average product price per category per region.

review score distribution by product category, resulting in a grouped barplot showing review score counts by product category

– order status, resulting in:

a stacked barplot showing order status delivery counts per product category,   
b scatterplot of delivery times from one state to another

2 Inferential analysis (based on confidence intervals)

– Relationship between product attributes and the shipping costs resulting in two scatterplots and fitted regression line:

a the scatterplot of freight value to product weight   
b the scatterplot of freight value to product volume   
c model summary

– Relationship between product and shipping attributes, and the review score, resulting in model accuracy, confusion matrix, and coefficients of logistic ordinal regression for a list of parameters, namely delivery\_time, price, freight\_value, product\_name\_lenght, product\_description\_lenght, product\_photos\_qty, product\_weight\_g, payment\_sequential, payment\_ installments, payment\_value, delivery\_time\_misestimation, product\_ volume, payment\_type\_boleto, payment\_type\_credit\_card, payment\_ type\_debit\_card, payment\_type\_voucher;

Differences in sales performance and customer satisfaction between sellers, resulting in a series of visualizations of confidence intervals of:

a average sales prices of a selected product category in different states,   
b average review score of a selected product category in different states.

In the next prompts, I will ask you some questions about interpreting results and possible business-related conclusions.

All the models we tested reacted with unwavering enthusiasm and tried to manage expectations, explaining what we can derive from different analyses and warned that due to the limited ability to pass precise results, we should take their opinions with a pinch of salt. Great suggestion, if we ever heard one!

# 4.2 Popularity of product categories

In section 3.3 of the previous chapter, you generated visualizations showing the breakdown of sales volume by state and product category. Let’s look again at the revenue heatmap from figure 3.3, presented here as figure 4.1.

![](images/73cb57b0200dc8685ba28708027cd6b0aeb6cad8999aec8560dc89be2b9dd03a.jpg)  
Figure 4.1 Heatmap of sales volume by product category and state

We can see that there are differences between states and product categories. Before we describe what we see to our AI advisor and check if it can provide any advice in return, let’s talk about the usefulness of heatmaps for business decision-making.

People, in general, have a pretty weak visual memory. That is the main reason why we repeated this image instead of just reminding you of its number in the previous chapter, or even just describing it. For that reason, it is really hard to compare multiple disconnected charts. Before you turn your attention to a new visualization, the old one starts to fade from your memory. It is of great importance to put all the relevant data in a decision-maker’s field of view. That is the reason behind the (deserved) popularity of all flavors of dashboards.

Heatmaps put hundreds of data points related to relations between categories into your field of view. However, the idea is not to go one-by-one. You can, of course, do that if you wish. But before getting into the fine details, you may want to take a broader look and search for certain patterns:

 Points of high performance (single cells of exceptionally high value) —Identifying points of high performance through heatmaps enables the discovery of regions where specific product categories excel, highlighting a strong alignment between consumer demand and product offerings. For example, the robust sales of gifts and watches in affluent regions may reflect a high-income consumer base with a preference for luxury items, while the widespread use of mobile internet among younger demographics could indicate a prime market for electronic devices. Such insights are invaluable for businesses looking to refine their strategies. Recommendations might include expanding the luxury product portfolio in affluent areas to tap into the high-income market or launching targeted marketing campaigns aimed at young consumers to enhance the visibility and appeal of tech gadgets. By leveraging data to pinpoint areas of exceptional fit between products and consumer segments, businesses can craft targeted strategies that capitalize on these opportunities, driving sales and fostering growth.

 Points of low performance (single cells of exceptionally low values)—Identifying points of low performance on heatmaps can reveal where certain product categories underperform in specific regions, signaling a mismatch between offerings and local market needs or preferences. For instance, the struggle of high-end electronics in rural areas might suggest a gap between product pricing and local purchasing power, while low engagement with online education platforms among older demographics could indicate barriers such as digital literacy or accessibility. On the basis of these insights, businesses should consider diversifying their product range or developing targeted initiatives, like outreach programs, to better engage these underrepresented consumer segments and enhance overall market performance.

 Unique category performance (lower or higher category performance across multiple crosscategories)—Trends of over- or underperformance that emerge across multiple cross-categories (e.g., a region of higher performance across multiple product categories) can offer a broad view of market dynamics, including economic factors or cultural influences shaping consumer behavior. For example, the consistent demand for outdoor and fitness products in coastal regions reflects a lifestyle preference, whereas the popularity of educational materials in areas with numerous educational institutions might highlight a community’s educational values. Recognizing these patterns enables businesses to fine-tune their inventory and marketing strategies, such as introducing a wider variety of lifestyle products in coastal areas or engaging in collaborative marketing with educational institutions in academic hubs, thereby leveraging regional strengths to boost sales and customer engagement.

Emerging hotspots (cells that become high-value over time)—The concept of emerging hotspots, where specific regions begin showing increased sales for certain product categories over time, highlights areas of growing market opportunity. This trend, best observed by comparing heatmaps across different time periods, indicates shifts in consumer needs or interests. A notable increase in home office equipment sales in suburban areas could reflect an adaptation to remote work trends, while a surge in health and wellness products in cities may point to a rising health consciousness among urbanites. Businesses that quickly adapt to these trends by stocking up on in-demand products and creating targeted marketing campaigns can seize growth opportunities, establishing a strong presence in emerging markets.

 Seasonal shifts (variations in patterns at different times of the year)—Seasonal shifts in product popularity, discernible through the analysis of heatmaps across various times of the year, underscore the influence of factors like weather, holidays, or academic calendars on consumer purchasing behavior. The spike in air conditioning unit and beachwear sales during the summer in warmer regions, or the increased demand for stationery and educational books during back-to-school seasons, exemplifies how seasonality affects shopping patterns. Aligning inventory planning and promotional activities with these seasonal trends is essential for businesses. Anticipating and responding to seasonal demand ensures that businesses can capture the peak sales potential, optimizing revenue generation throughout the year.

By identifying these insights and offering them as a foundation of strategic decisionmaking, you can help your business better align its product offerings, marketing efforts, and inventory management with regional consumer behaviors and market dynamics or enhance customer engagement through personalized experiences, optimize supply chain efficiency to reduce overhead costs, foster innovation in product development by identifying unmet needs, and drive sustainable growth by entering new markets with confidence.

The key to success, however, is not only to notice what happens but to understand why. Let’s try to inquire if generative AI advisors are capable of helping us interpret our Brazilian e-commerce-derived heatmap. This is the question we posed:

![](images/6ed237fd9db7f4088f6d21412ca21004bbac98d3c8d65cd90b44020756708ae8.jpg)

I look at a heatmap presenting sales revenue broken by the state where the sales had taken place and product categories sold. I can see that some states (e.g., SP) have much higher average sales than others - we’re talking about an order of magnitude difference. Some states have near-zero sales (e.g., RR, AP). I can also see differences between product categories. “Auto,” “Health and beauty,” and “Watches gifts” are much more popular than “Music” or “Fashion children’s clothes”. How should I interpret my results, and what actions could be taken to improve our business?

To that, we received the following answer from ChatGPT 4:

![](images/b154a7482f9fa8aacb48b9132d4ced7ac369ef2970517e47738cb9805f5c3ddb.jpg)

Your observations from the heatmap highlight significant regional and categoryspecific variations in sales performance within the Brazilian e-commerce landscape. Here’s how to interpret these results and potential actions for business improvement:

Interpretation:

1 Regional Sales Variance:

a High Sales in SP (São Paulo): São Paulo’s high sales volume could be attributed to its status as a major economic hub with higher population density, greater purchasing power, and possibly better logistics infrastructure. This suggests both a high demand and an efficient fulfillment capability.   
b Low Sales in RR (Roraima), AP (Amapá): The near-zero sales in these states might reflect several factors, including lower population density, potentially lower economic activity, or challenges in logistics and delivery infrastructure that make it difficult to serve these markets effectively.

2 Category Popularity:

a “Auto,” “Health and Beauty,” and “Watches Gifts” Popularity: These categories’ success might be driven by broader market trends, consumer preferences, or perhaps your platform’s competitive pricing, assortment, and marketing effectiveness in these segments.   
b Lower Popularity of “Music” and “Fashion Children’s Clothes”: These categories might be facing stiff competition from specialized platforms, digital streaming for music, or simply not aligning with consumer demand or preferences as well as other categories.

Actions for Business Improvement:

1 Regional Tailoring and Expansion Strategies:

a Enhance Focus on High-Performance States: For states like SP, consider doubling down on marketing efforts, expanding the product range, and enhancing logistics to capitalize on high demand.   
b Market Development in Low-Performance States: For states with low sales, conduct market research to understand barriers to entry and consumer needs. Consider targeted marketing campaigns, partnerships with local businesses, or logistical adjustments to improve market penetration.

2 Category-Specific Strategies:

a Capitalize on Popular Categories: Further invest in the “Auto,” “Health and Beauty,” and “Watches Gifts” categories by expanding product lines, offering promotions, and employing targeted marketing to leverage their popularity.   
b Revitalize Underperforming Categories: For categories like “Music” and “Fashion Children’s Clothes,” consider revisiting your product range, pricing strategy,

and marketing efforts. Partnerships with popular brands, influencers, or exclusive deals could also reignite interest in these categories.

3 Customized Marketing and Promotions: Use the data to tailor marketing campaigns and promotions to specific states and product categories. This could involve personalized email marketing, regional advertising campaigns, or special promotions for regions or categories that are lagging.   
4 Logistics and Delivery Optimization: Investigate the feasibility of improving logistics and delivery services in underperforming states. This could involve exploring new shipping partners, optimizing delivery routes, or offering incentives for faster delivery options to enhance customer satisfaction and increase sales.   
5 Continuous Monitoring and Adjustment: Regularly review sales data and customer feedback to quickly identify shifts in consumer behavior or market dynamics, allowing for rapid adjustment of strategies.

By tailoring your approach to capitalize on strengths and address weaknesses highlighted by your analysis, you can drive sales growth, improve market penetration, and enhance customer satisfaction across regions and product categories.

The Gemini Advanced generative AI provided the following on state-wise sales:

![](images/f1836b369ae3b8cb258fe869136d05067eafbf8f14269bade5b74b061e2e972b.jpg)

High vs. Low Sales States: The significant difference in sales revenue between states like SP and others like RR and AP indicates uneven geographic distribution. This could be due to various factors, including:

a Population density: States with higher populations are likely to have more potential customers.   
b Economic factors: States with higher disposable income might see increased spending on e-commerce.   
c Marketing reach: Your marketing efforts might not be reaching all states equally.   
d Product-market fit: The product categories you offer might not be as relevant to the needs and preferences of certain states.

Product Category Popularity:

a High vs. Low Popularity Categories: The difference in popularity between categories like “Auto” and “Music” suggests varying customer demand across different categories.

# Potential Actions:

1 Address the Uneven Geographic Distribution:

a Analyze customer demographics: Understand the demographic factors like age, income, and internet penetration in different states. This can help identify potential markets with untapped customer bases.   
b Targeted marketing: Tailor your marketing campaigns to specific states based on their demographics and product preferences.   
c Logistics optimization: Analyze shipping costs and delivery times across different states. Consider options like regional warehouses or partnerships with local delivery providers to improve efficiency and potentially lower costs in less populated areas.

2 Improve Product-Market Fit:

a Analyze category-specific sales trends: Investigate the performance of individual products within each category. This can help identify underperforming products within popular categories or potential for introducing new products in less popular categories that cater to specific state preferences.   
b Localized product offerings: Consider offering products tailored to the specific needs and preferences of different regions.   
c A/B testing: Test different marketing strategies and product offerings in different states to see what resonates best with local customers.

# Additionally:

Track the effectiveness of implemented actions: Monitor the impact of your changes on sales, customer satisfaction, and geographic distribution over time.   
Invest in customer relationship management (CRM): Build a strong customer base by collecting and analyzing customer data to understand their preferences and personalize their shopping experience.

By implementing these suggestions and continuously analyzing your data, you can gain valuable insights into your customer base and take targeted actions to improve your business performance across different regions and product categories.

The explanations provided by both of the generative AIs seem plausible, and the advice is worthy of a first-year marketing studies student. There is an important lesson to be learned here. Do you remember how we mentioned that your interpretation needs to be holistic, precise, and well-communicated? The reason behind the vagueness of these answers is a lack of detail in our prompt.

IMPOSSIBLE IS NOTHING The title of this callout is a blatant lie! The world of data analytics is full of limitations. In chapter 2, we explained how your analysis can only be as good as the data you have at your disposal. Generative AIs seem to be trained to respect such limitations and are reluctant to offer specific advice on the basis of vague data.

As a test, we uploaded into ChatGPT the whole table we built figure 4.1 on, but we didn’t get any business insights in response. Instead, we got a set of data processing and visualizing instructions very similar to what we did in chapters 2 and 3. While ChatGPT is capable of running a simple analysis on a limited dataset, deploying a fullblown, multistep analytical pipe still requires data analysts.

What can you do if you still want to get more specific answers for the business? Provide more data. Focus on regions or products to make the analysis more specific. As retyping the data from the chart doesn’t seem feasible, let’s ask a generative AI for code to provide revenue for each state.

# Listing 4.1 Creating a revenue by state table

\# Set your desired product category selected\_product\_category = 'your\_product\_category\_here'

```python
# Filter the revenue_df to get the row with the selected product category
category_data = revenue_df.loc[revenue_df['product_category'] == selected_product_category]

# Drop the product_category column to have only state-revenue pairs
state_revenue_pairs = category_data.drop(columns=['product_category'])

# Transpose the DataFrame and reset the index to have state and revenue as columns
state_revenue_pairs = state_revenue_pairs.T.reset_index()

# Rename the columns
state_revenue_pairs.columns = ['state', 'revenue']

# Display the state-revenue pairs for the selected product category
state_revenue_pairs 
```

Let’s use the code from the listing 4.1 and provide our AI advisors with the information on revenue by state. In our case, we’ll focus on the health and beauty category.

![](images/ec9b0ba5a37585efdbe5c3a2c2d664cf49839fab4459be6f495733b8e1b02a76.jpg)

For the health and beauty category, I got the following results in my analysis of revenue per Brazilian state:

AC 1386.58, AL 12780.26, AM 2776.03, AP 1380.58, BA 51367.91, CE 32419.18, DF 29862.82, ES 20214.49, GO 28312.30, MA 12747.18, MG 157558.30, MS 11289.57, MT 15301.79, PA 23755.83, PB 16286.98, PE 41604.78, PI 10290.19, PR 54949.36, RJ 145298.62, RN 13886.47, RO 7085.76, RR 1050.61, RS 51327.72, SC 39760.16, SE 8883.66, SP 462305.22, TO 4798.99

Use this data and information you have on Brazil, its geography, health and beauty market, the population of different states, and known differences in purchasing power in different states to help me draw business conclusions and advice from it.

ChatGPT 4 provided the following analysis:

![](images/a5d6f01f70384db1e83b871d13bef0f473a1519b7b4cebf5194afd0c31275083.jpg)

Based on the revenue data for the health and beauty category across Brazilian states and considering the country’s geography, population, and purchasing power differences, here are some business conclusions and recommendations:

1 Focus on high-revenue states: São Paulo (SP) and Rio de Janeiro (RJ) account for the largest shares of revenue. As these states have high population densities and purchasing power, it makes sense to concentrate marketing and promotional efforts in these areas to maximize sales.   
2 Cater to regional differences: Variations in revenue between states could be due to regional preferences, climate differences, and specific health and beauty concerns. Adjust product offerings to cater to these differences and create targeted marketing campaigns to resonate with regional audiences.   
3 Expand to emerging markets: States with lower revenues, such as Roraima (RR), Amapá (AP), and Acre (AC), might present untapped opportunities. Before expanding to these areas, research the local markets, considering factors like population, demographics, and purchasing power. To penetrate these markets, consider partnering with local retailers or leveraging e-commerce platforms.

4 Optimize distribution and logistics: Brazil’s large size and varying infrastructure can present challenges in product distribution. Focus on optimizing your supply chain and distribution network, especially in high-revenue states. Building strong relationships with local suppliers and distributors can help ensure timely and efficient delivery of products.   
5 Leverage digital marketing and e-commerce: Use online marketing and e-commerce platforms to increase reach, especially in states where revenue is currently low. A strong digital presence can help you connect with more customers, gain insights into their preferences, and drive sales.   
6 Analyze customer insights: Gather and analyze customer data and feedback to understand their preferences, needs, and regional trends better. Use this information to improve product offerings, marketing strategies, and customer experiences.   
7 Monitor competition and trends: Keep an eye on industry trends and competitor activities in the Brazilian health and beauty market. Stay ahead of the curve by adapting your strategies and product offerings accordingly.   
8 Invest in corporate social responsibility: Brazil’s diverse population cares about environmental and social issues. Investing in sustainable practices and supporting local communities can help improve your brand’s image and drive customer loyalty.

While these recommendations are based on the data provided and general knowledge of Brazil, it’s important to conduct further research and consider other factors like market size, competition, and economic conditions before making strategic decisions.

Gemini Advanced, in turn, generated the following:

![](images/1b8b499f6c23851088211bb171fc56b56c727e7881955b2de43ea1e90f715ddf.jpg)

 Concentration in Southeast and Northeast: The data reveals a significant concentration of sales in the Southeast (SP, RJ, MG, ES) and Northeast (BA, CE, PE) regions. This aligns with these regions having the highest populations in Brazil and potentially higher disposable income compared to other regions.   
Unexploited potential in North, Center-West, and some Southern states: While states like SP and RJ dominate sales, there seems to be untapped potential in the North (AC, AM, RO, RR), Center-West (DF, GO, MS, MT, TO), and some Southern states (SC, RS) where sales are considerably lower despite having decent populations.

Possible Reasons for Lower Sales:

Lower purchasing power: States with lower sales might have lower average incomes, limiting customer spending on non-essential items like health and beauty products.   
Limited marketing reach: Your marketing efforts might not be effectively reaching these regions, leading to lower brand awareness and customer acquisition.   
Product-market fit issues: The current product offerings might not cater to the specific needs and preferences of customers in these regions.

Actionable Recommendations:

 Targeted marketing: Increase marketing efforts in regions with lower sales, focusing on digital channels and strategies that resonate with the local population.

Consider using local influencers or tailoring messaging to address specific regional preferences.

Localized product offerings: Analyze local trends and preferences to understand what health and beauty products are most in demand in these regions. Consider introducing new products or adapting existing ones to cater to the local market.   
 Partnerships and distribution channels: Explore partnerships with local retailers or distributors to improve product availability and accessibility in these regions.   
Pricing strategies: Consider adjusting pricing strategies for specific regions, taking into account the purchasing power and local competition. However, be cautious about offering significant discounts as it could impact brand perception.

# Additional Considerations:

Logistics and delivery costs: Analyze the feasibility of expanding your reach to regions with lower sales by factoring in potential logistics and delivery cost increases.   
 Cultural factors: Be mindful of cultural factors and preferences that might influence consumer behavior in different regions.

By implementing these recommendations and continuously monitoring your results, you can expand your reach, improve market penetration, and potentially increase sales in the health and beauty category across various Brazilian states. Remember, it’s crucial to tailor your strategies to the specific characteristics and needs of each region for optimal results.

Some of the presented advice seems obvious, but some show a level of knowledge of the Brazilian market. Depending on the level of detail expected by your boss, you can either stop here or engage your generative AI advisor in a discussion about the details of each proposed solution.

GENERAL KNOWLEDGE VS. A SPECIALIZED TOOL ChatGPT 4, utilized in our system, is trained on an extensive data library, providing it with broad knowledge across various topics. However, it is essential to be aware that the nature of these models makes them generate the next token of the answer even if it leads to hallucinations. Therefore, verifying that the answers received are rooted in facts and evidence is crucial.

We conclude that you should ask your generative AI advisor for its opinion on analyzed topics. It may supplement your analytical effort with knowledge of business realities. Remember, some AIs can also use the internet to provide fresh data.

# 4.3 Performance of products in their categories and regions

The scatterplot we generated in chapter 3 when checking the performance of products in their categories and by region can be eye-glazing (figure 3.4). Let’s have a look at it again in figure 4.2.

Scatterplot Matrix of Average Values by State and Product Category   
![](images/ae20f4509532aad84fee452eaa8f709f8c15965efe545e1a1383b4569dcf517e.jpg)

<details>
<summary>scatter</summary>

| State | avg_product_price | avg_freight_value | avg_payment_value |
|-------|-------------------|-------------------|--------------------|
| AL    | 0                 | 0                 | 0                  |
| AP    | 0                 | 0                 | 0                  |
| BA    | 0                 | 0                 | 0                  |
| CE    | 0                 | 0                 | 0                  |
| ES    | 0                 | 0                 | 0                  |
| GO    | 0                 | 0                 | 0                  |
| MA    | 0                 | 0                 | 0                  |
| MG    | 0                 | 0                 | 0                  |
| MS    | 0                 | 0                 | 0                  |
| MT    | 0                 | 0                 | 0                  |
| PA    | 0                 | 0                 | 0                  |
| PB    | 0                 | 0                 | 0                  |
| PE    | 0                 | 0                 | 0                  |
| PI    | 0                 | 0                 | 0                  |
| PR    | 0                 | 0                 | 0                  |
| RJ    | 0                 | 0                 | 0                  |
| RO    | 0                 | 0                 | 0                  |
| RS    | 0                 | 0                 | 0                  |
| SC    | 0                 | 0                 | 0                  |
| SP    | 0                 | 0                 | 0                  |
| AM    | 0                 | 0                 | 0                  |
| DF    | 0                 | 0                 | 0                  |
| RN    | 0                 | 0                 | 0                  |
| TO    | 0                 | 0                 | 0                  |
| AC    | 0                 | 0                 | 0                  |
| RR    | 0                 | 0                 | 0                  |
| SE    | 0                 | 0                 | 0                  |
</details>

Figure 4.2 Scatterplot of relationships between average payment values, average freight values, and average product prices

At first glance, we can see that the relationship between product price and order value, described as avg\_payment\_value, is almost linear, while the relationship between freight value and other variables is not so much. Is that all that can be said from this figure? Let’s see what generative AI advises.

![](images/e0ed26cc1f1dc0449b1a0cbfd3f803d4878442f5d3ed8496bbfa4dba76632459.jpg)

What information or conclusions can I draw from the matrix of scatterplots showing pairwise relations between product prices, freight value, and order values?

![](images/72a7502cc307c81901beaa73ce98bc329f2a6794c3a69a1b686f90558dbf16a6.jpg)

A matrix of scatterplots showing pairwise relations between product prices, freight value, and order values can provide insights into the relationships between these variables and help you draw conclusions or identify trends. Here are some possible observations and conclusions:

1 Correlation between variables: Examine the direction and strength of the relationships between the variables. Positive correlations indicate that as one variable increases, the other tends to increase as well, while negative correlations indicate that as one variable increases, the other tends to decrease. Strong correlations might suggest that the variables influence each other or share a common underlying factor.   
2 Outliers: Identify any outliers that may affect the relationships between the variables. Outliers can be a result of data errors, unique circumstances, or genuine extreme cases. Investigate these outliers to understand their impact on your analysis and conclusions.   
3 Price sensitivity: Analyzing the relationship between product prices and order values can help you understand price sensitivity. If higher-priced products tend to have lower order values, it might indicate that customers are more price-sensitive and prefer more affordable products.   
4 Freight value impact: The relationship between freight value and order value can reveal how shipping costs influence customer purchasing behavior. If order values tend to decrease as freight values increase, it might indicate that customers are sensitive to shipping costs and prefer to purchase from sellers that offer lower freight values.   
5 Geographic factors: Comparing the scatterplot of freight value against product price or order value across different regions can highlight regional differences in shipping costs and customer preferences. It might be possible to identify areas where high freight values discourage customers from purchasing or where customers are more willing to pay higher shipping costs for specific products.   
6 Product categories: Analyzing the scatterplot matrix for different product categories can reveal category-specific trends and preferences. Some categories might have a stronger correlation between product price and order value, while others might show a more pronounced relationship between freight value and order value.   
7 Market segmentation: Based on the observed relationships between product prices, freight value, and order values, you can identify distinct market segments with different preferences and behaviors. This information can help you target your marketing efforts and tailor your product offerings to cater to these segments.

Remember that correlation does not imply causation. While the scatterplot matrix can help you identify patterns and relationships, it is essential to conduct further analysis and consider other factors before drawing definitive conclusions or making strategic decisions.

That is how far the GPT support can take us with the interpretation. It is now on us to painstakingly analyze each of the presented elements, like geographic factors or product categories. For the sake of brevity, we won’t go down this rabbit hole.

# 4.4 Review scores distribution analysis

In chapter 3, we prepared a bar chart of counts of positive and negative reviews per product category. If you are asking yourself why you should even read a discussion about bar charts, you’re not alone. At the beginning of our data journey, we wondered why we should prepare one. They seem so trivial. However, this section may be one of the most important in the book.

CLOTHES DON’T MAKETH THE MAN The business value of any analysis does not lie in its complexity. Write this in large letters on your office wall, and keep it in your field of view, not behind your back. Even if a method seems rudimentary, the insights derived from it may be anything but trivial. These insights may form the foundation of a data-informed strategy, guiding improvements, marketing, and operational decisions that can significantly impact a business’s success and customer satisfaction. By starting with this easy to understand analytical method, businesses can immediately dive deeper into the data, uncovering more nuanced insights and driving meaningful changes based on direct customer feedback.

While trying to make our analysis of the review scores more readable in chapter 3, we reduced the number of data points we visualized to a manageable number (originally shown in figure 3.8). The result is presented again in figure 4.3.

Simplified Review Score Distribution by Product Category Group   
![](images/d583d9a8a916f56d5d4ef0e70bac49e4650b1edb2d51a0744958355fc2c7a4e0.jpg)

<details>
<summary>bar</summary>

| Product Category Groups | Positive | Negative |
| :--- | :--- | :--- |
| Office&Industry | 9.5 | 5.6 |
| HomeAppliances | 4.8 | 2.2 |
| Entertainment | 10.2 | 4.2 |
| Electronics&Computers | 13.0 | 5.6 |
| Auto&Accessories | 6.5 | 2.8 |
| Baby&Kids | 7.0 | 3.3 |
| Home&Furniture | 12.2 | 5.8 |
| Tools&Construction | 4.4 | 2.5 |
| Food&Drink | 5.9 | 2.9 |
| Fashion | 9.7 | 3.1 |
| Miscellaneous | 6.7 | 2.7 |
| Sports&Leisure | 10.2 | 4.2 |
| Health&Beauty | 10.8 | 4.3 |
</details>

Figure 4.3 Grouped bar plot showing aggregated review score counts by product categories aggregated into product groups

At first glance, a grouped bar chart displaying counts of positive and negative reviews across different product categories may appear basic, but this simplicity belies its analytical power. By aggregating review scores into positive and negative categories and grouping them by product category, this chart distills complex consumer sentiment into an accessible, immediately understandable format. This clarity is not just about making data “easier” to digest; it provides a straightforward way to pinpoint areas of strength and weakness in a business’s product lineup at a glance.

One critical insight this type of analysis offers is the direct identification of product categories that excel in customer satisfaction versus those that may be underperforming. This can serve as a preliminary diagnostic tool: a high ratio of positive to negative reviews in a category suggests a strong market fit and customer approval, while a lower ratio might indicate areas where product or service improvements are necessary.

Moreover, this aggregated view allows businesses to benchmark performance across categories, fostering a competitive understanding internally and helping prioritize areas for strategic investment or product development. For instance, categories with high negative feedback might warrant further investigation into specific issues— be it product quality, customer expectations, or service delivery—providing actionable insights for targeted improvements.

Beyond immediate product improvement strategies, analyzing review scores in this manner can also influence broader business decisions. Positive review trends can guide marketing strategies, highlighting strong points to emphasize in promotional materials or identifying popular products to feature in campaigns. Conversely, understanding the nuances of negative feedback can inform not just product refinement but also customer service protocols, return policies, and even supply chain adjustments.

Expanding on the concept, this analytical approach isn’t limited to order reviews. Similar strategies can be applied to service evaluations, customer feedback on the shopping experience, and even employee satisfaction across different departments. Each application provides unique insights, from identifying best practices and areas of excellence to pinpointing challenges and opportunities for growth.

There is a catch, though. Did you notice that we sneaked an element important for deriving conclusions into the preceding description—one that is not directly visible in the chart? To evaluate market fit, you need to look not at bar heights but at their ratios. You could, of course, use a ruler, a piece of paper, a pen, and a calculator (optional), but that’s a suboptimal approach. Fortunately, your generative AI advisor can provide you with digital stationery.

In our experience, there is a useful lesson to learn here. Sometimes, you’ll follow your protocol and notice something interesting in one of the generated charts. If your deadline allows, you shouldn’t stick strictly to your protocol, and should instead take a look at the data from this new angle. The following example shows how you can quickly get the code needed to extract the data that interests you.

![](images/27a4ef278fbe8d27fa2a2cba2c2e931c9b38be7b1b4a9be3d2fc9a28e822e81d.jpg)

I have the following DataFrame review\_score\_distribution:   
```csv
product_category_name_english seller_id review_score count
review_category product_category_group
0 agro_industry_and_commerce 06579cb253ecd5a3a12a9e6eb6bf8f47 4 1
Positive Office & Industry
1 agro_industry_and_commerce 06579cb253ecd5a3a12a9e6eb6bf8f47 5 1
Positive Office & Industry
2 agro_industry_and_commerce 0ed6ce5d87fd9c69eaacaeb778d67235 4 1
Positive Office & Industry 
```

How can I get a list of values: product\_category\_group; review\_category; sum\_of\_counts

![](images/3019bfb1962b22379cd32c729eb1e3a00453b7174819c1ea16cb67f8749230d8.jpg)

You can use the pandas groupby() function to group the DataFrame by product\_- category\_group and review\_category, and then use the agg() function to calculate the sum of count. Here’s the code to do that:

```python
import pandas as pd
result =
review_score_distribution.groupby(['product_category_name_english', 'review_category']).agg({'count': 'sum'}).reset_index()
# Display the result
print(result) 
```

This code will give you a new DataFrame with the columns product\_category\_name\_english, review\_category, and the sum of count for each group.

As you can see, generative AI makes slicing and dicing the data easy. The resulting DataFrame allows you to easily work on grouped data. The next step is calculating the ratios of positive to negative reviews (and vice versa). This can be accomplished with a single line of code.

Listing 4.2 Calculating the positive to negative reviews ratios   
```txt
result['review_ratio'] = result.groupby('product_category_group')
[count'].transform(lambda x: x / x.sum())
    product_category_group review_category count review_ratio
0 Auto & Accessories Negative 965 0.229053
1 Auto & Accessories Positive 3248 0.770947
2 Baby & Kids Negative 790 0.255912
3 Baby & Kids Positive 2297 0.744088
4 Electronics & Computers Negative 4231 0.264124
5 Electronics & Computers Positive 11788 0.735876
6 Entertainment Negative 3844 0.225388
7 Entertainment Positive 13211 0.774612
8 Fashion Negative 579 0.218491
9 Fashion Positive 2071 0.781509
10 Food & Drink Negative 227 0.197220
11 Food & Drink Positive 924 0.802780
12 Health & Beauty Negative 2801 0.214373
13 Health & Beauty Positive 10265 0.785627 
```

<table><tr><td>14</td><td>Home &amp; Furniture</td><td>Negative</td><td>7842</td><td>0.276098</td></tr><tr><td>15</td><td>Home &amp; Furniture</td><td>Positive</td><td>20561</td><td>0.723902</td></tr><tr><td>16</td><td>Home Appliances</td><td>Negative</td><td>433</td><td>0.207276</td></tr><tr><td>17</td><td>Home Appliances</td><td>Positive</td><td>1656</td><td>0.792724</td></tr><tr><td>18</td><td>Miscellaneous</td><td>Negative</td><td>721</td><td>0.199061</td></tr><tr><td>19</td><td>Miscellaneous</td><td>Positive</td><td>2901</td><td>0.800939</td></tr><tr><td>20</td><td>Office &amp; Industry</td><td>Negative</td><td>1270</td><td>0.271832</td></tr><tr><td>21</td><td>Office &amp; Industry</td><td>Positive</td><td>3402</td><td>0.728168</td></tr><tr><td>22</td><td>Sports &amp; Leisure</td><td>Negative</td><td>2942</td><td>0.226849</td></tr><tr><td>23</td><td>Sports &amp; Leisure</td><td>Positive</td><td>10027</td><td>0.773151</td></tr><tr><td>24</td><td>Tools &amp; Construction</td><td>Negative</td><td>422</td><td>0.240593</td></tr><tr><td>25</td><td>Tools &amp; Construction</td><td>Positive</td><td>1332</td><td>0.759407</td></tr></table>

Some business stakeholders will prefer such results in the form of a table, so knowing how to use generative AI to pull out the required data from the charts is useful, especially if the charts were generated by someone else, and you drew the short straw of supplementing their work. It happens.

An image is worth a thousand tables for the other group of stakeholders. Again, modifying an existing chart using generative AI’s help is extremely simple.

Listing 4.3 Adding a line with ratios to an existing bar chart of review counts   
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Create a bar plot for counts
ax1 = sns.barplot(x="product_category_group", y="count", hue="review_category", data=result)

# Set x-axis label rotation
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)

# Remove gridlines for the primary axis
ax1.grid(False)

# Create a second y-axis
ax2 = ax1.twinx()

# Remove gridlines for the secondary axis
ax2.grid(False)

# Filter results for negative review_category
negative_results = result[result["review_category"] == "Negative"]

# Create a line plot for negative review ratios
ax2 = sns.lineplot(x="product_category_group", y="review_ratio", data=negative_results, ax=ax2, marker="o", color="red")

# Set y-axis labels
ax1.set_ylabel("Count")
ax2.set_ylabel("Negative Review Ratio") 
```

```python
# Set the legend
ax1.legend(title="Review Category", loc="upper left")
ax2.get_legend().remove()

# Show the plot
plt.show() 
```

We will ignore the error related to library syntax and focus on the result presented in figure 4.4.

![](images/8e5c694e4d6b3733ad0124dd7ea71ed9edce3362ccb54b84b8dbee6817023b95.jpg)

<details>
<summary>bar_line</summary>

| product_category_group | Negative Count | Positive Count | Negative Review Ratio |
| :--- | :--- | :--- | :--- |
| Auto&Accessories | 1000 | 3000 | 0.23 |
| Baby&Kids | 800 | 2200 | 0.25 |
| Electronics&Computers | 4000 | 11700 | 0.26 |
| Entertainment | 3600 | 13100 | 0.22 |
| Fashion | 600 | 1900 | 0.22 |
| Food&Drink | 300 | 800 | 0.20 |
| Health&Beauty | 2700 | 10100 | 0.21 |
| Home&Furniture | 7800 | 20500 | 0.28 |
| HomeAppliances | 500 | 1500 | 0.21 |
| Miscellaneous | 700 | 2800 | 0.20 |
| Office&Industry | 1200 | 3300 | 0.27 |
| Sports&Leisure | 2900 | 9900 | 0.23 |
| Tools&Construction | 500 | 1300 | 0.24 |
</details>

Figure 4.4 Grouped bar plot showing aggregated review score counts by product categories aggregated into product groups, with a line indicating the ratio of negative reviews to positive

For some categories, you can see a really high number of positive reviews. Others clearly present a high ratio of negative reviews. It’s important to note the scale on the right side. In this case, the differences in absolute values are not as dramatic as might be assumed from their amplitude on the chart. The raw number of reviews (both positive and negative) is a result of the high number of purchases in the category, so the ratio is a much better approximation of the relative happiness of customers with these purchases. A word of warning, though: if the raw number of reviews is really low, the ratio might not be representative.

We do realize that a similar result could easily be achieved in Excel. We performed this exercise because avoiding moving data between environments is very important. Copying and pasting is inherently risky—columns get merged or split, formulas get overwritten with raw data, and formats get mixed (especially for dates). Our guess is that many of our readers could turn this list of potential problems into a small book.

# 4.5 Order status

We approached this part of the analysis with real curiosity. The interpretation of figures 3.9 and 3.10 from the previous chapter is relatively straightforward. The majority of orders have been delivered, which we should expect, given that we are working with data from five years ago. Orders that are neither delivered nor canceled should be analyzed one by one. Did some system error cause their status, or was there another reason?

The heatmap of delivery times shows big differences in the average delivery time. Let’s visualize figure 3.10 again, as figure 4.5.

![](images/1f7f3b8629908c4d88fc4561256bc88723439da3f107d5ba66cb9d4acba97bc3.jpg)

<details>
<summary>scatter</summary>

| Seller State | Customer State | Delivery Time (log-scaled) |
| ------------ | -------------- | -------------------------- |
| TO           | AC             | ~10^0                      |
| TO           | AL             | ~10^0                      |
| TO           | AM             | ~10^0                      |
| TO           | AP             | ~10^0                      |
| TO           | BA             | ~10^0                      |
| TO           | CE             | ~10^0                      |
| TO           | DF             | ~10^0                      |
| TO           | MS             | ~10^0                      |
| TO           | MT             | ~10^0                      |
| TO           | PA             | ~10^0                      |
| TO           | PA             | ~10^0                      |
| TO           | PB             | ~10^0                      |
| TO           | PE             | ~10^0                      |
| TO           | MI             | ~10^0                      |
| TO           | MN             | ~10^0                      |
| TO           | MN             | ~10^0                      |
| SP           | AC             | ~10^0                      |
| SP           | AL             | ~10^0                      |
| SP           | AM             | ~10^0                      |
| SP           | AP             | ~10^0                      |
| SP           | BA             | ~10^0                      |
| SP           | CE             | ~10^0                      |
| SP           | DE             | ~10^0                      |
| SP           | ES             | ~10^0                      |
| SP           | GO             | ~10^0                      |
| SP           | MA             | ~10^0                      |
| SP           | MG             | ~10^0                      |
| SP           | MS             | ~10^0                      |
| SP           | MT             | ~10^0                      |
| SP           | PA             | ~10^0                      |
| SP           | PA             | ~10^0                      |
| SP           | PB             | ~10^0                      |
| SP           | PE             | ~10^0                      |
| SP           | PI             | ~10^0                      |
| SP           | PR             | ~10^0                      |
| SP           | RJ             | ~10^0                      |
| SP           | RN             | ~10^0                      |
| SP           | RO             | ~10^0                      |
| SP           | RR             | ~10^0                      |
| SP           | RS             | ~10^0                      |
| SP           | SC             | ~10^0                      |
| SP           | SE             | ~10^0                      |
| SP           | SP             | ~10^2                      |
| SP           | TO             | ~10^0                      |
| SE           | AC             | ~10^0                      |
| SE           | AL             | ~10^0                      |
| SE           | AM             | ~10^0                      |
| SE           | AP             | ~10^0                      |
| SE           | BA             | ~10^0                      |
| SE           | CE             | ~10^0                      |
| SE           | DE             | ~10^0                      |
| SE           | ES             | ~10^0                      |
| SE           | GO             | ~10^0                      |
| SE           | MA             | ~10^0                      |
| SE           | MG             | ~10^0                      |
| SE           | MS             | ~10^0                      |
| SE           | MT             | ~10^0                      |
| SE           | PA             | ~10^0                      |
| SE           | PA             | ~10^0                      |
| SE           | PB             | ~10^0                      |
| SE           | PE             | ~10^0                      |
| SE           | PI             | ~10^0                      |
| SE           | PR             | ~10^2                      |
| SE           | RJ             | ~10^2                      |
| SE           | RN             | ~10^2                      |
| SE           | RO             | ~10^2                      |
| SE           | RR             | ~10^2                      |
| SE           | RS             | ~10^2                      |
| SE           | SC             | ~10^2                      |
| SE           | SE             | ~10^2                      |
| SE           | SP             | ~10^2                      |
| SE           | TO             | ~10^2                      |
| MO           | AC             | ~10^0                      |
| MO           | AL             | ~10^0                      |
| MO           | AM             | ~10^0                      |
| MO           | AP             | ~10^0                      |
| MO           | BA             | ~10^0                      |
| MO           | CE             | ~10^0                      |
| MO           | DE             | ~10^0                      |
| MO           | ES             | ~10^0                      |
| MO           | GO             | ~10^0                      |
| MO           | MA             | ~10^0                      |
| MO           | MG             | ~10^2                      |
| MO           | MS             | ~10^2                      |
| MO           | MT             | ~10^2                      |
| MO           | PA             | ~10^2                      |
| MO           | PA             | ~10^2                      |
| MO           | PB             | ~10^2                      |
| MO           | PE             | ~10^2                      |
| MO           | PI             | ~10^2                      |
| MO           | PR             | ~10^2                      |
| MO           | RJ             | ~10^2                      |
| MO           | RN             | ~10^2                      |
| MO           | RO             | ~10^2                      |
| MO           | RR             | ~10^2                      |
| MO           | RS             | ~10^2                      |
| MO           | SC             | ~10^2                      |
| MO           | SE             | ~10^2                      |
| MO           | SP             | ~10^2                      |
| MO           | TO             | ~10^2                      |
| VA           | AC             | ~10^0                      |
| VA           | AL             | ~10^0                      |
| VA           | AM             | ~10^0                      |
| VA           | AP             | ~10^0                      |
| VA           | BA             | ~10^0                      |
| VA           | CE             | ~10^0                      |
| VA           | DE             | ~10^2                      |
| VA           | ES             | ~10^2                      |
| VA           | GO             | ~10^2                      |
| VA           | MA             | ~10^2                      |
| VA           | MG             | ~10^2                      |
| VA           | MS             | ~10^2                      |
| VA           | MT             | ~10^2                      |
| VA           | PA             | ~10^2                      |
| VA           | PA             | ~10^2                      |
| VA           | PB             | ~10^2                      |
| VA           | PE             | ~10^2                      |
| VA           | PI             | ~10^2                      |
| VA           | PR             | ~10^2                      |
| VA           | RJ             | ~10^2                      |
| VA           | RN             | ~10^2                      |
| VA           | RO             | ~10^2                      |
| VA           | RR             | ~10^2                      |
| VA           | RS             | ~10^2                      |
| VA           | SC             | ~10^2                      |
| VA           | SE             | ~10^2                      |
| VA           | SP             | ~1o                         |
| VA           | TO (not labeled)     {| CO            - CO          - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO        - CO       }
</details>

Figure 4.5 Scatterplot of delivery times from one state to another, colored by log-norm scale

The differences in average delivery time are a good topic to ask our generative AI advisor about. We need to make sure we describe the pattern of interest to the best of our ability.

![](images/f5091baccbfa54978cc0b5f0d765ec4fd3e47ee0aa671e3d2731caef562cc613.jpg)

I have a heatmap presenting delivery times broken by the state where the sales had taken place and product categories sold. I can see that some states have much higher average delivery times than others—we’re talking order of magnitude difference. We can also see differences between product categories, but not as dramatic. What could be the reasons for such results, and what actions could be taken to improve our business?

ChatGPT 4 returned the following answer:

![](images/2622f5287c962da822b5084ffab7d559383e61c549a037007c1bb8e6de20d6ab.jpg)

While I don’t have up-to-date knowledge on the current status of Brazilian logistics and distribution (as my knowledge is up to September 2021), I can provide some general insights that might help you interpret your results.

1 Infrastructure: Brazil has a diverse transportation system consisting of roads, railways, waterways, and air transportation. However, the quality of infrastructure can vary significantly between regions, impacting delivery times. For example, the southeastern region, which includes São Paulo and Rio de Janeiro, generally has better infrastructure compared to the northern and northeastern regions.   
2 Geography: Brazil is a vast country with diverse landscapes, including large cities, remote rural areas, and the Amazon rainforest. The geography of the country can pose challenges for logistics and distribution, especially when transporting goods to remote areas or across the Amazon rainforest.   
3 Road transportation: Road transportation is the most common mode of transportation for goods in Brazil. However, the quality of roads can be poor in some regions, leading to delays and increased transportation costs. Additionally, road transportation may be impacted by weather conditions, such as heavy rains causing flooding in certain regions.   
4 Bureaucracy and customs: In some cases, bureaucracy and customs procedures can slow down the logistics process, especially for cross-border shipments or when dealing with specific regulatory requirements.   
5 Regional disparities: Brazil has significant economic and social disparities between regions, which can impact the efficiency of the logistics and distribution system. More economically developed regions like São Paulo, Rio de Janeiro, and other southeastern states generally have better logistics infrastructure and services.

When analyzing the average delivery times for orders between different Brazilian states, consider the factors mentioned above. You might identify patterns and correlations between delivery times and specific regions, infrastructure quality, or geographical challenges. This information can help you identify areas where improvements can be made or where alternative distribution strategies may be needed.

Gemini Advanced returned the following:

# UNDERSTANDING THE DISPARITY

The significant difference in average delivery times between states is a crucial indicator of underlying operational or logistical issues. Possible reasons include:

State-Specific Factors:

Geographical Challenges: States with vast distances, mountainous terrain, or poor infrastructure can experience longer delivery times.

Population Density: Urban areas generally have better delivery infrastructure, while rural areas might face challenges.

Carrier Performance: The performance of carriers in different states can vary significantly.

Warehouse or Distribution Center Location: The proximity of warehouses to customers can impact delivery times.

Local Regulations: Different states might have varying regulations that impact transportation and delivery.

Product Category Factors:

Product Dimensions and Weight: Larger or heavier products typically have longer delivery times.

Product Fragility: Products requiring special handling or packaging can lead to slower delivery.

Inventory Availability: Stock levels at different warehouses can impact order fulfillment speed.

Order Processing Time: Complexity of orders (e.g., multiple items, customizations) can influence processing time.

# IMPROVING BUSINESS PERFORMANCE

To address the issue, consider the following actions:

Data Analysis and Refinement:

Deeper Dive: Analyze delivery times at a more granular level (city, zip code) to identify specific problem areas.

Correlation Analysis: Explore correlations between delivery times and other factors (e.g., order value, order volume).

Customer Segmentation: Analyze delivery times based on customer segments (e.g., residential, commercial) to identify patterns.

Operational Improvements:

Carrier Performance Evaluation: Assess the performance of different carriers in various states and optimize carrier selection.

Warehouse Network Optimization: Evaluate the location and capacity of warehouses to ensure efficient distribution.

Inventory Management: Improve inventory levels and distribution to reduce stockouts and expedite shipments.

Order Fulfillment Process Improvement: Streamline order processing to minimize delays.

Transportation Route Optimization: Use route planning software to optimize delivery routes and reduce travel time.

Technological Solutions:

Real-time Tracking: Implement real-time tracking systems to monitor shipments and identify potential delays.

Delivery Time Estimation: Provide accurate delivery time estimates to customers.

Advanced Analytics: Utilize data analytics to predict delivery times and optimize operations.

Customer Experience:

Communication: Keep customers informed about order status and any potential delays.

Delivery Options: Offer flexible delivery options (e.g., time slots, pickup locations) to meet customer needs.

By combining data-driven insights with operational improvements, you can effectively address the delivery time disparities and enhance overall customer satisfaction.

Would you like to delve deeper into any of these areas?

There you can see the difference between different generative AIs. ChatGPT tied the answer to specifics of Brazil’s diverse geography and variations in infrastructure quality, showing how economic development across regions can significantly impact sales revenues. We also learned that factors such as transport mode, road quality, weather conditions, bureaucracy, customs procedures, and regional economic disparities could lead to considerable differences in sales between states and product categories. Remember, though, that ChatGPT has a knowledge cutoff, so it would be prudent to confirm its revelations.

Gemini stuck to the vague “good advice.”

Let’s see if we will be able to get some specific insights now. Let’s select two pairs of states, and ask our GPT advisor about expected differences.

MA

Given that, how should I expect delivery times from RJ to ES compared to CE to MG?

6

Rio de Janeiro (RJ) and Espírito Santo (ES) are neighboring states in the southeastern region of Brazil. This region generally has better infrastructure, including roads and highways, compared to other parts of the country. As a result, you can expect relatively shorter delivery times for shipments between RJ and ES due to their proximity and the quality of the transportation infrastructure in the area.

On the other hand, the northeastern state of Ceará (CE) and the southeastern state of Minas Gerais (MG) are farther apart. The distance between these states is significantly larger than the distance between RJ and ES, which can result in longer delivery times. Additionally, while MG is in the southeastern region with generally better infrastructure, CE is in the northeastern region, which may have less developed transportation infrastructure in some areas. This factor could also contribute to longer delivery times for shipments between CE and MG.

In summary, you should generally expect shorter delivery times for shipments between Rio de Janeiro (RJ) and Espírito Santo (ES) compared to Ceará (CE) and

Minas Gerais (MG) due to their proximity and the transportation infrastructure in the southeastern region. However, it is important to note that there could be variations in delivery times depending on the specific locations within each state, the type of transportation used, and other factors such as weather conditions or bureaucratic processes.

If an employee could deliver an answer as rapidly and comprehensively as ChatGPT, we’d not only grant them a raise but double it, tossing in a side of fries for good measure. ChatGPT noted that delivery times between Brazilian states largely depend on their geographical proximity and the quality of local transportation infrastructure. For instance, the delivery times between neighboring states of Rio de Janeiro (RJ) and Espírito Santo (ES), both located in the better-connected southeastern region, are expected to be shorter.

However, delivery between Ceará (CE) in the northeastern region and Minas Gerais (MG) in the southeast may take longer due to their geographical distance and potential disparities in infrastructure development. Furthermore, specific locations within each state, the type of transportation used, and other factors such as weather conditions or bureaucratic processes can also influence delivery times. It’s evident that even when the data in a chart is too vast to squeeze into a text prompt, and the chart itself is a real head-scratcher to describe, a well-trained generative AI can still prove immensely valuable in interpreting the results.

# 4.6 Relationship between product attributes and the shipping costs

We never really expected an analysis of the relationship between product attributes and shipping costs to unravel any earth-shaking discoveries. In contrast, time spent on learning regression, one of the most powerful analytical tools, will be time well spent. In section 3.4.2, we presented you with a list of (not all) possible application areas for this methodology. But getting a result is one thing. Making sense of it . . . that’s where the value of analysis is.

You might expect that only large $\mathrm { R ^ { 2 } }$ values are worth reporting (recall that the $\mathrm { R ^ { 2 } }$ value is a measure of what percent of the variability in the dependent variable is explained by the changes in independent or tested variables). These are certainly the values most desired by business stakeholders. Who wouldn’t want to present a slide showing “85% of our sales are driven by our brilliant marketing”? I guess product development and customer support would turn green, but bragging rights are not the only business driver worth pursuing.

Another example comes from our experiences. A company invested in a massive retention campaign. In fact, it was so aggressive that clients who were exposed to it were less likely to repurchase the product! This fact was hidden for a long time by the campaign, which used feedback surveys that benefited from the fact that really irritated clients didn’t want to waste their time on the company. A negative $\mathrm { R ^ { 2 } }$ parameter value of regression testing the influence of the number of received messages on the likelihood of repurchase told a different story altogether. And this is not the end of the lesson. The company’s senior management didn’t want to admit to making a mistake and kept sending aggressive messages until the company went bankrupt.

Does this mean you should focus on large positive or negative $\mathrm { R } ^ { 2 }$ values? Yes and no. Such values are important, but this doesn’t mean that near-zero $\mathrm { R ^ { 2 } }$ values aren’t. Let’s assume you entered your office one day and found yourself surrounded by lifesized models of dinosaurs. HR came up with the idea of “Dinosaur Desk Mates.” They decided that triggering employees’ “fight or flight” response to loud, unexpected roars would boost their productivity. After a couple of weeks, you’re tasked with analyzing the effectiveness of this idea. If your stakeholders are lucky, the $\mathrm { R } ^ { 2 }$ of the relation between the number of roars per hour and productivity metrics will oscillate around zero; otherwise, you’d probably be in the negative $\mathrm { R } ^ { 2 }$ range.

Let’s return to the relationship between product size and weight and shipping costs. In the realm of supply chain management, you may encounter situations where regression analysis can help you understand how product dimensions or weight impact shipping costs and can lead your company to redesign products for efficiency, potentially saving millions in logistics expenses.

Let’s see if it’s worth querying generative AI about the results you’d get from regression analysis.

![](images/2e2861cbd51b63a250102d40c45deb53c4ea5d96a227b8e9c328c3c22ba2f5ce.jpg)

I’ve been testing the relationship between product attributes (in this case, its dimensions and weight) and the shipping costs.

I ran the linear regression model, and below are the results:

```txt
Product Weight Model: MAE=6.89, MSE=156.77, RMSE=12.52, R2=0.37
Product Volume Model: MAE=7.41, MSE=163.70, RMSE=12.79, R2=0.34
Then I tried to combine the two and got the following model summary:
OLS Regression Results 
```

<table><tr><td>Dep. Variable:</td><td>freight_value</td><td>R-squared:</td><td>0.399</td></tr><tr><td>Model:</td><td>OLS</td><td>Adj. R-squared:</td><td>0.399</td></tr><tr><td>Method:</td><td>Least Squares</td><td>F-statistic:</td><td>3.744e+04</td></tr><tr><td>Date:</td><td>Sun, 09 Apr 2023</td><td>Prob (F-statistic):</td><td>0.00</td></tr><tr><td>Time:</td><td>15:38:56</td><td>Log-Likelihood:</td><td>-4.4203e+05</td></tr><tr><td>No. Observations:</td><td>112632</td><td>AIC:</td><td>8.841e+05</td></tr><tr><td>Df Residuals:</td><td>112629</td><td>BIC:</td><td>8.841e+05</td></tr><tr><td>Df Model:</td><td>2</td><td></td><td></td></tr><tr><td>Covariance Type:</td><td>nonrobust</td><td></td><td></td></tr></table>

<table><tr><td></td><td>coef</td><td>std err</td><td>t</td><td>P&gt;|t|</td><td>[0.025</td><td>0.975]</td></tr><tr><td>const</td><td>13.7268</td><td>0.044</td><td>314.740</td><td>0.000</td><td>13.641</td><td>13.812</td></tr><tr><td>product_weight_g</td><td>0.0016</td><td>1.63e-05</td><td>101.023</td><td>0.000</td><td>0.002</td><td>0.002</td></tr><tr><td>product_volume</td><td>0.0002</td><td>2.61e-06</td><td>70.759</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Omnibus:</td><td colspan="2">105287.730</td><td colspan="2">Durbin-Watson:</td><td colspan="2">1.815</td></tr><tr><td>Prob(Omnibus):</td><td colspan="2">0.000</td><td colspan="2">Jarque-Bera (JB):</td><td colspan="2">12678300.032</td></tr><tr><td>Skew:</td><td colspan="2">4.145</td><td colspan="2">Prob(JB):</td><td colspan="2">0.00</td></tr><tr><td>Kurtosis:</td><td colspan="2">54.311</td><td colspan="2">Cond. No.</td><td colspan="2">3.37e+04</td></tr></table>

Is there any practical conclusion that could be derived for my business from these results?

The response of ChatGPT 4 was as follows:

![](images/d65c25162ecbab180d5c6784e592e3ef010cdedf214240dafcf753530f007bed.jpg)

Based on the results of the linear regression models, here are some practical conclusions and potential actions for your business:

1 Both product weight and volume are significant factors in determining shipping costs. The positive coefficients for both product\_weight\_g and product\_volume indicate that as the weight and volume of the product increase, the shipping cost also increases.   
2 The R-squared values for the individual models (0.37 for weight and 0.34 for volume) and the combined model (0.399) suggest that the models explain around 34-40% of the variance in the shipping costs. Although this is not a very strong relationship, it indicates that other factors also contribute to the shipping costs. It could be useful to explore additional factors that may impact shipping costs, such as the distance between the origin and destination, the shipping provider, or the shipping speed.   
3 Given that both weight and volume have an impact on shipping costs, you can consider optimizing your packaging to minimize shipping costs. This could involve using lighter packaging materials or designing more compact packages to reduce the overall volume.   
4 You could also consider offering different shipping options to customers based on the product’s weight and volume, allowing them to choose between more affordable, slower delivery options and faster, more expensive options.   
5 When sourcing or developing new products, keep the shipping costs in mind. Consider the weight and volume of the product and how they may impact the overall cost for customers. Lighter and more compact products may be more attractive to customers due to lower shipping costs.

Remember that these conclusions are based on the provided models and their assumptions, and real-life situations may have additional factors to consider. Additionally, it’s essential to validate the models with further data and analysis to ensure their accuracy and reliability.

Gemini Advanced returned the following:

![](images/06ba5fd597ab5506a35c3752a79813d40c15bfb9a37a087668a6e10328d469b3.jpg)

Yes, absolutely! Let’s break down what these regression results tell us and focus on the practical applications for your business:

Understanding the Models

MAE, MSE, RMSE: These are error metrics:

a MAE (Mean Absolute Error): The average absolute difference between the predicted shipping costs and actual costs. In both models, you’re off by about \$6-7 on average.   
b MSE (Mean Squared Error): Similar to MAE, but it squares the errors, emphasizing larger mistakes.

c RMSE (Root Mean Squared Error): The square root of MSE, making it easier to interpret in the same units as your costs (dollars).

R2 (R-squared): An indicator of how much variation in shipping costs is explained by your model. In both cases, roughly 34-39% of the changes in costs are captured by the model. While not extraordinarily high, this is still useful.

# Key Takeaways

1 Both Weight and Volume Matter: The combined model confirms that both product weight and volume are positively correlated with shipping costs. This means heavier and bulkier items cost more to ship.

2 Weight Might Be Slightly More Important: In the combined model, the coefficient for product\_weight\_g is slightly larger than that of product\_volume. This suggests an additional gram of weight could increase the shipping cost a bit more than an additional cubic unit of volume.

# Practical Applications

Pricing and Cost Estimation:

a Use these models to provide more accurate shipping estimates to customers on your website. Even a rough idea of shipping costs can improve the customer experience.

b Adjust product prices to account for varying shipping costs based on size and weight, especially for heavier or larger products.

 Optimizing Product Design:

a If possible, consider design changes to reduce product weight and volume without sacrificing value. This can potentially lead to long-term shipping cost savings.

Negotiating with Carriers:

a Demonstrate the relationship between product attributes and shipping costs when negotiating rates with carriers. This could give you leverage for better deals.

 Customer Communication:

a Be transparent about how size and weight factor into shipping costs. Help customers understand why some items cost more to ship and encourage them to consider consolidating orders.

Important Considerations:

a Other Factors: Remember, there are other variables affecting shipping rates (destination, carrier, fuel surcharges, etc.). This model provides a focused view but doesn’t capture everything.

b Data Quality: The accuracy of your results depends heavily on the quality of your shipping cost and product dimension data.

c Room for Improvement: These models have room for improvement. You might explore additional variables or different modeling techniques in the future.

Let me know if there’s a specific aspect of your business (pricing, logistics, etc.) you’d like to consider, and I can tailor the applications even further!

ChatGPT analyzed the given regression model results and concluded that both product weight and volume significantly influence shipping costs, explaining about 34–40% of the variance in these costs. We could read that from the $\mathrm { R ^ { 2 } }$ values ourselves. However, the general advice could be passed to management for consideration.

Gemini Advanced was a bit more specific and made a very important step in a good direction. It translated the regression errors into dollars (the data was likely in Brazilian Real, but that’s not important here).

MONEY TALKS If you want to make management see the value of your work, translate it to monetary value. This is universally true for all types of analyses. Before making a decision, they need to do this anyway.

In the following section, we’ll further probe generative AI’s ability to detect connections and possible causality in correlations between different parameters related to sold products.

# 4.7 Relationship between product, transaction, shipping attributes, and the review score

When you’re new to data analytics, ordinal logistic regression might seem an unnecessarily complex tool. The truth is, it’s necessarily a complex tool.

Imagine you’re analyzing adherence to a prescribed medication regimen. This variable can be categorized into levels such as “never adheres,” “sometimes adheres,” “often adheres,” and “always adheres.” Your boss asks you to plan how you will test the influence of a new patient education program on medication adherence among chronic disease patients.

Using ordinal logistic regression, you could investigate the program’s effectiveness by examining changes in adherence levels before and after the program’s implementation. Factors such as the thoroughness of the education, patient feedback on side effects, and frequency of follow-up consultations could be considered.

The results could show, for example, that patients who rated the education program highly were 40% more likely to be in the “always adheres” category compared to those who did not participate in the program. Alternatively, it might reveal that patients experiencing moderate to severe side effects are twice as likely to fall into the “never adheres” or “sometimes adheres” categories, highlighting the need for targeted strategies to address these side effects.

Analyzing data with ordinal logistic regression doesn’t stop at finding out what’s working or not. It may help you predict future trends and make informed decisions. If you are able to show that a particular aspect of your service, like personalized customer support, significantly boosts satisfaction, you’ll help your company enhance these areas and drive positive outcomes.

In section 3.4.3, we mentioned that the coefficients of ordinal logistic regressions are somewhat similar to their counterparts resulting from linear regression. We also warned you that, in the case of ordinal logistic regressions, coefficients should be interpreted with particular caution, especially if, like in the case of the data we analyzed, the model’s goodness-of-fit statistics (e.g., R2 , AIC) indicate that the model may not adequately capture the relationship between the predictor variables and the response variable.

Results that lurk in the gray area of “something somewhat depends on something else” are always good candidates to be bounced off your generative AI advisor.

![](images/33d1147fbfc750a3cc62755150722bf7fdbc08a9ddc7ebf01911b0824dd31aa5.jpg)

I ran the analysis of the relationship between product, transaction, shipping attributes, and the review score. I used ordinal logistic regression.

I got the following results:   
```yaml
1. Coefficients:
delivery_time: -0.04926184129232652
price: 0.0016396437688542174
freight_value: 0.003087605979194856
product_name_lenght: 0.013890193611842357
product_description_lenght: 1.938890383573905e-05
product_photos_qty: 0.4213701136980763
product_weight_g: -8.756509636657266e-06
payment_sequential: 0.35978743241417466
payment_installments: 0.02936386138061978
payment_value: -0.001722960231783981
delivery_time_misestimation: 0.02821300240733595
product_volume: 9.504512398147115e-07
payment_type_boleto: 0.1329365830670677
payment_type_credit_card: 0.22320994812520034
payment_type_debit_card: 0.013163990732791755
payment_type_voucher: -0.005952023594428278
2. Accuracy: 0.43035067573535907
3. Confusion Matrix:
[ [ 385 70 401 1637 1302 ]
[ 38 13 71 563 513 ]
[ 55 16 109 1342 1365 ]
[ 49 18 100 2909 3501 ]
[ 54 23 208 8021 11200 ]] 
```

What conclusions can be drawn about my business if I run the eCommerce platform, where multiple sellers offer their products to buyers?

ChatGPT 4 returned the following response:

![](images/595d9e8c4bc4bd44faaad82fd9812a7fa05397a1cabe7a81682ad88d8ff42890.jpg)

Your results from the ordinal logistic regression analysis illuminate several important factors influencing review scores in your eCommerce platform. Let’s dissect these findings, considering both the statistical significances (implied by the coefficients) and their practical implications for the business. The accuracy of the model stands at 43.03%, which, while not exceptionally high, does suggest that the variables considered do explain some of the variance in review scores.

1 Coefficients Interpretation:

a Delivery time (-0.04926): As expected, longer delivery times negatively impact review scores. This indicates that improving delivery speed can directly enhance customer satisfaction.

b Price (0.00164) and Freight value (0.00309): These have positive coefficients, but given their small magnitude, the impact on review scores might be less substantial. Price sensitivity could vary significantly across different product categories.   
c Product name length (0.01389): Longer product names, perhaps implying more detailed descriptions, slightly improve review scores. This might indicate that customers appreciate clearer information.   
d Product description length (very small positive impact): While statistically significant, its practical impact might be negligible due to the small coefficient.   
e Product photos qty (0.42137): A significant positive impact, suggesting that listings with more photos lead to higher satisfaction. Visual information appears crucial for customer decisions.   
f Product weight (negligible negative impact): The slight negative coefficient might be related to shipping costs or handling expectations but is likely not a major concern given its magnitude.   
g Payment attributes:

i Sequential (0.35979) and Installments (0.02936): Positive coefficients suggest that flexibility in payment options positively affects customer satisfaction.   
ii Payment value (negative): Higher overall payment amounts slightly decrease satisfaction, possibly reflecting higher expectations or buyer’s remorse at higher price points.   
iii Payment types: Credit card payments show the most substantial positive effect, indicating a preference or higher satisfaction among those users, while vouchers slightly decrease satisfaction.

h Delivery time misestimation (0.02821): When delivery estimates are inaccurate (whether early or late is not specified), it slightly increases review scores, suggesting that customers might appreciate conservatism in delivery estimates or be pleasantly surprised by early deliveries.

i Product volume (negligible positive impact): Its effect is minimal, suggesting that the size of the product is not a significant determinant of review scores.

2 Model’s Predictive Performance (Accuracy & Confusion Matrix):

a The accuracy, while not negligible, indicates a lot of room for improvement. This suggests either inherent unpredictability in review scores or the need for additional or different explanatory variables.   
b The confusion matrix shows a significant challenge in accurately predicting extreme review scores (1 and 5), with a tendency to predict towards the middle range. This might indicate either a model issue (such as assuming linearity in ordinal outcomes) or that customer satisfaction is influenced by factors not captured in the model.

# Business Implications:

 Prioritize Speed and Accuracy in Deliveries: Investment in logistics to improve delivery times and accuracy of estimates can directly enhance customer satisfaction.   
 Enhance Product Listings: Focus on improving the quality and quantity of product photos and detailed descriptions to aid in the buying decision process.

 Optimize Payment Options: Offering and possibly promoting flexible payment options, including credit card use, can improve satisfaction.   
 Review Strategy for Pricing and Freight: While the impact is small, understanding the nuanced effects of pricing and shipping costs on different product categories could offer competitive advantages.   
 Additional Factors: Considering the model’s moderate accuracy, it’s worth exploring other variables not included in the current analysis. These could include seller performance metrics, customer service interactions, and more granular shipping/ delivery experiences.

Your analysis has provided valuable insights, but it also highlights the complex nature of customer satisfaction and the potential need for more nuanced models or additional data to fully understand and predict review scores on your platform.

Gemini Advanced also answered the question:

![](images/50066b0b93c8c0898a6ad1014d29482eeadbf267deee7f5b7c2f1622f4471058.jpg)

Let’s break down what these ordinal logistic regression results tell us about the factors influencing your product review scores and how to apply them to improve your business.

Understanding Ordinal Logistic Regression

Ordinal logistic regression is appropriate when your outcome variable is ordered, like review scores (e.g., 1-star, 2-star, etc.). Here’s how to interpret the key elements:

 Coefficients:

a Positive Coefficient: Indicates that an increase in that variable is associated with a higher likelihood of a better review score.   
b Negative Coefficient: Indicates an increase in that variable is associated with a higher likelihood of a worse review score.   
c Magnitude of Coefficient: The larger the absolute value of the coefficient, the stronger the association with the review score.

 Accuracy: This tells you the percentage of reviews your model correctly classified into their score categories. An accuracy of 43% suggests your model does better than simply guessing but leaves significant room for improvement.

 Confusion Matrix: This shows how your model’s predictions compared to actual review scores. Read it diagonally for correct predictions, and other cells show misclassifications.

# Key Takeaways

1 Delivery & Price Matter Most: delivery\_time and price have the largest negative and positive coefficients, respectively. This strongly suggests:

a Late deliveries are detrimental to review scores.   
b Higher-priced items might lead to higher expectations, increasing the likelihood of both higher and lower scores.

2 Other Significant Factors:

a product\_photos\_qty: More product photos seem to help improve review scores.

b payment\_type: Interestingly, payment type influences scores, with credit cards being the most favorable.   
c payment\_sequential: This likely indicates whether a customer was a first-time or repeat buyer, with the latter potentially being more lenient.

3 Negligible or Confusing Factors:

a Several variables have very small coefficients, suggesting minimal impact (product\_weight\_g, product\_volume, freight\_value).   
b delivery\_time\_misestimation has a small but positive coefficient. This is counterintuitive and might need further investigation into how you calculate this variable.

# Practical Applications

 Prioritize On-Time Delivery: Focus heavily on timely delivery, as this has the most significant impact on customer satisfaction.   
 Competitive Pricing Strategy: Balance the desire for higher prices with the need to manage customer expectations and avoid negative reviews.   
 Invest in Product Photography: Add more high-quality product photos to give customers a clear picture of what they’re buying.   
Understand Payment Preferences: Explore why payment methods impact reviews. Perhaps credit card purchases are associated with higher-value orders?   
Target Repeat Customers: Since they seem more likely to give better reviews, implement strategies to build customer loyalty.

# Important Considerations

Accuracy Limitations: The model’s accuracy leaves room for other important factors not included. Consider collecting data on additional variables (product quality, customer service, etc.).   
Causation vs. Correlation: This analysis points towards associations, but it doesn’t prove that changing any specific factor will directly cause a change in review scores.

Let me know if you’d like help brainstorming improvement strategies in any of these areas!

Both generative AIs provided us with a lot of food for thought on the basis of a couple of parameters, their coefficients, and a single-sentence business description. Before being transformed into airtight business recommendations, most of these results would need deep-dive analytics, but we got some solid leads, and that’s more than we bargained for!

# 4.8 Differences in sales performance and customer satisfaction between sellers

In chapter 3, we used the bootstrap method to calculate the confidence intervals for the average price of health and beauty products and for the customer satisfaction across Brazilian states. The resulting figure 3.12 is repeated as figure 4.6.

![](images/feabb330a45dfbef0d01c074861598e2605294700493cd5e5ea89807586f9997.jpg)

<details>
<summary>bar</summary>

| Seller State | Average Sales |
| ------------ | ------------- |
| BA           | 120           |
| CE           | 480           |
| DF           | 110           |
| ES           | 150           |
| GO           | 120           |
| MA           | 80            |
| MG           | 140           |
| MS           | 190           |
| MT           | 100           |
| PE           | 40            |
| PR           | 200           |
| RJ           | 170           |
| RN           | -20           |
| RS           | 260           |
| SC           | 310           |
| SP           | 110           |
</details>

a

![](images/054ec7bf558fa588c385569e0a5aca7970057d06ae0ca1328ca0ff9e5f681052.jpg)

<details>
<summary>bar</summary>

| Seller State | Average Review Score |
| ------------ | -------------------- |
| BA           | 4.8                  |
| CE           | 4.7                  |
| DF           | 4.3                  |
| ES           | 3.2                  |
| GO           | 4.6                  |
| MA           | 4.1                  |
| MG           | 4.2                  |
| MS           | 5.0                  |
| MT           | 4.5                  |
| PE           | 3.3                  |
| PR           | 4.3                  |
| RJ           | 4.2                  |
| RN           | 5.0                  |
| RS           | 4.3                  |
| SC           | 4.1                  |
| SP           | 4.0                  |
</details>

b   
Figure 4.6 Confidence intervals for (a) average sales price and (b) average review scores, for transactions in the “health and beauty” category of products

The first important part of analyzing this result is to understand that the actual average value is somewhere within the confidence interval. Somewhere—we don’t know where. The width of the confidence intervals depend on three main factors:

The size of the sample   
The selected confidence level   
Inherent data variability

Many managers are used to seeing point estimations, and they want to be able to say that the average satisfaction of our customers is, for example, 3.7495735 points out of 5.

This is where we solve the riddle we posed in subsection 3.4.4. We asked you there, “why, when working with our example, does it make sense to use bootstrapping and calculate confidence intervals for our prices, and why would it most likely not make sense if you worked with your business data?” We calculated the average price confidence intervals, because we know from the exploratory data analysis that we are working with a subset of the data. In our table, we don’t have all the transactions for the analyzed period. If you work with complete data, your average sales price can be USD 3.7495735 (the purposefulness of reporting it with this level of accuracy is a different issue altogether). You don’t estimate the average of a complete population— you calculate it.

Working with surveys requires estimation, and estimations come with inherent limitations in accuracy and are subject to uncertainty. It’s crucial to account for this uncertainty in the decision-making process.

Have a look at figure 4.6.b, which shows the confidence interval between the SP and PE states. Customers in which state are more satisfied? We don’t know, mainly because we don’t really know how satisfied PE customers are.

In the figure, we have some conclusion-ready confidence intervals. ES customer satisfaction requires immediate attention, and that would be obvious even if you just calculated average scores. The average price of products in CE is much higher than anywhere else in the country.

There is more to analyzing confidence intervals. The most obvious interpretation is that if the confidence intervals calculated for two categories (e.g., states) are not overlapping, the actual calculated values indeed differ. There are analytical methods for estimating the difference of the overlapping confidence intervals, but we won’t follow this rabbit hole here. In many business contexts, the width of the confidence intervals, which indicates the estimate’s precision, can be just as crucial as the difference between the estimated values themselves. A narrower confidence interval implies greater precision and reliability in the estimate, which is important from an informed decision-making perspective.

Throughout this chapter, our generative AI advisor proved invaluable in crafting analyses, offering relevant questions that could be addressed using the available data, supplying code to transform that data into visualizations and models, and providing insightful hints about the results’ significance and potential avenues for further analysis and business implications.

The process also revealed the weaknesses of generative AIs. The most notable is their tendency to hallucinate when asked about topics and data defined too long before the prompt. Also, the provided code needs to be tested, as sometimes it’s buggy and sometimes prepared for outdated library versions.

All in all, we determined which topics are important to research with just a couple of discussions with generative AI about the goals of your analysis and what it could look like, running some code it developed for you, and then another couple of discussions on results. When you get fluent and choose the generative AI best fitted to help in your problems, you’ll be able to do it in a couple of hours instead of days!

# Things to ask generative AI

 What research questions related to the provided data can be asked?   
What should the design of the analysis leading to answering the following question look like? <provide question>   
What statistical method is best to analyze <available data>?   
 Provide me with code to <data transformation>.   
 How should I visualize <data structure>?   
Provide me with a solution answering the following question: . . .   
 Modify the code to change the visualization format.   
 How should I interpret this result of the modeling: . . . ?   
 What can you tell me about <market question> in <market definition>?   
 What business insights can be derived from this result: . . . ?

# Summary

Generative AI may be excellent in suggesting proper analytical tools and providing end-to-end analytical strategies.   
 Generative AIs will first suggest the most popular methods, but they can provide competent support in the implementation of more niche ones too.   
 Generative AI may supplement analysis with market-specific information.   
 Feeding generative AI results to get insights requires caution and sometimes reengineering of provided data.   
 Generative AI can offer sound business insights.   
 You need to control the context awareness of generative AI and be wary of their hallucinations. Jog their memory from time to time.   
The code provided by generative AI needs careful testing.

# Basic text mining using generative AI

# This chapter covers

 Frequency analysis   
 Co-occurrence analysis   
 Keyword search   
Dictionary-based methods

In previous chapters, you dealt with numerical data and learned the basic analytical methods for translating a bunch of numbers into sound business advice. This chapter and the next will show you how to deal with something far more sinister than numbers—text. Most of the text you’ll encounter won’t be clean, literary language that an author has double-checked and had edited by specialists. More often, you will deal with hastily prepared notes, offhand reviews, and emails. Such data is riddled with errors that can significantly impact the quality of analysis and results. These include spelling mistakes, typographical and punctuation errors, and irregular use of capitalization. Additionally, texts often contain irrelevant or redundant information such as headers, footers, or metadata, as well as linguistic noise from nonstandard abbreviations, slang, or jargon. Just when you think you are prepared to handle all this by adapting your text-cleaning functions, you may encounter another exception, like a piece of . . . ASCII art!

To make things worse, most text analysis is done on an amount of text exceeding the average person’s capacity for bedtime stories, especially since a lot of text you’ll work with is the stuff of nightmares. Fortunately, people who were likely fond of different types of literature developed many methods enabling them to draw conclusions from large amounts of text without reading it all. We’ll discuss some of these techniques in this and next chapter. And thanks to generative AI, they are readily available to you.

In particular, chapters 5 and 6 will guide you through the complexities of unstructured textual data to extract valuable insights, patterns, and knowledge. By the end of this chapter, you will be equipped to harness generative AI for a broad range of foundational text-mining tasks, all while avoiding the typical pitfalls associated with large language models (LLMs), such as hallucinations or ad hoc changed assumptions. As in previous chapters, you will learn how generative AI can aid you in information gathering, analytical planning, data interpretation, and coding, as well as enable you to perform quick, initial text analyses—either through direct interaction with the model or by leveraging its API. Moreover, you will learn about more of generative AI’s limitations, recognizing when they may provide unreliable results, and also about identifying key factors you’ll need to watch to ensure accurate results.

In this chapter, we will perform an analysis of customer reviews. You will also see how the polyglot abilities of generative AIs are invaluable for handling data in foreign languages. Additionally, you will be impressed by the generative capabilities of LLMs to summarize findings in a format that is ready to be presented to your boss.

# 5.1 Text mining in the era of generative AI

Even with well over half of internet traffic being dedicated to certain types of videos and unwanted marketing communications, there is a lot of data movement left to analyze. And there is a chance some of it will end up on your computer, with the expectation that you’ll be able to draw some insights from the content. As we mentioned in the chapter’s introduction, a lot of this data might, in fact, be text. The ever-increasing volume of unstructured textual content from social media, websites, emails, company documents, and academic publications has elevated the role of text mining.

Text mining employs the combined powers of natural language processing (NLP), machine learning (ML), and artificial intelligence (AI) to convert the deluge of unstructured text into organized data for more straightforward analysis and interpretation. NLP is crucial, as it allows systems to understand and manipulate human language, converting sentences into structured forms that a computer can understand. For instance, NLP techniques can break down text into components like phrases and sentences, identify parts of speech, and extract relationships and entities. This structured data is then more amenable to analysis. ML complements this by providing models that can learn from the structured data, identifying patterns or predicting outcomes without being explicitly programmed to look for something specific. This is particularly useful in sentiment analysis or topic modeling. Lastly, AI integrates these technologies to automate the entire process, enhancing the ability to make decisions or generate insights from large volumes of text data efficiently. AI systems can adapt to new patterns in text, refine their understanding over time, and handle a wide variety of text sources and formats, making the process of text mining more dynamic and context-aware.

In its final form, text mining enables the discovery of underlying patterns, trends, and insights, offering valuable capabilities such as sentiment tracking, trend spotting, threat identification, and a deeper understanding of customer preferences.

# 5.1.1 Generative AI is a game changer

Imagine you are assigned the task of understanding the trends in the latest technologies from technical articles (hopefully scraped for you beforehand) or of parsing customer feedback in product reviews. We already mentioned that actually reading all this data is an impractical feat, given its sheer volume and human life expectancy. In addition, while technical articles will allow you to build a coherent vision of the technological landscape, customer reviews are often contradictory—not just with multiple reviews contradicting each other but also with self-defeating prose within individual reviews!

Traditionally, pre-LLM text-mining techniques took a shortcut by not analyzing the entire text. Instead, they focused on extracting the most informative parts, such as the most frequent phrases, or they relied on predefined dictionaries to search for meaning. These methods are akin to statistical sampling, drawing conclusions about a whole population based on a limited sample. Similarly, identifying the most frequent terms or detecting certain keywords can hint at the overall message without the timeconsuming task of fully reading the text.

LLMs, however, have revolutionized this analytical landscape. They can process immense amounts of text (for instance, Gemini claims a million token context) and they do so word by word, sentence by sentence. More than just reading, LLMs can interpret text, connecting seemingly disparate pieces of data to provide a comprehensive overview without relying on the frequency-based shortcuts of old-school methods. While it is true that LLMs might still employ some form of data processing shortcuts— and perhaps not even their developers fully understand every intricacy of how LLMs process data—the outputs, as we will explore in the following sections, are impressive.

However, no solution is without its limitations, and LLMs are no exception. Before we examine these limitations, let’s take a moment to consider an often-overlooked aspect: the human psychology, and particularly how one can feel intimidated by the impressive capabilities of generative AI. Understanding this human element is crucial not only for using these tools effectively but also for ensuring your mental well-being.

# 5.1.2 Beware of AI intimidation

At first glance, seeking assistance from generative AI for traditional text-mining tasks might appear counterintuitive. Instead of merely using ChatGPT or Gemini as an advisor for rule-based sentiment analysis, you could submit a collection of texts to them, request a sentiment assessment, and often achieve results superior to constructing everything from scratch. Even a brief encounter with modern generative AI can reveal their astonishing capabilities in coding, data analysis, and extracting knowledge from data, potentially leaving you awestruck and questioning your professional relevance, if not identity. Given this context, the methods discussed in this chapter might seem analogous to retrofitting a chariot with racing car components to win a race when the optimal solution would be to simply drive the Formula 1 car itself. In the following sections, you will see that this attitude may be shortsighted.

A few years ago, the advent of deep learning methods seemingly rendered many traditional ML models antiquated. Deep learning often delivered superior results and proved easier to implement for numerous tasks. A similar scenario can be observed today with generative AIs, except their performance may surpass traditional ML models and deep learning by orders of magnitude. The reason is straightforward: an average programmer has limited resources, and training models with 100 trillion parameters is beyond their capabilities. This raises a pertinent question: why invest time in learning NLP basics or training your own language models? Instead, shouldn’t we focus solely on refining our communication skills with generative AIs while enjoying a cup of coffee?

NOTE If you want to learn more about how generative AIs are surpassing traditional ML models and deep learning, or want to find the means to stay competitive on the global AI market, I recommend reading “Choose Your Weapon: Survival Strategies for Depressed AI Academics,” an article by J. Togelius and G.N. Yannakakis (https://arxiv.org/abs/2304.06035).

This way of thinking is typical of AI intimidation and can be fatal; these models actually have many limitations that mean it is vital to maintain your own skills, if only to ensure that you are not accepting AI’s outputs purely on faith. Also note that, so far, no good metric to assess the quality of these outputs has been proposed, which means humans will have to rely on their own reason and expertise for a while longer. Keeping your own brain cells in shape is also crucial if you opt to refine your generative AI conversational counterparts by training them on specific datasets of your choice (refer to chapter 1 for details). This approach offers a balanced middle ground between grasping every nuance of the technology behind generative AI and placing unwavering trust in its outputs.

# 5.1.3 Unpacking the constraints

Using generative AI for text-mining tasks might seem appealing due to its broad language capabilities; however, in practical business applications, dedicated libraries may sometimes prove more effective. It should be stressed, though, that the area where traditional methods surpass generative AI is shrinking with almost every update. Nevertheless, let’s explore the scenarios in which generative AI may struggle:

Accuracy—Tools like Spacy, NLTK, and TextBlob provide a level of accuracy in text analysis that generative AI might not achieve, especially with specialized vocabularies. For instance, a company conducting competitive analysis can use these libraries to accurately track competitor announcements, capturing mentions of new product features or strategies that generative AI might overlook due to its broader focus.

 Ambiguity—While generative AI can offer a wide contextual understanding, it may struggle with ambiguous language, such as words with multiple meanings or slang. A social media platform, for example, might use dedicated libraries fine-tuned for hate speech detection, which can more accurately identify harmful content by recognizing specific linguistic patterns and expressions that generative AI could miss or has not yet learned.   
 Language proficiency—For text analysis in less common languages, dedicated libraries may be more effective than generative AI. However, with the latest updates, it is becoming increasingly difficult to find a niche language that generative AI cannot handle. Even less commonly spoken languages like Welsh or Basque seem to be well supported. Nevertheless, if you ever need to analyze customer reviews in Tolkien’s Sindarin or Star Trek’s Klingon, you might find it more practical to use specialized language models.   
 Consistency—Dedicated libraries offer consistent results, crucial for applications like content moderation on social media platforms. Unlike generative AI, which may vary in its interpretations, dedicated libraries apply the same rules and patterns for detection, ensuring equitable treatment across all content.   
 Speed and scalability—In handling large datasets, dedicated libraries outperform generative AI in terms of speed and scalability, processing text data more efficiently. A news aggregation platform, for instance, can categorize thousands of articles quickly using NLTK or Spacy, enabling faster updates and insights.   
 Customizability—The flexibility of dedicated libraries allows for tailoring to specific needs, such as a legal firm customizing search algorithms to navigate patent databases with precision—a level of customization generative AI cannot easily match, unless you download and fine-tune it yourself.   
 Integration—Dedicated libraries integrate smoothly into existing systems and workflows, enhancing the efficiency of data processing and analysis. For example, a retail company can incorporate text-mining libraries into their analytics platforms for automatic sentiment analysis of customer feedback, informing marketing and product development.

While these limitations suggest using generative AI for text mining with caution, it doesn’t imply that such LLMs should be omitted from your toolkit. By recognizing their strengths and weaknesses, generative AI can still play a significant role in your projects, offering valuable insights and enhancing the capabilities of more specialized tools. The key is to know when and how to effectively leverage each tool to fully realize its potential. With the knowledge gained from this chapter, you should be equipped to maximize the benefits of the generative AI of your choice.

# 5.2 Preparing for analysis

If you’ll ever work with marketing, product design, customer service, strategic planning, or . . . let’s keep it short. If you ever work with any customer-related business departments, there is a high probability they will task you with analyzing what customers think about their company product or service. Sometimes, companies decide to invest in customer surveys, but more often they decide to get insight from opinions available on their website or retail platform.

The basics of analyzing scores associated with product reviews are to be found in previous chapters. Here, as the chapter’s title suggests, we’ll focus on analyzing the actual comments left by users.

# 5.2.1 Data quality

Data cleaning has been addressed in previous chapters, but not all the elements of data preparation we previously discussed are applicable to text data. However, this does not mean it can be overlooked. It’s crucial to ensure you comprehend aspects such as the relevance, timeliness, uniqueness, and integrity of your data.

Are these reviews even about your product, or did the agency scraping online retail websites send you reviews of your competitor’s products? Did you get recent reviews or data your predecessor analyzed three years ago? Are the comments unique, or will you assign “Karen’s from NY” complaint 60 times more weight than anybody else’s opinion because a glitch in the system copied her comment every second for a full minute? Finally, are the reviews bound to an order, or are they general impressions left on a review site?

If you don’t answer these questions, you may chase the wrong rabbit. Take your time. Look at the data. The following list of practices will ensure you have high-quality data in your analysis:

 Text cleaning—Start by removing irrelevant characters, such as HTML tags, emojis (unless they are part of your analysis), stopwords (i.e., common words like “and,” “the,” or “a,” that do not provide much information), and extra white space. Normalization techniques such as lowercasing can also help reduce complexity.   
 Handling missing values—Decide on a strategy for missing data—whether to impute, ignore, or remove missing values. The choice might depend on the volume of missing data and its potential impact on the analysis.   
 Dealing with duplicates—Identify and remove duplicate reviews, as they can skew your analysis. Sometimes, duplicates are not exact matches but paraphrases or slightly altered texts, which might require more sophisticated detection methods.   
 Spell checking and correction—Reviews often contain spelling errors. Utilizing spell-check libraries can help correct these, but be cautious with domain-specific terms or slang.

 Language detection—Ensure your text data is in the expected language (or languages). Non-relevant language data can be filtered out, especially in global platforms where multiple languages are common.   
 Sentiment consistency—For sentiment analysis, it’s useful to check for consistency between the review rating and the sentiment expressed in the text. Anomalies might indicate sarcasm or incorrect ratings.   
Entity recognition—Identifying and standardizing entities mentioned in text data (e.g., product names, brands) can improve the accuracy of your analysis, especially when aggregating insights.   
 Removing or identifying biased data—Reviews may contain biased or non-representative views, especially if they are predominantly from a specific user group. Identifying and mitigating this bias is crucial for generalizable insights.   
 Data anonymization—Ensure compliance with privacy laws by anonymizing personal information in your dataset. In the case of data that we use as an example, the anonymization replaced actual names with fictional ones.   
 Use of domain-specific stopwords—Besides standard stopwords, consider removing or adding irrelevant or overly common words to your specific dataset of stopwords.   
 Quality control pipelines—Implement automated pipelines that continuously monitor data quality metrics and flag issues for review. This is particularly important for real-time data analysis systems.   
 Human-in-the-loop—Despite automation, having domain experts review and validate data quality and analysis outcomes periodically can catch nuances that automated systems miss.

These practices are time-consuming and require a blend of automated tools and human judgment, and their specifics can vary depending on the nature of the text data and the objectives of the analysis. However, implementing these practices not only ensures data quality but also enriches your analysis, leading to more accurate and actionable insights.

# 5.2.2 Customer feedback preparation example

A common task in customer review is identifying the main areas of customer feedback: both positive aspects, and areas requiring improvement to boost customer satisfaction. The review dataset we are going to use throughout this chapter, collected from postpurchase customer surveys, resembles typical datasets of this kind: disorganized, emotional, and likely containing spelling errors. Analyzing this dataset will show you the practical applications of generative AI in text mining, underscoring their potential to transform how we analyze and interpret vast amounts of textual data.

Throughout this and the next chapter, we will use the olist\_order\_reviews\_dataset .csv file from the Brazilian e-commerce dataset. Both the file and the dataset were presented in previous chapters. As you can probably guess, the reviews are not in English, and unless you are familiar with Portuguese, the entire exercise may appear needlessly complex. However, this intricacy is purposeful, designed to demonstrate that generative AI can transform what was previously considered an insurmountable language barrier into a mere curb. Although it will still require a bit of your attention, crossing it will not make you sweat.

As a reminder, the dataset file we will explore contains customers’ reviews of products and their buying experiences. It consists of seven columns:

review\_id—Unique review identifier, an alphanumeric string   
order\_id—Unique order identifier, an alphanumeric string   
review\_score—Rating ranging from 1 to 5 given by the customer on a satisfaction survey   
 review\_comment\_title—Comment title from the review left by the customer, in Portuguese   
 review\_comment\_message—Comment message from the review left by the customer, in Portuguese   
 review\_creation\_date—The date on which the satisfaction survey was sent to the customer in the format “YYYY-MM-DD hh:mm:ss”   
 review\_answer\_timestamp—The satisfaction survey answer timestamp in the format “YYYY-MM-DD hh:mm:ss”

The easiest way to use this data is to save the input file in the same folder as the Jupyter notebook you downloaded from our GitHub repository (otherwise, you will have to specify the path to your file manually). If you want generative AI to generate a piece of code that acknowledges your specific input file, you’ll have to specify the filename in the query. If you don’t specify the input file directly, generative AI will probably refer to the input as your\_data.csv or something similar. In such a case, you must manually replace this made-up filename with the path to your input file. The loaded input file will be stored as a pandas DataFrame under the variable df.

To demonstrate the utility of generative AI in analyzing the provided reviews, we will initially focus on fundamental techniques for extracting information from text, such as a frequency analysis of common words and expressions (section 5.3). After that, we will explore co-occurrence analysis to examine patterns of word associations (section 5.4). These two sections should offer insights into the most prevalent topics covered within the reviews. Our next step will involve the basic categorization of reviews as positive, negative, or neutral by analyzing the occurrence of sentimentrelated keywords (section 5.5) and lexicon phrases (section 5.6). More sophisticated text-mining techniques are presented and compared in chapter 6.

To evaluate the efficacy of the tested sentiment analysis methods, we will utilize the review\_score field, which conveys customer satisfaction on a scale of 1 to 5. This numerical score allows easy determination of negative, positive, or neutral reviews without any textual analysis. However, you must keep in mind that in real-life scenarios, analyzed texts, especially of a different nature than reviews, are rarely accompanied by such scores; we are employing them here strictly for research purposes.

# 5.3 Frequency analysis

Diving into frequency analysis is far from a ceremonial nod to data analytics’ past—it’s a smart strategy that fills your toolbox with useful, real-world applications. Besides its well-known importance in cryptography and security, frequency analysis also plays a big role in studying more exotic DNA and protein analysis terrains. For example, it helps find patterns or sequences that are key for understanding genetic diseases or developing groundbreaking drugs. Looking at more everyday uses, frequency analysis in e-commerce helps spot trends in customers’ buying, showing which products are hot and predicting future sales. In social media, it helps identify what topics or hashtags are getting attention, helping brands connect better with people. And in customer service, analyzing the most common complaints or questions can make everything run smoother and keep customers happier.

Frequency analysis offers a clear and direct path to uncovering insights, but what exactly is it? Simply put, frequency analysis tallies how frequently each item occurs within a dataset. When applied to text analysis, it enables us to measure how often certain words or phrases appear, providing a clear view of the primary topics or ideas being discussed.

To demonstrate how frequency analysis can help in everyday business situations, we will focus on analyzing customer reviews from the collection presented in the previous section. To learn what customers most often praise or complain about, our initial instinct might be to read a few randomly selected reviews. However, this approach may not be effective, especially if the reviews are in a foreign language, and the chosen sample may not represent the overall content. Examining frequently occurring words and phrases is a much more efficient method of grasping the overall sentiment of customer feedback.

The best way to utilize generative AI in frequency analysis is by letting it guide you through the process, offering suggestions on tools and techniques, and providing code examples in popular programming languages.

# 5.3.1 What can we learn from frequency analysis of customer reviews?

While a quick check of your product’s average rating (the number of stars) will provide an overall customer satisfaction level, frequency analysis of customer reviews offers a comprehensive view into the nuances of consumer sentiment, revealing what customers value and the areas requiring attention. By pinpointing the most frequently mentioned aspects of a product or service, such as “customer service” or “durability,” businesses can understand the key drivers of customer satisfaction. Positive examples, like repeated praise for a smartphone’s “battery life,” highlight the product features that resonate well with consumers, indicating areas of strength.

Conversely, the balance between positive and negative terms in reviews provides insight into the product’s overall reception. A higher frequency of positive terms suggests customer satisfaction, while prevalent negative terms might pinpoint issues needing resolution. This balance offers a clear gauge of how well a product meets customer expectations.

Moreover, frequency analysis can detect shifts in customer preferences and emerging trends. An increase in mentions of “eco-friendly” features could signal a growing demand for sustainable products, guiding businesses to adjust their offerings accordingly. It also reveals common use cases, such as the popularity of “low light performance” for cameras, indicating how customers commonly use the product.

By integrating these insights, frequency analysis serves as a powerful tool for businesses to understand both the current landscape of customer appreciation and the evolving trends in consumer preferences. This can enable a strategic approach to product development and marketing, ensuring that offerings not only meet current customer needs but are also positioned to adapt to future demands, leading to enhanced customer satisfaction and business success.

# 5.3.2 Direct frequency analysis with generative AI

The most straightforward and intuitive method for conducting frequency analysis using generative AI is to directly input the data into the chat interface and request the desired analysis. Upon testing, all GenAI models demonstrated consistent performance, producing similar results. Should there be any gaps or inaccuracies in the initial output, a follow-up query from the user can swiftly refine and enhance the accuracy of the response. Let’s look in detail at how ChatGPT handles this task.

![](images/c89ab92f70fcf0d800195a720593fdc0dbdf6d89ec22e5a0abaa0e7f17a1b5aa.jpg)

Can you perform basic frequency analysis on this bunch of reviews:

“Recebi bem antes do prazo estipulado.”

<HERE WE PROVIDED MORE REVIEWS>

![](images/297930adda480b8265f0b186a9a5d410ba6c4cbbed8856a821f72bfbda82ddb1.jpg)

The frequency analysis of the provided reviews reveals a focus on a few key terms:

“a” and “e” appear most frequently, but as they are articles and conjunctions in Portuguese, their high frequency is expected and not particularly informative.

“do” (of/from) and “o” (the) also show up frequently, again reflecting common Portuguese grammar structures rather than specific content.

More relevant to the reviews’ content, “antes” (before), “prazo” (deadline), and “aparelho” (device) each appear multiple times, indicating common themes around timely delivery and product discussions.

“prazo” appearing 3 times underscores a focus on delivery times in these reviews.

“aparelho” appearing 3 times suggests that the product, presumably some type of device, is a central topic of discussion.

The words “recebi” (I received), “parabéns” (congratulations), “pela” (by the/for the), “marca” (brand), “esta” (this/is), “com” (with), “que” (that/which), “produto” (product), “entrega” (delivery), “compra” (purchase), and “foi” (was) appearing twice each further highlight common elements of customer feedback, such as receiving products, brand mentions, and satisfaction with purchases and deliveries.

This analysis indicates a general satisfaction with delivery times and product quality, with some mentions of brand and product discrepancies.

In the preceding example, the model’s response was enriched with a Python code snippet used to perform the analysis. Interestingly, generative AI can also perform such analyses using its built-in language model capabilities, presenting an alternative method that doesn’t require external coding. It’s vital, however, to recognize the distinction between these two methodologies and to be conscious of which one your generative AI employs to deliver its insights. For example, ChatGPT, as of February 2024, shows a preference for a method that involves crafting and running Python code, followed by an interpretation of the outcomes. This preference underscores the method’s reliability and the tangible benefit of having a verifiable code snippet to review the analysis’s accuracy.

Nevertheless, invoking generative AI’s inherent language abilities through a specific prompt remains a viable option (e.g., by requesting “use your inherent abilities for this task”). This approach, while immediately accessible and not requiring any coding knowledge, tends to be more error-prone and less scalable due to token analysis limitations. Moreover, it functions as a black-box mechanism, where the underlying process isn’t as transparent, and users don’t receive a code snippet to verify the analysis’s logic.

Speaking of token number limitations, we pasted just the first ten reviews from the example data set into the previous dialogue. For an effective and manageable analysis within this format, it’s best to keep the input text to a moderate length—ideally, a few paragraphs or around 500 words. You should be aware that while there isn’t a strict limit on how much text you can paste for fast frequency analysis, excessively long texts may cause processing delays or exceed the context token limit for a single response. If your input or the AI-generated response exceeds this limit, the message may be truncated, and you may not receive the full information you require. In such cases, it’s advisable to divide your input or request into smaller portions and send them separately to ensure you receive complete and accurate responses. The input/output limits of generative AI were discussed in chapter 1.

# 5.3.3 Uploading a data file to ChatGPT for frequency analysis

For handling larger inputs, a more practical option to consider is directly uploading your data file to generative AI and requesting the specific analysis you need. However, not all generative AI platforms offer this feature, so it’s important to verify its availability.

When uploading data files, keeping the file size manageable, ideally below a few megabytes, is crucial for efficient processing. ChatGPT supports various formats, such as plain text (.txt), CSV (.csv), and Excel (.xlsx), making analysis more straightforward. While there is no strict limit on data size, very large datasets may necessitate focusing on particular segments to manage the analysis effectively within the platform’s processing capabilities. Moreover, it’s vital to ensure that the data does not contain sensitive or personally identifiable information to adhere to privacy regulations and company policies.

Furthermore, when uploading data files to a generative AI platform for analysis, several issues might arise that could affect the accuracy and reliability of the results. Issues with data cleanliness and formatting can lead to misinterpretations; incorrectly preprocessed data may result in skewed or erroneous analyses. Without a deep understanding of the dataset’s context and subtleties, the model may miss important insights or make inaccurate assumptions, particularly with complex or specialized data.

Therefore, for complex and nuanced datasets, it’s recommended that you maintain oversight throughout the analysis process. This involves breaking the analysis into manageable parts and using generative AI for assistance at each stage, while keeping a close watch on the progress. Although generative AI can help in deriving conclusions, relying entirely on it for a comprehensive large-scale data analysis project is asking for trouble. It’s important to understand that the issue isn’t just about the input size generative AI can handle, because with nearly every update, the capacity of LLMs increases. Employing a “divide and conquer” strategy is beneficial because it allows you to supervise the process, understand what is happening, and identify errors.

# 5.3.4 Extracting the most common words

Throughout this chapter, we emphasize the fact that in real-life scenarios, most of the text input data you’ll encounter will likely be neither small nor simple, unlike the examples provided earlier. In such situations, your strategy should include soliciting generative AI for a tailored code snippet to address your data analysis needs. To secure a snippet that’s ready for use, you might need to specify the name of your Data-Frame, the specific column where your data resides, or both. Generative AI may default to a generic naming convention if you don’t.°

Since the models won’t directly interact with your data this time, it is prudent to supply essential additional details about your dataset; in this example, highlighting that your data is in Portuguese could be crucial. Advanced frequency analysis requires the elimination of stopwords and the tokenization of text, which are inherently language-dependent tasks. You will need to employ an appropriate set of Portuguese stopwords and a tokenizer that is designed for the Portuguese language. The GenAI model is expected to adjust to these specifications accordingly, but as you will discover, this process may not always function flawlessly. Consider the following prompt.

![](images/c9fffb9de90eda8be1cf9089027112f60c51ebb5c97b04ff20f59db46664a7b3.jpg)

I have a Python data frame with a column review\_comment\_message containing customer reviews. Propose a code snippet in Python to perform frequency analysis on these reviews. The reviews are in Portuguese.

![](images/5e07e773852858ce1d6249513f91687c3692ce9bf6d15902dc029880c816eaa7.jpg)

To perform frequency analysis on the review\_comment\_message column of a Data-Frame, you can use the Pandas library for handling the DataFrame, and NLTK for text preprocessing and analysis. Make sure to install the required libraries before running the code:

pip install pandas nltk

Here’s a code snippet to perform frequency analysis:

import pandas as pd import nltk from nltk.corpus import stopwords

```python
from nltk.tokenize import word_tokenize
from collections import Counter

# Make sure to download Portuguese stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load your DataFrame
df = pd.read_csv('olist_order_reviews_dataset.csv')

# Preprocessing function
def preprocess_text(text):
    # Tokenize, convert to lowercase, and remove punctuation
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalpha()]

    # Remove Portuguese stopwords
    stop_words = set(stopwords.words('portuguese'))
    filtered_words = [word for word in words if word not in stop_words]

    return filtered_words

# Apply preprocessing to the 'review_comment_message' column
df['processed_review'] =
df['review_comment_message'].apply(preprocess_text)

# Calculate word frequencies
word_freq = Counter()
for _, row in df.iterrows():
    word_freq.update(row['processed_review'])

# Print the most common words and their frequencies
print(word_freq.most_common(10)) 
```

This code snippet reads your data into a DataFrame, preprocesses the review\_ comment\_message column, and calculates the frequency of each word. It then prints the 10 most common words along with their frequencies.

We have included the recording of the whole conversation to show you that even though we specifically informed ChatGPT that we would be working with reviews in Portuguese, it doesn’t take that fully into account. The proposed tokenizer uses its default settings and applies tokenization rules for English. In practice, this small oversight should not generate serious differences in the output, but it is a very important lesson for us.

GENERATIVE AIS FORGET ABOUT THE CONTEXT In some cases, generative AI may disregard crucial aspects of NLP analysis, such as the language of the input data. Consequently, certain portions of the code may use tools with default settings (usually for English), while others may leverage language-specific libraries. To ensure accuracy, always thoroughly review the recommended resources and their settings, ensuring they align with your analysis’s context.

You may wonder if talking to generative AIs in Portuguese would eliminate such errors. Remember that these AIs generate their answers based on the selected online resources it was trained on, and in the case of NLP, most of these resources are in English. The most popular generative AI will naturally drift toward English data solutions anytime you let them out of your sight. Even if communication in Portuguese may reduce the number of similar issues, there is no guarantee that you will be able to eliminate them completely. Stay alert!

Another question is whether other generative AIs perform better in this task. We posed the same query to Gemini and Code Llama, receiving varied responses. For instance, Gemini accurately recognized the need for Portuguese language support in its code, making it immediately usable. However, its analysis was rather basic, relying on Python’s split method for tokenization without employing a specialized tokenizer, and it failed to address stopword removal. Yet, Gemini did account for some text cleaning specific to the Portuguese language and encouraged users to refine their queries for enhanced results. Conversely, the code from Code Llama wasn’t immediately functional, requiring several manual adjustments even to run. Its proposed analysis lacked depth, with no cleaning, tokenization, or stopword removal, making it challenging to assess Code Llama’s ability to recognize the intended language of the input data.

If an error occurs, as in the preceding scenario, where the context of our analysis was overlooked, you can request a correction. Advanced generative AI, with ChatGPT as a frontrunner, can help you even if you don’t provide it with a very detailed problem description; even a slight hint can steer the generative AI toward an improved solution. This feature proves invaluable when you feel something is amiss with the answer but can’t identify the specifics.

Let’s see what happens when we informally ask ChatGPT about the language of our input data.

![](images/c537233b02bc48711c39029ff02673bc5183409989a8f87452af2e0d6e7b310a.jpg)

Are you sure it is for Portuguese?

![](images/7f2cefd032b7b5b4afe6b1ea2d2d2fd423a05fc07399a3904501cebe173c37d4.jpg)

Apologies for the confusion earlier. I made a mistake in my previous response. To ensure the correct processing of Portuguese text, you can use the NLTK library with the proper language settings. Here’s an updated version of the code snippet that takes into account Portuguese stopwords:

```python
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Make sure to download Portuguese stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load your DataFrame
df = pd.read_csv('olist_order_reviews_dataset.csv') 
```

```python
# Preprocessing function
def preprocess_text(text):
    # Tokenize, convert to lowercase, and remove punctuation
    tokens = word_tokenize(text.lower(), language='portuguese')
    words = [word for word in tokens if word.isalpha()]

    # Remove Portuguese stopwords
    stop_words = set(stopwords.words('portuguese'))
    filtered_words = [word for word in words if word not in stop_words]

    return filtered_words

# Apply preprocessing to the 'review_comment_message' column
df['processed_review'] =
→df['review_comment_message'].apply(preprocess_text)

# Calculate word frequencies
word_freq = Counter()
for _, row in df.iterrows():
    word_freq.update(row['processed_review'])

# Print the most common words and their frequencies
print(word_freq.most_common(10)) 
```

In this updated snippet, the word\_tokenize function has been given the language='portuguese' argument to ensure proper tokenization for the Portuguese language. The rest of the code remains the same as before, and it should now be better suited for analyzing Portuguese text.

Again, we present the full transcript to show you that “prompt engineering,” in the case of advanced generative AIs, is overrated—sufficiently developed generative AI really is capable of understanding your concerns from a laconic comment.

It may be beneficial to approach every answer the model returns with skepticism and questioning. Beware, however, of voicing all of your concerns. We warned you that advanced models have a high level of sycophancy and, when in doubt, will reverse from their initial proposition, irrespectively of its value. Just dropping “Are you sure about it?” after each prompt can take you down the rabbit hole. However, a question about a given aspect of the analysis should result in either a correction or an explanation of the selected method. With a healthy dose of skepticism, you will probably discover additional errors the model can correct without guidance.

# Generative AI should be able to correct its errors

Feel free to question the responses of generative AI whenever you have doubts about the output. The better you understand its errors, and the more accurately you can describe them in your next prompt, the more satisfying the final answer will be. Even if you cannot pinpoint the exact error, the AI might still manage to correct itself. However, there is a genuine risk of generative AI acknowledging mistakes it hasn’t actually made! When challenged, it might opt to deliver incorrect responses instead of contradicting the user.

The aim of this brief exercise is not to compare the capabilities of various generative AIs or to demonstrate how you can obtain a perfect code snippet with a single prompt. All the models mentioned are adept at handling such tasks, and with a little effort and attention to detail, you can extract the necessary information from them. Moreover, engineering of the prompts that elicit perfect responses is not an exact science. Interacting with generative AIs is a dynamic dialogue where you can progressively refine your queries based on the feedback you receive.

The key lesson from this exercise is the importance of vigilance in evaluating the output for accuracy and relevance. To do this effectively, you should understand the fundamentals of the techniques you’re employing. In our scenario, a thorough frequency analysis necessitates the removal of stopwords and proper tokenization with respect to the language of the input data. The good news is that if you’re unfamiliar with a method, you can always begin by asking generative AI about the basics of the technique.

Coming back to customer feedback, the basic frequency analysis generative AI presented works well. Now it is time to make it a bit more complicated.

# 5.3.5 Extracting the most common phrases

Once, a boss asked his employee to describe, “in one word,” how they felt at work. The reply was “good.” Feeling encouraged, the boss then asked for an answer “in two words,” to which the response was “not good.” While this joke may not be the height of humor, it illustrates a valid point: single, common words often fail to capture the essence of messages in our reviews. A more effective strategy involves focusing on groups of consecutive words, which offer a clearer view of customer sentiment by capturing the context and nuances that single words might miss. These sequences of n items, such as words, are referred to as n-grams in NLP.

To extract the most common phrases from customer reviews, you can analyze the frequency of n-grams, most commonly bigrams (where n=2) and trigrams (where n=3). Higher-order n-grams may also be useful, depending on the level of granularity required for your analysis, especially when the text data you are analyzing is more complex. By analyzing the frequency, you can identify trends, common concerns, or strengths in their products or services, allowing the business to address issues more effectively. For example, the mere recurrence of the word “delivery” does not provide much insight into customer satisfaction. However, noticing the frequent appearance of phrases like “failed delivery” or “super fast delivery” in reviews can lead to valuable and actionable insights. A quick request to generative AI can result in a code snippet that will analyze trigrams in our reviews. In the following example, we used the same ChatGPT session and the following prompt: “Propose code snippet to analyze trigrams in my reviews.”

# Listing 5.1 Code snippet for analyzing trigrams

import pandas as pd import nltk from nltk.corpus import stopwords

```python
from nltk.tokenize import word_tokenize
from nltk.collocations import TrigramAssocMeasures,
TrigramCollocationFinder
from collections import Counter

# Make sure to download Portuguese stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load your DataFrame
df = pd.read_csv('olist_order_reviews_dataset.csv')

# Preprocessing function
def preprocess_text(text):
    # Tokenize, convert to lowercase, and remove punctuation
    tokens = word_tokenize(text.lower(), language='portuguese')
    words = [word for word in tokens if word.isalpha()]

    # Remove Portuguese stopwords
    stop_words = set(stopwords.words('portuguese'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Apply preprocessing to the 'review_comment_message' column
df['processed_review'] =
df['review_comment_message'].apply(preprocess_text)

# Calculate trigram frequencies
trigram_measures = TrigramAssocMeasures()
trigram_freq = Counter()

for _, row in df.iterrows():
    finder = TrigramCollocationFinder.from_words(row['processed_review'])
    trigram_freq.update(finder.ngram_fd)

# Print the most common trigrams and their frequencies
print(trigram_freq.most_common(10)) 
```

The code works as intended. In our case, because we utilized the previous session, the model remembered about the Portuguese language trap.

As you’ve seen here, utilizing LLM’s assistance to analyze the most frequently occurring phrases is relatively simple. Even with this straightforward code, the output provides valuable information about the overall content of the review messages. The last step is to understand the results and draw conclusions.

# 5.3.6 Understanding the output

The output you receive by running the code from listing 5.1 is pretty simple to interpret: it is a list of the most commonly used words, together with the number of their instances in the analyzed texts.

Assuming, for the sake of this task, that you don’t speak Portuguese, your first step in understanding the output will be to translate it. The good news is that generative

AIs can easily do that for you. As a bonus, you don’t need to extract the words from the output lists or tuples before translation. You can simply copy and paste the raw output, and a sufficiently advanced generative AI should be able to process it. In our case, we got the following result:

```python
('chegou', 'antes', 'prazo') - (arrived, before, deadline)
('bem', 'antes', 'prazo') - (well, before, deadline)
('entregue', 'antes', 'prazo') - (delivered, before, deadline)
('produto', 'chegou', 'antes') - (product, arrived, before)
('entrega', 'antes', 'prazo') - (delivery, before, deadline)
('chegou', 'bem', 'antes') - (arrived, well, before)
('produto', 'entregue', 'antes') - (product, delivered, before)
('entrega', 'super', 'rápida') - (delivery, super, fast)
('antes', 'prazo', 'previsto') - (before, deadline, expected)
('produto', 'ótima', 'qualidade') - (product, great, quality) 
```

Another reason to turn to generative AI for help could be to make the output of your frequency analysis more visually appealing without dusting off your paint skills. You could request the code needed to present the result in the form of a word cloud, where the font size corresponds to the frequency of the word.

To demonstrate this, we used the following prompt: “How to show these results of the frequency analysis in the form of a word cloud with English translations?” and accompanied it with the 10 most common words used in the reviews and identified previously. After repeating these steps, you should get a snippet similar to the following.

Listing 5.2 Frequency analysis in a word cloud   
```python
import matplotlib.pyplot as plt

# Frequency analysis results with English translations
word_freq = {
    'product': 18344,
    'deadline': 8410,
    'delivery': 6486,
    'before': 5619,
    'arrived': 5535,
    'received': 5262,
    'good': 4592,
    'recommend': 4269,
    'delivered': 3769,
    'came': 3276
}

# Create a word cloud
wordcloud = WordCloud(width=800, height=400,
→background_color='white').generate_from_frequencies(word_freq)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear') 
```

plt.axis('off') # Hide the axes plt.show()

Generative AI should also inform you what packages or libraries are required—in this case, you should precede the code from listing 5.2 with pip install wordcloud matplotlib. The resulting visualization should resemble figure 5.1.

![](images/ff17e73d7db35c0a48699c97dba3fed1568228fc0809b9a366e786d669f347b4.jpg)

<details>
<summary>text_image</summary>

received
product
came
delivery recommend
before
deadline good
delivered arrived
</details>

Figure 5.1 Visualizing customer feedback: a word cloud of the most frequently mentioned terms in reviews

Having this elegant image at hand, you may want to send it to your boss, together with a short note summarizing the results. And here is another boon from using generative AI: this task perfectly suits it! You can use the following prompt:

![](images/4e6a342c5798c2f0fbba8bc488862dbccd983801324881e8c421b64105a5069f.jpg)

Can you summarize the results of the monograms and trigrams frequency analysis in a short email to my boss? Provide English translations.

![](images/a3059be3ab539560dcc30c9546606af8c6ba4023707bb7517f55189e2e71bf60.jpg)

Subject: Summary of Customer Reviews Analysis

Dear [Boss’s Name],

I’ve completed a thorough frequency analysis of customer reviews, focusing on the most mentioned words and phrases. Here are the key findings, translated into English for clarity:

Top Single Words:

‘Product’ was mentioned 18,344 times, highlighting its importance in reviews.

‘Deadline’ and ‘Delivery’ followed, with 8,410 and 6,486 mentions, respectively, indicating a strong focus on timely delivery.

Words like ‘Before’, ‘Arrived’, ‘Received’, ‘Good’, ‘Recommend’, ‘Delivered’, and ‘Came’ were also frequently used, reflecting overall satisfaction with our services and product quality.

Top Trigrams:

Phrases such as ‘Arrived before deadline’, ‘Delivered before deadline’, and ‘Product arrived before’ were most common, mentioned over a thousand times. This suggests that exceeding delivery expectations is highly valued by our customers.

‘Delivery super quick’ and ‘Product great quality’ were also notable, emphasizing the appreciation for prompt delivery and product excellence.

Conclusion:

The analysis underscores the critical role of prompt delivery and product quality in customer satisfaction. It’s clear that our efforts to exceed delivery expectations and maintain high-quality standards are resonating well with our clientele. Going forward, we should continue to focus on these areas while exploring opportunities to further enhance our services and product offerings.

Best regards,

[Your Name]

If you have decided to work with data, there is a chance you have some tendency toward introvertism (we’re not judging; we’re relating). If that’s so, what you may find most gratifying among the various capabilities of generative AIs is their knack for drawing insights in any preferred format. While their assistance in generating code for analysis, troubleshooting bugs, and interpreting results is amazing, their ability to supplement it with an email to business stakeholders is a cherry on top!

# Generative AI performs quick and rough text-mining tasks

Generative AI proves useful for small-scale text-mining operations. Many NLP tasks, such as frequency analysis, can be executed utilizing its intrinsic language model. However, for larger inputs and more functional applications, it’s preferable to leverage models to generate a dedicated script. The most convenient way to do so is to upload your data file and specify the desired analysis in the prompt, but not all GenAIs have this option.

In both cases—utilizing GenAI's intrinsic language model and asking it for dedicated scripts—it is crucial to stay alert to potential errors and the misinterpretation of data.

You have just observed how leveraging generative AIs for frequency analysis can swiftly and efficiently yield valuable and actionable insights. In the following section, we’ll explore whether this analysis can be enhanced using a slightly more advanced technique: co-occurrence analysis.

# 5.4 Co-occurrence analysis

Speaking of reviews, consider the feedback on how a software update affects device performance. Let’s assume your product development team has outdone itself, and your website is flooded with comments from users concerned specifically about how the new software version “slows down” the device “over time.” While trigram analysis might identify phrases like “software update slows,” “update slows down,” or “slows down device,” it could overlook the broader, nuanced issue of performance degradation “over time” after the update.

Is hope lost? Not really, unless it’s the hope, after the previous section, that your text analysis is done and dusted. There is still a lot to do!

The method that would identify the relationships between “software update,” “slows down,” and “over time,” even when these terms aren’t part of the same trigram, is called co-occurrence analysis. To examine relationships between specific terms like these, we must first clean and tokenize our text data. Next, we need to choose a context window, which dictates how many words around a target word are considered to establish relationships. For each word, we then count how often other words appear within this window and record these counts in a co-occurrence matrix.

This matrix helps identify which terms frequently appear near each other, providing insights into common themes and issues discussed across the dataset, such as potential impacts of software updates on device performance over time—a key insight for developers and customer service. It’s a simple yet potent tool!

# 5.4.1 What can we learn from co-occurrence analysis?

While co-occurrence analysis might seem similar to n-gram analysis at first glance, they tackle different aspects of text mining. Where the latter zooms in, searching for the words snugly fitting next to each other, co-occurrence analysis zooms out a bit, capturing word pairs in a broader context. This can reveal some surprising connections and insights that you wouldn’t get from just looking at immediate word sequences. For a more detailed comparison of these two methods, see table 5.1.

Table 5.1 Comparison of n-gram and co-occurrence analyses 

<table><tr><td>Feature</td><td>n-gram analysis</td><td>Co-occurrence analysis</td></tr><tr><td>Description</td><td>Analyzes sequences of n items (words or tokens) from text</td><td>Examines how often each word co-occurs with other words within a specified context window in the text</td></tr><tr><td>Strengths</td><td>■ Simple to implement and understand■ Effective for language modeling and predictions</td><td>■ Captures broader semantic relationships between words■ Useful for exploring word associations and meanings</td></tr><tr><td>Limitations</td><td>■ Context limited to fixed n words■ May miss longer-term dependencies between words</td><td>■ Potentially high computational cost due to large matrices■ Requires careful selection of the context window size</td></tr><tr><td>Usage examples</td><td>■ Predictive text and autocomplete features■ Speech recognition and machine translation</td><td>■ Semantic analysis for identifying themes and topics■ Building semantic networks or enhancing word embeddings</td></tr></table>

Generally, by tracking how often words are paired, co-occurrence analysis uncovers key themes, preferences, and issues mentioned in customer reviews. It’s an effective way to find insights that aren’t immediately obvious, providing a strong basis for improving products, refining marketing strategies, and enhancing customer service. This method is straightforward and easy to use, making it a valuable part of the analytics toolkit. It doesn’t require deep linguistic knowledge or complex algorithms, ensuring that time spent analyzing customer feedback is well-used and leads to actionable business insights.

# 5.4.2 Co-occurrence analysis in practice

We hope that we were able to convince you that analyzing the co-occurrence of words in your dataset is a worthwhile endeavor. Conducting it using generative AI is as simple as it was in the case of frequency analysis, and you can apply the approaches outlined in section 5.2 for frequency analysis.

For simple small datasets, you can directly input your data into the chat window and request the model to either leverage its inherent language processing capabilities or generate code for the desired analysis. For larger datasets, uploading a data file and requesting analysis will yield both the necessary code and a comprehensive analysis explanation. While these methods are handy for straightforward, small-scale analyses, more complex and voluminous data typically requires a more thorough approach. In those cases, it’s more efficient to request specific code snippets for an in-depth investigation of your data.

Moving forward, we will focus on acquiring code snippets for our queries, bypassing the steps of pasting or uploading data into the chat window. Future sections will also explore conducting analyses through the API, enhancing our ability to handle diverse analytical challenges.

Let’s start by asking generative AI for the desired code. In the following example, we used ChatGPT and the following prompt: “Propose a code snippet in Python to perform co-occurrence analysis for customer reviews in Portuguese stored as a column review\_comment\_message in a pandas dataframe.” For clarity, some elements of the code, such as imports, downloads, and data loading, were removed from the following listing, but you can still find them in the Jupyter notebook in the book’s GitHub repository. The following listing shows the core of the snippet returned to us.

Listing 5.3 Code snippet for co-occurrence analysis   
```python
# Preprocessing function
def preprocess(text):
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    words = [word for word in words if word not in
    →stopwords.words('portuguese')]
    return words

# Co-occurrence function
def co_occurrence_matrix(corpus, window_size=5):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_index = {word: i for i, word in enumerate(vocab)} 
```

```python
n = len(vocab)
co_occurrence_matrix = np.zeros((n, n))

for row in data['review_comment_message']:
    tokens = preprocess(row)
    for i, word in enumerate(tokens):
    for j in range(max(i - window_size, 0), min(i + window_size + 1, len(tokens)):
    if i != j:
    co_occurrence_matrix[vocab_index[word],
    vocab_index[tokens[j]]] += 1

return co_occurrence_matrix, vocab_index

# Calculate co-occurrence matrix
corpus = [word for row in data['review_comment_message'] for word in preprocess(row)]
co_matrix, vocab_index = co_occurrence_matrix(corpus)

# Visualize the co-occurrence matrix using a heatmap
plt.figure(figsize=(15, 15))
sns.heatmap(co_matrix, xticklabels=vocab_index.keys(),
yticklabels=vocab_index.keys(), cmap="YlGnBu")
plt.show() 
```

Unless you’re very specific in your request, the first version of any code you receive should be simple yet effective, meaning it will perform its intended function in the most straightforward and uncomplicated manner. However, the results, while accurate, might overlook some finer details of the data. For instance, in the preceding example, tokenization is based on the basic Python split method. If you find this approach insufficient for your analysis and want to explore more deeply, you might need to ask the model to revise the snippet using more advanced methods. For example, you could ask the model to use a specialized Portuguese tokenizer or apply lemmatization.

If you are not familiar with these advanced methods and are concerned you might not realize their potential necessity, we highly recommend spending some time learning and chatting with your generative AI advisor about the possibilities. Engage in an informative and open conversation about your analytical plans and seek their recommendations. This proactive approach ensures you’re well-prepared to make the most out of your data analysis.

# Generative AI can refine and guide your plans

Even if you are well-versed in the details of the analysis you intend to perform, discussing your plans with generative AI is strongly advised. Quite frequently, it can offer valuable insights and suggest approaches that hadn’t occurred to you.

Another issue with the code proposed in listing 5.3 is that it may be inefficient, considering the size of the input dataset. In co-occurrence analysis, we need to create matrices where rows and columns represent unique words, with values indicating their frequency of co-occurrence. Since most word pairs rarely occur together, the resulting matrices are predominantly filled with zeros, necessitating the use of sparse matrices, which are data structures that store only nonzero elements. Using sparse matrices saves significant amounts of memory and computational resources. If you’re anxious about the execution time, don’t worry. Generative AI rarely returns optimal code as its first answer. We’ll cover issues related to code optimization in detail in chapter 7.

Listing 5.4 shows how the core of the code can be improved after a little complaint about waiting time. As you can see, this time ChatGPT suggests using lil\_matrix from the scipy.sparse package, which is designed for efficient construction and modification of sparse matrices. Additionally, we requested an English translation of the output and limited the resulting image to show only the 30 most common co-occurring pairs.

Listing 5.4 A more optimal code snippet for co-occurrence analysis   
```python
<SOME IMPORTS HERE>
from scipy.sparse import lil_matrix

<DATA LOADING>

# Preprocessing function
def preprocess(text):
    text = re.sub(r'^\w\s]', '', text).lower()
    words = text.split()
    words = [word for word in words if word not in stopwords_set]
    return words

# Co-occurrence function
def co_occurrence_matrix(corpus, vocab, window_size=5):
    vocab_index = {word: i for i, word in enumerate(vocab)}
    n = len(vocab)
    co_occurrence_matrix = lil_matrix((n, n), dtype=np.float64)

    for row in data['review_comment_message']:
    tokens = preprocess(row)
    for i, word in enumerate(tokens):
    for j in range(max(i - window_size, 0), min(i + window_size + 1, len(tokens)):
    if i != j and word in vocab_index and tokens[j] in vocab_index:
    co_occurrence_matrix[vocab_index[word], vocab_index[tokens[j]] += 1

    return co_occurrence_matrix, vocab_index 
```

```python
# Calculate co-occurrence matrix
corpus = [word for row in data['review_comment_message'] for word in
preprocess(row)]
word_counts = Counter(corpus)
top_n_words = 30 # Adjust this number according to your needs
most_common_words = [word for word, count in
word_counts.most_common(top_n_words)]
co_matrix, vocab_index = co_occurrence_matrix(corpus, most_common_words)

# English translations of the words (this part was added by ChatGPT when we
asked directly for translations)
translations = {
    'produto': 'product',
    'prazo': 'deadline',
<MORE TRANSLATIONS HERE>
}

# Create a list of translated words for visualization
translated_words = [translations.get(word, word) for word in
vocab_index.keys()]

# Visualize the co-occurrence matrix using a heatmap
plt.figure(figsize=(15, 15))
sns.heatmap(co_matrix.toarray(), xticklabels=translated_words,
yticklabels=translated_words, cmap='coolwarm', annot=False)
plt.title("Co-occurrence Matrix Heatmap with English Translations")
plt.xlabel("Words")
plt.ylabel("Words")
plt.show() 
```

In response, the model generated fully functional code that includes English translations of the 30 most commonly occurring words from the reviews and a modified portion responsible for visualizing the results. Generative AI already knew the set of most commonly used words, because we asked it to translate them before, but generating code that will assess this list from the output should not be much of a problem.

# 5.4.3 Understanding the output

The results of the co-occurrence analysis presented in listing 5.4 are displayed in figure 5.2. The figure caption was written by generative AI as well.

It is evident from the figure that the two most common word co-occurrences (shown at the top left) are “product-deadline” and “deadline-before,” which confirms our findings from the trigram analysis. It suggests that customers are generally pleased with fast delivery. Additionally, interesting pairs include “great-product,” “excellentproduct,” and “super-recommend,” indicating customer satisfaction with product quality. The only indication of negative sentiment discernible in this figure is the cooccurrence of the words “not” and “received.” Furthermore, we can deduce that most reviews refer to the store or website codenamed “Lannister.”

Overall, these findings are quite remarkable, given the relatively simplistic nature of the analysis conducted.