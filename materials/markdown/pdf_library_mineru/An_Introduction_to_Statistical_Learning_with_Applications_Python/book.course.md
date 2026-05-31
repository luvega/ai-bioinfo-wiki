---
type: course-source
title: An Introduction to Statistical Learning_ with Applications Python
source_mineru: book.mineru.md
generated: 2026-05-24 12:34:06
status: generated_draft
tags: [mineru, course-material, auto-extract]
---

# An Introduction to Statistical Learning_ with Applications Python · 课程化整理

## 使用说明

本文件由 `book.mineru.md` 自动整理生成，服务于 36 课时课程备课。它不是原书全文，也不替代人工核验；完整解析结果请回到 `book.mineru.md`。

## 一句话定位

Python 版统计学习教材，适合支撑第 8-13 周统计推断、回归、分类、高维数据、PCA 和聚类。

## 推荐进入课程的周次

| 周次 | 课程主题 |
|---:|---|
| 3 | AI 辅助编程与 Python 快速入门 |
| 5 | 数据读取与整形 |
| 6 | 缺失值、异常值处理与分组汇总 |
| 7 | 描述统计与分布可视化 |
| 8 | 统计推断基础 |
| 9 | 相关分析与线性回归 |
| 10 | 分类问题与逻辑回归 |
| 11 | 科研图表规范与 SCI 图表表达 |
| 12 | 高维数据与数学直觉 |
| 13 | PCA、聚类与热图 |
| 17 | 综合项目工作坊：AI 协作分析与结果核验 |

## 章节层级索引

- H1 L9: An Introduction to Statistical Learning
- H1 L59: Contents
- H1 L61: Preface vii
- H1 L63: 1 Introduction 1
- H1 L65: 2 Statistical Learning 15
- H1 L95: 3 Linear Regression 69
- H1 L139: 4 Classification 135
- H1 L199: 5 Resampling Methods 201
- H1 L219: 6 Linear Model Selection and Regularization 229
- H1 L253: 7 Moving Beyond Linearity 289
- H1 L287: 8 Tree-Based Methods 331
- H1 L314: 9 Support Vector Machines 367
- H1 L358: 10 Deep Learning 399
- H1 L416: 11 Survival Analysis and Censored Data 469
- H1 L451: 12 Unsupervised Learning 503
- H1 L480: 13 Multiple Testing 557
- H1 L517: 1
- H1 L519: Introduction
- H1 L523: An Overview of Statistical Learning
- H1 L527: Wage Data
- H1 L574: Stock Market Data
- H1 L672: Gene Expression Data
- H1 L809: A Brief History of Statistical Learning
- H1 L817: This Book
- H1 L838: Who Should Read This Book?
- H1 L844: Notation and Simple Matrix Algebra
- H1 L928: Organization of This Book
- H1 L948: Data Sets Used in Labs and Exercises
- H1 L952: Book Website
- H1 L960: Acknowledgements
- H1 L964: 2
- H1 L966: Statistical Learning
- H1 L970: 2.1 What Is Statistical Learning?
- H1 L1107: 2.1.1 Why Estimate f?
- H1 L1111: Prediction
- H1 L1204: Inference
- H1 L1232: 2.1.2 How Do We Estimate $f$ ?
- H1 L1242: Parametric Methods
- H1 L1366: Non-Parametric Methods
- H1 L1441: 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability
- H1 L1468: 2.1.4 Supervised Versus Unsupervised Learning
- H1 L1504: 2.1.5 Regression Versus Classification Problems
- H1 L1520: 2.2 Assessing Model Accuracy
- H1 L1526: 2.2.1 Measuring the Quality of Fit
- H1 L1631: 2.2.2 The Bias-Variance Trade-Off
- H1 L1743: 2.2.3 The Classification Setting
- H1 L1761: The Bayes Classifier
- H1 L1815: K-Nearest Neighbors
- H1 L1932: 2.3 Lab: Introduction to Python
- H1 L1934: 2.3.1 Getting Started
- H1 L1959: 2.3.2 Basic Commands
- H1 L2014: 2.3.3 Introduction to Numerical Python
- H1 L2427: 2.3.4 Graphics
- H1 L2590: 2.3.5 Sequences and Slice Notation
- H1 L2640: 2.3.6 Indexing Data
- H1 L2740: Boolean Indexing
- H1 L2807: 2.3.7 Loading Data
- H1 L2813: Reading in a Data Set
- H1 L2901: Basics of Selecting Rows and Columns
- H1 L3053: More on Selecting Rows and Columns
- H1 L3100: 2.3.8 For Loops
- H1 L3151: String Formatting
- H1 L3201: 2.3.9 Additional Graphical and Numerical Summaries
- H1 L3297: 2.4 Exercises
- H1 L3299: Conceptual
- H1 L3341: Applied
- H1 L3423: 3
- H1 L3425: Linear Regression
- H1 L3433: 1. Is there a relationship between advertising budget and sales?
- H1 L3462: 3.1 Simple Linear Regression
- H1 L3493: 3.1.1 Estimating the Coefficients
- H1 L3577: 3.1.2 Assessing the Accuracy of the Coefficient Estimates
- H1 L3724: 3.1.3 Assessing the Accuracy of the Model
- H1 L3736: Residual Standard Error
- H1 L3754: $R^2$ Statistic
- H1 L3791: 3.2 Multiple Linear Regression
- H1 L3811: 3.2.1 Estimating the Regression Coefficients
- H1 L4053: 3.2.2 Some Important Questions
- H1 L4129: Two: Deciding on Important Variables
- H1 L4163: Three: Model Fit
- H1 L4217: Four: Predictions
- H1 L4244: 3.3 Other Considerations in the Regression Model
- H1 L4246: 3.3.1 Qualitative Predictors
- H1 L4252: Predictors with Only Two Levels
- H1 L4575: Qualitative Predictors with More than Two Levels
- H1 L4611: 3.3.2 Extensions of the Linear Model
- H1 L4620: Removing the Additive Assumption
- H1 L4714: Non-linear Relationships
- H1 L4760: 3.3.3 Potential Problems
- H1 L4774: 1. Non-linearity of the Data
- H1 L4816: 2. Correlation of Error Terms
- H1 L4858: 3. Non-constant Variance of Error Terms
- H1 L4871: 4. Outliers
- H1 L4929: 5. High Leverage Points
- H1 L5049: 6. Collinearity
- H1 L5118: 3.4 The Marketing Plan
- H1 L5154: 3.5 Comparison of Linear Regression with $K$ -Nearest Neighbors
- H1 L5351: 3.6 Lab: Linear Regression
- H1 L5353: 3.6.1 Importing packages
- H1 L5364: New imports
- H1 L5397: Inspecting Objects and Namespaces
- H1 L5454: 3.6.2 Simple Linear Regression
- H1 L5515: Using Transformations: Fit and Transform
- H1 L5645: Defining Functions
- H1 L5732: 3.6.3 Multiple Linear Regression
- H1 L5807: 3.6.4 Multivariate Goodness of Fit
- H1 L5815: List Comprehension
- H1 L5860: 3.6.5 Interaction Terms
- H1 L5880: 3.6.6 Non-linear Transformations of the Predictors
- H1 L5936: 3.6.7 Qualitative Predictors
- H1 L5970: 3.7 Exercises
- H1 L5972: Conceptual
- H1 L6030: Applied
- H1 L6178: 4.1 An Overview of Classification
- H1 L6217: 4.2 Why Not Linear Regression?
- H1 L6292: 4.3 Logistic Regression
- H1 L6336: 4.3.1 The Logistic Model
- H1 L6378: 4.3.2 Estimating the Regression Coefficients
- H1 L6396: 4.3.3 Making Predictions
- H1 L6424: 4.3.4 Multiple Logistic Regression
- H1 L6491: 4.3.5 Multinomial Logistic Regression
- H1 L6545: 4.4 Generative Models for Classification
- H1 L6575: 4.4.1 Linear Discriminant Analysis for $p = 1$
- H1 L6681: 4.4.2 Linear Discriminant Analysis for $p > 1$
- H1 L6888: 4.4.3 Quadratic Discriminant Analysis
- H1 L6949: 4.4.4 Naive Bayes
- H1 L7061: 4.5 A Comparison of Classification Methods
- H1 L7063: 4.5.1 An Analytical Comparison
- H1 L7121: 4.5.2 An Empirical Comparison
- H1 L7241: 4.6 Generalized Linear Models
- H1 L7249: 4.6.1 Linear Regression on the Bikeshare Data
- H1 L7395: 4.6.2 Poisson Regression on the Bikeshare Data
- H1 L7510: 4.6.3 Generalized Linear Models in Greater Generality
- H1 L7560: 4.7 Lab: Logistic Regression, LDA, QDA, and KNN
- H1 L7562: 4.7.1 The Stock Market Data
- H1 L7628: 4.7.2 Logistic Regression
- H1 L7802: 4.7.3 Linear Discriminant Analysis
- H1 L7914: 4.7.4 Quadratic Discriminant Analysis
- H1 L7979: 4.7.5 Naive Bayes
- H1 L8086: 4.7.6 K-Nearest Neighbors
- H1 L8262: Tuning Parameters
- H1 L8296: Comparison to Logistic Regression
- H1 L8340: 4.7.7 Linear and Poisson Regression on the Bikeshare Data
- H1 L8358: Linear Regression
- H1 L8527: Poisson Regression
- H1 L8584: 4.8 Exercises
- H1 L8586: Conceptual
- H1 L8659: Applied
- H1 L8737: 5.1 Cross-Validation
- H1 L8745: 5.1.1 The Validation Set Approach
- H1 L8816: 5.1.2 Leave-One-Out Cross-Validation
- H1 L8905: 5.1.3 k-Fold Cross-Validation
- H1 L8987: 5.1.4 Bias-Variance Trade-Of for k-Fold Cross-Validation
- H1 L8997: 5.1.5 Cross-Validation on Classifcation Problems
- H1 L9054: 5.2 The Bootstrap
- H1 L9532: 5.3 Lab: Cross-Validation and the Bootstrap
- H1 L9564: 5.3.1 The Validation Set Approach
- H1 L9663: 5.3.2 Cross-Validation
- H1 L9792: 5.3.3 The Bootstrap
- H1 L9796: Estimating the Accuracy of a Statistic of Interest
- H1 L9874: Estimating the Accuracy of a Linear Regression Model
- H1 L9984: 5.4 Exercises
- H1 L9986: Conceptual
- H1 L10025: Applied
- H1 L10116: 6
- H1 L10118: Linear Model Selection and Regularization
- H1 L10148: 6.1 Subset Selection
- H1 L10152: 6.1.1 Best Subset Selection
- H1 L10160: Algorithm 6.1 Best subset selection
- H1 L10220: Algorithm 6.2 Forward stepwise selection
- H1 L10230: 6.1.2 Stepwise Selection
- H1 L10236: Forward Stepwise Selection
- H1 L10254: Backward Stepwise Selection
- H1 L10262: Algorithm 6.3 Backward stepwise selection
- H1 L10276: Hybrid Approaches
- H1 L10280: 6.1.3 Choosing the Optimal Model
- H1 L10291: $C _ { p } ,$ , AIC, BIC, and Adjusted $R ^ { 2 }$
- H1 L10381: Validation and Cross-Validation
- H1 L10437: 6.2 Shrinkage Methods
- H1 L10441: 6.2.1 Ridge Regression
- H1 L10481: An Application to the Credit Data
- H1 L10495: Why Does Ridge Regression Improve Over Least Squares?
- H1 L10520: 6.2.2 The Lasso
- H1 L10557: Another Formulation for Ridge Regression and the Lasso
- H1 L10585: The Variable Selection Property of the Lasso
- H1 L10612: Comparing the Lasso and Ridge Regression
- H1 L10690: A Simple Special Case for Ridge Regression and the Lasso
- H1 L10764: Bayesian Interpretation of Ridge Regression and the Lasso
- H1 L10857: 6.2.3 Selecting the Tuning Parameter
- H1 L10870: 6.3 Dimension Reduction Methods
- H1 L10932: 6.3.1 Principal Components Regression
- H1 L10936: An Overview of Principal Components Analysis
- H1 L11054: The Principal Components Regression Approach
- H1 L11216: 6.3.2 Partial Least Squares
- H1 L11252: 6.4 Considerations in High Dimensions
- H1 L11254: 6.4.1 High-Dimensional Data
- H1 L11268: 6.4.2 What Goes Wrong in High Dimensions?
- H1 L11372: 6.4.3 Regression in High Dimensions
- H1 L11382: 6.4.4 Interpreting Results in High Dimensions
- H1 L11390: 6.5 Lab: Linear Models and Regularization Methods
- H1 L11430: 6.5.1 Subset Selection Methods
- H1 L11434: Forward Selection
- H1 L11524: Choosing Among Models Using the Validation Set Approach and Cross-Validation
- H1 L11662: Best Subset Selection
- H1 L11695: 6.5.2 Ridge Regression and the Lasso
- H1 L11699: Ridge Regression
- H1 L11879: Estimating Test Error of Ridge Regression
- H1 L11983: Fast Cross-Validation for Solution Paths
- H1 L12034: Evaluating Test Error of Cross-Validated Ridge
- H1 L12058: The Lasso
- H1 L12129: 6.5.3 PCR and PLS Regression
- H1 L12131: Principal Components Regression
- H1 L12217: Partial Least Squares
- H1 L12257: 6.6 Exercises
- H1 L12259: Conceptual
- H1 L12353: Applied
- H1 L12438: 7.1 Polynomial Regression
- H1 L12492: 7.2 Step Functions
- H1 L12554: 7.3 Basis Functions
- H1 L12568: 7.4 Regression Splines
- H1 L12572: 7.4.1 Piecewise Polynomials
- H1 L12603: 7.4.2 Constraints and Splines
- H1 L12613: 7.4.3 The Spline Basis Representation
- H1 L12657: 7.4.4 Choosing the Number and Locations of the Knots
- H1 L12729: 7.4.5 Comparison to Polynomial Regression
- H1 L12751: 7.5 Smoothing Splines
- H1 L12755: 7.5.1 An Overview of Smoothing Splines
- H1 L12773: 7.5.2 Choosing the Smoothing Parameter λ
- H1 L12824: 7.6 Local Regression
- H1 L12878: Algorithm 7.1 Local Regression At $X = x _ { 0 }$
- H1 L12908: 7.7 Generalized Additive Models
- H1 L12921: 7.7.1 GAMs for Regression Problems
- H1 L12960: Pros and Cons of GAMs
- H1 L12972: 7.7.2 GAMs for Classifcation Problems
- H1 L13005: 7.8 Lab: Non-Linear Modeling
- H1 L13046: 7.8.1 Polynomial Regression and Step Functions
- H1 L13259: 7.8.2 Splines
- H1 L13355: 7.8.3 Smoothing Splines and GAMs
- H1 L13441: Additive Models with Several Terms
- H1 L13593: ANOVA Tests for Additive Models
- H1 L13716: 7.8.4 Local Regression
- H1 L13744: 7.9 Exercises
- H1 L13746: Conceptual
- H1 L13840: Applied
- H1 L13905: 8.1 The Basics of Decision Trees
- H1 L13909: 8.1.1 Regression Trees
- H1 L13931: Predicting Baseball Players’ Salaries Using Regression Trees
- H1 L13955: Prediction via Stratifcation of the Feature Space
- H1 L14047: Tree Pruning
- H1 L14069: Algorithm 8.1 Building a Regression Tree
- H1 L14081: 8.1.2 Classifcation Trees
- H1 L14184: 8.1.3 Trees Versus Linear Models
- H1 L14204: 8.1.4 Advantages and Disadvantages of Trees
- H1 L14221: 8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees
- H1 L14231: 8.2.1 Bagging
- H1 L14281: Out-of-Bag Error Estimation
- H1 L14287: Variable Importance Measures
- H1 L14321: 8.2.2 Random Forests
- H1 L14337: 8.2.3 Boosting
- H1 L14375: Algorithm 8.2 Boosting for Regression Trees
- H1 L14430: 8.2.4 Bayesian Additive Regression Trees
- H1 L14533: Algorithm 8.3 Bayesian Additive Regression Trees
- H1 L14590: 8.2.5 Summary of Tree Ensemble Methods
- H1 L14599: 8.3 Lab: Tree-Based Methods
- H1 L14632: 8.3.1 Fitting Classifcation Trees
- H1 L14856: 8.3.2 Fitting Regression Trees
- H1 L14932: 8.3.3 Bagging and Random Forests
- H1 L15015: 8.3.4 Boosting
- H1 L15087: 8.3.5 Bayesian Additive Regression Trees
- H1 L15136: 8.4 Exercises
- H1 L15138: Conceptual
- H1 L15203: Applied
- H1 L15248: 9
- H1 L15250: Support Vector Machines
- H1 L15260: 9.1 Maximal Margin Classifer
- H1 L15264: 9.1.1 What Is a Hyperplane?
- H1 L15298: 9.1.2 Classifcation Using a Separating Hyperplane
- H1 L15353: 9.1.3 The Maximal Margin Classifer
- H1 L15441: 9.1.4 Construction of the Maximal Margin Classifer
- H1 L15473: 9.1.5 The Non-separable Case
- H1 L15523: 9.2 Support Vector Classifers
- H1 L15525: 9.2.1 Overview of the Support Vector Classifer
- H1 L15637: 9.2.2 Details of the Support Vector Classifer
- H1 L15715: 9.3 Support Vector Machines
- H1 L15773: 9.3.1 Classifcation with Non-Linear Decision Boundaries
- H1 L15805: 9.3.2 The Support Vector Machine
- H1 L15946: 9.3.3 An Application to the Heart Disease Data
- H1 L15998: 9.4 SVMs with More than Two Classes
- H1 L16002: 9.4.1 One-Versus-One Classifcation
- H1 L16008: 9.4.2 One-Versus-All Classifcation
- H1 L16014: 9.5 Relationship to Logistic Regression
- H1 L16077: 9.6 Lab: Support Vector Machines
- H1 L16110: 9.6.1 Support Vector Classifer
- H1 L16325: 9.6.2 Support Vector Machine
- H1 L16435: 9.6.3 ROC Curves
- H1 L16507: 9.6.4 SVM with Multiple Classes
- H1 L16541: 9.6.5 Application to Gene Expression Data
- H1 L16594: 9.7 Exercises
- H1 L16596: Conceptual
- H1 L16649: Applied
- H1 L16771: 10.1 Single Layer Neural Networks
- H1 L16887: 10.2 Multilayer Neural Networks
- H1 L17077: 10.3 Convolutional Neural Networks
- H1 L17113: 10.3.1 Convolution Layers
- H1 L17172: 10.3.2 Pooling Layers
- H1 L17184: 10.3.3 Architecture of a Convolutional Neural Network
- H1 L17231: 10.3.4 Data Augmentation
- H1 L17244: 10.3.5 Results Using a Pretrained Classifer
- H1 L17270: 10.4 Document Classifcation
- H1 L17348: 10.5 Recurrent Neural Networks
- H1 L17434: 10.5.1 Sequential Models for Document Classifcation
- H1 L17499: 10.5.2 Time Series Forecasting
- H1 L17581: RNN forecaster
- H1 L17618: Autoregression
- H1 L17648: 10.5.3 Summary of RNNs
- H1 L17662: 10.6 When to Use Deep Learning
- H1 L17688: 10.7 Fitting a Neural Network
- H1 L17740: 10.7.1 Backpropagation
- H1 L17792: 10.7.2 Regularization and Stochastic Gradient Descent
- H1 L17902: 10.7.3 Dropout Learning
- H1 L17908: 10.7.4 Network Tuning
- H1 L17959: 10.8 Interpolation and Double Descent
- H1 L18085: 10.9 Lab: Deep Learning
- H1 L18111: Torch-Specifc Imports
- H1 L18190: 10.9.1 Single Layer Network on Hitters Data
- H1 L18230: Linear Models
- H1 L18293: Specifying a Network: Classes and Inheritance
- H1 L18499: Cleanup
- H1 L18517: 10.9.2 Multilayer Network on the MNIST Digit Data
- H1 L18744: 10.9.3 Convolutional Neural Networks
- H1 L18940: Hardware Acceleration
- H1 L18965: 10.9.4 Using Pretrained CNN Models
- H1 L19084: 10.9.5 IMDB Document Classifcation
- H1 L19199: Comparison to Lasso
- H1 L19299: 10.9.6 Recurrent Neural Networks
- H1 L19303: Sequential Models for Document Classifcation
- H1 L19411: Time Series Prediction
- H1 L19680: 10.10 Exercises
- H1 L19682: Conceptual
- H1 L19712: Applied
- H1 L19748: 11.1 Survival and Censoring Times
- H1 L19768: 11.2 A Closer Look at Censoring
- H1 L19791: 11.3 The Kaplan–Meier Survival Curve
- H1 L19893: 11.4 The Log-Rank Test
- H1 L19945: 11.5 Regression Models With a Survival Response
- H1 L19951: 11.5.1 The Hazard Function
- H1 L20009: 11.5.2 Proportional Hazards
- H1 L20089: Cox’s Proportional Hazards Model
- H1 L20125: Connection With The Log-Rank Test
- H1 L20137: Additional Details
- H1 L20146: 11.5.3 Example: Brain Cancer Data
- H1 L20156: 11.5.4 Example: Publication Data
- H1 L20190: 11.6 Shrinkage for the Cox Model
- H1 L20235: 11.7 Additional Topics
- H1 L20237: 11.7.1 Area Under the Curve for Survival Analysis
- H1 L20273: 11.7.2 Choice of Time Scale
- H1 L20279: 11.7.3 Time-Dependent Covariates
- H1 L20289: 11.7.4 Checking the Proportional Hazards Assumption
- H1 L20293: 11.7.5 Survival Trees
- H1 L20301: 11.8 Lab: Survival Analysis
- H1 L20327: 11.8.1 Brain Cancer Data
- H1 L20538: 11.8.2 Publication Data
- H1 L20577: 11.8.3 Call Center Data
- H1 L20778: 11.9 Exercises
- H1 L20780: Conceptual
- H1 L20892: Applied
- H1 L20912: 12
- H1 L20914: Unsupervised Learning
- H1 L20922: 12.1 The Challenge of Unsupervised Learning
- H1 L20932: 12.2 Principal Components Analysis
- H1 L20944: 12.2.1 What Are Principal Components?
- H1 L21087: 12.2.2 Another Interpretation of Principal Components
- H1 L21223: 12.2.3 The Proportion of Variance Explained
- H1 L21299: 12.2.4 More on PCA
- H1 L21301: Scaling the Variables
- H1 L21339: Uniqueness of the Principal Components
- H1 L21343: Deciding How Many Principal Components to Use
- H1 L21353: 12.2.5 Other Uses for Principal Components
- H1 L21357: 12.3 Missing Values and Matrix Completion
- H1 L21377: Principal Components with Missing Values
- H1 L21396: Algorithm 12.1 Iterative Algorithm for Matrix Completion
- H1 L21438: Recommender Systems
- H1 L21494: 12.4 Clustering Methods
- H1 L21511: 12.4.1 K-Means Clustering
- H1 L21564: Algorithm 12.2 K-Means Clustering
- H1 L21591: 12.4.2 Hierarchical Clustering
- H1 L21740: Interpreting a Dendrogram
- H1 L22112: Algorithm 12.3 Hierarchical Clustering
- H1 L22121: The Hierarchical Clustering Algorithm
- H1 L22133: Choice of Dissimilarity Measure
- H1 L22220: 12.4.3 Practical Issues in Clustering
- H1 L22224: Small Decisions with Big Consequences
- H1 L22270: Validating the Clusters Obtained
- H1 L22309: Other Considerations in Clustering
- H1 L22315: A Tempered Approach to Interpreting the Results of Clustering
- H1 L22319: 12.5 Lab: Unsupervised Learning
- H1 L22345: 12.5.1 Principal Components Analysis
- H1 L22564: 12.5.2 Matrix Completion
- H1 L22716: 12.5.3 Clustering
- H1 L22718: K-Means Clustering
- H1 L22788: Hierarchical Clustering
- H1 L22915: 12.5.4 NCI60 Data Example
- H1 L22965: PCA on the NCI60 Data
- H1 L23178: Clustering the Observations of the NCI60 Data
- H1 L23328: 12.6 Exercises
- H1 L23330: Conceptual
- H1 L23376: Applied
- H1 L23441: 13
- H1 L23443: Multiple Testing
- H1 L23461: 13.1 A Quick Review of Hypothesis Testing
- H1 L23470: 13.1.1 Testing a Hypothesis
- H1 L23474: Step 1: Defne the Null and Alternative Hypotheses
- H1 L23489: Step 2: Construct the Test Statistic
- H1 L23524: Step 3: Compute the p-Value
- H1 L23548: Step 4: Decide Whether to Reject the Null Hypothesis
- H1 L23556: 13.1.2 Type I and Type II Errors
- H1 L23572: 13.2 The Challenge of Multiple Testing
- H1 L23596: 13.3 The Family-Wise Error Rate
- H1 L23600: 13.3.1 What is the Family-Wise Error Rate?
- H1 L23652: 13.3.2 Approaches to Control the Family-Wise Error Rate
- H1 L23658: The Bonferroni Method
- H1 L23678: Holm’s Step-Down Procedure
- H1 L23682: Algorithm 13.1 Holm’s Step-Down Procedure to Control the FWER
- H1 L23701: Two Special Cases: Tukey’s Method and Schefé’s Method
- H1 L23831: 13.3.3 Trade-Of Between the FWER and Power
- H1 L23860: 13.4 The False Discovery Rate
- H1 L23862: 13.4.1 Intuition for the False Discovery Rate
- H1 L23886: 13.4.2 The Benjamini–Hochberg Procedure
- H1 L23890: Algorithm 13.2 Benjamini–Hochberg Procedure to Control the FDR
- H1 L23925: 13.5 A Re-Sampling Approach to p-Values and False Discovery Rates
- H1 L23937: 13.5.1 A Re-Sampling Approach to the p-Value
- H1 L23959: Algorithm 13.3 Re-Sampling p-Value for a Two-Sample t-Test
- H1 L23979: 13.5.2 A Re-Sampling Approach to the False Discovery Rate
- H1 L24047: 13.5.3 When Are Re-Sampling Approaches Useful?
- H1 L24051: Algorithm 13.4 Plug-In FDR for a Two-Sample T -Test
- H1 L24098: 13.6 Lab: Multiple Testing
- H1 L24128: 13.6.1 Review of Hypothesis Tests
- H1 L24206: 13.6.2 Family-Wise Error Rate
- H1 L24349: 13.6.3 False Discovery Rate
- H1 L24425: 13.6.4 A Re-Sampling Approach
- H1 L24588: 13.7 Exercises
- H1 L24590: Conceptual
- H1 L24643: Applied

