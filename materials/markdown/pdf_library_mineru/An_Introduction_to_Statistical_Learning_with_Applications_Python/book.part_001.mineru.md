---
type: source
title: An Introduction to Statistical Learning_ with Applications Python
format: mineru-api-markdown
raw_path: materials/raw/pdf_originals/An Introduction to Statistical Learning_ with Applications Python.pdf
mineru_raw_markdown: materials/markdown/pdf_library_mineru/api_raw/An_Introduction_to_Statistical_Learning_with_Applications_Python/part_001/full.md
source_pages: 613
page_range: 1-200
generated: 2026-05-24 12:20:18
status: generated_part
---

Gareth James • Daniela Witten • Trevor Hastie
Robert Tibshirani • Jonathan Taylor

# An Introduction to Statistical Learning

with Applications in Python

First Printing: July 5, 2023

To our parents:

Alison and Michael James

Chiara Nappi and Edward Witten

Valerie and Patrick Hastie

Vera and Sami Tibshirani

John and Brenda Taylor

and to our families:

Michael, Daniel, and Catherine

Tessa, Theo, Otto, and Ari

Samantha, Timothy, and Lynda

Charlie, Ryan, Julie, and Cheryl

Lee-Ann and Isobel

Statistical learning refers to a set of tools for making sense of complex datasets. In recent years, we have seen a staggering increase in the scale and scope of data collection across virtually all areas of science and industry. As a result, statistical learning has become a critical toolkit for anyone who wishes to understand data — and as more and more of today's jobs involve data, this means that statistical learning is fast becoming a critical toolkit for everyone.

One of the first books on statistical learning — The Elements of Statistical Learning (ESL, by Hastie, Tibshirani, and Friedman) — was published in 2001, with a second edition in 2009. ESL has become a popular text not only in statistics but also in related fields. One of the reasons for ESL's popularity is its relatively accessible style. But ESL is best-suited for individuals with advanced training in the mathematical sciences.

An Introduction to Statistical Learning, With Applications in R (ISLR) — first published in 2013, with a second edition in 2021 — arose from the clear need for a broader and less technical treatment of the key topics in statistical learning. In addition to a review of linear regression, ISLR covers many of today's most important statistical and machine learning approaches, including resampling, sparse methods for classification and regression, generalized additive models, tree-based methods, support vector machines, deep learning, survival analysis, clustering, and multiple testing.

Since it was published in 2013, ISLR has become a mainstay of undergraduate and graduate classrooms worldwide, as well as an important reference book for data scientists. One of the keys to its success has been that, beginning with Chapter 2, each chapter contains an R lab illustrating how to implement the statistical learning methods seen in that chapter, providing the reader with valuable hands-on experience.

However, in recent years Python has become an increasingly popular language for data science, and there has been increasing demand for a Pythonbased alternative to ISLR. Hence, this book, An Introduction to Statistical Learning, With Applications in Python (ISLP), covers the same materials as ISLR but with labs implemented in Python — a feat accomplished by the addition of a new co-author, Jonathan Taylor. Several of the labs make use of the ISLP Python package, which we have written to facilitate carrying out the statistical learning methods covered in each chapter in Python. These labs will be useful both for Python novices, as well as experienced users.

The intention behind ISLP (and ISLR) is to concentrate more on the applications of the methods and less on the mathematical details, so it is appropriate for advanced undergraduates or master's students in statistics or related quantitative fields, or for individuals in other disciplines who wish to use statistical learning tools to analyze their data. It can be used as a textbook for a course spanning two semesters.

We are grateful to these readers for providing valuable comments on the first edition of ISLR: Pallavi Basu, Alexandra Chouldechova, Patrick Danaher, Will Fithian, Luella Fu, Sam Gross, Max Grazier G'Sell, Courtney Paulson, Xinghao Qiao, Elisa Sheng, Noah Simon, Kean Ming Tan, Xin Lu Tan. We thank these readers for helpful input on the second edition of ISLR: Alan Agresti, Iain Carmichael, Yiqun Chen, Erin Craig, Daisy Ding, Lucy Gao, Ismael Lemhadri, Bryan Martin, Anna Neufeld, Geoff Tims, Carsten Voelkmann, Steve Yadlowsky, and James Zou. We are immensely grateful to Balasubramanian “Naras” Narasimhan for his assistance on both ISLR and ISLP.

It has been an honor and a privilege for us to see the considerable impact that ISLR has had on the way in which statistical learning is practiced, both in and out of the academic setting. We hope that this new Python edition will continue to give today's and tomorrow's applied statisticians and data scientists the tools they need for success in a data-driven world.

It's tough to make predictions, especially about the future.

-Yogi Berra

# Contents

# Preface vii

# 1 Introduction 1

# 2 Statistical Learning 15

2.1 What Is Statistical Learning? 15

2.1.1 Why Estimate $f$ ? 17   
2.1.2 How Do We Estimate $f$ ? 20   
2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability ..... 23   
2.1.4 Supervised Versus Unsupervised Learning ..... 25   
2.1.5 Regression Versus Classification Problems ..... 27

2.2 Assessing Model Accuracy 27

2.2.1 Measuring the Quality of Fit 28   
2.2.2 The Bias-Variance Trade-Off ..... 31   
2.2.3 The Classification Setting 34

2.3 Lab: Introduction to Python 40

2.3.1 Getting Started 40   
2.3.2 Basic Commands 40   
2.3.3 Introduction to Numerical Python 42   
2.3.4 Graphics 48   
2.3.5 Sequences and Slice Notation 51   
2.3.6 Indexing Data 51   
2.3.7 Loading Data 55   
2.3.8 For Loops 59   
2.3.9 Additional Graphical and Numerical Summaries . . 61

2.4 Exercises 63

# 3 Linear Regression 69

3.1 Simple Linear Regression 70

3.1.1 Estimating the Coefficients 71   
3.1.2 Assessing the Accuracy of the Coefficient Estimates 72   
3.1.3 Assessing the Accuracy of the Model ..... 77

3.2 Multiple Linear Regression 80

3.2.1 Estimating the Regression Coefficients ..... 81

3.2.2 Some Important Questions ..... 83

3.3 Other Considerations in the Regression Model ..... 91

3.3.1 Qualitative Predictors 91

3.3.2 Extensions of the Linear Model 94

3.3.3 Potential Problems 100

3.4 The Marketing Plan 109

3.5 Comparison of Linear Regression with $K$ -Nearest Neighbors 111

3.6 Lab: Linear Regression 116

3.6.1 Importing packages ..... 116

3.6.2 Simple Linear Regression ..... 117

3.6.3 Multiple Linear Regression ..... 122

3.6.4 Multivariate Goodness of Fit 123

3.6.5 Interaction Terms 124

3.6.6 Non-linear Transformations of the Predictors . . . 125

3.6.7 Qualitative Predictors 126

3.7 Exercises 127

# 4 Classification 135

4.1 An Overview of Classification ..... 135

4.2 Why Not Linear Regression? 136

4.3 Logistic Regression 138

4.3.1 The Logistic Model ..... 139

4.3.2 Estimating the Regression Coefficients ..... 140

4.3.3 Making Predictions ..... 141

4.3.4 Multiple Logistic Regression ..... 142

4.3.5 Multinomial Logistic Regression ..... 144

4.4 Generative Models for Classification ..... 146

4.4.1 Linear Discriminant Analysis for $p = 1 \ldots 147$

4.4.2 Linear Discriminant Analysis for $p > 1$ . . . . . . . 150

4.4.3 Quadratic Discriminant Analysis 156

4.4.4 Naive Bayes 158

4.5 A Comparison of Classification Methods ..... 161

4.5.1 An Analytical Comparison ..... 161

4.5.2 An Empirical Comparison 164

4.6 Generalized Linear Models 167

4.6.1 Linear Regression on the Bikeshare Data ..... 167

4.6.2 Poisson Regression on the Bikeshare Data ..... 169

4.6.3 Generalized Linear Models in Greater Generality . 172

4.7 Lab: Logistic Regression, LDA, QDA, and KNN ..... 173

4.7.1 The Stock Market Data 173

4.7.2 Logistic Regression 174

4.7.3 Linear Discriminant Analysis 179

4.7.4 Quadratic Discriminant Analysis 181

4.7.5 Naive Bayes 182

4.7.6 K-Nearest Neighbors 183

4.7.7 Linear and Poisson Regression on the Bikeshare Data188

4.8 Exercises 193

# 5 Resampling Methods 201

5.1 Cross-Validation 202

5.1.1 The Validation Set Approach ..... 202   
5.1.2 Leave-One-Out Cross-Validation 204   
5.1.3 k-Fold Cross-Validation 206   
5.1.4 Bias-Variance Trade-Off for $k$ -Fold Cross-Validation 208   
5.1.5 Cross-Validation on Classification Problems ..... 209

5.2 The Bootstrap 212

5.3 Lab: Cross-Validation and the Bootstrap ..... 215

5.3.1 The Validation Set Approach 216   
5.3.2 Cross-Validation 217   
5.3.3 The Bootstrap 220

5.4 Exercises 224

# 6 Linear Model Selection and Regularization 229

6.1 Subset Selection 231

6.1.1 Best Subset Selection . . . . . . . . . . . . . . . 231   
6.1.2 Stepwise Selection 233   
6.1.3 Choosing the Optimal Model 235

6.2 Shrinkage Methods 240

6.2.1 Ridge Regression 240   
6.2.2 The Lasso 244   
6.2.3 Selecting the Tuning Parameter ..... 252

6.3 Dimension Reduction Methods 253

6.3.1 Principal Components Regression ..... 254   
6.3.2 Partial Least Squares 260

6.4 Considerations in High Dimensions 262

6.4.1 High-Dimensional Data 262   
6.4.2 What Goes Wrong in High Dimensions? ..... 263   
6.4.3 Regression in High Dimensions 265   
6.4.4 Interpreting Results in High Dimensions ..... 266

6.5 Lab: Linear Models and Regularization Methods ..... 267

6.5.1 Subset Selection Methods 268   
6.5.2 Ridge Regression and the Lasso 273   
6.5.3 PCR and PLS Regression 280

6.6 Exercises 283

# 7 Moving Beyond Linearity 289

7.1 Polynomial Regression 290   
7.2 Step Functions 292   
7.3 Basis Functions 293   
7.4 Regression Splines 294

7.4.1 Piecewise Polynomials 294   
7.4.2 Constraints and Splines 296   
7.4.3 The Spline Basis Representation 296   
7.4.4 Choosing the Number and Locations of the Knots . 297   
7.4.5 Comparison to Polynomial Regression ..... 299

7.5 Smoothing Splines 300

7.5.1 An Overview of Smoothing Splines ..... 300   
7.5.2 Choosing the Smoothing Parameter $\lambda$ 301

7.6 Local Regression 303

7.7 Generalized Additive Models 305

7.7.1 GAMs for Regression Problems ..... 306   
7.7.2 GAMs for Classification Problems ..... 308

7.8 Lab: Non-Linear Modeling 309

7.8.1 Polynomial Regression and Step Functions ..... 310   
7.8.2 Splines 315   
7.8.3 Smoothing Splines and GAMs ..... 317   
7.8.4 Local Regression 324

7.9 Exercises 325

# 8 Tree-Based Methods 331

8.1 The Basics of Decision Trees 331

8.1.1 Regression Trees 331   
8.1.2 Classification Trees 337   
8.1.3 Trees Versus Linear Models 341   
8.1.4 Advantages and Disadvantages of Trees ..... 341

8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 343

8.2.1 Bagging 343   
8.2.2 Random Forests . . . . . . . . . . . . . . . . . . 346   
8.2.3 Boosting 347   
8.2.4 Bayesian Additive Regression Trees ..... 350   
8.2.5 Summary of Tree Ensemble Methods ..... 353

8.3 Lab: Tree-Based Methods ..... 354

8.3.1 Fitting Classification Trees ..... 355   
8.3.2 Fitting Regression Trees 358   
8.3.3 Bagging and Random Forests 360   
8.3.4 Boosting 361   
8.3.5 Bayesian Additive Regression Trees ..... 362

8.4 Exercises 363

# 9 Support Vector Machines 367

9.1 Maximal Margin Classifier 367

9.1.1 What Is a Hyperplane? 368   
9.1.2 Classification Using a Separating Hyperplane . . . 368   
9.1.3 The Maximal Margin Classifier ..... 370   
9.1.4 Construction of the Maximal Margin Classifier . . 372   
9.1.5 The Non-separable Case 372

9.2 Support Vector Classifiers ..... 373

9.2.1 Overview of the Support Vector Classifier ..... 373   
9.2.2 Details of the Support Vector Classifier ..... 374

9.3 Support Vector Machines 377

9.3.1 Classification with Non-Linear Decision Boundaries 378   
9.3.2 The Support Vector Machine 379

9.3.3 An Application to the Heart Disease Data ..... 382

9.4 SVMs with More than Two Classes 383

9.4.1 One-Versus-One Classification ..... 384

9.4.2 One-Versus-All Classification 384

9.5 Relationship to Logistic Regression 384

9.6 Lab: Support Vector Machines 387

9.6.1 Support Vector Classifier ..... 387

9.6.2 Support Vector Machine 390

9.6.3 ROC Curves 392

9.6.4 SVM with Multiple Classes 393

9.6.5 Application to Gene Expression Data ..... 394

9.7 Exercises 395

# 10 Deep Learning 399

10.1 Single Layer Neural Networks 400

10.2 Multilayer Neural Networks ..... 402

10.3 Convolutional Neural Networks ..... 406

10.3.1 Convolution Layers 407

10.3.2 Pooling Layers 410

10.3.3 Architecture of a Convolutional Neural Network . . 410

10.3.4 Data Augmentation ..... 411

10.3.5 Results Using a Pretrained Classifier ..... 412

10.4 Document Classification ..... 413

10.5 Recurrent Neural Networks 416

10.5.1 Sequential Models for Document Classification . . 418

10.5.2 Time Series Forecasting 420

10.5.3 Summary of RNNs 424

10.6 When to Use Deep Learning 425

10.7 Fitting a Neural Network 427

10.7.1 Backpropagation 428

10.7.2 Regularization and Stochastic Gradient Descent . . 429

10.7.3 Dropout Learning 431

10.7.4 Network Tuning 431

10.8 Interpolation and Double Descent 432

10.9 Lab: Deep Learning 435

10.9.1 Single Layer Network on Hitters Data ..... 437

10.9.2 Multilayer Network on the MNIST Digit Data . . . 444

10.9.3 Convolutional Neural Networks ..... 448

10.9.4 Using Pretrained CNN Models 452

10.9.5 IMDB Document Classification ..... 454

10.9.6 Recurrent Neural Networks 458

10.10 Exercises 465

# 11 Survival Analysis and Censored Data 469

11.1 Survival and Censoring Times 470

11.2 A Closer Look at Censoring . . . . . . . . . . . . . . . . . 470

11.3 The Kaplan-Meier Survival Curve 472

11.4 The Log-Rank Test 474

11.5 Regression Models With a Survival Response ..... 476

11.5.1 The Hazard Function . . . . . . . . . . . . . . . . 476   
11.5.2 Proportional Hazards 478   
11.5.3 Example: Brain Cancer Data 482   
11.5.4 Example: Publication Data 482

11.6 Shrinkage for the Cox Model 484

11.7 Additional Topics 486

11.7.1 Area Under the Curve for Survival Analysis . . . . 486   
11.7.2 Choice of Time Scale 487   
11.7.3 Time-Dependent Covariates 488   
11.7.4 Checking the Proportional Hazards Assumption . . 488   
11.7.5 Survival Trees 488

11.8 Lab: Survival Analysis ..... 489

11.8.1 Brain Cancer Data 489   
11.8.2 Publication Data 493   
11.8.3 Call Center Data 494

11.9 Exercises 498

# 12 Unsupervised Learning 503

12.1 The Challenge of Unsupervised Learning ..... 503

12.2 Principal Components Analysis ..... 504

12.2.1 What Are Principal Components? ..... 505   
12.2.2 Another Interpretation of Principal Components . 508   
12.2.3 The Proportion of Variance Explained ..... 510   
12.2.4 More on PCA 512   
12.2.5 Other Uses for Principal Components ..... 515

12.3 Missing Values and Matrix Completion ..... 515

12.4 Clustering Methods 520

12.4.1 $K$ -Means Clustering 521   
12.4.2 Hierarchical Clustering ..... 525   
12.4.3 Practical Issues in Clustering 532

12.5 Lab: Unsupervised Learning 535

12.5.1 Principal Components Analysis ..... 535   
12.5.2 Matrix Completion 539   
12.5.3 Clustering 542   
12.5.4 NCI60 Data Example . . . . . . . . . . . . . . . . 546

12.6 Exercises 552

# 13 Multiple Testing 557

13.1 A Quick Review of Hypothesis Testing 558

13.1.1 Testing a Hypothesis 558   
13.1.2 Type I and Type II Errors ..... 562

13.2 The Challenge of Multiple Testing ..... 563

13.3 The Family-Wise Error Rate 565

13.3.1 What is the Family-Wise Error Rate? ..... 565   
13.3.2 Approaches to Control the Family-Wise Error Rate 567   
13.3.3 Trade-Off Between the FWER and Power ..... 572

13.4 The False Discovery Rate . . . . . . . . . . . . . . . . . . . 573

13.4.1 Intuition for the False Discovery Rate ..... 573   
13.4.2 The Benjamini-Hochberg Procedure ..... 575

13.5 A Re-Sampling Approach to $p$ -Values and False Discovery Rates 577

13.5.1 A Re-Sampling Approach to the $p$ -Value . . . . . . 578   
13.5.2 A Re-Sampling Approach to the False Discovery Rate579   
13.5.3 When Are Re-Sampling Approaches Useful? . . . . 581

13.6 Lab: Multiple Testing 583

13.6.1 Review of Hypothesis Tests 583   
13.6.2 Family-Wise Error Rate 585   
13.6.3 False Discovery Rate 588   
13.6.4 A Re-Sampling Approach 590

13.7 Exercises 593

Index

# 1

# Introduction

![](images/cf2e343907325803647d8b376eeb95b322cc7b0e11025cac648dfc6a61cf3c52.jpg)

# An Overview of Statistical Learning

Statistical learning refers to a vast set of tools for understanding data. These tools can be classified as supervised or unsupervised. Broadly speaking, supervised statistical learning involves building a statistical model for predicting, or estimating, an output based on one or more inputs. Problems of this nature occur in fields as diverse as business, medicine, astrophysics, and public policy. With unsupervised statistical learning, there are inputs but no supervising output; nevertheless we can learn relationships and structure from such data. To provide an illustration of some applications of statistical learning, we briefly discuss three real-world data sets that are considered in this book.

# Wage Data

In this application (which we refer to as the Wage data set throughout this book), we examine a number of factors that relate to wages for a group of men from the Atlantic region of the United States. In particular, we wish to understand the association between an employee's age and education, as well as the calendar year, on his wage. Consider, for example, the left-hand panel of Figure 1.1, which displays wage versus age for each of the individuals in the data set. There is evidence that wage increases with age but then decreases again after approximately age 60. The blue line, which provides an estimate of the average wage for a given age, makes this trend clearer. Given an employee's age, we can use this curve to predict his wage. However, it is also clear from Figure 1.1 that there is a significant amount of variability associated with this average value, and so age alone is unlikely to provide an accurate prediction of a particular man's wage.

![](images/4caea96ff4e28145fc3ee5c482671965dd2a8f0309ae6a4ae4e6869aa2716393.jpg)

<details>
<summary>scatter</summary>

| Age | Wage |
| --- | --- |
| 20 | 50 |
| 40 | 100 |
| 60 | 120 |
| 80 | 80 |
</details>

![](images/8071d42469fb727159e986d7eebacfcf6f0e36fa67162db7a77f459c52741220.jpg)

<details>
<summary>bar_line</summary>

| Year | Wage (Median) | Wage (Min) | Wage (Max) |
|------|---------------|------------|------------|
| 2003 | 100           | 50         | 200        |
| 2006 | 100           | 50         | 200        |
| 2009 | 100           | 50         | 200        |
</details>

![](images/dbf4e6bad74f5ace5261f89a714e198022620679113864cb355f2285463e1543.jpg)

<details>
<summary>boxplot</summary>

| Education Level | Wage (Min) | Wage (Q1) | Wage (Median) | Wage (Q3) | Wage (Max) |
| --------------- | ---------- | --------- | ------------- | --------- | ---------- |
| 1               | 40         | 70        | 80            | 90        | 120        |
| 2               | 50         | 90        | 100           | 110       | 160        |
| 3               | 60         | 100       | 110           | 120       | 180        |
| 4               | 70         | 110       | 120           | 130       | 200        |
| 5               | 80         | 120       | 130           | 140       | 220        |
</details>

FIGURE 1.1. Wage data, which contains income survey information for men from the central Atlantic region of the United States. Left: wage as a function of age. On average, wage increases with age until about 60 years of age, at which point it begins to decline. Center: wage as a function of year. There is a slow but steady increase of approximately \$10,000 in the average wage between 2003 and 2009. Right: Boxplots displaying wage as a function of education, with 1 indicating the lowest level (no high school diploma) and 5 the highest level (an advanced graduate degree). On average, wage increases with the level of education.

We also have information regarding each employee's education level and the year in which the wage was earned. The center and right-hand panels of Figure 1.1, which display wage as a function of both year and education, indicate that both of these factors are associated with wage. Wages increase by approximately \$10,000, in a roughly linear (or straight-line) fashion, between 2003 and 2009, though this rise is very slight relative to the variability in the data. Wages are also typically greater for individuals with higher education levels: men with the lowest education level (1) tend to have substantially lower wages than those with the highest education level (5). Clearly, the most accurate prediction of a given man's wage will be obtained by combining his age, his education, and the year. In Chapter 3, we discuss linear regression, which can be used to predict wage from this data set. Ideally, we should predict wage in a way that accounts for the non-linear relationship between wage and age. In Chapter 7, we discuss a class of approaches for addressing this problem.

# Stock Market Data

The Wage data involves predicting a continuous or quantitative output value. This is often referred to as a regression problem. However, in certain cases we may instead wish to predict a non-numerical value—that is, a categorical or qualitative output. For example, in Chapter 4 we examine a stock market data set that contains the daily movements in the Standard & Poor's 500 (S&P) stock index over a 5-year period between 2001 and 2005. We refer to this as the Smarket data. The goal is to predict whether the index will increase or decrease on a given day, using the past 5 days' percentage changes in the index. Here the statistical learning problem does not involve predicting a numerical value. Instead it involves predicting whether a given day's stock market performance will fall into the Up bucket or the Down bucket. This is known as a classification problem. A model that could accurately predict the direction in which the market will move would be very useful!

![](images/14dedf2f3656e4c77e4f50c94b1a2d6788a9df14467e837cae26a55127ab9b2d.jpg)

<details>
<summary>boxplot</summary>

| Today's Direction | Percentage change in S&P |
| ------------------ | ------------------------ |
| Down               | -3.0                     |
| Down               | -2.5                     |
| Down               | -2.0                     |
| Down               | -1.5                     |
| Down               | -1.0                     |
| Down               | -0.5                     |
| Down               | 0.0                      |
| Down               | 0.5                      |
| Down               | 1.0                      |
| Down               | 1.5                      |
| Down               | 2.0                      |
| Down               | 2.5                      |
| Down               | 3.0                      |
| Down               | 3.5                      |
| Down               | 4.0                      |
| Down               | 4.5                      |
| Down               | 5.0                      |
| Up                 | -3.0                     |
| Up                 | -2.5                     |
| Up                 | -2.0                     |
| Up                 | -1.5                     |
| Up                 | -1.0                     |
| Up                 | -0.5                     |
| Up                 | 0.0                      |
| Up                 | 0.5                      |
| Up                 | 1.0                      |
| Up                 | 1.5                      |
| Up                 | 2.0                      |
| Up                 | 2.5                      |
| Up                 | 3.0                      |
| Up                 | 3.5                      |
| Up                 | 4.0                      |
| Up                 | 4.5                      |
| Up                 | 5.0                      |
| Up                 | 5.5                      |
</details>

![](images/1f08dc9995c82ca6dd045cb188fba5c93ee9dd6bcf84f8a4d034bb166f9aab75.jpg)

<details>
<summary>boxplot</summary>

| Today's Direction | Percentage change in S&P |
| ------------------ | ------------------------ |
| Down               | -3.0                     |
| Down               | -2.5                     |
| Down               | -1.0                     |
| Down               | 0.5                      |
| Down               | 1.0                      |
| Up                 | -3.0                     |
| Up                 | -2.0                     |
| Up                 | -1.0                     |
| Up                 | 0.5                      |
| Up                 | 1.0                      |
| Up                 | 2.0                      |
| Up                 | 3.0                      |
| Up                 | 4.0                      |
| Up                 | 5.0                      |
</details>

![](images/9900b645dc4ef59306e7b35d52fcedeb15b450c209587d0166bcd049f7313dcf.jpg)

<details>
<summary>boxplot</summary>

| Today's Direction | Percentage change in S&P |
| ------------------ | ------------------------ |
| Down               | -3.0                     |
| Down               | -2.5                     |
| Down               | -1.0                     |
| Down               | 0.5                      |
| Down               | 1.0                      |
| Up                 | -3.0                     |
| Up                 | -2.5                     |
| Up                 | -1.0                     |
| Up                 | 0.5                      |
| Up                 | 1.0                      |
| Up                 | 2.0                      |
| Up                 | 3.0                      |
| Up                 | 4.0                      |
| Up                 | 5.0                      |
</details>

FIGURE 1.2. Left: Boxplots of the previous day's percentage change in the S&P index for the days for which the market increased or decreased, obtained from the Smarket data. Center and Right: Same as left panel, but the percentage changes for 2 and 3 days previous are shown.

The left-hand panel of Figure 1.2 displays two boxplots of the previous day's percentage changes in the stock index: one for the 648 days for which the market increased on the subsequent day, and one for the 602 days for which the market decreased. The two plots look almost identical, suggesting that there is no simple strategy for using yesterday's movement in the S&P to predict today's returns. The remaining panels, which display boxplots for the percentage changes 2 and 3 days previous to today, similarly indicate little association between past and present returns. Of course, this lack of pattern is to be expected: in the presence of strong correlations between successive days' returns, one could adopt a simple trading strategy to generate profits from the market. Nevertheless, in Chapter 4, we explore these data using several different statistical learning methods. Interestingly, there are hints of some weak trends in the data that suggest that, at least for this 5-year period, it is possible to correctly predict the direction of movement in the market approximately $60\%$ of the time (Figure 1.3).

# Gene Expression Data

The previous two applications illustrate data sets with both input and output variables. However, another important class of problems involves situations in which we only observe input variables, with no corresponding output. For example, in a marketing setting, we might have demographic information for a number of current or potential customers. We may wish to understand which types of customers are similar to each other by grouping individuals according to their observed characteristics. This is known as a clustering problem. Unlike in the previous examples, here we are not trying to predict an output variable.

![](images/71ae5126120af360dc1b47324dcba0f8fea6bf223a45c64504056528963d76fd.jpg)

<details>
<summary>boxplot</summary>

| Today's Direction | Predicted Probability (Min) | Predicted Probability (Q1) | Predicted Probability (Max) |
| ------------------ | --------------------------- | -------------------------- | --------------------------- |
| Down               | 0.46                        | 0.48                       | 0.52                        |
| Up                 | 0.46                        | 0.48                       | 0.52                        |
</details>

FIGURE 1.3. We fit a quadratic discriminant analysis model to the subset of the Smarket data corresponding to the 2001–2004 time period, and predicted the probability of a stock market decrease using the 2005 data. On average, the predicted probability of decrease is higher for the days in which the market does decrease. Based on these results, we are able to correctly predict the direction of movement in the market 60% of the time.

We devote Chapter 12 to a discussion of statistical learning methods for problems in which no natural output variable is available. We consider the NCI60 data set, which consists of 6,830 gene expression measurements for each of 64 cancer cell lines. Instead of predicting a particular output variable, we are interested in determining whether there are groups, or clusters, among the cell lines based on their gene expression measurements. This is a difficult question to address, in part because there are thousands of gene expression measurements per cell line, making it hard to visualize the data.

The left-hand panel of Figure 1.4 addresses this problem by representing each of the 64 cell lines using just two numbers, $Z_{1}$ and $Z_{2}$ . These are the first two principal components of the data, which summarize the 6,830 expression measurements for each cell line down to two numbers or dimensions. While it is likely that this dimension reduction has resulted in some loss of information, it is now possible to visually examine the data for evidence of clustering. Deciding on the number of clusters is often a difficult problem. But the left-hand panel of Figure 1.4 suggests at least four groups of cell lines, which we have represented using separate colors.

In this particular data set, it turns out that the cell lines correspond to 14 different types of cancer. (However, this information was not used to create the left-hand panel of Figure 1.4.) The right-hand panel of Figure 1.4 is identical to the left-hand panel, except that the 14 cancer types are shown using distinct colored symbols. There is clear evidence that cell lines with the same cancer type tend to be located near each other in this two-dimensional representation. In addition, even though the cancer information was not used to produce the left-hand panel, the clustering obtained does bear some resemblance to some of the actual cancer types observed in the right-hand panel. This provides some independent verification of the accuracy of our clustering analysis.

![](images/5761e6136a3a5c219f27ee1b86be370930bfa0ae0b7a6485dea7244d4da2cd5d.jpg)

<details>
<summary>scatter</summary>

| Z1  | Z2  | Color  |
| --- | --- | ------ |
| -45 | -5  | Red    |
| -30 | 10  | Blue   |
| -20 | 5   | Blue   |
| -10 | 15  | Blue   |
| 0   | 0   | Blue   |
| 10  | -5  | Blue   |
| 20  | -10 | Green  |
| 30  | -15 | Green  |
| 40  | -20 | Green  |
| 50  | -25 | Green  |
| 60  | -30 | Green  |
| 70  | -35 | Green  |
| -40 | -10 | Red    |
| -25 | 15  | Blue   |
| -15 | 20  | Blue   |
| -5  | 10  | Blue   |
| 5   | 5   | Blue   |
| 25  | 0   | Blue   |
| 35  | -5  | Blue   |
| 45  | -10 | Blue   |
| 55  | -15 | Blue   |
| 65  | -20 | Blue   |
| -35 | 10  | Blue   |
| -20 | 15  | Blue   |
| -10 | 20  | Blue   |
| 0   | 10  | Blue   |
| 10  | 5   | Blue   |
| 20  | 0   | Blue   |
| 30  | -5  | Blue   |
| 40  | -10 | Blue   |
| 50  | -15 | Blue   |
| 60  | -20 | Blue   |
| -30 | 15  | Blue   |
| -15 | 20  | Blue   |
| -5  | 15  | Blue   |
| 5   | 10  | Blue   |
| 25  | 5   | Blue   |
| 35  | 0   | Blue   |
| 45  | -5  | Blue   |
| 55  | -10 | Blue   |
| 65  | -15 | Blue   |
| -25 | -10 | Blue   |
| -10 | -5  | Blue   |
| -5  | -10 | Blue   |
| 0   | -5  | Blue   |
| 10  | -10 | Blue   |
| 20  | -15 | Blue   |
| 30  | -20 | Blue   |
| 40  | -25 | Blue   |
| 50  | -30 | Blue   |
| 60  | -35 | Blue   |
| -20 | -20 | Blue   |
| -10 | -10 | Blue   |
| -5  | -5  | Blue   |
| 0   | -10 | Blue   |
| 10  | -15 | Blue   |
| 20  | -20 | Blue   |
| 30  | -25 | Blue   |
| 40  | -30 | Blue   |
| 50  | -35 | Blue   |
| 60  | -40 | Blue   |
| -15 | -25 | Blue   |
| -5  | -15 | Blue   |
| -10 | -10 | Blue   |
| -15 | -5  | Blue   |
| -20 | -10 | Blue   |
| -25 | -15 | Blue   |
| -30 | -20 | Blue   |
| -35 | -25 | Blue   |
| -40 | -30 | Blue   |
| -45 | -35 | Blue   |
| -50 | -40 | Blue   |
| -45 | -35 | Red    |
| -35 | -30 | Red    |
| -25 | -25 | Red    |
| -15 | -20 | Red    |
| -5  | -15 | Red    |
| 5   | -10 | Red    |
| 15  | -5  | Red    |
| 25  | 0   | Red    |
| 35  | 5   | Red    |
| 45  | 10  | Red    |
| 55  | 15  | Red    |
| 65  | 20  | Red    |
| -30 | -20 | Red    |
| -15 | -10 | Red    |
| -5  | -5  | Red    |
| -10 | -10 | Red    |
| -15 | -15 | Red    |
| -20 | -20 | Red    |
| -25 | -25 | Red    |
| -30 | -30 | Red    |
| -35 | -35 | Red    |
| -40 | -40 | Red    |
| -45 | -45 | Red    |
| -48.76| -48.76| Red|
| -48.76| -48.76| Green|
| -48.76| -48.76| Green|
| -48.76| -48.76| Green|
| -48.76| -48.76| Green|
| -48.76| -48.76| Green|
| ... (additional values not labeled in the image) are not provided in the code.
</details>

![](images/e72b3e3f2651677ddfe869892ae3132280e6fa875bed8883264dc270dd3b3164.jpg)  
FIGURE 1.4. Left: Representation of the NCI60 gene expression data set in a two-dimensional space, $Z_{1}$ and $Z_{2}$ . Each point corresponds to one of the 64 cell lines. There appear to be four groups of cell lines, which we have represented using different colors. Right: Same as left panel except that we have represented each of the 14 different types of cancer using a different colored symbol. Cell lines corresponding to the same cancer type tend to be nearby in the two-dimensional space.

# A Brief History of Statistical Learning

Though the term statistical learning is fairly new, many of the concepts that underlie the field were developed long ago. At the beginning of the nineteenth century, the method of least squares was developed, implementing the earliest form of what is now known as linear regression. The approach was first successfully applied to problems in astronomy. Linear regression is used for predicting quantitative values, such as an individual's salary. In order to predict qualitative values, such as whether a patient survives or dies, or whether the stock market increases or decreases, linear discriminant analysis was proposed in 1936. In the 1940s, various authors put forth an alternative approach, logistic regression. In the early 1970s, the term generalized linear model was developed to describe an entire class of statistical learning methods that include both linear and logistic regression as special cases.

By the end of the 1970s, many more techniques for learning from data were available. However, they were almost exclusively linear methods because fitting non-linear relationships was computationally difficult at the time. By the 1980s, computing technology had finally improved sufficiently that non-linear methods were no longer computationally prohibitive. In the mid 1980s, classification and regression trees were developed, followed shortly by generalized additive models. Neural networks gained popularity in the 1980s, and support vector machines arose in the 1990s.

Since that time, statistical learning has emerged as a new subfield in statistics, focused on supervised and unsupervised modeling and prediction. In recent years, progress in statistical learning has been marked by the increasing availability of powerful and relatively user-friendly software, such as the popular and freely available Python system. This has the potential to continue the transformation of the field from a set of techniques used and developed by statisticians and computer scientists to an essential toolkit for a much broader community.

# This Book

The Elements of Statistical Learning (ESL) by Hastie, Tibshirani, and Friedman was first published in 2001. Since that time, it has become an important reference on the fundamentals of statistical machine learning. Its success derives from its comprehensive and detailed treatment of many important topics in statistical learning, as well as the fact that (relative to many upper-level statistics textbooks) it is accessible to a wide audience. However, the greatest factor behind the success of ESL has been its topical nature. At the time of its publication, interest in the field of statistical learning was starting to explode. ESL provided one of the first accessible and comprehensive introductions to the topic.

Since ESL was first published, the field of statistical learning has continued to flourish. The field's expansion has taken two forms. The most obvious growth has involved the development of new and improved statistical learning approaches aimed at answering a range of scientific questions across a number of fields. However, the field of statistical learning has also expanded its audience. In the 1990s, increases in computational power generated a surge of interest in the field from non-statisticians who were eager to use cutting-edge statistical tools to analyze their data. Unfortunately, the highly technical nature of these approaches meant that the user community remained primarily restricted to experts in statistics, computer science, and related fields with the training (and time) to understand and implement them.

In recent years, new and improved software packages have significantly eased the implementation burden for many statistical learning methods. At the same time, there has been growing recognition across a number of fields, from business to health care to genetics to the social sciences and beyond, that statistical learning is a powerful tool with important practical applications. As a result, the field has moved from one of primarily academic interest to a mainstream discipline, with an enormous potential audience. This trend will surely continue with the increasing availability of enormous quantities of data and the software to analyze it.

The purpose of An Introduction to Statistical Learning (ISL) is to facilitate the transition of statistical learning from an academic to a mainstream field. ISL is not intended to replace ESL, which is a far more comprehensive text both in terms of the number of approaches considered and the depth to which they are explored. We consider ESL to be an important companion for professionals (with graduate degrees in statistics, machine learning, or related fields) who need to understand the technical details behind statistical learning approaches. However, the community of users of statistical learning techniques has expanded to include individuals with a wider range of interests and backgrounds. Therefore, there is a place for a less technical and more accessible version of ESL.

In teaching these topics over the years, we have discovered that they are of interest to master's and PhD students in fields as disparate as business administration, biology, and computer science, as well as to quantitatively-oriented upper-division undergraduates. It is important for this diverse group to be able to understand the models, intuitions, and strengths and weaknesses of the various approaches. But for this audience, many of the technical details behind statistical learning methods, such as optimization algorithms and theoretical properties, are not of primary interest. We believe that these students do not need a deep understanding of these aspects in order to become informed users of the various methodologies, and in order to contribute to their chosen fields through the use of statistical learning tools.

ISL is based on the following four premises.

1. Many statistical learning methods are relevant and useful in a wide range of academic and non-academic disciplines, beyond just the statistical sciences. We believe that many contemporary statistical learning procedures should, and will, become as widely available and used as is currently the case for classical methods such as linear regression. As a result, rather than attempting to consider every possible approach (an impossible task), we have concentrated on presenting the methods that we believe are most widely applicable.   
2. Statistical learning should not be viewed as a series of black boxes. No single approach will perform well in all possible applications. Without understanding all of the cogs inside the box, or the interaction between those cogs, it is impossible to select the best box. Hence, we have attempted to carefully describe the model, intuition, assumptions, and trade-offs behind each of the methods that we consider.   
3. While it is important to know what job is performed by each cog, it is not necessary to have the skills to construct the machine inside the box! Thus, we have minimized discussion of technical details related to fitting procedures and theoretical properties. We assume that the reader is comfortable with basic mathematical concepts, but we do not assume a graduate degree in the mathematical sciences. For instance, we have almost completely avoided the use of matrix algebra, and it is possible to understand the entire book without a detailed knowledge of matrices and vectors.   
4. We presume that the reader is interested in applying statistical learning methods to real-world problems. In order to facilitate this, as well as to motivate the techniques discussed, we have devoted a section within each chapter to computer labs. In each lab, we walk the reader through a realistic application of the methods considered in that chapter. When we have taught this material in our courses, we have allocated roughly one-third of classroom time to working through the labs, and we have found them to be extremely useful. Many of the less computationally-oriented students who were initially intimidated by the labs got the hang of things over the course of the quarter or semester. This book originally appeared (2013, second edition 2021)

with computer labs written in the R language. Since then, there has been increasing demand for Python implementations of the important techniques in statistical learning. Consequently, this version has labs in Python. There are a rapidly growing number of Python packages available, and by examination of the imports at the beginning of each lab, readers will see that we have carefully selected and used the most appropriate. We have also supplied some additional code and functionality in our package ISLP. However, the labs in ISL are self-contained, and can be skipped if the reader wishes to use a different software package or does not wish to apply the methods discussed to real-world problems.

# Who Should Read This Book?

This book is intended for anyone who is interested in using modern statistical methods for modeling and prediction from data. This group includes scientists, engineers, data analysts, data scientists, and quants, but also less technical individuals with degrees in non-quantitative fields such as the social sciences or business. We expect that the reader will have had at least one elementary course in statistics. Background in linear regression is also useful, though not required, since we review the key concepts behind linear regression in Chapter 3. The mathematical level of this book is modest, and a detailed knowledge of matrix operations is not required. This book provides an introduction to Python. Previous exposure to a programming language, such as MATLAB or R, is useful but not required.

The first edition of this textbook has been used to teach master's and PhD students in business, economics, computer science, biology, earth sciences, psychology, and many other areas of the physical and social sciences. It has also been used to teach advanced undergraduates who have already taken a course on linear regression. In the context of a more mathematically rigorous course in which ESL serves as the primary textbook, ISL could be used as a supplementary text for teaching computational aspects of the various approaches.

# Notation and Simple Matrix Algebra

Choosing notation for a textbook is always a difficult task. For the most part we adopt the same notational conventions as ESL.

We will use n to represent the number of distinct data points, or observations, in our sample. We will let p denote the number of variables that are available for use in making predictions. For example, the Wage data set consists of 11 variables for 3,000 people, so we have n = 3,000 observations and p = 11 variables (such as year, age, race, and more). Note that throughout this book, we indicate variable names using colored font: Variable Name.

In some examples, p might be quite large, such as on the order of thousands or even millions; this situation arises quite often, for example, in the analysis of modern biological data or web-based advertising data.

In general, we will let $x_{ij}$ represent the value of the jth variable for the ith observation, where $i = 1, 2, \ldots, n$ and $j = 1, 2, \ldots, p$ . Throughout this book, i will be used to index the samples or observations (from 1 to n) and j will be used to index the variables (from 1 to p). We let X denote an $n \times p$ matrix whose $(i, j)$ th element is $x_{ij}$ . That is,

$$
\mathbf {X} = \left( \begin{array}{c c c c} x _ {1 1} & x _ {1 2} & \ldots & x _ {1 p} \\ x _ {2 1} & x _ {2 2} & \ldots & x _ {2 p} \\ \vdots & \vdots & \ddots & \vdots \\ x _ {n 1} & x _ {n 2} & \ldots & x _ {n p} \end{array} \right).
$$

For readers who are unfamiliar with matrices, it is useful to visualize $\mathbf{X}$ as a spreadsheet of numbers with $n$ rows and $p$ columns.

At times we will be interested in the rows of X, which we write as $x_{1}, x_{2}, \ldots, x_{n}$ . Here $x_{i}$ is a vector of length p, containing the p variable measurements for the ith observation. That is,

$$
x _ {i} = \left( \begin{array}{c} x _ {i 1} \\ x _ {i 2} \\ \vdots \\ x _ {i p} \end{array} \right). \tag {1.1}
$$

(Vectors are by default represented as columns.) For example, for the Wage data, $x_{i}$ is a vector of length 11, consisting of year, age, race, and other values for the ith individual. At other times we will instead be interested in the columns of X, which we write as $x_{1}, x_{2}, \ldots, x_{p}$ . Each is a vector of length n. That is,

$$
\mathbf {x} _ {j} = \left( \begin{array}{c} x _ {1 j} \\ x _ {2 j} \\ \vdots \\ x _ {n j} \end{array} \right).
$$

For example, for the Wage data, $x_{1}$ contains the n = 3,000 values for year. Using this notation, the matrix X can be written as

$$
\mathbf {X} = \left( \begin{array}{c c c c} \mathbf {x} _ {1} & \mathbf {x} _ {2} & \dots & \mathbf {x} _ {p} \end{array} \right),
$$

or

$$
\mathbf {X} = \left( \begin{array}{c} x _ {1} ^ {T} \\ x _ {2} ^ {T} \\ \vdots \\ x _ {n} ^ {T} \end{array} \right).
$$

The $^T$ notation denotes the transpose of a matrix or vector. So, for example,

$$
\mathbf {X} ^ {T} = \left( \begin{array}{c c c c} x _ {1 1} & x _ {2 1} & \ldots & x _ {n 1} \\ x _ {1 2} & x _ {2 2} & \ldots & x _ {n 2} \\ \vdots & \vdots & & \vdots \\ x _ {1 p} & x _ {2 p} & \ldots & x _ {n p} \end{array} \right),
$$

while

$$
x _ {i} ^ {T} = \left( \begin{array}{c c c c} x _ {i 1} & x _ {i 2} & \dots & x _ {i p} \end{array} \right).
$$

We use $y_{i}$ to denote the ith observation of the variable on which we wish to make predictions, such as wage. Hence, we write the set of all n observations in vector form as

$$
\mathbf {y} = \left( \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {n} \end{array} \right).
$$

Then our observed data consists of $\{(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)\}$ , where each $x_i$ is a vector of length $p$ . (If $p = 1$ , then $x_i$ is simply a scalar.)

In this text, a vector of length $n$ will always be denoted in lower case bold; e.g.

$$
\mathbf {a} = \left( \begin{array}{c} a _ {1} \\ a _ {2} \\ \vdots \\ a _ {n} \end{array} \right).
$$

However, vectors that are not of length n (such as feature vectors of length p, as in $(1.1)$ ) will be denoted in lower case normal font, e.g. a. Scalars will also be denoted in lower case normal font, e.g. a. In the rare cases in which these two uses for lower case normal font lead to ambiguity, we will clarify which use is intended. Matrices will be denoted using bold capitals, such as A. Random variables will be denoted using capital normal font, e.g. A, regardless of their dimensions.

Occasionally we will want to indicate the dimension of a particular object. To indicate that an object is a scalar, we will use the notation $a \in R$ . To indicate that it is a vector of length k, we will use $a \in R^{k}$ (or $a \in R^{n}$ if it is of length n). We will indicate that an object is an $r \times s$ matrix using $A \in R^{r \times s}$ .

We have avoided using matrix algebra whenever possible. However, in a few instances it becomes too cumbersome to avoid it entirely. In these rare instances it is important to understand the concept of multiplying two matrices. Suppose that $A \in R^{r \times d}$ and $B \in R^{d \times s}$ . Then the product of A and B is denoted AB. The $(i,j)$ th element of AB is computed by multiplying each element of the ith row of A by the corresponding element of the jth column of B. That is, $(\mathbf{AB})_{ij} = \sum_{k=1}^{d} a_{ik} b_{kj}$ . As an example, consider

$$
\mathbf {A} = \left( \begin{array}{c c} 1 & 2 \\ 3 & 4 \end{array} \right) \quad \text {and} \quad \mathbf {B} = \left( \begin{array}{c c} 5 & 6 \\ 7 & 8 \end{array} \right).
$$

Then

$$
\mathbf {A B} = \left( \begin{array}{c c} 1 & 2 \\ 3 & 4 \end{array} \right) \left( \begin{array}{c c} 5 & 6 \\ 7 & 8 \end{array} \right) = \left( \begin{array}{c c} 1 \times 5 + 2 \times 7 & 1 \times 6 + 2 \times 8 \\ 3 \times 5 + 4 \times 7 & 3 \times 6 + 4 \times 8 \end{array} \right) = \left( \begin{array}{c c} 1 9 & 2 2 \\ 4 3 & 5 0 \end{array} \right).
$$

Note that this operation produces an $r \times s$ matrix. It is only possible to compute AB if the number of columns of A is the same as the number of rows of B.

# Organization of This Book

Chapter 2 introduces the basic terminology and concepts behind statistical learning. This chapter also presents the K-nearest neighbor classifier, a very simple method that works surprisingly well on many problems. Chapters 3 and 4 cover classical linear methods for regression and classification. In particular, Chapter 3 reviews linear regression, the fundamental starting point for all regression methods. In Chapter 4 we discuss two of the most important classical classification methods, logistic regression and linear discriminant analysis.

A central problem in all statistical learning situations involves choosing the best method for a given application. Hence, in Chapter 5 we introduce cross-validation and the bootstrap, which can be used to estimate the accuracy of a number of different methods in order to choose the best one.

Much of the recent research in statistical learning has concentrated on non-linear methods. However, linear methods often have advantages over their non-linear competitors in terms of interpretability and sometimes also accuracy. Hence, in Chapter 6 we consider a host of linear methods, both classical and more modern, which offer potential improvements over standard linear regression. These include stepwise selection, ridge regression, principal components regression, and the lasso.

The remaining chapters move into the world of non-linear statistical learning. We first introduce in Chapter 7 a number of non-linear methods that work well for problems with a single input variable. We then show how these methods can be used to fit non-linear additive models for which there is more than one input. In Chapter 8, we investigate tree-based methods, including bagging, boosting, and random forests. Support vector machines, a set of approaches for performing both linear and non-linear classification, are discussed in Chapter 9. We cover deep learning, an approach for non-linear regression and classification that has received a lot of attention in recent years, in Chapter 10. Chapter 11 explores survival analysis, a regression approach that is specialized to the setting in which the output variable is censored, i.e. not fully observed.

In Chapter 12, we consider the unsupervised setting in which we have input variables but no output variable. In particular, we present principal components analysis, K-means clustering, and hierarchical clustering. Finally, in Chapter 13 we cover the very important topic of multiple hypothesis testing.

At the end of each chapter, we present one or more Python lab sections in which we systematically work through applications of the various methods discussed in that chapter. These labs demonstrate the strengths and weaknesses of the various approaches, and also provide a useful reference for the syntax required to implement the various methods. The reader may choose to work through the labs at their own pace, or the labs may be the focus of group sessions as part of a classroom environment. Within each Python lab, we present the results that we obtained when we performed the lab at the time of writing this book. However, new versions of Python are continuously released, and over time, the packages called in the labs will be updated. Therefore, in the future, it is possible that the results shown in the lab sections may no longer correspond precisely to the results obtained by the reader who performs the labs. As necessary, we will post updates to the labs on the book website.

<table><tr><td>Name</td><td>Description</td></tr><tr><td>Auto</td><td>Gas mileage, horsepower, and other information for cars.</td></tr><tr><td>Bikeshare</td><td>Hourly usage of a bike sharing program in Washington, DC.</td></tr><tr><td>Boston</td><td>Housing values and other information about Boston census tracts.</td></tr><tr><td>BrainCancer</td><td>Survival times for patients diagnosed with brain cancer.</td></tr><tr><td>Caravan</td><td>Information about individuals offered caravan insurance.</td></tr><tr><td>Carseats</td><td>Information about car seat sales in 400 stores.</td></tr><tr><td>College</td><td>Demographic characteristics, tuition, and more for USA colleges.</td></tr><tr><td>Credit</td><td>Information about credit card debt for 400 customers.</td></tr><tr><td>Default</td><td>Customer default records for a credit card company.</td></tr><tr><td>Fund</td><td>Returns of 2,000 hedge fund managers over 50 months.</td></tr><tr><td>Hitters</td><td>Records and salaries for baseball players.</td></tr><tr><td>Khan</td><td>Gene expression measurements for four cancer types.</td></tr><tr><td>NCI60</td><td>Gene expression measurements for 64 cancer cell lines.</td></tr><tr><td>NYSE</td><td>Returns, volatility, and volume for the New York Stock Exchange.</td></tr><tr><td>OJ</td><td>Sales information for Citrus Hill and Minute Maid orange juice.</td></tr><tr><td>Portfolio</td><td>Past values of financial assets, for use in portfolio allocation.</td></tr><tr><td>Publication</td><td>Time to publication for 244 clinical trials.</td></tr><tr><td>Smarket</td><td>Daily percentage returns for S&amp;P 500 over a 5-year period.</td></tr><tr><td>USArrests</td><td>Crime statistics per 100,000 residents in 50 states of USA.</td></tr><tr><td>Wage</td><td>Income survey data for men in central Atlantic region of USA.</td></tr><tr><td>Weekly</td><td>1,089 weekly stock market returns for 21 years.</td></tr></table>

TABLE 1.1. A list of data sets needed to perform the labs and exercises in this textbook. All data sets are available in the ISLP package, with the exception of USArrests, which is part of the base R distribution, but accessible from Python.

We use the ⚙ symbol to denote sections or exercises that contain more challenging concepts. These can be easily skipped by readers who do not wish to delve as deeply into the material, or who lack the mathematical background.

# Data Sets Used in Labs and Exercises

In this textbook, we illustrate statistical learning methods using applications from marketing, finance, biology, and other areas. The ISLP package contains a number of data sets that are required in order to perform the labs and exercises associated with this book. One other data set is part of the base R distribution (the USArrests data), and we show how to access it from Python in Section 12.5.1. Table 1.1 contains a summary of the data sets required to perform the labs and exercises. A couple of these data sets are also available as text files on the book website, for use in Chapter 2.

# Book Website

The website for this book is located at

www.statlearning.com

It contains a number of resources, including the Python package associated with this book, and some additional data sets.

# Acknowledgements

A few of the plots in this book were taken from ESL: Figures 6.7, 8.3, and 12.14. All other plots were produced for the R version of ISL, except for Figure 13.10 which differs because of the Python software supporting the plot.

# 2

# Statistical Learning

![](images/e6673d90e565b41c7f69f746c92bc187daca3467a5923867a7909520f1fe002a.jpg)

# 2.1 What Is Statistical Learning?

In order to motivate our study of statistical learning, we begin with a simple example. Suppose that we are statistical consultants hired by a client to investigate the association between advertising and sales of a particular product. The Advertising data set consists of the sales of that product in 200 different markets, along with advertising budgets for the product in each of those markets for three different media: TV, radio, and newspaper. The data are displayed in Figure 2.1. It is not possible for our client to directly increase sales of the product. On the other hand, they can control the advertising expenditure in each of the three media. Therefore, if we determine that there is an association between advertising and sales, then we can instruct our client to adjust advertising budgets, thereby indirectly increasing sales. In other words, our goal is to develop an accurate model that can be used to predict sales on the basis of the three media budgets.

In this setting, the advertising budgets are input variables while sales is an output variable. The input variables are typically denoted using the symbol X, with a subscript to distinguish them. So $X_{1}$ might be the TV budget, $X_{2}$ the radio budget, and $X_{3}$ the newspaper budget. The inputs go by different names, such as predictors, independent variables, features, or sometimes just variables. The output variable—in this case, sales—is often called the response or dependent variable, and is typically denoted using the symbol Y. Throughout this book, we will use all of these terms interchangeably.

More generally, suppose that we observe a quantitative response Y and p different predictors, $X_{1}, X_{2}, \ldots, X_{p}$ . We assume that there is some relationship between Y and $X = (X_{1}, X_{2}, \ldots, X_{p})$ , which can be written in the very general form

$$
Y = f (X) + \epsilon . \tag {2.1}
$$

input
variable
output
variable
predictor
independent
variable
feature
variable
response
dependent
variable

![](images/7cce57d248865f92c4275f571b7565e5605dc8891add20543f270f5575effba6.jpg)

<details>
<summary>scatter</summary>

| TV  | Sales |
| --- | ----- |
| 0   | 2     |
| 50  | 8     |
| 100 | 12    |
| 150 | 16    |
| 200 | 20    |
| 250 | 24    |
| 300 | 26    |
</details>

![](images/a9664a8d3acfb0e0bb7f73a30cf8aa02670a16c726ffef17b120c25e3ca02eb7.jpg)

<details>
<summary>scatter</summary>

| Radio | Sales |
|-------|-------|
| 0     | 8     |
| 5     | 10    |
| 10    | 12    |
| 15    | 14    |
| 20    | 16    |
| 25    | 18    |
| 30    | 20    |
| 35    | 22    |
| 40    | 24    |
| 45    | 26    |
| 50    | 28    |
</details>

![](images/c8db097667ab1b6b5a2ce68fb6805d8d72e609b1ab8d46a948aa4486fcccee5f.jpg)

<details>
<summary>scatter</summary>

| Newspaper | Sales |
| --------- | ----- |
| 0         | 10    |
| 10        | 12    |
| 20        | 14    |
| 30        | 16    |
| 40        | 18    |
| 50        | 20    |
| 60        | 22    |
| 70        | 24    |
| 80        | 26    |
| 90        | 28    |
| 100       | 30    |
</details>

FIGURE 2.1. The Advertising data set. The plot displays sales, in thousands of units, as a function of TV, radio, and newspaper budgets, in thousands of dollars, for 200 different markets. In each plot we show the simple least squares fit of sales to that variable, as described in Chapter 3. In other words, each blue line represents a simple model that can be used to predict sales using TV, radio, and newspaper, respectively.

Here f is some fixed but unknown function of $X_{1},\ldots,X_{p}$ , and $\epsilon$ is a random error term, which is independent of X and has mean zero. In this formulation, f represents the systematic information that X provides about Y. error term systematic

![](images/0d1aba4958a2ad044231eebd0573fcaeffec6d44ba95db6a00d601e5362f0c12.jpg)

<details>
<summary>scatter</summary>

| Years of Education | Income |
| ------------------ | ------ |
| 10                 | 25     |
| 11                 | 22     |
| 12                 | 18     |
| 13                 | 26     |
| 14                 | 35     |
| 15                 | 40     |
| 16                 | 45     |
| 17                 | 50     |
| 18                 | 58     |
| 19                 | 65     |
| 20                 | 70     |
| 21                 | 75     |
| 22                 | 80     |
</details>

![](images/92399f7e2b5ca8ff63a2e7abdaa674d0555dead3252dee614cd1279942ab501c.jpg)

<details>
<summary>line</summary>

| Years of Education | Income |
| ------------------ | ------ |
| 10                 | 25     |
| 11                 | 22     |
| 12                 | 18     |
| 13                 | 25     |
| 14                 | 35     |
| 15                 | 45     |
| 16                 | 55     |
| 17                 | 65     |
| 18                 | 70     |
| 19                 | 75     |
| 20                 | 78     |
| 21                 | 77     |
| 22                 | 80     |
</details>

FIGURE 2.2. The Income data set. Left: The red dots are the observed values of income (in thousands of dollars) and years of education for 30 individuals. Right: The blue curve represents the true underlying relationship between income and years of education, which is generally unknown (but is known in this case because the data were simulated). The black lines represent the error associated with each observation. Note that some errors are positive (if an observation lies above the blue curve) and some are negative (if an observation lies below the curve). Overall, these errors have approximately mean zero.

As another example, consider the left-hand panel of Figure 2.2, a plot of income versus years of education for 30 individuals in the Income data set. The plot suggests that one might be able to predict income using years of education. However, the function f that connects the input variable to the output variable is in general unknown. In this situation one must estimate f based on the observed points. Since Income is a simulated data set, f is known and is shown by the blue curve in the right-hand panel of Figure 2.2. The vertical lines represent the error terms $\epsilon$ . We note that some of the 30 observations lie above the blue curve and some lie below it; overall, the errors have approximately mean zero.

In general, the function f may involve more than one input variable. In Figure 2.3 we plot income as a function of years of education and seniority. Here f is a two-dimensional surface that must be estimated based on the observed data.

In essence, statistical learning refers to a set of approaches for estimating f. In this chapter we outline some of the key theoretical concepts that arise in estimating f, as well as tools for evaluating the estimates obtained.

# 2.1.1 Why Estimate f?

There are two main reasons that we may wish to estimate $f$ : prediction and inference. We discuss each in turn.

# Prediction

In many situations, a set of inputs X are readily available, but the output Y cannot be easily obtained. In this setting, since the error term averages to zero, we can predict Y using

$$
\hat {Y} = \hat {f} (X), \tag {2.2}
$$

where $\hat{f}$ represents our estimate for f, and $\hat{Y}$ represents the resulting prediction for Y. In this setting, $\hat{f}$ is often treated as a black box, in the sense that one is not typically concerned with the exact form of $\hat{f}$ , provided that it yields accurate predictions for Y.

As an example, suppose that $X_{1}, \ldots, X_{p}$ are characteristics of a patient's blood sample that can be easily measured in a lab, and $Y$ is a variable encoding the patient's risk for a severe adverse reaction to a particular drug. It is natural to seek to predict $Y$ using $X$ , since we can then avoid giving the drug in question to patients who are at high risk of an adverse reaction—that is, patients for whom the estimate of $Y$ is high.

The accuracy of $\hat{Y}$ as a prediction for Y depends on two quantities, which we will call the reducible error and the irreducible error. In general, $\hat{f}$ will not be a perfect estimate for f, and this inaccuracy will introduce some error. This error is reducible because we can potentially improve the accuracy of $\hat{f}$ by using the most appropriate statistical learning technique to estimate f. However, even if it were possible to form a perfect estimate for f, so that our estimated response took the form $\hat{Y} = f(X)$ , our prediction would still have some error in it! This is because Y is also a function of $\epsilon$ , which, by definition, cannot be predicted using X. Therefore, variability associated with $\epsilon$ also affects the accuracy of our predictions. This is known as the irreducible error, because no matter how well we estimate f, we cannot reduce the error introduced by $\epsilon$ .

Why is the irreducible error larger than zero? The quantity $\epsilon$ may contain unmeasured variables that are useful in predicting $Y$ : since we don't measure them, $f$ cannot use them for its prediction. The quantity $\epsilon$ may also contain unmeasurable variation. For example, the risk of an adverse reaction might vary for a given patient on a given day, depending on manufacturing variation in the drug itself or the patient's general feeling of well-being on that day.

![](images/3b195f97ee6321eb801149ffb927e9537ec54deef95729056fcd25d1513c7c9f.jpg)

<details>
<summary>scatter</summary>

| Years of Education | Income | Seniority |
| ------------------ | ------ | --------- |
| 0                  | 0      | 0         |
| 1                  | 1      | 1         |
| 2                  | 2      | 2         |
| 3                  | 3      | 3         |
| 4                  | 4      | 4         |
| 5                  | 5      | 5         |
| 6                  | 6      | 6         |
| 7                  | 7      | 7         |
| 8                  | 8      | 8         |
| 9                  | 9      | 9         |
| 10                 | 10     | 10        |
| 11                 | 11     | 11        |
| 12                 | 12     | 12        |
| 13                 | 13     | 13        |
| 14                 | 14     | 14        |
| 15                 | 15     | 15        |
| 16                 | 16     | 16        |
| 17                 | 17     | 17        |
| 18                 | 18     | 18        |
| 19                 | 19     | 19        |
| 20                 | 20     | 20        |
| 21                 | 21     | 21        |
| 22                 | 22     | 22        |
| 23                 | 23     | 23        |
| 24                 | 24     | 24        |
| 25                 | 25     | 25        |
| 26                 | 26     | 26        |
| 27                 | 27     | 27        |
| 28                 | 28     | 28        |
| 29                 | 29     | 29        |
| 30                 | 30     | 30        |
| 31                 | 31     | 31        |
| 32                 | 32     | 32        |
| 33                 | 33     | 33        |
| 34                 | 34     | 34        |
| 35                 | 35     | 35        |
| 36                 | 36     | 36        |
| 37                 | 37     | 37        |
| 38                 | 38     | 38        |
| 39                 | 39     | 39        |
| 40                 | 40     | 40        |
| 41                 | 41     | 41        |
| 42                 | 42     | 42        |
| 43                 | 43     | 43        |
| 44                 | 44     | 44        |
| 45                 | 45     | 45        |
| 46                 | 46     | 46        |
| 47                 | 47     | 47        |
| 48                 | 48     | 48        |
| 49                 | 49     | 49        |
| 50                 | 50     | 50        |
| Note: The data is not explicitly provided in the code. The box plot does not have explicit labels for the axes. The box plot is labeled 'Income' and 'Seniority'. The legend is not explicitly labeled but corresponds to the color scheme used in the box plot.
</details>

FIGURE 2.3. The plot displays income as a function of years of education and seniority in the Income data set. The blue surface represents the true underlying relationship between income and years of education and seniority, which is known since the data are simulated. The red dots indicate the observed values of these quantities for 30 individuals.

Consider a given estimate $\hat{f}$ and a set of predictors X, which yields the prediction $\hat{Y} = \hat{f}(X)$ . Assume for a moment that both $\hat{f}$ and X are fixed, so that the only variability comes from $\epsilon$ . Then, it is easy to show that

$$
\begin{array}{l} \operatorname{E} (Y - \hat {Y}) ^ {2} = \operatorname{E} [ f (X) + \epsilon - \hat {f} (X) ] ^ {2} \\ = \underbrace {[ f (X) - \hat {f} (X) ] ^ {2}} _ {\text { Reducible }} + \underbrace {\operatorname{Var} (\epsilon)} _ {\text { Irreducible }}, \tag {2.3} \\ \end{array}
$$

where $\mathrm{E}(Y-\hat{Y})^{2}$ represents the average, or expected value, of the squared difference between the predicted and actual value of Y, and $\operatorname{Var}(\epsilon)$ represents the variance associated with the error term $\epsilon$ .

The focus of this book is on techniques for estimating f with the aim of minimizing the reducible error. It is important to keep in mind that the irreducible error will always provide an upper bound on the accuracy of our prediction for Y. This bound is almost always unknown in practice.

expected
value
variance

# Inference

We are often interested in understanding the association between Y and $X_{1},\ldots,X_{p}$ . In this situation we wish to estimate f, but our goal is not necessarily to make predictions for Y. Now $\hat{f}$ cannot be treated as a black box, because we need to know its exact form. In this setting, one may be interested in answering the following questions:

\- Which predictors are associated with the response? It is often the case that only a small fraction of the available predictors are substantially associated with Y. Identifying the few important predictors among a large set of possible variables can be extremely useful, depending on the application.

\- What is the relationship between the response and each predictor? Some predictors may have a positive relationship with $Y$ , in the sense that larger values of the predictor are associated with larger values of $Y$ . Other predictors may have the opposite relationship. Depending on the complexity of $f$ , the relationship between the response and a given predictor may also depend on the values of the other predictors.

\- Can the relationship between Y and each predictor be adequately summarized using a linear equation, or is the relationship more complicated? Historically, most methods for estimating f have taken a linear form. In some situations, such an assumption is reasonable or even desirable. But often the true relationship is more complicated, in which case a linear model may not provide an accurate representation of the relationship between the input and output variables.

In this book, we will see a number of examples that fall into the prediction setting, the inference setting, or a combination of the two.

For instance, consider a company that is interested in conducting a direct-marketing campaign. The goal is to identify individuals who are likely to respond positively to a mailing, based on observations of demographic variables measured on each individual. In this case, the demographic variables serve as predictors, and response to the marketing campaign (either positive or negative) serves as the outcome. The company is not interested in obtaining a deep understanding of the relationships between each individual predictor and the response; instead, the company simply wants to accurately predict the response using the predictors. This is an example of modeling for prediction.

In contrast, consider the Advertising data illustrated in Figure 2.1. One may be interested in answering questions such as:

- Which media are associated with sales?   
- Which media generate the biggest boost in sales? or   
- How large of an increase in sales is associated with a given increase in TV advertising?

This situation falls into the inference paradigm. Another example involves modeling the brand of a product that a customer might purchase based on variables such as price, store location, discount levels, competition price, and so forth. In this situation one might really be most interested in the association between each variable and the probability of purchase. For instance, to what extent is the product's price associated with sales? This is an example of modeling for inference.

Finally, some modeling could be conducted both for prediction and inference. For example, in a real estate setting, one may seek to relate values of homes to inputs such as crime rate, zoning, distance from a river, air quality, schools, income level of community, size of houses, and so forth. In this case one might be interested in the association between each individual input variable and housing price—for instance, how much extra will a house be worth if it has a view of the river? This is an inference problem. Alternatively, one may simply be interested in predicting the value of a home given its characteristics: is this house under- or over-valued? This is a prediction problem.

Depending on whether our ultimate goal is prediction, inference, or a combination of the two, different methods for estimating f may be appropriate. For example, linear models allow for relatively simple and interpretable inference, but may not yield as accurate predictions as some other approaches. In contrast, some of the highly non-linear approaches that we discuss in the later chapters of this book can potentially provide quite accurate predictions for Y, but this comes at the expense of a less interpretable model for which inference is more challenging.

linear model

# 2.1.2 How Do We Estimate $f$ ?

Throughout this book, we explore many linear and non-linear approaches for estimating f. However, these methods generally share certain characteristics. We provide an overview of these shared characteristics in this section. We will always assume that we have observed a set of n different data points. For example in Figure 2.2 we observed n = 30 data points. These observations are called the training data because we will use these observations to train, or teach, our method how to estimate f. Let $x_{ij}$ represent the value of the jth predictor, or input, for observation i, where $i = 1, 2, \ldots, n$ and $j = 1, 2, \ldots, p$ . Correspondingly, let $y_i$ represent the response variable for the ith observation. Then our training data consist of $\{(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)\}$ where $x_i = (x_{i1}, x_{i2}, \ldots, x_{ip})^T$ .

Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function f. In other words, we want to find a function $\hat{f}$ such that $Y \approx \hat{f}(X)$ for any observation $(X, Y)$ . Broadly speaking, most statistical learning methods for this task can be characterized as either parametric or non-parametric. We now briefly discuss these two types of approaches.

training data

parametric non-parametric

# Parametric Methods

Parametric methods involve a two-step model-based approach.

1. First, we make an assumption about the functional form, or shape, of $f$ . For example, one very simple assumption is that $f$ is linear in $X$ :

$$
f (X) = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \dots + \beta_ {p} X _ {p}. \tag {2.4}
$$

This is a linear model, which will be discussed extensively in Chapter 3. Once we have assumed that $f$ is linear, the problem of estimating $f$ is greatly simplified. Instead of having to estimate an entirely arbitrary $p$ -dimensional function $f(X)$ , one only needs to estimate the $p + 1$ coefficients $\beta_0, \beta_1, \ldots, \beta_p$ .

![](images/f116d5a279e9f1d7cf5e87fb56713f5dcc3eb3cc9cced18b0fb88b87cc0ceae8.jpg)

<details>
<summary>scatter</summary>

| Years of Education | Income | Seniority |
| ------------------ | ------ | --------- |
| 1                  | 0.5    | 0.2       |
| 2                  | 0.6    | 0.3       |
| 3                  | 0.7    | 0.4       |
| 4                  | 0.8    | 0.5       |
| 5                  | 0.9    | 0.6       |
| 6                  | 1.0    | 0.7       |
| 7                  | 1.1    | 0.8       |
| 8                  | 1.2    | 0.9       |
| 9                  | 1.3    | 1.0       |
| 10                 | 1.4    | 1.1       |
| 11                 | 1.5    | 1.2       |
| 12                 | 1.6    | 1.3       |
| 13                 | 1.7    | 1.4       |
| 14                 | 1.8    | 1.5       |
| 15                 | 1.9    | 1.6       |
| 16                 | 2.0    | 1.7       |
| 17                 | 2.1    | 1.8       |
| 18                 | 2.2    | 1.9       |
| 19                 | 2.3    | 2.0       |
| 20                 | 2.4    | 2.1       |
| 21                 | 2.5    | 2.2       |
| 22                 | 2.6    | 2.3       |
| 23                 | 2.7    | 2.4       |
| 24                 | 2.8    | 2.5       |
| 25                 | 2.9    | 2.6       |
| 26                 | 3.0    | 2.7       |
| 27                 | 3.1    | 2.8       |
| 28                 | 3.2    | 2.9       |
| 29                 | 3.3    | 3.0       |
| 30                 | 3.4    | 3.1       |
| 31                 | 3.5    | 3.2       |
| 32                 | 3.6    | 3.3       |
| 33                 | 3.7    | 3.4       |
| 34                 | 3.8    | 3.5       |
| 35                 | 3.9    | 3.6       |
| 36                 | 4.0    | 3.7       |
| 37                 | 4.1    | 3.8       |
| 38                 | 4.2    | 3.9       |
| 39                 | 4.3    | 4.0       |
| 40                 | 4.4    | 4.1       |
| 41                 | 4.5    | 4.2       |
| 42                 | 4.6    | 4.3       |
| 43                 | 4.7    | 4.4       |
| 44                 | 4.8    | 4.5       |
| 45                 | 4.9    | 4.6       |
| 46                 | 5.0    | 4.7       |
| 47                 | 5.1    | 4.8       |
| 48                 | 5.2    | 4.9       |
| 49                 | 5.3    | 5.0       |
| 50                 | 5.4    | 5.1       |
| Note: The data is already in the required format for visualization purposes only on the axes labeled 'Income' and 'Seniority'. The values are estimated based on the provided code.
</details>

FIGURE 2.4. A linear model fit by least squares to the Income data from Figure 2.3. The observations are shown in red, and the yellow plane indicates the least squares fit to the data.

2. After a model has been selected, we need a procedure that uses the training data to fit or train the model. In the case of the linear model (2.4), we need to estimate the parameters $\beta_0, \beta_1, \ldots, \beta_p$ . That is, we want to find values of these parameters such that

fit
train

$$
Y \approx \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \dots + \beta_ {p} X _ {p}.
$$

The most common approach to fitting the model $(2.4)$ is referred to as (ordinary) least squares, which we discuss in Chapter 3. However, least squares is one of many possible ways to fit the linear model. In Chapter 6, we discuss other approaches for estimating the parameters in $(2.4)$ .

least squares

The model-based approach just described is referred to as parametric; it reduces the problem of estimating f down to one of estimating a set of parameters. Assuming a parametric form for f simplifies the problem of estimating f because it is generally much easier to estimate a set of parameters, such as $\beta_{0}, \beta_{1}, \ldots, \beta_{p}$ in the linear model (2.4), than it is to fit an entirely arbitrary function f. The potential disadvantage of a parametric approach is that the model we choose will usually not match the true unknown form of f. If the chosen model is too far from the true f, then our estimate will be poor. We can try to address this problem by choosing flexible models that can fit many different possible functional forms for f. But in general, fitting a more flexible model requires estimating a greater number of parameters. These more complex models can lead to a phenomenon known as overfitting the data, which essentially means they follow the errors, or noise, too closely. These issues are discussed throughout this book.

Figure 2.4 shows an example of the parametric approach applied to the Income data from Figure 2.3. We have fit a linear model of the form

flexible

overfitting
noise

$$
\text { income } \approx \beta_ {0} + \beta_ {1} \times \text { education } + \beta_ {2} \times \text { seniority }.
$$

![](images/d447286269e5b94ca75040ca54ea2b7f8534c1c20d885fc25956f125f20b4226.jpg)

<details>
<summary>surface_3d</summary>

| Years of Education | Income | Seniority |
| ------------------ | ------ | --------- |
| 0                  | 0      | 0         |
| 1                  | 1      | 1         |
| 2                  | 2      | 2         |
| 3                  | 3      | 3         |
| 4                  | 4      | 4         |
| 5                  | 5      | 5         |
| 6                  | 6      | 6         |
| 7                  | 7      | 7         |
| 8                  | 8      | 8         |
| 9                  | 9      | 9         |
| 10                 | 10     | 10        |
</details>

FIGURE 2.5. A smooth thin-plate spline fit to the Income data from Figure 2.3 is shown in yellow; the observations are displayed in red. Splines are discussed in Chapter 7.

Since we have assumed a linear relationship between the response and the two predictors, the entire fitting problem reduces to estimating $\beta_{0}$ , $\beta_{1}$ , and $\beta_{2}$ , which we do using least squares linear regression. Comparing Figure 2.3 to Figure 2.4, we can see that the linear fit given in Figure 2.4 is not quite right: the true f has some curvature that is not captured in the linear fit. However, the linear fit still appears to do a reasonable job of capturing the positive relationship between years of education and income, as well as the slightly less positive relationship between seniority and income. It may be that with such a small number of observations, this is the best we can do.

# Non-Parametric Methods

Non-parametric methods do not make explicit assumptions about the functional form of f. Instead they seek an estimate of f that gets as close to the data points as possible without being too rough or wiggly. Such approaches can have a major advantage over parametric approaches: by avoiding the assumption of a particular functional form for f, they have the potential to accurately fit a wider range of possible shapes for f. Any parametric approach brings with it the possibility that the functional form used to estimate f is very different from the true f, in which case the resulting model will not fit the data well. In contrast, non-parametric approaches completely avoid this danger, since essentially no assumption about the form of f is made. But non-parametric approaches do suffer from a major disadvantage: since they do not reduce the problem of estimating f to a small number of parameters, a very large number of observations (far more than is typically needed for a parametric approach) is required in order to obtain an accurate estimate for f.

An example of a non-parametric approach to fitting the Income data is shown in Figure 2.5. A thin-plate spline is used to estimate f. This approach does not impose any pre-specified model on f. It instead attempts

thin-plate spline

![](images/fa881fa5877eb5eb5c4b219e200a08dcaf4e62b91bfce667627326462032dc53.jpg)

<details>
<summary>surface_3d</summary>

| Years of Education | Income | Seniority |
| ------------------ | ------ | --------- |
| 0                  | 0      | 0         |
| 1                  | 1      | 1         |
| 2                  | 2      | 2         |
| 3                  | 3      | 3         |
| 4                  | 4      | 4         |
| 5                  | 5      | 5         |
| 6                  | 6      | 6         |
| 7                  | 7      | 7         |
| 8                  | 8      | 8         |
| 9                  | 9      | 9         |
| 10                 | 10     | 10        |
| 11                 | 11     | 11        |
| 12                 | 12     | 12        |
| 13                 | 13     | 13        |
| 14                 | 14     | 14        |
| 15                 | 15     | 15        |
| 16                 | 16     | 16        |
| 17                 | 17     | 17        |
| 18                 | 18     | 18        |
| 19                 | 19     | 19        |
| 20                 | 20     | 20        |
| 21                 | 21     | 21        |
| 22                 | 22     | 22        |
| 23                 | 23     | 23        |
| 24                 | 24     | 24        |
| 25                 | 25     | 25        |
| 26                 | 26     | 26        |
| 27                 | 27     | 27        |
| 28                 | 28     | 28        |
| 29                 | 29     | 29        |
| 30                 | 30     | 30        |
| 31                 | 31     | 31        |
| 32                 | 32     | 32        |
| 33                 | 33     | 33        |
| 34                 | 34     | 34        |
| 35                 | 35     | 35        |
| 36                 | 36     | 36        |
| 37                 | 37     | 37        |
| 38                 | 38     | 38        |
| 39                 | 39     | 39        |
| 40                 | 40     | 40        |
| 41                 | 41     | 41        |
| 42                 | 42     | 42        |
| 43                 | 43     | 43        |
| 44                 | 44     | 44        |
| 45                 | 45     | 45        |
| 46                 | 46     | 46        |
| 47                 | 47     | 47        |
| 48                 | 48     | 48        |
| 49                 | 49     | 49        |
| 50                 | 50     | 50        |
| Note: The data is not explicitly provided in the code. The 'Income' column is calculated based on the 'Years of Education' column. There is only one data series in this case. The 'Seniority' column is not used in the plot. The values are estimated based on the 'Income' and 'Seniority' columns. There is no additional data series labeled 'Income'.
</details>

FIGURE 2.6. A rough thin-plate spline fit to the Income data from Figure 2.3. This fit makes zero errors on the training data.

to produce an estimate for f that is as close as possible to the observed data, subject to the fit—that is, the yellow surface in Figure 2.5—being smooth. In this case, the non-parametric fit has produced a remarkably accurate estimate of the true f shown in Figure 2.3. In order to fit a thin-plate spline, the data analyst must select a level of smoothness. Figure 2.6 shows the same thin-plate spline fit using a lower level of smoothness, allowing for a rougher fit. The resulting estimate fits the observed data perfectly! However, the spline fit shown in Figure 2.6 is far more variable than the true function f, from Figure 2.3. This is an example of overfitting the data, which we discussed previously. It is an undesirable situation because the fit obtained will not yield accurate estimates of the response on new observations that were not part of the original training data set. We discuss methods for choosing the correct amount of smoothness in Chapter 5. Splines are discussed in Chapter 7.

As we have seen, there are advantages and disadvantages to parametric and non-parametric methods for statistical learning. We explore both types of methods throughout this book.

# 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

Of the many methods that we examine in this book, some are less flexible, or more restrictive, in the sense that they can produce just a relatively small range of shapes to estimate f. For example, linear regression is a relatively inflexible approach, because it can only generate linear functions such as the lines shown in Figure 2.1 or the plane shown in Figure 2.4. Other methods, such as the thin plate splines shown in Figures 2.5 and 2.6, are considerably more flexible because they can generate a much wider range of possible shapes to estimate f.

![](images/d92afcf3f394c278737fa0f0c16cb7b1160ad1d2ef982df20015c5f84b68c816.jpg)

<details>
<summary>scatter</summary>

| Method | Interpretability | Flexibility |
| --- | --- | --- |
| Subset Selection Lasso | High | Low |
| Least Squares | High | Low |
| Generalized Additive Models Trees | High | Low |
| Bagging, Boosting | High | Low |
| Support Vector Machines | High | Low |
| Deep Learning | High | Low |
</details>

FIGURE 2.7. A representation of the tradeoff between flexibility and interpretability, using different statistical learning methods. In general, as the flexibility of a method increases, its interpretability decreases.

One might reasonably ask the following question: why would we ever choose to use a more restrictive method instead of a very flexible approach? There are several reasons that we might prefer a more restrictive model. If we are mainly interested in inference, then restrictive models are much more interpretable. For instance, when inference is the goal, the linear model may be a good choice since it will be quite easy to understand the relationship between Y and $X_{1}, X_{2}, \ldots, X_{p}$ . In contrast, very flexible approaches, such as the splines discussed in Chapter 7 and displayed in Figures 2.5 and 2.6, and the boosting methods discussed in Chapter 8, can lead to such complicated estimates of f that it is difficult to understand how any individual predictor is associated with the response.

Figure 2.7 provides an illustration of the trade-off between flexibility and interpretability for some of the methods that we cover in this book. Least squares linear regression, discussed in Chapter 3, is relatively inflexible but is quite interpretable. The lasso, discussed in Chapter 6, relies upon the linear model (2.4) but uses an alternative fitting procedure for estimating the coefficients $\beta_{0},\beta_{1},\ldots,\beta_{p}$ . The new procedure is more restrictive in estimating the coefficients, and sets a number of them to exactly zero. Hence in this sense the lasso is a less flexible approach than linear regression. It is also more interpretable than linear regression, because in the final model the response variable will only be related to a small subset of the predictors—namely, those with nonzero coefficient estimates. Generalized additive models (GAMs), discussed in Chapter 7, instead extend the linear model (2.4) to allow for certain non-linear relationships. Consequently, GAMs are more flexible than linear regression. They are also somewhat less interpretable than linear regression, because the relationship between each predictor and the response is now modeled using a curve. Finally, fully non-linear methods such as bagging, boosting, support vector machines with non-linear kernels, and neural networks (deep learning), discussed in Chapters 8, 9, and 10, are highly flexible approaches that are harder to interpret.

We have established that when inference is the goal, there are clear advantages to using simple and relatively inflexible statistical learning methods. In some settings, however, we are only interested in prediction, and the interpretability of the predictive model is simply not of interest. For instance, if we seek to develop an algorithm to predict the price of a stock, our sole requirement for the algorithm is that it predict accurately—interpretability is not a concern. In this setting, we might expect that it will be best to use the most flexible model available. Surprisingly, this is not always the case! We will often obtain more accurate predictions using a less flexible method. This phenomenon, which may seem counterintuitive at first glance, has to do with the potential for overfitting in highly flexible methods. We saw an example of overfitting in Figure 2.6. We will discuss this very important concept further in Section 2.2 and throughout this book.

# 2.1.4 Supervised Versus Unsupervised Learning

Most statistical learning problems fall into one of two categories: supervised or unsupervised. The examples that we have discussed so far in this chapter all fall into the supervised learning domain. For each observation of the predictor measurement(s) $x_{i}, i = 1, \ldots, n$ there is an associated response measurement $y_{i}$ . We wish to fit a model that relates the response to the predictors, with the aim of accurately predicting the response for future observations (prediction) or better understanding the relationship between the response and the predictors (inference). Many classical statistical learning methods such as linear regression and logistic regression (Chapter 4), as well as more modern approaches such as GAM, boosting, and support vector machines, operate in the supervised learning domain. The vast majority of this book is devoted to this setting.

By contrast, unsupervised learning describes the somewhat more challenging situation in which for every observation $i = 1, \ldots, n$ , we observe a vector of measurements $x_{i}$ but no associated response $y_{i}$ . It is not possible to fit a linear regression model, since there is no response variable to predict. In this setting, we are in some sense working blind; the situation is referred to as unsupervised because we lack a response variable that can supervise our analysis. What sort of statistical analysis is possible? We can seek to understand the relationships between the variables or between the observations. One statistical learning tool that we may use in this setting is cluster analysis, or clustering. The goal of cluster analysis is to ascertain, on the basis of $x_{1}, \ldots, x_{n}$ , whether the observations fall into relatively distinct groups. For example, in a market segmentation study we might observe multiple characteristics (variables) for potential customers, such as zip code, family income, and shopping habits. We might believe that the customers fall into different groups, such as big spenders versus low spenders. If the information about each customer's spending patterns were available, then a supervised analysis would be possible. However, this information is not available—that is, we do not know whether each potential customer is a big spender or not. In this setting, we can try to cluster the customers on the basis of the variables measured, in order to identify distinct groups of potential customers. Identifying such groups can be of interest because it might be that the groups differ with respect to some property of interest, such as spending habits.

![](images/59f06dd8a6d6afc4929eed476ca7163bffc5d53b321184ec6eac41e772c452f1.jpg)

![](images/3f4dc01723f82738b5188f3357df8f28f07927ebb6e83920d9e934a64ba0d621.jpg)

<details>
<summary>scatter</summary>

| X1 | X2 | Group |
|----|----|-------|
| 0  | 6  | A     |
| 1  | 5  | B     |
| 2  | 4  | C     |
| 3  | 3  | D     |
| 4  | 2  | E     |
| 5  | 1  | F     |
| 6  | 0  | G     |
</details>

FIGURE 2.8. A clustering data set involving three groups. Each group is shown using a different colored symbol. Left: The three groups are well-separated. In this setting, a clustering approach should successfully identify the three groups. Right: There is some overlap among the groups. Now the clustering task is more challenging.

Figure 2.8 provides a simple illustration of the clustering problem. We have plotted 150 observations with measurements on two variables, $X_{1}$ and $X_{2}$ . Each observation corresponds to one of three distinct groups. For illustrative purposes, we have plotted the members of each group using different colors and symbols. However, in practice the group memberships are unknown, and the goal is to determine the group to which each observation belongs. In the left-hand panel of Figure 2.8, this is a relatively easy task because the groups are well-separated. By contrast, the right-hand panel illustrates a more challenging setting in which there is some overlap between the groups. A clustering method could not be expected to assign all of the overlapping points to their correct group (blue, green, or orange).

In the examples shown in Figure 2.8, there are only two variables, and so one can simply visually inspect the scatterplots of the observations in order to identify clusters. However, in practice, we often encounter data sets that contain many more than two variables. In this case, we cannot easily plot the observations. For instance, if there are p variables in our data set, then $p(p - 1)/2$ distinct scatterplots can be made, and visual inspection is simply not a viable way to identify clusters. For this reason, automated clustering methods are important. We discuss clustering and other unsupervised learning approaches in Chapter 12.

Many problems fall naturally into the supervised or unsupervised learning paradigms. However, sometimes the question of whether an analysis should be considered supervised or unsupervised is less clear-cut. For instance, suppose that we have a set of n observations. For m of the observations, where m < n, we have both predictor measurements and a response measurement. For the remaining n - m observations, we have predictor measurements but no response measurement. Such a scenario can arise if the predictors can be measured relatively cheaply but the corresponding responses are much more expensive to collect. We refer to this setting as a semi-supervised learning problem. In this setting, we wish to use a statistical learning method that can incorporate the m observations for which response measurements are available as well as the n - m observations for which they are not. Although this is an interesting topic, it is beyond the scope of this book.

semi-
supervised
learning

# 2.1.5 Regression Versus Classification Problems

Variables can be characterized as either quantitative or qualitative (also known as categorical). Quantitative variables take on numerical values. Examples include a person's age, height, or income, the value of a house, and the price of a stock. In contrast, qualitative variables take on values in one of K different classes, or categories. Examples of qualitative variables include a person's marital status (married or not), the brand of product purchased (brand A, B, or C), whether a person defaults on a debt (yes or no), or a cancer diagnosis (Acute Myelogenous Leukemia, Acute Lymphoblastic Leukemia, or No Leukemia). We tend to refer to problems with a quantitative response as regression problems, while those involving a qualitative response are often referred to as classification problems. However, the distinction is not always that crisp. Least squares linear regression (Chapter 3) is used with a quantitative response, whereas logistic regression (Chapter 4) is typically used with a qualitative (two-class, or binary) response. Thus, despite its name, logistic regression is a classification method. But since it estimates class probabilities, it can be thought of as a regression method as well. Some statistical methods, such as K-nearest neighbors (Chapters 2 and 4) and boosting (Chapter 8), can be used in the case of either quantitative or qualitative responses.

We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative. However, whether the predictors are qualitative or quantitative is generally considered less important. Most of the statistical learning methods discussed in this book can be applied regardless of the predictor variable type, provided that any qualitative predictors are properly coded before the analysis is performed. This is discussed in Chapter 3.

quantitative
qualitative
categorical
class

regression
classification

binary

# 2.2 Assessing Model Accuracy

One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach. Why is it necessary to introduce so many different statistical learning approaches, rather than just a single best method? There is no free lunch in statistics: no one method dominates all others over all possible data sets. On a particular data set, one specific method may work best, but some other method may work better on a similar but different data set. Hence it is an important task to decide for any given set of data which method produces the best results. Selecting the best approach can be one of the most challenging parts of performing statistical learning in practice.

In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set. As the book progresses, we will explain how the concepts presented here can be applied in practice.

# 2.2.1 Measuring the Quality of Fit

In order to evaluate the performance of a statistical learning method on a given data set, we need some way to measure how well its predictions actually match the observed data. That is, we need to quantify the extent to which the predicted response value for a given observation is close to the true response value for that observation. In the regression setting, the most commonly-used measure is the mean squared error (MSE), given by

$$
\mathrm{MSE} = \frac {1}{n} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {f} (x _ {i})) ^ {2}, \tag {2.5}
$$

where $\hat{f}(x_{i})$ is the prediction that $\hat{f}$ gives for the ith observation. The MSE will be small if the predicted responses are very close to the true responses, and will be large if for some of the observations, the predicted and true responses differ substantially.

The MSE in $(2.5)$ is computed using the training data that was used to fit the model, and so should more accurately be referred to as the training MSE. But in general, we do not really care how well the method works on the training data. Rather, we are interested in the accuracy of the predictions that we obtain when we apply our method to previously unseen test data. Why is this what we care about? Suppose that we are interested in developing an algorithm to predict a stock's price based on previous stock returns. We can train the method using stock returns from the past 6 months. But we don't really care how well our method predicts last week's stock price. We instead care about how well it will predict tomorrow's price or next month's price. On a similar note, suppose that we have clinical measurements (e.g. weight, blood pressure, height, age, family history of disease) for a number of patients, as well as information about whether each patient has diabetes. We can use these patients to train a statistical learning method to predict risk of diabetes based on clinical measurements. In practice, we want this method to accurately predict diabetes risk for future patients based on their clinical measurements. We are not very interested in whether or not the method accurately predicts diabetes risk for patients used to train the model, since we already know which of those patients have diabetes.

To state it more mathematically, suppose that we fit our statistical learning method on our training observations $\{(x_{1},y_{1}),(x_{2},y_{2}),\ldots,(x_{n},y_{n})\}$ , and we obtain the estimate $\hat{f}$ . We can then compute $\hat{f}(x_{1}),\hat{f}(x_{2}),\ldots,\hat{f}(x_{n})$ .

![](images/bc64534220213c5e34d2935c8277b9c7b1a9a1eafca1a15249192fd2cd133f7d.jpg)

<details>
<summary>line</summary>

| X  | Y (Black Line) | Y (Orange Line) | Y (Teal Line) |
|----|----------------|-----------------|---------------|
| 0  | 4.0            | 4.5             | 3.5           |
| 20 | 5.5            | 5.0             | 4.5           |
| 40 | 7.0            | 6.5             | 6.0           |
| 60 | 9.0            | 8.0             | 10.5          |
| 80 | 8.5            | 9.0             | 9.0           |
| 100| 6.0            | 10.0            | 5.0           |
</details>

![](images/2eb306495c7863e972775143153271d2e793d37f625aa22b7484719629a92075.jpg)

<details>
<summary>line</summary>

| Flexibility | Mean Squared Error |
| ----------- | ------------------ |
| 2           | 2.1                |
| 5           | 1.1                |
| 22          | 1.5                |
</details>

FIGURE 2.9. Left: Data simulated from f, shown in black. Three estimates of f are shown: the linear regression line (orange curve), and two smoothing spline fits (blue and green curves). Right: Training MSE (grey curve), test MSE (red curve), and minimum possible test MSE over all methods (dashed line). Squares represent the training and test MSEs for the three fits shown in the left-hand panel.

If these are approximately equal to $y_{1}, y_{2}, \ldots, y_{n}$ , then the training MSE given by (2.5) is small. However, we are really not interested in whether $\hat{f}(x_{i}) \approx y_{i}$ ; instead, we want to know whether $\hat{f}(x_{0})$ is approximately equal to $y_{0}$ , where $(x_{0}, y_{0})$ is a previously unseen test observation not used to train the statistical learning method. We want to choose the method that gives the lowest test MSE, as opposed to the lowest training MSE. In other words, if we had a large number of test observations, we could compute

$$
\operatorname{Ave} (y _ {0} - \hat {f} (x _ {0})) ^ {2}, \tag {2.6}
$$

test MSE

the average squared prediction error for these test observations $(x_0, y_0)$ . We'd like to select the model for which this quantity is as small as possible.

How can we go about trying to select a method that minimizes the test MSE? In some settings, we may have a test data set available—that is, we may have access to a set of observations that were not used to train the statistical learning method. We can then simply evaluate $(2.6)$ on the test observations, and select the learning method for which the test MSE is smallest. But what if no test observations are available? In that case, one might imagine simply selecting a statistical learning method that minimizes the training MSE $(2.5)$ . This seems like it might be a sensible approach, since the training MSE and the test MSE appear to be closely related. Unfortunately, there is a fundamental problem with this strategy: there is no guarantee that the method with the lowest training MSE will also have the lowest test MSE. Roughly speaking, the problem is that many statistical methods specifically estimate coefficients so as to minimize the training set MSE. For these methods, the training set MSE can be quite small, but the test MSE is often much larger.

Figure 2.9 illustrates this phenomenon on a simple example. In the left-hand panel of Figure 2.9, we have generated observations from (2.1) with the true f given by the black curve. The orange, blue and green curves illustrate three possible estimates for f obtained using methods with increasing levels of flexibility. The orange line is the linear regression fit, which is relatively inflexible. The blue and green curves were produced using smoothing splines, discussed in Chapter 7, with different levels of smoothness. It is clear that as the level of flexibility increases, the curves fit the observed data more closely. The green curve is the most flexible and matches the data very well; however, we observe that it fits the true f (shown in black) poorly because it is too wiggly. By adjusting the level of flexibility of the smoothing spline fit, we can produce many different fits to this data.

We now move on to the right-hand panel of Figure 2.9. The grey curve displays the average training MSE as a function of flexibility, or more formally the degrees of freedom, for a number of smoothing splines. The degrees of freedom is a quantity that summarizes the flexibility of a curve; it is discussed more fully in Chapter 7. The orange, blue and green squares indicate the MSEs associated with the corresponding curves in the left-hand panel. A more restricted and hence smoother curve has fewer degrees of freedom than a wiggly curve—note that in Figure 2.9, linear regression is at the most restrictive end, with two degrees of freedom. The training MSE declines monotonically as flexibility increases. In this example the true f is non-linear, and so the orange linear fit is not flexible enough to estimate f well. The green curve has the lowest training MSE of all three methods, since it corresponds to the most flexible of the three curves fit in the left-hand panel.

In this example, we know the true function f, and so we can also compute the test MSE over a very large test set, as a function of flexibility. (Of course, in general f is unknown, so this will not be possible.) The test MSE is displayed using the red curve in the right-hand panel of Figure 2.9. As with the training MSE, the test MSE initially declines as the level of flexibility increases. However, at some point the test MSE levels off and then starts to increase again. Consequently, the orange and green curves both have high test MSE. The blue curve minimizes the test MSE, which should not be surprising given that visually it appears to estimate f the best in the left-hand panel of Figure 2.9. The horizontal dashed line indicates $\operatorname{Var}(\epsilon)$ , the irreducible error in (2.3), which corresponds to the lowest achievable test MSE among all possible methods. Hence, the smoothing spline represented by the blue curve is close to optimal.

In the right-hand panel of Figure 2.9, as the flexibility of the statistical learning method increases, we observe a monotone decrease in the training MSE and a U-shape in the test MSE. This is a fundamental property of statistical learning that holds regardless of the particular data set at hand and regardless of the statistical method being used. As model flexibility increases, the training MSE will decrease, but the test MSE may not. When a given method yields a small training MSE but a large test MSE, we are said to be overfitting the data. This happens because our statistical learning procedure is working too hard to find patterns in the training data, and may be picking up some patterns that are just caused by random chance rather than by true properties of the unknown function f. When we overfit the training data, the test MSE will be very large because the supposed patterns that the method found in the training data simply don't exist in the test data. Note that regardless of whether or not overfitting has occurred, we almost always expect the training MSE to be smaller than the test MSE because most statistical learning methods either directly or indirectly seek to minimize the training MSE. Overfitting refers specifically to the case in which a less flexible model would have yielded a smaller test MSE.

![](images/637bf1d5969b083aec5f30ddada4b1c6764c47b89b27a3f5141ae1d184da9439.jpg)

<details>
<summary>scatter</summary>

| X  | Y  |
|----|----|
| 0  | 2  |
| 10 | 3  |
| 20 | 4  |
| 30 | 5  |
| 40 | 6  |
| 50 | 7  |
| 60 | 8  |
| 70 | 9  |
| 80 | 10 |
| 90 | 11 |
| 100| 12 |
</details>

![](images/1c232e61745262e93e84d786750f07d78e28acdbcc9b60182c14c019740b0115.jpg)

<details>
<summary>line</summary>

| Flexibility | Mean Squared Error |
| ----------- | ------------------ |
| 2           | 1.0                |
| 3           | 1.0                |
| 22          | 1.5                |
| 23          | 0.4                |
</details>

FIGURE 2.10. Details are as in Figure 2.9, using a different true f that is much closer to linear. In this setting, linear regression provides a very good fit to the data.

Figure 2.10 provides another example in which the true f is approximately linear. Again we observe that the training MSE decreases monotonically as the model flexibility increases, and that there is a U-shape in the test MSE. However, because the truth is close to linear, the test MSE only decreases slightly before increasing again, so that the orange least squares fit is substantially better than the highly flexible green curve. Finally, Figure 2.11 displays an example in which f is highly non-linear. The training and test MSE curves still exhibit the same general patterns, but now there is a rapid decrease in both curves before the test MSE starts to increase slowly.

In practice, one can usually compute the training MSE with relative ease, but estimating the test MSE is considerably more difficult because usually no test data are available. As the previous three examples illustrate, the flexibility level corresponding to the model with the minimal test MSE can vary considerably among data sets. Throughout this book, we discuss a variety of approaches that can be used in practice to estimate this minimum point. One important method is cross-validation (Chapter 5), which is a method for estimating the test MSE using the training data.

cross-
validation

# 2.2.2 The Bias-Variance Trade-Off

The U-shape observed in the test MSE curves (Figures 2.9-2.11) turns out to be the result of two competing properties of statistical learning methods.

![](images/280a9c7250ca8995fdbb29f6a5607f8a5e4d775ae81393aeceae246f5b791bdb.jpg)

<details>
<summary>line</summary>

| X   | Y (Line 1) | Y (Line 2) |
| --- | ---------- | ---------- |
| 0   | 25.0       | 20.0       |
| 10  | 20.0       | 18.0       |
| 20  | 15.0       | 16.0       |
| 30  | 12.0       | 14.0       |
| 40  | 10.0       | 12.0       |
| 50  | 12.0       | 10.0       |
| 60  | 14.0       | 8.0        |
| 70  | 16.0       | 6.0        |
| 80  | 18.0       | 4.0        |
| 90  | 20.0       | 2.0        |
| 100 | -15.0      | -5.0       |
</details>

![](images/355605b5c2049c224e3a837bd2c043a0d718f563685a3df0149d7d87e50f0e8f.jpg)

<details>
<summary>line</summary>

| Flexibility | Mean Squared Error |
| ----------- | ------------------ |
| 2           | 19.0               |
| 2           | 15.0               |
| 10          | 1.0                |
| 20          | 1.5                |
</details>

FIGURE 2.11. Details are as in Figure 2.9, using a different f that is far from linear. In this setting, linear regression provides a very poor fit to the data.

Though the mathematical proof is beyond the scope of this book, it is possible to show that the expected test MSE, for a given value $x_{0}$ , can always be decomposed into the sum of three fundamental quantities: the variance of $\hat{f}(x_{0})$ , the squared bias of $\hat{f}(x_{0})$ and the variance of the error terms $\epsilon$ . That is,

$$
E \left(y _ {0} - \hat {f} (x _ {0})\right) ^ {2} = \operatorname{Var} (\hat {f} (x _ {0})) + [ \operatorname{Bias} (\hat {f} (x _ {0})) ] ^ {2} + \operatorname{Var} (\epsilon). \tag {2.7}
$$

Here the notation $E\left(y_{0}-\hat{f}(x_{0})\right)^{2}$ defines the expected test MSE at $x_{0}$ , and refers to the average test MSE that we would obtain if we repeatedly estimated f using a large number of training sets, and tested each at $x_{0}$ . The overall expected test MSE can be computed by averaging $E\left(y_{0}-\hat{f}(x_{0})\right)^{2}$ over all possible values of $x_{0}$ in the test set.

Equation 2.7 tells us that in order to minimize the expected test error, we need to select a statistical learning method that simultaneously achieves low variance and low bias. Note that variance is inherently a nonnegative quantity, and squared bias is also nonnegative. Hence, we see that the expected test MSE can never lie below $\mathrm{Var}(\epsilon)$ , the irreducible error from (2.3).

What do we mean by the variance and bias of a statistical learning method? Variance refers to the amount by which $\hat{f}$ would change if we estimated it using a different training data set. Since the training data are used to fit the statistical learning method, different training data sets will result in a different $\hat{f}$ . But ideally the estimate for f should not vary too much between training sets. However, if a method has high variance then small changes in the training data can result in large changes in $\hat{f}$ . In general, more flexible statistical methods have higher variance. Consider the green and orange curves in Figure 2.9. The flexible green curve is following the observations very closely. It has high variance because changing any one of these data points may cause the estimate $\hat{f}$ to change considerably.

variance
bias

expected
test MSE

![](images/8999c3474b1046ba8e33fc2c8042da0905fb5002b7d57088f0bb05fbb4c8e612.jpg)

<details>
<summary>line</summary>

| Flexibility | Red Line | Cyan Line | Orange Line | Dark Red Line |
|-------------|----------|-----------|-------------|---------------|
| 2           | 2.1      | 1.1       | 0.0         | 0.0           |
| 5           | 1.1      | 0.0       | 0.1         | 0.0           |
| 10          | 1.2      | 0.0       | 0.3         | 0.0           |
| 20          | 1.5      | 0.0       | 0.8         | 0.0           |
| 25          | 2.4      | 0.0       | 1.4         | 0.0           |
</details>

![](images/e749e122f796f181036b2a5248fadc1b88ab4668dad565d0a6102dbda2750d9b.jpg)

<details>
<summary>line</summary>

| Flexibility | Red Line | Orange Line | Cyan Line |
| ----------- | -------- | ----------- | --------- |
| 2           | 1.0      | 0.0         | 0.0       |
| 5           | 1.0      | 0.1         | 0.0       |
| 10          | 1.1      | 0.3         | 0.0       |
| 20          | 1.5      | 0.8         | 0.0       |
| 25          | 2.3      | 1.3         | 0.0       |
</details>

![](images/71d8b93d67057b16cb502be2b51a240bf29e99073d2709158b626b2e780bdea9.jpg)

<details>
<summary>line</summary>

| Flexibility | MSE  | Bias | Var  |
| ----------- | ---- | ---- | ---- |
| 2           | 19.0 | 18.0 | 0.5  |
| 5           | 3.0  | 2.0  | 0.5  |
| 10          | 1.5  | 1.0  | 0.5  |
| 20          | 2.0  | 1.5  | 1.0  |
</details>

FIGURE 2.12. Squared bias (blue curve), variance (orange curve), Var( $\epsilon$ ) (dashed line), and test MSE (red curve) for the three data sets in Figures 2.9–2.11. The vertical dotted line indicates the flexibility level corresponding to the smallest test MSE.

In contrast, the orange least squares line is relatively inflexible and has low variance, because moving any single observation will likely cause only a small shift in the position of the line.

On the other hand, bias refers to the error that is introduced by approximating a real-life problem, which may be extremely complicated, by a much simpler model. For example, linear regression assumes that there is a linear relationship between Y and $X_{1}, X_{2}, \ldots, X_{p}$ . It is unlikely that any real-life problem truly has such a simple linear relationship, and so performing linear regression will undoubtedly result in some bias in the estimate of f. In Figure 2.11, the true f is substantially non-linear, so no matter how many training observations we are given, it will not be possible to produce an accurate estimate using linear regression. In other words, linear regression results in high bias in this example. However, in Figure 2.10 the true f is very close to linear, and so given enough data, it should be possible for linear regression to produce an accurate estimate. Generally, more flexible methods result in less bias.

As a general rule, as we use more flexible methods, the variance will increase and the bias will decrease. The relative rate of change of these two quantities determines whether the test MSE increases or decreases. As we increase the flexibility of a class of methods, the bias tends to initially decrease faster than the variance increases. Consequently, the expected test MSE declines. However, at some point increasing flexibility has little impact on the bias but starts to significantly increase the variance. When this happens the test MSE increases. Note that we observed this pattern of decreasing test MSE followed by increasing test MSE in the right-hand panels of Figures 2.9–2.11.

The three plots in Figure 2.12 illustrate Equation 2.7 for the examples in Figures 2.9–2.11. In each case the blue solid curve represents the squared bias, for different levels of flexibility, while the orange curve corresponds to the variance. The horizontal dashed line represents $\operatorname{Var}(\epsilon)$ , the irreducible error. Finally, the red curve, corresponding to the test set MSE, is the sum of these three quantities. In all three cases, the variance increases and the bias decreases as the method's flexibility increases. However, the flexibility level corresponding to the optimal test MSE differs considerably among the three data sets, because the squared bias and variance change at different rates in each of the data sets. In the left-hand panel of Figure 2.12, the bias initially decreases rapidly, resulting in an initial sharp decrease in the expected test MSE. On the other hand, in the center panel of Figure 2.12 the true $f$ is close to linear, so there is only a small decrease in bias as flexibility increases, and the test MSE only declines slightly before increasing rapidly as the variance increases. Finally, in the right-hand panel of Figure 2.12, as flexibility increases, there is a dramatic decline in bias because the true $f$ is very non-linear. There is also very little increase in variance as flexibility increases. Consequently, the test MSE declines substantially before experiencing a small increase as model flexibility increases.

The relationship between bias, variance, and test set MSE given in Equation 2.7 and displayed in Figure 2.12 is referred to as the bias-variance trade-off. Good test set performance of a statistical learning method requires low variance as well as low squared bias. This is referred to as a trade-off because it is easy to obtain a method with extremely low bias but high variance (for instance, by drawing a curve that passes through every single training observation) or a method with very low variance but high bias (by fitting a horizontal line to the data). The challenge lies in finding a method for which both the variance and the squared bias are low. This trade-off is one of the most important recurring themes in this book.

In a real-life situation in which f is unobserved, it is generally not possible to explicitly compute the test MSE, bias, or variance for a statistical learning method. Nevertheless, one should always keep the bias-variance trade-off in mind. In this book we explore methods that are extremely flexible and hence can essentially eliminate bias. However, this does not guarantee that they will outperform a much simpler method such as linear regression. To take an extreme example, suppose that the true f is linear. In this situation linear regression will have no bias, making it very hard for a more flexible method to compete. In contrast, if the true f is highly non-linear and we have an ample number of training observations, then we may do better using a highly flexible approach, as in Figure 2.11. In Chapter 5 we discuss cross-validation, which is a way to estimate the test MSE using the training data.

# 2.2.3 The Classification Setting

Thus far, our discussion of model accuracy has been focused on the regression setting. But many of the concepts that we have encountered, such as the bias-variance trade-off, transfer over to the classification setting with only some modifications due to the fact that $y_{i}$ is no longer quantitative. Suppose that we seek to estimate f on the basis of training observations $\{(x_{1},y_{1}),\ldots,(x_{n},y_{n})\}$ , where now $y_{1},\ldots,y_{n}$ are qualitative. The most common approach for quantifying the accuracy of our estimate $\hat{f}$ is the training error rate, the proportion of mistakes that are made if we apply our estimate $\hat{f}$ to the training observations:

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} I (y _ {i} \neq \hat {y} _ {i}). \tag {2.8}
$$

Here $\hat{y}_{i}$ is the predicted class label for the ith observation using $\hat{f}$ . And $I(y_{i} \neq \hat{y}_{i})$ is an indicator variable that equals 1 if $y_{i} \neq \hat{y}_{i}$ and zero if $y_{i} = \hat{y}_{i}$ . If $I(y_{i} \neq \hat{y}_{i}) = 0$ then the ith observation was classified correctly by our classification method; otherwise it was misclassified. Hence Equation 2.8 computes the fraction of incorrect classifications.

Equation 2.8 is referred to as the training error rate because it is computed based on the data that was used to train our classifier. As in the regression setting, we are most interested in the error rates that result from applying our classifier to test observations that were not used in training. The test error rate associated with a set of test observations of the form $(x_{0}, y_{0})$ is given by

$$
\operatorname{Ave} \left(I (y _ {0} \neq \hat {y} _ {0})\right), \tag {2.9}
$$

where $\hat{y}_{0}$ is the predicted class label that results from applying the classifier to the test observation with predictor $x_{0}$ . A good classifier is one for which the test error (2.9) is smallest.

# The Bayes Classifier

It is possible to show (though the proof is outside of the scope of this book) that the test error rate given in $(2.9)$ is minimized, on average, by a very simple classifier that assigns each observation to the most likely class, given its predictor values. In other words, we should simply assign a test observation with predictor vector $x_{0}$ to the class j for which

$$
\operatorname * {P r} (Y = j | X = x _ {0}) \tag {2.10}
$$

is largest. Note that $(2.10)$ is a conditional probability: it is the probability that Y = j, given the observed predictor vector $x_{0}$ . This very simple classifier is called the Bayes classifier. In a two-class problem where there are only two possible response values, say class 1 or class 2, the Bayes classifier corresponds to predicting class one if $\Pr(Y = 1|X = x_{0}) > 0.5$ , and class two otherwise.

Figure 2.13 provides an example using a simulated data set in a two-dimensional space consisting of predictors $X_{1}$ and $X_{2}$ . The orange and blue circles correspond to training observations that belong to two different classes. For each value of $X_{1}$ and $X_{2}$ , there is a different probability of the response being orange or blue. Since this is simulated data, we know how the data were generated and we can calculate the conditional probabilities for each value of $X_{1}$ and $X_{2}$ . The orange shaded region reflects the set of points for which $\Pr(Y = \text{orange}|X)$ is greater than 50%, while the blue shaded region indicates the set of points for which the probability is below 50%. The purple dashed line represents the points where the probability is exactly 50%. This is called the Bayes decision boundary. The Bayes classifier's prediction is determined by the Bayes decision boundary; an observation that falls on the orange side of the boundary will be assigned

indicator variable

training error

test error

conditional probability
Bayes classifier

Bayes
decision
boundary

![](images/f046615e3d4bdd2e65bdedf89857bd22416568bb6d076d5059a921e0accc3534.jpg)

<details>
<summary>scatter</summary>

| X1 | X2 | Group |
|----|----|-------|
| (various) | (various) | Blue Circle |
| (various) | (various) | Orange Circle |
| (various) | (various) | Purple Dashed Line |
| (various) | (various) | Blue Circle |
| (various) | (various) | Orange Circle |
| (various) | (various) | Purple Dashed Line |
</details>

FIGURE 2.13. A simulated data set consisting of 100 observations in each of two groups, indicated in blue and in orange. The purple dashed line represents the Bayes decision boundary. The orange background grid indicates the region in which a test observation will be assigned to the orange class, and the blue background grid indicates the region in which a test observation will be assigned to the blue class.

to the orange class, and similarly an observation on the blue side of the boundary will be assigned to the blue class.

The Bayes classifier produces the lowest possible test error rate, called the Bayes error rate. Since the Bayes classifier will always choose the class for which (2.10) is largest, the error rate will be $1 - \max_{j} \Pr(Y = j | X = x_0)$ at $X = x_0$ . In general, the overall Bayes error rate is given by

$$
1 - E \left(\max _ {j} \operatorname * {P r} (Y = j | X)\right), \tag {2.11}
$$

Bayes error rate

where the expectation averages the probability over all possible values of X. For our simulated data, the Bayes error rate is 0.133. It is greater than zero, because the classes overlap in the true population, which implies that $\max_{j}\Pr(Y=j|X=x_{0})<1$ for some values of $x_{0}$ . The Bayes error rate is analogous to the irreducible error, discussed earlier.

# K-Nearest Neighbors

In theory we would always like to predict qualitative responses using the Bayes classifier. But for real data, we do not know the conditional distribution of Y given X, and so computing the Bayes classifier is impossible. Therefore, the Bayes classifier serves as an unattainable gold standard against which to compare other methods. Many approaches attempt to estimate the conditional distribution of Y given X, and then classify a given observation to the class with highest estimated probability. One such method is the K-nearest neighbors (KNN) classifier. Given a positive integer K and a test observation $x_{0}$ , the KNN classifier first identifies the K points in the training data that are closest to $x_{0}$ , represented by $N_{0}$ . It then estimates the conditional probability for class j as the fraction of points in $N_{0}$ whose response values equal j:

$$
\operatorname * {P r} (Y = j | X = x _ {0}) = \frac {1}{K} \sum_ {i \in \mathcal {N} _ {0}} I (y _ {i} = j). \tag {2.12}
$$

Finally, KNN classifies the test observation $x_0$ to the class with the largest probability from (2.12).

Figure 2.14 provides an illustrative example of the KNN approach. In the left-hand panel, we have plotted a small training data set consisting of six blue and six orange observations. Our goal is to make a prediction for the point labeled by the black cross. Suppose that we choose K = 3. Then KNN will first identify the three observations that are closest to the cross. This neighborhood is shown as a circle. It consists of two blue points and one orange point, resulting in estimated probabilities of 2/3 for the blue class and 1/3 for the orange class. Hence KNN will predict that the black cross belongs to the blue class. In the right-hand panel of Figure 2.14 we have applied the KNN approach with K = 3 at all of the possible values for $X_{1}$ and $X_{2}$ , and have drawn in the corresponding KNN decision boundary.

Despite the fact that it is a very simple approach, KNN can often produce classifiers that are surprisingly close to the optimal Bayes classifier. Figure 2.15 displays the KNN decision boundary, using K = 10, when applied to the larger simulated data set from Figure 2.13. Notice that even though the true distribution is not known by the KNN classifier, the KNN decision boundary is very close to that of the Bayes classifier. The test error rate using KNN is 0.1363, which is close to the Bayes error rate of 0.1304.

The choice of $K$ has a drastic effect on the KNN classifier obtained. Figure 2.16 displays two KNN fits to the simulated data from Figure 2.13, using $K = 1$ and $K = 100$ . When $K = 1$ , the decision boundary is overly flexible and finds patterns in the data that don't correspond to the Bayes decision boundary. This corresponds to a classifier that has low bias but very high variance. As $K$ grows, the method becomes less flexible and produces a decision boundary that is close to linear. This corresponds to a low-variance but high-bias classifier. On this simulated data set, neither $K = 1$ nor $K = 100$ give good predictions: they have test error rates of 0.1695 and 0.1925, respectively.

Just as in the regression setting, there is not a strong relationship between the training error rate and the test error rate. With K = 1, the KNN training error rate is 0, but the test error rate may be quite high. In general, as we use more flexible classification methods, the training error rate will decline but the test error rate may not. In Figure 2.17, we have plotted the KNN test and training errors as a function of 1/K. As 1/K increases, the method becomes more flexible. As in the regression setting, the training error rate consistently declines as the flexibility increases. However, the test error exhibits a characteristic U-shape, declining at first (with a minimum at approximately K = 10) before increasing again when the method becomes excessively flexible and overfits.

![](images/d01d163f96b922fd5edb7e9edfd7b6737a539665ead9f2addd36365fd748a30b.jpg)

<details>
<summary>text_image</summary>

Diagram showing a green circle with an 'x' at center surrounded by scattered blue and orange circles, likely representing a mathematical or physical concept.
</details>

![](images/3856490aa7471191e59ec429740731bc8ae54df94b0decc789c772a1b852add0.jpg)

<details>
<summary>text_image</summary>

Diagram with colored dots and labeled points, showing a path through a region with blue and orange markers.
</details>

FIGURE 2.14. The KNN approach, using K = 3, is illustrated in a simple situation with six blue observations and six orange observations. Left: a test observation at which a predicted class label is desired is shown as a black cross. The three closest points to the test observation are identified, and it is predicted that the test observation belongs to the most commonly-occurring class, in this case blue. Right: The KNN decision boundary for this example is shown in black. The blue grid indicates the region in which a test observation will be assigned to the blue class, and the orange grid indicates the region in which it will be assigned to the orange class.

KNN: K=10   
![](images/a7bb8f9d7fb421f207a651b0e85591cf3cf5c9d76a753dd1db8bcfbd6b622f9b.jpg)

<details>
<summary>scatter</summary>

| X2 | Y |
|----|----|
| (Data not extractable as discrete values; visual scatter points) | (Data not extractable as discrete values; visual scatter points) |
</details>

$X_{1}$   
FIGURE 2.15. The black curve indicates the KNN decision boundary on the data from Figure 2.13, using K = 10. The Bayes decision boundary is shown as a purple dashed line. The KNN and Bayes decision boundaries are very similar.

In both the regression and classification settings, choosing the correct level of flexibility is critical to the success of any statistical learning method. The bias-variance tradeoff, and the resulting U-shape in the test error, can make this a difficult task. In Chapter 5, we return to this topic and discuss various methods for estimating test error rates and thereby choosing the optimal level of flexibility for a given statistical learning method.

![](images/c22760b87d9aada4836908526677cb23eb47b88fe7f7f1295206c401797fc2e0.jpg)

FIGURE 2.16. A comparison of the KNN decision boundaries (solid black curves) obtained using K = 1 and K = 100 on the data from Figure 2.13. With K = 1, the decision boundary is overly flexible, while with K = 100 it is not sufficiently flexible. The Bayes decision boundary is shown as a purple dashed line.   
![](images/67379ebee45cedc34be634cb4a37eb6240ccec1993318edfaedc6a55832648cb.jpg)

<details>
<summary>line</summary>

| 1/K    | Training Errors | Test Errors |
| ------ | --------------- | ----------- |
| 0.01   | 0.185           | 0.192       |
| 0.02   | 0.145           | 0.175       |
| 0.03   | 0.135           | 0.160       |
| 0.04   | 0.140           | 0.155       |
| 0.05   | 0.125           | 0.145       |
| 0.06   | 0.115           | 0.135       |
| 0.07   | 0.105           | 0.130       |
| 0.08   | 0.100           | 0.135       |
| 0.09   | 0.095           | 0.135       |
| 0.10   | 0.090           | 0.135       |
| 0.11   | 0.085           | 0.135       |
| 0.12   | 0.075           | 0.135       |
| 0.13   | 0.085           | 0.145       |
| 0.14   | 0.095           | 0.145       |
| 0.15   | 0.075           | 0.155       |
| 0.16   | 0.065           | 0.145       |
| 0.17   | 0.075           | 0.155       |
| 0.18   | 0.085           | 0.165       |
| 0.19   | 0.095           | 0.175       |
| 0.20   | 0.060           | 0.185       |
| 0.21   | 0.095           | 0.195       |
| 0.22   | 0.085           | 0.205       |
| 0.23   | 0.075           | 0.215       |
| 0.24   | 0.075           | 0.225       |
| 0.25   | 0.075           | 0.235       |
| 0.26   | 0.075           | 0.245       |
| 0.27   | 0.075           | 0.255       |
| 0.28   | 0.075           | 0.265       |
| 0.29   | 0.075           | 0.275       |
| 0.30   | 0.075           | 0.285       |
| 0.31   | 0.075           | 0.295       |
| 0.32   | 0.075           | 0.305       |
| 0.33   | 0.075           | 0.315       |
| 0.34   | 0.075           | 0.325       |
| 0.35   | 0.075           | 0.335       |
| 0.36   | 0.075           | 0.345       |
| 0.37   | 0.075           | 0.355       |
| 0.38   | 0.075           | 0.365       |
| 0.39   | 0.075           | 0.375       |
| 0.40   | 0.075           | 0.385       |
| 0.41   | 0.075           | 0.395       |
| 0.42   | 0.075           | 0.405       |
| 0.43   | 0.075           | 0.415       |
| 0.44   | 0.075           | 0.425       |
| 0.45   | 0.075           | 0.435       |
| 0.46   | 0.075           | 0.445       |
| 0.47   | 0.075           | 0.455       |
| 0.48   | 0.075           | 0.465       |
| 0.49   | 0.075           | 0.475       |
| 0.50   | 0.075           | 0.485       |
| 1      | -               | -           |
</details>

FIGURE 2.17. The KNN training error rate (blue, 200 observations) and test error rate (orange, 5,000 observations) on the data from Figure 2.13, as the level of flexibility (assessed using 1/K on the log scale) increases, or equivalently as the number of neighbors K decreases. The black dashed line indicates the Bayes error rate. The jumpiness of the curves is due to the small size of the training data set.

# 2.3 Lab: Introduction to Python

# 2.3.1 Getting Started

To run the labs in this book, you will need two things:

1. An installation of Python3, which is the specific version of Python used in the labs.   
2. Access to Jupyter, a very popular Python interface that runs code through a file called a notebook.

notebook

You can download and install Python3 by following the instructions available at anaconda.com.

There are a number of ways to get access to Jupyter. Here are just a few:

1. Using Google's Colaboratory service: colab.research.google.com/.   
2. Using JupyterHub, available at jupyter.org/hub.   
3. Using your own jupyter installation. Installation instructions are available at jupyter.org/install.

Please see the Python resources page on the book website statlearning.com for up-to-date information about getting Python and Jupyter working on your computer.

You will need to install the ISLP package, which provides access to the datasets and custom-built functions that we provide. Inside a macOS or Linux terminal type pip install ISLP; this also installs most other packages needed in the labs. The Python resources page has a link to the ISLP documentation website.

To run this lab, download the file Ch2-statlearn-lab.ipynb from the Python resources page. Now run the following code at the command line: jupyter lab Ch2-statlearn-lab.ipynb.

If you're using Windows, you can use the start menu to access anaconda, and follow the links. For example, to install ISLP and run this lab, you can run the same code above in an anaconda shell.

# 2.3.2 Basic Commands

In this lab, we will introduce some simple Python commands. For more resources about Python in general, readers may want to consult the tutorial at docs.python.org/3/tutorial/.

Like most programming languages, Python uses functions to perform operations. To run a function called fun, we type fun(input1, input2), where the inputs (or arguments) input1 and input2 tell Python how to run the function. A function can have any number of inputs. For example, the print() function outputs a text representation of all of its arguments to the console.

function

argument

print()

fit a model with 11 variables

The following command will provide information about the print() function.

In [2]: print?

Adding two integers in Python is pretty intuitive.

In [3]: 3 + 5

Out [3]: 8

In Python, textual data is handled using strings. For instance, "hello" and 'hello' are strings. We can concatenate them using the addition + symbol. string

In [4]: "hello" + " " + "world"

Out[4]: 'hello world'

A string is actually a type of sequence: this is a generic term for an ordered sequence list. The three most important types of sequences are lists, tuples, and strings. We introduce lists now.

The following command instructs Python to join together the numbers 3, 4, and 5, and to save them as a list named x. When we type x, it gives us back the list.

In [5]: x = [3, 4, 5]
x

Out[5]: [3, 4, 5]

Note that we used the brackets [] to construct this list.

We will often want to add two sets of numbers together. It is reasonable to try the following code, though it will not produce the desired results.

In [6]: y = [4, 9, 7]
x + y

Out[6]: [3, 4, 5, 4, 9, 7]

The result may appear slightly counterintuitive: why did Python not add the entries of the lists element-by-element? In Python, lists hold arbitrary objects, and are added using concatenation. In fact, concatenation is the behavior that we saw earlier when we entered "hello" + " " + "world".

This example reflects the fact that Python is a general-purpose programming language. Much of Python's data-specific functionality comes from other packages, notably numpy and pandas. In the next section, we will introduce the numpy package. See docs.scipy.org/doc/numpy/user/quickstart.html for more information about numpy.

concatenat-
ion

# 2.3.3 Introduction to Numerical Python

As mentioned earlier, this book makes use of functionality that is contained in the numpy library, or package. A package is a collection of modules that are not necessarily included in the base Python distribution. The name numpy is an abbreviation for numerical Python.

To access numpy, we must first import it.

numpy
package

In [7]:

```txt
import numpy as np 
```

import

In the previous line, we named the numpy module np; an abbreviation for easier referencing.

module

In numpy, an array is a generic term for a multidimensional set of numbers. We use the np.array() function to define x and y, which are one-dimensional arrays, i.e. vectors.

array

np.array()

In [8]:

```python
x = np.array([3, 4, 5])
y = np.array([4, 9, 7]) 
```

Note that if you forgot to run the import numpy as np command earlier, then you will encounter an error in calling the np.array() function in the previous line. The syntax np.array() indicates that the function being called is part of the numpy package, which we have abbreviated as np.

Since x and y have been defined using np.array(), we get a sensible result when we add them together. Compare this to our results in the previous section, when we tried to add two lists without using numpy.

In [9]:

```txt
x + y 
```

Out [9]:

```txt
array([7, 13, 12]) 
```

In numpy, matrices are typically represented as two-dimensional arrays, and vectors as one-dimensional arrays. $^{1}$ We can create a two-dimensional array as follows.

In [10]:

```txt
x = np.array([[1, 2], [3, 4]])
x 
```

Out [10]:

```txt
array([[1, 2], [3, 4]]) 
```

attribute

ndim

The object x has several attributes, or associated objects. To access an attribute of x, we type x.attribute, where we replace attribute with the name of the attribute. For instance, we can access the ndim attribute of x as follows.

In [11]:

```txt
x.ndim 
```

Out [11]: 2

The output indicates that x is a two-dimensional array. Similarly, x.dtype is the data type attribute of the object x. This indicates that x is comprised of 64-bit integers:

data type

In [12]: x.dtype

Out[12]: dtype('int64')

Why is x comprised of integers? This is because we created x by passing in exclusively integers to the np.array() function. If we had passed in any decimals, then we would have obtained an array of floating point numbers (i.e. real-valued numbers).

floating point

In [13]: np.array([[1, 2], [3.0, 4]]).dtype

Out[13]: dtype('float64')

Typing fun? will cause Python to display documentation associated with the function fun, if it exists. We can try this for np.array().

In [14]: np.array?

This documentation indicates that we could create a floating point array by passing a dtype argument into np.array().

dtype

In [15]: np.array([[1, 2], [3, 4]], float).dtype

Out[15]: dtype('float64')

The array x is two-dimensional. We can find out the number of rows and columns by looking at its shape attribute.

shape

In [16]: x.shape

Out [16]: (2, 2)

A method is a function that is associated with an object. For instance, given an array x, the expression x.sum() sums all of its elements, using the sum() method for arrays. The call x.sum() automatically provides x as the first argument to its sum() method.

method

.sum()

In [17]: x = np.array([1, 2, 3, 4])
x.sum()

Out [17]: 10

We could also sum the elements of x by passing in x as an argument to the np.sum() function.

np.sum()

In [18]: x = np.array([1, 2, 3, 4])
np.sum(x)

Out [18]: 10

As another example, the reshape() method returns a new array with the same elements as x, but a different shape. We do this by passing in a tuple

.reshape()
tuple

in our call to reshape(), in this case (2, 3). This tuple specifies that we would like to create a two-dimensional array with 2 rows and 3 columns. $^{2}$

In what follows, the \n character creates a new line.

In [19]:   
```python
x = np.array([1, 2, 3, 4, 5, 6])
print('beginning x:\n', x)
x_reshape = x.reshape((2, 3))
print('reshaped x:\n', x_reshape) 
```

```yaml
beginning x:
[1 2 3 4 5 6]
reshaped x:
[[1 2 3]
[4 5 6]] 
```

The previous output reveals that numpy arrays are specified as a sequence of rows. This is called row-major ordering, as opposed to column-major ordering.

Python (and hence numpy) uses 0-based indexing. This means that to access the top left element of x\_reshape, we type in x\_reshape[0,0].

In [20]:   
```txt
x_reshape[0, 0] 
```  
Out [20]: 1

Similarly, x\_reshape[1,2] yields the element in the second row and the third column of x\_reshape.

In [21]:   
```txt
x_reshape[1, 2] 
```  
Out [21]: 6

Similarly, x[2] yields the third entry of x.

Now, let's modify the top left element of $\mathbf{x\_reshape}$ . To our surprise, we discover that the first element of $\mathbf{x}$ has been modified as well!

In [22]:   
```python
print('x before we modify x_reshape:\n', x)
print('x_reshape before we modify x_reshape:\n', x_reshape)
x_reshape[0, 0] = 5
print('x_reshape after we modify its top left element:\n', x_reshape)
print('x after we modify top left element of x_reshape:\n', x) 
```

Out[22]: x before we modify x.reshape:   
```txt
[1 2 3 4 5 6]
x_reshape before we modify x_reshape:
[[1 2 3]
[4 5 6]]
x_reshape after we modify its top left element:
[[5 2 3] 
```

```ini
[4 5 6]]
x after we modify top left element of x.reshape:
[5 2 3 4 5 6] 
```

Modifying x\_reshape also modified x because the two objects occupy the same space in memory.

We just saw that we can modify an element of an array. Can we also modify a tuple? It turns out that we cannot — and trying to do so introduces an exception, or error.

exception

```python
In [23]: my_tuple = (3, 4, 5)
my_tuple[0] = 2 
```

```txt
TypeError: 'tuple' object does not support item assignment 
```

We now briefly mention some attributes of arrays that will come in handy. An array's shape attribute contains its dimension; this is always a tuple. The ndim attribute yields the number of dimensions, and T provides its transpose.

```javascript
In [24]: x_reshape.shape, x_reshape.ndim, x_reshape.T 
```

```python
Out[24]: ((2, 3),
    2,
    array([[5, 4],
    [2, 5],
    [3, 6]]) 
```

Notice that the three individual outputs $(2,3)$ , 2, and array([5, 4], [2, 5], [3,6]]) are themselves output as a tuple.

We will often want to apply functions to arrays. For instance, we can compute the square root of the entries using the np.sqrt() function:

np.sqrt()

```txt
In [25]: np.sqrt(x) 
```

```txt
Out[25]: array([2.24, 1.41, 1.73, 2., 2.24, 2.45])
```

We can also square the elements:

```txt
In [26]: x**2 
```

```txt
Out[26]: array([25, 4, 9, 16, 25, 36]) 
```

We can compute the square roots using the same notation, raising to the power of 1/2 instead of 2.

```txt
In [27]: x**0.5 
```

```txt
Out[27]: array([2.24, 1.41, 1.73, 2., 2.24, 2.45])
```

Throughout this book, we will often want to generate random data. The np.random.normal() function generates a vector of random normal variables. We can learn more about this function by looking at the help page, via a call to np.random.normal?. The first line of the help page reads normal(loc=0.0, scale=1.0, size=None). This signature line tells us that the function's ar-

np.random.
normal()

signature

guments are loc, scale, and size. These are keyword arguments, which means that when they are passed into the function, they can be referred to by name (in any order). $^{3}$ By default, this function will generate random normal variable(s) with mean (loc) 0 and standard deviation (scale) 1; furthermore, a single random variable will be generated unless the argument to size is changed.

keyword

We now generate 50 independent random variables from a $N(0,1)$ distribution.

```txt
In [28]: x = np.random.normal(size=50)
x 
```

```javascript
Out[28]: array([-1.19, 0.41, 0.9, -0.44, -0.9, -0.38, 0.13, 1.87, -0.35, 1.16, 0.79, -0.97, -1.21, 0.06, -1.62, -0.6, -0.77, -2.12, 0.38, -1.22, -0.06, -1.97, -1.74, -0.56, 1.7, -0.95, 0.56, 0.35, 0.87, 0.88, -1.66, -0.32, -0.3, -1.36, 0.92, -0.31, 1.28, -1.94, 1.07, 0.07, 0.79, -0.46, 2.19, -0.27, -0.64, 0.85, 0.13, 0.46, -0.09, 0.7]) 
```

We create an array y by adding an independent $N(50,1)$ random variable to each element of x.

```txt
In [29]: y = x + np.random.normal(loc=50, scale=1, size=50) 
```

The np.corrcoef() function computes the correlation matrix between x and y. The off-diagonal elements give the correlation between x and y.

np.corrcoef()

```javascript
In [30]: np.corrcoef(x, y) 
```

```txt
Out[30]: array([[1., 0.69], [0.69, 1.]]) 
```

If you're following along in your own Jupyter notebook, then you probably noticed that you got a different set of results when you ran the past few commands. In particular, each time we call np.random.normal(), we will get a different answer, as shown in the following example.

```python
In [31]: print(np.random.normal(scale=5, size=2))
print(np.random.normal(scale=5, size=2)) 
```

```txt
Out[31]: [4.28 2.59]
[4.62 -2.54] 
```

In order to ensure that our code provides exactly the same results each time it is run, we can set a random seed using the np.random.default\_rng() function. This function takes an arbitrary, user-specified integer argument. If we set a random seed before generating random data, then re-running our code will yield the same results. The object rng has essentially all the

random seed
np.random.
default\_rng()

random number generating methods found in np.random. Hence, to generate normal data we use rng.normal().

```python
In [32]: rng = np.random.default_rng(1303)
print(rng.normal(scale=5, size=2))
rng2 = np.random.default_rng(1303)
print(rng2.normal(scale=5, size=2)) 
```

```txt
Out [32]: [4.09 -1.07]
[4.09 -1.07] 
```

Throughout the labs in this book, we use np.random.default\_rng() whenever we perform calculations involving random quantities within numpy. In principle, this should enable the reader to exactly reproduce the stated results. However, as new versions of numpy become available, it is possible that some small discrepancies may occur between the output in the labs and the output from numpy.

The np.mean(), np.var(), and np.std() functions can be used to compute the mean, variance, and standard deviation of arrays. These functions are also available as methods on the arrays.

```txt
np.mean()
np.var()
np.std() 
```

```python
In [33]: rng = np.random.default_rng(3)
y = rng.standard_normal(10)
np.mean(y), y.mean() 
```

```txt
Out [33]: (-0.11, -0.11) 
```

```txt
In [34]: np.var(y), y.var(), np.mean((y - y.mean())**2) 
```

```txt
Out [34]: (2.72, 2.72, 2.72) 
```

Notice that by default np.var() divides by the sample size n rather than n-1; see the ddof argument in np.var?.

```javascript
In [35]: np.sqrt(np.var(y)), np.std(y) 
```

```txt
Out [35]: (1.65, 1.65) 
```

The np.mean(), np.var(), and np.std() functions can also be applied to the rows and columns of a matrix. To see this, we construct a $10 \times 3$ matrix of $N(0,1)$ random variables, and consider computing its row sums.

```python
In [36]: X = rng.standard_normal((10, 3))
X 
```

```javascript
Out[36]: array([[0.23, -0.35, -0.28], [-0.67, -1.06, -0.39], [0.48, -0.24, 0.96], [-0.2, 0.02, 1.55], [0.55, -0.51, -0.18], [0.54, 1.94, -0.27], [-0.24, 1., -0.89], [-0.29, 0.88, 0.58], [0.09, 0.67, -2.83], [1.02, -0.96, -1.67]]) 
```

Since arrays are row-major ordered, the first axis, i.e. axis=0, refers to its rows. We pass this argument into the mean() method for the object X.

```javascript
In [37]: X.mean(axis=0) 
```

.mean()

```txt
Out[37]: array([0.15, 0.14, -0.34])
```

The following yields the same result.

```javascript
In [38]: X.mean(0) 
```

```txt
Out[38]: array([0.15, 0.14, -0.34])
```

# 2.3.4 Graphics

In Python, common practice is to use the library matplotlib for graphics. However, since Python was not written with data analysis in mind, the notion of plotting is not intrinsic to the language. We will use the subplots() function from matplotlib.pyplot to create a figure and the axes onto which we plot our data. For many more examples of how to make plots in Python, readers are encouraged to visit matplotlib.org/stable/gallery/.

In matplotlib, a plot consists of a figure and one or more axes. You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window. The axes contain important information about each plot, such as its x- and y-axis labels, title, and more. (Note that in matplotlib, the word axes is not the plural of axis: a plot's axes contains much more information than just the x-axis and the y-axis.)

We begin by importing the subplots() function from matplotlib. We use this function throughout when creating figures. The function returns a tuple of length two: a figure object as well as the relevant axes object. We will typically pass figsize as a keyword argument. Having created our axes, we attempt our first plot using its plot() method. To learn more about it, type ax.plot?.

matplotlib

figure
axes

subplots()

.plot()

```python
In [39]: from matplotlib.pyplot import subplots
fig, ax = subplots(figsize=(8, 8))
x = rng.standard_normal(100)
y = rng.standard_normal(100)
ax.plot(x, y); 
```

We pause here to note that we have unpacked the tuple of length two returned by subplots() into the two distinct variables fig and ax. Unpacking is typically preferred to the following equivalent but slightly more verbose code:

```python
In [40]: output = subplots(figsize=(8, 8))
fig = output[0]
ax = output[1] 
```

We see that our earlier cell produced a line plot, which is the default. To create a scatterplot, we provide an additional argument to ax.plot(), indicating that circles should be displayed.

```matlab
In [41]: fig, ax = subplots(figsize=(8, 8))
ax.plot(x, y, 'o'); 
```

Different values of this additional argument can be used to produce different colored lines as well as different linestyles.

As an alternative, we could use the ax.scatter() function to create a scatterplot.

.scatter()

```javascript
In [42]: fig, ax = subplots(figsize=(8, 8))
ax.scatter(x, y, marker='o'); 
```

Notice that in the code blocks above, we have ended the last line with a semicolon. This prevents ax.plot(x, y) from printing text to the notebook. However, it does not prevent a plot from being produced. If we omit the trailing semi-colon, then we obtain the following output:

```txt
In [43]: fig, ax = subplots(figsize=(8, 8))
ax.scatter(x, y, marker='o') 
```

```txt
Out[43]: <matplotlib.collections.PathCollection at 0x7fb3d9c8f310> Figure(432x288) 
```

In what follows, we will use trailing semicolons whenever the text that would be output is not germane to the discussion at hand.

To label our plot, we make use of the set\_xlabel(), set\_ylabel(), and set\_title() methods of ax.

.set\_xlabel()

.set\_ylabel()

```txt
In [44]: fig, ax = subplots(figsize=(8, 8))
ax.scatter(x, y, marker='o')
ax.set_xlabel("this is the x-axis")
ax.set_ylabel("this is the y-axis")
ax.set_title("Plot of X vs Y"); 
```

.set\_title()

Having access to the figure object fig itself means that we can go in and change some aspects and then redisplay it. Here, we change the size from (8, 8) to (12, 3).

```txt
fig.set_size_inches(12,3)
fig 
```

Occasionally we will want to create several plots within a figure. This can be achieved by passing additional arguments to subplots(). Below, we create a $2 \times 3$ grid of plots in a figure of size determined by the figsize argument. In such situations, there is often a relationship between the axes in the plots. For example, all plots may have a common x-axis. The subplots() function can automatically handle this situation when passed the keyword argument sharex=True. The axes object below is an array pointing to different plots in the figure.

```txt
In [45]: fig, axes = subplots(nrows=2,
    ncols=3,
    figsize=(15, 5)) 
```

We now produce a scatter plot with 'o' in the second column of the first row and a scatter plot with '+' in the third column of the second row.

```asm
In [46]: axes[0,1].plot(x, y, 'o')
axes[1,2].scatter(x, y, marker=' +')
fig 
```

Type subplots? to learn more about subplots().

To save the output of fig, we call its savefig() method. The argument dpi is the dots per inch, used to determine how large the figure will be in pixels.

.savefig()

```txt
In [47]: fig.savefig("Figure.png", dpi=400)
fig.savefig("Figure.pdf", dpi=200); 
```

We can continue to modify fig using step-by-step updates; for example, we can modify the range of the $x$ -axis, re-save the figure, and even re-display it.

```txt
In [48]: axes[0,1].set_xlim([-1,1])
fig.savefig("Figure_updated.jpg")
fig 
```

We now create some more sophisticated plots. The ax.contour() method produces a contour plot in order to represent three-dimensional data, similar to a topographical map. It takes three arguments:

.contour()
contour plot

- A vector of $\mathbf{x}$ values (the first dimension),   
- A vector of $\mathbf{y}$ values (the second dimension), and   
- A matrix whose elements correspond to the $z$ value (the third dimension) for each pair of $(x, y)$ coordinates.

To create x and y, we'll use the command np.linspace(a, b, n), which returns a vector of n numbers starting at a and ending at b.

np.linspace()

```javascript
In [49]: fig, ax = subplots(figsize=(8, 8))
x = np.linspace(-np.pi, np.pi, 50)
y = x
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
ax.contour(x, y, f); 
```

We can increase the resolution by adding more levels to the image.

```javascript
In [50]: fig, ax = subplots(figsize=(8, 8))
ax.contour(x, y, f, levels=45); 
```

To fine-tune the output of the ax.contour() function, take a look at the help file by typing ?plt.contour.

.imshow()

The ax.imshow() method is similar to ax.contour(), except that it produces a color-coded plot whose colors depend on the z value. This is known as a heatmap, and is sometimes used to plot temperature in weather forecasts.

heatmap

```txt
In [51]: fig, ax = subplots(figsize=(8, 8))
ax.imshow(f); 
```

# 2.3.5 Sequences and Slice Notation

As seen above, the function np.linspace() can be used to create a sequence of numbers.

```txt
In [52]: seq1 = np.linspace(0, 10, 11)
seq1 
```

```txt
Out[52]: array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]) 
```

The function np.arange() returns a sequence of numbers spaced out by step. If step is not specified, then a default value of 1 is used. Let's create a sequence that starts at 0 and ends at 10.

np.arange()

```txt
In [53]: seq2 = np.arange(0, 10)
seq2 
```

```txt
Out[53]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
```

Why isn't 10 output above? This has to do with slice notation in Python. Slice notation is used to index sequences such as lists, tuples and arrays. Suppose we want to retrieve the fourth through sixth (inclusive) entries of a string. We obtain a slice of the string using the indexing notation [3:6].

slice

```txt
In [54]: "hello world" [3:6] 
```

```txt
Out[54]: 'lo'
```

In the code block above, the notation 3:6 is shorthand for slice(3,6) when used inside [].

```javascript
In [55]: "hello world" [slice(3,6)] 
```

```txt
Out[55]: 'lo'
```

You might have expected slice(3,6) to output the fourth through seventh characters in the text string (recalling that Python begins its indexing at zero), but instead it output the fourth through sixth. This also explains why the earlier np.arange(0, 10) command output only the integers from 0 to 9. See the documentation slice? for useful options in creating slices.

# 2.3.6 Indexing Data

To begin, we create a two-dimensional numpy array.

```txt
In [56]: A = np.array(np.arange(16)).reshape((4, 4))
A 
```

```txt
Out[56]: array([[0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]]) 
```

Typing A[1,2] retrieves the element corresponding to the second row and third column. (As usual, Python indexes from 0.)

In [57]: A[1,2]

Out [57]: 6

The first number after the open-bracket symbol [ refers to the row, and the second number refers to the column.

Indexing Rows, Columns, and Submatrices

To select multiple rows at a time, we can pass in a list specifying our selection. For instance, $[1,3]$ will retrieve the second and fourth rows:

In [58]: A [[1,3]]

Out[58]: array([[4, 5, 6, 7], [12, 13, 14, 15]])

To select the first and third columns, we pass in $[0,2]$ as the second argument in the square brackets. In this case we need to supply the first argument: which selects all rows.

In [59]: A [:, [0, 2]]

Out[59]: array([[0, 2], [4, 6], [8, 10], [12, 14]])

Now, suppose that we want to select the submatrix made up of the second and fourth rows as well as the first and third columns. This is where indexing gets slightly tricky. It is natural to try to use lists to retrieve the rows and columns:

In [60]: A [[1,3], [0,2]]

Out[60]: array([4, 14])

Oops — what happened? We got a one-dimensional array of length two identical to

In [61]: np.array([A[1,0],A[3,2]])

Out[61]: array([4, 14])

Similarly, the following code fails to extract the submatrix comprised of the second and fourth rows and the first, third, and fourth columns:

In [62]: A[[1,3],[0,2,3]]

IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (2,) (3,)

We can see what has gone wrong here. When supplied with two indexing lists, the numpy interpretation is that these provide pairs of i, j indices for a series of entries. That is why the pair of lists must have the same length. However, that was not our intent, since we are looking for a submatrix.

One easy way to do this is as follows. We first create a submatrix by subsetting the rows of A, and then on the fly we make a further submatrix by subsetting its columns.

```json
In [63]: A [[1,3]] [:,[0,2]] 
```

```txt
Out[63]: array([[4, 6], [12, 14]])
```

There are more efficient ways of achieving the same result.

The convenience function np.ix\_() allows us to extract a submatrix using lists, by creating an intermediate mesh object.

```txt
convenience
function
np.ix_()
mesh 
```

```txt
In [64]: idx = np.ix_([1,3], [0,2,3])
A[idx] 
```

```txt
Out[64]: array([[4, 6, 7], [12, 14, 15]]) 
```

Alternatively, we can subset matrices efficiently using slices. The slice 1:4:2 captures the second and fourth items of a sequence, while the slice 0:3:2 captures the first and third items (the third element in a slice sequence is the step size).

```json
In [65]: A [1:4:2, 0:3:2] 
```

```txt
Out[65]: array([[4, 6], [12, 14]]) 
```

Why are we able to retrieve a submatrix directly using slices but not using lists? Its because they are different Python types, and are treated differently by numpy. Slices can be used to extract objects from arbitrary sequences, such as strings, lists, and tuples, while the use of lists for indexing is more limited.

# Boolean Indexing

Boolean

In numpy, a Boolean is a type that equals either True or False (also represented as 1 and 0, respectively). The next line creates a vector of 0's, represented as Booleans, of length equal to the first dimension of A.

```txt
In [66]: keep_rows = np.zeros(A.shape[0], bool)
keep_rows 
```

```txt
Out[66]: array([False, False, False, False]) 
```

We now set two of the elements to True.

```txt
In [67]: keep_rows[[1,3]] = True
keep_rows 
```

Out[67]: array([False, True, False, True])

Note that the elements of keep\_rows, when viewed as integers, are the same as the values of np.array([0,1,0,1]). Below, we use == to verify their equality. When applied to two arrays, the == operation is applied elementwise.

In [68]: np.all(keep\_rows == np.array([0,1,0,1]))

Out[68]: True

(Here, the function np.all() has checked whether all entries of an array are True. A similar function, np.any(), can be used to check whether any entries of an array are True.)

np.all()
np.any()

However, even though np.array([0,1,0,1]) and keep\_rows are equal according to ==, they index different sets of rows! The former retrieves the first, second, first, and second rows of A.

In [69]: A [np.array([0,1,0,1])]

Out[69]: array([[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 2, 3], [4, 5, 6, 7]])

By contrast, keep\_rows retrieves only the second and fourth rows of A — i.e. the rows for which the Boolean equals TRUE.

In [70]: A[keep\_rows]

Out[70]: array([[4, 5, 6, 7], [12, 13, 14, 15]])

This example shows that Booleans and integers are treated differently by numpy.

We again make use of the np.ix\_() function to create a mesh containing the second and fourth rows, and the first, third, and fourth columns. This time, we apply the function to Booleans, rather than lists.

In [71]: keep\_cols = np.zeros(A.shape[1], bool)
keep\_cols[[0, 2, 3]] = True
idx\_bool = np.ix\_(keep\_rows, keep\_cols)
A[idx\_bool]

Out[71]: array([[4, 6, 7], [12, 14, 15]])

We can also mix a list with an array of Booleans in the arguments to np.ix\_():

In [72]: idx\_mixed = np.ix\_([1,3], keep\_cols)
A[idx\_mixed]

Out[72]: array([[4, 6, 7], [12, 14, 15]])

For more details on indexing in numpy, readers are referred to the numpy tutorial mentioned earlier.

# 2.3.7 Loading Data

Data sets often contain different types of data, and may have names associated with the rows or columns. For these reasons, they typically are best accommodated using a data frame. We can think of a data frame as a sequence of arrays of identical length; these are the columns. Entries in the different arrays can be combined to form a row. The pandas library can be used to create and work with data frame objects.

data frame

# Reading in a Data Set

The first step of most analyses involves importing a data set into Python. Before attempting to load a data set, we must make sure that Python knows where to find the file containing it. If the file is in the same location as this notebook file, then we are all set. Otherwise, the command os.chdir() can be used to change directory. (You will need to call import os before calling os.chdir().)

os.chdir()

We will begin by reading in Auto.csv, available on the book website. This is a comma-separated file, and can be read in using pd.read\_csv():

pd.read\_csv()

```txt
In [73]: import pandas as pd
Auto = pd.read_csv('Auto.csv')
Auto 
```

The book website also has a whitespace-delimited version of this data, called Auto.data. This can be read in as follows:

```python
In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True) 
```

Both Auto.csv and Auto.data are simply text files. Before loading data into Python, it is a good idea to view it using a text editor or other software, such as Microsoft Excel.

We now take a look at the column of Auto corresponding to the variable horsepower:

```txt
In [75]: Auto['horsepower'] 
```

```asm
Out [75]: 0 130.0
1 165.0
2 150.0
3 150.0
4 140.0
...
392 86.00
393 52.00
394 84.00
395 79.00
396 82.00 
```

Name: horsepower, Length: 397, dtype: object

We see that the dtype of this column is object. It turns out that all values of the horsepower column were interpreted as strings when reading in the data. We can find out why by looking at the unique values.

```javascript
In [76]: np.unique(Auto['horsepower']) 
```

To save space, we have omitted the output of the previous code block. We see the culprit is the value?, which is being used to encode missing values.

To fix the problem, we must provide pd.read\_csv() with an argument called na\_values. Now, each instance of ? in the file is replaced with the value np.nan, which means not a number:

```python
In [77]: Auto = pd.read_csv('Auto.data', na_values=['?'], delim_whitespace=True)
Auto['horsepower'].sum() 
```

```txt
Out [77]: 40952.0 
```

The Auto.shape attribute tells us that the data has 397 observations, or rows, and nine variables, or columns.

```javascript
In [78]: Auto.shape 
```

```txt
Out [78]: (397, 9) 
```

There are various ways to deal with missing data. In this case, since only five of the rows contain missing observations, we choose to use the Auto.dropna() method to simply remove these rows.

```python
In [79]: Auto_new = Auto.dropna()
Auto_new.shape 
```

```txt
Out [79]: (392, 9) 
```

.dropna()

# Basics of Selecting Rows and Columns

We can use Auto.columns to check the variable names.

```txt
In [80]: Auto = Auto_new # overwrite the previous value
Auto.columns 
```

```javascript
Out[80]: Index(['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'name'], dtype='object') 
```

Accessing the rows and columns of a data frame is similar, but not identical, to accessing the rows and columns of an array. Recall that the first argument to the [] method is always applied to the rows of the array. Similarly, passing in a slice to the [] method creates a data frame whose rows are determined by the slice:

```txt
In [81]: Auto[:3] 
```

```matlab
Out[81]: mpg cylinders displacement horsepower weight ...
0 18.0 8 307.0 130.0 3504.0 ...
1 15.0 8 350.0 165.0 3693.0 ...
2 18.0 8 318.0 150.0 3436.0 ... 
```

Similarly, an array of Booleans can be used to subset the rows:

```txt
In [82]: idx_80 = Auto['year'] > 80
Auto[idx_80] 
```

However, if we pass in a list of strings to the [] method, then we obtain a data frame containing the corresponding set of columns.

```txt
In [83]: Auto[['mpg', 'horsepower']] 
```

```txt
Out [83]: mpg horsepower
0 18.0 130.0
1 15.0 165.0
2 18.0 150.0
3 16.0 150.0
4 17.0 140.0
... ... ...
392 27.0 86.0
393 44.0 52.0
394 32.0 84.0
395 28.0 79.0
396 31.0 82.0
392 rows x 2 columns 
```

Since we did not specify an index column when we loaded our data frame, the rows are labeled using integers 0 to 396.

```txt
In [84]: Auto.index 
```

```javascript
Out[84]: Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ... 387, 388, 389, 390, 391, 392, 393, 394, 395, 396], dtype='int64', length=392) 
```

We can use the set\_index() method to re-name the rows using the contents of Auto['name'].

.set\_index()

```python
In [85]: Auto_re = Auto.set_index('name')
Auto_re 
```

```txt
Out[85]:
mpg cylinders displacement ...
name
chevrolet chevelle malibu 18.0 8 307.0 ...
buick skylark 32 15.0 8 350.0 ...
plymouth satellite 18.0 8 318.0 ...
amc rebel sst 16.0 8 304.0 ... 
```

```txt
In [86]: Auto_re.columns 
```

```javascript
Out[86]: Index(['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin'], dtype='object') 
```

We see that the column 'name' is no longer there.

Now that the index has been set to name, we can access rows of the data frame by name using the loc[] method of Auto:

.loc[]

```txt
In [87]: rows = ['amc rebel sst', 'ford torino']
Auto_re.loc[rows] 
```

```txt
Out[87]: mpg cylinders displacement horsepower ...
name
amc rebel sst 16.0 8 304.0 150.0 ...
ford torino 17.0 8 302.0 140.0 ... 
```

As an alternative to using the index name, we could retrieve the 4th and 5th rows of Auto using the iloc[] method:

.iloc[]

```txt
In [88]: Auto_re.iloc[[3,4]] 
```

We can also use it to retrieve the 1st, 3rd and and 4th columns of Auto\_re:

```txt
In [89]: Auto_re.iloc[:, [0, 2, 3]] 
```

We can extract the 4th and 5th rows, as well as the 1st, 3rd and 4th columns, using a single call to iloc[]:

```txt
In [90]: Auto_re.iloc[[3,4],[0,2,3]] 
```

```txt
Out[90]: mpg displacement horsepower
name
amc rebel sst 16.0 304.0 150.0
ford torino 17.0 302.0 140.0 
```

Index entries need not be unique: there are several cars in the data frame named ford galaxie 500.

```python
In [91]: Auto_re.loc['ford galaxie 500', ['mpg', 'origin']] 
```

```txt
Out [91]:
mpg origin
name
ford galaxie 500 15.0 1
ford galaxie 500 14.0 1
ford galaxie 500 14.0 1 
```

# More on Selecting Rows and Columns

Suppose now that we want to create a data frame consisting of the weight and origin of the subset of cars with year greater than 80 — i.e. those built after 1980. To do this, we first create a Boolean array that indexes the rows. The loc[] method allows for Boolean entries as well as strings:

```txt
In [92]: idx_80 = Auto_re['year'] > 80
Auto_re.loc[idx_80, ['weight', 'origin']] 
```

To do this more concisely, we can use an anonymous function called a lambda:

lambda

```txt
In [93]: Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']] 
```

The lambda call creates a function that takes a single argument, here df, and returns df['year]>80. Since it is created inside the loc[] method for the dataframe Auto\_re, that dataframe will be the argument supplied. As another example of using a lambda, suppose that we want all cars built after 1980 that achieve greater than 30 miles per gallon:

In [94]:

```txt
Auto_re.loc[lambda df: (df['year'] > 80) & (df['mpg'] > 30), ['weight', 'origin']
] 
```

The symbol & computes an element-wise and operation. As another example, suppose that we want to retrieve all Ford and Datsun cars with displacement less than 300. We check whether each name entry contains either the string ford or datsun using the str.contains() method of the index attribute of the dataframe:

```txt
.str.
contains() 
```

In [95]:

```txt
Auto_re.loc[lambda df: (df['displacement'] < 300)
& (df.index.str.contains('ford')
| df.index.str.contains('datsun'),
['weight', 'origin']
] 
```

Here, the symbol | computes an element-wise or operation.

In summary, a powerful set of operations is available to index the rows and columns of data frames. For integer based queries, use the iloc[] method. For string and Boolean selections, use the loc[] method. For functional queries that filter rows, use the loc[] method with a function (typically a lambda) in the rows argument.

# 2.3.8 For Loops

A for loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code. For example, suppose we loop over elements of a list and compute their sum.

for

In [96]:

```python
total = 0
for value in [3,2,19]:
    total += value
print('Total is: {0}'.format(total)) 
```

Total is: 24

The indented code beneath the line with the for statement is run for each value in the sequence specified in the for statement. The loop ends either when the cell ends or when code is indented at the same level as the original for statement. We see that the final line above which prints the total is executed only once after the for loop has terminated. Loops can be nested by additional indentation.

In [97]:

```python
total = 0
for value in [2,3,19]:
    for weight in [3, 2, 1]:
    total += value * weight
print('Total is: {0}'.format(total)) 
```

Total is: 144

Above, we summed over each combination of value and weight. We also took advantage of the increment notation in Python: the expression $a += b$ is equivalent to $a = a + b$ . Besides being a convenient notation, this can save time in computationally heavy tasks in which the intermediate value of $a+b$ need not be explicitly created.

increment

Perhaps a more common task would be to sum over (value, weight) pairs. For instance, to compute the average value of a random variable that takes on possible values 2, 3 or 19 with probability 0.2, 0.3, 0.5 respectively we would compute the weighted sum. Tasks such as this can often be accomplished using the zip() function that loops over a sequence of tuples.

zip()

In [98]:

```python
total = 0
for value, weight in zip([2,3,19],
    [0.2,0.3,0.5]):
    total += weight * value
print('Weighted average is: {0}'.format(total)) 
```

Weighted average is: 10.8

# String Formatting

In the code chunk above we also printed a string displaying the total. However, the object total is an integer and not a string. Inserting the value of something into a string is a common task, made simple using some of the powerful string formatting tools in Python. Many data cleaning tasks involve manipulating and programmatically producing strings.

np.nan

For example we may want to loop over the columns of a data frame and print the percent missing in each column. Let's create a data frame D with columns in which 20% of the entries are missing i.e. set to np.nan. We'll create the values in D from a normal distribution with mean 0 and variance 1 using rng.standard\_normal() and then overwrite some random entries using rng.choice().

In [99]:

```python
rng = np.random.default_rng(1)
A = rng.standard_normal((127, 5))
M = rng.choice([0, np.nan], p=[0.8,0.2], size=A.shape)
A += M
D = pd.DataFrame(A, columns=['food',
    'bar',
    'pickle',
    'snack',
    'popcorn'])
D[:3] 
```

Out [99]:

```txt
food bar pickle snack popcorn 0.345584 0.821618 0.330437 -1.303157 NaN 1 NaN -0.536953 0.581118 0.364572 0.294132 2 NaN 0.546713 NaN -0.162910 -0.482119 
```

In [100]:

```python
for col in D.columns:
    template = 'Column "{0}" has {1:.2%} missing values'
    print(template.format(col,
    np.isnan(D[col]).mean())) 
```

```txt
Column "food" has 16.54% missing values
Column "bar" has 25.98% missing values
Column "pickle" has 29.13% missing values
Column "snack" has 21.26% missing values
Column "popcorn" has 22.83% missing values 
```

We see that the template.format() method expects two arguments $\{0\}$ and $\{1:.2\%$ , and the latter includes some formatting information. In particular, it specifies that the second argument should be expressed as a percent with two decimal digits.

The reference docs.python.org/3/library/string.html includes many helpful and more complex examples.

# 2.3.9 Additional Graphical and Numerical Summaries

We can use the ax.plot() or ax.scatter() functions to display the quantitative variables. However, simply typing the variable names will produce an error message, because Python does not know to look in the Auto data set for those variables.

```txt
In [101]: fig, ax = subplots(figsize=(8, 8))
ax.plot(horsepower, mpg, 'o'); 
```

```txt
NameError: name 'horsepower' is not defined 
```

We can address this by accessing the columns directly:

```javascript
In [102]: fig, ax = subplots(figsize=(8, 8))
ax.plot(Auto['horsepower'], Auto['mpg'], 'o'); 
```

Alternatively, we can use the plot() method with the call Auto.plot(). Using this method, the variables can be accessed by name. The plot methods of a data frame return a familiar object: an axes. We can use it to update the plot as we did previously:

```txt
In [103]: ax = Auto.plot.scatter('horsepower', 'mpg');
ax.set_title('Horsepower vs. MPG') 
```

If we want to save the figure that contains a given axes, we can find the relevant figure by accessing the figure attribute:

```txt
In [104]: fig = ax.figure
fig.savefig('horsepower_mpg.png'); 
```

We can further instruct the data frame to plot to a particular axes object. In this case the corresponding plot() method will return the modified axes we passed in as an argument. Note that when we request a one-dimensional grid of plots, the object axes is similarly one-dimensional. We place our scatter plot in the middle plot of a row of three plots within a figure.

```javascript
In [105]: fig, axes = subplots(ncols=3, figsize=(15, 5))
Auto.plot.scatter('horsepower', 'mpg', ax=axes[1]); 
```

Note also that the columns of a data frame can be accessed as attributes: try typing in Auto.horsepower.

We now consider the cylinders variable. Typing in Auto.cylinders.dtype reveals that it is being treated as a quantitative variable. However, since there is only a small number of possible values for this variable, we may wish to treat it as qualitative. Below, we replace the cylinders column with a categorical version of Auto.cylinders. The function pd.Series() owes its name to the fact that pandas is often used in time series applications.

pd.Series()

In [106]: Auto.cylinders = pd.Series(Auto.cylinders, dtype='category')
Auto.cylinders.dtype

.boxplot()

Now that cylinders is qualitative, we can display it using the boxplot() method.

In [107]: fig, ax = subplots(figsize=(8, 8))
Auto.boxplot('mpg', by='cylinders', ax=ax);

.hist()

The hist() method can be used to plot a histogram.

In [108]: fig, ax = subplots(figsize=(8, 8))
Auto.hist('mpg', ax=ax);

The color of the bars and the number of bins can be changed:

In [109]: fig, ax = subplots(figsize=(8, 8))
Auto.hist('mpg', color='red', bins=12, ax=ax);

See Auto.hist? for more plotting options.

pd.plotting.
scatter\_
matrix()

We can use the pd.plotting.scatter\_matrix() function to create a scatterplot matrix to visualize all of the pairwise relationships between the columns in a data frame.

In [110]: pd.plotting.scatter\_matrix(Auto);

We can also produce scatterplots for a subset of the variables.

In [111]: pd.plotting.scatter\_matrix(Auto[['mpg', 'displacement', 'weight']]);

.describe()

The describe() method produces a numerical summary of each column in a data frame.

In [112]: Auto[['mpg', 'weight']].describe()

We can also produce a summary of just a single column.

In [113]: Auto['cylinders'].describe()
Auto['mpg'].describe()

To exit Jupyter, select File / Close and Halt.

# 2.4 Exercises

# Conceptual

1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

(a) The sample size $n$ is extremely large, and the number of predictors $p$ is small.   
(b) The number of predictors $p$ is extremely large, and the number of observations $n$ is small.   
(c) The relationship between the predictors and response is highly non-linear.   
(d) The variance of the error terms, i.e. $\sigma^2 = \mathrm{Var}(\epsilon)$ , is extremely high.

2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

(a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.   
(b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.   
(c) We are interested in predicting the \% change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the \% change in the USD/Euro, the \% change in the US market, the \% change in the British market, and the \% change in the German market.

3. We now revisit the bias-variance decomposition.

(a) Provide a sketch of typical (squared) bias, variance, training error, test error, and Bayes (or irreducible) error curves, on a single plot, as we go from less flexible statistical learning methods towards more flexible approaches. The $x$ -axis should represent the amount of flexibility in the method, and the $y$ -axis should represent the values for each curve. There should be five curves. Make sure to label each one.

(b) Explain why each of the five curves has the shape displayed in part (a).

4. You will now think of some real-life applications for statistical learning.

(a) Describe three real-life applications in which classification might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.   
(b) Describe three real-life applications in which regression might be useful. Describe the response, as well as the predictors. Is the goal of each application inference or prediction? Explain your answer.   
(c) Describe three real-life applications in which cluster analysis might be useful.

5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

<table><tr><td>Obs.</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td>Y</td></tr><tr><td>1</td><td>0</td><td>3</td><td>0</td><td>Red</td></tr><tr><td>2</td><td>2</td><td>0</td><td>0</td><td>Red</td></tr><tr><td>3</td><td>0</td><td>1</td><td>3</td><td>Red</td></tr><tr><td>4</td><td>0</td><td>1</td><td>2</td><td>Green</td></tr><tr><td>5</td><td>-1</td><td>0</td><td>1</td><td>Green</td></tr><tr><td>6</td><td>1</td><td>1</td><td>1</td><td>Red</td></tr></table>

Suppose we wish to use this data set to make a prediction for Y when $X_{1}=X_{2}=X_{3}=0$ using K-nearest neighbors.

(a) Compute the Euclidean distance between each observation and the test point, $X_{1} = X_{2} = X_{3} = 0$ .   
(b) What is our prediction with $K = 1$ ? Why?   
(c) What is our prediction with $K = 3$ ? Why?   
(d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for $K$ to be large or small? Why?

# Applied

8. This exercise relates to the College data set, which can be found in the file College.csv on the book website. It contains a number of variables for 777 different universities and colleges in the US. The variables are

- Private: Public/private indicator   
- Apps : Number of applications received   
- Accept : Number of applicants accepted   
• Enroll : Number of new students enrolled   
- Top10perc : New students from top $10\%$ of high school class   
- Top25perc : New students from top 25 % of high school class   
• F. Undergrad : Number of full-time undergraduates   
• P.Undergrad : Number of part-time undergraduates   
• Outstate : Out-of-state tuition   
• Room.Board : Room and board costs   
• Books : Estimated book costs   
• Personal : Estimated personal spending   
• PhD : Percent of faculty with Ph.D.s   
• Terminal : Percent of faculty with terminal degree   
• S.F.Ratio : Student/faculty ratio   
• perc.alumni : Percent of alumni who donate   
- Expend : Instructional expenditure per student   
• Grad.Rate : Graduation rate

Before reading the data into Python, it can be viewed in Excel or a text editor.

(a) Use the pd.read\_csv() function to read the data into Python. Call the loaded data college. Make sure that you have the directory set to the correct location for the data.   
(b) Look at the data used in the notebook by creating and running a new cell with just the code college in it. You should notice that the first column is just the name of each university in a column named something like Unnamed: 0. We don't really want pandas to treat this as data. However, it may be handy to have these names for later. Try the following commands and similarly look at the resulting data frames:

```python
college2 = pd.read_csv('College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College') 
```

This has used the first column in the file as an index for the data frame. This means that pandas has given each row a name corresponding to the appropriate university. Now you should see that the first data column is Private. Note that the names of the colleges appear on the left of the table. We also introduced a new python object above: a dictionary, which is specified by (key, value) pairs. Keep your modified version of the data with the following:

dictionary

```txt
college = college3 
```

(c) Use the describe() method of to produce a numerical summary of the variables in the data set.   
(d) Use the pd.plotting.scatter\_matrix() function to produce a scatterplot matrix of the first columns [Top10perc, Apps, Enroll]. Recall that you can reference a list C of columns of a data frame A using A[C].   
(e) Use the boxplot() method of college to produce side-by-side boxplots of Outstate versus Private.   
(f) Create a new qualitative variable, called Elite, by binning the Top10perc variable into two groups based on whether or not the proportion of students coming from the top 10% of their high school classes exceeds 50%.

```python
college['Elite'] = pd.cut(college['Top10perc'], [0, 0.5, 1], labels=['No', 'Yes']) 
```

Use the value\_counts() method of college['Elite'] to see how many elite universities there are. Finally, use the boxplot() method again to produce side-by-side boxplots of Outstate versus Elite.

(g) Use the plot.hist() method of college to produce some histograms with differing numbers of bins for a few of the quantitative variables. The command plt.subplots(2, 2) may be useful: it will divide the plot window into four regions so that four plots can be made simultaneously. By changing the arguments you can divide the screen up in other combinations.   
(h) Continue exploring the data, and provide a brief summary of what you discover.

9. This exercise involves the Auto data set studied in the lab. Make sure that the missing values have been removed from the data.

(a) Which of the predictors are quantitative, and which are qualitative?   
(b) What is the range of each quantitative predictor? You can answer this using the min() and max() methods in numpy.   
(c) What is the mean and standard deviation of each quantitative predictor?

.min()

.max()

(d) Now remove the 10th through 85th observations. What is the range, mean, and standard deviation of each predictor in the subset of the data that remains?   
(e) Using the full data set, investigate the predictors graphically, using scatterplots or other tools of your choice. Create some plots highlighting the relationships among the predictors. Comment on your findings.   
(f) Suppose that we wish to predict gas mileage (mpg) on the basis of the other variables. Do your plots suggest that any of the other variables might be useful in predicting mpg? Justify your answer.

10. This exercise involves the Boston housing data set.

(a) To begin, load in the Boston data set, which is part of the ISLP library.   
(b) How many rows are in this data set? How many columns? What do the rows and columns represent?   
(c) Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.   
(d) Are any of the predictors associated with per capita crime rate? If so, explain the relationship.   
(e) Do any of the suburbs of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.   
(f) How many of the suburbs in this data set bound the Charles river?   
(g) What is the median pupil-teacher ratio among the towns in this data set?   
(h) Which suburb of Boston has lowest median value of owner-occupied homes? What are the values of the other predictors for that suburb, and how do those values compare to the overall ranges for those predictors? Comment on your findings.   
(i) In this data set, how many of the suburbs average more than seven rooms per dwelling? More than eight rooms per dwelling? Comment on the suburbs that average more than eight rooms per dwelling.

# 3

# Linear Regression

![](images/5d1546f1e2492411ba7739f8974699115687229207bb2aeffafed1a664fbe834.jpg)

This chapter is about linear regression, a very simple approach for supervised learning. In particular, linear regression is a useful tool for predicting a quantitative response. It has been around for a long time and is the topic of innumerable textbooks. Though it may seem somewhat dull compared to some of the more modern statistical learning approaches described in later chapters of this book, linear regression is still a useful and widely used statistical learning method. Moreover, it serves as a good jumping-off point for newer approaches: as we will see in later chapters, many fancy statistical learning approaches can be seen as generalizations or extensions of linear regression. Consequently, the importance of having a good understanding of linear regression before studying more complex learning methods cannot be overstated. In this chapter, we review some of the key ideas underlying the linear regression model, as well as the least squares approach that is most commonly used to fit this model.

Recall the Advertising data from Chapter 2. Figure 2.1 displays sales (in thousands of units) for a particular product as a function of advertising budgets (in thousands of dollars) for TV, radio, and newspaper media. Suppose that in our role as statistical consultants we are asked to suggest, on the basis of this data, a marketing plan for next year that will result in high product sales. What information would be useful in order to provide such a recommendation? Here are a few important questions that we might seek to address:

# 1. Is there a relationship between advertising budget and sales?

Our first goal should be to determine whether the data provide evidence of an association between advertising expenditure and sales. If the evidence is weak, then one might argue that no money should be spent on advertising!

2. How strong is the relationship between advertising budget and sales? Assuming that there is a relationship between advertising and sales, we would like to know the strength of this relationship. Does knowledge of the advertising budget provide a lot of information about product sales?   
3. Which media are associated with sales?

Are all three media—TV, radio, and newspaper—associated with sales, or are just one or two of the media associated? To answer this question, we must find a way to separate out the individual contribution of each medium to sales when we have spent money on all three media.

4. How large is the association between each medium and sales?

For every dollar spent on advertising in a particular medium, by what amount will sales increase? How accurately can we predict this amount of increase?

5. How accurately can we predict future sales?

For any given level of television, radio, or newspaper advertising, what is our prediction for sales, and what is the accuracy of this prediction?

6. Is the relationship linear?

If there is approximately a straight-line relationship between advertising expenditure in the various media and sales, then linear regression is an appropriate tool. If not, then it may still be possible to transform the predictor or the response so that linear regression can be used.

7. Is there synergy among the advertising media?

Perhaps spending \$50,000 on television advertising and \$50,000 on radio advertising is associated with higher sales than allocating \$100,000 to either television or radio individually. In marketing, this is known as a synergy effect, while in statistics it is called an interaction effect.

It turns out that linear regression can be used to answer each of these questions. We will first discuss all of these questions in a general context, and then return to them in this specific context in Section 3.4.

synergy interaction

# 3.1 Simple Linear Regression

Simple linear regression lives up to its name: it is a very straightforward approach for predicting a quantitative response Y on the basis of a single predictor variable X. It assumes that there is approximately a linear relationship between X and Y. Mathematically, we can write this linear relationship as

$$
Y \approx \beta_ {0} + \beta_ {1} X. \tag {3.1}
$$

You might read “ $\approx$ ” as “is approximately modeled as”. We will sometimes describe (3.1) by saying that we are regressing Y on X (or Y onto X).

simple linear regression

For example, X may represent TV advertising and Y may represent sales. Then we can regress sales onto TV by fitting the model

$$
\mathsf {s a l e s} \approx \beta_ {0} + \beta_ {1} \times \mathsf {T V}.
$$

In Equation 3.1, $\beta_{0}$ and $\beta_{1}$ are two unknown constants that represent the intercept and slope terms in the linear model. Together, $\beta_{0}$ and $\beta_{1}$ are known as the model coefficients or parameters. Once we have used our training data to produce estimates $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ for the model coefficients, we can predict future sales on the basis of a particular value of TV advertising by computing

$$
\hat {y} = \hat {\beta} _ {0} + \hat {\beta} _ {1} x, \tag {3.2}
$$

where $\hat{y}$ indicates a prediction of Y on the basis of X = x. Here we use a hat symbol, $\hat{}$ , to denote the estimated value for an unknown parameter or coefficient, or to denote the predicted value of the response.

intercept
slope
coefficient
parameter

# 3.1.1 Estimating the Coefficients

In practice, $\beta_{0}$ and $\beta_{1}$ are unknown. So before we can use (3.1) to make predictions, we must use data to estimate the coefficients. Let

$$
(x _ {1}, y _ {1}), (x _ {2}, y _ {2}), \dots , (x _ {n}, y _ {n})
$$

represent n observation pairs, each of which consists of a measurement of X and a measurement of Y. In the Advertising example, this data set consists of the TV advertising budget and product sales in n = 200 different markets. (Recall that the data are displayed in Figure 2.1.) Our goal is to obtain coefficient estimates $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ such that the linear model (3.1) fits the available data well—that is, so that $y_{i} \approx \hat{\beta}_{0} + \hat{\beta}_{1} x_{i}$ for $i = 1, \ldots, n$ . In other words, we want to find an intercept $\hat{\beta}_{0}$ and a slope $\hat{\beta}_{1}$ such that the resulting line is as close as possible to the n = 200 data points. There are a number of ways of measuring closeness. However, by far the most common approach involves minimizing the least squares criterion, and we take that approach in this chapter. Alternative approaches will be considered in Chapter 6.

Let $\hat{y}_{i}=\hat{\beta}_{0}+\hat{\beta}_{1}x_{i}$ be the prediction for Y based on the ith value of X. Then $e_{i}=y_{i}-\hat{y}_{i}$ represents the ith residual—this is the difference between the ith observed response value and the ith response value that is predicted by our linear model. We define the residual sum of squares (RSS) as

$$
\mathrm{RSS} = e _ {1} ^ {2} + e _ {2} ^ {2} + \dots + e _ {n} ^ {2},
$$

least squares

residual

residual sum of squares

or equivalently as

$$
\mathrm{RSS} = \left(y _ {1} - \hat {\beta} _ {0} - \hat {\beta} _ {1} x _ {1}\right) ^ {2} + \left(y _ {2} - \hat {\beta} _ {0} - \hat {\beta} _ {1} x _ {2}\right) ^ {2} + \dots + \left(y _ {n} - \hat {\beta} _ {0} - \hat {\beta} _ {1} x _ {n}\right) ^ {2}. \tag {3.3}
$$

The least squares approach chooses $\hat{\beta}_0$ and $\hat{\beta}_1$ to minimize the RSS. Using some calculus, one can show that the minimizers are

$$
\hat {\beta} _ {1} = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) (y _ {i} - \bar {y})}{\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}}, \tag {3.4}
$$

$$
\hat {\beta} _ {0} = \bar {y} - \hat {\beta} _ {1} \bar {x},
$$

![](images/4e4298a3f09bef98f40e689f3d05d691ec741afb1f7395f2ca67e629f0ef0cbd.jpg)

<details>
<summary>scatter</summary>

| TV  | Sales |
| --- | ----- |
| 0   | 2     |
| 10  | 5     |
| 20  | 7     |
| 30  | 8     |
| 40  | 9     |
| 50  | 10    |
| 60  | 11    |
| 70  | 12    |
| 80  | 13    |
| 90  | 14    |
| 100 | 15    |
| 110 | 16    |
| 120 | 17    |
| 130 | 18    |
| 140 | 19    |
| 150 | 20    |
| 160 | 21    |
| 170 | 22    |
| 180 | 23    |
| 190 | 24    |
| 200 | 25    |
| 210 | 24    |
| 220 | 23    |
| 230 | 22    |
| 240 | 21    |
| 250 | 20    |
| 260 | 19    |
| 270 | 18    |
| 280 | 17    |
| 290 | 16    |
| 300 | 15    |
</details>

FIGURE 3.1. For the Advertising data, the least squares fit for the regression of sales onto TV is shown. The fit is found by minimizing the residual sum of squares. Each grey line segment represents a residual. In this case a linear fit captures the essence of the relationship, although it overestimates the trend in the left of the plot.

where $\bar{y} \equiv \frac{1}{n} \sum_{i=1}^{n} y_i$ and $\bar{x} \equiv \frac{1}{n} \sum_{i=1}^{n} x_i$ are the sample means. In other words, (3.4) defines the least squares coefficient estimates for simple linear regression.

Figure 3.1 displays the simple linear regression fit to the Advertising data, where $\hat{\beta}_0 = 7.03$ and $\hat{\beta}_1 = 0.0475$ . In other words, according to this approximation, an additional \$1,000 spent on TV advertising is associated with selling approximately 47.5 additional units of the product. In Figure 3.2, we have computed RSS for a number of values of $\beta_0$ and $\beta_1$ , using the advertising data with sales as the response and TV as the predictor. In each plot, the red dot represents the pair of least squares estimates ( $\hat{\beta}_0$ , $\hat{\beta}_1$ ) given by (3.4). These values clearly minimize the RSS.

# 3.1.2 Assessing the Accuracy of the Coefficient Estimates

Recall from (2.1) that we assume that the true relationship between $X$ and $Y$ takes the form $Y = f(X) + \epsilon$ for some unknown function $f$ , where $\epsilon$ is a mean-zero random error term. If $f$ is to be approximated by a linear function, then we can write this relationship as

$$
Y = \beta_ {0} + \beta_ {1} X + \epsilon . \tag {3.5}
$$

Here $\beta_{0}$ is the intercept term—that is, the expected value of Y when X = 0, and $\beta_{1}$ is the slope—the average increase in Y associated with a one-unit increase in X. The error term is a catch-all for what we miss with this simple model: the true relationship is probably not linear, there may be other variables that cause variation in Y, and there may be measurement error. We typically assume that the error term is independent of X.

![](images/70e09d9bcf0d6bbdd724a7981d20b904abdcdb77b51a2fe937977578957ea62f.jpg)

<details>
<summary>contour</summary>

| β₀   | β₁   |
| ---- | ---- |
| 7.0  | 0.05 |
| 6.0  | 0.04 |
| 5.0  | 0.03 |
</details>

![](images/fe12a0f61903793cf928cb7e5c0c138a40f676332415a477c3abeaed0ef1da5d.jpg)

<details>
<summary>text_image</summary>

RSS
β₀
β₁
</details>

FIGURE 3.2. Contour and three-dimensional plots of the RSS on the Advertising data, using sales as the response and TV as the predictor. The red dots correspond to the least squares estimates $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ , given by (3.4).

The model given by (3.5) defines the population regression line, which is the best linear approximation to the true relationship between $X$ and $Y$ . The least squares regression coefficient estimates (3.4) characterize the least squares line (3.2). The left-hand panel of Figure 3.3 displays these two lines in a simple simulated example. We created 100 random $Xs$ , and generated 100 corresponding $Ys$ from the model

$$
Y = 2 + 3 X + \epsilon , \tag {3.6}
$$

where $\epsilon$ was generated from a normal distribution with mean zero. The red line in the left-hand panel of Figure 3.3 displays the true relationship, $f(X) = 2 + 3X$ , while the blue line is the least squares estimate based on the observed data. The true relationship is generally not known for real data, but the least squares line can always be computed using the coefficient estimates given in (3.4). In other words, in real applications, we have access to a set of observations from which we can compute the least squares line; however, the population regression line is unobserved. In the right-hand panel of Figure 3.3 we have generated ten different data sets from the model given by (3.6) and plotted the corresponding ten least squares lines. Notice that different data sets generated from the same true model result in slightly different least squares lines, but the unobserved population regression line does not change.

At first glance, the difference between the population regression line and the least squares line may seem subtle and confusing. We only have one data set, and so what does it mean that two different lines describe the relationship between the predictor and the response? Fundamentally, the concept of these two lines is a natural extension of the standard statistical approach of using information from a sample to estimate characteristics of a large population. For example, suppose that we are interested in knowing

population
regression
line
least squares
line

![](images/4bdaf8d37406fd9bd47ecd0689bdba1ce993f13baae1e0d15049e7825a805287.jpg)  
FIGURE 3.3. A simulated data set. Left: The red line represents the true relationship, $f(X) = 2 + 3X$ , which is known as the population regression line. The blue line is the least squares line; it is the least squares estimate for $f(X)$ based on the observed data, shown in black. Right: The population regression line is again shown in red, and the least squares line in dark blue. In light blue, ten least squares lines are shown, each computed on the basis of a separate random set of observations. Each least squares line is different, but on average, the least squares lines are quite close to the population regression line.

the population mean $\mu$ of some random variable Y. Unfortunately, $\mu$ is unknown, but we do have access to n observations from Y, $y_{1},\ldots,y_{n}$ , which we can use to estimate $\mu$ . A reasonable estimate is $\hat{\mu}=\bar{y}$ , where $\bar{y}=\frac{1}{n}\sum_{i=1}^{n}y_{i}$ is the sample mean. The sample mean and the population mean are different, but in general the sample mean will provide a good estimate of the population mean. In the same way, the unknown coefficients $\beta_{0}$ and $\beta_{1}$ in linear regression define the population regression line. We seek to estimate these unknown coefficients using $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ given in (3.4). These coefficient estimates define the least squares line.

The analogy between linear regression and estimation of the mean of a random variable is an apt one based on the concept of bias. If we use the sample mean $\hat{\mu}$ to estimate $\mu$ , this estimate is unbiased, in the sense that on average, we expect $\hat{\mu}$ to equal $\mu$ . What exactly does this mean? It means that on the basis of one particular set of observations $y_{1},\ldots ,y_{n}$ , $\hat{\mu}$ might overestimate $\mu$ , and on the basis of another set of observations, $\hat{\mu}$ might underestimate $\mu$ . But if we could average a huge number of estimates of $\mu$ obtained from a huge number of sets of observations, then this average would exactly equal $\mu$ . Hence, an unbiased estimator does not systematically over- or under-estimate the true parameter. The property of unbiasedness holds for the least squares coefficient estimates given by (3.4) as well: if we estimate $\beta_0$ and $\beta_{1}$ on the basis of a particular data set, then our estimates won't be exactly equal to $\beta_0$ and $\beta_{1}$ . But if we could average the estimates obtained over a huge number of data sets, then the average of these estimates would be spot on! In fact, we can see from the right-hand panel of Figure 3.3 that the average of many least squares lines, each estimated from a separate data set, is pretty close to the true population regression line.

We continue the analogy with the estimation of the population mean $\mu$ of a random variable Y. A natural question is as follows: how accurate is the sample mean $\hat{\mu}$ as an estimate of $\mu$ ? We have established that the average of $\hat{\mu}$ 's over many data sets will be very close to $\mu$ , but that a single estimate $\hat{\mu}$ may be a substantial underestimate or overestimate of $\mu$ . How far off will that single estimate of $\hat{\mu}$ be? In general, we answer this question by computing the standard error of $\hat{\mu}$ , written as SE( $\hat{\mu}$ ). We have the well-known formula

standard error

$$
\mathrm{Var} (\hat {\mu}) = \mathrm{SE} (\hat {\mu}) ^ {2} = \frac {\sigma^ {2}}{n}, \tag {3.7}
$$

where $\sigma$ is the standard deviation of each of the realizations $y_{i}$ of $Y.^{2}$ . Roughly speaking, the standard error tells us the average amount that this estimate $\hat{\mu}$ differs from the actual value of $\mu$ . Equation 3.7 also tells us how this deviation shrinks with n—the more observations we have, the smaller the standard error of $\hat{\mu}$ . In a similar vein, we can wonder how close $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ are to the true values $\beta_{0}$ and $\beta_{1}$ . To compute the standard errors associated with $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ , we use the following formulas:

$$
\mathrm{SE} (\hat {\beta} _ {0}) ^ {2} = \sigma^ {2} \left[ \frac {1}{n} + \frac {\bar {x} ^ {2}}{\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}} \right], \quad \mathrm{SE} (\hat {\beta} _ {1}) ^ {2} = \frac {\sigma^ {2}}{\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}}, \tag {3.8}
$$

where $\sigma^{2} = \operatorname{Var}(\epsilon)$ . For these formulas to be strictly valid, we need to assume that the errors $\epsilon_{i}$ for each observation have common variance $\sigma^{2}$ and are uncorrelated. This is clearly not true in Figure 3.1, but the formula still turns out to be a good approximation. Notice in the formula that $\mathrm{SE}(\hat{\beta}_{1})$ is smaller when the $x_{i}$ are more spread out; intuitively we have more leverage to estimate a slope when this is the case. We also see that $\mathrm{SE}(\hat{\beta}_{0})$ would be the same as $\mathrm{SE}(\hat{\mu})$ if $\bar{x}$ were zero (in which case $\hat{\beta}_{0}$ would be equal to $\bar{y}$ ). In general, $\sigma^{2}$ is not known, but can be estimated from the data. This estimate of $\sigma$ is known as the residual standard error, and is given by the formula $\mathrm{RSE} = \sqrt{\mathrm{RSS}/(n-2)}$ . Strictly speaking, when $\sigma^{2}$ is estimated from the data we should write $\widehat{\mathrm{SE}}(\hat{\beta}_{1})$ to indicate that an estimate has been made, but for simplicity of notation we will drop this extra “hat”.

Standard errors can be used to compute confidence intervals. A 95% confidence interval is defined as a range of values such that with 95% probability, the range will contain the true unknown value of the parameter. The range is defined in terms of lower and upper limits computed from the sample of data. A 95% confidence interval has the following property: if we take repeated samples and construct the confidence interval for each sample, 95% of the intervals will contain the true unknown value of the parameter. For linear regression, the 95% confidence interval for $\beta_{1}$ approximately takes the form

$$
\hat {\beta} _ {1} \pm 2 \cdot \mathrm{SE} (\hat {\beta} _ {1}). \tag {3.9}
$$

residual standard error

confidence interval

That is, there is approximately a $95\%$ chance that the interval

$$
\left[ \hat {\beta} _ {1} - 2 \cdot \mathrm{SE} (\hat {\beta} _ {1}), \hat {\beta} _ {1} + 2 \cdot \mathrm{SE} (\hat {\beta} _ {1}) \right] \tag {3.10}
$$

will contain the true value of $\beta_{1}$ . $^{3}$ Similarly, a confidence interval for $\beta_{0}$ approximately takes the form

$$
\hat {\beta} _ {0} \pm 2 \cdot \mathrm{SE} (\hat {\beta} _ {0}). \tag {3.11}
$$

In the case of the advertising data, the 95% confidence interval for $\beta_{0}$ is [6.130, 7.935] and the 95% confidence interval for $\beta_{1}$ is [0.042, 0.053]. Therefore, we can conclude that in the absence of any advertising, sales will, on average, fall somewhere between 6,130 and 7,935 units. Furthermore, for each 1,000 increase in television advertising, there will be an average increase in sales of between 42 and 53 units.

Standard errors can also be used to perform hypothesis tests on the coefficients. The most common hypothesis test involves testing the null hypothesis of

$$
H _ {0}: \text { There   is   no   relationship   between } X \text { and } Y \tag {3.12}
$$

versus the alternative hypothesis

$$
H _ {a}: \text { There   is   some   relationship   between } X \text { and } Y. \tag {3.13}
$$

Mathematically, this corresponds to testing

$$
H _ {0}: \beta_ {1} = 0
$$

versus

$$
H _ {a}: \beta_ {1} \neq 0,
$$

since if $\beta_{1}=0$ then the model (3.5) reduces to $Y=\beta_{0}+\epsilon$ , and X is not associated with Y. To test the null hypothesis, we need to determine whether $\hat{\beta}_{1}$ , our estimate for $\beta_{1}$ , is sufficiently far from zero that we can be confident that $\beta_{1}$ is non-zero. How far is far enough? This of course depends on the accuracy of $\hat{\beta}_{1}$ —that is, it depends on $\mathrm{SE}(\hat{\beta}_{1})$ . If $\mathrm{SE}(\hat{\beta}_{1})$ is small, then even relatively small values of $\hat{\beta}_{1}$ may provide strong evidence that $\beta_{1}\neq0$ , and hence that there is a relationship between X and Y. In contrast, if $\mathrm{SE}(\hat{\beta}_{1})$ is large, then $\hat{\beta}_{1}$ must be large in absolute value in order for us to reject the null hypothesis. In practice, we compute a t-statistic, given by

$$
t = \frac {\hat {\beta} _ {1} - 0}{\mathrm{SE} (\hat {\beta} _ {1})}, \tag {3.14}
$$

hypothesis test

null
hypothesis

alternative
hypothesis

t-statistic

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>7.0325</td><td>0.4578</td><td>15.36</td><td>&lt; 0.0001</td></tr><tr><td>TV</td><td>0.0475</td><td>0.0027</td><td>17.67</td><td>&lt; 0.0001</td></tr></table>

TABLE 3.1. For the Advertising data, coefficients of the least squares model for the regression of number of units sold on TV advertising budget. An increase of \$1,000 in the TV advertising budget is associated with an increase in sales by around 50 units. (Recall that the sales variable is in thousands of units, and the TV variable is in thousands of dollars.)

which measures the number of standard deviations that $\hat{\beta}_{1}$ is away from 0. If there really is no relationship between X and Y, then we expect that (3.14) will have a t-distribution with n-2 degrees of freedom. The t-distribution has a bell shape and for values of n greater than approximately 30 it is quite similar to the standard normal distribution. Consequently, it is a simple matter to compute the probability of observing any number equal to $|t|$ or larger in absolute value, assuming $\beta_{1}=0$ . We call this probability the p-value. Roughly speaking, we interpret the p-value as follows: a small p-value indicates that it is unlikely to observe such a substantial association between the predictor and the response due to chance, in the absence of any real association between the predictor and the response. Hence, if we see a small p-value, then we can infer that there is an association between the predictor and the response. We reject the null hypothesis—that is, we declare a relationship to exist between X and Y—if the p-value is small enough. Typical p-value cutoffs for rejecting the null hypothesis are 5% or 1%, although this topic will be explored in much greater detail in Chapter 13. When n=30, these correspond to t-statistics (3.14) of around 2 and 2.75, respectively.

Table 3.1 provides details of the least squares model for the regression of number of units sold on TV advertising budget for the Advertising data. Notice that the coefficients for $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ are very large relative to their standard errors, so the t-statistics are also large; the probabilities of seeing such values if $H_{0}$ is true are virtually zero. Hence we can conclude that $\beta_{0} \neq 0$ and $\beta_{1} \neq 0.^{4}$

p-value

# 3.1.3 Assessing the Accuracy of the Model

Once we have rejected the null hypothesis $(3.12)$ in favor of the alternative hypothesis $(3.13)$ , it is natural to want to quantify the extent to which the model fits the data. The quality of a linear regression fit is typically assessed using two related quantities: the residual standard error (RSE) and the $R^{2}$ statistic.

$R^2$

<table><tr><td>Quantity</td><td>Value</td></tr><tr><td>Residual standard error</td><td>3.26</td></tr><tr><td> $R^{2}$ </td><td>0.612</td></tr><tr><td>F-statistic</td><td>312.1</td></tr></table>

TABLE 3.2. For the Advertising data, more information about the least squares model for the regression of number of units sold on TV advertising budget.

Table 3.2 displays the RSE, the $R^{2}$ statistic, and the F-statistic (to be described in Section 3.2.2) for the linear regression of number of units sold on TV advertising budget.

# Residual Standard Error

Recall from the model (3.5) that associated with each observation is an error term $\epsilon$ . Due to the presence of these error terms, even if we knew the true regression line (i.e. even if $\beta_{0}$ and $\beta_{1}$ were known), we would not be able to perfectly predict Y from X. The RSE is an estimate of the standard deviation of $\epsilon$ . Roughly speaking, it is the average amount that the response will deviate from the true regression line. It is computed using the formula

$$
\mathrm{RSE} = \sqrt {\frac {1}{n - 2} \mathrm{RSS}} = \sqrt {\frac {1}{n - 2} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}}. \tag {3.15}
$$

Note that RSS was defined in Section 3.1.1, and is given by the formula

$$
\mathrm{RSS} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}. \tag {3.16}
$$

In the case of the advertising data, we see from the linear regression output in Table 3.2 that the RSE is 3.26. In other words, actual sales in each market deviate from the true regression line by approximately 3,260 units, on average. Another way to think about this is that even if the model were correct and the true values of the unknown coefficients $\beta_0$ and $\beta_{1}$ were known exactly, any prediction of sales on the basis of TV advertising would still be off by about 3,260 units on average. Of course, whether or not 3,260 units is an acceptable prediction error depends on the problem context. In the advertising data set, the mean value of sales over all markets is approximately 14,000 units, and so the percentage error is $3,260 / 14,000 = 23\%$ .

The RSE is considered a measure of the lack of fit of the model (3.5) to the data. If the predictions obtained using the model are very close to the true outcome values—that is, if $\hat{y}_i \approx y_i$ for $i = 1, \dots, n$ —then (3.15) will be small, and we can conclude that the model fits the data very well. On the other hand, if $\hat{y}_i$ is very far from $y_i$ for one or more observations, then the RSE may be quite large, indicating that the model doesn't fit the data well.

# $R^2$ Statistic

The RSE provides an absolute measure of lack of fit of the model (3.5) to the data. But since it is measured in the units of $Y$ , it is not always clear what constitutes a good RSE. The $R^{2}$ statistic provides an alternative measure of fit. It takes the form of a proportion—the proportion of variance explained—and so it always takes on a value between 0 and 1, and is independent of the scale of Y.

To calculate $R^{2}$ , we use the formula

$$
R ^ {2} = \frac {\mathrm{TSS-RSS}}{\mathrm{TSS}} = 1 - \frac {\mathrm{RSS}}{\mathrm{TSS}} \tag {3.17}
$$

where $\mathrm{TSS} = \sum(y_{i} - \bar{y})^{2}$ is the total sum of squares, and RSS is defined in (3.16). TSS measures the total variance in the response Y, and can be thought of as the amount of variability inherent in the response before the regression is performed. In contrast, RSS measures the amount of variability that is left unexplained after performing the regression. Hence, TSS – RSS measures the amount of variability in the response that is explained (or removed) by performing the regression, and $R^{2}$ measures the proportion of variability in Y that can be explained using X. An $R^{2}$ statistic that is close to 1 indicates that a large proportion of the variability in the response is explained by the regression. A number near 0 indicates that the regression does not explain much of the variability in the response; this might occur because the linear model is wrong, or the error variance $\sigma^{2}$ is high, or both. In Table 3.2, the $R^{2}$ was 0.61, and so just under two-thirds of the variability in sales is explained by a linear regression on TV.

The $R^{2}$ statistic (3.17) has an interpretational advantage over the RSE (3.15), since unlike the RSE, it always lies between 0 and 1. However, it can still be challenging to determine what is a good $R^{2}$ value, and in general, this will depend on the application. For instance, in certain problems in physics, we may know that the data truly comes from a linear model with a small residual error. In this case, we would expect to see an $R^{2}$ value that is extremely close to 1, and a substantially smaller $R^{2}$ value might indicate a serious problem with the experiment in which the data were generated. On the other hand, in typical applications in biology, psychology, marketing, and other domains, the linear model (3.5) is at best an extremely rough approximation to the data, and residual errors due to other unmeasured factors are often very large. In this setting, we would expect only a very small proportion of the variance in the response to be explained by the predictor, and an $R^{2}$ value well below 0.1 might be more realistic!

The $R^{2}$ statistic is a measure of the linear relationship between X and Y. Recall that correlation, defined as

total sum of
squares

correlation

$$
\operatorname{Cor} (X, Y) = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{x}}}) (y _ {i} - \overline {{{y}}})}{\sqrt {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{x}}}) ^ {2}} \sqrt {\sum_ {i = 1} ^ {n} (y _ {i} - \overline {{{y}}}) ^ {2}}}, \tag {3.18}
$$

is also a measure of the linear relationship between X and Y. $^{5}$ This suggests that we might be able to use $r = \text{Cor}(X, Y)$ instead of $R^{2}$ in order to assess the fit of the linear model. In fact, it can be shown that in the simple linear regression setting, $R^{2} = r^{2}$ . In other words, the squared correlation and the $R^{2}$ statistic are identical. However, in the next section we will discuss the multiple linear regression problem, in which we use several predictors simultaneously to predict the response. The concept of correlation between the predictors and the response does not extend automatically to this setting, since correlation quantifies the association between a single pair of variables rather than between a larger number of variables. We will see that $R^{2}$ fills this role.

Simple regression of sales on radio 

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>9.312</td><td>0.563</td><td>16.54</td><td>&lt; 0.0001</td></tr><tr><td>radio</td><td>0.203</td><td>0.020</td><td>9.92</td><td>&lt; 0.0001</td></tr></table>

Simple regression of sales on newspaper 

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>12.351</td><td>0.621</td><td>19.88</td><td>&lt; 0.0001</td></tr><tr><td>newspaper</td><td>0.055</td><td>0.017</td><td>3.30</td><td>0.00115</td></tr></table>

TABLE 3.3. More simple linear regression models for the Advertising data. Coefficients of the simple linear regression model for number of units sold on Top: radio advertising budget and Bottom: newspaper advertising budget. A \$1,000 increase in spending on radio advertising is associated with an average increase in sales by around 203 units, while the same increase in spending on newspaper advertising is associated with an average increase in sales by around 55 units. (Note that the sales variable is in thousands of units, and the radio and newspaper variables are in thousands of dollars.)

# 3.2 Multiple Linear Regression

Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the Advertising data, we have examined the relationship between sales and TV advertising. We also have data for the amount of money spent advertising on the radio and in newspapers, and we may want to know whether either of these two media is associated with sales. How can we extend our analysis of the advertising data in order to accommodate these two additional predictors?

One option is to run three separate simple linear regressions, each of which uses a different advertising medium as a predictor. For instance, we can fit a simple linear regression to predict sales on the basis of the amount spent on radio advertisements. Results are shown in Table 3.3 (top table). We find that a \$1,000 increase in spending on radio advertising is associated with an increase in sales of around 203 units. Table 3.3 (bottom table) contains the least squares coefficients for a simple linear regression of sales onto newspaper advertising budget. A \$1,000 increase in newspaper advertising budget is associated with an increase in sales of approximately 55 units.

However, the approach of fitting a separate simple linear regression model for each predictor is not entirely satisfactory. First of all, it is unclear how to make a single prediction of sales given the three advertising media budgets, since each of the budgets is associated with a separate regression equation. Second, each of the three regression equations ignores the other two media in forming estimates for the regression coefficients. We will see shortly that if the media budgets are correlated with each other in the 200 markets in our data set, then this can lead to very misleading estimates of the association between each media budget and sales.

Instead of fitting a separate simple linear regression model for each predictor, a better approach is to extend the simple linear regression model $(3.5)$ so that it can directly accommodate multiple predictors. We can do this by giving each predictor a separate slope coefficient in a single model. In general, suppose that we have p distinct predictors. Then the multiple linear regression model takes the form

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \dots + \beta_ {p} X _ {p} + \epsilon , \tag {3.19}
$$

where $X_{j}$ represents the jth predictor and $\beta_{j}$ quantifies the association between that variable and the response. We interpret $\beta_{j}$ as the average effect on Y of a one unit increase in $X_{j}$ , holding all other predictors fixed. In the advertising example, (3.19) becomes

$$
\text { sales } = \beta_ {0} + \beta_ {1} \times \mathrm{TV} + \beta_ {2} \times \text { radio } + \beta_ {3} \times \text { newspaper } + \epsilon . \tag {3.20}
$$

# 3.2.1 Estimating the Regression Coefficients

As was the case in the simple linear regression setting, the regression coefficients $\beta_{0},\beta_{1},\ldots,\beta_{p}$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_{0},\hat{\beta}_{1},\ldots,\hat{\beta}_{p}$ , we can make predictions using the formula

$$
\hat {y} = \hat {\beta} _ {0} + \hat {\beta} _ {1} x _ {1} + \hat {\beta} _ {2} x _ {2} + \dots + \hat {\beta} _ {p} x _ {p}. \tag {3.21}
$$

The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_{0}, \beta_{1}, \ldots, \beta_{p}$ to minimize the sum of squared residuals

$$
\begin{array}{l} \mathrm{RSS} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2} \\ = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {\beta} _ {0} - \hat {\beta} _ {1} x _ {i 1} - \hat {\beta} _ {2} x _ {i 2} - \dots - \hat {\beta} _ {p} x _ {i p}) ^ {2}. \tag {3.22} \\ \end{array}
$$

The values $\hat{\beta}_{0},\hat{\beta}_{1},\ldots,\hat{\beta}_{p}$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the multiple regression coefficient estimates have somewhat complicated forms that are most easily represented using matrix algebra. For this reason, we do not provide them here. Any statistical software package can be used to compute these coefficient estimates, and later in this chapter we will show how this can be done in R. Figure 3.4 illustrates an example of the least squares fit to a toy data set with $p = 2$ predictors.

![](images/61d6d80ad89f347d9d82294135de5d79cafcd02f9deb2305f9f02983316f4a22.jpg)

<details>
<summary>scatter</summary>

| X1 | Y |
|----|----|
| 0  | 0  |
| 1  | 1  |
| 2  | 2  |
| 3  | 3  |
| 4  | 4  |
| 5  | 5  |
| 6  | 6  |
| 7  | 7  |
| 8  | 8  |
| 9  | 9  |
| 10 | 10 |
| 11 | 11 |
| 12 | 12 |
| 13 | 13 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |
| 17 | 17 |
| 18 | 18 |
| 19 | 19 |
| 20 | 20 |
| 21 | 21 |
| 22 | 22 |
| 23 | 23 |
| 24 | 24 |
| 25 | 25 |
| 26 | 26 |
| 27 | 27 |
| 28 | 28 |
| 29 | 29 |
| 30 | 30 |
| 31 | 31 |
| 32 | 32 |
| 33 | 33 |
| 34 | 34 |
| 35 | 35 |
| 36 | 36 |
| 37 | 37 |
| 38 | 38 |
| 39 | 39 |
| 40 | 40 |
| 41 | 41 |
| 42 | 42 |
| 43 | 43 |
| 44 | 44 |
| 45 | 45 |
| 46 | 46 |
| 47 | 47 |
| 48 | 48 |
| 49 | 49 |
| 50 | 50 |
| 51 | 51 |
| 52 | 52 |
| 53 | 53 |
| 54 | 54 |
| 55 | 55 |
| 56 | 56 |
| 57 | 57 |
| 58 | 58 |
| 59 | 59 |
| 60 | 60 |
| 61 | 61 |
| 62 | 62 |
| 63 | 63 |
| 64 | 64 |
| 65 | 65 |
| 66 | 66 |
| 67 | 67 |
| 68 | 68 |
| 69 | 69 |
| 70 | 70 |
| 71 | 71 |
| 72 | 72 |
| 73 | 73 |
| 74 | 74 |
| 75 | 75 |
| 76 | 76 |
| 77 | 77 |
| 78 | 78 |
| 79 | 79 |
| 80 | 80 |
| 81 | 81 |
| 82 | 82 |
| 83 | 83 |
| 84 | 84 |
| 85 | 85 |
| 86 | 86 |
| 87 | 87 |
| 88 | 88 |
| 89 | 89 |
| 90 | 90 |
| 91 | 91 |
| 92 | 92 |
| 93 | 93 |
| 94 | 94 |
| 95 | 95 |
| 96 | 96 |
| 97 | 97 |
| 98 | 98 |
| 99 | 99 |
| X1 | Y
Y
X2
X3
X4
X5
X6
X7
X8
X9
X10
X11
X12
X13
X14
X15
X16
X17
X18
X19
X20
X21
X22
X23
X24
X25
X26
X27
X28
X29
X30
X31
X32
X33
X34
X35
X36
X37
X38
X39
X40
X41
X42
X43
X44
X45
X46
X47
X48
X49
X50
X51
X52
X53
X54
X55
X56
X57
X58
X59
X60
X61
X62
X63
X64
X65
X66
X67
X68
X69
X70
X71
X72
X73
X74
X75
X76
X77
X78
X79
X80
X81
X82
X83
X84
X85
X86
X87
X88
X89
X90
X91
X92
X93
X94
X95
X96
X97
X98
X99
Z
</details>

FIGURE 3.4. In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each observation (shown in red) and the plane.

Table 3.4 displays the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict product sales using the Advertising data. We interpret these results as follows: for a given amount of TV and newspaper advertising, spending an additional \$1,000 on radio advertising is associated with approximately 189 units of additional sales. Comparing these coefficient estimates to those displayed in Tables 3.1 and 3.3, we notice that the multiple regression coefficient estimates for TV and radio are pretty similar to the simple linear regression coefficient estimates. However, while the newspaper regression coefficient estimate in Table 3.3 was significantly non-zero, the coefficient estimate for newspaper in the multiple regression model is close to zero, and the corresponding p-value is no longer significant, with a value around 0.86. This illustrates that the simple and multiple regression coefficients can be quite different. This difference stems from the fact that in the simple regression case, the slope term represents the average increase in product sales associated with a \$1,000 increase in newspaper advertising, ignoring other predictors such as TV and radio. By contrast, in the multiple regression setting, the coefficient for newspaper represents the average increase in product sales associated with increasing newspaper spending by \$1,000 while holding TV and radio fixed.

Does it make sense for the multiple regression to suggest no relationship between sales and newspaper while the simple linear regression implies the opposite? In fact it does. Consider the correlation matrix for the three predictor variables and response variable, displayed in Table 3.5. Notice that the correlation between radio and newspaper is 0.35. This indicates that markets with high newspaper advertising tend to also have high radio advertising. Now suppose that the multiple regression is correct and newspaper advertising is not associated with sales, but radio advertising is associated with sales. Then in markets where we spend more on radio our sales will tend to be higher, and as our correlation matrix shows, we also tend to spend more on newspaper advertising in those same markets. Hence, in a simple linear regression which only examines sales versus newspaper, we will observe that higher values of newspaper tend to be associated with higher values of sales, even though newspaper advertising is not directly associated with sales. So newspaper advertising is a surrogate for radio advertising; newspaper gets “credit” for the association between radio on sales.

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>2.939</td><td>0.3119</td><td>9.42</td><td>&lt; 0.0001</td></tr><tr><td>TV</td><td>0.046</td><td>0.0014</td><td>32.81</td><td>&lt; 0.0001</td></tr><tr><td>radio</td><td>0.189</td><td>0.0086</td><td>21.89</td><td>&lt; 0.0001</td></tr><tr><td>newspaper</td><td>-0.001</td><td>0.0059</td><td>-0.18</td><td>0.8599</td></tr></table>

TABLE 3.4. For the Advertising data, least squares coefficient estimates of the multiple linear regression of number of units sold on TV, radio, and newspaper advertising budgets.

<table><tr><td></td><td>TV</td><td>radio</td><td>newspaper</td><td>sales</td></tr><tr><td>TV</td><td>1.0000</td><td>0.0548</td><td>0.0567</td><td>0.7822</td></tr><tr><td>radio</td><td></td><td>1.0000</td><td>0.3541</td><td>0.5762</td></tr><tr><td>newspaper</td><td></td><td></td><td>1.0000</td><td>0.2283</td></tr><tr><td>sales</td><td></td><td></td><td></td><td>1.0000</td></tr></table>

TABLE 3.5. Correlation matrix for TV, radio, newspaper, and sales for the Advertising data.

This slightly counterintuitive result is very common in many real life situations. Consider an absurd example to illustrate the point. Running a regression of shark attacks versus ice cream sales for data collected at a given beach community over a period of time would show a positive relationship, similar to that seen between sales and newspaper. Of course no one has (yet) suggested that ice creams should be banned at beaches to reduce shark attacks. In reality, higher temperatures cause more people to visit the beach, which in turn results in more ice cream sales and more shark attacks. A multiple regression of shark attacks onto ice cream sales and temperature reveals that, as intuition implies, ice cream sales is no longer a significant predictor after adjusting for temperature.

# 3.2.2 Some Important Questions

When we perform multiple linear regression, we usually are interested in answering a few important questions.

1. Is at least one of the predictors $X_{1}, X_{2}, \ldots, X_{p}$ useful in predicting the response?   
2. Do all the predictors help to explain Y, or is only a subset of the predictors useful?   
3. How well does the model fit the data?   
4. Given a set of predictor values, what response value should we predict, and how accurate is our prediction?

We now address each of these questions in turn.

One: Is There a Relationship Between the Response and Predictors?

Recall that in the simple linear regression setting, in order to determine whether there is a relationship between the response and the predictor we can simply check whether $\beta_{1}=0$ . In the multiple regression setting with p predictors, we need to ask whether all of the regression coefficients are zero, i.e. whether $\beta_{1}=\beta_{2}=\cdots=\beta_{p}=0$ . As in the simple linear regression setting, we use a hypothesis test to answer this question. We test the null hypothesis,

$$
H _ {0}: \beta_ {1} = \beta_ {2} = \dots = \beta_ {p} = 0
$$

versus the alternative

$$
H _ {a}: \mathrm{atleastone} \beta_ {j} \mathrm{isnon-zero}.
$$

This hypothesis test is performed by computing the F-statistic,

F-statistic

$$
F = \frac {(\mathrm{TSS} - \mathrm{RSS}) / p}{\mathrm{RSS} / (n - p - 1)}, \tag {3.23}
$$

where, as with simple linear regression, $\mathrm{TSS} = \sum(y_{i} - \bar{y})^{2}$ and $\mathrm{RSS} = \sum(y_{i} - \hat{y}_{i})^{2}$ . If the linear model assumptions are correct, one can show that

$$
E \{\mathrm{RSS} / (n - p - 1) \} = \sigma^ {2}
$$

and that, provided $H_{0}$ is true,

$$
E \{(\mathrm{TSS-RSS}) / p \} = \sigma^ {2}.
$$

Hence, when there is no relationship between the response and predictors, one would expect the F-statistic to take on a value close to 1. On the other hand, if $H_{a}$ is true, then $E\{(\mathrm{TSS}-\mathrm{RSS})/p\} > \sigma^{2}$ , so we expect F to be greater than 1.

The F-statistic for the multiple linear regression model obtained by regressing sales onto radio, TV, and newspaper is shown in Table 3.6. In this example the F-statistic is 570. Since this is far larger than 1, it provides compelling evidence against the null hypothesis $H_{0}$ . In other words, the large F-statistic suggests that at least one of the advertising media must be related to sales. However, what if the F-statistic had been closer to 1? How large does the F-statistic need to be before we can reject $H_{0}$ and conclude that there is a relationship? It turns out that the answer depends on the values of n and p. When n is large, an F-statistic that is just a little larger than 1 might still provide evidence against $H_{0}$ . In contrast, a larger F-statistic is needed to reject $H_{0}$ if n is small. When $H_{0}$ is true and the errors $\epsilon_{i}$ have a normal distribution, the F-statistic follows an F-distribution. $^{6}$ For any given value of n and p, any statistical software package can be used to compute the p-value associated with the F-statistic using this distribution. Based on this p-value, we can determine whether or not to reject $H_{0}$ . For the advertising data, the p-value associated with the F-statistic in Table 3.6 is essentially zero, so we have extremely strong evidence that at least one of the media is associated with increased sales.

<table><tr><td>Quantity</td><td>Value</td></tr><tr><td>Residual standard error</td><td>1.69</td></tr><tr><td> $R^{2}$ </td><td>0.897</td></tr><tr><td>F-statistic</td><td>570</td></tr></table>

TABLE 3.6. More information about the least squares model for the regression of number of units sold on TV, newspaper, and radio advertising budgets in the Advertising data. Other information about this model was displayed in Table 3.4.

In (3.23) we are testing $H_{0}$ that all the coefficients are zero. Sometimes we want to test that a particular subset of q of the coefficients are zero. This corresponds to a null hypothesis

$$
H _ {0}: \quad \beta_ {p - q + 1} = \beta_ {p - q + 2} = \dots = \beta_ {p} = 0,
$$

where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables except those last q. Suppose that the residual sum of squares for that model is $RSS_{0}$ . Then the appropriate F-statistic is

$$
F = \frac {(\mathrm{RSS} _ {0} - \mathrm{RSS}) / q}{\mathrm{RSS} / (n - p - 1)}. \tag {3.24}
$$

Notice that in Table 3.4, for each individual predictor a t-statistic and a p-value were reported. These provide information about whether each individual predictor is related to the response, after adjusting for the other predictors. It turns out that each of these is exactly equivalent $^{7}$ to the F-test that omits that single variable from the model, leaving all the others in—i.e. q=1 in (3.24). So it reports the partial effect of adding that variable to the model. For instance, as we discussed earlier, these p-values indicate that TV and radio are related to sales, but that there is no evidence that newspaper is associated with sales, when TV and radio are held fixed.

Given these individual p-values for each variable, why do we need to look at the overall F-statistic? After all, it seems likely that if any one of the p-values for the individual variables is very small, then at least one of the predictors is related to the response. However, this logic is flawed, especially when the number of predictors p is large.

For instance, consider an example in which p = 100 and $H_{0} : \beta_{1} = \beta_{2} = \cdots = \beta_{p} = 0$ is true, so no variable is truly associated with the response. In this situation, about 5% of the p-values associated with each variable (of the type shown in Table 3.4) will be below 0.05 by chance. In other words, we expect to see approximately five small p-values even in the absence of any true association between the predictors and the response. $^{8}$ In fact, it is likely that we will observe at least one p-value below 0.05 by chance! Hence, if we use the individual t-statistics and associated p-values in order to decide whether or not there is any association between the variables and the response, there is a very high chance that we will incorrectly conclude that there is a relationship. However, the F-statistic does not suffer from this problem because it adjusts for the number of predictors. Hence, if $H_{0}$ is true, there is only a 5% chance that the F-statistic will result in a p-value below 0.05, regardless of the number of predictors or the number of observations.

The approach of using an F-statistic to test for any association between the predictors and the response works when p is relatively small, and certainly small compared to n. However, sometimes we have a very large number of variables. If p > n then there are more coefficients $\beta_{j}$ to estimate than observations from which to estimate them. In this case we cannot even fit the multiple linear regression model using least squares, so the F-statistic cannot be used, and neither can most of the other concepts that we have seen so far in this chapter. When p is large, some of the approaches discussed in the next section, such as forward selection, can be used. This high-dimensional setting is discussed in greater detail in Chapter 6.

high-
dimensional

# Two: Deciding on Important Variables

As discussed in the previous section, the first step in a multiple regression analysis is to compute the F-statistic and to examine the associated p-value. If we conclude on the basis of that p-value that at least one of the predictors is related to the response, then it is natural to wonder which are the guilty ones! We could look at the individual p-values as in Table 3.4, but as discussed (and as further explored in Chapter 13), if p is large we are likely to make some false discoveries.

It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors. The task of determining which predictors are associated with the response, in order to fit a single model involving only those predictors, is referred to as variable selection. The variable selection problem is studied extensively in Chapter 6, and so here we will provide only a brief outline of some classical approaches.

Ideally, we would like to perform variable selection by trying out a lot of different models, each containing a different subset of the predictors. For instance, if p = 2, then we can consider four models: (1) a model containing no variables, (2) a model containing $X_{1}$ only, (3) a model containing

variable selection

$X_{2}$ only, and (4) a model containing both $X_{1}$ and $X_{2}$ . We can then select the best model out of all of the models that we have considered. How do we determine which model is best? Various statistics can be used to judge the quality of a model. These include Mallow's $C_{p}$ , Akaike information criterion (AIC), Bayesian information criterion (BIC), and adjusted $R^{2}$ . These are discussed in more detail in Chapter 6. We can also determine which model is best by plotting various model outputs, such as the residuals, in order to search for patterns.

Unfortunately, there are a total of $2^{p}$ models that contain subsets of p variables. This means that even for moderate p, trying out every possible subset of the predictors is infeasible. For instance, we saw that if p = 2, then there are $2^{2} = 4$ models to consider. But if p = 30, then we must consider $2^{30} = 1,073,741,824$ models! This is not practical. Therefore, unless p is very small, we cannot consider all $2^{p}$ models, and instead we need an automated and efficient approach to choose a smaller set of models to consider. There are three classical approaches for this task:

Mallow's $C_p$ Akaike information criterion Bayesian information criterion adjusted $R^2$

\- Forward selection. We begin with the null model—a model that contains an intercept but no predictors. We then fit p simple linear regressions and add to the null model the variable that results in the lowest RSS. We then add to that model the variable that results in the lowest RSS for the new two-variable model. This approach is continued until some stopping rule is satisfied.

forward
selection
null model

\- Backward selection. We start with all variables in the model, and remove the variable with the largest $p$ -value—that is, the variable that is the least statistically significant. The new $(p - 1)$ -variable model is fit, and the variable with the largest $p$ -value is removed. This procedure continues until a stopping rule is reached. For instance, we may stop when all remaining variables have a $p$ -value below some threshold.

backward
selection

\- Mixed selection. This is a combination of forward and backward selection. We start with no variables in the model, and as with forward selection, we add the variable that provides the best fit. We continue to add variables one-by-one. Of course, as we noted with the Advertising example, the p-values for variables can become larger as new predictors are added to the model. Hence, if at any point the p-value for one of the variables in the model rises above a certain threshold, then we remove that variable from the model. We continue to perform these forward and backward steps until all variables in the model have a sufficiently low p-value, and all variables outside the model would have a large p-value if added to the model.

mixed
selection

Backward selection cannot be used if p > n, while forward selection can always be used. Forward selection is a greedy approach, and might include variables early that later become redundant. Mixed selection can remedy this.

# Three: Model Fit

Two of the most common numerical measures of model fit are the RSE and $R^{2}$ , the fraction of variance explained. These quantities are computed and interpreted in the same fashion as for simple linear regression.

Recall that in simple regression, $R^{2}$ is the square of the correlation of the response and the variable. In multiple linear regression, it turns out that it equals $\operatorname{Cor}(Y,\hat{Y})^{2}$ , the square of the correlation between the response and the fitted linear model; in fact one property of the fitted linear model is that it maximizes this correlation among all possible linear models.

An $R^{2}$ value close to 1 indicates that the model explains a large portion of the variance in the response variable. As an example, we saw in Table 3.6 that for the Advertising data, the model that uses all three advertising media to predict sales has an $R^{2}$ of 0.8972. On the other hand, the model that uses only TV and radio to predict sales has an $R^{2}$ value of 0.89719. In other words, there is a small increase in $R^{2}$ if we include newspaper advertising in the model that already contains TV and radio advertising, even though we saw earlier that the p-value for newspaper advertising in Table 3.4 is not significant. It turns out that $R^{2}$ will always increase when more variables are added to the model, even if those variables are only weakly associated with the response. This is due to the fact that adding another variable always results in a decrease in the residual sum of squares on the training data (though not necessarily the testing data). Thus, the $R^{2}$ statistic, which is also computed on the training data, must increase. The fact that adding newspaper advertising to the model containing only TV and radio advertising leads to just a tiny increase in $R^{2}$ provides additional evidence that newspaper can be dropped from the model. Essentially, newspaper provides no real improvement in the model fit to the training samples, and its inclusion will likely lead to poor results on independent test samples due to overfitting.

By contrast, the model containing only TV as a predictor had an $R^{2}$ of 0.61 (Table 3.2). Adding radio to the model leads to a substantial improvement in $R^{2}$ . This implies that a model that uses TV and radio expenditures to predict sales is substantially better than one that uses only TV advertising. We could further quantify this improvement by looking at the p-value for the radio coefficient in a model that contains only TV and radio as predictors.

The model that contains only TV and radio as predictors has an RSE of 1.681, and the model that also contains newspaper as a predictor has an RSE of 1.686 (Table 3.6). In contrast, the model that contains only TV has an RSE of 3.26 (Table 3.2). This corroborates our previous conclusion that a model that uses TV and radio expenditures to predict sales is much more accurate (on the training data) than one that only uses TV spending. Furthermore, given that TV and radio expenditures are used as predictors, there is no point in also using newspaper spending as a predictor in the model. The observant reader may wonder how RSE can increase when newspaper is added to the model given that RSS must decrease. In general RSE is defined as

$$
\mathrm{RSE} = \sqrt {\frac {1}{n - p - 1} \mathrm{RSS}}, \tag {3.25}
$$

![](images/b9ebb9165a2694099727adf620d34fb22c4fe1cfe91e1a6704b46207be7f9f93.jpg)

<details>
<summary>scatter</summary>

| Radio | Sales |
|-------|-------|
| 0     | 0     |
| 10    | 5     |
| 20    | 10    |
| 30    | 15    |
| 40    | 20    |
| 50    | 25    |
| 60    | 30    |
| 70    | 35    |
| 80    | 40    |
| 90    | 45    |
| 100   | 50    |
| 110   | 55    |
| 120   | 60    |
| 130   | 65    |
| 140   | 70    |
| 150   | 75    |
| 160   | 80    |
| 170   | 85    |
| 180   | 90    |
| 190   | 95    |
| 200   | 100   |
</details>

FIGURE 3.5. For the Advertising data, a linear regression fit to sales using TV and radio as predictors. From the pattern of the residuals, we can see that there is a pronounced non-linear relationship in the data. The positive residuals (those visible above the surface), tend to lie along the 45-degree line, where TV and Radio budgets are split evenly. The negative residuals (most not visible), tend to lie away from this line, where budgets are more lopsided.

which simplifies to $(3.15)$ for a simple linear regression. Thus, models with more variables can have higher RSE if the decrease in RSS is small relative to the increase in p.

In addition to looking at the RSE and $R^{2}$ statistics just discussed, it can be useful to plot the data. Graphical summaries can reveal problems with a model that are not visible from numerical statistics. For example, Figure 3.5 displays a three-dimensional plot of TV and radio versus sales. We see that some observations lie above and some observations lie below the least squares regression plane. In particular, the linear model seems to overestimate sales for instances in which most of the advertising money was spent exclusively on either TV or radio. It underestimates sales for instances where the budget was split between the two media. This pronounced non-linear pattern suggests a synergy or interaction effect between the advertising media, whereby combining the media together results in a bigger boost to sales than using any single medium. In Section 3.3.2, we will discuss extending the linear model to accommodate such synergistic effects through the use of interaction terms.

interaction

# Four: Predictions

Once we have fit the multiple regression model, it is straightforward to apply $(3.21)$ in order to predict the response Y on the basis of a set of values for the predictors $X_{1}, X_{2}, \ldots, X_{p}$ . However, there are three sorts of uncertainty associated with this prediction.

1. The coefficient estimates $\hat{\beta}_0, \hat{\beta}_1, \ldots, \hat{\beta}_p$ are estimates for $\beta_0, \beta_1, \ldots, \beta_p$ . That is, the least squares plane

$$
\hat {Y} = \hat {\beta} _ {0} + \hat {\beta} _ {1} X _ {1} + \dots + \hat {\beta} _ {p} X _ {p}
$$

is only an estimate for the true population regression plane

$$
f (X) = \beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}.
$$

The inaccuracy in the coefficient estimates is related to the reducible error from Chapter 2. We can compute a confidence interval in order to determine how close $\hat{Y}$ will be to $f(X)$ .

2. Of course, in practice assuming a linear model for $f(X)$ is almost always an approximation of reality, so there is an additional source of potentially reducible error which we call model bias. So when we use a linear model, we are in fact estimating the best linear approximation to the true surface. However, here we will ignore this discrepancy, and operate as if the linear model were correct.   
3. Even if we knew $f(X)$ —that is, even if we knew the true values for $\beta_{0},\beta_{1},\ldots,\beta_{p}$ —the response value cannot be predicted perfectly because of the random error $\epsilon$ in the model (3.20). In Chapter 2, we referred to this as the irreducible error. How much will Y vary from $\hat{Y}$ ? We use prediction intervals to answer this question. Prediction intervals are always wider than confidence intervals, because they incorporate both the error in the estimate for $f(X)$ (the reducible error) and the uncertainty as to how much an individual point will differ from the population regression plane (the irreducible error).

We use a confidence interval to quantify the uncertainty surrounding the average sales over a large number of cities. For example, given that 100,000 is spent on TV advertising and 20,000 is spent on radio advertising in each city, the 95% confidence interval is [10,985, 11,528]. We interpret this to mean that 95% of intervals of this form will contain the true value of $f(X)$ .⁹ On the other hand, a prediction interval can be used to quantify the uncertainty surrounding sales for a particular city. Given that 100,000 is spent on TV advertising and 20,000 is spent on radio advertising in that city the 95% prediction interval is [7,930, 14,580]. We interpret this to mean that 95% of intervals of this form will contain the true value of Y for this city. Note that both intervals are centered at 11,256, but that the prediction interval is substantially wider than the confidence interval, reflecting the increased uncertainty about sales for a given city in comparison to the average sales over many locations.

confidence interval

prediction interval

# 3.3 Other Considerations in the Regression Model

# 3.3.1 Qualitative Predictors

In our discussion so far, we have assumed that all variables in our linear regression model are quantitative. But in practice, this is not necessarily the case; often some predictors are qualitative.

For example, the Credit data set displayed in Figure 3.6 records variables for a number of credit card holders. The response is balance (average credit card debt for each individual) and there are several quantitative predictors: age, cards (number of credit cards), education (years of education), income (in thousands of dollars), limit (credit limit), and rating (credit rating). Each panel of Figure 3.6 is a scatterplot for a pair of variables whose identities are given by the corresponding row and column labels. For example, the scatterplot directly to the right of the word “Balance” depicts balance versus age, while the plot directly to the right of “Age” corresponds to age versus cards. In addition to these quantitative variables, we also have four qualitative variables: own (house ownership), student (student status), status (marital status), and region (East, West or South).

# Predictors with Only Two Levels

Suppose that we wish to investigate differences in credit card balance between those who own a house and those who don't, ignoring the other variables for the moment. If a qualitative predictor (also known as a factor) only has two levels, or possible values, then incorporating it into a regression model is very simple. We simply create an indicator or dummy variable that takes on two possible numerical values. $^{10}$ For example, based on the own variable, we can create a new variable that takes the form

factor
level
dummy
variable

$$
x _ {i} = \left\{ \begin{array}{l l} 1 & \text {   if   } i \text {th   person   owns   a   house   } \\ 0 & \text {   if   } i \text {th   person   does   not   own   a   house,   } \end{array} \right. \tag {3.26}
$$

and use this variable as a predictor in the regression equation. This results in the model

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \epsilon_ {i} = \left\{ \begin{array}{l l} \beta_ {0} + \beta_ {1} + \epsilon_ {i} & \text { if   } i \text { th   person   owns   a   house } \\ \beta_ {0} + \epsilon_ {i} & \text { if   } i \text { th   person   does   not. } \end{array} \right. \tag {3.27}
$$

Now $\beta_{0}$ can be interpreted as the average credit card balance among those who do not own, $\beta_{0} + \beta_{1}$ as the average credit card balance among those who do own their house, and $\beta_{1}$ as the average difference in credit card balance between owners and non-owners.

Table 3.7 displays the coefficient estimates and other information associated with the model (3.27). The average credit card debt for non-owners is estimated to be \$509.80, whereas owners are estimated to carry \$19.73 in additional debt for a total of \$509.80 + \$19.73 = \$529.53. However, we notice that the p-value for the dummy variable is very high. This indicates that there is no statistical evidence of a difference in average credit card balance based on house ownership.

![](images/1335377c0bae432551d6c03c6f01d0e6220c997c7b62a804ed55062bebbe55a3.jpg)

<details>
<summary>scatter</summary>

| Variable   | Value |
|------------|-------|
| Balance    | 20    |
| Balance    | 40    |
| Balance    | 60    |
| Balance    | 80    |
| Balance    | 100   |
| Balance    | 120   |
| Balance    | 140   |
| Balance    | 160   |
| Balance    | 180   |
| Balance    | 200   |
| Balance    | 220   |
| Balance    | 240   |
| Balance    | 260   |
| Balance    | 280   |
| Balance    | 300   |
| Balance    | 320   |
| Balance    | 340   |
| Balance    | 360   |
| Balance    | 380   |
| Balance    | 400   |
| Balance    | 420   |
| Balance    | 440   |
| Balance    | 460   |
| Balance    | 480   |
| Balance    | 500   |
| Balance    | 520   |
| Balance    | 540   |
| Balance    | 560   |
| Balance    | 580   |
| Balance    | 600   |
| Balance    | 620   |
| Balance    | 640   |
| Balance    | 660   |
| Balance    | 680   |
| Balance    | 700   |
| Balance    | 720   |
| Balance    | 740   |
| Balance    | 760   |
| Balance    | 780   |
| Balance    | 800   |
| Balance    | 820   |
| Balance    | 840   |
| Balance    | 860   |
| Balance    | 880   |
| Balance    | 900   |
| Balance    | 920   |
| Balance    | 940   |
| Balance    | 960   |
| Balance    | 980   |
| Balance    | 1000  |
| Age        | 20    |
| Age        | 40    |
| Age        | 60    |
| Age        | 80    |
| Age        | 100   |
| Age        | 120   |
| Age        | 140   |
| Age        | 160   |
| Age        | 180   |
| Age        | 200   |
| Age        | 220   |
| Age        | 240   |
| Age        | 260   |
| Age        | 280   |
| Age        | 300   |
| Age        | 320   |
| Age        | 340   |
| Age        | 360   |
| Age        | 380   |
| Age        | 400   |
| Age        | 420   |
| Age        | 440   |
| Age        | 460   |
| Age        | 480   |
| Age        | 500   |
| Age        | 520   |
| Age        | 540   |
| Age        | 560   |
| Age        | 580   |
| Age        | 600   |
| Age        | 620   |
| Age        | 640   |
| Age        | 660   |
| Age        | 680   |
| Age        | 700   |
| Age        | 720   |
| Age        | 740   |
| Age        | 760   |
| Age        | 780   |
| Age        | 800   |
| Age        | 820   |
| Age        | 840   |
| Age        | 860   |
| Age        | 880   |
| Age        | 900   |
| Age        | 920   |
| Age        | 940   |
| Age        | 960   |
| Age        | 980   |
| Age        | 1000  |
| Cards      | 20    |
| Cards      | 40    |
| Cards      | 60    |
| Cards      | 80    |
| Cards      | 100   |
| Cards      | 120   |
| Cards      | 140   |
| Cards      | 160   |
| Cards      | 180   |
| Cards      | 200   |
| Cards      | 220   |
| Cards      | 240   |
| Cards      | 260   |
| Cards      | 280   |
| Cards      | 300   |
| Cards      | 320   |
| Cards      | 340   |
| Cards      | 360   |
| Cards      | 380   |
| Cards      | 400   |
| Cards      | 420   |
| Cards      | 440   |
| Cards      | 460   |
| Cards      | 480   |
| Cards      | 500   |
| Cards      | 520   |
| Cards      | 540   |
| Cards      | 560   |
| Cards      | 580   |
| Cards      | 600   |
| Cards      | 620   |
| Cards      | 640   |
| Cards      | 660   |
| Cards      | 680   |
| Cards      | 700   |
| Cards      | 720   |
| Cards      | 740   |
| Cards      | 760   |
| Cards      | 780   |
| Cards      | 800   |
| Cards      | 820   |
| Cards      | 840   |
| Cards      | 860   |
| Cards      | 880   |
| Cards      | 900   |
| Cards      | 920   |
| Cards      | 940   |
| Cards      | 960   |
| Cards      | 980   |
| Cards      | 1000  |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
| Education  | -     |
|
| Education  | -     |
|
| Education  | -     (with label "Income")<br>[Value] position in the image on the right side of the chart] 
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|\( \text{Income} \) vs. \( \text{Limit} \) vs. \( \text{Rating} \) 
\(\text{Limit} \) vs.\(\text{Rating} \)<br>[Value] position in the image
</details>

FIGURE 3.6. The Credit data set contains information about balance, age, cards, education, income, limit, and rating for a number of potential customers.

The decision to code owners as 1 and non-owners as 0 in (3.27) is arbitrary, and has no effect on the regression fit, but does alter the interpretation of the coefficients. If we had coded non-owners as 1 and owners as 0, then the estimates for $\beta_{0}$ and $\beta_{1}$ would have been 529.53 and -19.73, respectively, leading once again to a prediction of credit card debt of \$529.53 - \$19.73 = \$509.80 for non-owners and a prediction of \$529.53 for owners. Alternatively, instead of a 0/1 coding scheme, we could create a dummy variable

$$
x _ {i} = \left\{ \begin{array}{l l} 1 & \quad \text { if   } i \text { th   person   owns   a   house } \\ - 1 & \quad \text { if   } i \text { th   person   does   not   own   a   house } \end{array} \right.
$$

and use this variable in the regression equation. This results in the model

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \epsilon_ {i} = \left\{ \begin{array}{l l} \beta_ {0} + \beta_ {1} + \epsilon_ {i} & \text {if i \text {th person owns a house}} \\ \beta_ {0} - \beta_ {1} + \epsilon_ {i} & \text {if i \text {th person does not own a house.}} \end{array} \right.
$$

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>509.80</td><td>33.13</td><td>15.389</td><td>&lt; 0.0001</td></tr><tr><td>own[Yes]</td><td>19.73</td><td>46.05</td><td>0.429</td><td>0.6690</td></tr></table>

TABLE 3.7. Least squares coefficient estimates associated with the regression of balance onto own in the Credit data set. The linear model is given in (3.27). That is, ownership is encoded as a dummy variable, as in (3.26).

Now $\beta_{0}$ can be interpreted as the overall average credit card balance (ignoring the house ownership effect), and $\beta_{1}$ is the amount by which house owners and non-owners have credit card balances that are above and below the average, respectively. $^{11}$ In this example, the estimate for $\beta_{0}$ is 519.665, halfway between the non-owner and owner averages of 509.80 and 529.53. The estimate for $\beta_{1}$ is 9.865, which is half of 19.73, the average difference between owners and non-owners. It is important to note that the final predictions for the credit balances of owners and non-owners will be identical regardless of the coding scheme used. The only difference is in the way that the coefficients are interpreted.

# Qualitative Predictors with More than Two Levels

When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values. In this situation, we can create additional dummy variables. For example, for the region variable we create two dummy variables. The first could be

$$
x _ {i 1} = \left\{ \begin{array}{l l} 1 & \text {   if   } i \text {th   person   is   from   the   South   } \\ 0 & \text {   if   } i \text {th   person   is   not   from   the   South,   } \end{array} \right. \tag {3.28}
$$

and the second could be

$$
x _ {i 2} = \left\{ \begin{array}{l l} 1 & \text {   if   } i \text {th   person   is   from   the   West   } \\ 0 & \text {   if   } i \text {th   person   is   not   from   the   West.   } \end{array} \right. \tag {3.29}
$$

Then both of these variables can be used in the regression equation, in order to obtain the model

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i 1} + \beta_ {2} x _ {i 2} + \epsilon_ {i} = \left\{ \begin{array}{l l} \beta_ {0} + \beta_ {1} + \epsilon_ {i} & \text { if   } i \text {th   person   is   from   the   South } \\ \beta_ {0} + \beta_ {2} + \epsilon_ {i} & \text { if   } i \text {th   person   is   from   the   West } \\ \beta_ {0} + \epsilon_ {i} & \text { if   } i \text {th   person   is   from   the   East. } \end{array} \right. \tag {3.30}
$$

Now $\beta_{0}$ can be interpreted as the average credit card balance for individuals from the East, $\beta_{1}$ can be interpreted as the difference in the average balance between people from the South versus the East, and $\beta_{2}$ can be interpreted as the difference in the average balance between those from the West versus the East. There will always be one fewer dummy variable than the number of levels. The level with no dummy variable—East in this example—is known as the baseline.

baseline

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>531.00</td><td>46.32</td><td>11.464</td><td>&lt; 0.0001</td></tr><tr><td>region [South]</td><td>-12.50</td><td>56.68</td><td>-0.221</td><td>0.8260</td></tr><tr><td>region [West]</td><td>-18.69</td><td>65.02</td><td>-0.287</td><td>0.7740</td></tr></table>

TABLE 3.8. Least squares coefficient estimates associated with the regression of balance onto region in the Credit data set. The linear model is given in (3.30). That is, region is encoded via two dummy variables (3.28) and (3.29).

From Table 3.8, we see that the estimated balance for the baseline, East, is \$531.00. It is estimated that those in the South will have \$18.69 less debt than those in the East, and that those in the West will have \$12.50 less debt than those in the East. However, the $p$ -values associated with the coefficient estimates for the two dummy variables are very large, suggesting no statistical evidence of a real difference in average credit card balance between South and East or between West and East. $^{12}$ Once again, the level selected as the baseline category is arbitrary, and the final predictions for each group will be the same regardless of this choice. However, the coefficients and their $p$ -values do depend on the choice of dummy variable coding. Rather than rely on the individual coefficients, we can use an $F$ -test to test $H_0: \beta_1 = \beta_2 = 0$ ; this does not depend on the coding. This $F$ -test has a $p$ -value of 0.96, indicating that we cannot reject the null hypothesis that there is no relationship between balance and region.

Using this dummy variable approach presents no difficulties when incorporating both quantitative and qualitative predictors. For example, to regress balance on both a quantitative variable such as income and a qualitative variable such as student, we must simply create a dummy variable for student and then fit a multiple regression model using income and the dummy variable as predictors for credit card balance.

There are many different ways of coding qualitative variables besides the dummy variable approach taken here. All of these approaches lead to equivalent model fits, but the coefficients are different and have different interpretations, and are designed to measure particular contrasts. This topic is beyond the scope of the book.

contrast

# 3.3.2 Extensions of the Linear Model

The standard linear regression model (3.19) provides interpretable results and works quite well on many real-world problems. However, it makes several highly restrictive assumptions that are often violated in practice. Two of the most important assumptions state that the relationship between the predictors and response are additive and linear. The additivity assumption means that the association between a predictor $X_{j}$ and the response Y does not depend on the values of the other predictors. The linearity assumption states that the change in the response Y associated with a one-unit change in $X_{j}$ is constant, regardless of the value of $X_{j}$ . In later chapters of this book, we examine a number of sophisticated methods that relax these two

additive
linear

assumptions. Here, we briefly examine some common classical approaches for extending the linear model.

# Removing the Additive Assumption

In our previous analysis of the Advertising data, we concluded that both TV and radio seem to be associated with sales. The linear models that formed the basis for this conclusion assumed that the effect on sales of increasing one advertising medium is independent of the amount spent on the other media. For example, the linear model $(3.20)$ states that the average increase in sales associated with a one-unit increase in TV is always $\beta_{1}$ , regardless of the amount spent on radio.

However, this simple model may be incorrect. Suppose that spending money on radio advertising actually increases the effectiveness of TV advertising, so that the slope term for TV should increase as radio increases. In this situation, given a fixed budget of \$100,000, spending half on radio and half on TV may increase sales more than allocating the entire amount to either TV or to radio. In marketing, this is known as a synergy effect, and in statistics it is referred to as an interaction effect. Figure 3.5 suggests that such an effect may be present in the advertising data. Notice that when levels of either TV or radio are low, then the true sales are lower than predicted by the linear model. But when advertising is split between the two media, then the model tends to underestimate sales.

Consider the standard linear regression model with two variables,

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \epsilon .
$$

According to this model, a one-unit increase in $X_{1}$ is associated with an average increase in Y of $\beta_{1}$ units. Notice that the presence of $X_{2}$ does not alter this statement—that is, regardless of the value of $X_{2}$ , a one-unit increase in $X_{1}$ is associated with a $\beta_{1}$ -unit increase in Y. One way of extending this model is to include a third predictor, called an interaction term, which is constructed by computing the product of $X_{1}$ and $X_{2}$ . This results in the model

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \beta_ {3} X _ {1} X _ {2} + \epsilon . \tag {3.31}
$$

How does inclusion of this interaction term relax the additive assumption? Notice that (3.31) can be rewritten as

$$
Y = \beta_ {0} + \left(\beta_ {1} + \beta_ {3} X _ {2}\right) X _ {1} + \beta_ {2} X _ {2} + \epsilon \tag {3.32}
$$

$$
= \beta_ {0} + \tilde {\beta} _ {1} X _ {1} + \beta_ {2} X _ {2} + \epsilon
$$

where $\tilde{\beta}_{1} = \beta_{1} + \beta_{3}X_{2}$ . Since $\tilde{\beta}_{1}$ is now a function of $X_{2}$ , the association between $X_{1}$ and Y is no longer constant: a change in the value of $X_{2}$ will change the association between $X_{1}$ and Y. A similar argument shows that a change in the value of $X_{1}$ changes the association between $X_{2}$ and Y.

For example, suppose that we are interested in studying the productivity of a factory. We wish to predict the number of units produced on the basis of the number of production lines and the total number of workers. It seems likely that the effect of increasing the number of production lines will depend on the number of workers, since if no workers are available to operate the lines, then increasing the number of lines will not increase production. This suggests that it would be appropriate to include an interaction term between lines and workers in a linear model to predict units. Suppose that when we fit the model, we obtain

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>6.7502</td><td>0.248</td><td>27.23</td><td>&lt; 0.0001</td></tr><tr><td>TV</td><td>0.0191</td><td>0.002</td><td>12.70</td><td>&lt; 0.0001</td></tr><tr><td>radio</td><td>0.0289</td><td>0.009</td><td>3.24</td><td>0.0014</td></tr><tr><td>TV×radio</td><td>0.0011</td><td>0.000</td><td>20.73</td><td>&lt; 0.0001</td></tr></table>

TABLE 3.9. For the Advertising data, least squares coefficient estimates associated with the regression of sales onto TV and radio, with an interaction term, as in (3.33).

$$
\begin{array}{l} \text { units } \approx 1. 2 + 3. 4 \times \text { lines } + 0. 2 2 \times \text { workers } + 1. 4 \times (\text { lines } \times \text { workers }) \\ = 1. 2 + (3. 4 + 1. 4 \times \text { workers }) \times \text { lines } + 0. 2 2 \times \text { workers }. \\ \end{array}
$$

In other words, adding an additional line will increase the number of units produced by $3.4 + 1.4 \times workers$ . Hence the more workers we have, the stronger will be the effect of lines.

We now return to the Advertising example. A linear model that uses radio, TV, and an interaction between the two to predict sales takes the form

$$
\begin{array}{l} \text { sales } = \beta_ {0} + \beta_ {1} \times \mathrm{TV} + \beta_ {2} \times \text { radio } + \beta_ {3} \times (\text { radio } \times \mathrm{TV}) + \epsilon \\ = \beta_ {0} + \left(\beta_ {1} + \beta_ {3} \times \text { radio }\right) \times \mathrm{TV} + \beta_ {2} \times \text { radio } + \epsilon . \tag {3.33} \\ \end{array}
$$

We can interpret $\beta_{3}$ as the increase in the effectiveness of TV advertising associated with a one-unit increase in radio advertising (or vice-versa). The coefficients that result from fitting the model (3.33) are given in Table 3.9.

The results in Table 3.9 strongly suggest that the model that includes the interaction term is superior to the model that contains only main effects. The p-value for the interaction term, TV×radio, is extremely low, indicating that there is strong evidence for $H_{a}:\beta_{3}\neq0$ . In other words, it is clear that the true relationship is not additive. The $R^{2}$ for the model (3.33) is 96.8%, compared to only 89.7% for the model that predicts sales using TV and radio without an interaction term. This means that $(96.8-89.7)/(100-89.7)=69\%$ of the variability in sales that remains after fitting the additive model has been explained by the interaction term. The coefficient estimates in Table 3.9 suggest that an increase in TV advertising of 1,000 is associated with increased sales of $(\hat{\beta}_{1}+\hat{\beta}_{3}\times\text{radio})\times1,000=19+1.1\times\text{radio}$ units. And an increase in radio advertising of 1,000 will be associated with an increase in sales of $(\hat{\beta}_{2}+\hat{\beta}_{3}\times\text{TV})\times1,000=29+1.1\times\text{TV}$ units.

In this example, the p-values associated with TV, radio, and the interaction term all are statistically significant (Table 3.9), and so it is obvious that all three variables should be included in the model. However, it is sometimes the case that an interaction term has a very small p-value, but the associated main effects (in this case, TV and radio) do not. The hierarchical principle states that if we include an interaction in a model, we should also include the main effects, even if the p-values associated with their coefficients are not significant. In other words, if the interaction between $X_{1}$ and $X_{2}$ seems important, then we should include both $X_{1}$ and $X_{2}$ in the model even if their coefficient estimates have large p-values. The rationale for this principle is that if $X_{1} \times X_{2}$ is related to the response, then whether or not the coefficients of $X_{1}$ or $X_{2}$ are exactly zero is of little interest. Also $X_{1} \times X_{2}$ is typically correlated with $X_{1}$ and $X_{2}$ , and so leaving them out tends to alter the meaning of the interaction.

In the previous example, we considered an interaction between TV and radio, both of which are quantitative variables. However, the concept of interactions applies just as well to qualitative variables, or to a combination of quantitative and qualitative variables. In fact, an interaction between a qualitative variable and a quantitative variable has a particularly nice interpretation. Consider the Credit data set from Section 3.3.1, and suppose that we wish to predict balance using the income (quantitative) and student (qualitative) variables. In the absence of an interaction term, the model takes the form

$$
\begin{array}{l} \text {balance} _ {i} \approx \beta_ {0} + \beta_ {1} \times \text {income} _ {i} + \left\{ \begin{array}{l l} \beta_ {2} & \text {if ith person is a student} \\ 0 & \text {if ith person is not a student} \end{array} \right. \\ = \beta_ {1} \times \text { income } _ {i} + \left\{ \begin{array}{l l} \beta_ {0} + \beta_ {2} & \text { if   } i \text { th   person   is   a   student } \\ \beta_ {0} & \text { if   } i \text { th   person   is   not   a   student. } \end{array} \right. \tag {3.34} \\ \end{array}
$$

Notice that this amounts to fitting two parallel lines to the data, one for students and one for non-students. The lines for students and non-students have different intercepts, $\beta_{0} + \beta_{2}$ versus $\beta_{0}$ , but the same slope, $\beta_{1}$ . This is illustrated in the left-hand panel of Figure 3.7. The fact that the lines are parallel means that the average effect on balance of a one-unit increase in income does not depend on whether or not the individual is a student. This represents a potentially serious limitation of the model, since in fact a change in income may have a very different effect on the credit card balance of a student versus a non-student.

This limitation can be addressed by adding an interaction variable, created by multiplying income with the dummy variable for student. Our model now becomes

$$
\begin{array}{l} \text {balance} _ {i} \approx \beta_ {0} + \beta_ {1} \times \text {income} _ {i} + \left\{ \begin{array}{l l} \beta_ {2} + \beta_ {3} \times \text {income} _ {i} & \text {if student} \\ 0 & \text {if not student} \end{array} \right. \\ = \left\{ \begin{array}{l l} \left(\beta_ {0} + \beta_ {2}\right) + \left(\beta_ {1} + \beta_ {3}\right) \times \text {income} _ {i} & \text {if student} \\ \beta_ {0} + \beta_ {1} \times \text {income} _ {i} & \text {if not student.} \end{array} \right. \tag {3.35} \\ \end{array}
$$

Once again, we have two different regression lines for the students and the non-students. But now those regression lines have different intercepts, $\beta_{0}+\beta_{2}$ versus $\beta_{0}$ , as well as different slopes, $\beta_{1}+\beta_{3}$ versus $\beta_{1}$ . This allows for the possibility that changes in income may affect the credit card balances of students and non-students differently. The right-hand panel of Figure 3.7 shows the estimated relationships between income and balance for students and non-students in the model $(3.35)$ . We note that the slope for students is lower than the slope for non-students. This suggests that increases in income are associated with smaller increases in credit card balance among students as compared to non-students.

![](images/f4a8c7defebd8120b06acffa61c674d00803159f848f2ae705e809a0ee118802.jpg)

<details>
<summary>line</summary>

| Income | Balance (Red Line) | Balance (Black Line) |
| ------ | ------------------ | -------------------- |
| 0      | 600                | 200                  |
| 150    | 1400               | 1100                 |
</details>

![](images/6ef11d9e49aed9c03f9632f541d97fd283edde3a36d2046b20365575ab5067cf.jpg)

<details>
<summary>line</summary>

| Income | student | non-student |
| ------ | ------- | ----------- |
| 0      | 700     | 200         |
| 150    | 1350    | 1200        |
</details>

FIGURE 3.7. For the Credit data, the least squares lines are shown for prediction of balance from income for students and non-students. Left: The model (3.34) was fit. There is no interaction between income and student. Right: The model (3.35) was fit. There is an interaction term between income and student.

# Non-linear Relationships

As discussed previously, the linear regression model $(3.19)$ assumes a linear relationship between the response and predictors. But in some cases, the true relationship between the response and the predictors may be nonlinear. Here we present a very simple way to directly extend the linear model to accommodate non-linear relationships, using polynomial regression. In later chapters, we will present more complex approaches for performing non-linear fits in more general settings.

Consider Figure 3.8, in which the mpg (gas mileage in miles per gallon) versus horsepower is shown for a number of cars in the Auto data set. The orange line represents the linear regression fit. There is a pronounced relationship between mpg and horsepower, but it seems clear that this relationship is in fact non-linear: the data suggest a curved relationship. A simple approach for incorporating non-linear associations in a linear model is to include transformed versions of the predictors. For example, the points in Figure 3.8 seem to have a quadratic shape, suggesting that a model of the form

$$
\mathrm{mpg} = \beta_ {0} + \beta_ {1} \times \text { horsepower } + \beta_ {2} \times \text { horsepower } ^ {2} + \epsilon \tag {3.36}
$$

may provide a better fit. Equation 3.36 involves predicting mpg using a non-linear function of horsepower. But it is still a linear model! That is, (3.36) is simply a multiple linear regression model with $X_{1} = \text{horsepower}$ and $X_{2} = \text{horsepower}^{2}$ . So we can use standard linear regression software to estimate $\beta_{0}, \beta_{1}$ , and $\beta_{2}$ in order to produce a non-linear fit. The blue curve in Figure 3.8 shows the resulting quadratic fit to the data. The quadratic fit appears to be substantially better than the fit obtained when just the linear term is included. The $R^2$ of the quadratic fit is 0.688, compared to 0.606 for the linear fit, and the $p$ -value in Table 3.10 for the quadratic term is highly significant.

![](images/ed77e355ed46ab6948fcc512a0c7edde88baed8f0d55ae36d64d273b03c7167e.jpg)

<details>
<summary>scatter</summary>

| Horsepower | Miles per gallon | Series     |
| ---------- | ---------------- | ---------- |
| 50         | 40               | Linear     |
| 50         | 35               | Degree 2   |
| 50         | 35               | Degree 5   |
| 100        | 25               | Linear     |
| 100        | 20               | Degree 2   |
| 100        | 20               | Degree 5   |
| 150        | 15               | Linear     |
| 150        | 15               | Degree 2   |
| 150        | 15               | Degree 5   |
| 200        | 10               | Linear     |
| 200        | 15               | Degree 2   |
| 200        | 10               | Degree 5   |
| 220        | 5                | Linear     |
| 220        | 15               | Degree 2   |
| 220        | 20               | Degree 5   |
</details>

FIGURE 3.8. The Auto data set. For a number of cars, mpg and horsepower are shown. The linear regression fit is shown in orange. The linear regression fit for a model that includes horsepower $^{2}$ is shown as a blue curve. The linear regression fit for a model that includes all polynomials of horsepower up to fifth-degree is shown in green. 

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>56.9001</td><td>1.8004</td><td>31.6</td><td>&lt; 0.0001</td></tr><tr><td>horsepower</td><td>-0.4662</td><td>0.0311</td><td>-15.0</td><td>&lt; 0.0001</td></tr><tr><td> $horsepower^2$ </td><td>0.0012</td><td>0.0001</td><td>10.1</td><td>&lt; 0.0001</td></tr></table>

TABLE 3.10. For the Auto data set, least squares coefficient estimates associated with the regression of mpg onto horsepower and horsepower $^{2}$ .

If including horsepower $^{2}$ led to such a big improvement in the model, why not include horsepower $^{3}$ , horsepower $^{4}$ , or even horsepower $^{5}$ ? The green curve in Figure 3.8 displays the fit that results from including all polynomials up to fifth degree in the model (3.36). The resulting fit seems unnecessarily wiggly—that is, it is unclear that including the additional terms really has led to a better fit to the data.

The approach that we have just described for extending the linear model to accommodate non-linear relationships is known as polynomial regression, since we have included polynomial functions of the predictors in the regression model. We further explore this approach and other non-linear extensions of the linear model in Chapter 7.

# 3.3.3 Potential Problems

When we fit a linear regression model to a particular data set, many problems may occur. Most common among these are the following:

2. Correlation of error terms.   
3. Non-constant variance of error terms.   
4. Outliers.   
5. High-leverage points.   
6. Collinearity.

1. Non-linearity of the response-predictor relationships.

In practice, identifying and overcoming these problems is as much an art as a science. Many pages in countless books have been written on this topic. Since the linear regression model is not our primary focus here, we will provide only a brief summary of some key points.

# 1. Non-linearity of the Data

![](images/9e2983164d909474e7e5002b8440cb485b27bcee84799b5c1a58454ef9a44c7e.jpg)

<details>
<summary>scatter</summary>

| Fitted values | Residuals |
| ------------- | --------- |
| 334           | 15        |
| 323           | 18        |
| 330           | 16        |
</details>

![](images/5dc34758fe7c23d4006a9287f988e87c05bbb59bb217510933856f8ae1fd6af5.jpg)

<details>
<summary>scatter</summary>

| Fitted values | Residuals |
| ------------- | --------- |
| 15            | 0         |
| 20            | -2        |
| 25            | -1        |
| 30            | 0         |
| 35            | 2         |
</details>

FIGURE 3.9. Plots of residuals versus predicted (or fitted) values for the Auto data set. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. Left: A linear regression of mpg on horsepower. A strong pattern in the residuals indicates non-linearity in the data. Right: A linear regression of mpg on horsepower and horsepower $^{2}$ . There is little pattern in the residuals.

The linear regression model assumes that there is a straight-line relationship between the predictors and the response. If the true relationship is far from linear, then virtually all of the conclusions that we draw from the fit are suspect. In addition, the prediction accuracy of the model can be significantly reduced.

Residual plots are a useful graphical tool for identifying non-linearity. Given a simple linear regression model, we can plot the residuals, $e_{i} =$

residual plot

$y_{i}-\hat{y}_{i}$ , versus the predictor $x_{i}$ . In the case of a multiple regression model, since there are multiple predictors, we instead plot the residuals versus the predicted (or fitted) values $\hat{y}_{i}$ . Ideally, the residual plot will show no discernible pattern. The presence of a pattern may indicate a problem with some aspect of the linear model.

The left panel of Figure 3.9 displays a residual plot from the linear regression of mpg onto horsepower on the Auto data set that was illustrated in Figure 3.8. The red line is a smooth fit to the residuals, which is displayed in order to make it easier to identify any trends. The residuals exhibit a clear U-shape, which provides a strong indication of non-linearity in the data. In contrast, the right-hand panel of Figure 3.9 displays the residual plot that results from the model (3.36), which contains a quadratic term. There appears to be little pattern in the residuals, suggesting that the quadratic term improves the fit to the data.

If the residual plot indicates that there are non-linear associations in the data, then a simple approach is to use non-linear transformations of the predictors, such as $\log X$ , $\sqrt{X}$ , and $X^{2}$ , in the regression model. In the later chapters of this book, we will discuss other more advanced non-linear approaches for addressing this issue.

# 2. Correlation of Error Terms

An important assumption of the linear regression model is that the error terms, $\epsilon_{1}, \epsilon_{2}, \ldots, \epsilon_{n}$ , are uncorrelated. What does this mean? For instance, if the errors are uncorrelated, then the fact that $\epsilon_{i}$ is positive provides little or no information about the sign of $\epsilon_{i+1}$ . The standard errors that are computed for the estimated regression coefficients or the fitted values are based on the assumption of uncorrelated error terms. If in fact there is correlation among the error terms, then the estimated standard errors will tend to underestimate the true standard errors. As a result, confidence and prediction intervals will be narrower than they should be. For example, a 95% confidence interval may in reality have a much lower probability than 0.95 of containing the true value of the parameter. In addition, p-values associated with the model will be lower than they should be; this could cause us to erroneously conclude that a parameter is statistically significant. In short, if the error terms are correlated, we may have an unwarranted sense of confidence in our model.

As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs. If we ignored this, our standard error calculations would be as if we had a sample of size 2n, when in fact we have only n samples. Our estimated parameters would be the same for the 2n samples as for the n samples, but the confidence intervals would be narrower by a factor of $\sqrt{2}!$

Why might correlations among the error terms occur? Such correlations frequently occur in the context of time series data, which consists of observations for which measurements are obtained at discrete points in time. In many cases, observations that are obtained at adjacent time points will have positively correlated errors. In order to determine if this is the case for a given data set, we can plot the residuals from our model as a function of time. If the errors are uncorrelated, then there should be no discernible pattern. On the other hand, if the error terms are positively correlated, then we may see tracking in the residuals—that is, adjacent residuals may have similar values. Figure 3.10 provides an illustration. In the top panel, we see the residuals from a linear regression fit to data generated with uncorrelated errors. There is no evidence of a time-related trend in the residuals. In contrast, the residuals in the bottom panel are from a data set in which adjacent errors had a correlation of 0.9. Now there is a clear pattern in the residuals—adjacent residuals tend to take on similar values. Finally, the center panel illustrates a more moderate case in which the residuals had a correlation of 0.5. There is still evidence of tracking, but the pattern is less clear.

![](images/2f1d318321b150daab4bd90216540835b54b1a38b1cde893f75477e69cfe1954.jpg)  
FIGURE 3.10. Plots of residuals from simulated time series data sets generated with differing levels of correlation $\rho$ between error terms for adjacent time points.

Many methods have been developed to properly take account of correlations in the error terms in time series data. Correlation among the error terms can also occur outside of time series data. For instance, consider a study in which individuals' heights are predicted from their weights. The assumption of uncorrelated errors could be violated if some of the individuals in the study are members of the same family, eat the same diet, or have been exposed to the same environmental factors. In general, the assumption of uncorrelated errors is extremely important for linear regression as well as for other statistical methods, and good experimental design is crucial in order to mitigate the risk of such correlations.

![](images/7e79d43cbdafcb37795bd3ad452c5d5da300aedcbea3a6f2ae4295a8baef99a4.jpg)

<details>
<summary>scatter</summary>

| Fitted values | Residuals |
| ------------- | --------- |
| 30            | 998       |
| 28            | 875       |
| 26            | 845       |
</details>

![](images/9dd055cce57269d7133d0f20d8abfb552a415de56f57e01af89121aeb5f500d1.jpg)

<details>
<summary>line</summary>

| Fitted values | Residuals |
| ------------- | --------- |
| 2.4           | -0.2      |
| 2.6           | 0.0       |
| 2.8           | 0.1       |
| 3.0           | 0.2       |
| 3.2           | 0.1       |
| 3.4           | 0.0       |
</details>

FIGURE 3.11. Residual plots. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. The blue lines track the outer quantiles of the residuals, and emphasize patterns. Left: The funnel shape indicates heteroscedasticity. Right: The response has been log transformed, and there is now no evidence of heteroscedasticity.

# 3. Non-constant Variance of Error Terms

Another important assumption of the linear regression model is that the error terms have a constant variance, $\operatorname{Var}(\epsilon_{i}) = \sigma^{2}$ . The standard errors, confidence intervals, and hypothesis tests associated with the linear model rely upon this assumption.

Unfortunately, it is often the case that the variances of the error terms are non-constant. For instance, the variances of the error terms may increase with the value of the response. One can identify non-constant variances in the errors, or heteroscedasticity, from the presence of a funnel shape in the residual plot. An example is shown in the left-hand panel of Figure 3.11, in which the magnitude of the residuals tends to increase with the fitted values. When faced with this problem, one possible solution is to transform the response Y using a concave function such as $\log Y$ or $\sqrt{Y}$ . Such a transformation results in a greater amount of shrinkage of the larger responses, leading to a reduction in heteroscedasticity. The right-hand panel of Figure 3.11 displays the residual plot after transforming the response using $\log Y$ . The residuals now appear to have constant variance, though there is some evidence of a slight non-linear relationship in the data.

Sometimes we have a good idea of the variance of each response. For example, the ith response could be an average of $n_{i}$ raw observations. If each of these raw observations is uncorrelated with variance $\sigma^{2}$ , then their average has variance $\sigma_{i}^{2} = \sigma^{2}/n_{i}$ . In this case a simple remedy is to fit our model by weighted least squares, with weights proportional to the inverse variances—i.e. $w_{i} = n_{i}$ in this case. Most linear regression software allows for observation weights.

hetero-
scedasticity

weighted least squares

# 4. Outliers

An outlier is a point for which $y_{i}$ is far from the value predicted by the

outlier

![](images/33f2173417e3f9384ad2f5f3ced0024059368a29f0a41fc66f9b9e932954f0f2.jpg)

<details>
<summary>scatter</summary>

| X    | Y    |
| ---- | ---- |
| -2   | -4   |
| -1   | 0    |
| 0    | 2    |
| 1    | 4    |
| 2    | 6    |
</details>

![](images/7374cc5b77cf47bc03f400bca19e24318c4d8d34dc3b700ea9857f17c4c8ec49.jpg)

<details>
<summary>scatter</summary>

| Fitted Values | Residuals |
| ------------- | --------- |
| -2            | -1        |
| 0             | 0         |
| 2             | 1         |
| 4             | 0         |
| 6             | -1        |
</details>

![](images/9c3d371d883ff2b67255eae1a97de29d0c7b3e867e2ba000c836322e83898eac.jpg)

<details>
<summary>scatter</summary>

| Fitted Values | Studentized Residuals |
| ------------- | --------------------- |
| -2            | 0                     |
| 0             | 0                     |
| 2             | 0                     |
| 4             | 0                     |
| 6             | 0                     |
</details>

FIGURE 3.12. Left: The least squares regression line is shown in red, and the regression line after removing the outlier is shown in blue. Center: The residual plot clearly identifies the outlier. Right: The outlier has a studentized residual of 6; typically we expect values between -3 and 3.

model. Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.

The red point (observation 20) in the left-hand panel of Figure 3.12 illustrates a typical outlier. The red solid line is the least squares regression fit, while the blue dashed line is the least squares fit after removal of the outlier. In this case, removing the outlier has little effect on the least squares line: it leads to almost no change in the slope, and a miniscule reduction in the intercept. It is typical for an outlier that does not have an unusual predictor value to have little effect on the least squares fit. However, even if an outlier does not have much effect on the least squares fit, it can cause other problems. For instance, in this example, the RSE is 1.09 when the outlier is included in the regression, but it is only 0.77 when the outlier is removed. Since the RSE is used to compute all confidence intervals and p-values, such a dramatic increase caused by a single data point can have implications for the interpretation of the fit. Similarly, inclusion of the outlier causes the $R^{2}$ to decline from 0.892 to 0.805.

Residual plots can be used to identify outliers. In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12. But in practice, it can be difficult to decide how large a residual needs to be before we consider the point to be an outlier. To address this problem, instead of plotting the residuals, we can plot the studentized residuals, computed by dividing each residual $e_i$ by its estimated standard error. Observations whose studentized residuals are greater than 3 in absolute value are possible outliers. In the right-hand panel of Figure 3.12, the outlier's studentized residual exceeds 6, while all other observations have studentized residuals between -2 and 2.

If we believe that an outlier has occurred due to an error in data collection or recording, then one solution is to simply remove the observation. However, care should be taken, since an outlier may instead indicate a deficiency with the model, such as a missing predictor.

# 5. High Leverage Points

We just saw that outliers are observations for which the response $y_{i}$ is unusual given the predictor $x_{i}$ . In contrast, observations with high leverage have an unusual value for $x_{i}$ . For example, observation 41 in the left-hand panel of Figure 3.13 has high leverage, in that the predictor value for this observation is large relative to the other observations. (Note that the data displayed in Figure 3.13 are the same as the data displayed in Figure 3.12, but with the addition of a single high leverage observation.) The red solid line is the least squares fit to the data, while the blue dashed line is the fit produced when observation 41 is removed. Comparing the left-hand panels of Figures 3.12 and 3.13, we observe that removing the high leverage observation has a much more substantial impact on the least squares line than removing the outlier. In fact, high leverage observations tend to have a sizable impact on the estimated regression line. It is cause for concern if the least squares line is heavily affected by just a couple of observations, because any problems with these points may invalidate the entire fit. For this reason, it is important to identify high leverage observations.

![](images/0a69819d985b2412ad7a7bb05360ef3aed42cb1a83939790c2dfe2e9dc464120.jpg)

<details>
<summary>scatter</summary>

| X    | Y    |
| ---- | ---- |
| -2   | 0    |
| -1   | 1    |
| 0    | 2    |
| 1    | 3    |
| 2    | 4    |
| 3    | 5    |
| 4    | 6    |
</details>

![](images/5a7d28b1b89e34c7e689b667a2dbf0623fe81dbc09485e79a9331135c51fd39b.jpg)

<details>
<summary>scatter</summary>

| X1    | X2    |
|-------|-------|
| -2.0  | -2.0  |
| -1.5  | -1.5  |
| -1.0  | -1.0  |
| -0.5  | -0.5  |
| 0.0   | 0.0   |
| 0.5   | 0.5   |
| 1.0   | 1.0   |
| 1.5   | 1.5   |
| 2.0   | 2.0   |
</details>

![](images/083ebdc348af76de2245c87a80e2930421e8c9c6b1f23fee0cfa303ba66d9d16.jpg)

<details>
<summary>scatter</summary>

| Leverage | Studentized Residuals |
| -------- | --------------------- |
| 0.01     | 5                     |
| 0.25     | 3                     |
</details>

FIGURE 3.13. Left: Observation 41 is a high leverage point, while 20 is not. The red line is the fit to all the data, and the blue line is the fit with observation 41 removed. Center: The red observation is not unusual in terms of its $X_{1}$ value or its $X_{2}$ value, but still falls outside the bulk of the data, and hence has high leverage. Right: Observation 41 has a high leverage and a high residual.

In a simple linear regression, high leverage observations are fairly easy to identify, since we can simply look for observations for which the predictor value is outside of the normal range of the observations. But in a multiple linear regression with many predictors, it is possible to have an observation that is well within the range of each individual predictor's values, but that is unusual in terms of the full set of predictors. An example is shown in the center panel of Figure 3.13, for a data set with two predictors, $X_{1}$ and $X_{2}$ . Most of the observations' predictor values fall within the blue dashed ellipse, but the red observation is well outside of this range. But neither its value for $X_{1}$ nor its value for $X_{2}$ is unusual. So if we examine just $X_{1}$ or just $X_{2}$ , we will fail to notice this high leverage point. This problem is more pronounced in multiple regression settings with more than two predictors, because then there is no simple way to plot all dimensions of the data simultaneously.

In order to quantify an observation's leverage, we compute the leverage statistic. A large value of this statistic indicates an observation with high leverage. For a simple linear regression,

leverage statistic

$$
h _ {i} = \frac {1}{n} + \frac {(x _ {i} - \bar {x}) ^ {2}}{\sum_ {i ^ {\prime} = 1} ^ {n} (x _ {i ^ {\prime}} - \bar {x}) ^ {2}}. \tag {3.37}
$$

![](images/c3c8e351117492bfba4a768a712d67cb3741193e4cb2a6edc693b98e25258f99.jpg)

<details>
<summary>scatter</summary>

| Limit | Age |
| ----- | --- |
| 2000  | 45  |
| 2500  | 65  |
| 3000  | 75  |
| 3500  | 70  |
| 4000  | 65  |
| 4500  | 60  |
| 5000  | 55  |
| 5500  | 50  |
| 6000  | 45  |
| 6500  | 40  |
| 7000  | 35  |
| 7500  | 30  |
| 8000  | 25  |
| 8500  | 20  |
| 9000  | 15  |
| 9500  | 10  |
| 10000 | 5   |
| 10500 | 3   |
| 11000 | 2   |
| 11500 | 1   |
| 12000 | 0   |
| 12500 | -1  |
</details>

![](images/2949085958dc3abe277ed6c1ffc244411bc0a9af847c0f572256f49397a5d9a8.jpg)

<details>
<summary>scatter</summary>

| Limit | Rating |
| ----- | ------ |
| 1000  | 120    |
| 2000  | 200    |
| 3000  | 280    |
| 4000  | 360    |
| 5000  | 440    |
| 6000  | 520    |
| 7000  | 600    |
| 8000  | 680    |
| 9000  | 760    |
| 10000 | 840    |
| 11000 | 920    |
| 12000 | 1000   |
| 13000 | 1180   |
</details>

FIGURE 3.14. Scatterplots of the observations from the Credit data set. Left: A plot of age versus limit. These two variables are not collinear. Right: A plot of rating versus limit. There is high collinearity.

It is clear from this equation that $h_{i}$ increases with the distance of $x_{i}$ from $\bar{x}$ . There is a simple extension of $h_{i}$ to the case of multiple predictors, though we do not provide the formula here. The leverage statistic $h_{i}$ is always between 1/n and 1, and the average leverage for all the observations is always equal to $(p+1)/n$ . So if a given observation has a leverage statistic that greatly exceeds $(p+1)/n$ , then we may suspect that the corresponding point has high leverage.

The right-hand panel of Figure 3.13 provides a plot of the studentized residuals versus $h_{i}$ for the data in the left-hand panel of Figure 3.13. Observation 41 stands out as having a very high leverage statistic as well as a high studentized residual. In other words, it is an outlier as well as a high leverage observation. This is a particularly dangerous combination! This plot also reveals the reason that observation 20 had relatively little effect on the least squares fit in Figure 3.12: it has low leverage.

# 6. Collinearity

Collinearity refers to the situation in which two or more predictor variables are closely related to one another. The concept of collinearity is illustrated in Figure 3.14 using the Credit data set. In the left-hand panel of Figure 3.14, the two predictors limit and age appear to have no obvious relationship. In contrast, in the right-hand panel of Figure 3.14, the predictors limit and rating are very highly correlated with each other, and we say that they are collinear. The presence of collinearity can pose problems in the regression context, since it can be difficult to separate out the individual effects of collinear variables on the response. In other words, since limit and rating tend to increase or decrease together, it can be difficult to determine how each one separately is associated with the response, balance.

Figure 3.15 illustrates some of the difficulties that can result from collinearity. The left-hand panel of Figure 3.15 is a contour plot of the RSS (3.22) associated with different possible coefficient estimates for the regression of balance on limit and age. Each ellipse represents a set of coefficients that correspond to the same RSS, with ellipses nearest to the center taking on the lowest values of RSS. The black dots and associated dashed lines represent the coefficient estimates that result in the smallest possible RSS—in other words, these are the least squares estimates. The axes for limit and age have been scaled so that the plot includes possible coefficient estimates that are up to four standard errors on either side of the least squares estimates. Thus the plot includes all plausible values for the coefficients. For example, we see that the true limit coefficient is almost certainly somewhere between 0.15 and 0.20.

![](images/5df6f09f853d8e38e1821e0244fa9c3f97a48123dfd1e22dde699e23f6b66597.jpg)

<details>
<summary>radar</summary>

| βLimit | βAge  |
|--------|-------|
| 0.17   | -2.5  |
| 0.16   | -2.0  |
| 0.15   | -1.5  |
| 0.14   | -1.0  |
| 0.13   | -0.5  |
| 0.12   | 0.0   |
| 0.11   | 0.5   |
| 0.10   | 1.0   |
| 0.09   | 1.5   |
| 0.08   | 2.0   |
| 0.07   | 2.5   |
| 0.06   | 3.0   |
| 0.05   | 3.5   |
| 0.04   | 4.0   |
| 0.03   | 4.5   |
| 0.02   | 5.0   |
| 0.01   | 5.5   |
| 0.00   | 6.0   |
</details>

![](images/84c3f9fefb2eb218b5519ccd4774074b9d1d24dc62de47cad04e5d5a42ac9f8c.jpg)

<details>
<summary>scatter</summary>

| β_Limit | β_Rating |
| ------- | -------- |
| -0.1    | 4.5      |
| 0.0     | 2.0      |
| 0.2     | 0.0      |
</details>

FIGURE 3.15. Contour plots for the RSS values as a function of the parameters $\beta$ for various regressions involving the Credit data set. In each plot, the black dots represent the coefficient values corresponding to the minimum RSS. Left: A contour plot of RSS for the regression of balance onto age and limit. The minimum value is well defined. Right: A contour plot of RSS for the regression of balance onto rating and limit. Because of the collinearity, there are many pairs ( $\beta_{Limit}, \beta_{Rating}$ ) with a similar value for RSS.

In contrast, the right-hand panel of Figure 3.15 displays contour plots of the RSS associated with possible coefficient estimates for the regression of balance onto limit and rating, which we know to be highly collinear. Now the contours run along a narrow valley; there is a broad range of values for the coefficient estimates that result in equal values for RSS. Hence a small change in the data could cause the pair of coefficient values that yield the smallest RSS—that is, the least squares estimates—to move anywhere along this valley. This results in a great deal of uncertainty in the coefficient estimates. Notice that the scale for the limit coefficient now runs from roughly -0.2 to 0.2; this is an eight-fold increase over the plausible range of the limit coefficient in the regression with age. Interestingly, even though the limit and rating coefficients now have much more individual uncertainty, they will almost certainly lie somewhere in this contour valley. For example, we would not expect the true value of the limit and rating coefficients to be -0.1 and 1 respectively, even though such a value is plausible for each coefficient individually.

Since collinearity reduces the accuracy of the estimates of the regression coefficients, it causes the standard error for $\hat{\beta}_{j}$ to grow. Recall that the t-statistic for each predictor is calculated by dividing $\hat{\beta}_{j}$ by its standard error. Consequently, collinearity results in a decline in the t-statistic. As a result, in the presence of collinearity, we may fail to reject $H_{0} : \beta_{j} = 0$ . This means that the power of the hypothesis test—the probability of correctly detecting a non-zero coefficient—is reduced by collinearity.

<table><tr><td colspan="2"></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td rowspan="3">Model 1</td><td>Intercept</td><td>-173.411</td><td>43.828</td><td>-3.957</td><td>&lt; 0.0001</td></tr><tr><td>age</td><td>-2.292</td><td>0.672</td><td>-3.407</td><td>0.0007</td></tr><tr><td>limit</td><td>0.173</td><td>0.005</td><td>34.496</td><td>&lt; 0.0001</td></tr><tr><td rowspan="3">Model 2</td><td>Intercept</td><td>-377.537</td><td>45.254</td><td>-8.343</td><td>&lt; 0.0001</td></tr><tr><td>rating</td><td>2.202</td><td>0.952</td><td>2.312</td><td>0.0213</td></tr><tr><td>limit</td><td>0.025</td><td>0.064</td><td>0.384</td><td>0.7012</td></tr></table>

TABLE 3.11. The results for two multiple regression models involving the Credit data set are shown. Model 1 is a regression of balance on age and limit, and Model 2 a regression of balance on rating and limit. The standard error of $\hat{\beta}_{limit}$ increases 12-fold in the second regression, due to collinearity.

Table 3.11 compares the coefficient estimates obtained from two separate multiple regression models. The first is a regression of balance on age and limit, and the second is a regression of balance on rating and limit. In the first regression, both age and limit are highly significant with very small p-values. In the second, the collinearity between limit and rating has caused the standard error for the limit coefficient estimate to increase by a factor of 12 and the p-value to increase to 0.701. In other words, the importance of the limit variable has been masked due to the presence of collinearity. To avoid such a situation, it is desirable to identify and address potential collinearity problems while fitting the model.

A simple way to detect collinearity is to look at the correlation matrix of the predictors. An element of this matrix that is large in absolute value indicates a pair of highly correlated variables, and therefore a collinearity problem in the data. Unfortunately, not all collinearity problems can be detected by inspection of the correlation matrix: it is possible for collinearity to exist between three or more variables even if no pair of variables has a particularly high correlation. We call this situation multicollinearity. Instead of inspecting the correlation matrix, a better way to assess multicollinearity is to compute the variance inflation factor (VIF). The VIF is the ratio of the variance of $\hat{\beta}_{j}$ when fitting the full model divided by the variance of $\hat{\beta}_{j}$ if fit on its own. The smallest possible value for VIF is 1, which indicates the complete absence of collinearity. Typically in practice there is a small amount of collinearity among the predictors. As a rule of thumb, a VIF value that exceeds 5 or 10 indicates a problematic amount of collinearity. The VIF for each variable can be computed using the formula

$$
\mathrm{VIF} (\hat {\beta} _ {j}) = \frac {1}{1 - R _ {X _ {j} | X _ {- j}} ^ {2}},
$$

where $R_{X_{j}|X_{-j}}^{2}$ is the $R^{2}$ from a regression of $X_{j}$ onto all of the other predictors. If $R_{X_{j}|X_{-j}}^{2}$ is close to one, then collinearity is present, and so the VIF will be large.

In the Credit data, a regression of balance on age, rating, and limit indicates that the predictors have VIF values of 1.01, 160.67, and 160.59. As we suspected, there is considerable collinearity in the data!

When faced with the problem of collinearity, there are two simple solutions. The first is to drop one of the problematic variables from the regression. This can usually be done without much compromise to the regression fit, since the presence of collinearity implies that the information that this variable provides about the response is redundant in the presence of the other variables. For instance, if we regress balance onto age and limit, without the rating predictor, then the resulting VIF values are close to the minimum possible value of 1, and the $R^{2}$ drops from 0.754 to 0.75. So dropping rating from the set of predictors has effectively solved the collinearity problem without compromising the fit. The second solution is to combine the collinear variables together into a single predictor. For instance, we might take the average of standardized versions of limit and rating in order to create a new variable that measures credit worthiness.

# 3.4 The Marketing Plan

We now briefly return to the seven questions about the Advertising data that we set out to answer at the beginning of this chapter.

1. Is there a relationship between sales and advertising budget?

This question can be answered by fitting a multiple regression model of sales onto TV, radio, and newspaper, as in (3.20), and testing the hypothesis $H_{0} : \beta_{TV} = \beta_{radio} = \beta_{newspaper} = 0$ . In Section 3.2.2, we showed that the F-statistic can be used to determine whether or not we should reject this null hypothesis. In this case the p-value corresponding to the F-statistic in Table 3.6 is very low, indicating clear evidence of a relationship between advertising and sales.

2. How strong is the relationship?

We discussed two measures of model accuracy in Section 3.1.3. First, the RSE estimates the standard deviation of the response from the population regression line. For the Advertising data, the RSE is 1.69 units while the mean value for the response is 14.022, indicating a percentage error of roughly 12%. Second, the $R^{2}$ statistic records the percentage of variability in the response that is explained by the predictors. The predictors explain almost 90% of the variance in sales. The RSE and $R^{2}$ statistics are displayed in Table 3.6.

3. Which media are associated with sales?

To answer this question, we can examine the p-values associated with each predictor's t-statistic (Section 3.1.2). In the multiple linear regression displayed in Table 3.4, the p-values for TV and radio are low, but the p-value for newspaper is not. This suggests that only TV and radio are related to sales. In Chapter 6 we explore this question in greater detail.

4. How large is the association between each medium and sales?

We saw in Section 3.1.2 that the standard error of $\hat{\beta}_j$ can be used to construct confidence intervals for $\beta_{j}$ . For the Advertising data, we can use the results in Table 3.4 to compute the $95\%$ confidence intervals for the coefficients in a multiple regression model using all three media budgets as predictors. The confidence intervals are as follows: (0.043, 0.049) for TV, (0.172, 0.206) for radio, and $(-0.013, 0.011)$ for newspaper. The confidence intervals for TV and radio are narrow and far from zero, providing evidence that these media are related to sales. But the interval for newspaper includes zero, indicating that the variable is not statistically significant given the values of TV and radio.

We saw in Section 3.3.3 that collinearity can result in very wide standard errors. Could collinearity be the reason that the confidence interval associated with newspaper is so wide? The VIF scores are 1.005, 1.145, and 1.145 for TV, radio, and newspaper, suggesting no evidence of collinearity.

In order to assess the association of each medium individually on sales, we can perform three separate simple linear regressions. Results are shown in Tables 3.1 and 3.3. There is evidence of an extremely strong association between TV and sales and between radio and sales. There is evidence of a mild association between newspaper and sales, when the values of TV and radio are ignored.

5. How accurately can we predict future sales?

The response can be predicted using $(3.21)$ . The accuracy associated with this estimate depends on whether we wish to predict an individual response, $Y = f(X) + \epsilon$ , or the average response, $f(X)$ (Section 3.2.2). If the former, we use a prediction interval, and if the latter, we use a confidence interval. Prediction intervals will always be wider than confidence intervals because they account for the uncertainty associated with $\epsilon$ , the irreducible error.

6. Is the relationship linear?

In Section 3.3.3, we saw that residual plots can be used in order to identify non-linearity. If the relationships are linear, then the residual plots should display no pattern. In the case of the Advertising data, we observe a non-linear effect in Figure 3.5, though this effect could also be observed in a residual plot. In Section 3.3.2, we discussed the inclusion of transformations of the predictors in the linear regression model in order to accommodate non-linear relationships.

7. Is there synergy among the advertising media?

The standard linear regression model assumes an additive relationship between the predictors and the response. An additive model is easy to interpret because the association between each predictor and the response is unrelated to the values of the other predictors. However, the additive assumption may be unrealistic for certain data sets. In Section 3.3.2, we showed how to include an interaction term in the regression model in order to accommodate non-additive relationships. A small p-value associated with the interaction term indicates the presence of such relationships. Figure 3.5 suggested that the Advertising data may not be additive. Including an interaction term in the model results in a substantial increase in $R^{2}$ , from around 90% to almost 97%.

# 3.5 Comparison of Linear Regression with $K$ -Nearest Neighbors

As discussed in Chapter 2, linear regression is an example of a parametric approach because it assumes a linear functional form for $f(X)$ . Parametric methods have several advantages. They are often easy to fit, because one need estimate only a small number of coefficients. In the case of linear regression, the coefficients have simple interpretations, and tests of statistical significance can be easily performed. But parametric methods do have a disadvantage: by construction, they make strong assumptions about the form of $f(X)$ . If the specified functional form is far from the truth, and prediction accuracy is our goal, then the parametric method will perform poorly. For instance, if we assume a linear relationship between X and Y but the true relationship is far from linear, then the resulting model will provide a poor fit to the data, and any conclusions drawn from it will be suspect.

In contrast, non-parametric methods do not explicitly assume a parametric form for $f(X)$ , and thereby provide an alternative and more flexible approach for performing regression. We discuss various non-parametric methods in this book. Here we consider one of the simplest and best-known non-parametric methods, K-nearest neighbors regression (KNN regression). The KNN regression method is closely related to the KNN classifier discussed in Chapter 2. Given a value for K and a prediction point $x_{0}$ , KNN regression first identifies the K training observations that are closest to $x_{0}$ , represented by $N_{0}$ . It then estimates $f(x_{0})$ using the average of all the training responses in $N_{0}$ . In other words,

$$
\hat {f} (x _ {0}) = \frac {1}{K} \sum_ {x _ {i} \in \mathcal {N} _ {0}} y _ {i}.
$$

Figure 3.16 illustrates two KNN fits on a data set with p = 2 predictors. The fit with K = 1 is shown in the left-hand panel, while the right-hand panel corresponds to K = 9. We see that when K = 1, the KNN fit perfectly interpolates the training observations, and consequently takes the form of a step function. When K = 9, the KNN fit still is a step function, but averaging over nine observations results in much smaller regions of constant prediction, and consequently a smoother fit. In general, the optimal value for K will depend on the bias-variance tradeoff, which we introduced in Chapter 2. A small value for K provides the most flexible fit, which will have low bias but high variance. This variance is due to the fact that the prediction in a given region is entirely dependent on just one observation.

K-nearest
neighbors
regression

![](images/8c39a71be45c935390161c3493175d865557d90350fbc2f0b8308d1a99d71fe1.jpg)

<details>
<summary>natural_image</summary>

3D rendered cube with colored blocks and orange-yellow dots, labeled x₁, x₂, y axes (no text or symbols on the blocks themselves)
</details>

![](images/2e81390b95ecc6de6317ab29f7cb2189a9bc50d28e976ad0199764529703f6bc.jpg)

<details>
<summary>surface_3d</summary>

| x1 | y1 | x2 |
|----|----|----|
| (data not extractable as discrete values) | (data not extractable as discrete values) | (data not extractable as discrete values) |
</details>

FIGURE 3.16. Plots of $\hat{f}(X)$ using KNN regression on a two-dimensional data set with 64 observations (orange dots). Left: K = 1 results in a rough step function fit. Right: K = 9 produces a much smoother fit.

In contrast, larger values of K provide a smoother and less variable fit; the prediction in a region is an average of several points, and so changing one observation has a smaller effect. However, the smoothing may cause bias by masking some of the structure in $f(X)$ . In Chapter 5, we introduce several approaches for estimating test error rates. These methods can be used to identify the optimal value of K in KNN regression.

In what setting will a parametric approach such as least squares linear regression outperform a non-parametric approach such as KNN regression? The answer is simple: the parametric approach will outperform the nonparametric approach if the parametric form that has been selected is close to the true form of f. Figure 3.17 provides an example with data generated from a one-dimensional linear regression model. The black solid lines represent $f(X)$ , while the blue curves correspond to the KNN fits using K = 1 and K = 9. In this case, the K = 1 predictions are far too variable, while the smoother K = 9 fit is much closer to $f(X)$ . However, since the true relationship is linear, it is hard for a non-parametric approach to compete with linear regression: a non-parametric approach incurs a cost in variance that is not offset by a reduction in bias. The blue dashed line in the left-hand panel of Figure 3.18 represents the linear regression fit to the same data. It is almost perfect. The right-hand panel of Figure 3.18 reveals that linear regression outperforms KNN for this data. The green solid line, plotted as a function of 1/K, represents the test set mean squared error (MSE) for KNN. The KNN errors are well above the black dashed line, which is the test MSE for linear regression. When the value of K is large, then KNN performs only a little worse than least squares regression in terms of MSE. It performs far worse when K is small.

In practice, the true relationship between X and Y is rarely exactly linear. Figure 3.19 examines the relative performances of least squares regression and KNN under increasing levels of non-linearity in the relationship between X and Y. In the top row, the true relationship is nearly linear. In this case we see that the test MSE for linear regression is still superior

![](images/a6e67d78debd9be532b36229a667d5631a820cb175a896d93d92f2fd1e60b4ce.jpg)

<details>
<summary>line</summary>

| x     | y (red dots) | y (blue line) |
|-------|--------------|---------------|
| -1.0  | 0.5          | 0.5           |
| -0.8  | 1.0          | 1.0           |
| -0.6  | 1.2          | 1.2           |
| -0.4  | 1.5          | 1.5           |
| -0.2  | 2.0          | 2.0           |
| 0.0   | 2.2          | 2.2           |
| 0.2   | 2.5          | 2.5           |
| 0.4   | 3.0          | 3.0           |
| 0.6   | 3.5          | 3.5           |
| 0.8   | 3.8          | 3.8           |
| 1.0   | 4.0          | 4.0           |
</details>

![](images/f99747018f735260181de487e0cb45b26b9e5b093721c40f3623d2bd1da636d8.jpg)

<details>
<summary>scatter</summary>

| x    | y    |
| ---- | ---- |
| -1.0 | 0.5  |
| -0.8 | 0.7  |
| -0.6 | 1.0  |
| -0.4 | 1.3  |
| -0.2 | 1.6  |
| 0.0  | 1.9  |
| 0.2  | 2.2  |
| 0.4  | 2.5  |
| 0.6  | 2.8  |
| 0.8  | 3.1  |
| 1.0  | 3.4  |
</details>

FIGURE 3.17. Plots of $\hat{f}(X)$ using KNN regression on a one-dimensional data set with 50 observations. The true relationship is given by the black solid line. Left: The blue curve corresponds to K = 1 and interpolates (i.e. passes directly through) the training data. Right: The blue curve corresponds to K = 9, and represents a smoother fit.

![](images/298be708f46c580467c28591f2b75738c6199b6d3c84e1d110be907c910b1e92.jpg)

<details>
<summary>scatter</summary>

| x       | y       |
| ------- | ------- |
| -1.0    | 0.5     |
| -0.8    | 0.7     |
| -0.6    | 1.0     |
| -0.4    | 1.3     |
| -0.2    | 1.6     |
| 0.0     | 1.9     |
| 0.2     | 2.2     |
| 0.4     | 2.5     |
| 0.6     | 2.8     |
| 0.8     | 3.1     |
| 1.0     | 3.4     |
</details>

![](images/7e4b07eb742a2bf034049528b9a89b747ec1d851b29548f1090609a58c655543.jpg)

<details>
<summary>line</summary>

| 1/K   | Mean Squared Error |
|-------|---------------------|
| 0.0   | 0.11                |
| 0.1   | 0.11                |
| 0.2   | 0.12                |
| 0.3   | 0.12                |
| 0.4   | 0.12                |
| 0.5   | 0.14                |
| 1.0   | 0.18                |
</details>

FIGURE 3.18. The same data set shown in Figure 3.17 is investigated further. Left: The blue dashed line is the least squares fit to the data. Since $f(X)$ is in fact linear (displayed as the black line), the least squares regression line provides a very good estimate of $f(X)$ . Right: The dashed horizontal line represents the least squares test set MSE, while the green solid line corresponds to the MSE for KNN as a function of 1/K (on the log scale). Linear regression achieves a lower test MSE than does KNN regression, since $f(X)$ is in fact linear. For KNN regression, the best results occur with a very large value of K, corresponding to a small value of 1/K.

![](images/e0db46480eed97898bb267dfe1c0444446968f57d0de3bd7e0e75e393bd6b7a1.jpg)

<details>
<summary>line</summary>

| x    | y (black line) | y (red line) |
| ---- | -------------- | ------------ |
| -1.0 | 0.5            | 0.9          |
| -0.5 | 1.0            | 1.2          |
| 0.0  | 2.0            | 2.0          |
| 0.5  | 3.0            | 3.0          |
| 1.0  | 3.5            | 3.5          |
</details>

![](images/d82716585dddab2ff38ded453f2248c6e586fd2653fdc92806236598f5b95d1b.jpg)

<details>
<summary>line</summary>

| 1/K   | Mean Squared Error |
|-------|---------------------|
| 0.0   | 0.06                |
| 0.1   | 0.055               |
| 0.2   | 0.055               |
| 0.3   | 0.055               |
| 0.4   | 0.06                |
| 0.5   | 0.07                |
| 1.0   | 0.085               |
</details>

![](images/f4a28d403059b7622f007c5f432ab645b0a704db40fa47e9d7cc00261b0fcd41.jpg)

<details>
<summary>line</summary>

| x     | y (black line) | y (red line) | y (blue step) |
|-------|----------------|--------------|---------------|
| -1.0  | 1.0            | 1.0          | 1.0           |
| -0.5  | 1.5            | 1.5          | 1.5           |
| 0.0   | 2.5            | 2.5          | 2.5           |
| 0.5   | 3.5            | 3.5          | 3.5           |
| 1.0   | 3.0            | 3.0          | 3.0           |
</details>

![](images/0940b5f9d6f78ab3d0b411b42a8817221a82ba7867e3fcb1e5962f18003c25e2.jpg)

<details>
<summary>line</summary>

| 1/K   | Mean Squared Error |
|-------|---------------------|
| 0.0   | 0.058               |
| 0.1   | 0.053               |
| 0.2   | 0.052               |
| 0.3   | 0.053               |
| 0.4   | 0.060               |
| 0.5   | 0.070               |
| 1.0   | 0.090               |
</details>

FIGURE 3.19. Top Left: In a setting with a slightly non-linear relationship between X and Y (solid black line), the KNN fits with K = 1 (blue) and K = 9 (red) are displayed. Top Right: For the slightly non-linear data, the test set MSE for least squares regression (horizontal black) and KNN with various values of 1/K (green) are displayed. Bottom Left and Bottom Right: As in the top panel, but with a strongly non-linear relationship between X and Y.

to that of KNN for low values of K. However, for $K \geq 4$ , KNN outperforms linear regression. The second row illustrates a more substantial deviation from linearity. In this situation, KNN substantially outperforms linear regression for all values of K. Note that as the extent of non-linearity increases, there is little change in the test set MSE for the non-parametric KNN method, but there is a large increase in the test set MSE of linear regression.

Figures 3.18 and 3.19 display situations in which KNN performs slightly worse than linear regression when the relationship is linear, but much better than linear regression for nonlinear situations. In a real life situation in which the true relationship is unknown, one might suspect that KNN should be favored over linear regression because it will at worst be slightly inferior to linear regression if the true relationship is linear, and may give substantially better results if the true relationship is non-linear. But in reality, even when the true relationship is highly non-linear, KNN may still provide inferior results to linear regression. In particular, both Figures 3.18 and 3.19 illustrate settings with p = 1 predictor. But in higher dimensions, KNN often performs worse than linear regression.

![](images/72f565d31de56b7c9cc0d2f11e05cd4938f3ff51db4edfb969283e6f67fdd26d.jpg)  
FIGURE 3.20. Test MSE for linear regression (black dashed lines) and KNN (green curves) as the number of variables p increases. The true function is nonlinear in the first variable, as in the lower panel in Figure 3.19, and does not depend on the additional variables. The performance of linear regression deteriorates slowly in the presence of these additional noise variables, whereas KNN's performance degrades much more quickly as p increases.

Figure 3.20 considers the same strongly non-linear situation as in the second row of Figure 3.19, except that we have added additional noise predictors that are not associated with the response. When p = 1 or p = 2, KNN outperforms linear regression. But for p = 3 the results are mixed, and for $p \geq 4$ linear regression is superior to KNN. In fact, the increase in dimension has only caused a small deterioration in the linear regression test set MSE, but it has caused more than a ten-fold increase in the MSE for KNN. This decrease in performance as the dimension increases is a common problem for KNN, and results from the fact that in higher dimensions there is effectively a reduction in sample size. In this data set there are 50 training observations; when p = 1, this provides enough information to accurately estimate $f(X)$ . However, spreading 50 observations over p = 20 dimensions results in a phenomenon in which a given observation has no nearby neighbors—this is the so-called curse of dimensionality. That is, the K observations that are nearest to a given test observation $x_{0}$ may be very far away from $x_{0}$ in p-dimensional space when p is large, leading to a very poor prediction of $f(x_{0})$ and hence a poor KNN fit. As a general rule, parametric methods will tend to outperform non-parametric approaches when there is a small number of observations per predictor.

Even when the dimension is small, we might prefer linear regression to KNN from an interpretability standpoint. If the test MSE of KNN is only slightly lower than that of linear regression, we might be willing to forego a little bit of prediction accuracy for the sake of a simple model that can be described in terms of just a few coefficients, and for which p-values are available.

curse of dimensionality

# 3.6 Lab: Linear Regression

# 3.6.1 Importing packages

We import our standard libraries at this top level.

In [1]:   
```python
import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots 
```

# New imports

Throughout this lab we will introduce new functions and libraries. However, we will import them here to emphasize these are the new code objects in this lab. Keeping imports near the top of a notebook makes the code more readable, since scanning the first few lines tells us what libraries are used.

In [2]:   
```python
import statsmodels.api as sm 
```

We will provide relevant details about the functions below as they are needed.

Besides importing whole modules, it is also possible to import only a few items from a given module. This will help keep the namespace clean. We will use a few specific objects from the statsmodels package which we import here.

namespace
statsmodels

In [3]:   
```python
from statsmodels.stats.outliers_influence \
import variance_inflation_factor as VIF
from statsmodels.stats.anova import anova_lm 
```

As one of the import statements above is quite a long line, we inserted a line break \ to ease readability.

We will also use some functions written for the labs in this book in the ISLP package.

In [4]:   
```python
from ISLP import load_data
from ISLP.models import (ModelSpec as MS, summarize, poly) 
```

# Inspecting Objects and Namespaces

The function dir() provides a list of objects in a namespace.

dir()

In [5]:   
```txt
dir() 
```

```python
Out[5]: ['In',
    'MS',
    '_, 
    '_, 
    '_, 
    '_, 
    '__builtin_', 
    '__builtins_', 
    ... 
```

```txt
'poly',
'quit',
'sm',
'summarize'] 
```

This shows you everything that Python can find at the top level. There are certain objects like \_\_builtins\_\_ that contain references to built-in functions like print().

Every python object has its own notion of namespace, also accessible with dir(). This will include both the attributes of the object as well as any methods associated with it. For instance, we see 'sum' in the listing for an array.

```txt
In [6]: A = np.array([3,5,11])
dir(A) 
```

```txt
Out[6]: ...
'strides',
'sum',
'swapaxes',
... 
```

This indicates that the object A.sum exists. In this case it is a method that can be used to compute the sum of the array A as can be seen by typing A.sum?.

```txt
In [7]: A. sum() 
```

```txt
Out [7]: 19 
```

# 3.6.2 Simple Linear Regression

In this section we will construct model matrices (also called design matrices) using the ModelSpec() transform from ISLP.models.

We will use the Boston housing data set, which is contained in the ISLP package. The Boston dataset records medv (median house value) for 506 neighborhoods around Boston. We will build a regression model to predict medv using 13 predictors such as rmvar (average number of rooms per house), age (proportion of owner-occupied units built prior to 1940), and lstat (percent of households with low socioeconomic status). We will use statsmodels for this task, a Python package that implements several commonly used regression methods.

We have included a simple loading function load\_data() in the ISLP package:

load\_data()

```python
In [8]: Boston = load_data("Boston")
Boston.columns 
```

```javascript
Out[8]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv'], dtype='object') 
```

Type Boston? to find out more about these data.

We start by using the sm.OLS() function to fit a simple linear regression model. Our response will be medv and lstat will be the single predictor. For this model, we can create the model matrix by hand.

```python
In [9]: X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]), 'lstat': Boston['lstat']} X[:4] 
```

```csv
Out[9]: intercept lstat
0 1.0 4.98
1 1.0 9.14
2 1.0 4.03
3 1.0 2.94 
```

We extract the response, and fit the model.

```python
In [10]: y = Boston['medv']
model = sm.OLS(y, X)
results = model.fit() 
```

Note that sm.OLS() does not fit the model; it specifies the model, and then model.fit() does the actual fitting.

Our ISLP function summarize() produces a simple table of the parameter estimates, their standard errors, t-statistics and p-values. The function takes a single argument, such as the object results returned here by the fit method, and returns such a summary.

summarize()

```txt
In [11]: summarize(results) 
```

```txt
Out[11]: coef std err t P>|t|
intercept 34.5538 0.563 61.415 0.0
lstat -0.9500 0.039 -24.528 0.0 
```

Before we describe other methods for working with fitted models, we outline a more useful and general framework for constructing a model matrix X.

# Using Transformations: Fit and Transform

Our model above has a single predictor, and constructing x was straightforward. In practice we often fit models with more than one predictor, typically selected from an array or data frame. We may wish to introduce transformations to the variables before fitting the model, specify interactions between variables, and expand some particular variables into sets of variables (e.g. polynomials). The sklearn package has a particular notion for this type of task: a transform. A transform is an object that is created with some parameters as arguments. The object has two main methods: fit() and transform().

We provide a general approach for specifying models and constructing the model matrix through the transform ModelSpec() in the ISLP library. ModelSpec() (renamed MS() in the preamble) creates a transform object, and then a pair of methods transform() and fit() are used to construct a corresponding model matrix.

sklearn

.fit()

.transform()

ModelSpec()

We first describe this process for our simple regression model using a single predictor lstat in the Boston data frame, but will use it repeatedly in more complex tasks in this and other labs in this book. In our case the transform is created by the expression design = MS(['lstat']).

The fit() method takes the original array and may do some initial computations on it, as specified in the transform object. For example, it may compute means and standard deviations for centering and scaling. The transform() method applies the fitted transformation to the array of data, and produces the model matrix.

```python
In [12]: design = MS(['lstat'])
design = design.fit(Boston)
X = design.transform(Boston)
X[:4] 
```

```csv
Out[12]: intercept lstat
0 1.0 4.98
1 1.0 9.14
2 1.0 4.03
3 1.0 2.94 
```

In this simple case, the fit() method does very little; it simply checks that the variable 'lstat' specified in design exists in Boston. Then transform() constructs the model matrix with two columns: an intercept and the variable lstat.

These two operations can be combined with the fit\_transform() method.

```python
In [13]: design = MS(['lstat'])
X = design.fit_transform(Boston)
X[:4] 
```

.fit\_ transform()

```csv
Out[13]: intercept lstat
0 1.0 4.98
1 1.0 9.14
2 1.0 4.03
3 1.0 2.94 
```

Note that, as in the previous code chunk when the two steps were done separately, the design object is changed as a result of the fit() operation. The power of this pipeline will become clearer when we fit more complex models that involve interactions and transformations.

Let's return to our fitted regression model. The object results has several methods that can be used for inference. We already presented a function summarize() for showing the essentials of the fit. For a full and somewhat exhaustive summary of the fit, we can use the summary() method (output not shown).

```javascript
In [14]: results.summary() 
```

The fitted coefficients can also be retrieved as the params attribute of results.

```txt
In [15]: results.params 
```

```txt
Out[15]: intercept 34.553841
lstat -0.950049
dtype: float64 
```

The get\_prediction() method can be used to obtain predictions, and produce confidence intervals and prediction intervals for the prediction of medv for given values of lstat.

.get\_ prediction()

We first create a new data frame, in this case containing only the variable lstat, with the values for this variable at which we wish to make predictions. We then use the transform() method of design to create the corresponding model matrix.

```python
In [16]: new_df = pd.DataFrame({'lstat': [5, 10, 15]})
newX = design.transform(new_df)
newX 
```

```asm
Out[16]: intercept lstat
0 1.0 5
1 1.0 10
2 1.0 15 
```

Next we compute the predictions at newX, and view them by extracting the predicted\_mean attribute.

```txt
In [17]: new_predictions = results.get_prediction(newX);
new_predictions.predicted_mean 
```

```txt
Out[17]: array([29.80359411, 25.05334734, 20.30310057]) 
```

We can produce confidence intervals for the predicted values.

```txt
In [18]: new_predictions.conf_int(alpha=0.05) 
```

```javascript
Out[18]: array([[29.00741194, 30.59977628], [24.47413202, 25.63256267], [19.73158815, 20.87461299]]) 
```

Prediction intervals are computing by setting obs=True:

```txt
In [19]: new_predictions.conf_int(obs=True, alpha=0.05) 
```

```txt
Out[19]: array([[17.56567478, 42.04151344], [12.82762635, 37.27906833], [8.0777421, 32.52845905]]) 
```

For instance, the 95% confidence interval associated with an lstat value of 10 is (24.47, 25.63), and the 95% prediction interval is (12.82, 37.28). As expected, the confidence and prediction intervals are centered around the same point (a predicted value of 25.05 for medv when lstat equals 10), but the latter are substantially wider.

Next we will plot medv and lstat using DataFrame.plot.scatter(), and wish to add the regression line to the resulting plot.

.plot.
scatter()

# Defining Functions

While there is a function within the ISLP package that adds a line to an existing plot, we take this opportunity to define our first function to do so.

def

In [20]:

```python
def abline(ax, b, m):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim) 
```

A few things are illustrated above. First we see the syntax for defining a function: def funcname(...). The function has arguments ax, b, m where ax is an axis object for an existing plot, b is the intercept and m is the slope of the desired line. Other plotting options can be passed on to ax.plot by including additional optional arguments as follows:

In [21]:

```python
def abline(ax, b, m, *args, **kwargs):
    "Add a line with slope m and intercept b to ax"
    xlim = ax.get_xlim()
    ylim = [m * xlim[0] + b, m * xlim[1] + b]
    ax.plot(xlim, ylim, *args, **kwargs) 
```

The addition of \*args allows any number of non-named arguments to abline, while \*kwargs allows any number of named arguments (such as linewidth=3) to abline. In our function, we pass these arguments verbatim to ax.plot above. Readers interested in learning more about functions are referred to the section on defining functions in docs.python.org/tutorial.

Let's use our new function to add this regression line to a plot of medv vs. lstat.

In [22]:

```python
ax = Boston.plot.scatter('lstat', 'medv')
abline(ax,
    results.params[0],
    results.params[1],
    'r--',
    linewidth=3) 
```

Thus, the final call to ax.plot() is ax.plot(xlim, ylim, 'r--', linewidth=3). We have used the argument 'r--' to produce a red dashed line, and added an argument to make it of width 3. There is some evidence for non-linearity in the relationship between lstat and medv. We will explore this issue later in this lab.

As mentioned above, there is an existing function to add a line to a plot — ax.axline() — but knowing how to write such functions empowers us to create more expressive displays.

Next we examine some diagnostic plots, several of which were discussed in Section 3.3.3. We can find the fitted values and residuals of the fit as attributes of the results object. Various influence measures describing the regression model are computed with the get\_influence() method. As we will not use the fig component returned as the first value from subplots(), we simply capture the second returned value in ax below.

.get\_ influence()

In [23]:

```javascript
ax = subplots(figsize=(8,8))[1] 
```

```txt
ax.scatter(results.fittedvalues, results.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--'); 
```

We add a horizontal line at 0 for reference using the ax.axhline() method, indicating it should be black (c='k') and have a dashed linestyle (ls='--').

On the basis of the residual plot (not shown), there is some evidence of non-linearity. Leverage statistics can be computed for any number of predictors using the hat\_matrix\_diag attribute of the value returned by the get\_influence() method.

.axhline()

In [24]:

```python
infl = results.get_influence()
ax = subplots(figsize=(8,8))[1]
ax.scatter(np.arange(X.shape[0]), infl.hat_matrix_diag)
ax.set_xlabel('Index')
ax.set_ylabel('Leverage')
np.argmax(infl.hat_matrix_diag) 
```

Out [24]: 374

The np.argmax() function identifies the index of the largest element of an array, optionally computed over an axis of the array. In this case, we maximized over the entire array to determine which observation has the largest leverage statistic.

np.argmax()

# 3.6.3 Multiple Linear Regression

In order to fit a multiple linear regression model using least squares, we again use the ModelSpec() transform to construct the required model matrix and response. The arguments to ModelSpec() can be quite general, but in this case a list of column names suffice. We consider a fit here with the two variables lstat and age.

In [25]:

```matlab
X = MS(['lstat', 'age']).fit_transform(Boston)
model1 = sm.OLS(y, X)
results1 = model1.fit()
summarize(results1) 
```

Out [25]:

```batch
coef std err t P>|t|
intercept 33.2228 0.731 45.458 0.000
lstat -1.0321 0.048 -21.416 0.000
age 0.0345 0.012 2.826 0.005 
```

Notice how we have compacted the first line into a succinct expression describing the construction of x.

The Boston data set contains 12 variables, and so it would be cumbersome to have to type all of these in order to perform a regression using all of the predictors. Instead, we can use the following short-hand:

.columns.
drop()

In [26]:

```txt
terms = Boston.columns.drop('medv')
terms 
```

```javascript
Out[26]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'lstat'], dtype='object') 
```

We can now fit the model with all the variables in terms using the same model matrix builder.

```txt
In [27]: X = MS(terms).fit_transform(Boston)
model = sm.OLS(y, X)
results = model.fit()
summarize(results) 
```

```txt
Out[27]: coef std err t P>|t|
intercept 41.6173 4.936 8.431 0.000
crim -0.1214 0.033 -3.678 0.000
zn 0.0470 0.014 3.384 0.001
indus 0.0135 0.062 0.217 0.829
chas 2.8400 0.870 3.264 0.001
nox -18.7580 3.851 -4.870 0.000
rm 3.6581 0.420 8.705 0.000
age 0.0036 0.013 0.271 0.787
dis -1.4908 0.202 -7.394 0.000
rad 0.2894 0.067 4.325 0.000
tax -0.0127 0.004 -3.337 0.001
ptratio -0.9375 0.132 -7.091 0.000
lstat -0.5520 0.051 -10.897 0.000 
```

What if we would like to perform a regression using all of the variables but one? For example, in the above regression output, age has a high p-value. So we may wish to run a regression excluding this predictor. The following syntax results in a regression using all predictors except age (output not shown).

```python
In [28]: minus_age = Boston.columns.drop(['medv', 'age'])
Xma = MS(minus_age).fit_transform(Boston)
model1 = sm.OLS(y, Xma)
summarize(model1.fit()) 
```

# 3.6.4 Multivariate Goodness of Fit

We can access the individual components of results by name (dir(results) shows us what is available). Hence results.rsquared gives us the $R^{2}$ , and np.sqrt(results.scale) gives us the RSE.

Variance inflation factors (section 3.3.3) are sometimes useful to assess the effect of collinearity in the model matrix of a regression model. We will compute the VIFs in our multiple regression fit, and use the opportunity to introduce the idea of list comprehension.

list comprehension

# List Comprehension

Often we encounter a sequence of objects which we would like to transform for some other task. Below, we compute the VIF for each feature in our x matrix and produce a data frame whose index agrees with the columns of x. The notion of list comprehension can often make such a task easier.

List comprehensions are simple and powerful ways to form lists of Python objects. The language also supports dictionary and generator comprehension, though these are beyond our scope here. Let's look at an example. We compute the VIF for each of the variables in the model matrix X, using the function variance\_inflation\_factor().

In [29]:   
```python
vals = [VIF(X, i)
    for i in range(1, X.shape[1])]
vif = pd.DataFrame({'vif':vals},
    index=X.columns[1:])
vif 
```  
variance\_inflation\_factor()

```csv
Out[29]: vif
crim 1.767
zn 2.298
indus 3.987
chas 1.071
nox 4.369
rm 1.913
age 3.088
dis 3.954
rad 7.445
tax 9.002
ptratio 1.797
lstat 2.871 
```

The function VIF() takes two arguments: a dataframe or array, and a variable column index. In the code above we call VIF() on the fly for all columns in x. We have excluded column 0 above (the intercept), which is not of interest. In this case the VIFs are not that exciting.

The object vals above could have been constructed with the following for loop:

In [30]:   
```python
vals = []
for i in range(1, X.values.shape[1]):
    vals.append(VIF(X.values, i)) 
```

List comprehension allows us to perform such repetitive operations in a more straightforward way.

# 3.6.5 Interaction Terms

It is easy to include interaction terms in a linear model using ModelSpec(). Including a tuple ("lstat", "age") tells the model matrix builder to include an interaction term between lstat and age.

In [31]:   
```python
X = MS(['lstat', 'age', ('lstat', 'age')]).fit_transform(Boston)
model2 = sm.OLS(y, X)
summarize(model2.fit()) 
```

Out [31]:   
```txt
coef std err t P>|t|
intercept 36.0885 1.470 24.553 0.000
lstat -1.3921 0.167 -8.313 0.000 
```

<table><tr><td>age</td><td>-0.0007</td><td>0.020</td><td>-0.036</td><td>0.971</td></tr><tr><td>lstat:age</td><td>0.0042</td><td>0.002</td><td>2.244</td><td>0.025</td></tr></table>

# 3.6.6 Non-linear Transformations of the Predictors

The model matrix builder can include terms beyond just column names and interactions. For instance, the poly() function supplied in ISLP specifies that columns representing polynomial functions of its first argument are added to the model matrix.

poly()

```python
In [32]: X = MS([poly('lstat', degree=2), 'age']).fit_transform(Boston)
model3 = sm.OLS(y, X)
results3 = model3.fit()
summarize(results3) 
```

```txt
Out[32]: coef std err t P>|t|
intercept 17.7151 0.781 22.681 0.000
poly(lstat, degree=2)[0] -179.2279 6.733 -26.620 0.000
poly(lstat, degree=2)[1] 72.9908 5.482 13.315 0.000
age 0.0703 0.011 6.471 0.000 
```

The effectively zero $p$ -value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model.

By default, poly() creates a basis matrix for inclusion in the model matrix whose columns are orthogonal polynomials, which are designed for stable least squares computations. $^{13}$ Alternatively, had we included an argument raw=True in the above call to poly(), the basis matrix would consist simply of lstat and lstat\*\*2. Since either of these bases represent quadratic polynomials, the fitted values would not change in this case, just the polynomial coefficients. Also by default, the columns created by poly() do not include an intercept column as that is automatically added by MS().

We use the anova\_lm() function to further quantify the extent to which the quadratic fit is superior to the linear fit.

orthogonal
polynomial

anova\_lm()

```txt
In [33]: anova_lm(results1, results3) 
```

```csv
Out[33]: df_resid ssr df_diff ss_diff F Pr(>F)
0 503.0 19168.13 0.0 NaN NaN NaN
1 502.0 14165.61 1.0 5002.52 177.28 7.47e-35 
```

Here results1 represents the linear submodel containing predictors lstat and age, while results3 corresponds to the larger model above with a quadratic term in lstat. The anova\_lm() function performs a hypothesis test comparing the two models. The null hypothesis is that the quadratic term in the bigger model is not needed, and the alternative hypothesis is that the bigger model is superior. Here the $F$ -statistic is 177.28 and the associated $p$ -value is zero. In this case the $F$ -statistic is the square of the $t$ -statistic for the quadratic term in the linear model summary for results3 — a consequence of the fact that these nested models differ by one degree of freedom. This provides very clear evidence that the quadratic polynomial in lstat improves the linear model. This is not surprising, since earlier we saw evidence for non-linearity in the relationship between medv and lstat.

The function anova\_lm() can take more than two nested models as input, in which case it compares every successive pair of models. That also explains why their are NaNs in the first row above, since there is no previous model with which to compare the first.

```txt
In [34]: ax = subplots(figsize=(8,8))[1]
ax.scatter(results3.fittedvalues, results3.resid)
ax.set_xlabel('Fitted value')
ax.set_ylabel('Residual')
ax.axhline(0, c='k', ls='--') 
```

We see that when the quadratic term is included in the model, there is little discernible pattern in the residuals. In order to create a cubic or higher-degree polynomial fit, we can simply change the degree argument to poly().

# 3.6.7 Qualitative Predictors

Here we use the Carseats data, which is included in the ISLP package. We will attempt to predict Sales (child car seat sales) in 400 locations based on a number of predictors.

```python
In [35]: Carseats = load_data('Carseats')
Carseats.columns 
```

```javascript
Out[35]: Index(['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'ShelveLoc', 'Age', 'Education', 'Urban', 'US'], dtype='object') 
```

The Carseats data includes qualitative predictors such as ShelveLoc, an indicator of the quality of the shelving location — that is, the space within a store in which the car seat is displayed. The predictor ShelveLoc takes on three possible values, Bad, Medium, and Good. Given a qualitative variable such as ShelveLoc, ModelSpec() generates dummy variables automatically. These variables are often referred to as a one-hot encoding of the categorical feature. Their columns sum to one, so to avoid collinearity with an intercept, the first column is dropped. Below we see the column ShelveLoc[Bad] has been dropped, since Bad is the first level of ShelveLoc. Below we fit a multiple regression model that includes some interaction terms.

```txt
In [36]: allvars = list(Carseats.columns.drop('Sales'))
y = Carseats['Sales']
final = allvars + [('Income', 'Advertising'),
    ('Price', 'Age')]
X = MS(final).fit_transform(Carseats)
model = sm.OLS(y, X)
summarize(model.fit()) 
```

```txt
Out [36]: coef std err t P>|t|
intercept 6.5756 1.009 6.519 0.000 
```

<table><tr><td>CompPrice</td><td>0.0929</td><td>0.004</td><td>22.567</td><td>0.000</td></tr><tr><td>Income</td><td>0.0109</td><td>0.003</td><td>4.183</td><td>0.000</td></tr><tr><td>Advertising</td><td>0.0702</td><td>0.023</td><td>3.107</td><td>0.002</td></tr><tr><td>Population</td><td>0.0002</td><td>0.000</td><td>0.433</td><td>0.665</td></tr><tr><td>Price</td><td>-0.1008</td><td>0.007</td><td>-13.549</td><td>0.000</td></tr><tr><td>ShelveLoc[Good]</td><td>4.8487</td><td>0.153</td><td>31.724</td><td>0.000</td></tr><tr><td>ShelveLoc[Medium]</td><td>1.9533</td><td>0.126</td><td>15.531</td><td>0.000</td></tr><tr><td>Age</td><td>-0.0579</td><td>0.016</td><td>-3.633</td><td>0.000</td></tr><tr><td>Education</td><td>-0.0209</td><td>0.020</td><td>-1.063</td><td>0.288</td></tr><tr><td>Urban[Yes]</td><td>0.1402</td><td>0.112</td><td>1.247</td><td>0.213</td></tr><tr><td>US[Yes]</td><td>-0.1576</td><td>0.149</td><td>-1.058</td><td>0.291</td></tr><tr><td>Income:Advertising</td><td>0.0008</td><td>0.000</td><td>2.698</td><td>0.007</td></tr><tr><td>Price:Age</td><td>0.0001</td><td>0.000</td><td>0.801</td><td>0.424</td></tr></table>

In the first line above, we made allvars a list, so that we could add the interaction terms two lines down. Our model-matrix builder has created a ShelveLoc[Good] dummy variable that takes on a value of 1 if the shelving location is good, and 0 otherwise. It has also created a ShelveLoc[Medium] dummy variable that equals 1 if the shelving location is medium, and 0 otherwise. A bad shelving location corresponds to a zero for each of the two dummy variables. The fact that the coefficient for ShelveLoc[Good] in the regression output is positive indicates that a good shelving location is associated with high sales (relative to a bad location). And ShelveLoc[Medium] has a smaller positive coefficient, indicating that a medium shelving location leads to higher sales than a bad shelving location, but lower sales than a good shelving location.

# 3.7 Exercises

# Conceptual

1. Describe the null hypotheses to which the p-values given in Table 3.4 correspond. Explain what conclusions you can draw based on these p-values. Your explanation should be phrased in terms of sales, TV, radio, and newspaper, rather than in terms of the coefficients of the linear model.   
2. Carefully explain the differences between the KNN classifier and KNN regression methods.   
3. Suppose we have a data set with five predictors, $X_{1} = GPA$ , $X_{2} = IQ$ , $X_{3} = Level$ (1 for College and 0 for High School), $X_{4} = Interaction$ between GPA and IQ, and $X_{5} = Interaction$ between GPA and Level. The response is starting salary after graduation (in thousands of dollars). Suppose we use least squares to fit the model, and get $\hat{\beta}_{0} = 50$ , $\hat{\beta}_{1} = 20$ , $\hat{\beta}_{2} = 0.07$ , $\hat{\beta}_{3} = 35$ , $\hat{\beta}_{4} = 0.01$ , $\hat{\beta}_{5} = -10$ .

(a) Which answer is correct, and why?

i. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates.

ii. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates.

iii. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates provided that the GPA is high enough.

iv. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates provided that the GPA is high enough.

(b) Predict the salary of a college graduate with IQ of 110 and a GPA of 4.0.

(c) True or false: Since the coefficient for the GPA/IQ interaction term is very small, there is very little evidence of an interaction effect. Justify your answer.

4. I collect a set of data ( $n = 100$ observations) containing a single predictor and a quantitative response. I then fit a linear regression model to the data, as well as a separate cubic regression, i.e. $Y = \beta_0 + \beta_1X + \beta_2X^2 + \beta_3X^3 + \epsilon$ .

(a) Suppose that the true relationship between X and Y is linear, i.e. $Y = \beta_{0} + \beta_{1}X + \epsilon$ . Consider the training residual sum of squares (RSS) for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer.

(b) Answer (a) using test rather than training RSS.

(c) Suppose that the true relationship between X and Y is not linear, but we don't know how far it is from linear. Consider the training RSS for the linear regression, and also the training RSS for the cubic regression. Would we expect one to be lower than the other, would we expect them to be the same, or is there not enough information to tell? Justify your answer.

(d) Answer (c) using test rather than training RSS.

5. Consider the fitted values that result from performing linear regression without an intercept. In this setting, the ith fitted value takes the form

$$
\hat {y} _ {i} = x _ {i} \hat {\beta},
$$

where

$$
\hat {\beta} = \left(\sum_ {i = 1} ^ {n} x _ {i} y _ {i}\right) / \left(\sum_ {i ^ {\prime} = 1} ^ {n} x _ {i ^ {\prime}} ^ {2}\right). \tag {3.38}
$$

Show that we can write

$$
\hat {y} _ {i} = \sum_ {i ^ {\prime} = 1} ^ {n} a _ {i ^ {\prime}} y _ {i ^ {\prime}}.
$$

What is $a_{i'}$ ?

Note: We interpret this result by saying that the fitted values from linear regression are linear combinations of the response values.

6. Using (3.4), argue that in the case of simple linear regression, the least squares line always passes through the point $(\bar{x}, \bar{y})$ .

7. It is claimed in the text that in the case of simple linear regression of $Y$ onto $X$ , the $R^2$ statistic (3.17) is equal to the square of the correlation between $X$ and $Y$ (3.18). Prove that this is the case. For simplicity, you may assume that $\bar{x} = \bar{y} = 0$ .

![](images/5fc20a94fa323e43a50dd472a5707c7df8b37fb9e4fd05e534683fdfb226041c.jpg)

# Applied

8. This question involves the use of simple linear regression on the Auto data set.

(a) Use the sm.OLS() function to perform a simple linear regression with mpg as the response and horsepower as the predictor. Use the summarize() function to print the results. Comment on the output. For example:

i. Is there a relationship between the predictor and the response?   
ii. How strong is the relationship between the predictor and the response?   
iii. Is the relationship between the predictor and the response positive or negative?   
iv. What is the predicted mpg associated with a horsepower of 98? What are the associated 95% confidence and prediction intervals?

(b) Plot the response and the predictor in a new set of axes ax. Use the ax.axline() method or the abline() function defined in the lab to display the least squares regression line.   
(c) Produce some of diagnostic plots of the least squares regression fit as described in the lab. Comment on any problems you see with the fit.

9. This question involves the use of multiple linear regression on the Auto data set.

(a) Produce a scatterplot matrix which includes all of the variables in the data set.

(b) Compute the matrix of correlations between the variables using the DataFrame.corr() method.

(c) Use the sm.OLS() function to perform a multiple linear regression with mpg as the response and all other variables except name as the predictors. Use the summarize() function to print the results. Comment on the output. For instance:

i. Is there a relationship between the predictors and the response? Use the anova\_lm() function from statsmodels to answer this question.

.corr()

ii. Which predictors appear to have a statistically significant relationship to the response?

iii. What does the coefficient for the year variable suggest?

(d) Produce some of diagnostic plots of the linear regression fit as described in the lab. Comment on any problems you see with the fit. Do the residual plots suggest any unusually large outliers?   
Does the leverage plot identify any observations with unusually high leverage?   
(e) Fit some models with interactions as described in the lab. Do any interactions appear to be statistically significant?   
(f) Try a few different transformations of the variables, such as $\log(X)$ , $\sqrt{X}$ , $X^2$ . Comment on your findings.

10. This question should be answered using the Carseats data set.

(a) Fit a multiple regression model to predict Sales using Price, Urban, and US.   
(b) Provide an interpretation of each coefficient in the model. Be careful—some of the variables in the model are qualitative!   
(c) Write out the model in equation form, being careful to handle the qualitative variables properly.   
(d) For which of the predictors can you reject the null hypothesis $H_0: \beta_j = 0$ ?   
(e) On the basis of your response to the previous question, fit a smaller model that only uses the predictors for which there is evidence of association with the outcome.   
(f) How well do the models in (a) and (e) fit the data?   
(g) Using the model from (e), obtain $95\%$ confidence intervals for the coefficient(s).   
(h) Is there evidence of outliers or high leverage observations in the model from (e)?

11. In this problem we will investigate the t-statistic for the null hypothesis $H_{0} : \beta = 0$ in simple linear regression without an intercept. To begin, we generate a predictor x and a response y as follows.

```python
rng = np.random.default_rng(1)
x = rng.normal(size=100)
y = 2 * x + rng.normal(size=100) 
```

(a) Perform a simple linear regression of y onto x, without an intercept. Report the coefficient estimate $\hat{\beta}$ , the standard error of this coefficient estimate, and the t-statistic and p-value associated with the null hypothesis $H_{0}: \beta = 0$ . Comment on these results. (You can perform regression without an intercept using the keywords argument intercept=False to ModelSpec().)

(b) Now perform a simple linear regression of x onto y without an intercept, and report the coefficient estimate, its standard error, and the corresponding t-statistic and p-values associated with the null hypothesis $H_{0} : \beta = 0$ . Comment on these results.   
(c) What is the relationship between the results obtained in (a) and (b)?   
(d) For the regression of $Y$ onto $X$ without an intercept, the $t$ -statistic for $H_0: \beta = 0$ takes the form $\hat{\beta} / \mathrm{SE}(\hat{\beta})$ , where $\hat{\beta}$ is given by (3.38), and where

$$
\mathrm{SE} (\hat {\beta}) = \sqrt {\frac {\sum_ {i = 1} ^ {n} (y _ {i} - x _ {i} \hat {\beta}) ^ {2}}{(n - 1) \sum_ {i ^ {\prime} = 1} ^ {n} x _ {i ^ {\prime}} ^ {2}}}.
$$

(These formulas are slightly different from those given in Sections 3.1.1 and 3.1.2, since here we are performing regression without an intercept.) Show algebraically, and confirm numerically in $\mathbb{R}$ , that the $t$ -statistic can be written as

$$
\frac {(\sqrt {n - 1}) \sum_ {i = 1} ^ {n} x _ {i} y _ {i}}{\sqrt {(\sum_ {i = 1} ^ {n} x _ {i} ^ {2}) (\sum_ {i ^ {\prime} = 1} ^ {n} y _ {i ^ {\prime}} ^ {2}) - (\sum_ {i ^ {\prime} = 1} ^ {n} x _ {i ^ {\prime}} y _ {i ^ {\prime}}) ^ {2}}}.
$$

(e) Using the results from (d), argue that the $t$ -statistic for the regression of $\mathbf{y}$ onto $\mathbf{x}$ is the same as the $t$ -statistic for the regression of $\mathbf{x}$ onto $\mathbf{y}$ .   
(f) In R, show that when regression is performed with an intercept, the t-statistic for $H_{0} : \beta_{1} = 0$ is the same for the regression of y onto x as it is for the regression of x onto y.

12. This problem involves simple linear regression without an intercept.

(a) Recall that the coefficient estimate $\hat{\beta}$ for the linear regression of $Y$ onto $X$ without an intercept is given by (3.38). Under what circumstance is the coefficient estimate for the regression of $X$ onto $Y$ the same as the coefficient estimate for the regression of $Y$ onto $X$ ?   
(b) Generate an example in Python with $n = 100$ observations in which the coefficient estimate for the regression of $X$ onto $Y$ is different from the coefficient estimate for the regression of $Y$ onto $X$ .   
(c) Generate an example in Python with $n = 100$ observations in which the coefficient estimate for the regression of $X$ onto $Y$ is the same as the coefficient estimate for the regression of $Y$ onto $X$ .

13. In this exercise you will create some simulated data and will fit simple linear regression models to it. Make sure to use the default random number generator with seed set to 1 prior to starting part (a) to ensure consistent results.

![](images/7d9251358226ed18095ed066f779609af254eaa04669433b9cc24fe60c7c5619.jpg)

(a) Using the normal() method of your random number generator, create a vector, x, containing 100 observations drawn from a $N(0,1)$ distribution. This represents a feature, X.   
(b) Using the normal() method, create a vector, eps, containing 100 observations drawn from a $N(0,0.25)$ distribution—a normal distribution with mean zero and variance 0.25.   
(c) Using $\mathbf{x}$ and eps, generate a vector $\mathbf{y}$ according to the model

$$
Y = - 1 + 0. 5 X + \epsilon . \tag {3.39}
$$

What is the length of the vector $\mathbf{y}$ ? What are the values of $\beta_0$ and $\beta_{1}$ in this linear model?

(d) Create a scatterplot displaying the relationship between $\mathbf{x}$ and $\mathbf{y}$ . Comment on what you observe.   
(e) Fit a least squares linear model to predict y using x. Comment on the model obtained. How do $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ compare to $\beta_{0}$ and $\beta_{1}$ ?   
(f) Display the least squares line on the scatterplot obtained in (d). Draw the population regression line on the plot, in a different color. Use the legend() method of the axes to create an appropriate legend.   
(g) Now fit a polynomial regression model that predicts y using x and $x^{2}$ . Is there evidence that the quadratic term improves the model fit? Explain your answer.   
(h) Repeat (a)-(f) after modifying the data generation process in such a way that there is less noise in the data. The model (3.39) should remain the same. You can do this by decreasing the variance of the normal distribution used to generate the error term $\epsilon$ in (b). Describe your results.   
(i) Repeat (a)-(f) after modifying the data generation process in such a way that there is more noise in the data. The model (3.39) should remain the same. You can do this by increasing the variance of the normal distribution used to generate the error term $\epsilon$ in (b). Describe your results.   
(j) What are the confidence intervals for $\beta_{0}$ and $\beta_{1}$ based on the original data set, the noisier data set, and the less noisy data set? Comment on your results.

14. This problem focuses on the collinearity problem.

(a) Perform the following commands in Python:

```python
rng = np.random.default_rng(10)
x1 = rng.uniform(0, 1, size=100)
x2 = 0.5 * x1 + rng.normal(size=100) / 10
y = 2 + 2 * x1 + 0.3 * x2 + rng.normal(size=100) 
```

The last line corresponds to creating a linear model in which y is a function of x1 and x2. Write out the form of the linear model. What are the regression coefficients?

(b) What is the correlation between $\mathbf{x1}$ and $\mathbf{x2}$ ? Create a scatterplot displaying the relationship between the variables.   
(c) Using this data, fit a least squares regression to predict y using x1 and x2. Describe the results obtained. What are $\hat{\beta}_{0}$ , $\hat{\beta}_{1}$ , and $\hat{\beta}_{2}$ ? How do these relate to the true $\beta_{0}$ , $\beta_{1}$ , and $\beta_{2}$ ? Can you reject the null hypothesis $H_{0}: \beta_{1} = 0$ ? How about the null hypothesis $H_{0}: \beta_{2} = 0$ ?   
(d) Now fit a least squares regression to predict y using only x1. Comment on your results. Can you reject the null hypothesis $H_{0}:\beta_{1}=0?$   
(e) Now fit a least squares regression to predict y using only x2. Comment on your results. Can you reject the null hypothesis $H_{0}:\beta_{1}=0?$   
(f) Do the results obtained in (c)-(e) contradict each other? Explain your answer.   
(g) Suppose we obtain one additional observation, which was unfortunately mismeasured. We use the function np.concatenate() to add this additional observation to each of x1, x2 and y.

np.conca-
tenate()

```txt
x1 = np.concatenate([x1, [0.1]])
x2 = np.concatenate([x2, [0.8]])
y = np.concatenate([y, [6]]) 
```

Re-fit the linear models from (c) to (e) using this new data. What effect does this new observation have on the each of the models? In each model, is this observation an outlier? A high-leverage point? Both? Explain your answers.

15. This problem involves the Boston data set, which we saw in the lab for this chapter. We will now try to predict per capita crime rate using the other variables in this data set. In other words, per capita crime rate is the response, and the other variables are the predictors.

(a) For each predictor, fit a simple linear regression model to predict the response. Describe your results. In which of the models is there a statistically significant association between the predictor and the response? Create some plots to back up your assertions.   
(b) Fit a multiple regression model to predict the response using all of the predictors. Describe your results. For which predictors can we reject the null hypothesis $H_0: \beta_j = 0$ ?   
(c) How do your results from (a) compare to your results from (b)? Create a plot displaying the univariate regression coefficients from (a) on the $x$ -axis, and the multiple regression coefficients from (b) on the $y$ -axis. That is, each predictor is displayed as a single point in the plot. Its coefficient in a simple linear regression model is shown on the $x$ -axis, and its coefficient estimate in the multiple linear regression model is shown on the $y$ -axis.

(d) Is there evidence of non-linear association between any of the predictors and the response? To answer this question, for each predictor $X$ , fit a model of the form

$$
Y = \beta_ {0} + \beta_ {1} X + \beta_ {2} X ^ {2} + \beta_ {3} X ^ {3} + \epsilon .
$$

The linear regression model discussed in Chapter 3 assumes that the response variable Y is quantitative. But in many situations, the response variable is instead qualitative. For example, eye color is qualitative. Often qualitative variables are referred to as categorical; we will use these terms interchangeably. In this chapter, we study approaches for predicting qualitative responses, a process that is known as classification. Predicting a qualitative response for an observation can be referred to as classifying that observation, since it involves assigning the observation to a category, or class. On the other hand, often the methods used for classification first predict the probability that the observation belongs to each of the categories of a qualitative variable, as the basis for making the classification. In this sense they also behave like regression methods.

There are many possible classification techniques, or classifiers, that one might use to predict a qualitative response. We touched on some of these in Sections 2.1.5 and 2.2.3. In this chapter we discuss some widely-used classifiers: logistic regression, linear discriminant analysis, quadratic discriminant analysis, naive Bayes, and K-nearest neighbors. The discussion of logistic regression is used as a jumping-off point for a discussion of generalized linear models, and in particular, Poisson regression. We discuss more computer-intensive classification methods in later chapters: these include generalized additive models (Chapter 7); trees, random forests, and boosting (Chapter 8); and support vector machines (Chapter 9).

# 4.1 An Overview of Classification

Classification problems occur often, perhaps even more so than regression problems. Some examples include:

qualitative

classification

classifier

logistic
regression
linear
discriminant
analysis
quadratic
discriminant
analysis
naive Bayes
K-nearest
neighbors
generalized
linear
models
Poisson
regression

1. A person arrives at the emergency room with a set of symptoms that could possibly be attributed to one of three medical conditions. Which of the three conditions does the individual have?

2. An online banking service must be able to determine whether or not a transaction being performed on the site is fraudulent, on the basis of the user's IP address, past transaction history, and so forth.

3. On the basis of DNA sequence data for a number of patients with and without a given disease, a biologist would like to figure out which DNA mutations are deleterious (disease-causing) and which are not.

Just as in the regression setting, in the classification setting we have a set of training observations $(x_{1}, y_{1}), \ldots, (x_{n}, y_{n})$ that we can use to build a classifier. We want our classifier to perform well not only on the training data, but also on test observations that were not used to train the classifier.

In this chapter, we will illustrate the concept of classification using the simulated Default data set. We are interested in predicting whether an individual will default on his or her credit card payment, on the basis of annual income and monthly credit card balance. The data set is displayed in Figure 4.1. In the left-hand panel of Figure 4.1, we have plotted annual income and monthly credit card balance for a subset of 10,000 individuals. The individuals who defaulted in a given month are shown in orange, and those who did not in blue. (The overall default rate is about $3\%$ , so we have plotted only a fraction of the individuals who did not default.) It appears that individuals who defaulted tended to have higher credit card balances than those who did not. In the center and right-hand panels of Figure 4.1, two pairs of boxplots are shown. The first shows the distribution of balance split by the binary default variable; the second is a similar plot for income. In this chapter, we learn how to build a model to predict default $(Y)$ for any given value of balance $(X_{1})$ and income $(X_{2})$ . Since $Y$ is not quantitative, the simple linear regression model of Chapter 3 is not a good choice: we will elaborate on this further in Section 4.2.

It is worth noting that Figure 4.1 displays a very pronounced relationship between the predictor balance and the response default. In most real applications, the relationship between the predictor and the response will not be nearly so strong. However, for the sake of illustrating the classification procedures discussed in this chapter, we use an example in which the relationship between the predictor and the response is somewhat exaggerated.

# 4.2 Why Not Linear Regression?

We have stated that linear regression is not appropriate in the case of a qualitative response. Why not?

Suppose that we are trying to predict the medical condition of a patient in the emergency room on the basis of her symptoms. In this simplified example, there are three possible diagnoses: stroke, drug overdose, and epileptic seizure. We could consider encoding these values as a quantitative response variable, Y, as follows:

![](images/2cea0a45c0a29e167f0ab615359d090d4a6cf6ec861405185b0b84a92bc91f43.jpg)

<details>
<summary>scatter</summary>

| Balance | Income | Group |
| ------- | ------ | ----- |
| 0       | 60000  | Blue  |
| 500     | 40000  | Blue  |
| 1000    | 20000  | Blue  |
| 1500    | 10000  | Orange|
| 2000    | 5000   | Orange|
| 2500    | 2000   | Orange|
</details>

![](images/83f693a720d5d8ce115bb330e447b2990e9ea7742c49e6315d4b7ed4959d9edf.jpg)

<details>
<summary>boxplot</summary>

| Default | Balance |
| ------- | ------- |
| No      | 0       |
| Yes     | 1000    |
| Yes     | 2000    |
| Yes     | 2500    |
</details>

![](images/8c24d7b57f87841a5d71aa49d0d7d43ef06c9e714cca8ab04d7aabb8b22fa8cb.jpg)

<details>
<summary>boxplot</summary>

| Default | Income (Min) | Income (Q1) | Income (Max) |
| ------- | ------------ | ----------- | ------------ |
| No      | 0            | 20000       | 45000        |
| Yes     | 10000        | 30000       | 45000        |
</details>

FIGURE 4.1. The Default data set. Left: The annual incomes and monthly credit card balances of a number of individuals. The individuals who defaulted on their credit card payments are shown in orange, and those who did not are shown in blue. Center: Boxplots of balance as a function of default status. Right: Boxplots of income as a function of default status.

$$
Y = \left\{ \begin{array}{l l} 1 & \text { if   stroke; } \\ 2 & \text { if   drug   overdose; } \\ 3 & \text { if   epileptic   seizure. } \end{array} \right.
$$

Using this coding, least squares could be used to fit a linear regression model to predict Y on the basis of a set of predictors $X_{1},\ldots,X_{p}$ . Unfortunately, this coding implies an ordering on the outcomes, putting drug overdose in between stroke and epileptic seizure, and insisting that the difference between stroke and drug overdose is the same as the difference between drug overdose and epileptic seizure. In practice there is no particular reason that this needs to be the case. For instance, one could choose an equally reasonable coding,

$$
Y = \left\{ \begin{array}{l l} 1 & \text { if   epileptic   seizure; } \\ 2 & \text { if   stroke; } \\ 3 & \text { if   drug   overdose, } \end{array} \right.
$$

which would imply a totally different relationship among the three conditions. Each of these codings would produce fundamentally different linear models that would ultimately lead to different sets of predictions on test observations.

If the response variable's values did take on a natural ordering, such as mild, moderate, and severe, and we felt the gap between mild and moderate was similar to the gap between moderate and severe, then a 1, 2, 3 coding would be reasonable. Unfortunately, in general there is no natural way to convert a qualitative response variable with more than two levels into a quantitative response that is ready for linear regression.

For a binary (two level) qualitative response, the situation is better. For instance, perhaps there are only two possibilities for the patient's medical condition: stroke and drug overdose. We could then potentially use the dummy variable approach from Section 3.3.1 to code the response as follows:

$$
Y = \left\{ \begin{array}{l l} 0 & \text { if   stroke; } \\ 1 & \text { if   drug   overdose. } \end{array} \right.
$$

binary

We could then fit a linear regression to this binary response, and predict drug overdose if $\hat{Y} > 0.5$ and stroke otherwise. In the binary case it is not hard to show that even if we flip the above coding, linear regression will produce the same final predictions.

For a binary response with a 0/1 coding as above, regression by least squares is not completely unreasonable: it can be shown that the $X\hat{\beta}$ obtained using linear regression is in fact an estimate of $\Pr(\text{drug overdose}|X)$ in this special case. However, if we use linear regression, some of our estimates might be outside the [0, 1] interval (see Figure 4.2), making them hard to interpret as probabilities! Nevertheless, the predictions provide an ordering and can be interpreted as crude probability estimates. Curiously, it turns out that the classifications that we get if we use linear regression to predict a binary response will be the same as for the linear discriminant analysis (LDA) procedure we discuss in Section 4.4.

To summarize, there are at least two reasons not to perform classification using a regression method: (a) a regression method cannot accommodate a qualitative response with more than two classes; (b) a regression method will not provide meaningful estimates of $\Pr(Y|X)$ , even with just two classes. Thus, it is preferable to use a classification method that is truly suited for qualitative response values. In the next section, we present logistic regression, which is well-suited for the case of a binary qualitative response; in later sections we will cover classification methods that are appropriate when the qualitative response has two or more classes.

# 4.3 Logistic Regression

Consider again the Default data set, where the response default falls into one of two categories, Yes or No. Rather than modeling this response Y directly, logistic regression models the probability that Y belongs to a particular category.

For the Default data, logistic regression models the probability of default. For example, the probability of default given balance can be written as

$$
\operatorname * {P r} (\text { default } = \text { Yes } | \text { balance }).
$$

The values of $\Pr(\text{default} = \text{Yes}|\text{balance})$ , which we abbreviate $p(\text{balance})$ , will range between 0 and 1. Then for any given value of balance, a prediction can be made for default. For example, one might predict default = Yes for any individual for whom $p(\text{balance}) > 0.5$ . Alternatively, if a company wishes to be conservative in predicting individuals who are at risk for default, then they may choose to use a lower threshold, such as $p(\text{balance}) > 0.1$ .

![](images/01cef9bd25a2e2da89c60486a67519228ca8f9d40fd49a8e49026383d9527f8e.jpg)

<details>
<summary>line</summary>

| Balance | Probability of Default (Blue Line) | Probability of Default (Orange Dashed Line) |
| ------- | ---------------------------------- | ------------------------------------------ |
| 0       | ~0.0                               | 1.0                                        |
| 500     | ~0.05                              | 1.0                                        |
| 1000    | ~0.1                               | 1.0                                        |
| 1500    | ~0.15                              | 1.0                                        |
| 2000    | ~0.2                               | 1.0                                        |
| 2500    | ~0.25                              | 1.0                                        |
</details>

![](images/9af039110a64d83a97e344f1bd56fd0ce1c805a068ed05322ecb888b1bef4c8c.jpg)

<details>
<summary>line</summary>

| Balance | Probability of Default |
| ------- | ---------------------- |
| 0       | 0.0                    |
| 500     | 0.0                    |
| 1000    | 0.0                    |
| 1500    | 0.2                    |
| 2000    | 0.8                    |
| 2500    | 1.0                    |
</details>

FIGURE 4.2. Classification using the Default data. Left: Estimated probability of default using linear regression. Some estimated probabilities are negative! The orange ticks indicate the 0/1 values coded for default (No or Yes). Right: Predicted probabilities of default using logistic regression. All probabilities lie between 0 and 1.

# 4.3.1 The Logistic Model

How should we model the relationship between $p(X) = \Pr(Y = 1|X)$ and X? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent these probabilities:

$$
p (X) = \beta_ {0} + \beta_ {1} X. \tag {4.1}
$$

If we use this approach to predict default=Yes using balance, then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1. These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1. This problem is not unique to the credit default data. Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict $p(X) < 0$ for some values of X and $p(X) > 1$ for others (unless the range of X is limited).

To avoid this problem, we must model $p(X)$ using a function that gives outputs between 0 and 1 for all values of X. Many functions meet this description. In logistic regression, we use the logistic function,

$$
p (X) = \frac {e ^ {\beta_ {0} + \beta_ {1} X}}{1 + e ^ {\beta_ {0} + \beta_ {1} X}}. \tag {4.2}
$$

To fit the model $(4.2)$ , we use a method called maximum likelihood, which we discuss in the next section. The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the Default data. Notice that for

logistic function

maximum likelihood

low balances we now predict the probability of default as close to, but never below, zero. Likewise, for high balances we predict a default probability close to, but never above, one. The logistic function will always produce an S-shaped curve of this form, and so regardless of the value of X, we will obtain a sensible prediction. We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot. The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set.

After a bit of manipulation of (4.2), we find that

$$
\frac {p (X)}{1 - p (X)} = e ^ {\beta_ {0} + \beta_ {1} X}. \tag {4.3}
$$

The quantity $p(X)/[1-p(X)]$ is called the odds, and can take on any value between 0 and $\infty$ . Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively. For example, on average 1 in 5 people with an odds of 1/4 will default, since $p(X)=0.2$ implies an odds of $\frac{0.2}{1-0.2}=1/4$ . Likewise, on average nine out of every ten people with an odds of 9 will default, since $p(X)=0.9$ implies an odds of $\frac{0.9}{1-0.9}=9$ . Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy.

By taking the logarithm of both sides of $(4.3)$ , we arrive at

$$
\log \left(\frac {p (X)}{1 - p (X)}\right) = \beta_ {0} + \beta_ {1} X. \tag {4.4}
$$

The left-hand side is called the log odds or logit. We see that the logistic regression model (4.2) has a logit that is linear in $X$ .

Recall from Chapter 3 that in a linear regression model, $\beta_{1}$ gives the average change in Y associated with a one-unit increase in X. By contrast, in a logistic regression model, increasing X by one unit changes the log odds by $\beta_{1}$ (4.4). Equivalently, it multiplies the odds by $e^{\beta_{1}}$ (4.3). However, because the relationship between $p(X)$ and X in (4.2) is not a straight line, $\beta_{1}$ does not correspond to the change in $p(X)$ associated with a one-unit increase in X. The amount that $p(X)$ changes due to a one-unit change in X depends on the current value of X. But regardless of the value of X, if $\beta_{1}$ is positive then increasing X will be associated with increasing $p(X)$ , and if $\beta_{1}$ is negative then increasing X will be associated with decreasing $p(X)$ . The fact that there is not a straight-line relationship between $p(X)$ and X, and the fact that the rate of change in $p(X)$ per unit change in X depends on the current value of X, can also be seen by inspection of the right-hand panel of Figure 4.2.

# 4.3.2 Estimating the Regression Coefficients

The coefficients $\beta_{0}$ and $\beta_{1}$ in (4.2) are unknown, and must be estimated based on the available training data. In Chapter 3, we used the least squares approach to estimate the unknown linear regression coefficients. Although we could use (non-linear) least squares to fit the model (4.4), the more general method of maximum likelihood is preferred, since it has better statistical properties. The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: we seek estimates for $\beta_{0}$ and $\beta_{1}$ such that the predicted probability $\hat{p}(x_{i})$ of default for each individual, using (4.2), corresponds as closely as possible to the individual's observed default status. In other words, we try to find $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ such that plugging these estimates into the model for $p(X)$ , given in (4.2), yields a number close to one for all individuals who defaulted, and a number close to zero for all individuals who did not. This intuition can be formalized using a mathematical equation called a likelihood function:

$$
\ell (\beta_ {0}, \beta_ {1}) = \prod_ {i: y _ {i} = 1} p (x _ {i}) \prod_ {i ^ {\prime}: y _ {i ^ {\prime}} = 0} (1 - p (x _ {i ^ {\prime}})). \tag {4.5}
$$

likelihood function

The estimates $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ are chosen to maximize this likelihood function.

Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book. In the linear regression setting, the least squares approach is in fact a special case of maximum likelihood. The mathematical details of maximum likelihood are beyond the scope of this book. However, in general, logistic regression and other models can be easily fit using statistical software such as R, and so we do not need to concern ourselves with the details of the maximum likelihood fitting procedure.

Table 4.1 shows the coefficient estimates and related information that result from fitting a logistic regression model on the Default data in order to predict the probability of default=Yes using balance. We see that $\hat{\beta}_{1}=0.0055$ ; this indicates that an increase in balance is associated with an increase in the probability of default. To be precise, a one-unit increase in balance is associated with an increase in the log odds of default by 0.0055 units.

Many aspects of the logistic regression output shown in Table 4.1 are similar to the linear regression output of Chapter 3. For example, we can measure the accuracy of the coefficient estimates by computing their standard errors. The z-statistic in Table 4.1 plays the same role as the t-statistic in the linear regression output, for example in Table 3.1 on page 77. For instance, the z-statistic associated with $\beta_{1}$ is equal to $\hat{\beta}_{1}/\mathrm{SE}(\hat{\beta}_{1})$ , and so a large (absolute) value of the z-statistic indicates evidence against the null hypothesis $H_{0}: \beta_{1} = 0$ . This null hypothesis implies that $p(X) = \frac{e^{\beta_{0}}}{1 + e^{\beta_{0}}}$ : in other words, that the probability of default does not depend on balance. Since the p-value associated with balance in Table 4.1 is tiny, we can reject $H_{0}$ . In other words, we conclude that there is indeed an association between balance and probability of default. The estimated intercept in Table 4.1 is typically not of interest; its main purpose is to adjust the average fitted probabilities to the proportion of ones in the data (in this case, the overall default rate).

# 4.3.3 Making Predictions

Once the coefficients have been estimated, we can compute the probability of default for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probability for an individual with a balance of \$1,000 is

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>z-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>-10.6513</td><td>0.3612</td><td>-29.5</td><td>&lt;0.0001</td></tr><tr><td>balance</td><td>0.0055</td><td>0.0002</td><td>24.9</td><td>&lt;0.0001</td></tr></table>

TABLE 4.1. For the Default data, estimated coefficients of the logistic regression model that predicts the probability of default using balance. A one-unit increase in balance is associated with an increase in the log odds of default by 0.0055 units. 

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>z-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>-3.5041</td><td>0.0707</td><td>-49.55</td><td>&lt;0.0001</td></tr><tr><td>student[Yes]</td><td>0.4049</td><td>0.1150</td><td>3.52</td><td>0.0004</td></tr></table>

TABLE 4.2. For the Default data, estimated coefficients of the logistic regression model that predicts the probability of default using student status. Student status is encoded as a dummy variable, with a value of 1 for a student and a value of 0 for a non-student, and represented by the variable student [Yes] in the table.

$$
\hat {p} (X) = \frac {e ^ {\hat {\beta} _ {0} + \hat {\beta} _ {1} X}}{1 + e ^ {\hat {\beta} _ {0} + \hat {\beta} _ {1} X}} = \frac {e ^ {- 1 0 . 6 5 1 3 + 0 . 0 0 5 5 \times 1 , 0 0 0}}{1 + e ^ {- 1 0 . 6 5 1 3 + 0 . 0 0 5 5 \times 1 , 0 0 0}} = 0. 0 0 5 7 6,
$$

which is below 1%. In contrast, the predicted probability of default for an individual with a balance of \$2,000 is much higher, and equals 0.586 or 58.6%.

One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the Default data set contains the qualitative variable student. To fit a model that uses student status as a predictor variable, we simply create a dummy variable that takes on a value of 1 for students and 0 for non-students. The logistic regression model that results from predicting probability of default from student status can be seen in Table 4.2. The coefficient associated with the dummy variable is positive, and the associated p-value is statistically significant. This indicates that students tend to have higher default probabilities than non-students:

$$
\widehat {\operatorname * {P r}} (\text { default } = \text { Yes } | \text { student } = \text { Yes }) = \frac {e ^ {- 3 . 5 0 4 1 + 0 . 4 0 4 9 \times 1}}{1 + e ^ {- 3 . 5 0 4 1 + 0 . 4 0 4 9 \times 1}} = 0. 0 4 3 1,
$$

$$
\widehat {\operatorname * {P r}} (\text { default } = \text { Yes } | \text { student } = \text { No }) = \frac {e ^ {- 3 . 5 0 4 1 + 0 . 4 0 4 9 \times 0}}{1 + e ^ {- 3 . 5 0 4 1 + 0 . 4 0 4 9 \times 0}} = 0. 0 2 9 2.
$$

# 4.3.4 Multiple Logistic Regression

We now consider the problem of predicting a binary response using multiple predictors. By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows:

$$
\log \left(\frac {p (X)}{1 - p (X)}\right) = \beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}, \tag {4.6}
$$

where $X = (X_{1},\ldots ,X_{p})$ are $p$ predictors. Equation 4.6 can be rewritten as

$$
p (X) = \frac {e ^ {\beta_ {0} + \beta_ {1} X _ {1} + \cdots + \beta_ {p} X _ {p}}}{1 + e ^ {\beta_ {0} + \beta_ {1} X _ {1} + \cdots + \beta_ {p} X _ {p}}}. \tag {4.7}
$$

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>z-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>-10.8690</td><td>0.4923</td><td>-22.08</td><td>&lt;0.0001</td></tr><tr><td>balance</td><td>0.0057</td><td>0.0002</td><td>24.74</td><td>&lt;0.0001</td></tr><tr><td>income</td><td>0.0030</td><td>0.0082</td><td>0.37</td><td>0.7115</td></tr><tr><td>student[Yes]</td><td>-0.6468</td><td>0.2362</td><td>-2.74</td><td>0.0062</td></tr></table>

TABLE 4.3. For the Default data, estimated coefficients of the logistic regression model that predicts the probability of default using balance, income, and student status. Student status is encoded as a dummy variable student [Yes], with a value of 1 for a student and a value of 0 for a non-student. In fitting this model, income was measured in thousands of dollars.

Just as in Section 4.3.2, we use the maximum likelihood method to estimate $\beta_0, \beta_1, \ldots, \beta_p$ .

Table 4.3 shows the coefficient estimates for a logistic regression model that uses balance, income (in thousands of dollars), and student status to predict probability of default. There is a surprising result here. The p-values associated with balance and the dummy variable for student status are very small, indicating that each of these variables is associated with the probability of default. However, the coefficient for the dummy variable is negative, indicating that students are less likely to default than non-students. In contrast, the coefficient for the dummy variable is positive in Table 4.2. How is it possible for student status to be associated with an increase in probability of default in Table 4.2 and a decrease in probability of default in Table 4.3? The left-hand panel of Figure 4.3 provides a graphical illustration of this apparent paradox. The orange and blue solid lines show the average default rates for students and non-students, respectively, as a function of credit card balance. The negative coefficient for student in the multiple logistic regression indicates that for a fixed value of balance and income, a student is less likely to default than a non-student. Indeed, we observe from the left-hand panel of Figure 4.3 that the student default rate is at or below that of the non-student default rate for every value of balance. But the horizontal broken lines near the base of the plot, which show the default rates for students and non-students averaged over all values of balance and income, suggest the opposite effect: the overall student default rate is higher than the non-student default rate. Consequently, there is a positive coefficient for student in the single variable logistic regression output shown in Table 4.2.

The right-hand panel of Figure 4.3 provides an explanation for this discrepancy. The variables student and balance are correlated. Students tend to hold higher levels of debt, which is in turn associated with higher probability of default. In other words, students are more likely to have large credit card balances, which, as we know from the left-hand panel of Figure 4.3, tend to be associated with high default rates. Thus, even though an individual student with a given credit card balance will tend to have a lower probability of default than a non-student with the same credit card balance, the fact that students on the whole tend to have higher credit card balances means that overall, students tend to default at a higher rate than non-students. This is an important distinction for a credit card company that is trying to determine to whom they should offer credit. A student is riskier than a non-student if no information about the student's credit card balance is available. However, that student is less risky than a non-student with the same credit card balance!

![](images/8c3655f0dae89572111af7dd5e0208f220a02473c8e046defa154b60c19c8fcb.jpg)

<details>
<summary>line</summary>

| Credit Card Balance | Default Rate (Blue Line) | Default Rate (Orange Line) |
| ------------------- | ------------------------ | -------------------------- |
| 500                 | 0.0                      | 0.0                        |
| 1000                | 0.0                      | 0.0                        |
| 1500                | 0.1                      | 0.1                        |
| 2000                | 0.8                      | 0.7                        |
| 2500                | 0.9                      | 0.8                        |
</details>

![](images/09f1e8ea715677f3e5405d17e3d92f827e69b09117ed81949c81722019fc8cf8.jpg)

<details>
<summary>boxplot</summary>

| Student Status | Credit Card Balance |
| -------------- | ------------------- |
| No             | 0 to 2500           |
| Yes            | 0 to 2500           |
</details>

FIGURE 4.3. Confounding in the Default data. Left: Default rates are shown for students (orange) and non-students (blue). The solid lines display default rate as a function of balance, while the horizontal broken lines display the overall default rates. Right: Boxplots of balance for students (orange) and non-students (blue) are shown.

This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant. As in the linear regression setting, the results obtained using one predictor may be quite different from those obtained using multiple predictors, especially when there is correlation among the predictors. In general, the phenomenon seen in Figure 4.3 is known as confounding.

By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions. For example, a student with a credit card balance of \$1,500 and an income of \$40,000 has an estimated probability of default of

$$
\hat {p} (X) = \frac {e ^ {- 1 0 . 8 6 9 + 0 . 0 0 5 7 4 \times 1 , 5 0 0 + 0 . 0 0 3 \times 4 0 - 0 . 6 4 6 8 \times 1}}{1 + e ^ {- 1 0 . 8 6 9 + 0 . 0 0 5 7 4 \times 1 , 5 0 0 + 0 . 0 0 3 \times 4 0 - 0 . 6 4 6 8 \times 1}} = 0. 0 5 8. \tag {4.8}
$$

A non-student with the same balance and income has an estimated probability of default of

$$
\hat {p} (X) = \frac {e ^ {- 1 0 . 8 6 9 + 0 . 0 0 5 7 4 \times 1 , 5 0 0 + 0 . 0 0 3 \times 4 0 - 0 . 6 4 6 8 \times 0}}{1 + e ^ {- 1 0 . 8 6 9 + 0 . 0 0 5 7 4 \times 1 , 5 0 0 + 0 . 0 0 3 \times 4 0 - 0 . 6 4 6 8 \times 0}} = 0. 1 0 5. \tag {4.9}
$$

(Here we multiply the income coefficient estimate from Table 4.3 by 40, rather than by 40,000, because in that table the model was fit with income measured in units of \$1,000.)

# 4.3.5 Multinomial Logistic Regression

We sometimes wish to classify a response variable that has more than two classes. For example, in Section 4.2 we had three categories of medical condition in the emergency room: stroke, drug overdose, epileptic seizure. However, the logistic regression approach that we have seen in this section only allows for K = 2 classes for the response variable.

confounding

It turns out that it is possible to extend the two-class logistic regression approach to the setting of K > 2 classes. This extension is sometimes known as multinomial logistic regression. To do this, we first select a single class to serve as the baseline; without loss of generality, we select the Kth class for this role. Then we replace the model (4.7) with the model

multinomial
logistic
regression

$$
\operatorname * {P r} (Y = k | X = x) = \frac {e ^ {\beta_ {k 0} + \beta_ {k 1} x _ {1} + \cdots + \beta_ {k p} x _ {p}}}{1 + \sum_ {l = 1} ^ {K - 1} e ^ {\beta_ {l 0} + \beta_ {l 1} x _ {1} + \cdots + \beta_ {l p} x _ {p}}} \tag {4.10}
$$

for $k = 1, \ldots, K - 1$ , and

$$
\operatorname * {P r} (Y = K | X = x) = \frac {1}{1 + \sum_ {l = 1} ^ {K - 1} e ^ {\beta_ {l 0} + \beta_ {l 1} x _ {1} + \cdots + \beta_ {l p} x _ {p}}}. \tag {4.11}
$$

It is not hard to show that for $k = 1, \ldots, K - 1$ ,

$$
\log \left(\frac {\operatorname * {P r} (Y = k | X = x)}{\operatorname * {P r} (Y = K | X = x)}\right) = \beta_ {k 0} + \beta_ {k 1} x _ {1} + \dots + \beta_ {k p} x _ {p}. \tag {4.12}
$$

Notice that (4.12) is quite similar to (4.6). Equation 4.12 indicates that once again, the log odds between any pair of classes is linear in the features.

It turns out that in $(4.10)-(4.12)$ , the decision to treat the Kth class as the baseline is unimportant. For example, when classifying emergency room visits into stroke, drug overdose, and epileptic seizure, suppose that we fit two multinomial logistic regression models: one treating stroke as the baseline, another treating drug overdose as the baseline. The coefficient estimates will differ between the two fitted models due to the differing choice of baseline, but the fitted values (predictions), the log odds between any pair of classes, and the other key model outputs will remain the same.

Nonetheless, interpretation of the coefficients in a multinomial logistic regression model must be done with care, since it is tied to the choice of baseline. For example, if we set epileptic seizure to be the baseline, then we can interpret $\beta_{stroke0}$ as the log odds of stroke versus epileptic seizure, given that $x_{1} = \cdots = x_{p} = 0$ . Furthermore, a one-unit increase in $X_{j}$ is associated with a $\beta_{strokej}$ increase in the log odds of stroke over epileptic seizure. Stated another way, if $X_{j}$ increases by one unit, then

$$
\frac {\operatorname* {P r} (Y = \text { stroke } | X = x)}{\operatorname* {P r} (Y = \text { epileptic   seizure } | X = x)}
$$

increases by $e^{\beta_{\mathrm{stroke}j}}$

We now briefly present an alternative coding for multinomial logistic regression, known as the softmax coding. The softmax coding is equivalent to the coding just described in the sense that the fitted values, log odds between any pair of classes, and other key model outputs will remain the same, regardless of coding. But the softmax coding is used extensively in some areas of the machine learning literature (and will appear again in Chapter 10), so it is worth being aware of it. In the softmax coding, rather than selecting a baseline class, we treat all K classes symmetrically, and assume that for $k = 1, \ldots, K$ ,

softmax

$$
\operatorname * {P r} (Y = k | X = x) = \frac {e ^ {\beta_ {k 0} + \beta_ {k 1} x _ {1} + \cdots + \beta_ {k p} x _ {p}}}{\sum_ {l = 1} ^ {K} e ^ {\beta_ {l 0} + \beta_ {l 1} x _ {1} + \cdots + \beta_ {l p} x _ {p}}}. \tag {4.13}
$$

Thus, rather than estimating coefficients for K - 1 classes, we actually estimate coefficients for all K classes. It is not hard to see that as a result of (4.13), the log odds ratio between the kth and $k'$ th classes equals

$$
\log \left(\frac {\operatorname* {P r} (Y = k | X = x)}{\operatorname* {P r} (Y = k ^ {\prime} | X = x)}\right) = (\beta_ {k 0} - \beta_ {k ^ {\prime} 0}) + (\beta_ {k 1} - \beta_ {k ^ {\prime} 1}) x _ {1} + \dots + (\beta_ {k p} - \beta_ {k ^ {\prime} p}) x _ {p}. \tag {4.14}
$$

# 4.4 Generative Models for Classification

Logistic regression involves directly modeling $\Pr(Y = k|X = x)$ using the logistic function, given by (4.7) for the case of two response classes. In statistical jargon, we model the conditional distribution of the response Y, given the predictor(s) X. We now consider an alternative and less direct approach to estimating these probabilities. In this new approach, we model the distribution of the predictors X separately in each of the response classes (i.e. for each value of Y). We then use Bayes' theorem to flip these around into estimates for $\Pr(Y = k|X = x)$ . When the distribution of X within each class is assumed to be normal, it turns out that the model is very similar in form to logistic regression.

Why do we need another method, when we have logistic regression? There are several reasons:

- When there is substantial separation between the two classes, the parameter estimates for the logistic regression model are surprisingly unstable. The methods that we consider in this section do not suffer from this problem.   
- If the distribution of the predictors $X$ is approximately normal in each of the classes and the sample size is small, then the approaches in this section may be more accurate than logistic regression.   
- The methods in this section can be naturally extended to the case of more than two response classes. (In the case of more than two response classes, we can also use multinomial logistic regression from Section 4.3.5.)

Suppose that we wish to classify an observation into one of $K$ classes, where $K \geq 2$ . In other words, the qualitative response variable $Y$ can take on $K$ possible distinct and unordered values. Let $\pi_k$ represent the overall or prior probability that a randomly chosen observation comes from the $k$ th class. Let $f_k(X) \equiv \Pr(X|Y = k)^1$ denote the density function of $X$ for an observation that comes from the $k$ th class. In other words, $f_k(x)$ is relatively large if there is a high probability that an observation in the $k$ th class has $X \approx x$ , and $f_k(x)$ is small if it is very unlikely that an observation in the $k$ th class has $X \approx x$ . Then Bayes' theorem states that

prior
density
function

Bayes' theorem

$$
\operatorname * {P r} (Y = k | X = x) = \frac {\pi_ {k} f _ {k} (x)}{\sum_ {l = 1} ^ {K} \pi_ {l} f _ {l} (x)}. \tag {4.15}
$$

In accordance with our earlier notation, we will use the abbreviation $p_{k}(x) = \Pr(Y = k | X = x)$ ; this is the posterior probability that an observation X = x belongs to the kth class. That is, it is the probability that the observation belongs to the kth class, given the predictor value for that observation.

Equation 4.15 suggests that instead of directly computing the posterior probability $p_k(x)$ as in Section 4.3.1, we can simply plug in estimates of $\pi_k$ and $f_{k}(x)$ into (4.15). In general, estimating $\pi_k$ is easy if we have a random sample from the population: we simply compute the fraction of the training observations that belong to the $k$ th class. However, estimating the density function $f_{k}(x)$ is much more challenging. As we will see, to estimate $f_{k}(x)$ , we will typically have to make some simplifying assumptions.

We know from Chapter 2 that the Bayes classifier, which classifies an observation $x$ to the class for which $p_k(x)$ is largest, has the lowest possible error rate out of all classifiers. (Of course, this is only true if all of the terms in (4.15) are correctly specified.) Therefore, if we can find a way to estimate $f_k(x)$ , then we can plug it into (4.15) in order to approximate the Bayes classifier.

In the following sections, we discuss three classifiers that use different estimates of $f_{k}(x)$ in (4.15) to approximate the Bayes classifier: linear discriminant analysis, quadratic discriminant analysis, and naive Bayes.

# 4.4.1 Linear Discriminant Analysis for $p = 1$

For now, assume that $p = 1$ — that is, we have only one predictor. We would like to obtain an estimate for $f_{k}(x)$ that we can plug into (4.15) in order to estimate $p_{k}(x)$ . We will then classify an observation to the class for which $p_{k}(x)$ is greatest. To estimate $f_{k}(x)$ , we will first make some assumptions about its form.

In particular, we assume that $f_{k}(x)$ is normal or Gaussian. In the one-dimensional setting, the normal density takes the form

$$
f _ {k} (x) = \frac {1}{\sqrt {2 \pi} \sigma_ {k}} \exp \left(- \frac {1}{2 \sigma_ {k} ^ {2}} (x - \mu_ {k}) ^ {2}\right), \tag {4.16}
$$

where $\mu_{k}$ and $\sigma_{k}^{2}$ are the mean and variance parameters for the kth class. For now, let us further assume that $\sigma_{1}^{2}=\cdots=\sigma_{K}^{2}$ : that is, there is a shared variance term across all K classes, which for simplicity we can denote by $\sigma^{2}$ . Plugging (4.16) into (4.15), we find that

$$
p _ {k} (x) = \frac {\pi_ {k} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {1}{2 \sigma^ {2}} (x - \mu_ {k}) ^ {2}\right)}{\sum_ {l = 1} ^ {K} \pi_ {l} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {1}{2 \sigma^ {2}} (x - \mu_ {l}) ^ {2}\right)}. \tag {4.17}
$$

(Note that in (4.17), $\pi_k$ denotes the prior probability that an observation belongs to the $k$ th class, not to be confused with $\pi \approx 3.14159$ , the mathematical constant.) The Bayes classifier $^2$ involves assigning an observation

![](images/237bc9219387ed273cf0463c6bf360f395c07a40267e8e4e42c0f3c507ab9dd9.jpg)

<details>
<summary>line</summary>

| x    | Green Line | Pink Line |
| ---- | ---------- | --------- |
| -4   | 0          | 0         |
| -2   | 0.8796     | 0         |
| 0    | 0          | 0         |
| 2    | 0.8796     | 0.8796    |
| 4    | 0          | 0         |
</details>

![](images/11439b22ed3360f55653f6b9f897d084727df0a47b985205ee7f6fb8512b9e7c.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Green Count | Pink Count |
|-----------|-------------|------------|
| -3 to -2  | 2           | 0          |
| -2 to -1  | 5           | 1          |
| -1 to 0   | 3           | 2          |
| 0 to 1    | 1           | 3          |
| 1 to 2    | 0           | 5          |
| 2 to 3    | 0           | 3          |
| 3 to 4    | 0           | 2          |
</details>

FIGURE 4.4. Left: Two one-dimensional normal density functions are shown. The dashed vertical line represents the Bayes decision boundary. Right: 20 observations were drawn from each of the two classes, and are shown as histograms. The Bayes decision boundary is again shown as a dashed vertical line. The solid vertical line represents the LDA decision boundary estimated from the training data.

X = x to the class for which $(4.17)$ is largest. Taking the log of $(4.17)$ and rearranging the terms, it is not hard to show $^{3}$ that this is equivalent to assigning the observation to the class for which

$$
\delta_ {k} (x) = x \cdot \frac {\mu_ {k}}{\sigma^ {2}} - \frac {\mu_ {k} ^ {2}}{2 \sigma^ {2}} + \log (\pi_ {k}) \tag {4.18}
$$

is largest. For instance, if $K = 2$ and $\pi_1 = \pi_2$ , then the Bayes classifier assigns an observation to class 1 if $2x(\mu_1 - \mu_2) > \mu_1^2 - \mu_2^2$ , and to class 2 otherwise. The Bayes decision boundary is the point for which $\delta_1(x) = \delta_2(x)$ ; one can show that this amounts to

$$
x = \frac {\mu_ {1} ^ {2} - \mu_ {2} ^ {2}}{2 (\mu_ {1} - \mu_ {2})} = \frac {\mu_ {1} + \mu_ {2}}{2}. \tag {4.19}
$$

An example is shown in the left-hand panel of Figure 4.4. The two normal density functions that are displayed, $f_{1}(x)$ and $f_{2}(x)$ , represent two distinct classes. The mean and variance parameters for the two density functions are $\mu_{1} = -1.25$ , $\mu_{2} = 1.25$ , and $\sigma_{1}^{2} = \sigma_{2}^{2} = 1$ . The two densities overlap, and so given that X = x, there is some uncertainty about the class to which the observation belongs. If we assume that an observation is equally likely to come from either class—that is, $\pi_{1} = \pi_{2} = 0.5$ —then by inspection of (4.19), we see that the Bayes classifier assigns the observation to class 1 if x < 0 and class 2 otherwise. Note that in this case, we can compute the Bayes classifier because we know that X is drawn from a Gaussian distribution within each class, and we know all of the parameters involved. In a real-life situation, we are not able to calculate the Bayes classifier.

In practice, even if we are quite certain of our assumption that $X$ is drawn from a Gaussian distribution within each class, to apply the Bayes classifier we still have to estimate the parameters $\mu_1, \ldots, \mu_K$ , $\pi_1, \ldots, \pi_K$ , and $\sigma^2$ . The linear discriminant analysis (LDA) method approximates the Bayes classifier by plugging estimates for $\pi_k$ , $\mu_k$ , and $\sigma^2$ into (4.18). In linear
discriminant
analysis

particular, the following estimates are used:

$$
\hat {\mu} _ {k} = \frac {1}{n _ {k}} \sum_ {i: y _ {i} = k} x _ {i}
$$

$$
\hat {\sigma} ^ {2} = \frac {1}{n - K} \sum_ {k = 1} ^ {K} \sum_ {i: y _ {i} = k} (x _ {i} - \hat {\mu} _ {k}) ^ {2} \tag {4.20}
$$

where n is the total number of training observations, and $n_{k}$ is the number of training observations in the kth class. The estimate for $\mu_{k}$ is simply the average of all the training observations from the kth class, while $\hat{\sigma}^{2}$ can be seen as a weighted average of the sample variances for each of the K classes. Sometimes we have knowledge of the class membership probabilities $\pi_{1},\ldots,\pi_{K}$ , which can be used directly. In the absence of any additional information, LDA estimates $\pi_{k}$ using the proportion of the training observations that belong to the kth class. In other words,

$$
\hat {\pi} _ {k} = n _ {k} / n. \tag {4.21}
$$

The LDA classifier plugs the estimates given in (4.20) and (4.21) into (4.18), and assigns an observation $X = x$ to the class for which

$$
\hat {\delta} _ {k} (x) = x \cdot \frac {\hat {\mu} _ {k}}{\hat {\sigma} ^ {2}} - \frac {\hat {\mu} _ {k} ^ {2}}{2 \hat {\sigma} ^ {2}} + \log (\hat {\pi} _ {k}) \tag {4.22}
$$

is largest. The word linear in the classifier's name stems from the fact that the discriminant functions $\hat{\delta}_k(x)$ in (4.22) are linear functions of $x$ (as opposed to a more complex function of $x$ ).

The right-hand panel of Figure 4.4 displays a histogram of a random sample of 20 observations from each class. To implement LDA, we began by estimating $\pi_k$ , $\mu_k$ , and $\sigma^2$ using (4.20) and (4.21). We then computed the decision boundary, shown as a black solid line, that results from assigning an observation to the class for which (4.22) is largest. All points to the left of this line will be assigned to the green class, while points to the right of this line are assigned to the purple class. In this case, since $n_1 = n_2 = 20$ , we have $\hat{\pi}_1 = \hat{\pi}_2$ . As a result, the decision boundary corresponds to the midpoint between the sample means for the two classes, $(\hat{\mu}_1 + \hat{\mu}_2)/2$ . The figure indicates that the LDA decision boundary is slightly to the left of the optimal Bayes decision boundary, which instead equals $(\mu_1 + \mu_2)/2 = 0$ . How well does the LDA classifier perform on this data? Since this is simulated data, we can generate a large number of test observations in order to compute the Bayes error rate and the LDA test error rate. These are $10.6\%$ and $11.1\%$ , respectively. In other words, the LDA classifier's error rate is only $0.5\%$ above the smallest possible error rate! This indicates that LDA is performing pretty well on this data set.

To reiterate, the LDA classifier results from assuming that the observations within each class come from a normal distribution with a class-specific mean and a common variance $\sigma^{2}$ , and plugging estimates for these parameters into the Bayes classifier. In Section 4.4.3, we will consider a less stringent set of assumptions, by allowing the observations in the kth class to have a class-specific variance, $\sigma_{k}^{2}$ .

![](images/ad1dcd207238952195b002e92fe6ca0f9ad6e99df954c53f05c40dffc0779dc3.jpg)

<details>
<summary>natural_image</summary>

Two 3D surface plots with grid patterns, labeled x₁ and x₂, showing a gradient-filled surface (no text or symbols beyond labels)
</details>

FIGURE 4.5. Two multivariate Gaussian density functions are shown, with p = 2. Left: The two predictors are uncorrelated. Right: The two variables have a correlation of 0.7.

# 4.4.2 Linear Discriminant Analysis for $p > 1$

We now extend the LDA classifier to the case of multiple predictors. To do this, we will assume that $X = (X_{1}, X_{2}, \ldots, X_{p})$ is drawn from a multivariate Gaussian (or multivariate normal) distribution, with a class-specific mean vector and a common covariance matrix. We begin with a brief review of this distribution.

The multivariate Gaussian distribution assumes that each individual predictor follows a one-dimensional normal distribution, as in (4.16), with some correlation between each pair of predictors. Two examples of multivariate Gaussian distributions with p = 2 are shown in Figure 4.5. The height of the surface at any particular point represents the probability that both $X_{1}$ and $X_{2}$ fall in a small region around that point. In either panel, if the surface is cut along the $X_{1}$ axis or along the $X_{2}$ axis, the resulting cross-section will have the shape of a one-dimensional normal distribution. The left-hand panel of Figure 4.5 illustrates an example in which $\operatorname{Var}(X_{1}) = \operatorname{Var}(X_{2})$ and $\operatorname{Cor}(X_{1}, X_{2}) = 0$ ; this surface has a characteristic bell shape. However, the bell shape will be distorted if the predictors are correlated or have unequal variances, as is illustrated in the right-hand panel of Figure 4.5. In this situation, the base of the bell will have an elliptical, rather than circular, shape. To indicate that a p-dimensional random variable X has a multivariate Gaussian distribution, we write $X \sim N(\mu, \Sigma)$ . Here $\operatorname{E}(X) = \mu$ is the mean of X (a vector with p components), and $\operatorname{Cov}(X) = \Sigma$ is the $p \times p$ covariance matrix of X. Formally, the multivariate Gaussian density is defined as

$$
f (x) = \frac {1}{(2 \pi) ^ {p / 2} | \boldsymbol {\Sigma} | ^ {1 / 2}} \exp \left(- \frac {1}{2} (x - \mu) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (x - \mu)\right). \tag {4.23}
$$

In the case of p > 1 predictors, the LDA classifier assumes that the observations in the kth class are drawn from a multivariate Gaussian distribution $N(\mu_{k}, \Sigma)$ , where $\mu_{k}$ is a class-specific mean vector, and $\Sigma$ is a covariance matrix that is common to all K classes. Plugging the density function for the kth class, $f_{k}(X = x)$ , into (4.15) and performing a little bit of algebra reveals that the Bayes classifier assigns an observation X = x

multivariate Gaussian

![](images/2e076a8eb253bad95a568e796981dc38e6afbcf189518748129426769c32b85e.jpg)

<details>
<summary>scatter</summary>

| Group | X1    | X2    |
|-------|-------|-------|
| Green | -3.5  | -3.8  |
| Green | -1.0  | -1.5  |
| Green | 0.5   | 0.0   |
| Blue  | 1.0   | 0.5   |
| Blue  | 2.5   | 3.0   |
| Blue  | 4.0   | 4.5   |
| Orange| 1.5   | 1.0   |
| Orange| 2.0   | 2.5   |
| Orange| 3.0   | 4.0   |
</details>

![](images/270ccfb78204b9b7ed3fda568ee61617d1e2a4b330cc226b90ccff1b6c6de6b4.jpg)

<details>
<summary>scatter</summary>

| X1    | X2    | Group |
|-------|-------|-------|
| -3.5  | -3.0  | Green |
| -2.8  | -2.5  | Green |
| -2.2  | -2.0  | Green |
| -1.5  | -1.5  | Green |
| -0.8  | -1.0  | Green |
| 0.0   | -0.5  | Green |
| 0.5   | 0.0   | Green |
| 1.0   | 0.5   | Green |
| 1.5   | 1.0   | Green |
| 2.0   | 1.5   | Green |
| 2.5   | 2.0   | Green |
| 3.0   | 2.5   | Green |
| 3.5   | 3.0   | Green |
| -3.0  | 2.0   | Orange |
| -2.5  | 2.5   | Orange |
| -2.0  | 3.0   | Orange |
| -1.5  | 3.5   | Orange |
| -1.0  | 4.0   | Orange |
| -0.5  | 4.5   | Orange |
| 0.0   | 5.0   | Orange |
| 0.5   | 4.5   | Orange |
| 1.0   | 4.0   | Orange |
| 1.5   | 3.5   | Orange |
| 2.0   | 3.0   | Orange |
| 2.5   | 2.5   | Orange |
| 3.0   | 2.0   | Orange |
| 3.5   | 1.5   | Orange |
| 4.0   | 1.0   | Orange |
| -3.5  | -1.5  | Blue  |
| -3.0  | -2.0  | Blue  |
| -2.5  | -2.5  | Blue  |
| -2.0  | -3.0  | Blue  |
| -1.5  | -3.5  | Blue  |
| -1.0  | -4.0  | Blue  |
| -0.5  | -3.5  | Blue  |
| 0.0   | -3.0  | Blue  |
| 0.5   | -2.5  | Blue  |
| 1.0   | -2.0  | Blue  |
| 1.5   | -1.5  | Blue  |
| 2.0   | -1.0  | Blue  |
| 2.5   | -0.5  | Blue  |
| 3.0   | 0.0   | Blue  |
| 3.5   | 0.5   | Blue  |
| 4.0   | 1.0   | Blue  |
</details>

FIGURE 4.6. An example with three classes. The observations from each class are drawn from a multivariate Gaussian distribution with p = 2, with a class-specific mean vector and a common covariance matrix. Left: Ellipses that contain 95% of the probability for each of the three classes are shown. The dashed lines are the Bayes decision boundaries. Right: 20 observations were generated from each class, and the corresponding LDA decision boundaries are indicated using solid black lines. The Bayes decision boundaries are once again shown as dashed lines.

to the class for which

$$
\delta_ {k} (x) = x ^ {T} \boldsymbol {\Sigma} ^ {- 1} \mu_ {k} - \frac {1}{2} \mu_ {k} ^ {T} \boldsymbol {\Sigma} ^ {- 1} \mu_ {k} + \log \pi_ {k} \tag {4.24}
$$

is largest. This is the vector/matrix version of (4.18).

An example is shown in the left-hand panel of Figure 4.6. Three equally-sized Gaussian classes are shown with class-specific mean vectors and a common covariance matrix. The three ellipses represent regions that contain $95\%$ of the probability for each of the three classes. The dashed lines are the Bayes decision boundaries. In other words, they represent the set of values $x$ for which $\delta_k(x) = \delta_\ell(x)$ ; i.e.

$$
x ^ {T} \boldsymbol {\Sigma} ^ {- 1} \mu_ {k} - \frac {1}{2} \mu_ {k} ^ {T} \boldsymbol {\Sigma} ^ {- 1} \mu_ {k} = x ^ {T} \boldsymbol {\Sigma} ^ {- 1} \mu_ {l} - \frac {1}{2} \mu_ {l} ^ {T} \boldsymbol {\Sigma} ^ {- 1} \mu_ {l} \tag {4.25}
$$

for $k \neq l$ . (The $\log \pi_{k}$ term from (4.24) has disappeared because each of the three classes has the same number of training observations; i.e. $\pi_{k}$ is the same for each class.) Note that there are three lines representing the Bayes decision boundaries because there are three pairs of classes among the three classes. That is, one Bayes decision boundary separates class 1 from class 2, one separates class 1 from class 3, and one separates class 2 from class 3. These three Bayes decision boundaries divide the predictor space into three regions. The Bayes classifier will classify an observation according to the region in which it is located.

Once again, we need to estimate the unknown parameters $\mu_{1},\ldots,\mu_{K}$ , $\pi_{1},\ldots,\pi_{K}$ , and $\Sigma$ ; the formulas are similar to those used in the one-dimensional case, given in (4.20). To assign a new observation X = x, LDA plugs these estimates into (4.24) to obtain quantities $\hat{\delta}_{k}(x)$ , and classifies to the class for which $\hat{\delta}_{k}(x)$ is largest. Note that in (4.24) $\delta_{k}(x)$ is a linear function of x; that is, the LDA decision rule depends on x only through a linear combination of its elements. As previously discussed, this is the reason for the word linear in LDA.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">True default status</td></tr><tr><td>No</td><td>Yes</td><td>Total</td></tr><tr><td rowspan="3">Predicted default status</td><td>No</td><td>9644</td><td>252</td><td>9896</td></tr><tr><td>Yes</td><td>23</td><td>81</td><td>104</td></tr><tr><td>Total</td><td>9667</td><td>333</td><td>10000</td></tr></table>

TABLE 4.4. A confusion matrix compares the LDA predictions to the true default statuses for the 10,000 training observations in the Default data set. Elements on the diagonal of the matrix represent individuals whose default statuses were correctly predicted, while off-diagonal elements represent individuals that were misclassified. LDA made incorrect predictions for 23 individuals who did not default and for 252 individuals who did default.

In the right-hand panel of Figure 4.6, 20 observations drawn from each of the three classes are displayed, and the resulting LDA decision boundaries are shown as solid black lines. Overall, the LDA decision boundaries are pretty close to the Bayes decision boundaries, shown again as dashed lines. The test error rates for the Bayes and LDA classifiers are 0.0746 and 0.0770, respectively. This indicates that LDA is performing well on this data.

We can perform LDA on the Default data in order to predict whether or not an individual will default on the basis of credit card balance and student status. $^{4}$ The LDA model fit to the 10,000 training samples results in a training error rate of 2.75%. This sounds like a low error rate, but two caveats must be noted.

- First of all, training error rates will usually be lower than test error rates, which are the real quantity of interest. In other words, we might expect this classifier to perform worse if we use it to predict whether or not a new set of individuals will default. The reason is that we specifically adjust the parameters of our model to do well on the training data. The higher the ratio of parameters $p$ to number of samples $n$ , the more we expect this overfitting to play a role. For these data we don't expect this to be a problem, since $p = 2$ and $n = 10,000$ .   
- Second, since only 3.33% of the individuals in the training sample defaulted, a simple but useless classifier that always predicts that an individual will not default, regardless of his or her credit card balance and student status, will result in an error rate of 3.33%. In other words, the trivial null classifier will achieve an error rate that is only a bit higher than the LDA training set error rate.

In practice, a binary classifier such as this one can make two types of errors: it can incorrectly assign an individual who defaults to the no default category, or it can incorrectly assign an individual who does not default to

overfitting

null

the default category. It is often of interest to determine which of these two types of errors are being made. A confusion matrix, shown for the Default data in Table 4.4, is a convenient way to display this information. The table reveals that LDA predicted that a total of 104 people would default. Of these people, 81 actually defaulted and 23 did not. Hence only 23 out of 9,667 of the individuals who did not default were incorrectly labeled. This looks like a pretty low error rate! However, of the 333 individuals who defaulted, 252 (or $75.7\%$ ) were missed by LDA. So while the overall error rate is low, the error rate among individuals who defaulted is very high. From the perspective of a credit card company that is trying to identify high-risk individuals, an error rate of $252 / 333 = 75.7\%$ among individuals who default may well be unacceptable.

Class-specific performance is also important in medicine and biology, where the terms sensitivity and specificity characterize the performance of a classifier or screening test. In this case the sensitivity is the percentage of true defaulters that are identified; it equals 24.3%. The specificity is the percentage of non-defaulters that are correctly identified; it equals $(1 - 23/9667) = 99.8\%$ .

Why does LDA do such a poor job of classifying the customers who default? In other words, why does it have such low sensitivity? As we have seen, LDA is trying to approximate the Bayes classifier, which has the lowest total error rate out of all classifiers. That is, the Bayes classifier will yield the smallest possible total number of misclassified observations, regardless of the class from which the errors stem. Some misclassifications will result from incorrectly assigning a customer who does not default to the default class, and others will result from incorrectly assigning a customer who defaults to the non-default class. In contrast, a credit card company might particularly wish to avoid incorrectly classifying an individual who will default, whereas incorrectly classifying an individual who will not default, though still to be avoided, is less problematic. We will now see that it is possible to modify LDA in order to develop a classifier that better meets the credit card company's needs.

The Bayes classifier works by assigning an observation to the class for which the posterior probability $p_{k}(X)$ is greatest. In the two-class case, this amounts to assigning an observation to the default class if

$$
\operatorname * {P r} (\text { default } = \text { Yes } | X = x) > 0. 5. \tag {4.26}
$$

Thus, the Bayes classifier, and by extension LDA, uses a threshold of 50% for the posterior probability of default in order to assign an observation to the default class. However, if we are concerned about incorrectly predicting the default status for individuals who default, then we can consider lowering this threshold. For instance, we might label any customer with a posterior probability of default above 20% to the default class. In other words, instead of assigning an observation to the default class if $(4.26)$ holds, we could instead assign an observation to this class if

$$
\operatorname * {P r} (\text { default } = \text { Yes } | X = x) > 0. 2. \tag {4.27}
$$

The error rates that result from taking this approach are shown in Table 4.5. Now LDA predicts that 430 individuals will default. Of the 333 individuals who default, LDA correctly predicts all but 138, or $41.4\%$ . This is a vast improvement over the error rate of 75.7% that resulted from using the threshold of 50%. However, this improvement comes at a cost: now 235 individuals who do not default are incorrectly classified. As a result, the overall error rate has increased slightly to 3.73%. But a credit card company may consider this slight increase in the total error rate to be a small price to pay for more accurate identification of individuals who do indeed default.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">True default status</td></tr><tr><td>No</td><td>Yes</td><td>Total</td></tr><tr><td rowspan="3">Predicted default status</td><td>No</td><td>9432</td><td>138</td><td>9570</td></tr><tr><td>Yes</td><td>235</td><td>195</td><td>430</td></tr><tr><td>Total</td><td>9667</td><td>333</td><td>10000</td></tr></table>

TABLE 4.5. A confusion matrix compares the LDA predictions to the true default statuses for the 10,000 training observations in the Default data set, using a modified threshold value that predicts default for any individuals whose posterior default probability exceeds 20 %.

![](images/6d89ffc4646af90ec0c0700385495198693beb6a8f326ba58f5d9f2c6bdfda8d.jpg)

<details>
<summary>line</summary>

| Threshold | Error Rate (Solid Line) | Error Rate (Dashed Line) |
| --------- | ------------------------ | ------------------------- |
| 0.0       | 0.7                      | 0.0                       |
| 0.1       | 0.1                      | 0.2                       |
| 0.2       | 0.05                     | 0.35                      |
| 0.3       | 0.02                     | 0.45                      |
| 0.4       | 0.01                     | 0.55                      |
| 0.5       | 0.0                      | 0.65                      |
</details>

FIGURE 4.7. For the Default data set, error rates are shown as a function of the threshold value for the posterior probability that is used to perform the assignment. The black solid line displays the overall error rate. The blue dashed line represents the fraction of defaulting customers that are incorrectly classified, and the orange dotted line indicates the fraction of errors among the non-defaulting customers.

Figure 4.7 illustrates the trade-off that results from modifying the threshold value for the posterior probability of default. Various error rates are shown as a function of the threshold value. Using a threshold of 0.5, as in (4.26), minimizes the overall error rate, shown as a black solid line. This is to be expected, since the Bayes classifier uses a threshold of 0.5 and is known to have the lowest overall error rate. But when a threshold of 0.5 is used, the error rate among the individuals who default is quite high (blue dashed line). As the threshold is reduced, the error rate among individuals who default decreases steadily, but the error rate among the individuals who do not default increases. How can we decide which threshold value is best? Such a decision must be based on domain knowledge, such as detailed information about the costs associated with default.

The ROC curve is a popular graphic for simultaneously displaying the two types of errors for all possible thresholds. The name “ROC” is historic, and comes from communications theory. It is an acronym for receiver operating characteristics. Figure 4.8 displays the ROC curve for the LDA classifier on the training data. The overall performance of a classifier, sum-

ROC curve

![](images/dd19177b76bcbf5f349d5f00a0e1d83908a01fb1164888b13aef43d4b533ad8b.jpg)

<details>
<summary>line</summary>

| False positive rate | True positive rate |
| ------------------- | ------------------ |
| 0.0                 | 0.0                |
| 0.2                 | 0.8                |
| 0.4                 | 0.95               |
| 0.6                 | 0.98               |
| 0.8                 | 0.99               |
| 1.0                 | 1.0                |
</details>

FIGURE 4.8. A ROC curve for the LDA classifier on the Default data. It traces out two types of error as we vary the threshold value for the posterior probability of default. The actual thresholds are not shown. The true positive rate is the sensitivity: the fraction of defaulters that are correctly identified, using a given threshold value. The false positive rate is 1-specificity: the fraction of non-defaulters that we classify incorrectly as defaulters, using that same threshold value. The ideal ROC curve hugs the top left corner, indicating a high true positive rate and a low false positive rate. The dotted line represents the “no information” classifier; this is what we would expect if student status and credit card balance are not associated with probability of default.

marized over all possible thresholds, is given by the area under the (ROC) curve (AUC). An ideal ROC curve will hug the top left corner, so the larger the AUC the better the classifier. For this data the AUC is 0.95, which is close to the maximum of 1.0, so would be considered very good. We expect a classifier that performs no better than chance to have an AUC of 0.5 (when evaluated on an independent test set not used in model training). ROC curves are useful for comparing different classifiers, since they take into account all possible thresholds. It turns out that the ROC curve for the logistic regression model of Section 4.3.4 fit to these data is virtually indistinguishable from this one for the LDA model, so we do not display it here.

As we have seen above, varying the classifier threshold changes its true positive and false positive rate. These are also called the sensitivity and one minus the specificity of our classifier. Since there is an almost bewildering array of terms used in this context, we now give a summary. Table 4.6 shows the possible results when applying a classifier (or diagnostic test) to a population. To make the connection with the epidemiology literature, we think of “+” as the “disease” that we are trying to detect, and “−” as the “non-disease” state. To make the connection to the classical hypothesis testing literature, we think of “−” as the null hypothesis and “+” as the

area under the (ROC) curve

sensitivity
specificity

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">True class</td></tr><tr><td>- or Null</td><td>+ or Non-null</td><td>Total</td></tr><tr><td rowspan="3">Predicted class</td><td>- or Null</td><td>True Neg. (TN)</td><td>False Neg. (FN)</td><td>N*</td></tr><tr><td>+ or Non-null</td><td>False Pos. (FP)</td><td>True Pos. (TP)</td><td>P*</td></tr><tr><td>Total</td><td>N</td><td>P</td><td></td></tr></table>

TABLE 4.6. Possible results when applying a classifier or diagnostic test to a population. 

<table><tr><td>Name</td><td>Definition</td><td>Synonyms</td></tr><tr><td>False Pos. rate</td><td>FP/N</td><td>Type I error, 1-Specificity</td></tr><tr><td>True Pos. rate</td><td>TP/P</td><td>1-Type II error, power, sensitivity, recall</td></tr><tr><td>Pos. Pred. value</td><td>TP/P*</td><td>Precision, 1-false discovery proportion</td></tr><tr><td>Neg. Pred. value</td><td>TN/N*</td><td></td></tr></table>

TABLE 4.7. Important measures for classification and diagnostic testing, derived from quantities in Table 4.6.

alternative (non-null) hypothesis. In the context of the Default data, “+” indicates an individual who defaults, and “−” indicates one who does not.

Table 4.7 lists many of the popular performance measures that are used in this context. The denominators for the false positive and true positive rates are the actual population counts in each class. In contrast, the denominators for the positive predictive value and the negative predictive value are the total predicted counts for each class.

# 4.4.3 Quadratic Discriminant Analysis

As we have discussed, LDA assumes that the observations within each class are drawn from a multivariate Gaussian distribution with a class-specific mean vector and a covariance matrix that is common to all K classes. Quadratic discriminant analysis (QDA) provides an alternative approach. Like LDA, the QDA classifier results from assuming that the observations from each class are drawn from a Gaussian distribution, and plugging estimates for the parameters into Bayes' theorem in order to perform prediction. However, unlike LDA, QDA assumes that each class has its own covariance matrix. That is, it assumes that an observation from the kth class is of the form $X \sim N(\mu_k, \Sigma_k)$ , where $\Sigma_k$ is a covariance matrix for the kth class. Under this assumption, the Bayes classifier assigns an observation X = x to the class for which

$$
\begin{array}{l} \delta_ {k} (x) = - \frac {1}{2} (x - \mu_ {k}) ^ {T} \boldsymbol {\Sigma} _ {k} ^ {- 1} (x - \mu_ {k}) - \frac {1}{2} \log | \boldsymbol {\Sigma} _ {k} | + \log \pi_ {k} \\ = - \frac {1}{2} x ^ {T} \boldsymbol {\Sigma} _ {k} ^ {- 1} x + x ^ {T} \boldsymbol {\Sigma} _ {k} ^ {- 1} \mu_ {k} - \frac {1}{2} \mu_ {k} ^ {T} \boldsymbol {\Sigma} _ {k} ^ {- 1} \mu_ {k} - \frac {1}{2} \log | \boldsymbol {\Sigma} _ {k} | + \log \pi_ {k} \tag {4.28} \\ \end{array}
$$

is largest. So the QDA classifier involves plugging estimates for $\Sigma_{k}$ , $\mu_{k}$ , and $\pi_{k}$ into (4.28), and then assigning an observation X = x to the class for which this quantity is largest. Unlike in (4.24), the quantity x appears as a quadratic function in (4.28). This is where QDA gets its name.

Why does it matter whether or not we assume that the K classes share a common covariance matrix? In other words, why would one prefer LDA to

![](images/939dce332b5ea4e63a5d5eab9b1dd965e5732a10ad37c31b602f760fed74df02.jpg)

![](images/7f77464720ee10a872ae78ea51b4593b967296564551ddb2543382a3784b7094.jpg)

<details>
<summary>scatter</summary>

| X1    | X2    | Group |
|-------|-------|-------|
| -4.0  | 2.0   | Blue  |
| -3.5  | 1.5   | Blue  |
| -3.0  | 1.0   | Blue  |
| -2.5  | 0.5   | Blue  |
| -2.0  | 0.0   | Blue  |
| -1.5  | -0.5  | Blue  |
| -1.0  | -1.0  | Blue  |
| -0.5  | -1.5  | Blue  |
| 0.0   | -2.0  | Blue  |
| 0.5   | -2.5  | Blue  |
| 1.0   | -3.0  | Blue  |
| 1.5   | -3.5  | Blue  |
| 2.0   | -4.0  | Blue  |
| 2.5   | -4.5  | Blue  |
| 3.0   | -5.0  | Blue  |
| 3.5   | -5.5  | Blue  |
| -4.0  | -2.5  | Orange|
| -3.5  | -2.0  | Orange|
| -3.0  | -1.5  | Orange|
| -2.5  | -1.0  | Orange|
| -2.0  | -0.5  | Orange|
| -1.5  | 0.0   | Orange|
| -1.0  | 0.5   | Orange|
| -0.5  | 1.0   | Orange|
| 0.0   | 1.5   | Orange|
| 0.5   | 2.0   | Orange|
| 1.0   | 2.5   | Orange|
| 1.5   | 3.0   | Orange|
| 2.0   | 3.5   | Orange|
| 2.5   | 4.0   | Orange|
| 3.0   | 4.5   | Orange|
| 3.5   | 5.0   | Orange|
</details>

FIGURE 4.9. Left: The Bayes (purple dashed), LDA (black dotted), and QDA (green solid) decision boundaries for a two-class problem with $\Sigma_{1} = \Sigma_{2}$ . The shading indicates the QDA decision rule. Since the Bayes decision boundary is linear, it is more accurately approximated by LDA than by QDA. Right: Details are as given in the left-hand panel, except that $\Sigma_{1} \neq \Sigma_{2}$ . Since the Bayes decision boundary is non-linear, it is more accurately approximated by QDA than by LDA.

QDA, or vice-versa? The answer lies in the bias-variance trade-off. When there are $p$ predictors, then estimating a covariance matrix requires estimating $p(p + 1) / 2$ parameters. QDA estimates a separate covariance matrix for each class, for a total of $Kp(p + 1) / 2$ parameters. With 50 predictors this is some multiple of 1,275, which is a lot of parameters. By instead assuming that the $K$ classes share a common covariance matrix, the LDA model becomes linear in $x$ , which means there are $Kp$ linear coefficients to estimate. Consequently, LDA is a much less flexible classifier than QDA, and so has substantially lower variance. This can potentially lead to improved prediction performance. But there is a trade-off: if LDA's assumption that the $K$ classes share a common covariance matrix is badly off, then LDA can suffer from high bias. Roughly speaking, LDA tends to be a better bet than QDA if there are relatively few training observations and so reducing variance is crucial. In contrast, QDA is recommended if the training set is very large, so that the variance of the classifier is not a major concern, or if the assumption of a common covariance matrix for the $K$ classes is clearly untenable.

Figure 4.9 illustrates the performances of LDA and QDA in two scenarios. In the left-hand panel, the two Gaussian classes have a common correlation of 0.7 between $X_{1}$ and $X_{2}$ . As a result, the Bayes decision boundary is linear and is accurately approximated by the LDA decision boundary. The QDA decision boundary is inferior, because it suffers from higher variance without a corresponding decrease in bias. In contrast, the right-hand panel displays a situation in which the orange class has a correlation of 0.7 between the variables and the blue class has a correlation of -0.7. Now the Bayes decision boundary is quadratic, and so QDA more accurately approximates this boundary than does LDA.

# 4.4.4 Naive Bayes

In previous sections, we used Bayes' theorem (4.15) to develop the LDA and QDA classifiers. Here, we use Bayes' theorem to motivate the popular naive Bayes classifier.

Recall that Bayes' theorem (4.15) provides an expression for the posterior probability $p_k(x) = \Pr(Y = k|X = x)$ in terms of $\pi_1, \ldots, \pi_K$ and $f_1(x), \ldots, f_K(x)$ . To use (4.15) in practice, we need estimates for $\pi_1, \ldots, \pi_K$ and $f_1(x), \ldots, f_K(x)$ . As we saw in previous sections, estimating the prior probabilities $\pi_1, \ldots, \pi_K$ is typically straightforward: for instance, we can estimate $\hat{\pi}_k$ as the proportion of training observations belonging to the $k$ th class, for $k = 1, \ldots, K$ .

However, estimating $f_{1}(x),\ldots,f_{K}(x)$ is more subtle. Recall that $f_{k}(x)$ is the p-dimensional density function for an observation in the kth class, for $k=1,\ldots,K$ . In general, estimating a p-dimensional density function is challenging. In LDA, we make a very strong assumption that greatly simplifies the task: we assume that $f_{k}$ is the density function for a multivariate normal random variable with class-specific mean $\mu_{k}$ , and shared covariance matrix $\Sigma$ . By contrast, in QDA, we assume that $f_{k}$ is the density function for a multivariate normal random variable with class-specific mean $\mu_{k}$ , and class-specific covariance matrix $\Sigma_{k}$ . By making these very strong assumptions, we are able to replace the very challenging problem of estimating K p-dimensional density functions with the much simpler problem of estimating K p-dimensional mean vectors and one (in the case of LDA) or K (in the case of QDA) ( $p\times p$ )-dimensional covariance matrices.

The naive Bayes classifier takes a different tack for estimating $f_{1}(x),\ldots,f_{K}(x)$ . Instead of assuming that these functions belong to a particular family of distributions (e.g. multivariate normal), we instead make a single assumption:

Within the kth class, the p predictors are independent.

Stated mathematically, this assumption means that for $k = 1, \ldots, K$ ,

$$
f _ {k} (x) = f _ {k 1} (x _ {1}) \times f _ {k 2} (x _ {2}) \times \dots \times f _ {k p} (x _ {p}), \tag {4.29}
$$

where $f_{kj}$ is the density function of the $j$ th predictor among observations in the $k$ th class.

Why is this assumption so powerful? Essentially, estimating a p-dimensional density function is challenging because we must consider not only the marginal distribution of each predictor — that is, the distribution of each predictor on its own — but also the joint distribution of the predictors — that is, the association between the different predictors. In the case of a multivariate normal distribution, the association between the different predictors is summarized by the off-diagonal elements of the covariance matrix. However, in general, this association can be very hard to characterize, and exceedingly challenging to estimate. But by assuming that the p covariates are independent within each class, we completely eliminate the need to worry about the association between the p predictors, because we have simply assumed that there is no association between the predictors!

Do we really believe the naive Bayes assumption that the p covariates are independent within each class? In most settings, we do not. But even though this modeling assumption is made for convenience, it often leads to pretty decent results, especially in settings where n is not large enough relative to p for us to effectively estimate the joint distribution of the predictors within each class. In fact, since estimating a joint distribution requires such a huge amount of data, naive Bayes is a good choice in a wide range of settings. Essentially, the naive Bayes assumption introduces some bias, but reduces variance, leading to a classifier that works quite well in practice as a result of the bias-variance trade-off.

Once we have made the naive Bayes assumption, we can plug $(4.29)$ into $(4.15)$ to obtain an expression for the posterior probability,

$$
\operatorname * {P r} (Y = k \mid X = x) = \frac {\pi_ {k} \times f _ {k 1} \left(x _ {1}\right) \times f _ {k 2} \left(x _ {2}\right) \times \cdots \times f _ {k p} \left(x _ {p}\right)}{\sum_ {l = 1} ^ {K} \pi_ {l} \times f _ {l 1} \left(x _ {1}\right) \times f _ {l 2} \left(x _ {2}\right) \times \cdots \times f _ {l p} \left(x _ {p}\right)} \tag {4.30}
$$

for $k = 1, \ldots, K$ .

To estimate the one-dimensional density function $f_{kj}$ using training data $x_{1j},\ldots,x_{nj}$ , we have a few options.

- If $X_{j}$ is quantitative, then we can assume that $X_{j}|Y = k \sim N(\mu_{jk}, \sigma_{jk}^{2})$ . In other words, we assume that within each class, the $j$ th predictor is drawn from a (univariate) normal distribution. While this may sound a bit like QDA, there is one key difference, in that here we are assuming that the predictors are independent; this amounts to QDA with an additional assumption that the class-specific covariance matrix is diagonal.   
- If $X_{j}$ is quantitative, then another option is to use a non-parametric estimate for $f_{kj}$ . A very simple way to do this is by making a histogram for the observations of the $j$ th predictor within each class. Then we can estimate $f_{kj}(x_{j})$ as the fraction of the training observations in the $k$ th class that belong to the same histogram bin as $x_{j}$ . Alternatively, we can use a kernel density estimator, which is essentially a smoothed version of a histogram.   
- If $X_{j}$ is qualitative, then we can simply count the proportion of training observations for the $j$ th predictor corresponding to each class. For instance, suppose that $X_{j} \in \{1,2,3\}$ , and we have 100 observations in the $k$ th class. Suppose that the $j$ th predictor takes on values of 1, 2, and 3 in 32, 55, and 13 of those observations, respectively. Then we can estimate $f_{kj}$ as

$$
\hat {f} _ {k j} (x _ {j}) = \left\{ \begin{array}{l l} 0. 3 2 & \text { if } x _ {j} = 1 \\ 0. 5 5 & \text { if } x _ {j} = 2 \\ 0. 1 3 & \text { if } x _ {j} = 3. \end{array} \right.
$$

We now consider the naive Bayes classifier in a toy example with p = 3 predictors and K = 2 classes. The first two predictors are quantitative, and the third predictor is qualitative with three levels. Suppose further that $\hat{\pi}_{1} = \hat{\pi}_{2} = 0.5$ . The estimated density functions $\hat{f}_{kj}$ for k = 1, 2 and j = 1, 2, 3 are displayed in Figure 4.10. Now suppose that we wish to classify a new observation, $x^{*} = (0.4, 1.5, 1)^{T}$ . It turns out that in this

kernel
density
estimator

Density estimates for class k=1   
![](images/9e5d9da6f738f58d9075f5adb17e82386a4dbc0e428b7b87f32c60e3f6c32d7d.jpg)

Density estimates for class k=2   
$\hat{f}_{21}$   
![](images/1a4b6ddfe61a47fa77aa6e67784352b801c18485ba29c479da266e8e545071a3.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --------- | --------- |
| -4 to -3  | 1         |
| -3 to -2  | 3         |
| -2 to -1  | 8         |
| -1 to 0   | 10        |
| 0 to 1    | 5         |
| 1 to 2    | 2         |
| 2 to 3    | 1         |
| 3 to 4    | 0         |
</details>

$\hat{f}_{22}$   
![](images/704c2562de84d9a27a8974b7bfb64b95460ea530ecdfeb013ce23cfcdb8c3ab8.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --------- | --------- |
| -3 to -2  | 1         |
| -2 to -1  | 3         |
| -1 to 0   | 8         |
| 0 to 1    | 10        |
| 1 to 2    | 7         |
| 2 to 3    | 3         |
| 3 to 4    | 1         |
</details>

$\hat{f}_{23}$   
![](images/7aff69c31a0346dfa1fa3dc8012be83ba04d22b176cb43afa5914c79cef6c82b.jpg)

![](images/ee8148ab6ac126aacc5d92ffe9659584349b3351958d4875e179a8f916b8759e.jpg)

![](images/dd6b360684d8c246908600fb734422ffacd554bb25fdc27a5f6163c4e5664a43.jpg)

FIGURE 4.10. In the toy example in Section 4.4.4, we generate data with p = 3 predictors and K = 2 classes. The first two predictors are quantitative, and the third predictor is qualitative with three levels. In each class, the estimated density for each of the three predictors is displayed. If the prior probabilities for the two classes are equal, then the observation $x^{*} = (0.4, 1.5, 1)^{T}$ has a 94.4% posterior probability of belonging to the first class. 

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">True default status</td></tr><tr><td>No</td><td>Yes</td><td>Total</td></tr><tr><td rowspan="3">Predicted default status</td><td>No</td><td>9621</td><td>244</td><td>9865</td></tr><tr><td>Yes</td><td>46</td><td>89</td><td>135</td></tr><tr><td>Total</td><td>9667</td><td>333</td><td>10000</td></tr></table>

TABLE 4.8. Comparison of the naive Bayes predictions to the true default status for the 10,000 training observations in the Default data set, when we predict default for any observation for which $P(Y = \text{default}|X = x) > 0.5$ .

example, $\hat{f}_{11}(0.4) = 0.368$ , $\hat{f}_{12}(1.5) = 0.484$ , $\hat{f}_{13}(1) = 0.226$ , and $\hat{f}_{21}(0.4) = 0.030$ , $\hat{f}_{22}(1.5) = 0.130$ , $\hat{f}_{23}(1) = 0.616$ . Plugging these estimates into (4.30) results in posterior probability estimates of $\Pr(Y = 1|X = x^*) = 0.944$ and $\Pr(Y = 2|X = x^*) = 0.056$ .

Table 4.8 provides the confusion matrix resulting from applying the naive Bayes classifier to the Default data set, where we predict a default if the posterior probability of a default — that is, $P(Y = \text{default}|X = x)$ — exceeds 0.5. Comparing this to the results for LDA in Table 4.4, our findings are mixed. While LDA has a slightly lower overall error rate, naive Bayes correctly predicts a higher fraction of the true defaulters. In this implementation of naive Bayes, we have assumed that each quantitative predictor is drawn from a Gaussian distribution (and, of course, that within each class, each predictor is independent).

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">True default status</td></tr><tr><td>No</td><td>Yes</td><td>Total</td></tr><tr><td rowspan="3">Predicted default status</td><td>No</td><td>9339</td><td>130</td><td>9469</td></tr><tr><td>Yes</td><td>328</td><td>203</td><td>531</td></tr><tr><td>Total</td><td>9667</td><td>333</td><td>10000</td></tr></table>

TABLE 4.9. Comparison of the naive Bayes predictions to the true default status for the 10,000 training observations in the Default data set, when we predict default for any observation for which $P(Y = \text{default}|X = x) > 0.2$ .

Just as with LDA, we can easily adjust the probability threshold for predicting a default. For example, Table 4.9 provides the confusion matrix resulting from predicting a default if $P(Y = \text{default}|X = x) > 0.2$ . Again, the results are mixed relative to LDA with the same threshold (Table 4.5). Naive Bayes has a higher error rate, but correctly predicts almost two-thirds of the true defaults.

In this example, it should not be too surprising that naive Bayes does not convincingly outperform LDA: this data set has n = 10,000 and p = 2, and so the reduction in variance resulting from the naive Bayes assumption is not necessarily worthwhile. We expect to see a greater pay-off to using naive Bayes relative to LDA or QDA in instances where p is larger or n is smaller, so that reducing the variance is very important.

# 4.5 A Comparison of Classification Methods

# 4.5.1 An Analytical Comparison

We now perform an analytical (or mathematical) comparison of LDA, QDA, naive Bayes, and logistic regression. We consider these approaches in a setting with K classes, so that we assign an observation to the class that maximizes $\Pr(Y = k|X = x)$ . Equivalently, we can set K as the baseline class and assign an observation to the class that maximizes

$$
\log \left(\frac {\operatorname* {P r} (Y = k | X = x)}{\operatorname* {P r} (Y = K | X = x)}\right) \tag {4.31}
$$

for $k = 1, \ldots, K$ . Examining the specific form of (4.31) for each method provides a clear understanding of their similarities and differences.

First, for LDA, we can make use of Bayes' theorem (4.15) as well as the assumption that the predictors within each class are drawn from a multivariate normal density (4.23) with class-specific mean and shared covariance matrix in order to show that

$$
\begin{array}{l} \log \left(\frac {\operatorname* {P r} (Y = k | X = x)}{\operatorname* {P r} (Y = K | X = x)}\right) = \log \left(\frac {\pi_ {k} f _ {k} (x)}{\pi_ {K} f _ {K} (x)}\right) \\ { = } { \log \left( \frac { \pi _ { k } \exp \left( - \frac { 1 } { 2 } ( x - \mu _ { k } ) ^ { T } \pmb { \Sigma } ^ { - 1 } ( x - \mu _ { k } ) \right) } { \pi _ { K } \exp \left( - \frac { 1 } { 2 } ( x - \mu _ { K } ) ^ { T } \pmb { \Sigma } ^ { - 1 } ( x - \mu _ { K } ) \right) } \right) } \\ = \log \left(\frac {\pi_ {k}}{\pi_ {K}}\right) - \frac {1}{2} (x - \mu_ {k}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (x - \mu_ {k}) \\ + \frac {1}{2} (x - \mu_ {K}) ^ {T} \pmb {\Sigma} ^ {- 1} (x - \mu_ {K}) \\ = \log \left(\frac {\pi_ {k}}{\pi_ {K}}\right) - \frac {1}{2} (\mu_ {k} + \mu_ {K}) ^ {T} \boldsymbol {\Sigma} ^ {- 1} (\mu_ {k} - \mu_ {K}) \\ + x ^ {T} \pmb {\Sigma} ^ {- 1} (\mu_ {k} - \mu_ {K}) \\ = a _ {k} + \sum_ {j = 1} ^ {p} b _ {k j} x _ {j}, \tag {4.32} \\ \end{array}
$$

where $a_{k} = \log \left(\frac{\pi_{k}}{\pi_{K}}\right) - \frac{1}{2} (\mu_{k} + \mu_{K})^{T}\pmb{\Sigma}^{-1}(\mu_{k} - \mu_{K})$ and $b_{kj}$ is the $j$ th component of $\pmb{\Sigma}^{-1}(\mu_k - \mu_K)$ . Hence LDA, like logistic regression, assumes that the log odds of the posterior probabilities is linear in $x$ .

Using similar calculations, in the QDA setting (4.31) becomes

$$
\log \left(\frac {\operatorname* {P r} (Y = k | X = x)}{\operatorname* {P r} (Y = K | X = x)}\right) = a _ {k} + \sum_ {j = 1} ^ {p} b _ {k j} x _ {j} + \sum_ {j = 1} ^ {p} \sum_ {l = 1} ^ {p} c _ {k j l} x _ {j} x _ {l}, \tag {4.33}
$$

where $a_{k}, b_{kj}$ , and $c_{kjl}$ are functions of $\pi_{k}, \pi_{K}, \mu_{k}, \mu_{K}, \Sigma_{k}$ and $\Sigma_{K}$ . Again, as the name suggests, QDA assumes that the log odds of the posterior probabilities is quadratic in x.

Finally, we examine (4.31) in the naive Bayes setting. Recall that in this setting, $f_{k}(x)$ is modeled as a product of p one-dimensional functions $f_{kj}(x_{j})$ for $j=1,\ldots,p$ . Hence,

$$
\begin{array}{l} \log \left(\frac {\operatorname* {P r} (Y = k | X = x)}{\operatorname* {P r} (Y = K | X = x)}\right) = \log \left(\frac {\pi_ {k} f _ {k} (x)}{\pi_ {K} f _ {K} (x)}\right) \\ = \log \left(\frac {\pi_ {k} \prod_ {j = 1} ^ {p} f _ {k j} (x _ {j})}{\pi_ {K} \prod_ {j = 1} ^ {p} f _ {K j} (x _ {j})}\right) \\ = \log \left(\frac {\pi_ {k}}{\pi_ {K}}\right) + \sum_ {j = 1} ^ {p} \log \left(\frac {f _ {k j} (x _ {j})}{f _ {K j} (x _ {j})}\right) \\ = a _ {k} + \sum_ {j = 1} ^ {p} g _ {k j} (x _ {j}), \tag {4.34} \\ \end{array}
$$

where $a_{k} = \log\left(\frac{\pi_{k}}{\pi_{K}}\right)$ and $g_{kj}(x_{j}) = \log\left(\frac{f_{kj}(x_{j})}{f_{Kj}(x_{j})}\right)$ . Hence, the right-hand side of (4.34) takes the form of a generalized additive model, a topic that is discussed further in Chapter 7.

Inspection of $(4.32)$ , $(4.33)$ , and $(4.34)$ yields the following observations about LDA, QDA, and naive Bayes:

- LDA is a special case of QDA with $c_{kjl} = 0$ for all $j = 1, \ldots, p$ , $l = 1, \ldots, p$ , and $k = 1, \ldots, K$ . (Of course, this is not surprising, since LDA is simply a restricted version of QDA with $\Sigma_{1} = \cdots = \Sigma_{K} = \Sigma$ .)   
- Any classifier with a linear decision boundary is a special case of naive Bayes with $g_{kj}(x_j) = b_{kj}x_j$ . In particular, this means that LDA is a special case of naive Bayes! This is not at all obvious from the descriptions of LDA and naive Bayes earlier in this chapter, since each method makes very different assumptions: LDA assumes that the features are normally distributed with a common within-class covariance matrix, and naive Bayes instead assumes independence of the features.   
- If we model $f_{kj}(x_j)$ in the naive Bayes classifier using a one-dimensional Gaussian distribution $N(\mu_{kj},\sigma_j^2)$ , then we end up with $g_{kj}(x_j)=b_{kj}x_j$ where $b_{kj}=(\mu_{kj}-\mu_{Kj})/\sigma_j^2$ . In this case, naive Bayes is actually a special case of LDA with $\Sigma$ restricted to be a diagonal matrix with jth diagonal element equal to $\sigma_j^2$ .   
- Neither QDA nor naive Bayes is a special case of the other. Naive Bayes can produce a more flexible fit, since any choice can be made for $g_{kj}(x_j)$ . However, it is restricted to a purely additive fit, in the sense that in (4.34), a function of $x_j$ is added to a function of $x_l$ , for $j \neq l$ ; however, these terms are never multiplied. By contrast, QDA includes multiplicative terms of the form $c_{kjl}x_jx_l$ . Therefore, QDA has the potential to be more accurate in settings where interactions among the predictors are important in discriminating between classes.

None of these methods uniformly dominates the others: in any setting, the choice of method will depend on the true distribution of the predictors in each of the K classes, as well as other considerations, such as the values of n and p. The latter ties into the bias-variance trade-off.

How does logistic regression tie into this story? Recall from $(4.12)$ that multinomial logistic regression takes the form

$$
\log \left(\frac {\operatorname * {P r} (Y = k | X = x)}{\operatorname * {P r} (Y = K | X = x)}\right) = \beta_ {k 0} + \sum_ {j = 1} ^ {p} \beta_ {k j} x _ {j}.
$$

This is identical to the linear form of LDA (4.32): in both cases, $\log\left(\frac{\Pr(Y=k|X=x)}{\Pr(Y=K|X=x)}\right)$ is a linear function of the predictors. In LDA, the coefficients in this linear function are functions of estimates for $\pi_{k}$ , $\pi_{K}$ , $\mu_{k}$ , $\mu_{K}$ , and $\Sigma$ obtained by assuming that $X_{1},\ldots,X_{p}$ follow a normal distribution within each class. By contrast, in logistic regression, the coefficients are chosen to maximize the likelihood function (4.5). Thus, we expect LDA to outperform logistic regression when the normality assumption (approximately) holds, and we expect logistic regression to perform better when it does not.

We close with a brief discussion of K-nearest neighbors (KNN), introduced in Chapter 2. Recall that KNN takes a completely different approach from the classifiers seen in this chapter. In order to make a prediction for an observation X = x, the training observations that are closest to x are identified. Then X is assigned to the class to which the plurality of these observations belong. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary. We make the following observations about KNN:

- Because KNN is completely non-parametric, we can expect this approach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that n is very large and p is small.   
- In order to provide accurate classification, KNN requires a lot of observations relative to the number of predictors—that is, n much larger than p. This has to do with the fact that KNN is non-parametric, and thus tends to reduce the bias while incurring a lot of variance.   
- In settings where the decision boundary is non-linear but n is only modest, or p is not very small, then QDA may be preferred to KNN. This is because QDA can provide a non-linear decision boundary while taking advantage of a parametric form, which means that it requires a smaller sample size for accurate classification, relative to KNN.   
- Unlike logistic regression, KNN does not tell us which predictors are important: we don't get a table of coefficients as in Table 4.3.

# 4.5.2 An Empirical Comparison

We now compare the empirical (practical) performance of logistic regression, LDA, QDA, naive Bayes, and KNN. We generated data from six different scenarios, each of which involves a binary (two-class) classification problem. In three of the scenarios, the Bayes decision boundary is linear, and in the remaining scenarios it is non-linear. For each scenario, we produced 100 random training data sets. On each of these training sets, we fit each method to the data and computed the resulting test error rate on a large test set. Results for the linear scenarios are shown in Figure 4.11, and the results for the non-linear scenarios are in Figure 4.12. The KNN method requires selection of $K$ , the number of neighbors (not to be confused with the number of classes in earlier sections of this chapter). We performed KNN with two values of $K$ : $K = 1$ , and a value of $K$ that was chosen automatically using an approach called cross-validation, which we discuss further in Chapter 5. We applied naive Bayes assuming univariate Gaussian densities for the features within each class (and, of course — since this is the key characteristic of naive Bayes — assuming independence of the features).

In each of the six scenarios, there were $p = 2$ quantitative predictors. The scenarios were as follows:

![](images/286b807af9087bb3dd909363c95b1676f20a5314fe28ebf89aec81eac9ea66d5.jpg)

<details>
<summary>boxplot</summary>

| Method   | Min  | Q1   | Median | Q3   | Max  |
| -------- | ---- | ---- | ------ | ---- | ---- |
| KNN-1    | 0.27 | 0.31 | 0.33   | 0.35 | 0.45 |
| KNN-CV   | 0.26 | 0.29 | 0.28   | 0.30 | 0.36 |
| LDA      | 0.25 | 0.26 | 0.25   | 0.27 | 0.29 |
| Logistic | 0.24 | 0.25 | 0.24   | 0.26 | 0.28 |
| NBayes   | 0.23 | 0.24 | 0.23   | 0.25 | 0.27 |
| QDA      | 0.22 | 0.25 | 0.24   | 0.26 | 0.29 |
</details>

![](images/eb2e623b3632ef9ca1120a615f138c4309f4aec0a7b106c5be6a530dea8a7500.jpg)

<details>
<summary>boxplot</summary>

| Method   | Min  | Q1   | Median | Q3   | Max  |
| -------- | ---- | ---- | ------ | ---- | ---- |
| KNN-1    | 0.17 | 0.24 | 0.23   | 0.26 | 0.31 |
| KNN-CV   | 0.15 | 0.20 | 0.19   | 0.21 | 0.25 |
| LDA      | 0.14 | 0.18 | 0.17   | 0.19 | 0.20 |
| Logistic | 0.14 | 0.17 | 0.16   | 0.18 | 0.20 |
| NBayes   | 0.15 | 0.19 | 0.18   | 0.20 | 0.27 |
| QDA      | 0.14 | 0.18 | 0.17   | 0.19 | 0.21 |
</details>

![](images/e8979192a91d09c1befc5ff7b4264091a27a9a7ecf0c9450ef06335569fcff4f.jpg)

<details>
<summary>boxplot</summary>

| Method   | Min  | Q1   | Median | Q3   | Max  |
| -------- | ---- | ---- | ------ | ---- | ---- |
| KNN-1    | 0.20 | 0.30 | 0.32   | 0.34 | 0.38 |
| KNN-CV   | 0.20 | 0.25 | 0.27   | 0.29 | 0.31 |
| LDA      | 0.20 | 0.26 | 0.28   | 0.30 | 0.33 |
| Logistic | 0.20 | 0.24 | 0.26   | 0.28 | 0.31 |
| NBayes   | 0.20 | 0.40 | 0.42   | 0.44 | 0.48 |
| QDA      | 0.20 | 0.38 | 0.39   | 0.41 | 0.45 |
</details>

FIGURE 4.11. Boxplots of the test error rates for each of the linear scenarios described in the main text.

Scenario 1: There were 20 training observations in each of two classes. The observations within each class were uncorrelated random normal variables with a different mean in each class. The left-hand panel of Figure 4.11 shows that LDA performed well in this setting, as one would expect since this is the model assumed by LDA. Logistic regression also performed quite well, since it assumes a linear decision boundary. KNN performed poorly because it paid a price in terms of variance that was not offset by a reduction in bias. QDA also performed worse than LDA, since it fit a more flexible classifier than necessary. The performance of naive Bayes was slightly better than QDA, because the naive Bayes assumption of independent predictors is correct.

Scenario 2: Details are as in Scenario 1, except that within each class, the two predictors had a correlation of -0.5. The center panel of Figure 4.11 indicates that the performance of most methods is similar to the previous scenario. The notable exception is naive Bayes, which performs very poorly here, since the naive Bayes assumption of independent predictors is violated.

Scenario 3: As in the previous scenario, there is substantial negative correlation between the predictors within each class. However, this time we generated $X_{1}$ and $X_{2}$ from the t-distribution, with 50 observations per class. The t-distribution has a similar shape to the normal distribution, but it has a tendency to yield more extreme points—that is, more points that are far from the mean. In this setting, the decision boundary was still linear, and so fit into the logistic regression framework. The set-up violated the assumptions of LDA, since the observations were not drawn from a normal distribution. The right-hand panel of Figure 4.11 shows that logistic regression outperformed LDA, though both methods were superior to the other approaches. In particular, the QDA results deteriorated considerably as a consequence of non-normality. Naive Bayes performed very poorly because the independence assumption is violated.

Scenario 4: The data were generated from a normal distribution, with a correlation of 0.5 between the predictors in the first class, and correlation of -0.5 between the predictors in the second class. This setup corresponded to the QDA assumption, and resulted in quadratic decision boundaries. The left-hand panel of Figure 4.12 shows that QDA outperformed all of the other approaches. The naive Bayes assumption of independent predictors is violated, so naive Bayes performs poorly.

![](images/f41dea387648f29288aac4f90c53547b75cd0c0efdb22ec2856b20c0924ba24b.jpg)

<details>
<summary>boxplot</summary>

| Method   | Min  | Q1   | Median | Q3   | Max  |
| -------- | ---- | ---- | ------ | ---- | ---- |
| KNN-1    | 0.25 | 0.35 | 0.37   | 0.38 | 0.40 |
| KNN-CV   | 0.20 | 0.32 | 0.34   | 0.36 | 0.39 |
| LDA      | 0.28 | 0.36 | 0.37   | 0.38 | 0.40 |
| Logistic | 0.25 | 0.35 | 0.36   | 0.37 | 0.39 |
| NBayes   | 0.28 | 0.38 | 0.39   | 0.40 | 0.41 |
| QDA      | 0.22 | 0.31 | 0.32   | 0.33 | 0.34 |
</details>

![](images/d11d9bb88d3f0fd2b404f88f75bdafba392c5eb74fafe5672fc7d8f4eb6afd03.jpg)

<details>
<summary>boxplot</summary>

| Method    | Min  | Q1   | Median | Q3   | Max  |
|-----------|------|------|--------|------|------|
| KNN-1     | 0.18 | 0.24 | 0.26   | 0.28 | 0.32 |
| KNN-CV    | 0.18 | 0.20 | 0.22   | 0.24 | 0.28 |
| LDA       | 0.18 | 0.22 | 0.24   | 0.26 | 0.30 |
| Logistic  | 0.18 | 0.22 | 0.24   | 0.26 | 0.28 |
| NBayes    | 0.18 | 0.22 | 0.24   | 0.26 | 0.28 |
| QDA       | 0.18 | 0.22 | 0.24   | 0.26 | 0.28 |
</details>

![](images/fa2cd03047068b9f51b83786860f00503a83b29a17445115a2d3aff5faaa49cf.jpg)

<details>
<summary>boxplot</summary>

| Method   | Min  | Q1   | Median | Q3   | Max  |
| -------- | ---- | ---- | ------ | ---- | ---- |
| KNN-1    | 0.15 | 0.20 | 0.22   | 0.25 | 0.28 |
| KNN-CV   | 0.15 | 0.20 | 0.22   | 0.25 | 0.28 |
| LDA      | 0.15 | 0.20 | 0.22   | 0.25 | 0.28 |
| Logistic | 0.15 | 0.20 | 0.22   | 0.25 | 0.28 |
| NBayes   | 0.15 | 0.18 | 0.19   | 0.21 | 0.23 |
| QDA      | 0.15 | 0.19 | 0.20   | 0.22 | 0.24 |
</details>

FIGURE 4.12. Boxplots of the test error rates for each of the non-linear scenarios described in the main text.

Scenario 5: The data were generated from a normal distribution with uncorrelated predictors. Then the responses were sampled from the logistic function applied to a complicated non-linear function of the predictors. The center panel of Figure 4.12 shows that both QDA and naive Bayes gave slightly better results than the linear methods, while the much more flexible KNN-CV method gave the best results. But KNN with K = 1 gave the worst results out of all methods. This highlights the fact that even when the data exhibits a complex non-linear relationship, a non-parametric method such as KNN can still give poor results if the level of smoothness is not chosen correctly.

Scenario 6: The observations were generated from a normal distribution with a different diagonal covariance matrix for each class. However, the sample size was very small: just n = 6 in each class. Naive Bayes performed very well, because its assumptions are met. LDA and logistic regression performed poorly because the true decision boundary is non-linear, due to the unequal covariance matrices. QDA performed a bit worse than naive Bayes, because given the very small sample size, the former incurred too much variance in estimating the correlation between the predictors within each class. KNN's performance also suffered due to the very small sample size.

These six examples illustrate that no one method will dominate the others in every situation. When the true decision boundaries are linear, then the LDA and logistic regression approaches will tend to perform well. When the boundaries are moderately non-linear, QDA or naive Bayes may give better results. Finally, for much more complicated decision boundaries, a non-parametric approach such as KNN can be superior. But the level of smoothness for a non-parametric approach must be chosen carefully. In the next chapter we examine a number of approaches for choosing the correct level of smoothness and, in general, for selecting the best overall method.

Finally, recall from Chapter 3 that in the regression setting we can accommodate a non-linear relationship between the predictors and the response by performing regression using transformations of the predictors. A similar approach could be taken in the classification setting. For instance, we could create a more flexible version of logistic regression by including $X^{2}$ , $X^{3}$ , and even $X^{4}$ as predictors. This may or may not improve logistic regression's performance, depending on whether the increase in variance due to the added flexibility is offset by a sufficiently large reduction in bias. We could do the same for LDA. If we added all possible quadratic terms and cross-products to LDA, the form of the model would be the same as the QDA model, although the parameter estimates would be different. This device allows us to move somewhere between an LDA and a QDA model.

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>t-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>73.60</td><td>5.13</td><td>14.34</td><td>0.00</td></tr><tr><td>workingday</td><td>1.27</td><td>1.78</td><td>0.71</td><td>0.48</td></tr><tr><td>temp</td><td>157.21</td><td>10.26</td><td>15.32</td><td>0.00</td></tr><tr><td>weathersit[cloudy/misty]</td><td>-12.89</td><td>1.96</td><td>-6.56</td><td>0.00</td></tr><tr><td>weathersit[light rain/snow]</td><td>-66.49</td><td>2.97</td><td>-22.43</td><td>0.00</td></tr><tr><td>weathersit[heavy rain/snow]</td><td>-109.75</td><td>76.67</td><td>-1.43</td><td>0.15</td></tr></table>

TABLE 4.10. Results for a least squares linear model fit to predict bikers in the Bikeshare data. The predictors mth and hr are omitted from this table due to space constraints, and can be seen in Figure 4.13. For the qualitative variable weathersit, the baseline level corresponds to clear skies.

# 4.6 Generalized Linear Models

In Chapter 3, we assumed that the response Y is quantitative, and explored the use of least squares linear regression to predict Y. Thus far in this chapter, we have instead assumed that Y is qualitative. However, we may sometimes be faced with situations in which Y is neither qualitative nor quantitative, and so neither linear regression from Chapter 3 nor the classification approaches covered in this chapter is applicable.

As a concrete example, we consider the Bikeshare data set. The response is bikers, the number of hourly users of a bike sharing program in Washington, DC. This response value is neither qualitative nor quantitative: instead, it takes on non-negative integer values, or counts. We will consider predicting bikers using the covariates mnth (month of the year), hr (hour of the day, from 0 to 23), workingday (an indicator variable that equals 1 if it is neither a weekend nor a holiday), temp (the normalized temperature, in Celsius), and weathersit (a qualitative variable that takes on one of four possible values: clear; misty or cloudy; light rain or light snow; or heavy rain or heavy snow.)

In the analyses that follow, we will treat mnth, hr, and weathersit as qualitative variables.

# 4.6.1 Linear Regression on the Bikeshare Data

To begin, we consider predicting bikers using linear regression. The results are shown in Table 4.10.

We see, for example, that a progression of weather from clear to cloudy results in, on average, 12.89 fewer bikers per hour; however, if the weather progresses further to rain or snow, then this further results in 53.60 fewer bikers per hour. Figure 4.13 displays the coefficients associated with mnth and the coefficients associated with hr. We see that bike usage is highest in the spring and fall, and lowest during the winter months. Furthermore, bike usage is greatest around rush hour (9 AM and 6 PM), and lowest overnight. Thus, at first glance, fitting a linear regression model to the Bikeshare data set seems to provide reasonable and intuitive results.

![](images/6c80d311085eee7def4d5a1a6882c2ed0b3435d161f0506c204099daff06443f.jpg)

<details>
<summary>line</summary>

| Month | Coefficient |
|-------|-------------|
| J     | -48         |
| F     | -38         |
| M     | -28         |
| A     | -5          |
| M     | 25          |
| J     | 20          |
| J     | 0           |
| A     | 10          |
| S     | 20          |
| O     | 25          |
| N     | 15          |
| D     | 0           |
</details>

![](images/77a5d6b990845b8ac2b45df3b6713a22726429af1d7b785b58b7dc13dba211cd.jpg)

<details>
<summary>line</summary>

| Hour | Coefficient |
| ---- | ----------- |
| 1    | -80         |
| 2    | -90         |
| 3    | -100        |
| 4    | -110        |
| 5    | -120        |
| 6    | -130        |
| 7    | -100        |
| 8    | 30          |
| 9    | 120         |
| 10   | 30          |
| 11   | -20         |
| 12   | 10          |
| 13   | 40          |
| 14   | 45          |
| 15   | 35          |
| 16   | 40          |
| 17   | 80          |
| 18   | 200         |
| 19   | 180         |
| 20   | 90          |
| 21   | 30          |
| 22   | -20         |
| 23   | -40         |
| 24   | -60         |
| 25+  | -80         |
</details>

FIGURE 4.13. A least squares linear regression model was fit to predict bikers in the Bikeshare data set. Left: The coefficients associated with the month of the year. Bike usage is highest in the spring and fall, and lowest in the winter. Right: The coefficients associated with the hour of the day. Bike usage is highest during peak commute times, and lowest overnight.

But upon more careful inspection, some issues become apparent. For example, 9.6% of the fitted values in the Bikeshare data set are negative: that is, the linear regression model predicts a negative number of users during 9.6% of the hours in the data set. This calls into question our ability to perform meaningful predictions on the data, and it also raises concerns about the accuracy of the coefficient estimates, confidence intervals, and other outputs of the regression model.

Furthermore, it is reasonable to suspect that when the expected value of bikers is small, the variance of bikers should be small as well. For instance, at 2 AM during a heavy December snow storm, we expect that extremely few people will use a bike, and moreover that there should be little variance associated with the number of users during those conditions. This is borne out in the data: between 1 AM and 4 AM, in December, January, and February, when it is raining, there are 5.05 users, on average, with a standard deviation of 3.73. By contrast, between 7 AM and 10 AM, in April, May, and June, when skies are clear, there are 243.59 users, on average, with a standard deviation of 131.7. The mean-variance relationship is displayed in the left-hand panel of Figure 4.14. This is a major violation of the assumptions of a linear model, which state that $Y = \sum_{j=1}^{p} X_j \beta_j + \epsilon$ , where $\epsilon$ is a mean-zero error term with variance $\sigma^2$ that is constant, and not a function of the covariates. Therefore, the heteroscedasticity of the data calls into question the suitability of a linear regression model.

Finally, the response bikers is integer-valued. But under a linear model, $Y = \beta_{0} + \sum_{j=1}^{p} X_{j} \beta_{j} + \epsilon$ , where $\epsilon$ is a continuous-valued error term. This means that in a linear model, the response Y is necessarily continuous-valued (quantitative). Thus, the integer nature of the response bikers suggests that a linear regression model is not entirely satisfactory for this data set.

![](images/4909b2105d6bf66514dcf48290580ac3e5af03a8144e754735087fae2586bff5.jpg)

<details>
<summary>bar_line</summary>

| Hour | Number of Bikers |
| ---- | ---------------- |
| 0    | 0                |
| 1    | 50               |
| 2    | 100              |
| 3    | 150              |
| 4    | 200              |
| 5    | 250              |
| 6    | 300              |
| 7    | 350              |
| 8    | 400              |
| 9    | 450              |
| 10   | 500              |
| 11   | 550              |
| 12   | 600              |
| 13   | 550              |
| 14   | 500              |
| 15   | 450              |
| 16   | 400              |
| 17   | 350              |
| 18   | 300              |
| 19   | 250              |
| 20   | 200              |
| 21   | 150              |
| 22   | 100              |
| 23   | 50               |
</details>

![](images/7b14bc31dcfb4e8f59c582c8c692f9ac3d34f895a055ac98b1bf538e92603594.jpg)

<details>
<summary>line</summary>

| Hour | Log(Number of Bikers) |
| ---- | --------------------- |
| 0    | 0                     |
| 1    | 1                     |
| 2    | 2                     |
| 3    | 3                     |
| 4    | 4                     |
| 5    | 5                     |
| 6    | 4                     |
| 7    | 3                     |
| 8    | 2                     |
| 9    | 1                     |
| 10   | 2                     |
| 11   | 3                     |
| 12   | 4                     |
| 13   | 5                     |
| 14   | 4                     |
| 15   | 3                     |
| 16   | 2                     |
| 17   | 1                     |
| 18   | 2                     |
| 19   | 3                     |
| 20   | 4                     |
| 21   | 5                     |
| 22   | 4                     |
| 23   | 3                     |
| 24   | 2                     |
</details>

FIGURE 4.14. Left: On the Bikeshare dataset, the number of bikers is displayed on the y-axis, and the hour of the day is displayed on the x-axis. Jitter was applied for ease of visualization. For the most part, as the mean number of bikers increases, so does the variance in the number of bikers. A smoothing spline fit is shown in green. Right: The log of the number of bikers is now displayed on the y-axis.

Some of the problems that arise when fitting a linear regression model to the Bikeshare data can be overcome by transforming the response; for instance, we can fit the model

$$
\log (Y) = \sum_ {j = 1} ^ {p} X _ {j} \beta_ {j} + \epsilon .
$$

Transforming the response avoids the possibility of negative predictions, and it overcomes much of the heteroscedasticity in the untransformed data, as is shown in the right-hand panel of Figure 4.14. However, it is not quite a satisfactory solution, since predictions and inference are made in terms of the log of the response, rather than the response. This leads to challenges in interpretation, e.g. “a one-unit increase in $X_{j}$ is associated with an increase in the mean of the log of Y by an amount $\beta_{j}$ ”. Furthermore, a log transformation of the response cannot be applied in settings where the response can take on a value of 0. Thus, while fitting a linear model to a transformation of the response may be an adequate approach for some count-valued data sets, it often leaves something to be desired. We will see in the next section that a Poisson regression model provides a much more natural and elegant approach for this task.

# 4.6.2 Poisson Regression on the Bikeshare Data

To overcome the inadequacies of linear regression for analyzing the Bikeshare data set, we will make use of an alternative approach, called Poisson regression. Before we can talk about Poisson regression, we must first introduce the Poisson distribution.

Suppose that a random variable Y takes on nonnegative integer values, i.e. $Y \in \{0, 1, 2, \ldots\}$ . If Y follows the Poisson distribution, then

$$
\operatorname * {P r} (Y = k) = \frac {e ^ {- \lambda} \lambda^ {k}}{k !} \text {   for   } k = 0, 1, 2, \dots . \tag {4.35}
$$

![](images/2640b2fdbda5da45668a273c0a8230118ffae39bc92b141470d81ce5b28a4330.jpg)

Poisson
regression
Poisson
distribution

Here, $\lambda > 0$ is the expected value of Y, i.e. $\mathrm{E}(Y)$ . It turns out that $\lambda$ also equals the variance of Y, i.e. $\lambda = \mathrm{E}(Y) = \mathrm{Var}(Y)$ . This means that if Y follows the Poisson distribution, then the larger the mean of Y, the larger its variance. (In (4.35), the notation $k!$ , pronounced “k factorial”, is defined as $k! = k \times (k - 1) \times (k - 2) \times \ldots \times 3 \times 2 \times 1$ .)

The Poisson distribution is typically used to model counts; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values. To see how we might use the Poisson distribution in practice, let Y denote the number of users of the bike sharing program during a particular hour of the day, under a particular set of weather conditions, and during a particular month of the year. We might model Y as a Poisson distribution with mean $\mathrm{E}(Y)=\lambda=5$ . This means that the probability of no users during this particular hour is $\Pr(Y=0)=\frac{e^{-5}5^{0}}{0!}=e^{-5}=0.0067$ (where $0!=1$ by convention). The probability that there is exactly one user is $\Pr(Y=1)=\frac{e^{-5}5^{1}}{1!}=5e^{-5}=0.034$ , the probability of two users is $\Pr(Y=2)=\frac{e^{-5}5^{2}}{2!}=0.084$ , and so on.

Of course, in reality, we expect the mean number of users of the bike sharing program, $\lambda = \mathrm{E}(Y)$ , to vary as a function of the hour of the day, the month of the year, the weather conditions, and so forth. So rather than modeling the number of bikers, Y, as a Poisson distribution with a fixed mean value like $\lambda = 5$ , we would like to allow the mean to vary as a function of the covariates. In particular, we consider the following model for the mean $\lambda = \mathrm{E}(Y)$ , which we now write as $\lambda(X_{1}, \ldots, X_{p})$ to emphasize that it is a function of the covariates $X_{1}, \ldots, X_{p}$ :

$$
\log (\lambda (X _ {1}, \dots , X _ {p})) = \beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p} \tag {4.36}
$$

or equivalently

$$
\lambda (X _ {1}, \dots , X _ {p}) = e ^ {\beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}}. \tag {4.37}
$$

Here, $\beta_0, \beta_1, \ldots, \beta_p$ are parameters to be estimated. Together, (4.35) and (4.36) define the Poisson regression model. Notice that in (4.36), we take the log of $\lambda(X_1, \ldots, X_p)$ to be linear in $X_1, \ldots, X_p$ , rather than having $\lambda(X_1, \ldots, X_p)$ itself be linear in $X_1, \ldots, X_p$ ; this ensures that $\lambda(X_1, \ldots, X_p)$ takes on nonnegative values for all values of the covariates.

To estimate the coefficients $\beta_{0},\beta_{1},\ldots,\beta_{p}$ , we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2. Specifically, given n independent observations from the Poisson regression model, the likelihood takes the form

$$
\ell (\beta_ {0}, \beta_ {1}, \dots , \beta_ {p}) = \prod_ {i = 1} ^ {n} \frac {e ^ {- \lambda (x _ {i})} \lambda (x _ {i}) ^ {y _ {i}}}{y _ {i} !}, \tag {4.38}
$$

where $\lambda(x_{i}) = e^{\beta_{0} + \beta_{1}x_{i1} + \cdots + \beta_{p}x_{ip}}$ , due to (4.37). We estimate the coefficients that maximize the likelihood $\ell(\beta_{0}, \beta_{1}, \ldots, \beta_{p})$ , i.e. that make the observed data as likely as possible.

We now fit a Poisson regression model to the Bikeshare data set. The results are shown in Table 4.11 and Figure 4.15. Qualitatively, the results are similar to those from linear regression in Section 4.6.1. We again see that bike usage is highest in the spring and fall and during rush hour, and lowest during the winter and in the early morning hours. Moreover, bike usage increases as the temperature increases, and decreases as the weather worsens. Interestingly, the coefficient associated with workingday is statistically significant under the Poisson regression model, but not under the linear regression model.

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>z-statistic</td><td>p-value</td></tr><tr><td>Intercept</td><td>4.12</td><td>0.01</td><td>683.96</td><td>0.00</td></tr><tr><td>workingday</td><td>0.01</td><td>0.00</td><td>7.5</td><td>0.00</td></tr><tr><td>temp</td><td>0.79</td><td>0.01</td><td>68.43</td><td>0.00</td></tr><tr><td>weathersit[cloudy/misty]</td><td>-0.08</td><td>0.00</td><td>-34.53</td><td>0.00</td></tr><tr><td>weathersit[light rain/snow]</td><td>-0.58</td><td>0.00</td><td>-141.91</td><td>0.00</td></tr><tr><td>weathersit[heavy rain/snow]</td><td>-0.93</td><td>0.17</td><td>-5.55</td><td>0.00</td></tr></table>

TABLE 4.11. Results for a Poisson regression model fit to predict bikers in the Bikeshare data. The predictors mth and hr are omitted from this table due to space constraints, and can be seen in Figure 4.15. For the qualitative variable weathersit, the baseline corresponds to clear skies.

![](images/413478039e49ef4f4067b9a00610ebeb046bc5e8b8070daae5dfb7c562b6062b.jpg)

<details>
<summary>line</summary>

| Month | Coefficient |
|-------|-------------|
| J     | -0.8        |
| F     | -0.5        |
| M     | -0.3        |
| A     | 0.0         |
| M     | 0.2         |
| J     | 0.15        |
| J     | 0.1         |
| A     | 0.15        |
| S     | 0.2         |
| O     | 0.25        |
| N     | 0.15        |
| D     | 0.0         |
</details>

![](images/9cdde73861c4da12a67a8b15545c90c260565fa49764a2da6f510fc24b2a9ded.jpg)

<details>
<summary>line</summary>

| Hour | Coefficient |
| ---- | ----------- |
| 1    | -0.8        |
| 2    | -1.2        |
| 3    | -1.6        |
| 4    | -2.2        |
| 5    | -3.0        |
| 6    | -1.8        |
| 7    | -0.5        |
| 8    | 0.5         |
| 9    | 1.0         |
| 10   | 0.5         |
| 11   | 0.3         |
| 12   | 0.5         |
| 13   | 0.6         |
| 14   | 0.6         |
| 15   | 0.6         |
| 16   | 0.7         |
| 17   | 0.8         |
| 18   | 1.0         |
| 19   | 1.2         |
| 20   | 1.0         |
| 21   | 0.7         |
| 22   | 0.5         |
| 23   | 0.2         |
| 24   | -0.2        |
</details>

FIGURE 4.15. A Poisson regression model was fit to predict bikers in the Bikeshare data set. Left: The coefficients associated with the month of the year. Bike usage is highest in the spring and fall, and lowest in the winter. Right: The coefficients associated with the hour of the day. Bike usage is highest during peak commute times, and lowest overnight.

Some important distinctions between the Poisson regression model and the linear regression model are as follows:

\- Interpretation: To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in $X_{j}$ by one unit is associated with a change in $\mathrm{E}(Y) = \lambda$ by a factor of $\exp (\beta_j)$ . For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of $\exp (-0.08) = 0.923$ , i.e. on average, only $92.3\%$ as many people will use bikes when it is cloudy relative to when it is clear. If the weather worsens further and it begins to rain, then the mean bike usage will further change by a factor of $\exp (-0.5) = 0.607$ , i.e. on average only $60.7\%$ as many people will use bikes when it is rainy relative to when it is cloudy.

\- Mean-variance relationship: As mentioned earlier, under the Poisson model, $\lambda = \mathrm{E}(Y) = \mathrm{Var}(Y)$ . Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. By contrast, under a linear regression model, the variance of bike usage always takes on a constant value. Recall from Figure 4.14 that in the Bikeshare data, when biking conditions are favorable, both the mean and the variance in bike usage are much higher than when conditions are unfavorable. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the Bikeshare data in a way that the linear regression model is not. $^{5}$

\- nonnegative fitted values: There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values; see (4.35). By contrast, when we fit a linear regression model to the Bikeshare data set, almost 10% of the predictions were negative.

overdispersion

# 4.6.3 Generalized Linear Models in Greater Generality

We have now discussed three types of regression models: linear, logistic and Poisson. These approaches share some common characteristics:

![](images/9fc9739855c1fc68d5cece9248615aba5193707ae920dec86e0b9e817550a90c.jpg)

1. Each approach uses predictors $X_{1},\ldots,X_{p}$ to predict a response Y. We assume that, conditional on $X_{1},\ldots,X_{p}$ , Y belongs to a certain family of distributions. For linear regression, we typically assume that Y follows a Gaussian or normal distribution. For logistic regression, we assume that Y follows a Bernoulli distribution. Finally, for Poisson regression, we assume that Y follows a Poisson distribution.

2. Each approach models the mean of $Y$ as a function of the predictors. In linear regression, the mean of $Y$ takes the form

$$
\mathrm{E} (Y | X _ {1}, \dots , X _ {p}) = \beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}, \tag {4.39}
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form

$$
\begin{array}{l} \operatorname{E} (Y | X _ {1}, \ldots , X _ {p}) = \operatorname * {P r} (Y = 1 | X _ {1}, \ldots , X _ {p}) \\ = \frac {e ^ {\beta_ {0} + \beta_ {1} X _ {1} + \cdots + \beta_ {p} X _ {p}}}{1 + e ^ {\beta_ {0} + \beta_ {1} X _ {1} + \cdots + \beta_ {p} X _ {p}}}, \tag {4.40} \\ \end{array}
$$

while for Poisson regression it takes the form

$$
\mathrm{E} (Y | X _ {1}, \dots , X _ {p}) = \lambda (X _ {1}, \dots , X _ {p}) = e ^ {\beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}}. \tag {4.41}
$$

Equations (4.39)-(4.41) can be expressed using a link function, $\eta$ , which

link function

applies a transformation to $\mathrm{E}(Y|X_{1},\ldots,X_{p})$ so that the transformed mean is a linear function of the predictors. That is,

$$
\eta (\mathrm{E} (Y | X _ {1}, \dots , X _ {p})) = \beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}. \tag {4.42}
$$

The link functions for linear, logistic and Poisson regression are $\eta(\mu) = \mu$ , $\eta(\mu) = \log(\mu/(1 - \mu))$ , and $\eta(\mu) = \log(\mu)$ , respectively.

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the exponential family. Other well-known members of this family are the exponential distribution, the Gamma distribution, and the negative binomial distribution. In general, we can perform a regression by modeling the response Y as coming from a particular member of the exponential family, and then transforming the mean of the response so that the transformed mean is a linear function of the predictors via $(4.42)$ . Any regression approach that follows this very general recipe is known as a generalized linear model (GLM). Thus, linear regression, logistic regression, and Poisson regression are three examples of GLMs. Other examples not covered here include Gamma regression and negative binomial regression.

exponential
family
exponential
Gamma
negative
binomial

generalized
linear model

# 4.7 Lab: Logistic Regression, LDA, QDA, and KNN

# 4.7.1 The Stock Market Data

In this lab we will examine the Smarket data, which is part of the ISLP library. This data set consists of percentage returns for the S&P 500 stock index over 1,250 days, from the beginning of 2001 until the end of 2005. For each date, we have recorded the percentage returns for each of the five previous trading days, Lag1 through Lag5. We have also recorded Volume (the number of shares traded on the previous day, in billions), Today (the percentage return on the date in question) and Direction (whether the market was Up or Down on this date).

We start by importing our libraries at this top level; these are all imports we have seen in previous labs.

In [1]:

```python
import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots
import statsmodels.api as sm
from ISLP import load_data
from ISLP.models import (ModelSpec as MS, summarize) 
```

We also collect together the new imports needed for this lab.

In [2]:

```python
from ISLP import confusion_table
from ISLP.models import contrast
from sklearn.discriminant_analysis import \
(LinearDiscriminantAnalysis as LDA,
QuadraticDiscriminantAnalysis as QDA)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler 
```

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
```

Now we are ready to load the Smarket data.

```python
In [3]: Smarket = load_data('Smarket')
Smarket 
```

This gives a truncated listing of the data, which we do not show here. We can see what the variable names are.

```txt
In [4]: Smarket.columns 
```

```javascript
Out[4]: Index(['Year', 'Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5', 'Volume', 'Today', 'Direction'], dtype='object') 
```

We compute the correlation matrix using the corr() method for data frames, which produces a matrix that contains all of the pairwise correlations among the variables. (We suppress the output here.) The pandas library does not report a correlation for the Direction variable because it is qualitative.

```txt
In [5]: Smarket.corr() 
```

As one would expect, the correlations between the lagged return variables and today's return are close to zero. The only substantial correlation is between Year and Volume. By plotting the data we see that Volume is increasing over time. In other words, the average number of shares traded daily increased from 2001 to 2005.

```javascript
In [6]: Smarket.plot(y='Volume'); 
```

# 4.7.2 Logistic Regression

Next, we will fit a logistic regression model in order to predict Direction using Lag1 through Lag5 and Volume. The sm.GLM() function fits generalized linear models, a class of models that includes logistic regression. Alternatively, the function sm.Logit() fits a logistic regression model directly. The syntax of sm.GLM() is similar to that of sm.OLS(), except that we must pass in the argument family=sm.families.Binomial() in order to tell statsmodels to run a logistic regression rather than some other type of generalized linear model.

```python
In [7]: allvars = Smarket.columns.drop(['Today', 'Direction', 'Year'])
design = MS(allvars)
X = design.fit_transform(Smarket)
y = Smarket.Direction == 'Up'
glm = sm.GLM(y,
    X,
    family=sm.families.Binomial())
results = glm.fit()
summarize(results) 
```

<table><tr><td>Out[7]:</td><td>coef</td><td>std err</td><td>z</td><td>P&gt;|z|</td></tr><tr><td>intercept</td><td>-0.1260</td><td>0.241</td><td>-0.523</td><td>0.601</td></tr><tr><td>Lag1</td><td>-0.0731</td><td>0.050</td><td>-1.457</td><td>0.145</td></tr><tr><td>Lag2</td><td>-0.0423</td><td>0.050</td><td>-0.845</td><td>0.398</td></tr><tr><td>Lag3</td><td>0.0111</td><td>0.050</td><td>0.222</td><td>0.824</td></tr><tr><td>Lag4</td><td>0.0094</td><td>0.050</td><td>0.187</td><td>0.851</td></tr><tr><td>Lag5</td><td>0.0103</td><td>0.050</td><td>0.208</td><td>0.835</td></tr><tr><td>Volume</td><td>0.1354</td><td>0.158</td><td>0.855</td><td>0.392</td></tr></table>

The smallest p-value here is associated with Lag1. The negative coefficient for this predictor suggests that if the market had a positive return yesterday, then it is less likely to go up today. However, at a value of 0.15, the p-value is still relatively large, and so there is no clear evidence of a real association between Lag1 and Direction.

We use the params attribute of results in order to access just the coefficients for this fitted model.

In [8]: results.params

<table><tr><td>Out [8]: intercept</td><td>-0.126000</td></tr><tr><td>Lag1</td><td>-0.073074</td></tr><tr><td>Lag2</td><td>-0.042301</td></tr><tr><td>Lag3</td><td>0.011085</td></tr><tr><td>Lag4</td><td>0.009359</td></tr><tr><td>Lag5</td><td>0.010313</td></tr><tr><td>Volume</td><td>0.135441</td></tr><tr><td colspan="2">dtype: float64</td></tr></table>

Likewise we can use the pvalues attribute to access the p-values for the coefficients (not shown).

In [9]: results.pvalues

The predict() method of results can be used to predict the probability that the market will go up, given values of the predictors. This method returns predictions on the probability scale. If no data set is supplied to the predict() function, then the probabilities are computed for the training data that was used to fit the logistic regression model. As with linear regression, one can pass an optional exog argument consistent with a design matrix if desired. Here we have printed only the first ten probabilities.

In [10]: probs = results.predict()
probs[:10]

Out[10]: array([0.5070841, 0.4814679, 0.4811388, 0.5152223, 0.5107812, 0.5069565, 0.4926509, 0.5092292, 0.5176135, 0.4888378])

In order to make a prediction as to whether the market will go up or down on a particular day, we must convert these predicted probabilities into class labels, Up or Down. The following two commands create a vector of class predictions based on whether the predicted probability of a market increase is greater than or less than 0.5.

In [11]: labels = np.array(['Down'] \* 1250)
labels[probs > 0.5] = "Up"

The confusion\_table() function from the ISLP package summarizes these predictions, showing how many observations were correctly or incorrectly classified. Our function, which is adapted from a similar function in the module sklearn.metrics, transposes the resulting matrix and includes row and column labels. The confusion\_table() function takes as first argument the predicted labels, and second argument the true labels.

confusion\_table()

In [12]: confusion\_table(labels, Smarket.Direction)   
```txt
Out[12]: Truth Down Up
Predicted
Down 145 141
Up 457 507 
```

The diagonal elements of the confusion matrix indicate correct predictions, while the off-diagonals represent incorrect predictions. Hence our model correctly predicted that the market would go up on 507 days and that it would go down on 145 days, for a total of $507 + 145 = 652$ correct predictions. The np.mean() function can be used to compute the fraction of days for which the prediction was correct. In this case, logistic regression correctly predicted the movement of the market $52.2\%$ of the time.

In [13]: (507+145)/1250, np.mean(labels == Smarket.Direction)

Out[13]: (0.5216, 0.5216)

At first glance, it appears that the logistic regression model is working a little better than random guessing. However, this result is misleading because we trained and tested the model on the same set of 1,250 observations. In other words, $100 - 52.2 = 47.8\%$ is the training error rate. As we have seen previously, the training error rate is often overly optimistic — it tends to underestimate the test error rate. In order to better assess the accuracy of the logistic regression model in this setting, we can fit the model using part of the data, and then examine how well it predicts the held out data. This will yield a more realistic error rate, in the sense that in practice we will be interested in our model's performance not on the data that we used to fit the model, but rather on days in the future for which the market's movements are unknown.

To implement this strategy, we first create a Boolean vector corresponding to the observations from 2001 through 2004. We then use this vector to create a held out data set of observations from 2005.

```txt
In [14]: train = (Smarket.Year < 2005)
Smarket_train = Smarket.loc[train]
Smarket_test = Smarket.loc[~train]
Smarket_test.shape 
```  
Out [14]: (252, 9)

The object train is a vector of 1,250 elements, corresponding to the observations in our data set. The elements of the vector that correspond to observations that occurred before 2005 are set to True, whereas those that correspond to observations in 2005 are set to False. Hence train is a boolean array, since its elements are True and False. Boolean arrays can be used to obtain a subset of the rows or columns of a data frame using the loc method. For instance, the command Smarket.loc[train] would pick out a submatrix of the stock market data set, corresponding only to the dates before 2005, since those are the ones for which the elements of train are True. The \~ symbol can be used to negate all of the elements of a Boolean vector. That is, \~train is a vector similar to train, except that the elements that are True in train get swapped to False in \~train, and vice versa. Therefore, Smarket.loc[\~train] yields a subset of the rows of the data frame of the stock market data containing only the observations for which train is False. The output above indicates that there are 252 such observations.

We now fit a logistic regression model using only the subset of the observations that correspond to dates before 2005. We then obtain predicted probabilities of the stock market going up for each of the days in our test set — that is, for the days in 2005.

```python
In [15]: X_train, X_test = X.loc[train], X.loc[~train]
y_train, y_test = y.loc[train], y.loc[~train]
glm_train = sm.GLM(y_train,
    X_train,
    family=sm.families.Binomial())
results = glm_train.fit()
probs = results.predict(exog=X_test) 
```

Notice that we have trained and tested our model on two completely separate data sets: training was performed using only the dates before 2005, and testing was performed using only the dates in 2005.

Finally, we compare the predictions for 2005 to the actual movements of the market over that time period. We will first store the test and training labels (recall y\_test is binary).

```txt
In [16]: D = Smarket.Direction
L_train, L_test = D.loc[train], D.loc[~train] 
```

Now we threshold the fitted probability at 50% to form our predicted labels.

```python
In [17]: labels = np.array(['Down'] * 252)
labels[probs > 0.5] = 'Up'
confusion_table(labels, L_test) 
```

```txt
Out[17]: Truth Down Up
Predicted
Down 77 97
Up 34 44 
```

The test accuracy is about 48% while the error rate is about 52%

```txt
In [18]: np.mean(labels == L_test), np.mean(labels != L_test) 
```

```txt
Out [18]: (0.4802, 0.5198) 
```

The != notation means not equal to, and so the last command computes the test set error rate. The results are rather disappointing: the test error rate is 52%, which is worse than random guessing! Of course this result is not all that surprising, given that one would not generally expect to be able to use previous days' returns to predict future market performance. (After all, if it were possible to do so, then the authors of this book would be out striking it rich rather than writing a statistics textbook.)

We recall that the logistic regression model had very underwhelming p-values associated with all of the predictors, and that the smallest p-value, though not very small, corresponded to Lag1. Perhaps by removing the variables that appear not to be helpful in predicting Direction, we can obtain a more effective model. After all, using predictors that have no relationship with the response tends to cause a deterioration in the test error rate (since such predictors cause an increase in variance without a corresponding decrease in bias), and so removing such predictors may in turn yield an improvement. Below we refit the logistic regression using just Lag1 and Lag2, which seemed to have the highest predictive power in the original logistic regression model.

```python
In [19]: model = MS(['Lag1', 'Lag2']).fit(Smarket)
X = model.transform(Smarket)
X_train, X_test = X.loc[train], X.loc[~train]
glm_train = sm.GLM(y_train,
    X_train,
    family=sm.families.Binomial())
results = glm_train.fit()
probs = results.predict(exog=X_test)
labels = np.array(['Down']*252)
labels[probs>0.5] = 'Up'
confusion_table(labels, L_test) 
```

```txt
Out[19]: Truth Down Up
Predicted
Down 35 35
Up 76 106 
```

Let's evaluate the overall accuracy as well as the accuracy within the days when logistic regression predicts an increase.

```javascript
In [20]: (35+106)/252,106/(106+76) 
```

```txt
Out [20]: (0.5595, 0.5824) 
```

Now the results appear to be a little better: 56% of the daily movements have been correctly predicted. It is worth noting that in this case, a much simpler strategy of predicting that the market will increase every day will also be correct 56% of the time! Hence, in terms of overall error rate, the logistic regression method is no better than the naive approach. However, the confusion matrix shows that on days when logistic regression predicts an increase in the market, it has a 58% accuracy rate. This suggests a possible trading strategy of buying on days when the model predicts an increasing market, and avoiding trades on days when a decrease is predicted. Of course one would need to investigate more carefully whether this small improvement was real or just due to random chance.

Suppose that we want to predict the returns associated with particular values of Lag1 and Lag2. In particular, we want to predict Direction on a day when Lag1 and Lag2 equal 1.2 and 1.1, respectively, and on a day when they equal 1.5 and -0.8. We do this using the predict() function.

```javascript
In [21]: newdata = pd.DataFrame({'Lag1': [1.2, 1.5], 'Lag2': [1.1, -0.8]}); 
```

```txt
newX = model.transform(newdata)
results.predict(newX) 
```

```yaml
Out[21]: 0 0.4791
1 0.4961
dtype: float64 
```

# 4.7.3 Linear Discriminant Analysis

We begin by performing LDA on the Smarket data, using the function LinearDiscriminantAnalysis(), which we have abbreviated LDA(). We fit the model using only the observations before 2005.

```txt
Linear
Discriminant
Analysis() 
```

```txt
In [22]: lda = LDA(store_covariance=True) 
```

Since the LDA estimator automatically adds an intercept, we should remove the column corresponding to the intercept in both X\_train and X\_test. We can also directly use the labels rather than the Boolean vectors y\_train.

```python
In [23]: X_train, X_test = [M.drop(columns=['intercept'])
    for M in [X_train, X_test]]
lda.fit(X_train, L_train) 
```

```txt
Out[23]: LinearDiscriminantAnalysis(store_covariance=True) 
```

Here we have used the list comprehensions introduced in Section 3.6.4. Looking at our first line above, we see that the right-hand side is a list of length two. This is because the code for M in [X\_train, X\_test] iterates over a list of length two. While here we loop over a list, the list comprehension method works when looping over any iterable object. We then apply the drop() method to each element in the iteration, collecting the result in a list. The left-hand side tells Python to unpack this list of length two, assigning its elements to the variables X\_train and X\_test. Of course, this overwrites the previous values of X\_train and X\_test.

```txt
.drop() 
```

Having fit the model, we can extract the means in the two classes with the means\_ attribute. These are the average of each predictor within each class, and are used by LDA as estimates of $\mu_{k}$ . These suggest that there is a tendency for the previous 2 days' returns to be negative on days when the market increases, and a tendency for the previous days' returns to be positive on days when the market declines.

```txt
In [24]: lda.means_ 
```

```clojure
Out [24]: array([[0.04, 0.03], [-0.04, -0.03]])
```

The estimated prior probabilities are stored in the priors\_ attribute. The package sklearn typically uses this trailing \_ to denote a quantity estimated when using the fit() method. We can be sure of which entry corresponds to which label by looking at the classes\_ attribute.

```txt
In [25]: lda.classes_ 
```

```txt
Out[25]: array(['Down', 'Up'], dtype='<U4') 
```

The LDA output indicates that $\hat{\pi}_{Down} = 0.492$ and $\hat{\pi}_{Up} = 0.508$ .

In [26]: lda.priors\_

Out[26]: array([0.492, 0.508])

The linear discriminant vectors can be found in the scalings\_ attribute:

In [27]: lda.scalings\_

Out[27]: array([[-0.642], [-0.513]])

These values provide the linear combination of Lag1 and Lag2 that are used to form the LDA decision rule. In other words, these are the multipliers of the elements of X = x in $(4.24)$ . If $-0.64 \times Lag1 - 0.51 \times Lag2$ is large, then the LDA classifier will predict a market increase, and if it is small, then the LDA classifier will predict a market decline.

In [28]: lda\_pred = lda.predict(X\_test)

As we observed in our comparison of classification methods (Section 4.5), the LDA and logistic regression predictions are almost identical.

In [29]: confusion\_table(lda\_pred, L\_test)

Out[29]: Truth Down Up
Predicted
Down 35 35
Up 76 106

We can also estimate the probability of each class for each point in a training set. Applying a 50% threshold to the posterior probabilities of being in class one allows us to recreate the predictions contained in lda\_pred.

In [30]: lda\_prob = lda.predict\_proba(X\_test)
np.all(
    np.where(lda\_prob[:,1] >= 0.5, 'Up', 'Down') == lda\_pred)

Out[30]: True

Above, we used the np.where() function that creates an array with value 'Up' for indices where the second column of lda\_prob (the estimated posterior probability of 'Up') is greater than 0.5. For problems with more than two classes the labels are chosen as the class whose posterior probability is highest:

In [31]: np.all(
    [lda.classes\_[i] for i in np.argmax(lda\_prob, 1)] == 
    lda\_pred
)

Out [31]: True

If we wanted to use a posterior probability threshold other than 50% in order to make predictions, then we could easily do so. For instance, suppose that we wish to predict a market decrease only if we are very certain that the

np.where()

market will indeed decrease on that day — say, if the posterior probability is at least 90%. We know that the first column of lda\_prob corresponds to the label Down after having checked the classes\_ attribute, hence we use the column index 0 rather than 1 as we did above.

```txt
In [32]: np.sum(lda_prob[:,0] > 0.9) 
```

```txt
Out [32]: 0 
```

No days in 2005 meet that threshold! In fact, the greatest posterior probability of decrease in all of 2005 was 52.02%.

The LDA classifier above is the first classifier from the sklearn library. We will use several other objects from this library. The objects follow a common structure that simplifies tasks such as cross-validation, which we will see in Chapter 5. Specifically, the methods first create a generic classifier without referring to any data. This classifier is then fit to data with the fit() method and predictions are always produced with the predict() method. This pattern of first instantiating the classifier, followed by fitting it, and then producing predictions is an explicit design choice of sklearn. This uniformity makes it possible to cleanly copy the classifier so that it can be fit on different data; e.g. different training sets arising in cross-validation. This standard pattern also allows for a predictable formation of workflows.

# 4.7.4 Quadratic Discriminant Analysis

We will now fit a QDA model to the Smarket data. QDA is implemented via QuadraticDiscriminantAnalysis() in the sklearn package, which we abbreviate to QDA(). The syntax is very similar to LDA().

```txt
Quadratic
Discriminant
Analysis() 
```

```python
In [33]: qda = QDA(store_covariance=True)
qda.fit(X_train, L_train) 
```

```python
Out[33]: QuadraticDiscriminantAnalysis(store_covariance=True) 
```

The QDA() function will again compute means\_ and priors\_.

```txt
In [34]: qda.means_, qda.priors_ 
```

```javascript
Out[34]: (array([[0.04279022, 0.03389409], [-0.03954635, -0.03132544]]), array([0.49198397, 0.50801603]))
```

The QDA() classifier will estimate one covariance per class. Here is the estimated covariance in the first class:

```txt
In [35]: qda.covariance_[0] 
```

```txt
Out[35]: array([[1.50662277, -0.03924806], [-0.03924806, 1.53559498]])
```

The output contains the group means. But it does not contain the coefficients of the linear discriminants, because the QDA classifier involves a quadratic, rather than a linear, function of the predictors. The predict() function works in exactly the same fashion as for LDA.

```python
In [36]: qda_pred = qda.predict(X_test)
confusion_table(qda_pred, L_test) 
```

```txt
Out[36]: Truth Down Up
Predicted
Down 30 20
Up 81 121 
```

Interestingly, the QDA predictions are accurate almost 60% of the time, even though the 2005 data was not used to fit the model.

```txt
In [37]: np.mean(qda_pred == L_test) 
```

```txt
Out [37]: 0.599 
```

This level of accuracy is quite impressive for stock market data, which is known to be quite hard to model accurately. This suggests that the quadratic form assumed by QDA may capture the true relationship more accurately than the linear forms assumed by LDA and logistic regression. However, we recommend evaluating this method's performance on a larger test set before betting that this approach will consistently beat the market!

# 4.7.5 Naive Bayes

Next, we fit a naive Bayes model to the Smarket data. The syntax is similar to that of LDA() and QDA(). By default, this implementation GaussianNB() of the naive Bayes classifier models each quantitative feature using a Gaussian distribution. However, a kernel density method can also be used to estimate the distributions.

GaussianNB()

```python
In [38]: NB = GaussianNB()
NB.fit(X_train, L_train) 
```

```javascript
Out[38]: GaussianNB()
```

The classes are stored as classes\_.

```txt
In [39]: NB.classes_ 
```

```txt
Out[39]: array(['Down', 'Up'], dtype='<U4') 
```

The class prior probabilities are stored in the class\_prior\_attribute.

```txt
In [40]: NB.class_prior_ 
```

```txt
Out[40]: array([0.49, 0.51])
```

The parameters of the features can be found in the theta\_ and var attributes. The number of rows is equal to the number of classes, while the number of columns is equal to the number of features. We see below that the mean for feature Lag1 in the Down class is 0.043.

```txt
In [41]: NB.theta_ 
```

```txt
Out[41]: array([[0.043, 0.034], [-0.040, -0.031]])
```

Its variance is 1.503.

```txt
In [42]: NB.var_ 
```

```txt
Out[42]: array([[1.503, 1.532], [1.514, 1.487]]) 
```

How do we know the names of these attributes? We use NB? (or ?NB).

We can easily verify the mean computation:

```python
In [43]: X_train[L_train == 'Down'].mean() 
```

```yaml
Out[43]: Lag1 0.042790
Lag2 0.033894
dtype: float64 
```

Similarly for the variance:

```python
In [44]: X_train[L_train == 'Down'].var(ddof=0) 
```

```txt
Out [44]: Lag1 1.503554
Lag2 1.532467
dtype: float64 
```

The GaussianNB() function calculates variances using the 1/n formula. $^{6}$ Since NB() is a classifier in the sklearn library, making predictions uses the same syntax as for LDA() and QDA() above.

```python
In [45]: nb_labels = NB.predict(X_test)
confusion_table(nb_labels, L_test) 
```

```txt
Out[45]: Truth Down Up
Predicted
Down 29 20
Up 82 121 
```

Naive Bayes performs well on these data, with accurate predictions over 59% of the time. This is slightly worse than QDA, but much better than LDA.

As for LDA, the predict\_proba() method estimates the probability that each observation belongs to a particular class.

```python
In [46]: NB.predict_proba(X_test)[:5] 
```

```txt
Out[46]: array([[0.4873, 0.5127], [0.4762, 0.5238], [0.4653, 0.5347], [0.4748, 0.5252], [0.4902, 0.5098]]) 
```

# 4.7.6 K-Nearest Neighbors

We will now perform KNN using the KNeighborsClassifier() function. This

KNeighbors
Classifier()

function works similarly to the other model-fitting functions that we have encountered thus far.

As is the case for LDA and QDA, we fit the classifier using the fit method. New predictions are formed using the predict method of the object returned by fit().

```python
In [47]: knn1 = KNeighborsClassifier(n_neighbors=1)
knn1.fit(X_train, L_train)
knn1_pred = knn1.predict(X_test)
confusion_table(knn1_pred, L_test) 
```

```txt
Out[47]: Truth Down Up
Predicted
Down 43 58
Up 68 83 
```

The results using K = 1 are not very good, since only 50% of the observations are correctly predicted. Of course, it may be that K = 1 results in an overly-flexible fit to the data.

```javascript
In [48]: (83+43)/252, np.mean(knn1_pred == L_test) 
```

```txt
Out [48]: (0.5, 0.5) 
```

We repeat the analysis below using $K = 3$ .

```txt
In [49]: knn3 = KNeighborsClassifier(n_neighbors=3)
knn3_pred = knn3.fit(X_train, L_train).predict(X_test)
np.mean(knn3_pred == L_test) 
```

```txt
Out [49]: 0.532 
```

The results have improved slightly. But increasing K further provides no further improvements. It appears that for these data, and this train/test split, QDA gives the best results of the methods that we have examined so far.

KNN does not perform well on the Smarket data, but it often does provide impressive results. As an example we will apply the KNN approach to the Caravan data set, which is part of the ISLP library. This data set includes 85 predictors that measure demographic characteristics for 5,822 individuals. The response variable is Purchase, which indicates whether or not a given individual purchases a caravan insurance policy. In this data set, only 6% of people purchased caravan insurance.

```python
In [50]: Caravan = load_data('Caravan')
Purchase = Caravan.Purchase
Purchase.value_counts() 
```

```txt
Out [50]: No 5474
Yes 348 
```

Name: Purchase, dtype: int64

The method value\_counts() takes a pd.Series or pd.DataFrame and returns a pd.Series with the corresponding counts for each unique element. In this case Purchase has only Yes and No values and returns how many values of each there are.

In [51]: 348 / 5822

Out [51]: 0.0598

Our features will include all columns except Purchase.

In [52]: feature\_df = Caravan.drop(columns=['Purchase'])

Because the KNN classifier predicts the class of a given test observation by identifying the observations that are nearest to it, the scale of the variables matters. Any variables that are on a large scale will have a much larger effect on the distance between the observations, and hence on the KNN classifier, than variables that are on a small scale. For instance, imagine a data set that contains two variables, salary and age (measured in dollars and years, respectively). As far as KNN is concerned, a difference of 1,000 USD in salary is enormous compared to a difference of 50 years in age. Consequently, salary will drive the KNN classification results, and age will have almost no effect. This is contrary to our intuition that a salary difference of 1,000 USD is quite small compared to an age difference of 50 years. Furthermore, the importance of scale to the KNN classifier leads to another issue: if we measured salary in Japanese yen, or if we measured age in minutes, then we'd get quite different classification results from what we get if these two variables are measured in dollars and years.

A good way to handle this problem is to standardize the data so that all variables are given a mean of zero and a standard deviation of one. Then all variables will be on a comparable scale. This is accomplished using the StandardScaler() transformation.

standardize

In [53]: scaler = StandardScaler(with\_mean=True, with\_std=True, copy=True)

Standard
Scaler()

The argument with\_mean indicates whether or not we should subtract the mean, while with\_std indicates whether or not we should scale the columns to have standard deviation of 1 or not. Finally, the argument copy=True indicates that we will always copy data, rather than trying to do calculations in place where possible.

This transformation can be fit and then applied to arbitrary data. In the first line below, the parameters for the scaling are computed and stored in scaler, while the second line actually constructs the standardized set of features.

In [54]: scaler.fit(feature\_df)
X\_std = scaler.transform(feature\_df)

Now every column of feature\_std below has a standard deviation of one and a mean of zero.

In [55]: feature\_std = pd.DataFrame(
    X\_std,
    columns=feature\_df.columns);
feature\_std.std()

Out [55]: MOSTYPE 1.000086
MAANTHUI 1.000086

```txt
MGEMOMV 1.000086
MGEMLEEF 1.000086
MOSHOOFD 1.000086
...
AZEILPL 1.000086
APLEZIER 1.000086
AFIETS 1.000086
AINBOED 1.000086
ABYSTAND 1.000086
Length: 85, dtype: float64 
```

Notice that the standard deviations are not quite 1 here; this is again due to some procedures using the $1 / n$ convention for variances (in this case scaler()), while others use $1 / (n - 1)$ (the std() method). See the footnote on page 183. In this case it does not matter, as long as the variables are all on the same scale.

Using the function train\_test\_split() we now split the observations into a test set, containing 1000 observations, and a training set containing the remaining observations. The argument random\_state=0 ensures that we get the same split each time we rerun the code.

.std()

train\_test\_split()

In [56]:

```python
(X_train,
X_test,
y_train,
y_test) = train_test_split(feature_std,
    Purchase,
    test_size=1000,
    random_state=0) 
```

?train\_test\_split reveals that the non-keyword arguments can be lists, arrays, pandas dataframes etc that all have the same length (shape[0]) and hence are indexable. In this case they are the dataframe feature\_std and the response variable Purchase. We fit a KNN model on the training data using $K = 1$ , and evaluate its performance on the test data.

indexable

In [57]:

```python
knn1 = KNeighborsClassifier(n_neighbors=1)
knn1_pred = knn1.fit(X_train, y_train).predict(X_test)
np.mean(y_test != knn1_pred), np.mean(y_test != "No") 
```

Out[57]: (0.111, 0.067)

The KNN error rate on the 1,000 test observations is about 11%. At first glance, this may appear to be fairly good. However, since just over 6% of customers purchased insurance, we could get the error rate down to almost 6% by always predicting No regardless of the values of the predictors! This is known as the null rate.

null rate

Suppose that there is some non-trivial cost to trying to sell insurance to a given individual. For instance, perhaps a salesperson must visit each potential customer. If the company tries to sell insurance to a random selection of customers, then the success rate will be only 6%, which may be far too low given the costs involved. Instead, the company would like to try to sell insurance only to customers who are likely to buy it. So the overall error rate is not of interest. Instead, the fraction of individuals that are correctly predicted to buy insurance is of interest.

In [58]:

```python
confusion_table(knn1_pred, y_test)
```

```txt
Out[58]: Truth No Yes
Predicted
No 880 58
Yes 53 9 
```

It turns out that KNN with K = 1 does far better than random guessing among the customers that are predicted to buy insurance. Among 62 such customers, 9, or 14.5%, actually do purchase insurance. This is double the rate that one would obtain from random guessing.

In [59]: $9/(53+9)$

```txt
Out [59]: 0.145 
```

# Tuning Parameters

The number of neighbors in KNN is referred to as a tuning parameter, also referred to as a hyperparameter. We do not know a priori what value to use. It is therefore of interest to see how the classifier performs on test data as we vary these parameters. This can be achieved with a for loop, described in Section 2.3.8. Here we use a for loop to look at the accuracy of our classifier in the group predicted to purchase insurance as we vary the number of neighbors from 1 to 5:

tuning
parameter
hyper-
parameter

```python
In [60]: for K in range(1,6):
    knn = KNeighborsClassifier(n_neighbors=K)
    knn_pred = knn.fit(X_train, y_train).predict(X_test)
    C = confusion_table(knn_pred, y_test)
    templ = ('K={0:d}: # predicted to rent: {1:>2}, ' + ' # who did rent {2:d}, accuracy {3:.1%}')
    pred = C.loc['Yes'].sum()
    did_rent = C.loc['Yes', 'Yes']
    print(templ.format(
    K,
    pred,
    did_rent,
    did_rent / pred)) 
```

```txt
K=1: # predicted to rent: 62,# who did rent 9, accuracy 14.5%
K=2: # predicted to rent: 6,# who did rent 1, accuracy 16.7%
K=3: # predicted to rent: 20,# who did rent 3, accuracy 15.0%
K=4: # predicted to rent: 3,# who did rent 0, accuracy 0.0%
K=5: # predicted to rent: 7,# who did rent 1, accuracy 14.3% 
```

We see some variability — the numbers for K=4 are very different from the rest.

# Comparison to Logistic Regression

As a comparison, we can also fit a logistic regression model to the data. This can also be done with sklearn, though by default it fits something like the ridge regression version of logistic regression, which we introduce in Chapter 6. This can be modified by appropriately setting the argument c below. Its default value is 1 but by setting it to a very large number, the algorithm converges to the same solution as the usual (unregularized) logistic regression estimator discussed above.

Unlike the statsmodels package, sklearn focuses less on inference and more on classification. Hence, the summary methods seen in statsmodels and our simplified version seen with summarize are not generally available for the classifiers in sklearn.

```python
In [61]: logit = LogisticRegression(C=1e10, solver='liblinear')
logit.fit(X_train, y_train)
logit_pred = logit.predict_proba(X_test)
logit_labels = np.where(logit_pred[:,1] > 5, 'Yes', 'No')
confusion_table(logit_labels, y_test) 
```

```txt
Out[61]: Truth No Yes
Predicted
No 933 67
Yes 0 0 
```

We used the argument solver='liblinear' above to avoid a warning with the default solver which would indicate that the algorithm does not converge.

If we use 0.5 as the predicted probability cut-off for the classifier, then we have a problem: none of the test observations are predicted to purchase insurance. However, we are not required to use a cut-off of 0.5. If we instead predict a purchase any time the predicted probability of purchase exceeds 0.25, we get much better results: we predict that 29 people will purchase insurance, and we are correct for about 31% of these people. This is almost five times better than random guessing!

```python
In [62]: logit_labels = np.where(logit_pred[:,1]>0.25, 'Yes', 'No') confusion_table(logit_labels, y_test) 
```

```txt
Out[62]: Truth No Yes
Predicted
No 913 58
Yes 20 9 
```

```txt
In [63]: 9/(20+9) 
```

```txt
Out [63]: 0.310 
```

# 4.7.7 Linear and Poisson Regression on the Bikeshare Data

Here we fit linear and Poisson regression models to the Bikeshare data, as described in Section 4.6. The response bikers measures the number of bike rentals per hour in Washington, DC in the period 2010–2012.

```javascript
In [64]: Bike = load_data('Bikeshare') 
```

Let's have a peek at the dimensions and names of the variables in this dataframe.

```txt
In [65]: Bike.shape, Bike.columns 
```

```javascript
Out[65]: ((8645, 15), Index(['season', 'mth', 'day', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'bikers'], dtype='object')) 
```

# Linear Regression

We begin by fitting a linear regression model to the data.

```python
In [66]: X = MS(['mth', 'hr', 'workingday', 'temp', 'weathersit']).fit_transform(Bike)
Y = Bike['bikers']
M_lm = sm.OLS(Y, X).fit()
summarize(M_lm) 
```

```batch
Out [66]:
coef std err t P>|t|
intercept -68.6317 5.307 -12.932 0.000
mth [Feb] 6.8452 4.287 1.597 0.110
mth [March] 16.5514 4.301 3.848 0.000
mth [April] 41.4249 4.972 8.331 0.000
mth [May] 72.5571 5.641 12.862 0.000
mth [June] 67.8187 6.544 10.364 0.000
mth [July] 45.3245 7.081 6.401 0.000
mth [Aug] 53.2430 6.640 8.019 0.000
mth [Sept] 66.6783 5.925 11.254 0.000
mth [Oct] 75.8343 4.950 15.319 0.000
mth [Nov] 60.3100 4.610 13.083 0.000
mth [Dec] 46.4577 4.271 10.878 0.000
hr [1] -14.5793 5.699 -2.558 0.011
hr [2] -21.5791 5.733 -3.764 0.000
hr [3] -31.1408 5.778 -5.389 0.000
...... .... .... .... .... .... 
```

There are 24 levels in hr and 40 rows in all, so we have truncated the summary. In M\_1m, the first levels hr[0] and mnth[Jan] are treated as the baseline values, and so no coefficient estimates are provided for them: implicitly, their coefficient estimates are zero, and all other levels are measured relative to these baselines. For example, the Feb coefficient of 6.845 signifies that, holding all other variables constant, there are on average about 7 more riders in February than in January. Similarly there are about 16.5 more riders in March than in January.

The results seen in Section 4.6.1 used a slightly different coding of the variables hr and mth, as follows:

```python
In [67]: hr_encode = contrast('hr', 'sum')
    mth_encode = contrast('mth', 'sum') 
```

Refitting again:

```txt
In [68]: X2 = MS([mnth_encode, hr_encode, 'workingday', 'temp', 
```

```txt
'weathersit']).fit_transform(Bike)
M2_lm = sm.OLS(Y, X2).fit()
S2 = summarize(M2_lm)
S2 
```

<table><tr><td>Out [68]:</td><td>coef</td><td>std err</td><td>t</td><td>P&gt;|t|</td></tr><tr><td>intercept</td><td>73.5974</td><td>5.132</td><td>14.340</td><td>0.000</td></tr><tr><td>mnth [Jan]</td><td>-46.0871</td><td>4.085</td><td>-11.281</td><td>0.000</td></tr><tr><td>mnth [Feb]</td><td>-39.2419</td><td>3.539</td><td>-11.088</td><td>0.000</td></tr><tr><td>mnth [March]</td><td>-29.5357</td><td>3.155</td><td>-9.361</td><td>0.000</td></tr><tr><td>mnth [April]</td><td>-4.6622</td><td>2.741</td><td>-1.701</td><td>0.089</td></tr><tr><td>mnth [May]</td><td>26.4700</td><td>2.851</td><td>9.285</td><td>0.000</td></tr><tr><td>mnth [June]</td><td>21.7317</td><td>3.465</td><td>6.272</td><td>0.000</td></tr><tr><td>mnth [July]</td><td>-0.7626</td><td>3.908</td><td>-0.195</td><td>0.845</td></tr><tr><td>mnth [Aug]</td><td>7.1560</td><td>3.535</td><td>2.024</td><td>0.043</td></tr><tr><td>mnth [Sept]</td><td>20.5912</td><td>3.046</td><td>6.761</td><td>0.000</td></tr><tr><td>mnth [Oct]</td><td>29.7472</td><td>2.700</td><td>11.019</td><td>0.000</td></tr><tr><td>mnth [Nov]</td><td>14.2229</td><td>2.860</td><td>4.972</td><td>0.000</td></tr><tr><td>hr [0]</td><td>-96.1420</td><td>3.955</td><td>-24.307</td><td>0.000</td></tr><tr><td>hr [1]</td><td>-110.7213</td><td>3.966</td><td>-27.916</td><td>0.000</td></tr><tr><td>hr [2]</td><td>-117.7212</td><td>4.016</td><td>-29.310</td><td>0.000</td></tr><tr><td>......</td><td>......</td><td>......</td><td>......</td><td>......</td></tr></table>

What is the difference between the two codings? In M2\_lm, a coefficient estimate is reported for all but level 23 of hr and level Dec of mnth. Importantly, in M2\_lm, the (unreported) coefficient estimate for the last level of mnth is not zero: instead, it equals the negative of the sum of the coefficient estimates for all of the other levels. Similarly, in M2\_lm, the coefficient estimate for the last level of hr is the negative of the sum of the coefficient estimates for all of the other levels. This means that the coefficients of hr and mnth in M2\_lm will always sum to zero, and can be interpreted as the difference from the mean level. For example, the coefficient for January of -46.087 indicates that, holding all other variables constant, there are typically 46 fewer riders in January relative to the yearly average.

It is important to realize that the choice of coding really does not matter, provided that we interpret the model output correctly in light of the coding used. For example, we see that the predictions from the linear model are the same regardless of coding:

```txt
In [69]: np.sum((M_lm.fittedvalues - M2_lm.fittedvalues)**2) 
```

```javascript
Out [69]: 1.53e-20 
```

The sum of squared differences is zero. We can also see this using the np.allclose() function:

```python
In [70]: np.allclose(M_lm.fittedvalues, M2_lm.fittedvalues) 
```

np.allclose()

```txt
Out[70]: True 
```

To reproduce the left-hand side of Figure 4.13 we must first obtain the coefficient estimates associated with $\text{mnth}$ . The coefficients for January through November can be obtained directly from the M2\_lm object. The coefficient for December must be explicitly computed as the negative sum of all the other months. We first extract all the coefficients for month from the coefficients of M2\_lm.

```python
In [71]: coef_month = S2[S2.index.str.contains('mnth')]['coef']
coef_month 
```

```txt
Out[71]: mnth [Jan] -46.0871  
mnth [Feb] -39.2419  
mnth [March] -29.5357  
mnth [April] -4.6622  
mnth [May] 26.4700  
mnth [June] 21.7317  
mnth [July] -0.7626  
mnth [Aug] 7.1560  
mnth [Sept] 20.5912  
mnth [Oct] 29.7472  
mnth [Nov] 14.2229  
Name: coef, dtype: float64 
```

Next, we append Dec as the negative of the sum of all other months.

```python
In [72]: months = Bike['mth'].dtype.categories
coef_month = pd.concat([
    coef_month,
    pd.Series([-coef_month.sum()],
    index=['mth[Dec]']
])
coef_month 
```

```txt
Out[72]: mnth [Jan] -46.0871  
mnth [Feb] -39.2419  
mnth [March] -29.5357  
mnth [April] -4.6622  
mnth [May] 26.4700  
mnth [June] 21.7317  
mnth [July] -0.7626  
mnth [Aug] 7.1560  
mnth [Sept] 20.5912  
mnth [Oct] 29.7472  
mnth [Nov] 14.2229  
mnth [Dec] 0.3705  
Name: coef, dtype: float64 
```

Finally, to make the plot neater, we'll just use the first letter of each month, which is the 6th entry of each of the labels in the index.

```python
In [73]: fig_month, ax_month = subplots(figsize=(8,8))
x_month = np.arange(coef_month.shape[0])
ax_month.plot(x_month, coef_month, marker='o', ms=10)
ax_month.set_xticks(x_month)
ax_month.set_xticklabels([l[5] for l in coef_month.index], fontsize=20)
ax_month.set_xlabel('Month', fontsize=20)
ax_month.set_ylabel('Coefficient', fontsize=20); 
```

Reproducing the right-hand plot in Figure 4.13 follows a similar process.

```python
In [74]: coef_hr = S2[S2.index.str.contains('hr')]['coef']
coef_hr = coef_hr.reindex(['hr[{0}]'.format(h) for h in range(23)])
coef_hr = pd.concat([coef_hr, 
```