## 自动抽取的教学卡片

> [!todo] 本书候选大节共有 443 个，本文件先生成前 120 个教学卡片；完整层级见上方索引。

### 1. An Introduction to Statistical Learning

- 原始层级：H1，源行：L9
- 推荐周次：第 3 周, 第 4 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Chiara Nappi and Edward Witten
- Michael, Daniel, and Catherine
- Charlie, Ryan, Julie, and Cheryl

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Since it was published in 2013, ISLR has become a mainstay of undergraduate and graduate classrooms worldwide, as well as an important reference book for data scientists. One of the keys to its success has been that, be…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「An Introduction to Statistical Learning」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 2. Contents

- 原始层级：H1，源行：L59
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Contents」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 3. Preface vii

- 原始层级：H1，源行：L61
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Preface vii」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 4. 1 Introduction 1

- 原始层级：H1，源行：L63
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1 Introduction 1」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 5. 2 Statistical Learning 15

- 原始层级：H1，源行：L65
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 2.1 What Is Statistical Learning? 15
- 2.1.1 Why Estimate $f$ ? 17 2.1.2 How Do We Estimate $f$ ? 20 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability ..... 23 2.1.4 Supervised Versus Unsupervised Learning ..... 25 2.1.5 Regression V…
- 2.2 Assessing Model Accuracy 27

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 2.3 Lab: Introduction to Python 40

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2 Statistical Learning 15」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 6. 3 Linear Regression 69

- 原始层级：H1，源行：L95
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 3.1 Simple Linear Regression 70
- 3.1.1 Estimating the Coefficients 71 3.1.2 Assessing the Accuracy of the Coefficient Estimates 72 3.1.3 Assessing the Accuracy of the Model ..... 77
- 3.2 Multiple Linear Regression 80

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 3.6 Lab: Linear Regression 116

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3 Linear Regression 69」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 7. 4 Classification 135

- 原始层级：H1，源行：L139
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 4.1 An Overview of Classification ..... 135
- 4.2 Why Not Linear Regression? 136
- 4.3.1 The Logistic Model ..... 139

#### 公式与符号

- 4.4.1 Linear Discriminant Analysis for $p = 1 \ldots 147$

#### 例子 / 代码 / 图表

- 4.7 Lab: Logistic Regression, LDA, QDA, and KNN ..... 173

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4 Classification 135」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 8. 5 Resampling Methods 201

- 原始层级：H1，源行：L199
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 5.1.1 The Validation Set Approach ..... 202 5.1.2 Leave-One-Out Cross-Validation 204 5.1.3 k-Fold Cross-Validation 206 5.1.4 Bias-Variance Trade-Off for $k$ -Fold Cross-Validation 208 5.1.5 Cross-Validation on Classific…
- 5.3 Lab: Cross-Validation and the Bootstrap ..... 215
- 5.3.1 The Validation Set Approach 216 5.3.2 Cross-Validation 217 5.3.3 The Bootstrap 220

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 5.3 Lab: Cross-Validation and the Bootstrap ..... 215

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5 Resampling Methods 201」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 9. 6 Linear Model Selection and Regularization 229

- 原始层级：H1，源行：L219
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 6.1.1 Best Subset Selection . . . . . . . . . . . . . . . 231 6.1.2 Stepwise Selection 233 6.1.3 Choosing the Optimal Model 235
- 6.2.1 Ridge Regression 240 6.2.2 The Lasso 244 6.2.3 Selecting the Tuning Parameter ..... 252
- 6.3 Dimension Reduction Methods 253

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 6.5 Lab: Linear Models and Regularization Methods ..... 267

#### 备课摘取建议

- 若用于 PPT，可把本节作为「6 Linear Model Selection and Regularization 229」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 10. 7 Moving Beyond Linearity 289

- 原始层级：H1，源行：L253
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 7.1 Polynomial Regression 290 7.2 Step Functions 292 7.3 Basis Functions 293 7.4 Regression Splines 294
- 7.4.1 Piecewise Polynomials 294 7.4.2 Constraints and Splines 296 7.4.3 The Spline Basis Representation 296 7.4.4 Choosing the Number and Locations of the Knots . 297 7.4.5 Comparison to Polynomial Regression ..... 299
- 7.5.1 An Overview of Smoothing Splines ..... 300 7.5.2 Choosing the Smoothing Parameter $\lambda$ 301

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 7.8 Lab: Non-Linear Modeling 309

#### 备课摘取建议

- 若用于 PPT，可把本节作为「7 Moving Beyond Linearity 289」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 11. 8 Tree-Based Methods 331

- 原始层级：H1，源行：L287
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 8.1 The Basics of Decision Trees 331
- 8.1.1 Regression Trees 331 8.1.2 Classification Trees 337 8.1.3 Trees Versus Linear Models 341 8.1.4 Advantages and Disadvantages of Trees ..... 341
- 8.2 Bagging, Random Forests, Boosting, and Bayesian Additive Regression Trees 343

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 8.3 Lab: Tree-Based Methods ..... 354

#### 备课摘取建议

- 若用于 PPT，可把本节作为「8 Tree-Based Methods 331」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 12. 9 Support Vector Machines 367

- 原始层级：H1，源行：L314
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 9.1 Maximal Margin Classifier 367
- 9.1.1 What Is a Hyperplane? 368 9.1.2 Classification Using a Separating Hyperplane . . . 368 9.1.3 The Maximal Margin Classifier ..... 370 9.1.4 Construction of the Maximal Margin Classifier . . 372 9.1.5 The Non-separa…
- 9.2 Support Vector Classifiers ..... 373

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 9.1.1 What Is a Hyperplane? 368 9.1.2 Classification Using a Separating Hyperplane . . . 368 9.1.3 The Maximal Margin Classifier ..... 370 9.1.4 Construction of the Maximal Margin Classifier . . 372 9.1.5 The Non-separa…
- 9.6 Lab: Support Vector Machines 387

#### 备课摘取建议

- 若用于 PPT，可把本节作为「9 Support Vector Machines 367」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 13. 10 Deep Learning 399

- 原始层级：H1，源行：L358
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 10.1 Single Layer Neural Networks 400
- 10.2 Multilayer Neural Networks ..... 402
- 10.3 Convolutional Neural Networks ..... 406

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「10 Deep Learning 399」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 14. 11 Survival Analysis and Censored Data 469

- 原始层级：H1，源行：L416
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- 11.1 Survival and Censoring Times 470
- 11.2 A Closer Look at Censoring . . . . . . . . . . . . . . . . . 470
- 11.3 The Kaplan-Meier Survival Curve 472

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 11.5.1 The Hazard Function . . . . . . . . . . . . . . . . 476 11.5.2 Proportional Hazards 478 11.5.3 Example: Brain Cancer Data 482 11.5.4 Example: Publication Data 482
- 11.8 Lab: Survival Analysis ..... 489

#### 备课摘取建议

- 若用于 PPT，可把本节作为「11 Survival Analysis and Censored Data 469」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 15. 12 Unsupervised Learning 503

- 原始层级：H1，源行：L451
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 12.1 The Challenge of Unsupervised Learning ..... 503
- 12.2 Principal Components Analysis ..... 504
- 12.2.1 What Are Principal Components? ..... 505 12.2.2 Another Interpretation of Principal Components . 508 12.2.3 The Proportion of Variance Explained ..... 510 12.2.4 More on PCA 512 12.2.5 Other Uses for Principal Co…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 12.5 Lab: Unsupervised Learning 535
- 12.5.1 Principal Components Analysis ..... 535 12.5.2 Matrix Completion 539 12.5.3 Clustering 542 12.5.4 NCI60 Data Example . . . . . . . . . . . . . . . . 546

#### 备课摘取建议

- 若用于 PPT，可把本节作为「12 Unsupervised Learning 503」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 16. 13 Multiple Testing 557

- 原始层级：H1，源行：L480
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- 13.1 A Quick Review of Hypothesis Testing 558
- 13.1.1 Testing a Hypothesis 558 13.1.2 Type I and Type II Errors ..... 562
- 13.2 The Challenge of Multiple Testing ..... 563

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 13.6 Lab: Multiple Testing 583

#### 备课摘取建议

- 若用于 PPT，可把本节作为「13 Multiple Testing 557」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 17. 1

- 原始层级：H1，源行：L517
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 18. Introduction

- 原始层级：H1，源行：L519
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 图片引用：`images/cf2e343907325803647d8b376eeb95b322cc7b0e11025cac648dfc6a61cf3c52.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Introduction」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 19. An Overview of Statistical Learning

- 原始层级：H1，源行：L523
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Statistical learning refers to a vast set of tools for understanding data. These tools can be classified as supervised or unsupervised. Broadly speaking, supervised statistical learning involves building a statistical m…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「An Overview of Statistical Learning」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 20. Wage Data

- 原始层级：H1，源行：L527
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- FIGURE 1.1. Wage data, which contains income survey information for men from the central Atlantic region of the United States. Left: wage as a function of age. On average, wage increases with age until about 60 years of…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- FIGURE 1.1. Wage data, which contains income survey information for men from the central Atlantic region of the United States. Left: wage as a function of age. On average, wage increases with age until about 60 years of…
- 图片引用：`images/4caea96ff4e28145fc3ee5c482671965dd2a8f0309ae6a4ae4e6869aa2716393.jpg`
- 图片引用：`images/8071d42469fb727159e986d7eebacfcf6f0e36fa67162db7a77f459c52741220.jpg`
- 图片引用：`images/dbf4e6bad74f5ace5261f89a714e198022620679113864cb355f2285463e1543.jpg`
- 表格行：| Age | Wage |
- 表格行：| --- | --- |
- 表格行：| 20 | 50 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Wage Data」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 21. Stock Market Data

- 原始层级：H1，源行：L574
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- FIGURE 1.2. Left: Boxplots of the previous day's percentage change in the S&P index for the days for which the market increased or decreased, obtained from the Smarket data. Center and Right: Same as left panel, but the…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- FIGURE 1.2. Left: Boxplots of the previous day's percentage change in the S&P index for the days for which the market increased or decreased, obtained from the Smarket data. Center and Right: Same as left panel, but the…
- 图片引用：`images/14dedf2f3656e4c77e4f50c94b1a2d6788a9df14467e837cae26a55127ab9b2d.jpg`
- 图片引用：`images/1f08dc9995c82ca6dd045cb188fba5c93ee9dd6bcf84f8a4d034bb166f9aab75.jpg`
- 图片引用：`images/9900b645dc4ef59306e7b35d52fcedeb15b450c209587d0166bcd049f7313dcf.jpg`
- 表格行：| Today's Direction | Percentage change in S&P |
- 表格行：| ------------------ | ------------------------ |
- 表格行：| Down | -3.0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Stock Market Data」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 22. Gene Expression Data

- 原始层级：H1，源行：L672
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The previous two applications illustrate data sets with both input and output variables. However, another important class of problems involves situations in which we only observe input variables, with no corresponding o…
- FIGURE 1.3. We fit a quadratic discriminant analysis model to the subset of the Smarket data corresponding to the 2001–2004 time period, and predicted the probability of a stock market decrease using the 2005 data. On a…
- We devote Chapter 12 to a discussion of statistical learning methods for problems in which no natural output variable is available. We consider the NCI60 data set, which consists of 6,830 gene expression measurements fo…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- The previous two applications illustrate data sets with both input and output variables. However, another important class of problems involves situations in which we only observe input variables, with no corresponding o…
- FIGURE 1.3. We fit a quadratic discriminant analysis model to the subset of the Smarket data corresponding to the 2001–2004 time period, and predicted the probability of a stock market decrease using the 2005 data. On a…
- The left-hand panel of Figure 1.4 addresses this problem by representing each of the 64 cell lines using just two numbers, $Z_{1}$ and $Z_{2}$ . These are the first two principal components of the data, which summarize…
- 图片引用：`images/71ae5126120af360dc1b47324dcba0f8fea6bf223a45c64504056528963d76fd.jpg`
- 图片引用：`images/5761e6136a3a5c219f27ee1b86be370930bfa0ae0b7a6485dea7244d4da2cd5d.jpg`
- 图片引用：`images/e72b3e3f2651677ddfe869892ae3132280e6fa875bed8883264dc270dd3b3164.jpg`
- 表格行：| Today's Direction | Predicted Probability (Min) | Predicted Probability (Q1) | Predicted Probability (Max) |
- 表格行：| ------------------ | --------------------------- | -------------------------- | --------------------------- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Gene Expression Data」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 23. A Brief History of Statistical Learning

- 原始层级：H1，源行：L809
- 推荐周次：第 3 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- By the end of the 1970s, many more techniques for learning from data were available. However, they were almost exclusively linear methods because fitting non-linear relationships was computationally difficult at the tim…
- Since that time, statistical learning has emerged as a new subfield in statistics, focused on supervised and unsupervised modeling and prediction. In recent years, progress in statistical learning has been marked by the…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「A Brief History of Statistical Learning」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 24. This Book

- 原始层级：H1，源行：L817
- 推荐周次：第 3 周, 第 4 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- The Elements of Statistical Learning (ESL) by Hastie, Tibshirani, and Friedman was first published in 2001. Since that time, it has become an important reference on the fundamentals of statistical machine learning. Its…
- In recent years, new and improved software packages have significantly eased the implementation burden for many statistical learning methods. At the same time, there has been growing recognition across a number of field…
- The purpose of An Introduction to Statistical Learning (ISL) is to facilitate the transition of statistical learning from an academic to a mainstream field. ISL is not intended to replace ESL, which is a far more compre…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- with computer labs written in the R language. Since then, there has been increasing demand for Python implementations of the important techniques in statistical learning. Consequently, this version has labs in Python. T…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「This Book」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 25. Who Should Read This Book?

- 原始层级：H1，源行：L838
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The first edition of this textbook has been used to teach master's and PhD students in business, economics, computer science, biology, earth sciences, psychology, and many other areas of the physical and social sciences…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Who Should Read This Book?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 26. Notation and Simple Matrix Algebra

- 原始层级：H1，源行：L844
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Choosing notation for a textbook is always a difficult task. For the most part we adopt the same notational conventions as ESL.
- We will use n to represent the number of distinct data points, or observations, in our sample. We will let p denote the number of variables that are available for use in making predictions. For example, the Wage data se…
- In some examples, p might be quite large, such as on the order of thousands or even millions; this situation arises quite often, for example, in the analysis of modern biological data or web-based advertising data.

#### 公式与符号

- $$
- \mathbf {X} = \left( \begin{array}{c c c c} x _ {1 1} & x _ {1 2} & \ldots & x _ {1 p} \\ x _ {2 1} & x _ {2 2} & \ldots & x _ {2 p} \\ \vdots & \vdots & \ddots & \vdots \\ x _ {n 1} & x _ {n 2} & \ldots & x _ {n p} \en…
- $$
- $$
- x _ {i} = \left( \begin{array}{c} x _ {i 1} \\ x _ {i 2} \\ \vdots \\ x _ {i p} \end{array} \right). \tag {1.1}

#### 例子 / 代码 / 图表

- We will use n to represent the number of distinct data points, or observations, in our sample. We will let p denote the number of variables that are available for use in making predictions. For example, the Wage data se…
- In some examples, p might be quite large, such as on the order of thousands or even millions; this situation arises quite often, for example, in the analysis of modern biological data or web-based advertising data.
- (Vectors are by default represented as columns.) For example, for the Wage data, $x_{i}$ is a vector of length 11, consisting of year, age, race, and other values for the ith individual. At other times we will instead b…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Notation and Simple Matrix Algebra」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 27. Organization of This Book

- 原始层级：H1，源行：L928
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Chapter 2 introduces the basic terminology and concepts behind statistical learning. This chapter also presents the K-nearest neighbor classifier, a very simple method that works surprisingly well on many problems. Chap…
- A central problem in all statistical learning situations involves choosing the best method for a given application. Hence, in Chapter 5 we introduce cross-validation and the bootstrap, which can be used to estimate the…
- Much of the recent research in statistical learning has concentrated on non-linear methods. However, linear methods often have advantages over their non-linear competitors in terms of interpretability and sometimes also…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Organization of This Book」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 28. Data Sets Used in Labs and Exercises

- 原始层级：H1，源行：L948
- 推荐周次：第 3 周, 第 4 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In this textbook, we illustrate statistical learning methods using applications from marketing, finance, biology, and other areas. The ISLP package contains a number of data sets that are required in order to perform th…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Data Sets Used in Labs and Exercises」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 29. Book Website

- 原始层级：H1，源行：L952
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The website for this book is located at
- It contains a number of resources, including the Python package associated with this book, and some additional data sets.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Book Website」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 30. Acknowledgements

- 原始层级：H1，源行：L960
- 推荐周次：第 3 周, 第 4 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- A few of the plots in this book were taken from ESL: Figures 6.7, 8.3, and 12.14. All other plots were produced for the R version of ISL, except for Figure 13.10 which differs because of the Python software supporting t…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- A few of the plots in this book were taken from ESL: Figures 6.7, 8.3, and 12.14. All other plots were produced for the R version of ISL, except for Figure 13.10 which differs because of the Python software supporting t…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Acknowledgements」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 31. 2

- 原始层级：H1，源行：L964
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 32. Statistical Learning

- 原始层级：H1，源行：L966
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 图片引用：`images/e6673d90e565b41c7f69f746c92bc187daca3467a5923867a7909520f1fe002a.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Statistical Learning」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 33. 2.1 What Is Statistical Learning?

- 原始层级：H1，源行：L970
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In this setting, the advertising budgets are input variables while sales is an output variable. The input variables are typically denoted using the symbol X, with a subscript to distinguish them. So $X_{1}$ might be the…
- More generally, suppose that we observe a quantitative response Y and p different predictors, $X_{1}, X_{2}, \ldots, X_{p}$ . We assume that there is some relationship between Y and $X = (X_{1}, X_{2}, \ldots, X_{p})$ ,…
- $$ Y = f (X) + \epsilon . \tag {2.1} $$

#### 公式与符号

- $$
- Y = f (X) + \epsilon . \tag {2.1}
- $$

#### 例子 / 代码 / 图表

- In this setting, the advertising budgets are input variables while sales is an output variable. The input variables are typically denoted using the symbol X, with a subscript to distinguish them. So $X_{1}$ might be the…
- FIGURE 2.1. The Advertising data set. The plot displays sales, in thousands of units, as a function of TV, radio, and newspaper budgets, in thousands of dollars, for 200 different markets. In each plot we show the simpl…
- FIGURE 2.2. The Income data set. Left: The red dots are the observed values of income (in thousands of dollars) and years of education for 30 individuals. Right: The blue curve represents the true underlying relationshi…
- 图片引用：`images/7cce57d248865f92c4275f571b7565e5605dc8891add20543f270f5575effba6.jpg`
- 图片引用：`images/a9664a8d3acfb0e0bb7f73a30cf8aa02670a16c726ffef17b120c25e3ca02eb7.jpg`
- 图片引用：`images/c8db097667ab1b6b5a2ce68fb6805d8d72e609b1ab8d46a948aa4486fcccee5f.jpg`
- 表格行：| TV | Sales |
- 表格行：| --- | ----- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1 What Is Statistical Learning?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 34. 2.1.1 Why Estimate f?

- 原始层级：H1，源行：L1107
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- There are two main reasons that we may wish to estimate $f$ : prediction and inference. We discuss each in turn.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1.1 Why Estimate f?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 35. Prediction

- 原始层级：H1，源行：L1111
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In many situations, a set of inputs X are readily available, but the output Y cannot be easily obtained. In this setting, since the error term averages to zero, we can predict Y using
- $$ \hat {Y} = \hat {f} (X), \tag {2.2} $$
- where $\hat{f}$ represents our estimate for f, and $\hat{Y}$ represents the resulting prediction for Y. In this setting, $\hat{f}$ is often treated as a black box, in the sense that one is not typically concerned with t…

#### 公式与符号

- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- As an example, suppose that $X_{1}, \ldots, X_{p}$ are characteristics of a patient's blood sample that can be easily measured in a lab, and $Y$ is a variable encoding the patient's risk for a severe adverse reaction to…
- Why is the irreducible error larger than zero? The quantity $\epsilon$ may contain unmeasured variables that are useful in predicting $Y$ : since we don't measure them, $f$ cannot use them for its prediction. The quanti…
- FIGURE 2.3. The plot displays income as a function of years of education and seniority in the Income data set. The blue surface represents the true underlying relationship between income and years of education and senio…
- 图片引用：`images/3b195f97ee6321eb801149ffb927e9537ec54deef95729056fcd25d1513c7c9f.jpg`
- 表格行：| Years of Education | Income | Seniority |
- 表格行：| ------------------ | ------ | --------- |
- 表格行：| 0 | 0 | 0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Prediction」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 36. Inference

- 原始层级：H1，源行：L1204
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We are often interested in understanding the association between Y and $X_{1},\ldots,X_{p}$ . In this situation we wish to estimate f, but our goal is not necessarily to make predictions for Y. Now $\hat{f}$ cannot be t…
- \- Which predictors are associated with the response? It is often the case that only a small fraction of the available predictors are substantially associated with Y. Identifying the few important predictors among a lar…
- \- What is the relationship between the response and each predictor? Some predictors may have a positive relationship with $Y$ , in the sense that larger values of the predictor are associated with larger values of $Y$…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- \- Which predictors are associated with the response? It is often the case that only a small fraction of the available predictors are substantially associated with Y. Identifying the few important predictors among a lar…
- \- Can the relationship between Y and each predictor be adequately summarized using a linear equation, or is the relationship more complicated? Historically, most methods for estimating f have taken a linear form. In so…
- For instance, consider a company that is interested in conducting a direct-marketing campaign. The goal is to identify individuals who are likely to respond positively to a mailing, based on observations of demographic…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Inference」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 37. 2.1.2 How Do We Estimate $f$ ?

- 原始层级：H1，源行：L1232
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Our goal is to apply a statistical learning method to the training data in order to estimate the unknown function f. In other words, we want to find a function $\hat{f}$ such that $Y \approx \hat{f}(X)$ for any observat…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1.2 How Do We Estimate $f$ ?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 38. Parametric Methods

- 原始层级：H1，源行：L1242
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Parametric methods involve a two-step model-based approach.
- 1. First, we make an assumption about the functional form, or shape, of $f$ . For example, one very simple assumption is that $f$ is linear in $X$ :
- $$ f (X) = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \dots + \beta_ {p} X _ {p}. \tag {2.4} $$

#### 公式与符号

- $$
- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- 1. First, we make an assumption about the functional form, or shape, of $f$ . For example, one very simple assumption is that $f$ is linear in $X$ :
- FIGURE 2.4. A linear model fit by least squares to the Income data from Figure 2.3. The observations are shown in red, and the yellow plane indicates the least squares fit to the data.
- 2. After a model has been selected, we need a procedure that uses the training data to fit or train the model. In the case of the linear model (2.4), we need to estimate the parameters $\beta_0, \beta_1, \ldots, \beta_p…
- 图片引用：`images/f116d5a279e9f1d7cf5e87fb56713f5dcc3eb3cc9cced18b0fb88b87cc0ceae8.jpg`
- 图片引用：`images/d447286269e5b94ca75040ca54ea2b7f8534c1c20d885fc25956f125f20b4226.jpg`
- 表格行：| Years of Education | Income | Seniority |
- 表格行：| ------------------ | ------ | --------- |
- 表格行：| 1 | 0.5 | 0.2 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Parametric Methods」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 39. Non-Parametric Methods

- 原始层级：H1，源行：L1366
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- An example of a non-parametric approach to fitting the Income data is shown in Figure 2.5. A thin-plate spline is used to estimate f. This approach does not impose any pre-specified model on f. It instead attempts
- FIGURE 2.6. A rough thin-plate spline fit to the Income data from Figure 2.3. This fit makes zero errors on the training data.
- As we have seen, there are advantages and disadvantages to parametric and non-parametric methods for statistical learning. We explore both types of methods throughout this book.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- An example of a non-parametric approach to fitting the Income data is shown in Figure 2.5. A thin-plate spline is used to estimate f. This approach does not impose any pre-specified model on f. It instead attempts
- FIGURE 2.6. A rough thin-plate spline fit to the Income data from Figure 2.3. This fit makes zero errors on the training data.
- 图片引用：`images/fa881fa5877eb5eb5c4b219e200a08dcaf4e62b91bfce667627326462032dc53.jpg`
- 表格行：| Years of Education | Income | Seniority |
- 表格行：| ------------------ | ------ | --------- |
- 表格行：| 0 | 0 | 0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Non-Parametric Methods」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 40. 2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability

- 原始层级：H1，源行：L1441
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Of the many methods that we examine in this book, some are less flexible, or more restrictive, in the sense that they can produce just a relatively small range of shapes to estimate f. For example, linear regression is…
- FIGURE 2.7. A representation of the tradeoff between flexibility and interpretability, using different statistical learning methods. In general, as the flexibility of a method increases, its interpretability decreases.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Of the many methods that we examine in this book, some are less flexible, or more restrictive, in the sense that they can produce just a relatively small range of shapes to estimate f. For example, linear regression is…
- FIGURE 2.7. A representation of the tradeoff between flexibility and interpretability, using different statistical learning methods. In general, as the flexibility of a method increases, its interpretability decreases.
- 图片引用：`images/d92afcf3f394c278737fa0f0c16cb7b1160ad1d2ef982df20015c5f84b68c816.jpg`
- 表格行：| Method | Interpretability | Flexibility |
- 表格行：| --- | --- | --- |
- 表格行：| Subset Selection Lasso | High | Low |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1.3 The Trade-Off Between Prediction Accuracy and Model Interpretability」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 41. 2.1.4 Supervised Versus Unsupervised Learning

- 原始层级：H1，源行：L1468
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- FIGURE 2.8. A clustering data set involving three groups. Each group is shown using a different colored symbol. Left: The three groups are well-separated. In this setting, a clustering approach should successfully ident…
- In the examples shown in Figure 2.8, there are only two variables, and so one can simply visually inspect the scatterplots of the observations in order to identify clusters. However, in practice, we often encounter data…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- FIGURE 2.8. A clustering data set involving three groups. Each group is shown using a different colored symbol. Left: The three groups are well-separated. In this setting, a clustering approach should successfully ident…
- In the examples shown in Figure 2.8, there are only two variables, and so one can simply visually inspect the scatterplots of the observations in order to identify clusters. However, in practice, we often encounter data…
- 图片引用：`images/59f06dd8a6d6afc4929eed476ca7163bffc5d53b321184ec6eac41e772c452f1.jpg`
- 图片引用：`images/3f4dc01723f82738b5188f3357df8f28f07927ebb6e83920d9e934a64ba0d621.jpg`
- 表格行：| X1 | X2 | Group |
- 表格行：|----|----|-------|
- 表格行：| 0 | 6 | A |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1.4 Supervised Versus Unsupervised Learning」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 42. 2.1.5 Regression Versus Classification Problems

- 原始层级：H1，源行：L1504
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We tend to select statistical learning methods on the basis of whether the response is quantitative or qualitative; i.e. we might use linear regression when quantitative and logistic regression when qualitative. However…
- quantitative qualitative categorical class

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.1.5 Regression Versus Classification Problems」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 43. 2.2 Assessing Model Accuracy

- 原始层级：H1，源行：L1520
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- One of the key aims of this book is to introduce the reader to a wide range of statistical learning methods that extend far beyond the standard linear regression approach. Why is it necessary to introduce so many differ…
- In this section, we discuss some of the most important concepts that arise in selecting a statistical learning procedure for a specific data set. As the book progresses, we will explain how the concepts presented here c…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.2 Assessing Model Accuracy」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 44. 2.2.1 Measuring the Quality of Fit

- 原始层级：H1，源行：L1526
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- In order to evaluate the performance of a statistical learning method on a given data set, we need some way to measure how well its predictions actually match the observed data. That is, we need to quantify the extent t…
- $$ \mathrm{MSE} = \frac {1}{n} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {f} (x _ {i})) ^ {2}, \tag {2.5} $$
- where $\hat{f}(x_{i})$ is the prediction that $\hat{f}$ gives for the ith observation. The MSE will be small if the predicted responses are very close to the true responses, and will be large if for some of the observat…

#### 公式与符号

- $$
- \mathrm{MSE} = \frac {1}{n} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {f} (x _ {i})) ^ {2}, \tag {2.5}
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 2.9. Left: Data simulated from f, shown in black. Three estimates of f are shown: the linear regression line (orange curve), and two smoothing spline fits (blue and green curves). Right: Training MSE (grey curve)…
- FIGURE 2.10. Details are as in Figure 2.9, using a different true f that is much closer to linear. In this setting, linear regression provides a very good fit to the data.
- Figure 2.10 provides another example in which the true f is approximately linear. Again we observe that the training MSE decreases monotonically as the model flexibility increases, and that there is a U-shape in the tes…
- 图片引用：`images/bc64534220213c5e34d2935c8277b9c7b1a9a1eafca1a15249192fd2cd133f7d.jpg`
- 图片引用：`images/2eb306495c7863e972775143153271d2e793d37f625aa22b7484719629a92075.jpg`
- 图片引用：`images/637bf1d5969b083aec5f30ddada4b1c6764c47b89b27a3f5141ae1d184da9439.jpg`
- 表格行：| X | Y (Black Line) | Y (Orange Line) | Y (Teal Line) |
- 表格行：|----|----------------|-----------------|---------------|

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.2.1 Measuring the Quality of Fit」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 45. 2.2.2 The Bias-Variance Trade-Off

- 原始层级：H1，源行：L1631
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- The U-shape observed in the test MSE curves (Figures 2.9-2.11) turns out to be the result of two competing properties of statistical learning methods.
- FIGURE 2.11. Details are as in Figure 2.9, using a different f that is far from linear. In this setting, linear regression provides a very poor fit to the data.
- Though the mathematical proof is beyond the scope of this book, it is possible to show that the expected test MSE, for a given value $x_{0}$ , can always be decomposed into the sum of three fundamental quantities: the v…

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 2.11. Details are as in Figure 2.9, using a different f that is far from linear. In this setting, linear regression provides a very poor fit to the data.
- FIGURE 2.12. Squared bias (blue curve), variance (orange curve), Var( $\epsilon$ ) (dashed line), and test MSE (red curve) for the three data sets in Figures 2.9–2.11. The vertical dotted line indicates the flexibility…
- The relationship between bias, variance, and test set MSE given in Equation 2.7 and displayed in Figure 2.12 is referred to as the bias-variance trade-off. Good test set performance of a statistical learning method requ…
- 图片引用：`images/280a9c7250ca8995fdbb29f6a5607f8a5e4d775ae81393aeceae246f5b791bdb.jpg`
- 图片引用：`images/355605b5c2049c224e3a837bd2c043a0d718f563685a3df0149d7d87e50f0e8f.jpg`
- 图片引用：`images/8999c3474b1046ba8e33fc2c8042da0905fb5002b7d57088f0bb05fbb4c8e612.jpg`
- 表格行：| X | Y (Line 1) | Y (Line 2) |
- 表格行：| --- | ---------- | ---------- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.2.2 The Bias-Variance Trade-Off」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 46. 2.2.3 The Classification Setting

- 原始层级：H1，源行：L1743
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Thus far, our discussion of model accuracy has been focused on the regression setting. But many of the concepts that we have encountered, such as the bias-variance trade-off, transfer over to the classification setting…
- $$ \frac {1}{n} \sum_ {i = 1} ^ {n} I (y _ {i} \neq \hat {y} _ {i}). \tag {2.8} $$
- Here $\hat{y}_{i}$ is the predicted class label for the ith observation using $\hat{f}$ . And $I(y_{i} \neq \hat{y}_{i})$ is an indicator variable that equals 1 if $y_{i} \neq \hat{y}_{i}$ and zero if $y_{i} = \hat{y}_{…

#### 公式与符号

- $$
- \frac {1}{n} \sum_ {i = 1} ^ {n} I (y _ {i} \neq \hat {y} _ {i}). \tag {2.8}
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.2.3 The Classification Setting」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 47. The Bayes Classifier

- 原始层级：H1，源行：L1761
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- It is possible to show (though the proof is outside of the scope of this book) that the test error rate given in $(2.9)$ is minimized, on average, by a very simple classifier that assigns each observation to the most li…
- $$ \operatorname * {P r} (Y = j | X = x _ {0}) \tag {2.10} $$
- is largest. Note that $(2.10)$ is a conditional probability: it is the probability that Y = j, given the observed predictor vector $x_{0}$ . This very simple classifier is called the Bayes classifier. In a two-class pro…

#### 公式与符号

- $$
- \operatorname * {P r} (Y = j | X = x _ {0}) \tag {2.10}
- $$
- $$
- 1 - E \left(\max _ {j} \operatorname * {P r} (Y = j | X)\right), \tag {2.11}

#### 例子 / 代码 / 图表

- FIGURE 2.13. A simulated data set consisting of 100 observations in each of two groups, indicated in blue and in orange. The purple dashed line represents the Bayes decision boundary. The orange background grid indicate…
- 图片引用：`images/f046615e3d4bdd2e65bdedf89857bd22416568bb6d076d5059a921e0accc3534.jpg`
- 表格行：| X1 | X2 | Group |
- 表格行：|----|----|-------|
- 表格行：| (various) | (various) | Blue Circle |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「The Bayes Classifier」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 48. K-Nearest Neighbors

- 原始层级：H1，源行：L1815
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- $$ \operatorname * {P r} (Y = j | X = x _ {0}) = \frac {1}{K} \sum_ {i \in \mathcal {N} _ {0}} I (y _ {i} = j). \tag {2.12} $$
- Finally, KNN classifies the test observation $x_0$ to the class with the largest probability from (2.12).
- Despite the fact that it is a very simple approach, KNN can often produce classifiers that are surprisingly close to the optimal Bayes classifier. Figure 2.15 displays the KNN decision boundary, using K = 10, when appli…

#### 公式与符号

- $$
- \operatorname * {P r} (Y = j | X = x _ {0}) = \frac {1}{K} \sum_ {i \in \mathcal {N} _ {0}} I (y _ {i} = j). \tag {2.12}
- $$
- KNN: K=10
- FIGURE 2.15. The black curve indicates the KNN decision boundary on the data from Figure 2.13, using K = 10. The Bayes decision boundary is shown as a purple dashed line. The KNN and Bayes decision boundaries are very s…

#### 例子 / 代码 / 图表

- Despite the fact that it is a very simple approach, KNN can often produce classifiers that are surprisingly close to the optimal Bayes classifier. Figure 2.15 displays the KNN decision boundary, using K = 10, when appli…
- The choice of $K$ has a drastic effect on the KNN classifier obtained. Figure 2.16 displays two KNN fits to the simulated data from Figure 2.13, using $K = 1$ and $K = 100$ . When $K = 1$ , the decision boundary is over…
- Just as in the regression setting, there is not a strong relationship between the training error rate and the test error rate. With K = 1, the KNN training error rate is 0, but the test error rate may be quite high. In…
- 图片引用：`images/d01d163f96b922fd5edb7e9edfd7b6737a539665ead9f2addd36365fd748a30b.jpg`
- 图片引用：`images/3856490aa7471191e59ec429740731bc8ae54df94b0decc789c772a1b852add0.jpg`
- 图片引用：`images/a7bb8f9d7fb421f207a651b0e85591cf3cf5c9d76a753dd1db8bcfbd6b622f9b.jpg`
- 表格行：| X2 | Y |
- 表格行：|----|----|

#### 备课摘取建议

- 若用于 PPT，可把本节作为「K-Nearest Neighbors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 49. 2.3 Lab: Introduction to Python

- 原始层级：H1，源行：L1932
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3 Lab: Introduction to Python」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 50. 2.3.1 Getting Started

- 原始层级：H1，源行：L1934
- 推荐周次：第 3 周, 第 4 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- To run the labs in this book, you will need two things:
- 1. An installation of Python3, which is the specific version of Python used in the labs. 2. Access to Jupyter, a very popular Python interface that runs code through a file called a notebook.
- You can download and install Python3 by following the instructions available at anaconda.com.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- To run this lab, download the file Ch2-statlearn-lab.ipynb from the Python resources page. Now run the following code at the command line: jupyter lab Ch2-statlearn-lab.ipynb.
- If you're using Windows, you can use the start menu to access anaconda, and follow the links. For example, to install ISLP and run this lab, you can run the same code above in an anaconda shell.

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.1 Getting Started」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 51. 2.3.2 Basic Commands

- 原始层级：H1，源行：L1959
- 推荐周次：第 3 周, 第 4 周, 第 5 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In this lab, we will introduce some simple Python commands. For more resources about Python in general, readers may want to consult the tutorial at docs.python.org/3/tutorial/.
- Like most programming languages, Python uses functions to perform operations. To run a function called fun, we type fun(input1, input2), where the inputs (or arguments) input1 and input2 tell Python how to run the funct…
- The following command will provide information about the print() function.

#### 公式与符号

- In [5]: x = [3, 4, 5]
- In [6]: y = [4, 9, 7]

#### 例子 / 代码 / 图表

- In this lab, we will introduce some simple Python commands. For more resources about Python in general, readers may want to consult the tutorial at docs.python.org/3/tutorial/.
- Like most programming languages, Python uses functions to perform operations. To run a function called fun, we type fun(input1, input2), where the inputs (or arguments) input1 and input2 tell Python how to run the funct…
- This example reflects the fact that Python is a general-purpose programming language. Much of Python's data-specific functionality comes from other packages, notably numpy and pandas. In the next section, we will introd…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.2 Basic Commands」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 52. 2.3.3 Introduction to Numerical Python

- 原始层级：H1，源行：L2014
- 推荐周次：第 3 周, 第 4 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- As mentioned earlier, this book makes use of functionality that is contained in the numpy library, or package. A package is a collection of modules that are not necessarily included in the base Python distribution. The…
- To access numpy, we must first import it.
- In the previous line, we named the numpy module np; an abbreviation for easier referencing.

#### 公式与符号

- x = np.array([3, 4, 5])
- y = np.array([4, 9, 7])
- x = np.array([[1, 2], [3, 4]])
- In [17]: x = np.array([1, 2, 3, 4])
- In [18]: x = np.array([1, 2, 3, 4])

#### 例子 / 代码 / 图表

- As another example, the reshape() method returns a new array with the same elements as x, but a different shape. We do this by passing in a tuple
- in our call to reshape(), in this case (2, 3). This tuple specifies that we would like to create a two-dimensional array with 2 rows and 3 columns. $^{2}$
- If you're following along in your own Jupyter notebook, then you probably noticed that you got a different set of results when you ran the past few commands. In particular, each time we call np.random.normal(), we will…
- `txt` 代码块，源行 2025：import numpy as np
- `python` 代码块，源行 2043：x = np.array([3, 4, 5]) / y = np.array([4, 9, 7])
- `txt` 代码块，源行 2054：x + y

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.3 Introduction to Numerical Python」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 53. 2.3.4 Graphics

- 原始层级：H1，源行：L2427
- 推荐周次：第 3 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In Python, common practice is to use the library matplotlib for graphics. However, since Python was not written with data analysis in mind, the notion of plotting is not intrinsic to the language. We will use the subplo…
- In matplotlib, a plot consists of a figure and one or more axes. You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window. The axes contain importa…
- We begin by importing the subplots() function from matplotlib. We use this function throughout when creating figures. The function returns a tuple of length two: a figure object as well as the relevant axes object. We w…

#### 公式与符号

- fig, ax = subplots(figsize=(8, 8))
- x = rng.standard_normal(100)
- y = rng.standard_normal(100)
- In [40]: output = subplots(figsize=(8, 8))
- fig = output[0]

#### 例子 / 代码 / 图表

- In Python, common practice is to use the library matplotlib for graphics. However, since Python was not written with data analysis in mind, the notion of plotting is not intrinsic to the language. We will use the subplo…
- In matplotlib, a plot consists of a figure and one or more axes. You can think of the figure as the blank canvas upon which one or more plots will be displayed: it is the entire plotting window. The axes contain importa…
- We begin by importing the subplots() function from matplotlib. We use this function throughout when creating figures. The function returns a tuple of length two: a figure object as well as the relevant axes object. We w…
- `python` 代码块，源行 2444：In [39]: from matplotlib.pyplot import subplots / fig, ax = subplots(figsize=(8, 8)) / x = rng.standard_normal(100) / y = rng.standard_normal(100)
- `python` 代码块，源行 2454：In [40]: output = subplots(figsize=(8, 8)) / fig = output[0] / ax = output[1]
- `matlab` 代码块，源行 2462：In [41]: fig, ax = subplots(figsize=(8, 8)) / ax.plot(x, y, 'o');

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.4 Graphics」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 54. 2.3.5 Sequences and Slice Notation

- 原始层级：H1，源行：L2590
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- As seen above, the function np.linspace() can be used to create a sequence of numbers.
- The function np.arange() returns a sequence of numbers spaced out by step. If step is not specified, then a default value of 1 is used. Let's create a sequence that starts at 0 and ends at 10.
- Why isn't 10 output above? This has to do with slice notation in Python. Slice notation is used to index sequences such as lists, tuples and arrays. Suppose we want to retrieve the fourth through sixth (inclusive) entri…

#### 公式与符号

- In [52]: seq1 = np.linspace(0, 10, 11)
- In [53]: seq2 = np.arange(0, 10)

#### 例子 / 代码 / 图表

- `txt` 代码块，源行 2594：In [52]: seq1 = np.linspace(0, 10, 11) / seq1
- `txt` 代码块，源行 2599：Out[52]: array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
- `txt` 代码块，源行 2607：In [53]: seq2 = np.arange(0, 10) / seq2

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.5 Sequences and Slice Notation」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 55. 2.3.6 Indexing Data

- 原始层级：H1，源行：L2640
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- To begin, we create a two-dimensional numpy array.
- Typing A[1,2] retrieves the element corresponding to the second row and third column. (As usual, Python indexes from 0.)
- The first number after the open-bracket symbol [ refers to the row, and the second number refers to the column.

#### 公式与符号

- In [56]: A = np.array(np.arange(16)).reshape((4, 4))
- In [64]: idx = np.ix_([1,3], [0,2,3])

#### 例子 / 代码 / 图表

- To select the first and third columns, we pass in $[0,2]$ as the second argument in the square brackets. In this case we need to supply the first argument: which selects all rows.
- `txt` 代码块，源行 2644：In [56]: A = np.array(np.arange(16)).reshape((4, 4)) / A
- `txt` 代码块，源行 2649：Out[56]: array([[0, 1, 2, 3], / [4, 5, 6, 7], / [8, 9, 10, 11], / [12, 13, 14, 15]])
- `json` 代码块，源行 2700：In [63]: A [[1,3]] [:,[0,2]]

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.6 Indexing Data」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 56. Boolean Indexing

- 原始层级：H1，源行：L2740
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In numpy, a Boolean is a type that equals either True or False (also represented as 1 and 0, respectively). The next line creates a vector of 0's, represented as Booleans, of length equal to the first dimension of A.
- We now set two of the elements to True.
- Out[67]: array([False, True, False, True])

#### 公式与符号

- In [66]: keep_rows = np.zeros(A.shape[0], bool)
- In [71]: keep\_cols = np.zeros(A.shape[1], bool)
- idx\_bool = np.ix\_(keep\_rows, keep\_cols)
- In [72]: idx\_mixed = np.ix\_([1,3], keep\_cols)

#### 例子 / 代码 / 图表

- This example shows that Booleans and integers are treated differently by numpy.
- `txt` 代码块，源行 2746：In [66]: keep_rows = np.zeros(A.shape[0], bool) / keep_rows
- `txt` 代码块，源行 2751：Out[66]: array([False, False, False, False])
- `txt` 代码块，源行 2757：In [67]: keep_rows[[1,3]] = True / keep_rows

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Boolean Indexing」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 57. 2.3.7 Loading Data

- 原始层级：H1，源行：L2807
- 推荐周次：第 5 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Data sets often contain different types of data, and may have names associated with the rows or columns. For these reasons, they typically are best accommodated using a data frame. We can think of a data frame as a sequ…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.7 Loading Data」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 58. Reading in a Data Set

- 原始层级：H1，源行：L2813
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The first step of most analyses involves importing a data set into Python. Before attempting to load a data set, we must make sure that Python knows where to find the file containing it. If the file is in the same locat…
- We will begin by reading in Auto.csv, available on the book website. This is a comma-separated file, and can be read in using pd.read\_csv():
- The book website also has a whitespace-delimited version of this data, called Auto.data. This can be read in as follows:

#### 公式与符号

- Auto = pd.read_csv('Auto.csv')
- In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True)
- In [77]: Auto = pd.read_csv('Auto.data', na_values=['?'], delim_whitespace=True)
- In [79]: Auto_new = Auto.dropna()

#### 例子 / 代码 / 图表

- There are various ways to deal with missing data. In this case, since only five of the rows contain missing observations, we choose to use the Auto.dropna() method to simply remove these rows.
- `txt` 代码块，源行 2823：In [73]: import pandas as pd / Auto = pd.read_csv('Auto.csv') / Auto
- `python` 代码块，源行 2831：In [74]: Auto = pd.read_csv('Auto.data', delim_whitespace=True)
- `txt` 代码块，源行 2839：In [75]: Auto['horsepower']

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Reading in a Data Set」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 59. Basics of Selecting Rows and Columns

- 原始层级：H1，源行：L2901
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We can use Auto.columns to check the variable names.
- Accessing the rows and columns of a data frame is similar, but not identical, to accessing the rows and columns of an array. Recall that the first argument to the [] method is always applied to the rows of the array. Si…
- Similarly, an array of Booleans can be used to subset the rows:

#### 公式与符号

- In [80]: Auto = Auto_new # overwrite the previous value
- Out[80]: Index(['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'name'], dtype='object')
- In [82]: idx_80 = Auto['year'] > 80
- Out[84]: Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ... 387, 388, 389, 390, 391, 392, 393, 394, 395, 396], dtype='int64', length=392)
- In [85]: Auto_re = Auto.set_index('name')

#### 例子 / 代码 / 图表

- `txt` 代码块，源行 2905：In [80]: Auto = Auto_new # overwrite the previous value / Auto.columns
- `javascript` 代码块，源行 2910：Out[80]: Index(['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration…
- `txt` 代码块，源行 2916：In [81]: Auto[:3]

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Basics of Selecting Rows and Columns」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 60. More on Selecting Rows and Columns

- 原始层级：H1，源行：L3053
- 推荐周次：第 5 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Suppose now that we want to create a data frame consisting of the weight and origin of the subset of cars with year greater than 80 — i.e. those built after 1980. To do this, we first create a Boolean array that indexes…
- To do this more concisely, we can use an anonymous function called a lambda:
- The lambda call creates a function that takes a single argument, here df, and returns df['year]>80. Since it is created inside the loc[] method for the dataframe Auto\_re, that dataframe will be the argument supplied. A…

#### 公式与符号

- In [92]: idx_80 = Auto_re['year'] > 80

#### 例子 / 代码 / 图表

- The lambda call creates a function that takes a single argument, here df, and returns df['year]>80. Since it is created inside the loc[] method for the dataframe Auto\_re, that dataframe will be the argument supplied. A…
- The symbol & computes an element-wise and operation. As another example, suppose that we want to retrieve all Ford and Datsun cars with displacement less than 300. We check whether each name entry contains either the st…
- `txt` 代码块，源行 3057：In [92]: idx_80 = Auto_re['year'] > 80 / Auto_re.loc[idx_80, ['weight', 'origin']]
- `txt` 代码块，源行 3066：In [93]: Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]
- `txt` 代码块，源行 3074：Auto_re.loc[lambda df: (df['year'] > 80) & (df['mpg'] > 30), ['weight', 'origin'] / ]

#### 备课摘取建议

- 若用于 PPT，可把本节作为「More on Selecting Rows and Columns」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 61. 2.3.8 For Loops

- 原始层级：H1，源行：L3100
- 推荐周次：第 3 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- A for loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code. For example, suppose we loop over elements of a list and compute their sum.
- The indented code beneath the line with the for statement is run for each value in the sequence specified in the for statement. The loop ends either when the cell ends or when code is indented at the same level as the o…
- Above, we summed over each combination of value and weight. We also took advantage of the increment notation in Python: the expression $a += b$ is equivalent to $a = a + b$ . Besides being a convenient notation, this ca…

#### 公式与符号

- total = 0
- total = 0
- total = 0

#### 例子 / 代码 / 图表

- A for loop is a standard tool in many languages that repeatedly evaluates some chunk of code while varying different values inside the code. For example, suppose we loop over elements of a list and compute their sum.
- `python` 代码块，源行 3108：total = 0 / for value in [3,2,19]: / total += value / print('Total is: {0}'.format(total))
- `python` 代码块，源行 3121：total = 0 / for value in [2,3,19]: / for weight in [3, 2, 1]: / total += value * weight
- `python` 代码块，源行 3141：total = 0 / for value, weight in zip([2,3,19], / [0.2,0.3,0.5]): / total += weight * value

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.8 For Loops」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 62. String Formatting

- 原始层级：H1，源行：L3151
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In the code chunk above we also printed a string displaying the total. However, the object total is an integer and not a string. Inserting the value of something into a string is a common task, made simple using some of…
- For example we may want to loop over the columns of a data frame and print the percent missing in each column. Let's create a data frame D with columns in which 20% of the entries are missing i.e. set to np.nan. We'll c…
- We see that the template.format() method expects two arguments $\{0\}$ and $\{1:.2\%$ , and the latter includes some formatting information. In particular, it specifies that the second argument should be expressed as a…

#### 公式与符号

- rng = np.random.default_rng(1)
- A = rng.standard_normal((127, 5))
- M = rng.choice([0, np.nan], p=[0.8,0.2], size=A.shape)
- D = pd.DataFrame(A, columns=['food',
- template = 'Column "{0}" has {1:.2%} missing values'

#### 例子 / 代码 / 图表

- For example we may want to loop over the columns of a data frame and print the percent missing in each column. Let's create a data frame D with columns in which 20% of the entries are missing i.e. set to np.nan. We'll c…
- `python` 代码块，源行 3161：rng = np.random.default_rng(1) / A = rng.standard_normal((127, 5)) / M = rng.choice([0, np.nan], p=[0.8,0.2], size=A.shape) / A += M
- `txt` 代码块，源行 3176：food bar pickle snack popcorn 0.345584 0.821618 0.330437 -1.303157 NaN 1 NaN -0.536953 0.…
- `python` 代码块，源行 3182：for col in D.columns: / template = 'Column "{0}" has {1:.2%} missing values' / print(template.format(col, / np.isnan(D[col]).mean()))

#### 备课摘取建议

- 若用于 PPT，可把本节作为「String Formatting」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 63. 2.3.9 Additional Graphical and Numerical Summaries

- 原始层级：H1，源行：L3201
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We can use the ax.plot() or ax.scatter() functions to display the quantitative variables. However, simply typing the variable names will produce an error message, because Python does not know to look in the Auto data se…
- We can address this by accessing the columns directly:
- Alternatively, we can use the plot() method with the call Auto.plot(). Using this method, the variables can be accessed by name. The plot methods of a data frame return a familiar object: an axes. We can use it to updat…

#### 公式与符号

- In [101]: fig, ax = subplots(figsize=(8, 8))
- In [102]: fig, ax = subplots(figsize=(8, 8))
- In [103]: ax = Auto.plot.scatter('horsepower', 'mpg');
- In [104]: fig = ax.figure
- In [105]: fig, axes = subplots(ncols=3, figsize=(15, 5))

#### 例子 / 代码 / 图表

- If we want to save the figure that contains a given axes, we can find the relevant figure by accessing the figure attribute:
- We can further instruct the data frame to plot to a particular axes object. In this case the corresponding plot() method will return the modified axes we passed in as an argument. Note that when we request a one-dimensi…
- `txt` 代码块，源行 3205：In [101]: fig, ax = subplots(figsize=(8, 8)) / ax.plot(horsepower, mpg, 'o');
- `txt` 代码块，源行 3210：NameError: name 'horsepower' is not defined
- `javascript` 代码块，源行 3216：In [102]: fig, ax = subplots(figsize=(8, 8)) / ax.plot(Auto['horsepower'], Auto['mpg'], 'o');

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.3.9 Additional Graphical and Numerical Summaries」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 64. 2.4 Exercises

- 原始层级：H1，源行：L3297
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2.4 Exercises」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 65. Conceptual

- 原始层级：H1，源行：L3299
- 推荐周次：第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.
- (a) The sample size $n$ is extremely large, and the number of predictors $p$ is small. (b) The number of predictors $p$ is extremely large, and the number of observations $n$ is small. (c) The relationship between the p…
- 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

#### 公式与符号

- (d) The variance of the error terms, i.e. $\sigma^2 = \mathrm{Var}(\epsilon)$ , is extremely high.
- (b) What is our prediction with $K = 1$ ? Why?
- (c) What is our prediction with $K = 3$ ? Why?

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Conceptual」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 66. Applied

- 原始层级：H1，源行：L3341
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 8. This exercise relates to the College data set, which can be found in the file College.csv on the book website. It contains a number of variables for 777 different universities and colleges in the US. The variables are
- - Private: Public/private indicator - Apps : Number of applications received - Accept : Number of applicants accepted • Enroll : Number of new students enrolled - Top10perc : New students from top $10\%$ of high school…
- Before reading the data into Python, it can be viewed in Excel or a text editor.

#### 公式与符号

- college2 = pd.read_csv('College.csv', index_col=0)
- college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
- college3 = college3.set_index('College')
- college = college3
- college['Elite'] = pd.cut(college['Top10perc'], [0, 0.5, 1], labels=['No', 'Yes'])

#### 例子 / 代码 / 图表

- 8. This exercise relates to the College data set, which can be found in the file College.csv on the book website. It contains a number of variables for 777 different universities and colleges in the US. The variables are
- 9. This exercise involves the Auto data set studied in the lab. Make sure that the missing values have been removed from the data.
- 10. This exercise involves the Boston housing data set.
- `python` 代码块，源行 3369：college2 = pd.read_csv('College.csv', index_col=0) / college3 = college.rename({'Unnamed: 0': 'College'}, axis=1) / college3 = college3.set_index('College')
- `txt` 代码块，源行 3379：college = college3
- `python` 代码块，源行 3388：college['Elite'] = pd.cut(college['Top10perc'], [0, 0.5, 1], labels=['No', 'Yes'])

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Applied」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 67. 3

- 原始层级：H1，源行：L3423
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 68. Linear Regression

- 原始层级：H1，源行：L3425
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Recall the Advertising data from Chapter 2. Figure 2.1 displays sales (in thousands of units) for a particular product as a function of advertising budgets (in thousands of dollars) for TV, radio, and newspaper media. S…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Recall the Advertising data from Chapter 2. Figure 2.1 displays sales (in thousands of units) for a particular product as a function of advertising budgets (in thousands of dollars) for TV, radio, and newspaper media. S…
- 图片引用：`images/5d1546f1e2492411ba7739f8974699115687229207bb2aeffafed1a664fbe834.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Linear Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 69. 1. Is there a relationship between advertising budget and sales?

- 原始层级：H1，源行：L3433
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Our first goal should be to determine whether the data provide evidence of an association between advertising expenditure and sales. If the evidence is weak, then one might argue that no money should be spent on adverti…
- 2. How strong is the relationship between advertising budget and sales? Assuming that there is a relationship between advertising and sales, we would like to know the strength of this relationship. Does knowledge of the…
- Are all three media—TV, radio, and newspaper—associated with sales, or are just one or two of the media associated? To answer this question, we must find a way to separate out the individual contribution of each medium…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1. Is there a relationship between advertising budget and sales?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 70. 3.1 Simple Linear Regression

- 原始层级：H1，源行：L3462
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Simple linear regression lives up to its name: it is a very straightforward approach for predicting a quantitative response Y on the basis of a single predictor variable X. It assumes that there is approximately a linea…
- $$ Y \approx \beta_ {0} + \beta_ {1} X. \tag {3.1} $$
- You might read “ $\approx$ ” as “is approximately modeled as”. We will sometimes describe (3.1) by saying that we are regressing Y on X (or Y onto X).

#### 公式与符号

- $$
- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- For example, X may represent TV advertising and Y may represent sales. Then we can regress sales onto TV by fitting the model

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1 Simple Linear Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 71. 3.1.1 Estimating the Coefficients

- 原始层级：H1，源行：L3493
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In practice, $\beta_{0}$ and $\beta_{1}$ are unknown. So before we can use (3.1) to make predictions, we must use data to estimate the coefficients. Let
- $$ (x _ {1}, y _ {1}), (x _ {2}, y _ {2}), \dots , (x _ {n}, y _ {n}) $$
- Let $\hat{y}_{i}=\hat{\beta}_{0}+\hat{\beta}_{1}x_{i}$ be the prediction for Y based on the ith value of X. Then $e_{i}=y_{i}-\hat{y}_{i}$ represents the ith residual—this is the difference between the ith observed resp…

#### 公式与符号

- $$
- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 3.1. For the Advertising data, the least squares fit for the regression of sales onto TV is shown. The fit is found by minimizing the residual sum of squares. Each grey line segment represents a residual. In this…
- Figure 3.1 displays the simple linear regression fit to the Advertising data, where $\hat{\beta}_0 = 7.03$ and $\hat{\beta}_1 = 0.0475$ . In other words, according to this approximation, an additional \$1,000 spent on T…
- 图片引用：`images/4e4298a3f09bef98f40e689f3d05d691ec741afb1f7395f2ca67e629f0ef0cbd.jpg`
- 表格行：| TV | Sales |
- 表格行：| --- | ----- |
- 表格行：| 0 | 2 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1.1 Estimating the Coefficients」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 72. 3.1.2 Assessing the Accuracy of the Coefficient Estimates

- 原始层级：H1，源行：L3577
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Recall from (2.1) that we assume that the true relationship between $X$ and $Y$ takes the form $Y = f(X) + \epsilon$ for some unknown function $f$ , where $\epsilon$ is a mean-zero random error term. If $f$ is to be app…
- $$ Y = \beta_ {0} + \beta_ {1} X + \epsilon . \tag {3.5} $$
- Here $\beta_{0}$ is the intercept term—that is, the expected value of Y when X = 0, and $\beta_{1}$ is the slope—the average increase in Y associated with a one-unit increase in X. The error term is a catch-all for what…

#### 公式与符号

- $$
- Y = \beta_ {0} + \beta_ {1} X + \epsilon . \tag {3.5}
- $$
- $$
- Y = 2 + 3 X + \epsilon , \tag {3.6}

#### 例子 / 代码 / 图表

- FIGURE 3.2. Contour and three-dimensional plots of the RSS on the Advertising data, using sales as the response and TV as the predictor. The red dots correspond to the least squares estimates $\hat{\beta}_{0}$ and $\hat…
- The model given by (3.5) defines the population regression line, which is the best linear approximation to the true relationship between $X$ and $Y$ . The least squares regression coefficient estimates (3.4) characteriz…
- At first glance, the difference between the population regression line and the least squares line may seem subtle and confusing. We only have one data set, and so what does it mean that two different lines describe the…
- 图片引用：`images/70e09d9bcf0d6bbdd724a7981d20b904abdcdb77b51a2fe937977578957ea62f.jpg`
- 图片引用：`images/fe12a0f61903793cf928cb7e5c0c138a40f676332415a477c3abeaed0ef1da5d.jpg`
- 图片引用：`images/4bdaf8d37406fd9bd47ecd0689bdba1ce993f13baae1e0d15049e7825a805287.jpg`
- 表格行：| β₀ | β₁ |
- 表格行：| ---- | ---- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1.2 Assessing the Accuracy of the Coefficient Estimates」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 73. 3.1.3 Assessing the Accuracy of the Model

- 原始层级：H1，源行：L3724
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Once we have rejected the null hypothesis $(3.12)$ in favor of the alternative hypothesis $(3.13)$ , it is natural to want to quantify the extent to which the model fits the data. The quality of a linear regression fit…
- Quantity Value Residual standard error 3.26 $R^{2}$ 0.612 F-statistic 312.1
- TABLE 3.2. For the Advertising data, more information about the least squares model for the regression of number of units sold on TV advertising budget.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.1.3 Assessing the Accuracy of the Model」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 74. Residual Standard Error

- 原始层级：H1，源行：L3736
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Recall from the model (3.5) that associated with each observation is an error term $\epsilon$ . Due to the presence of these error terms, even if we knew the true regression line (i.e. even if $\beta_{0}$ and $\beta_{1}…
- $$ \mathrm{RSE} = \sqrt {\frac {1}{n - 2} \mathrm{RSS}} = \sqrt {\frac {1}{n - 2} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}}. \tag {3.15} $$
- Note that RSS was defined in Section 3.1.1, and is given by the formula

#### 公式与符号

- $$
- \mathrm{RSE} = \sqrt {\frac {1}{n - 2} \mathrm{RSS}} = \sqrt {\frac {1}{n - 2} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}}. \tag {3.15}
- $$
- $$
- \mathrm{RSS} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}. \tag {3.16}

#### 例子 / 代码 / 图表

- In the case of the advertising data, we see from the linear regression output in Table 3.2 that the RSE is 3.26. In other words, actual sales in each market deviate from the true regression line by approximately 3,260 u…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Residual Standard Error」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 75. $R^2$ Statistic

- 原始层级：H1，源行：L3754
- 推荐周次：第 4 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The RSE provides an absolute measure of lack of fit of the model (3.5) to the data. But since it is measured in the units of $Y$ , it is not always clear what constitutes a good RSE. The $R^{2}$ statistic provides an al…
- To calculate $R^{2}$ , we use the formula
- $$ R ^ {2} = \frac {\mathrm{TSS-RSS}}{\mathrm{TSS}} = 1 - \frac {\mathrm{RSS}}{\mathrm{TSS}} \tag {3.17} $$

#### 公式与符号

- $$
- $$
- $$
- \operatorname{Cor} (X, Y) = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{x}}}) (y _ {i} - \overline {{{y}}})}{\sqrt {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{{x}}}) ^ {2}} \sqrt {\sum_ {i = 1} ^ {n} (y _ {i} - \…
- $$

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「$R^2$ Statistic」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 76. 3.2 Multiple Linear Regression

- 原始层级：H1，源行：L3791
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the Advertising data, we h…
- One option is to run three separate simple linear regressions, each of which uses a different advertising medium as a predictor. For instance, we can fit a simple linear regression to predict sales on the basis of the a…
- However, the approach of fitting a separate simple linear regression model for each predictor is not entirely satisfactory. First of all, it is unclear how to make a single prediction of sales given the three advertisin…

#### 公式与符号

- $$
- Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \dots + \beta_ {p} X _ {p} + \epsilon , \tag {3.19}
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- Simple linear regression is a useful approach for predicting a response on the basis of a single predictor variable. However, in practice we often have more than one predictor. For example, in the Advertising data, we h…
- where $X_{j}$ represents the jth predictor and $\beta_{j}$ quantifies the association between that variable and the response. We interpret $\beta_{j}$ as the average effect on Y of a one unit increase in $X_{j}$ , holdi…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.2 Multiple Linear Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 77. 3.2.1 Estimating the Regression Coefficients

- 原始层级：H1，源行：L3811
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- As was the case in the simple linear regression setting, the regression coefficients $\beta_{0},\beta_{1},\ldots,\beta_{p}$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_{0},\hat{\beta}_{1},…
- $$ \hat {y} = \hat {\beta} _ {0} + \hat {\beta} _ {1} x _ {1} + \hat {\beta} _ {2} x _ {2} + \dots + \hat {\beta} _ {p} x _ {p}. \tag {3.21} $$
- The parameters are estimated using the same least squares approach that we saw in the context of simple linear regression. We choose $\beta_{0}, \beta_{1}, \ldots, \beta_{p}$ to minimize the sum of squared residuals

#### 公式与符号

- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- As was the case in the simple linear regression setting, the regression coefficients $\beta_{0},\beta_{1},\ldots,\beta_{p}$ in (3.19) are unknown, and must be estimated. Given estimates $\hat{\beta}_{0},\hat{\beta}_{1},…
- The values $\hat{\beta}_{0},\hat{\beta}_{1},\ldots,\hat{\beta}_{p}$ that minimize (3.22) are the multiple least squares regression coefficient estimates. Unlike the simple linear regression estimates given in (3.4), the…
- FIGURE 3.4. In a three-dimensional setting, with two predictors and one response, the least squares regression line becomes a plane. The plane is chosen to minimize the sum of the squared vertical distances between each…
- 图片引用：`images/61d6d80ad89f347d9d82294135de5d79cafcd02f9deb2305f9f02983316f4a22.jpg`
- 表格行：| X1 | Y |
- 表格行：|----|----|
- 表格行：| 0 | 0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.2.1 Estimating the Regression Coefficients」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 78. 3.2.2 Some Important Questions

- 原始层级：H1，源行：L4053
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- When we perform multiple linear regression, we usually are interested in answering a few important questions.
- 1. Is at least one of the predictors $X_{1}, X_{2}, \ldots, X_{p}$ useful in predicting the response? 2. Do all the predictors help to explain Y, or is only a subset of the predictors useful? 3. How well does the model…
- We now address each of these questions in turn.

#### 公式与符号

- $$
- H _ {0}: \beta_ {1} = \beta_ {2} = \dots = \beta_ {p} = 0
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- where for convenience we have put the variables chosen for omission at the end of the list. In this case we fit a second model that uses all the variables except those last q. Suppose that the residual sum of squares fo…
- The approach of using an F-statistic to test for any association between the predictors and the response works when p is relatively small, and certainly small compared to n. However, sometimes we have a very large numbe…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.2.2 Some Important Questions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 79. Two: Deciding on Important Variables

- 原始层级：H1，源行：L4129
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- As discussed in the previous section, the first step in a multiple regression analysis is to compute the F-statistic and to examine the associated p-value. If we conclude on the basis of that p-value that at least one o…
- It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors. The task of determining which predictors ar…
- Ideally, we would like to perform variable selection by trying out a lot of different models, each containing a different subset of the predictors. For instance, if p = 2, then we can consider four models: (1) a model c…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors. The task of determining which predictors ar…
- \- Mixed selection. This is a combination of forward and backward selection. We start with no variables in the model, and as with forward selection, we add the variable that provides the best fit. We continue to add var…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Two: Deciding on Important Variables」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 80. Three: Model Fit

- 原始层级：H1，源行：L4163
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Two of the most common numerical measures of model fit are the RSE and $R^{2}$ , the fraction of variance explained. These quantities are computed and interpreted in the same fashion as for simple linear regression.
- Recall that in simple regression, $R^{2}$ is the square of the correlation of the response and the variable. In multiple linear regression, it turns out that it equals $\operatorname{Cor}(Y,\hat{Y})^{2}$ , the square of…
- By contrast, the model containing only TV as a predictor had an $R^{2}$ of 0.61 (Table 3.2). Adding radio to the model leads to a substantial improvement in $R^{2}$ . This implies that a model that uses TV and radio exp…

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 3.5. For the Advertising data, a linear regression fit to sales using TV and radio as predictors. From the pattern of the residuals, we can see that there is a pronounced non-linear relationship in the data. The…
- 图片引用：`images/b9ebb9165a2694099727adf620d34fb22c4fe1cfe91e1a6704b46207be7f9f93.jpg`
- 表格行：| Radio | Sales |
- 表格行：|-------|-------|
- 表格行：| 0 | 0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Three: Model Fit」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 81. Four: Predictions

- 原始层级：H1，源行：L4217
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Once we have fit the multiple regression model, it is straightforward to apply $(3.21)$ in order to predict the response Y on the basis of a set of values for the predictors $X_{1}, X_{2}, \ldots, X_{p}$ . However, ther…
- 1. The coefficient estimates $\hat{\beta}_0, \hat{\beta}_1, \ldots, \hat{\beta}_p$ are estimates for $\beta_0, \beta_1, \ldots, \beta_p$ . That is, the least squares plane
- $$ \hat {Y} = \hat {\beta} _ {0} + \hat {\beta} _ {1} X _ {1} + \dots + \hat {\beta} _ {p} X _ {p} $$

#### 公式与符号

- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Four: Predictions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 82. 3.3 Other Considerations in the Regression Model

- 原始层级：H1，源行：L4244
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.3 Other Considerations in the Regression Model」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 83. 3.3.1 Qualitative Predictors

- 原始层级：H1，源行：L4246
- 推荐周次：第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In our discussion so far, we have assumed that all variables in our linear regression model are quantitative. But in practice, this is not necessarily the case; often some predictors are qualitative.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- In our discussion so far, we have assumed that all variables in our linear regression model are quantitative. But in practice, this is not necessarily the case; often some predictors are qualitative.

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.3.1 Qualitative Predictors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 84. Predictors with Only Two Levels

- 原始层级：H1，源行：L4252
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Suppose that we wish to investigate differences in credit card balance between those who own a house and those who don't, ignoring the other variables for the moment. If a qualitative predictor (also known as a factor)…
- $$ x _ {i} = \left\{ \begin{array}{l l} 1 & \text { if } i \text {th person owns a house } \\ 0 & \text { if } i \text {th person does not own a house, } \end{array} \right. \tag {3.26} $$
- and use this variable as a predictor in the regression equation. This results in the model

#### 公式与符号

- $$
- x _ {i} = \left\{ \begin{array}{l l} 1 & \text { if } i \text {th person owns a house } \\ 0 & \text { if } i \text {th person does not own a house, } \end{array} \right. \tag {3.26}
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- Suppose that we wish to investigate differences in credit card balance between those who own a house and those who don't, ignoring the other variables for the moment. If a qualitative predictor (also known as a factor)…
- FIGURE 3.6. The Credit data set contains information about balance, age, cards, education, income, limit, and rating for a number of potential customers.
- Now $\beta_{0}$ can be interpreted as the overall average credit card balance (ignoring the house ownership effect), and $\beta_{1}$ is the amount by which house owners and non-owners have credit card balances that are…
- 图片引用：`images/1335377c0bae432551d6c03c6f01d0e6220c997c7b62a804ed55062bebbe55a3.jpg`
- 表格行：| Variable | Value |
- 表格行：|------------|-------|
- 表格行：| Balance | 20 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Predictors with Only Two Levels」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 85. Qualitative Predictors with More than Two Levels

- 原始层级：H1，源行：L4575
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values. In this situation, we can create additional dummy variables. For example, for the region variable we c…
- $$ x _ {i 1} = \left\{ \begin{array}{l l} 1 & \text { if } i \text {th person is from the South } \\ 0 & \text { if } i \text {th person is not from the South, } \end{array} \right. \tag {3.28} $$
- $$ x _ {i 2} = \left\{ \begin{array}{l l} 1 & \text { if } i \text {th person is from the West } \\ 0 & \text { if } i \text {th person is not from the West. } \end{array} \right. \tag {3.29} $$

#### 公式与符号

- $$
- x _ {i 1} = \left\{ \begin{array}{l l} 1 & \text { if } i \text {th person is from the South } \\ 0 & \text { if } i \text {th person is not from the South, } \end{array} \right. \tag {3.28}
- $$
- $$
- x _ {i 2} = \left\{ \begin{array}{l l} 1 & \text { if } i \text {th person is from the West } \\ 0 & \text { if } i \text {th person is not from the West. } \end{array} \right. \tag {3.29}

#### 例子 / 代码 / 图表

- When a qualitative predictor has more than two levels, a single dummy variable cannot represent all possible values. In this situation, we can create additional dummy variables. For example, for the region variable we c…
- Now $\beta_{0}$ can be interpreted as the average credit card balance for individuals from the East, $\beta_{1}$ can be interpreted as the difference in the average balance between people from the South versus the East,…
- Using this dummy variable approach presents no difficulties when incorporating both quantitative and qualitative predictors. For example, to regress balance on both a quantitative variable such as income and a qualitati…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Qualitative Predictors with More than Two Levels」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 86. 3.3.2 Extensions of the Linear Model

- 原始层级：H1，源行：L4611
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The standard linear regression model (3.19) provides interpretable results and works quite well on many real-world problems. However, it makes several highly restrictive assumptions that are often violated in practice.…
- assumptions. Here, we briefly examine some common classical approaches for extending the linear model.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.3.2 Extensions of the Linear Model」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 87. Removing the Additive Assumption

- 原始层级：H1，源行：L4620
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In our previous analysis of the Advertising data, we concluded that both TV and radio seem to be associated with sales. The linear models that formed the basis for this conclusion assumed that the effect on sales of inc…
- Consider the standard linear regression model with two variables,
- $$ Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \epsilon . $$

#### 公式与符号

- $$
- Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \epsilon .
- $$
- $$
- Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \beta_ {3} X _ {1} X _ {2} + \epsilon . \tag {3.31}

#### 例子 / 代码 / 图表

- In our previous analysis of the Advertising data, we concluded that both TV and radio seem to be associated with sales. The linear models that formed the basis for this conclusion assumed that the effect on sales of inc…
- For example, suppose that we are interested in studying the productivity of a factory. We wish to predict the number of units produced on the basis of the number of production lines and the total number of workers. It s…
- We now return to the Advertising example. A linear model that uses radio, TV, and an interaction between the two to predict sales takes the form
- 图片引用：`images/f4a8c7defebd8120b06acffa61c674d00803159f848f2ae705e809a0ee118802.jpg`
- 图片引用：`images/6ef11d9e49aed9c03f9632f541d97fd283edde3a36d2046b20365575ab5067cf.jpg`
- 表格行：| Income | Balance (Red Line) | Balance (Black Line) |
- 表格行：| ------ | ------------------ | -------------------- |
- 表格行：| 0 | 600 | 200 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Removing the Additive Assumption」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 88. Non-linear Relationships

- 原始层级：H1，源行：L4714
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- As discussed previously, the linear regression model $(3.19)$ assumes a linear relationship between the response and predictors. But in some cases, the true relationship between the response and the predictors may be no…
- Consider Figure 3.8, in which the mpg (gas mileage in miles per gallon) versus horsepower is shown for a number of cars in the Auto data set. The orange line represents the linear regression fit. There is a pronounced r…
- $$ \mathrm{mpg} = \beta_ {0} + \beta_ {1} \times \text { horsepower } + \beta_ {2} \times \text { horsepower } ^ {2} + \epsilon \tag {3.36} $$

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- Consider Figure 3.8, in which the mpg (gas mileage in miles per gallon) versus horsepower is shown for a number of cars in the Auto data set. The orange line represents the linear regression fit. There is a pronounced r…
- may provide a better fit. Equation 3.36 involves predicting mpg using a non-linear function of horsepower. But it is still a linear model! That is, (3.36) is simply a multiple linear regression model with $X_{1} = \text…
- FIGURE 3.8. The Auto data set. For a number of cars, mpg and horsepower are shown. The linear regression fit is shown in orange. The linear regression fit for a model that includes horsepower $^{2}$ is shown as a blue c…
- 图片引用：`images/ed77e355ed46ab6948fcc512a0c7edde88baed8f0d55ae36d64d273b03c7167e.jpg`
- 表格行：| Horsepower | Miles per gallon | Series |
- 表格行：| ---------- | ---------------- | ---------- |
- 表格行：| 50 | 40 | Linear |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Non-linear Relationships」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 89. 3.3.3 Potential Problems

- 原始层级：H1，源行：L4760
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- When we fit a linear regression model to a particular data set, many problems may occur. Most common among these are the following:
- 2. Correlation of error terms. 3. Non-constant variance of error terms. 4. Outliers. 5. High-leverage points. 6. Collinearity.
- 1. Non-linearity of the response-predictor relationships.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.3.3 Potential Problems」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 90. 1. Non-linearity of the Data

- 原始层级：H1，源行：L4774
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- FIGURE 3.9. Plots of residuals versus predicted (or fitted) values for the Auto data set. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. Left: A linear regre…
- The linear regression model assumes that there is a straight-line relationship between the predictors and the response. If the true relationship is far from linear, then virtually all of the conclusions that we draw fro…
- Residual plots are a useful graphical tool for identifying non-linearity. Given a simple linear regression model, we can plot the residuals, $e_{i} =$

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- FIGURE 3.9. Plots of residuals versus predicted (or fitted) values for the Auto data set. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. Left: A linear regre…
- $y_{i}-\hat{y}_{i}$ , versus the predictor $x_{i}$ . In the case of a multiple regression model, since there are multiple predictors, we instead plot the residuals versus the predicted (or fitted) values $\hat{y}_{i}$ .…
- The left panel of Figure 3.9 displays a residual plot from the linear regression of mpg onto horsepower on the Auto data set that was illustrated in Figure 3.8. The red line is a smooth fit to the residuals, which is di…
- 图片引用：`images/9e2983164d909474e7e5002b8440cb485b27bcee84799b5c1a58454ef9a44c7e.jpg`
- 图片引用：`images/5dc34758fe7c23d4006a9287f988e87c05bbb59bb217510933856f8ae1fd6af5.jpg`
- 表格行：| Fitted values | Residuals |
- 表格行：| ------------- | --------- |
- 表格行：| 334 | 15 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「1. Non-linearity of the Data」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 91. 2. Correlation of Error Terms

- 原始层级：H1，源行：L4816
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs. If we ignored this, our standard error calculations would be as if we had a sample of size 2n,…
- FIGURE 3.10. Plots of residuals from simulated time series data sets generated with differing levels of correlation $\rho$ between error terms for adjacent time points.
- Many methods have been developed to properly take account of correlations in the error terms in time series data. Correlation among the error terms can also occur outside of time series data. For instance, consider a st…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- As an extreme example, suppose we accidentally doubled our data, leading to observations and error terms identical in pairs. If we ignored this, our standard error calculations would be as if we had a sample of size 2n,…
- FIGURE 3.10. Plots of residuals from simulated time series data sets generated with differing levels of correlation $\rho$ between error terms for adjacent time points.
- FIGURE 3.11. Residual plots. In each plot, the red line is a smooth fit to the residuals, intended to make it easier to identify a trend. The blue lines track the outer quantiles of the residuals, and emphasize patterns…
- 图片引用：`images/2f1d318321b150daab4bd90216540835b54b1a38b1cde893f75477e69cfe1954.jpg`
- 图片引用：`images/7e79d43cbdafcb37795bd3ad452c5d5da300aedcbea3a6f2ae4295a8baef99a4.jpg`
- 图片引用：`images/9dd055cce57269d7133d0f20d8abfb552a415de56f57e01af89121aeb5f500d1.jpg`
- 表格行：| Fitted values | Residuals |
- 表格行：| ------------- | --------- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「2. Correlation of Error Terms」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 92. 3. Non-constant Variance of Error Terms

- 原始层级：H1，源行：L4858
- 推荐周次：第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Another important assumption of the linear regression model is that the error terms have a constant variance, $\operatorname{Var}(\epsilon_{i}) = \sigma^{2}$ . The standard errors, confidence intervals, and hypothesis t…
- Sometimes we have a good idea of the variance of each response. For example, the ith response could be an average of $n_{i}$ raw observations. If each of these raw observations is uncorrelated with variance $\sigma^{2}$…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Sometimes we have a good idea of the variance of each response. For example, the ith response could be an average of $n_{i}$ raw observations. If each of these raw observations is uncorrelated with variance $\sigma^{2}$…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3. Non-constant Variance of Error Terms」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 93. 4. Outliers

- 原始层级：H1，源行：L4871
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- An outlier is a point for which $y_{i}$ is far from the value predicted by the
- FIGURE 3.12. Left: The least squares regression line is shown in red, and the regression line after removing the outlier is shown in blue. Center: The residual plot clearly identifies the outlier. Right: The outlier has…
- model. Outliers can arise for a variety of reasons, such as incorrect recording of an observation during data collection.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- FIGURE 3.12. Left: The least squares regression line is shown in red, and the regression line after removing the outlier is shown in blue. Center: The residual plot clearly identifies the outlier. Right: The outlier has…
- Residual plots can be used to identify outliers. In this example, the outlier is clearly visible in the residual plot illustrated in the center panel of Figure 3.12. But in practice, it can be difficult to decide how la…
- 图片引用：`images/33f2173417e3f9384ad2f5f3ced0024059368a29f0a41fc66f9b9e932954f0f2.jpg`
- 图片引用：`images/7374cc5b77cf47bc03f400bca19e24318c4d8d34dc3b700ea9857f17c4c8ec49.jpg`
- 图片引用：`images/9c3d371d883ff2b67255eae1a97de29d0c7b3e867e2ba000c836322e83898eac.jpg`
- 表格行：| X | Y |
- 表格行：| ---- | ---- |
- 表格行：| -2 | -4 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4. Outliers」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 94. 5. High Leverage Points

- 原始层级：H1，源行：L4929
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- FIGURE 3.13. Left: Observation 41 is a high leverage point, while 20 is not. The red line is the fit to all the data, and the blue line is the fit with observation 41 removed. Center: The red observation is not unusual…
- In order to quantify an observation's leverage, we compute the leverage statistic. A large value of this statistic indicates an observation with high leverage. For a simple linear regression,
- $$ h _ {i} = \frac {1}{n} + \frac {(x _ {i} - \bar {x}) ^ {2}}{\sum_ {i ^ {\prime} = 1} ^ {n} (x _ {i ^ {\prime}} - \bar {x}) ^ {2}}. \tag {3.37} $$

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 3.13. Left: Observation 41 is a high leverage point, while 20 is not. The red line is the fit to all the data, and the blue line is the fit with observation 41 removed. Center: The red observation is not unusual…
- FIGURE 3.14. Scatterplots of the observations from the Credit data set. Left: A plot of age versus limit. These two variables are not collinear. Right: A plot of rating versus limit. There is high collinearity.
- It is clear from this equation that $h_{i}$ increases with the distance of $x_{i}$ from $\bar{x}$ . There is a simple extension of $h_{i}$ to the case of multiple predictors, though we do not provide the formula here. T…
- 图片引用：`images/0a69819d985b2412ad7a7bb05360ef3aed42cb1a83939790c2dfe2e9dc464120.jpg`
- 图片引用：`images/5a7d28b1b89e34c7e689b667a2dbf0623fe81dbc09485e79a9331135c51fd39b.jpg`
- 图片引用：`images/083ebdc348af76de2245c87a80e2930421e8c9c6b1f23fee0cfa303ba66d9d16.jpg`
- 表格行：| X | Y |
- 表格行：| ---- | ---- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「5. High Leverage Points」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 95. 6. Collinearity

- 原始层级：H1，源行：L5049
- 推荐周次：第 4 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- FIGURE 3.15. Contour plots for the RSS values as a function of the parameters $\beta$ for various regressions involving the Credit data set. In each plot, the black dots represent the coefficient values corresponding to…
- Since collinearity reduces the accuracy of the estimates of the regression coefficients, it causes the standard error for $\hat{\beta}_{j}$ to grow. Recall that the t-statistic for each predictor is calculated by dividi…
- Coefficient Std. error t-statistic p-value Model 1 Intercept -173.411 43.828 -3.957 &lt; 0.0001 age -2.292 0.672 -3.407 0.0007 limit 0.173 0.005 34.496 &lt; 0.0001 Model 2 Intercept -377.537 45.254 -8.343 &lt; 0.0001 ra…

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 3.15. Contour plots for the RSS values as a function of the parameters $\beta$ for various regressions involving the Credit data set. In each plot, the black dots represent the coefficient values corresponding to…
- 图片引用：`images/5df6f09f853d8e38e1821e0244fa9c3f97a48123dfd1e22dde699e23f6b66597.jpg`
- 图片引用：`images/84c3f9fefb2eb218b5519ccd4774074b9d1d24dc62de47cad04e5d5a42ac9f8c.jpg`
- 表格行：| βLimit | βAge |
- 表格行：|--------|-------|
- 表格行：| 0.17 | -2.5 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「6. Collinearity」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 96. 3.4 The Marketing Plan

- 原始层级：H1，源行：L5118
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- We now briefly return to the seven questions about the Advertising data that we set out to answer at the beginning of this chapter.
- 1. Is there a relationship between sales and advertising budget?
- This question can be answered by fitting a multiple regression model of sales onto TV, radio, and newspaper, as in (3.20), and testing the hypothesis $H_{0} : \beta_{TV} = \beta_{radio} = \beta_{newspaper} = 0$ . In Sec…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- This question can be answered by fitting a multiple regression model of sales onto TV, radio, and newspaper, as in (3.20), and testing the hypothesis $H_{0} : \beta_{TV} = \beta_{radio} = \beta_{newspaper} = 0$ . In Sec…
- In Section 3.3.3, we saw that residual plots can be used in order to identify non-linearity. If the relationships are linear, then the residual plots should display no pattern. In the case of the Advertising data, we ob…
- The standard linear regression model assumes an additive relationship between the predictors and the response. An additive model is easy to interpret because the association between each predictor and the response is un…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.4 The Marketing Plan」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 97. 3.5 Comparison of Linear Regression with $K$ -Nearest Neighbors

- 原始层级：H1，源行：L5154
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- In contrast, non-parametric methods do not explicitly assume a parametric form for $f(X)$ , and thereby provide an alternative and more flexible approach for performing regression. We discuss various non-parametric meth…
- $$ \hat {f} (x _ {0}) = \frac {1}{K} \sum_ {x _ {i} \in \mathcal {N} _ {0}} y _ {i}. $$
- K-nearest neighbors regression

#### 公式与符号

- $$
- $$
- FIGURE 3.16. Plots of $\hat{f}(X)$ using KNN regression on a two-dimensional data set with 64 observations (orange dots). Left: K = 1 results in a rough step function fit. Right: K = 9 produces a much smoother fit.

#### 例子 / 代码 / 图表

- FIGURE 3.16. Plots of $\hat{f}(X)$ using KNN regression on a two-dimensional data set with 64 observations (orange dots). Left: K = 1 results in a rough step function fit. Right: K = 9 produces a much smoother fit.
- In practice, the true relationship between X and Y is rarely exactly linear. Figure 3.19 examines the relative performances of least squares regression and KNN under increasing levels of non-linearity in the relationshi…
- FIGURE 3.17. Plots of $\hat{f}(X)$ using KNN regression on a one-dimensional data set with 50 observations. The true relationship is given by the black solid line. Left: The blue curve corresponds to K = 1 and interpola…
- 图片引用：`images/8c39a71be45c935390161c3493175d865557d90350fbc2f0b8308d1a99d71fe1.jpg`
- 图片引用：`images/2e81390b95ecc6de6317ab29f7cb2189a9bc50d28e976ad0199764529703f6bc.jpg`
- 图片引用：`images/a6e67d78debd9be532b36229a667d5631a820cb175a896d93d92f2fd1e60b4ce.jpg`
- 表格行：| x1 | y1 | x2 |
- 表格行：|----|----|----|

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.5 Comparison of Linear Regression with $K$ -Nearest Neighbors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 98. 3.6 Lab: Linear Regression

- 原始层级：H1，源行：L5351
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6 Lab: Linear Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 99. 3.6.1 Importing packages

- 原始层级：H1，源行：L5353
- 推荐周次：第 3 周, 第 5 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We import our standard libraries at this top level.

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- `python` 代码块，源行 5358：import numpy as np / import pandas as pd / from matplotlib.pyplot import subplots

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.1 Importing packages」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 100. New imports

- 原始层级：H1，源行：L5364
- 推荐周次：第 3 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Throughout this lab we will introduce new functions and libraries. However, we will import them here to emphasize these are the new code objects in this lab. Keeping imports near the top of a notebook makes the code mor…
- We will provide relevant details about the functions below as they are needed.
- Besides importing whole modules, it is also possible to import only a few items from a given module. This will help keep the namespace clean. We will use a few specific objects from the statsmodels package which we impo…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- Throughout this lab we will introduce new functions and libraries. However, we will import them here to emphasize these are the new code objects in this lab. Keeping imports near the top of a notebook makes the code mor…
- `python` 代码块，源行 5369：import statsmodels.api as sm
- `python` 代码块，源行 5381：from statsmodels.stats.outliers_influence \ / import variance_inflation_factor as VIF / from statsmodels.stats.anova import anova_lm
- `python` 代码块，源行 5392：from ISLP import load_data / from ISLP.models import (ModelSpec as MS, summarize, poly)

#### 备课摘取建议

- 若用于 PPT，可把本节作为「New imports」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 101. Inspecting Objects and Namespaces

- 原始层级：H1，源行：L5397
- 推荐周次：第 3 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- The function dir() provides a list of objects in a namespace.
- This shows you everything that Python can find at the top level. There are certain objects like \_\_builtins\_\_ that contain references to built-in functions like print().
- Every python object has its own notion of namespace, also accessible with dir(). This will include both the attributes of the object as well as any methods associated with it. For instance, we see 'sum' in the listing f…

#### 公式与符号

- In [6]: A = np.array([3,5,11])

#### 例子 / 代码 / 图表

- This indicates that the object A.sum exists. In this case it is a method that can be used to compute the sum of the array A as can be seen by typing A.sum?.
- `txt` 代码块，源行 5404：dir()
- `python` 代码块，源行 5408：Out[5]: ['In', / 'MS', / '_, / '_,
- `txt` 代码块，源行 5420：'poly', / 'quit', / 'sm', / 'summarize']

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Inspecting Objects and Namespaces」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 102. 3.6.2 Simple Linear Regression

- 原始层级：H1，源行：L5454
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In this section we will construct model matrices (also called design matrices) using the ModelSpec() transform from ISLP.models.
- We will use the Boston housing data set, which is contained in the ISLP package. The Boston dataset records medv (median house value) for 506 neighborhoods around Boston. We will build a regression model to predict medv…
- We have included a simple loading function load\_data() in the ISLP package:

#### 公式与符号

- In [8]: Boston = load_data("Boston")
- Out[8]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat', 'medv'], dtype='object')
- In [9]: X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]), 'lstat': Boston['lstat']} X[:4]
- In [10]: y = Boston['medv']
- model = sm.OLS(y, X)

#### 例子 / 代码 / 图表

- `python` 代码块，源行 5464：In [8]: Boston = load_data("Boston") / Boston.columns
- `javascript` 代码块，源行 5469：Out[8]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'p…
- `python` 代码块，源行 5477：In [9]: X = pd.DataFrame({'intercept': np.ones(Boston.shape[0]), 'lstat': Boston['lstat']…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.2 Simple Linear Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 103. Using Transformations: Fit and Transform

- 原始层级：H1，源行：L5515
- 推荐周次：第 3 周, 第 4 周, 第 5 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Our model above has a single predictor, and constructing x was straightforward. In practice we often fit models with more than one predictor, typically selected from an array or data frame. We may wish to introduce tran…
- We provide a general approach for specifying models and constructing the model matrix through the transform ModelSpec() in the ISLP library. ModelSpec() (renamed MS() in the preamble) creates a transform object, and the…
- We first describe this process for our simple regression model using a single predictor lstat in the Boston data frame, but will use it repeatedly in more complex tasks in this and other labs in this book. In our case t…

#### 公式与符号

- In [12]: design = MS(['lstat'])
- design = design.fit(Boston)
- X = design.transform(Boston)
- In [13]: design = MS(['lstat'])
- X = design.fit_transform(Boston)

#### 例子 / 代码 / 图表

- We first describe this process for our simple regression model using a single predictor lstat in the Boston data frame, but will use it repeatedly in more complex tasks in this and other labs in this book. In our case t…
- The fit() method takes the original array and may do some initial computations on it, as specified in the transform object. For example, it may compute means and standard deviations for centering and scaling. The transf…
- In this simple case, the fit() method does very little; it simply checks that the variable 'lstat' specified in design exists in Boston. Then transform() constructs the model matrix with two columns: an intercept and th…
- `python` 代码块，源行 5533：In [12]: design = MS(['lstat']) / design = design.fit(Boston) / X = design.transform(Boston) / X[:4]
- `csv` 代码块，源行 5540：Out[12]: intercept lstat / 0 1.0 4.98 / 1 1.0 9.14 / 2 1.0 4.03
- `python` 代码块，源行 5552：In [13]: design = MS(['lstat']) / X = design.fit_transform(Boston) / X[:4]

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Using Transformations: Fit and Transform」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 104. Defining Functions

- 原始层级：H1，源行：L5645
- 推荐周次：第 3 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- While there is a function within the ISLP package that adds a line to an existing plot, we take this opportunity to define our first function to do so.
- A few things are illustrated above. First we see the syntax for defining a function: def funcname(...). The function has arguments ax, b, m where ax is an axis object for an existing plot, b is the intercept and m is th…
- The addition of \*args allows any number of non-named arguments to abline, while \*kwargs allows any number of named arguments (such as linewidth=3) to abline. In our function, we pass these arguments verbatim to ax.plo…

#### 公式与符号

- xlim = ax.get_xlim()
- ylim = [m * xlim[0] + b, m * xlim[1] + b]
- xlim = ax.get_xlim()
- ylim = [m * xlim[0] + b, m * xlim[1] + b]
- ax = Boston.plot.scatter('lstat', 'medv')

#### 例子 / 代码 / 图表

- Thus, the final call to ax.plot() is ax.plot(xlim, ylim, 'r--', linewidth=3). We have used the argument 'r--' to produce a red dashed line, and added an argument to make it of width 3. There is some evidence for non-lin…
- The np.argmax() function identifies the index of the largest element of an array, optionally computed over an axis of the array. In this case, we maximized over the entire array to determine which observation has the la…
- `python` 代码块，源行 5653：def abline(ax, b, m): / "Add a line with slope m and intercept b to ax" / xlim = ax.get_xlim() / ylim = [m * xlim[0] + b, m * xlim[1] + b]
- `python` 代码块，源行 5665：def abline(ax, b, m, *args, **kwargs): / "Add a line with slope m and intercept b to ax" / xlim = ax.get_xlim() / ylim = [m * xlim[0] + b, m * xlim[1] + b]
- `python` 代码块，源行 5679：ax = Boston.plot.scatter('lstat', 'medv') / abline(ax, / results.params[0], / results.params[1],

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Defining Functions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 105. 3.6.3 Multiple Linear Regression

- 原始层级：H1，源行：L5732
- 推荐周次：第 3 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- In order to fit a multiple linear regression model using least squares, we again use the ModelSpec() transform to construct the required model matrix and response. The arguments to ModelSpec() can be quite general, but…
- Notice how we have compacted the first line into a succinct expression describing the construction of x.
- The Boston data set contains 12 variables, and so it would be cumbersome to have to type all of these in order to perform a regression using all of the predictors. Instead, we can use the following short-hand:

#### 公式与符号

- X = MS(['lstat', 'age']).fit_transform(Boston)
- model1 = sm.OLS(y, X)
- results1 = model1.fit()
- terms = Boston.columns.drop('medv')
- Out[26]: Index(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'lstat'], dtype='object')

#### 例子 / 代码 / 图表

- In order to fit a multiple linear regression model using least squares, we again use the ModelSpec() transform to construct the required model matrix and response. The arguments to ModelSpec() can be quite general, but…
- What if we would like to perform a regression using all of the variables but one? For example, in the above regression output, age has a high p-value. So we may wish to run a regression excluding this predictor. The fol…
- `matlab` 代码块，源行 5738：X = MS(['lstat', 'age']).fit_transform(Boston) / model1 = sm.OLS(y, X) / results1 = model1.fit() / summarize(results1)
- `batch` 代码块，源行 5747：coef std err t P>|t| / intercept 33.2228 0.731 45.458 0.000 / lstat -1.0321 0.048 -21.416 0.000 / age 0.0345 0.012 2.826 0.005
- `txt` 代码块，源行 5763：terms = Boston.columns.drop('medv') / terms

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.3 Multiple Linear Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 106. 3.6.4 Multivariate Goodness of Fit

- 原始层级：H1，源行：L5807
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We can access the individual components of results by name (dir(results) shows us what is available). Hence results.rsquared gives us the $R^{2}$ , and np.sqrt(results.scale) gives us the RSE.
- Variance inflation factors (section 3.3.3) are sometimes useful to assess the effect of collinearity in the model matrix of a regression model. We will compute the VIFs in our multiple regression fit, and use the opport…

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.4 Multivariate Goodness of Fit」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 107. List Comprehension

- 原始层级：H1，源行：L5815
- 推荐周次：第 3 周, 第 5 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Often we encounter a sequence of objects which we would like to transform for some other task. Below, we compute the VIF for each feature in our x matrix and produce a data frame whose index agrees with the columns of x…
- List comprehensions are simple and powerful ways to form lists of Python objects. The language also supports dictionary and generator comprehension, though these are beyond our scope here. Let's look at an example. We c…
- The function VIF() takes two arguments: a dataframe or array, and a variable column index. In the code above we call VIF() on the fly for all columns in x. We have excluded column 0 above (the intercept), which is not o…

#### 公式与符号

- vals = [VIF(X, i)
- vif = pd.DataFrame({'vif':vals},
- index=X.columns[1:])
- vals = []

#### 例子 / 代码 / 图表

- List comprehensions are simple and powerful ways to form lists of Python objects. The language also supports dictionary and generator comprehension, though these are beyond our scope here. Let's look at an example. We c…
- The function VIF() takes two arguments: a dataframe or array, and a variable column index. In the code above we call VIF() on the fly for all columns in x. We have excluded column 0 above (the intercept), which is not o…
- `python` 代码块，源行 5822：vals = [VIF(X, i) / for i in range(1, X.shape[1])] / vif = pd.DataFrame({'vif':vals}, / index=X.columns[1:])
- `csv` 代码块，源行 5831：Out[29]: vif / crim 1.767 / zn 2.298 / indus 3.987
- `python` 代码块，源行 5852：vals = [] / for i in range(1, X.values.shape[1]): / vals.append(VIF(X.values, i))

#### 备课摘取建议

- 若用于 PPT，可把本节作为「List Comprehension」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 108. 3.6.5 Interaction Terms

- 原始层级：H1，源行：L5860
- 推荐周次：第 3 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- It is easy to include interaction terms in a linear model using ModelSpec(). Including a tuple ("lstat", "age") tells the model matrix builder to include an interaction term between lstat and age.
- age -0.0007 0.020 -0.036 0.971 lstat:age 0.0042 0.002 2.244 0.025

#### 公式与符号

- X = MS(['lstat', 'age', ('lstat', 'age')]).fit_transform(Boston)
- model2 = sm.OLS(y, X)

#### 例子 / 代码 / 图表

- `python` 代码块，源行 5865：X = MS(['lstat', 'age', ('lstat', 'age')]).fit_transform(Boston) / model2 = sm.OLS(y, X) / summarize(model2.fit())
- `txt` 代码块，源行 5872：coef std err t P>|t| / intercept 36.0885 1.470 24.553 0.000 / lstat -1.3921 0.167 -8.313 0.000

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.5 Interaction Terms」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 109. 3.6.6 Non-linear Transformations of the Predictors

- 原始层级：H1，源行：L5880
- 推荐周次：第 3 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- The model matrix builder can include terms beyond just column names and interactions. For instance, the poly() function supplied in ISLP specifies that columns representing polynomial functions of its first argument are…
- The effectively zero $p$ -value associated with the quadratic term (i.e. the third row above) suggests that it leads to an improved model.
- By default, poly() creates a basis matrix for inclusion in the model matrix whose columns are orthogonal polynomials, which are designed for stable least squares computations. $^{13}$ Alternatively, had we included an a…

#### 公式与符号

- In [32]: X = MS([poly('lstat', degree=2), 'age']).fit_transform(Boston)
- model3 = sm.OLS(y, X)
- results3 = model3.fit()
- poly(lstat, degree=2)[0] -179.2279 6.733 -26.620 0.000
- poly(lstat, degree=2)[1] 72.9908 5.482 13.315 0.000

#### 例子 / 代码 / 图表

- By default, poly() creates a basis matrix for inclusion in the model matrix whose columns are orthogonal polynomials, which are designed for stable least squares computations. $^{13}$ Alternatively, had we included an a…
- The function anova\_lm() can take more than two nested models as input, in which case it compares every successive pair of models. That also explains why their are NaNs in the first row above, since there is no previous…
- `python` 代码块，源行 5886：In [32]: X = MS([poly('lstat', degree=2), 'age']).fit_transform(Boston) / model3 = sm.OLS(y, X) / results3 = model3.fit() / summarize(results3)
- `txt` 代码块，源行 5893：Out[32]: coef std err t P>|t| / intercept 17.7151 0.781 22.681 0.000 / poly(lstat, degree=2)[0] -179.2279 6.733 -26.620 0.000 / poly(lstat, degree=2)[1] 72.9908 5.482 13.315 0.000
- `txt` 代码块，源行 5912：In [33]: anova_lm(results1, results3)

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.6 Non-linear Transformations of the Predictors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 110. 3.6.7 Qualitative Predictors

- 原始层级：H1，源行：L5936
- 推荐周次：第 3 周, 第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Here we use the Carseats data, which is included in the ISLP package. We will attempt to predict Sales (child car seat sales) in 400 locations based on a number of predictors.
- The Carseats data includes qualitative predictors such as ShelveLoc, an indicator of the quality of the shelving location — that is, the space within a store in which the car seat is displayed. The predictor ShelveLoc t…
- CompPrice 0.0929 0.004 22.567 0.000 Income 0.0109 0.003 4.183 0.000 Advertising 0.0702 0.023 3.107 0.002 Population 0.0002 0.000 0.433 0.665 Price -0.1008 0.007 -13.549 0.000 ShelveLoc[Good] 4.8487 0.153 31.724 0.000 Sh…

#### 公式与符号

- In [35]: Carseats = load_data('Carseats')
- Out[35]: Index(['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'ShelveLoc', 'Age', 'Education', 'Urban', 'US'], dtype='object')
- In [36]: allvars = list(Carseats.columns.drop('Sales'))
- y = Carseats['Sales']
- final = allvars + [('Income', 'Advertising'),

#### 例子 / 代码 / 图表

- `python` 代码块，源行 5940：In [35]: Carseats = load_data('Carseats') / Carseats.columns
- `javascript` 代码块，源行 5945：Out[35]: Index(['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'Sh…
- `txt` 代码块，源行 5951：In [36]: allvars = list(Carseats.columns.drop('Sales')) / y = Carseats['Sales'] / final = allvars + [('Income', 'Advertising'), / ('Price', 'Age')]

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.6.7 Qualitative Predictors」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 111. 3.7 Exercises

- 原始层级：H1，源行：L5970
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 未在本节自动识别到明显例子、代码或图表。

#### 备课摘取建议

- 若用于 PPT，可把本节作为「3.7 Exercises」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 112. Conceptual

- 原始层级：H1，源行：L5972
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- (a) Which answer is correct, and why?
- i. For a fixed value of IQ and GPA, high school graduates earn more, on average, than college graduates.
- ii. For a fixed value of IQ and GPA, college graduates earn more, on average, than high school graduates.

#### 公式与符号

- $$
- $$
- $$
- \hat {\beta} = \left(\sum_ {i = 1} ^ {n} x _ {i} y _ {i}\right) / \left(\sum_ {i ^ {\prime} = 1} ^ {n} x _ {i ^ {\prime}} ^ {2}\right). \tag {3.38}
- $$

#### 例子 / 代码 / 图表

- 6. Using (3.4), argue that in the case of simple linear regression, the least squares line always passes through the point $(\bar{x}, \bar{y})$ .
- 7. It is claimed in the text that in the case of simple linear regression of $Y$ onto $X$ , the $R^2$ statistic (3.17) is equal to the square of the correlation between $X$ and $Y$ (3.18). Prove that this is the case. F…
- 图片引用：`images/5fc20a94fa323e43a50dd472a5707c7df8b37fb9e4fd05e534683fdfb226041c.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Conceptual」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 113. Applied

- 原始层级：H1，源行：L6030
- 推荐周次：第 3 周, 第 5 周, 第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- 8. This question involves the use of simple linear regression on the Auto data set.
- (a) Use the sm.OLS() function to perform a simple linear regression with mpg as the response and horsepower as the predictor. Use the summarize() function to print the results. Comment on the output. For example:
- i. Is there a relationship between the predictor and the response? ii. How strong is the relationship between the predictor and the response? iii. Is the relationship between the predictor and the response positive or n…

#### 公式与符号

- (d) For which of the predictors can you reject the null hypothesis $H_0: \beta_j = 0$ ?
- 11. In this problem we will investigate the t-statistic for the null hypothesis $H_{0} : \beta = 0$ in simple linear regression without an intercept. To begin, we generate a predictor x and a response y as follows.
- rng = np.random.default_rng(1)
- x = rng.normal(size=100)
- y = 2 * x + rng.normal(size=100)

#### 例子 / 代码 / 图表

- (a) Use the sm.OLS() function to perform a simple linear regression with mpg as the response and horsepower as the predictor. Use the summarize() function to print the results. Comment on the output. For example:
- (b) Plot the response and the predictor in a new set of axes ax. Use the ax.axline() method or the abline() function defined in the lab to display the least squares regression line. (c) Produce some of diagnostic plots…
- (d) Produce some of diagnostic plots of the linear regression fit as described in the lab. Comment on any problems you see with the fit. Do the residual plots suggest any unusually large outliers? Does the leverage plot…
- `python` 代码块，源行 6078：rng = np.random.default_rng(1) / x = rng.normal(size=100) / y = 2 * x + rng.normal(size=100)
- `python` 代码块，源行 6135：rng = np.random.default_rng(10) / x1 = rng.uniform(0, 1, size=100) / x2 = 0.5 * x1 + rng.normal(size=100) / 10 / y = 2 + 2 * x1 + 0.3 * x2 + rng.normal(size=100)
- `txt` 代码块，源行 6154：x1 = np.concatenate([x1, [0.1]]) / x2 = np.concatenate([x2, [0.8]]) / y = np.concatenate([y, [6]])
- 图片引用：`images/7d9251358226ed18095ed066f779609af254eaa04669433b9cc24fe60c7c5619.jpg`

#### 备课摘取建议

- 若用于 PPT，可把本节作为「Applied」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 114. 4.1 An Overview of Classification

- 原始层级：H1，源行：L6178
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- Classification problems occur often, perhaps even more so than regression problems. Some examples include:
- logistic regression linear discriminant analysis quadratic discriminant analysis naive Bayes K-nearest neighbors generalized linear models Poisson regression
- 1. A person arrives at the emergency room with a set of symptoms that could possibly be attributed to one of three medical conditions. Which of the three conditions does the individual have?

#### 公式与符号

- 未在本节自动识别到明显公式。

#### 例子 / 代码 / 图表

- 3. On the basis of DNA sequence data for a number of patients with and without a given disease, a biologist would like to figure out which DNA mutations are deleterious (disease-causing) and which are not.
- It is worth noting that Figure 4.1 displays a very pronounced relationship between the predictor balance and the response default. In most real applications, the relationship between the predictor and the response will…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.1 An Overview of Classification」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 115. 4.2 Why Not Linear Regression?

- 原始层级：H1，源行：L6217
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周, 第 17 周

#### 核心重点

- We have stated that linear regression is not appropriate in the case of a qualitative response. Why not?
- Suppose that we are trying to predict the medical condition of a patient in the emergency room on the basis of her symptoms. In this simplified example, there are three possible diagnoses: stroke, drug overdose, and epi…
- FIGURE 4.1. The Default data set. Left: The annual incomes and monthly credit card balances of a number of individuals. The individuals who defaulted on their credit card payments are shown in orange, and those who did…

#### 公式与符号

- $$
- Y = \left\{ \begin{array}{l l} 1 & \text { if stroke; } \\ 2 & \text { if drug overdose; } \\ 3 & \text { if epileptic seizure. } \end{array} \right.
- $$
- $$
- Y = \left\{ \begin{array}{l l} 1 & \text { if epileptic seizure; } \\ 2 & \text { if stroke; } \\ 3 & \text { if drug overdose, } \end{array} \right.

#### 例子 / 代码 / 图表

- We have stated that linear regression is not appropriate in the case of a qualitative response. Why not?
- Suppose that we are trying to predict the medical condition of a patient in the emergency room on the basis of her symptoms. In this simplified example, there are three possible diagnoses: stroke, drug overdose, and epi…
- FIGURE 4.1. The Default data set. Left: The annual incomes and monthly credit card balances of a number of individuals. The individuals who defaulted on their credit card payments are shown in orange, and those who did…
- 图片引用：`images/2cea0a45c0a29e167f0ab615359d090d4a6cf6ec861405185b0b84a92bc91f43.jpg`
- 图片引用：`images/83f693a720d5d8ce115bb330e447b2990e9ea7742c49e6315d4b7ed4959d9edf.jpg`
- 图片引用：`images/8c24d7b57f87841a5d71aa49d0d7d43ef06c9e714cca8ab04d7aabb8b22fa8cb.jpg`
- 表格行：| Balance | Income | Group |
- 表格行：| ------- | ------ | ----- |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.2 Why Not Linear Regression?」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 116. 4.3 Logistic Regression

- 原始层级：H1，源行：L6292
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Consider again the Default data set, where the response default falls into one of two categories, Yes or No. Rather than modeling this response Y directly, logistic regression models the probability that Y belongs to a…
- For the Default data, logistic regression models the probability of default. For example, the probability of default given balance can be written as
- $$ \operatorname * {P r} (\text { default } = \text { Yes } | \text { balance }). $$

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- For the Default data, logistic regression models the probability of default. For example, the probability of default given balance can be written as
- The values of $\Pr(\text{default} = \text{Yes}|\text{balance})$ , which we abbreviate $p(\text{balance})$ , will range between 0 and 1. Then for any given value of balance, a prediction can be made for default. For exam…
- FIGURE 4.2. Classification using the Default data. Left: Estimated probability of default using linear regression. Some estimated probabilities are negative! The orange ticks indicate the 0/1 values coded for default (N…
- 图片引用：`images/01cef9bd25a2e2da89c60486a67519228ca8f9d40fd49a8e49026383d9527f8e.jpg`
- 图片引用：`images/9af039110a64d83a97e344f1bd56fd0ce1c805a068ed05322ecb888b1bef4c8c.jpg`
- 表格行：| Balance | Probability of Default (Blue Line) | Probability of Default (Orange Dashed Line) |
- 表格行：| ------- | ---------------------------------- | ------------------------------------------ |
- 表格行：| 0 | ~0.0 | 1.0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3 Logistic Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 117. 4.3.1 The Logistic Model

- 原始层级：H1，源行：L6336
- 推荐周次：第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- How should we model the relationship between $p(X) = \Pr(Y = 1|X)$ and X? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent…
- $$ p (X) = \beta_ {0} + \beta_ {1} X. \tag {4.1} $$
- If we use this approach to predict default=Yes using balance, then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a nega…

#### 公式与符号

- How should we model the relationship between $p(X) = \Pr(Y = 1|X)$ and X? (For convenience we are using the generic 0/1 coding for the response.) In Section 4.2 we considered using a linear regression model to represent…
- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- If we use this approach to predict default=Yes using balance, then we obtain the model shown in the left-hand panel of Figure 4.2. Here we see the problem with this approach: for balances close to zero we predict a nega…
- To fit the model $(4.2)$ , we use a method called maximum likelihood, which we discuss in the next section. The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the Default data. No…
- The quantity $p(X)/[1-p(X)]$ is called the odds, and can take on any value between 0 and $\infty$ . Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively. For…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.1 The Logistic Model」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 118. 4.3.2 Estimating the Regression Coefficients

- 原始层级：H1，源行：L6378
- 推荐周次：第 6 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- $$ \ell (\beta_ {0}, \beta_ {1}) = \prod_ {i: y _ {i} = 1} p (x _ {i}) \prod_ {i ^ {\prime}: y _ {i ^ {\prime}} = 0} (1 - p (x _ {i ^ {\prime}})). \tag {4.5} $$
- The estimates $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$ are chosen to maximize this likelihood function.
- Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book. In the linear regression setting, the least squares approach is in fact a special cas…

#### 公式与符号

- $$
- $$

#### 例子 / 代码 / 图表

- Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book. In the linear regression setting, the least squares approach is in fact a special cas…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.2 Estimating the Regression Coefficients」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 119. 4.3.3 Making Predictions

- 原始层级：H1，源行：L6396
- 推荐周次：第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- Once the coefficients have been estimated, we can compute the probability of default for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probab…
- Coefficient Std. error z-statistic p-value Intercept -10.6513 0.3612 -29.5 &lt;0.0001 balance 0.0055 0.0002 24.9 &lt;0.0001
- TABLE 4.1. For the Default data, estimated coefficients of the logistic regression model that predicts the probability of default using balance. A one-unit increase in balance is associated with an increase in the log o…

#### 公式与符号

- $$
- $$
- $$
- $$
- $$

#### 例子 / 代码 / 图表

- Once the coefficients have been estimated, we can compute the probability of default for any given credit card balance. For example, using the coefficient estimates given in Table 4.1, we predict that the default probab…
- One can use qualitative predictors with the logistic regression model using the dummy variable approach from Section 3.3.1. As an example, the Default data set contains the qualitative variable student. To fit a model t…

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.3 Making Predictions」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。

### 120. 4.3.4 Multiple Logistic Regression

- 原始层级：H1，源行：L6424
- 推荐周次：第 6 周, 第 7 周, 第 8 周, 第 9 周, 第 10 周, 第 11 周, 第 12 周, 第 13 周

#### 核心重点

- We now consider the problem of predicting a binary response using multiple predictors. By analogy with the extension from simple to multiple linear regression in Chapter 3, we can generalize (4.4) as follows:
- $$ \log \left(\frac {p (X)}{1 - p (X)}\right) = \beta_ {0} + \beta_ {1} X _ {1} + \dots + \beta_ {p} X _ {p}, \tag {4.6} $$
- where $X = (X_{1},\ldots ,X_{p})$ are $p$ predictors. Equation 4.6 can be rewritten as

#### 公式与符号

- $$
- $$
- where $X = (X_{1},\ldots ,X_{p})$ are $p$ predictors. Equation 4.6 can be rewritten as
- $$
- $$

#### 例子 / 代码 / 图表

- FIGURE 4.3. Confounding in the Default data. Left: Default rates are shown for students (orange) and non-students (blue). The solid lines display default rate as a function of balance, while the horizontal broken lines…
- This simple example illustrates the dangers and subtleties associated with performing regressions involving only a single predictor when other predictors may also be relevant. As in the linear regression setting, the re…
- By substituting estimates for the regression coefficients from Table 4.3 into (4.7), we can make predictions. For example, a student with a credit card balance of \$1,500 and an income of \$40,000 has an estimated proba…
- 图片引用：`images/8c3655f0dae89572111af7dd5e0208f220a02473c8e046defa154b60c19c8fcb.jpg`
- 图片引用：`images/09f1e8ea715677f3e5405d17e3d92f827e69b09117ed81949c81722019fc8cf8.jpg`
- 表格行：| Credit Card Balance | Default Rate (Blue Line) | Default Rate (Orange Line) |
- 表格行：| ------------------- | ------------------------ | -------------------------- |
- 表格行：| 500 | 0.0 | 0.0 |

#### 备课摘取建议

- 若用于 PPT，可把本节作为「4.3.4 Multiple Logistic Regression」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。
