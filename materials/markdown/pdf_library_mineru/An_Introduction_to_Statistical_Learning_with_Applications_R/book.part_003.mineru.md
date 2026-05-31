---
type: source
title: An Introduction to Statistical Learning_ with Applications R--
format: mineru-api-markdown
raw_path: materials/raw/pdf_originals/An Introduction to Statistical Learning_ with Applications R--.pdf
mineru_raw_markdown: materials/markdown/pdf_library_mineru/api_raw/An_Introduction_to_Statistical_Learning_with_Applications_R/part_003/full.md
source_pages: 436
page_range: 401-436
generated: 2026-05-24 12:20:18
status: generated_part
---

![](images/5f5071d7125a472b07341b65f35adcbe31770c232cf61378d4c9879b33e7ea55.jpg)  
FIGURE 10.8. Forty-five observations generated in two-dimensional space. In reality there are three distinct classes, shown in separate colors. However, we will treat these class labels as unknown and will seek to cluster the observations in order to discover the classes from the data.

Figure 10.9) is built starting from the leaves and combining clusters up to the trunk. We will begin with a discussion of how to interpret a dendrogram and then discuss how hierarchical clustering is actually performed—that is, how the dendrogram is built.

# Interpreting a Dendrogram

We begin with the simulated data set shown in Figure 10.8, consisting of 45 observations in two-dimensional space. The data were generated from a three-class model; the true class labels for each observation are shown in distinct colors. However, suppose that the data were observed without the class labels, and that we wanted to perform hierarchical clustering of the data. Hierarchical clustering (with complete linkage, to be discussed later) yields the result shown in the left-hand panel of Figure 10.9. How can we interpret this dendrogram?

In the left-hand panel of Figure 10.9, each leaf of the dendrogram represents one of the 45 observations in Figure 10.8. However, as we move up the tree, some leaves begin to fuse into branches. These correspond to observations that are similar to each other. As we move higher up the tree, branches themselves fuse, either with leaves or other branches. The earlier (lower in the tree) fusions occur, the more similar the groups of observations are to each other. On the other hand, observations that fuse later (near the top of the tree) can be quite different. In fact, this statement can be made precise: for any two observations, we can look for the point in the tree where branches containing those two observations are first fused. The height of this fusion, as measured on the vertical axis, indicates how different the two observations are. Thus, observations that fuse at the very bottom of the tree are quite similar to each other, whereas observations that fuse close to the top of the tree will tend to be quite different.

![](images/3b9546a11ae75eb32107d2aae71b586b76be32e6bd16f535e670db5f484ae543.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| Row 1 | 10 |
| Row 2 | 4 |
| Row 3 | 3 |
| Row 4 | 2 |
| Row 5 | 1 |
| Row 6 | 7 |
| Row 7 | 4 |
| Row 8 | 3 |
| Row 9 | 2 |
| Row 10 | 1 |
| Row 11 | 1 |
| Row 12 | 1 |
| Row 13 | 1 |
| Row 14 | 1 |
| Row 15 | 1 |
| Row 16 | 1 |
| Row 17 | 1 |
| Row 18 | 1 |
| Row 19 | 1 |
| Row 20 | 1 |
| Row 21 | 1 |
| Row 22 | 1 |
| Row 23 | 1 |
| Row 24 | 1 |
| Row 25 | 1 |
| Row 26 | 1 |
| Row 27 | 1 |
| Row 28 | 1 |
| Row 29 | 1 |
| Row 30 | 1 |
| Row 31 | 1 |
| Row 32 | 1 |
| Row 33 | 1 |
| Row 34 | 1 |
| Row 35 | 1 |
| Row 36 | 1 |
| Row 37 | 1 |
| Row 38 | 1 |
| Row 39 | 1 |
| Row 40 | 1 |
| Row 41 | 1 |
| Row 42 | 1 |
| Row 43 | 1 |
| Row 44 | 1 |
| Row 45 | 1 |
| Row 46 | 1 |
| Row 47 | 1 |
| Row 48 | 1 |
| Row 49 | 1 |
| Row 50 | 1 |
| Row 51 | 1 |
| Row 52 | 1 |
| Row 53 | 1 |
| Row 54 | 1 |
| Row 55 | 1 |
| Row 56 | 1 |
| Row 57 | 1 |
| Row 58 | 1 |
| Row 59 | 1 |
| Row 60 | 1 |
| Row 61 | 1 |
| Row 62 | 1 |
| Row 63 | 1 |
| Row 64 | 1 |
| Row 65 | 1 |
| Row 66 | 1 |
| Row 67 | 1 |
| Row 68 | 1 |
| Row 69 | 1 |
| Row 70 | 1 |
| Row 71 | 1 |
| Row 72 | 1 |
| Row 73 | 1 |
| Row 74 | 1 |
| Row 75 | 1 |
| Row 76 | 1 |
| Row 77 | 1 |
| Row 78 | 1 |
| Row 79 | 1 |
| Row 80 | 1 |
| Row 81 | 1 |
| Row 82 | 1 |
| Row 83 | 1 |
| Row 84 | 1 |
| Row 85 | 1 |
| Row 86 | 1 |
| Row 87 | 1 |
| Row 88 | 1 |
| Row 89 | 1 |
| Row 90 | 1 |
| Row 91 | 1 |
| Row 92 | 1 |
| Row 93 | 1 |
| Row 94 | 1 |
| Row 95 | 1 |
| Row 96 | 1 |
| Row 97 | 1 |
| Row 98 | 1 |
| Row 99 | 1 |
| Column End | -2.
</details>

![](images/23f1d6c39d6d47cb8de3c01b00088c31fb477ee2e84d412fcc036357521bab16.jpg)

<details>
<summary>bar</summary>

| Level | Count |
|---|---|
| Row 1 | 10 |
| Row 2 | 4 |
| Row 3 | 3 |
| Row 4 | 2 |
| Row 5 | 1 |
| Row 6 | 7 |
| Row 7 | 4 |
| Row 8 | 2 |
| Row 9 | 1 |
| Row 10 | 1 |
| Row 11 | 1 |
| Row 12 | 1 |
| Row 13 | 1 |
| Row 14 | 1 |
| Row 15 | 1 |
| Row 16 | 1 |
| Row 17 | 1 |
| Row 18 | 1 |
| Row 19 | 1 |
| Row 20 | 1 |
| Row 21 | 1 |
| Row 22 | 1 |
| Row 23 | 1 |
| Row 24 | 1 |
| Row 25 | 1 |
| Row 26 | 1 |
| Row 27 | 1 |
| Row 28 | 1 |
| Row 29 | 1 |
| Row 30 | 1 |
| Row 31 | 1 |
| Row 32 | 1 |
| Row 33 | 1 |
| Row 34 | 1 |
| Row 35 | 1 |
| Row 36 | 1 |
| Row 37 | 1 |
| Row 38 | 1 |
| Row 39 | 1 |
| Row 40 | 1 |
| Row 41 | 1 |
| Row 42 | 1 |
| Row 43 | 1 |
| Row 44 | 1 |
| Row 45 | 1 |
| Row 46 | 1 |
| Row 47 | 1 |
| Row 48 | 1 |
| Row 49 | 1 |
| Row 50 | 1 |
| Row 51 | 1 |
| Row 52 | 1 |
| Row 53 | 1 |
| Row 54 | 1 |
| Row 55 | 1 |
| Row 56 | 1 |
| Row 57 | 1 |
| Row 58 | 1 |
| Row 59 | 1 |
| Row 60 | 1 |
| Row 61 | 1 |
| Row 62 | 1 |
| Row 63 | 1 |
| Row 64 | 1 |
| Row 65 | 1 |
| Row 66 | 1 |
| Row 67 | 1 |
| Row 68 | 1 |
| Row 69 | 1 |
| Row 70 | 1 |
| Row 71 | 1 |
| Row 72 | 1 |
| Row 73 | 1 |
| Row 74 | 1 |
| Row 75 | 1 |
| Row 76 | 1 |
| Row 77 | 1 |
| Row 78 | 1 |
| Row 79 | 1 |
| Row 80 | 1 |
| Row 81 | 1 |
| Row 82 | 1 |
| Row 83 | 1 |
| Row 84 | 1 |
| Row 85 | 1 |
| Row 86 | 1 |
| Row 87 | 1 |
| Row 88 | 1 |
| Row 89 | 1 |
| Row 90 | 1 |
| Row 91 | 1 |
| Row 92 | 1 |
| Row 93 | 1 |
| Row 94 | 1 |
| Row 95 | 1 |
| Row 96 | 1 |
| Row 97 | 1 |
| Row 98 | 1 |
| Row 99 | 1 |
| Column End: Column End = -2 (not explicitly labeled). The chart displays the same row labels as 'Row' in the table. The values are estimated based on the number of rows and columns. There is no additional data series or categories provided in the image.
</details>

![](images/cae7ad0c1e41fc6051b362d35a6a81f1096b73d38a19f9daa6c0b1dd2bc4c0cb.jpg)

<details>
<summary>bar</summary>

| Level | Value |
|---|---|
| 1 | 10 |
| 2 | 7 |
| 3 | 4 |
| 4 | 3 |
| 5 | 2 |
| 6 | 1 |
| 7 | 1 |
| 8 | 1 |
| 9 | 1 |
| 10 | 1 |
| 11 | 1 |
| 12 | 1 |
| 13 | 1 |
| 14 | 1 |
| 15 | 1 |
| 16 | 1 |
| 17 | 1 |
| 18 | 1 |
| 19 | 1 |
| 20 | 1 |
| 21 | 1 |
| 22 | 1 |
| 23 | 1 |
| 24 | 1 |
| 25 | 1 |
| 26 | 1 |
| 27 | 1 |
| 28 | 1 |
| 29 | 1 |
| 30 | 1 |
| 31 | 1 |
| 32 | 1 |
| 33 | 1 |
| 34 | 1 |
| 35 | 1 |
| 36 | 1 |
| 37 | 1 |
| 38 | 1 |
| 39 | 1 |
| 40 | 1 |
| 41 | 1 |
| 42 | 1 |
| 43 | 1 |
| 44 | 1 |
| 45 | 1 |
| 46 | 1 |
| 47 | 1 |
| 48 | 1 |
| 49 | 1 |
| 50 | 1 |
| 51 | 1 |
| 52 | 1 |
| 53 | 1 |
| 54 | 1 |
| 55 | 1 |
| 56 | 1 |
| 57 | 1 |
| 58 | 1 |
| 59 | 1 |
| 60 | 1 |
| 61 | 1 |
| 62 | 1 |
| 63 | 1 |
| 64 | 1 |
| 65 | 1 |
| 66 | 1 |
| 67 | 1 |
| 68 | 1 |
| 69 | 1 |
| 70 | 1 |
| 71 | 1 |
| 72 | 1 |
| 73 | 1 |
| 74 | 1 |
| 75 | 1 |
| 76 | 1 |
| 77 | 1 |
| 78 | 1 |
| 79 | 1 |
| 80 | 1 |
| 81 | 1 |
| 82 | 1 |
| 83 | 1 |
| 84 | 1 |
| 85 | 1 |
| 86 | 1 |
| 87 | 1 |
| 88 | 1 |
| 89 | 1 |
| 90 | 1 |
| 91 | 1 |
| 92 | 1 |
| 93 | 1 |
| 94 | 1 |
| 95 | 1 |
| 96 | 1 |
| 97 | 1 |
| 98 | 1 |
| 99 | 1 |
| Note: The 'Value' in the chart is not explicitly labeled in the code, so it is inferred from the visual structure of the tree diagram. The 'Category' labels are not present in the image.
</details>

FIGURE 10.9. Left: dendrogram obtained from hierarchically clustering the data from Figure 10.8 with complete linkage and Euclidean distance. Center: the dendrogram from the left-hand panel, cut at a height of nine (indicated by the dashed line). This cut results in two distinct clusters, shown in different colors. Right: the dendrogram from the left-hand panel, now cut at a height of five. This cut results in three distinct clusters, shown in different colors. Note that the colors were not used in clustering, but are simply used for display purposes in this figure.

This highlights a very important point in interpreting dendrograms that is often misunderstood. Consider the left-hand panel of Figure 10.10, which shows a simple dendrogram obtained from hierarchically clustering nine observations. One can see that observations 5 and 7 are quite similar to each other, since they fuse at the lowest point on the dendrogram. Observations 1 and 6 are also quite similar to each other. However, it is tempting but incorrect to conclude from the figure that observations 9 and 2 are quite similar to each other on the basis that they are located near each other on the dendrogram. In fact, based on the information contained in the dendrogram, observation 9 is no more similar to observation 2 than it is to observations 8, 5, and 7. (This can be seen from the right-hand panel of Figure 10.10, in which the raw data are displayed.) To put it mathematically, there are $2 ^ { n - 1 }$ possible reorderings of the dendrogram, where n is the number of leaves. This is because at each of the $n - 1$ points where fusions occur, the positions of the two fused branches could be swapped without affecting the meaning of the dendrogram. Therefore, we cannot draw conclusions about the similarity of two observations based on their proximity along the horizontal axis. Rather, we draw conclusions about the similarity of two observations based on the location on the vertical axis where branches containing those two observations first are fused.

![](images/5efbcfa975258fc9305d3fbd3f73d9398f375c4ec626d8ab331ee0d7280735af.jpg)

<details>
<summary>tree</summary>

| Level | Value |
|---|---|
| 1 | 0.3 |
| 2 | 1.5 |
| 3 | 1.2 |
| 4 | 0.9 |
| 5 | 0.3 |
| 6 | 0.4 |
| 7 | 0.3 |
| 8 | 0.7 |
| 9 | 1.7 |
</details>

![](images/8a4c4826b6e8210252d9f813631095ce6b5de0e858b8f3e3742f365d0c519df3.jpg)

<details>
<summary>scatter</summary>

| Point | X₁    | X₂    |
|-------|-------|-------|
| 1     | -0.5  | -1.2  |
| 2     | 0.0   | -1.0  |
| 3     | -1.5  | -0.5  |
| 4     | -1.5  | -1.5  |
| 5     | 1.0   | -0.2  |
| 6     | -1.0  | -1.2  |
| 7     | 1.0   | 0.0   |
| 8     | 0.5   | -0.2  |
| 9     | 0.0   | 0.5   |
</details>

FIGURE 10.10. An illustration of how to properly interpret a dendrogram with nine observations in two-dimensional space. Left: a dendrogram generated using Euclidean distance and complete linkage. Observations 5 and 7 are quite similar to each other, as are observations 1 and 6. However, observation 9 is no more similar to observation 2 than it is to observations 8, 5, and 7, even though observations 9 and 2 are close together in terms of horizontal distance. This is because observations 2, 8, 5, and 7 all fuse with observation 9 at the same height, approximately 1.8. Right: the raw data used to generate the dendrogram can be used to confirm that indeed, observation 9 is no more similar to observation 2 than it is to observations 8, 5, and 7.

Now that we understand how to interpret the left-hand panel of Figure 10.9, we can move on to the issue of identifying clusters on the basis of a dendrogram. In order to do this, we make a horizontal cut across the dendrogram, as shown in the center and right-hand panels of Figure 10.9. The distinct sets of observations beneath the cut can be interpreted as clusters. In the center panel of Figure 10.9, cutting the dendrogram at a height of nine results in two clusters, shown in distinct colors. In the right-hand panel, cutting the dendrogram at a height of five results in three clusters. Further cuts can be made as one descends the dendrogram in order to obtain any number of clusters, between 1 (corresponding to no cut) and n (corresponding to a cut at height 0, so that each observation is in its own cluster). In other words, the height of the cut to the dendrogram serves the same role as the K in K-means clustering: it controls the number of clusters obtained.

Figure 10.9 therefore highlights a very attractive aspect of hierarchical clustering: one single dendrogram can be used to obtain any number of clusters. In practice, people often look at the dendrogram and select by eye a sensible number of clusters, based on the heights of the fusion and the number of clusters desired. In the case of Figure 10.9, one might choose to select either two or three clusters. However, often the choice of where to cut the dendrogram is not so clear.

The term hierarchical refers to the fact that clusters obtained by cutting the dendrogram at a given height are necessarily nested within the clusters obtained by cutting the dendrogram at any greater height. However, on an arbitrary data set, this assumption of hierarchical structure might be unrealistic. For instance, suppose that our observations correspond to a group of people with a 50–50 split of males and females, evenly split among Americans, Japanese, and French. We can imagine a scenario in which the best division into two groups might split these people by gender, and the best division into three groups might split them by nationality. In this case, the true clusters are not nested, in the sense that the best division into three groups does not result from taking the best division into two groups and splitting up one of those groups. Consequently, this situation could not be well-represented by hierarchical clustering. Due to situations such as this one, hierarchical clustering can sometimes yield worse (i.e. less accurate) results than K-means clustering for a given number of clusters.

# The Hierarchical Clustering Algorithm

The hierarchical clustering dendrogram is obtained via an extremely simple algorithm. We begin by defining some sort of dissimilarity measure between each pair of observations. Most often, Euclidean distance is used; we will discuss the choice of dissimilarity measure later in this chapter. The algorithm proceeds iteratively. Starting out at the bottom of the dendrogram, each of the n observations is treated as its own cluster. The two clusters that are most similar to each other are then fused so that there now are n 1 clusters. Next the two clusters that are most similar to each other are fused again, so that there now are n 2 clusters. The algorithm proceeds in this fashion until all of the observations belong to one single cluster, and the dendrogram is complete. Figure 10.11 depicts the first few steps of the algorithm, for the data from Figure 10.9. To summarize, the hierarchical clustering algorithm is given in Algorithm 10.2.

This algorithm seems simple enough, but one issue has not been addressed. Consider the bottom right panel in Figure 10.11. How did we determine that the cluster 5, 7 should be fused with the cluster 8 ? We have a concept of the dissimilarity between pairs of observations, but how do we define the dissimilarity between two clusters if one or both of the clusters contains multiple observations? The concept of dissimilarity between a pair of observations needs to be extended to a pair of groups of observations. This extension is achieved by developing the notion of linkage, which defines the dissimilarity between two groups of observations. The four most common types of linkage—complete, average, single, and centroid—are briefly described in Table 10.2. Average, complete, and single linkage are most popular among statisticians. Average and complete

linkage

# Algorithm 10.2 Hierarchical Clustering

1. Begin with n observations and a measure (such as Euclidean distance) of all the n 	 = n(n 1)/2 pairwise dissimilarities. Treat each observation as its own cluster.

2. For i = n, n 1, . . . , 2:

(a) Examine all pairwise inter-cluster dissimilarities among the i clusters and identify the pair of clusters that are least dissimilar (that is, most similar). Fuse these two clusters. The dissimilarity between these two clusters indicates the height in the dendrogram at which the fusion should be placed.   
(b) Compute the new pairwise inter-cluster dissimilarities among the i 1 remaining clusters.

<table><tr><td>Linkage</td><td>Description</td></tr><tr><td>Complete</td><td>Maximal intercluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster A and the observations in cluster B, and record the largest of these dissimilarities.</td></tr><tr><td>Single</td><td>Minimal intercluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster A and the observations in cluster B, and record the smallest of these dissimilarities. Single linkage can result in extended, trailing clusters in which single observations are fused one-at-a-time.</td></tr><tr><td>Average</td><td>Mean intercluster dissimilarity. Compute all pairwise dissimilarities between the observations in cluster A and the observations in cluster B, and record the average of these dissimilarities.</td></tr><tr><td>Centroid</td><td>Dissimilarity between the centroid for cluster A (a mean vector of length p) and the centroid for cluster B. Centroid linkage can result in undesirable inversions.</td></tr></table>

TABLE 10.2. A summary of the four most commonly-used types of linkage in hierarchical clustering.

linkage are generally preferred over single linkage, as they tend to yield more balanced dendrograms. Centroid linkage is often used in genomics, but suffers from a major drawback in that an inversion can occur, whereby two clusters are fused at a height below either of the individual clusters in the dendrogram. This can lead to difficulties in visualization as well as in interpretation of the dendrogram. The dissimilarities computed in Step 2(b) of the hierarchical clustering algorithm will depend on the type of linkage used, as well as on the choice of dissimilarity measure. Hence, the resulting dendrogram typically depends quite strongly on the type of linkage used, as is shown in Figure 10.12.

![](images/cc0137c28e04dea438d5c6fd3f18a800aba3b3e82ea8f65f996fe1e1c7255b28.jpg)

<details>
<summary>scatter</summary>

| Point | X1    | X2    |
|-------|-------|-------|
| 1     | -0.6  | -1.0  |
| 2     | 0.0   | -0.8  |
| 3     | -1.3  | -0.5  |
| 4     | -1.3  | -1.5  |
| 5     | 1.0   | 0.0   |
| 6     | -0.9  | -1.2  |
| 7     | 1.1   | 0.1   |
| 8     | 0.6   | -0.3  |
| 9     | -0.2  | 0.3   |
</details>

![](images/317cca9346541a9f4ad3ac9e9b8c2931fd7111d07d3f9f261626f137a56859d0.jpg)

<details>
<summary>scatter</summary>

| Point | X1    | X2    |
|-------|-------|-------|
| 1     | -0.6  | -1.0  |
| 2     | 0.0   | -0.8  |
| 3     | -1.4  | -0.5  |
| 4     | -1.4  | -1.5  |
| 5     | 1.0   | 0.0   |
| 6     | -0.9  | -1.2  |
| 7     | 1.0   | 0.0   |
| 8     | 0.6   | -0.2  |
| 9     | 0.0   | 0.5   |
</details>

![](images/73d902609ff0f37fd15270d57f92c469b8d6bac144d6c0463b8146ddae5d4e6e.jpg)

<details>
<summary>scatter</summary>

| Point | X1    | X2    |
|-------|-------|-------|
| 1     | -0.8  | -1.2  |
| 2     | 0.0   | -0.8  |
| 3     | -1.3  | -1.4  |
| 4     | -1.4  | -1.5  |
| 5     | 1.0   | -0.2  |
| 6     | -0.9  | -1.2  |
| 7     | 1.0   | 0.1   |
| 8     | 0.7   | 0.3   |
| 9     | 0.8   | 0.5   |
</details>

![](images/2dc6e057865c3ce5eef886e42401b0748a134903085f1a97d810e2cfdc09facc.jpg)

<details>
<summary>scatter</summary>

| Point | X1    | X2    |
|-------|-------|-------|
| 1     | -0.8  | -1.2  |
| 2     | -0.5  | -0.8  |
| 3     | -1.0  | -1.0  |
| 4     | -1.3  | -1.4  |
| 5     | 1.0   | 0.0   |
| 6     | -0.9  | -1.1  |
| 7     | 1.0   | 0.1   |
| 8     | 0.6   | 0.2   |
| 9     | 0.8   | 0.3   |
</details>

FIGURE 10.11. An illustration of the first few steps of the hierarchical clustering algorithm, using the data from Figure 10.10, with complete linkage and Euclidean distance. Top Left: initially, there are nine distinct clusters, $\{ 1 \} , \{ 2 \} , \dots , \{ 9 \}$ . Top Right: the two clusters that are closest together, 5 and 7 , are fused into a single cluster. Bottom Left: the two clusters that are closest together, 6 and 1 , are fused into a single cluster. Bottom Right: the two clusters that are closest together using complete linkage, 8 and the cluster 5, 7 , are fused into a single cluster.

# Choice of Dissimilarity Measure

Thus far, the examples in this chapter have used Euclidean distance as the dissimilarity measure. But sometimes other dissimilarity measures might be preferred. For example, correlation-based distance considers two observations to be similar if their features are highly correlated, even though the observed values may be far apart in terms of Euclidean distance. This is an unusual use of correlation, which is normally computed between variables; here it is computed between the observation profiles for each pair of observations. Figure 10.13 illustrates the difference between Euclidean and correlation-based distance. Correlation-based distance focuses on the shapes of observation profiles rather than their magnitudes.

![](images/13ac06a2426644d7aa41c4a5018d6ca9b0ec8e4d24427f2555b7f6e58f585aeb.jpg)

<details>
<summary>tree</summary>

| Category         | Value |
| ---------------- | ----- |
| Average Linkage  | 100   |
| Complete Linkage | 50    |
| Single Linkage   | 30    |
</details>

FIGURE 10.12. Average, complete, and single linkage applied to an example data set. Average and complete linkage tend to yield more balanced clusters.

The choice of dissimilarity measure is very important, as it has a strong effect on the resulting dendrogram. In general, careful attention should be paid to the type of data being clustered and the scientific question at hand. These considerations should determine what type of dissimilarity measure is used for hierarchical clustering.

For instance, consider an online retailer interested in clustering shoppers based on their past shopping histories. The goal is to identify subgroups of similar shoppers, so that shoppers within each subgroup can be shown items and advertisements that are particularly likely to interest them. Suppose the data takes the form of a matrix where the rows are the shoppers and the columns are the items available for purchase; the elements of the data matrix indicate the number of times a given shopper has purchased a given item (i.e. a 0 if the shopper has never purchased this item, a 1 if the shopper has purchased it once, etc.) What type of dissimilarity measure should be used to cluster the shoppers? If Euclidean distance is used, then shoppers who have bought very few items overall (i.e. infrequent users of the online shopping site) will be clustered together. This may not be desirable. On the other hand, if correlation-based distance is used, then shoppers with similar preferences (e.g. shoppers who have bought items A and B but never items C or D) will be clustered together, even if some shoppers with these preferences are higher-volume shoppers than others. Therefore, for this application, correlation-based distance may be a better choice.

![](images/735d3998e36d2b358007bcd9d561e10bcb30f501c344ee9901b1f46a34125807.jpg)

<details>
<summary>line</summary>

| Variable Index | Observation 1 | Observation 2 | Observation 3 |
| -------------- | ------------- | ------------- | ------------- |
| 1              | 4             | 14            | 2             |
| 2              | 4             | 15            | 2             |
| 3              | 3             | 13            | 3             |
| 4              | 1             | 6             | 2             |
| 5              | 0             | 6             | 1             |
| 6              | -1            | 5             | 1             |
| 7              | 4             | 14            | 2             |
| 8              | 4             | 14            | 3             |
| 9              | 4             | 14            | 2             |
| 10             | 4             | 14            | 3             |
| 11             | 1             | 8             | 2             |
| 12             | -1            | 6             | 1             |
| 13             | -1            | 5             | 2             |
| 14             | 3             | 12            | 1             |
| 15             | 5             | 14            | 4             |
| 16             | 4             | 14            | 4             |
| 17             | 4             | 14            | 2             |
| 18             | 1             | 7             | 1             |
| 19             | 0             | 7             | 2             |
| 20             | 0             | 7             | 3             |
</details>

FIGURE 10.13. Three observations with measurements on 20 variables are shown. Observations 1 and 3 have similar values for each variable and so there is a small Euclidean distance between them. But they are very weakly correlated, so they have a large correlation-based distance. On the other hand, observations 1 and 2 have quite different values for each variable, and so there is a large Euclidean distance between them. But they are highly correlated, so there is a small correlation-based distance between them.

In addition to carefully selecting the dissimilarity measure used, one must also consider whether or not the variables should be scaled to have standard deviation one before the dissimilarity between the observations is computed. To illustrate this point, we continue with the online shopping example just described. Some items may be purchased more frequently than others; for instance, a shopper might buy ten pairs of socks a year, but a computer very rarely. High-frequency purchases like socks therefore tend to have a much larger effect on the inter-shopper dissimilarities, and hence on the clustering ultimately obtained, than rare purchases like computers. This may not be desirable. If the variables are scaled to have standard deviation one before the inter-observation dissimilarities are computed, then each variable will in effect be given equal importance in the hierarchical clustering performed. We might also want to scale the variables to have standard deviation one if they are measured on different scales; otherwise, the choice of units (e.g. centimeters versus kilometers) for a particular variable will greatly affect the dissimilarity measure obtained. It should come as no surprise that whether or not it is a good decision to scale the variables before computing the dissimilarity measure depends on the application at hand. An example is shown in Figure 10.14. We note that the issue of whether or not to scale the variables before performing clustering applies to K-means clustering as well.

![](images/291ef205ccfaf336de5133eaec703398ca6ff7b86573cb1237ba612fa66c9404.jpg)

<details>
<summary>bar</summary>

| Category   | Value |
| ---------- | ----- |
| Socks      | 8     |
| Socks      | 11    |
| Socks      | 6     |
| Socks      | 5     |
| Socks      | 6     |
| Socks      | 7     |
| Socks      | 8     |
| Computers  | 1     |
| Computers  | 1     |
| Computers  | 1     |
</details>

![](images/7aae46b9475586ea802c994e025e87a7efef75cadfcc65a973186405cc0d74e5.jpg)

<details>
<summary>bar</summary>

| Category | Series 1 | Series 2 | Series 3 | Series 4 | Series 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Socks | 1.0 | 0.87 | 0.74 | 0.62 | 1.3 |
| Computers | 0.0 | 1.3 | 1.3 | 1.3 | 0.0 |
</details>

![](images/5f51d03a32cb7413342af19ab5679bb1877bb1c9c5cd5940b0ed09eca50e9806.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| Socks | 0 |
| Computers | 1800 |
</details>

FIGURE 10.14. An eclectic online retailer sells two items: socks and computers. Left: the number of pairs of socks, and computers, purchased by eight online shoppers is displayed. Each shopper is shown in a different color. If inter-observation dissimilarities are computed using Euclidean distance on the raw variables, then the number of socks purchased by an individual will drive the dissimilarities obtained, and the number of computers purchased will have little effect. This might be undesirable, since (1) computers are more expensive than socks and so the online retailer may be more interested in encouraging shoppers to buy computers than socks, and (2) a large difference in the number of socks purchased by two shoppers may be less informative about the shoppers’ overall shopping preferences than a small difference in the number of computers purchased. Center: the same data is shown, after scaling each variable by its standard deviation. Now the number of computers purchased will have a much greater effect on the inter-observation dissimilarities obtained. Right: the same data are displayed, but now the y-axis represents the number of dollars spent by each online shopper on socks and on computers. Since computers are much more expensive than socks, now computer purchase history will drive the inter-observation dissimilarities obtained.

# 10.3.3 Practical Issues in Clustering

Clustering can be a very useful tool for data analysis in the unsupervised setting. However, there are a number of issues that arise in performing clustering. We describe some of these issues here.

# Small Decisions with Big Consequences

In order to perform clustering, some decisions must be made.

Should the observations or features first be standardized in some way? For instance, maybe the variables should be centered to have mean zero and scaled to have standard deviation one.

In the case of hierarchical clustering,

– What dissimilarity measure should be used?   
– What type of linkage should be used?   
– Where should we cut the dendrogram in order to obtain clusters?

In the case of K-means clustering, how many clusters should we look for in the data?

Each of these decisions can have a strong impact on the results obtained. In practice, we try several different choices, and look for the one with the most useful or interpretable solution. With these methods, there is no single right answer—any solution that exposes some interesting aspects of the data should be considered.

# Validating the Clusters Obtained

Any time clustering is performed on a data set we will find clusters. But we really want to know whether the clusters that have been found represent true subgroups in the data, or whether they are simply a result of clustering the noise. For instance, if we were to obtain an independent set of observations, then would those observations also display the same set of clusters? This is a hard question to answer. There exist a number of techniques for assigning a p-value to a cluster in order to assess whether there is more evidence for the cluster than one would expect due to chance. However, there has been no consensus on a single best approach. More details can be found in Hastie et al. (2009).

# Other Considerations in Clustering

Both K-means and hierarchical clustering will assign each observation to a cluster. However, sometimes this might not be appropriate. For instance, suppose that most of the observations truly belong to a small number of (unknown) subgroups, and a small subset of the observations are quite different from each other and from all other observations. Then since Kmeans and hierarchical clustering force every observation into a cluster, the clusters found may be heavily distorted due to the presence of outliers that do not belong to any cluster. Mixture models are an attractive approach for accommodating the presence of such outliers. These amount to a soft version of K-means clustering, and are described in Hastie et al. (2009).

In addition, clustering methods generally are not very robust to perturbations to the data. For instance, suppose that we cluster n observations, and then cluster the observations again after removing a subset of the n observations at random. One would hope that the two sets of clusters obtained would be quite similar, but often this is not the case!

# A Tempered Approach to Interpreting the Results of Clustering

We have described some of the issues associated with clustering. However, clustering can be a very useful and valid statistical tool if used properly. We mentioned that small decisions in how clustering is performed, such as how the data are standardized and what type of linkage is used, can have a large effect on the results. Therefore, we recommend performing clustering with different choices of these parameters, and looking at the full set of results in order to see what patterns consistently emerge. Since clustering can be non-robust, we recommend clustering subsets of the data in order to get a sense of the robustness of the clusters obtained. Most importantly, we must be careful about how the results of a clustering analysis are reported. These results should not be taken as the absolute truth about a data set. Rather, they should constitute a starting point for the development of a scientific hypothesis and further study, preferably on an independent data set.

# 10.4 Lab 1: Principal Components Analysis

In this lab, we perform PCA on the USArrests data set, which is part of the base R package. The rows of the data set contain the 50 states, in alphabetical order.

```txt
> states=row.names(USArrests)
> states 
```

The columns of the data set contain the four variables.

```powershell
> names(USArrests)
[1] "Murder" "Assault" "UrbanPop" "Rape" 
```

We first briefly examine the data. We notice that the variables have vastly different means.

```txt
> apply(USArrests, 2, mean)
Murder Assault UrbanPop Rape
7.79 170.76 65.54 21.23 
```

Note that the apply() function allows us to apply a function—in this case, the mean() function—to each row or column of the data set. The second input here denotes whether we wish to compute the mean of the rows, 1, or the columns, 2. We see that there are on average three times as many rapes as murders, and more than eight times as many assaults as rapes. We can also examine the variances of the four variables using the apply() function.

```csv
> apply(USArrests, 2, var)
Murder Assault UrbanPop Rape
19.0 6945.2 209.5 87.7 
```

Not surprisingly, the variables also have vastly different variances: the UrbanPop variable measures the percentage of the population in each state living in an urban area, which is not a comparable number to the number of rapes in each state per 100,000 individuals. If we failed to scale the variables before performing PCA, then most of the principal components that we observed would be driven by the Assault variable, since it has by far the largest mean and variance. Thus, it is important to standardize the variables to have mean zero and standard deviation one before performing PCA.

We now perform principal components analysis using the prcomp() function, which is one of several functions in R that perform PCA.

prcomp()

```txt
> pr.out=prcomp(USArrests, scale=TRUE) 
```

By default, the prcomp() function centers the variables to have mean zero. By using the option scale=TRUE, we scale the variables to have standard deviation one. The output from prcomp() contains a number of useful quantities.

```snap
> names(pr.out)
[1] "sdev" "rotation" "center" "scale" "x" 
```

The center and scale components correspond to the means and standard deviations of the variables that were used for scaling prior to implementing PCA.

```csv
> pr.out$center
Murder Assault UrbanPop Rape
7.79 170.76 65.54 21.23
> pr.out$scale
Murder Assault UrbanPop Rape
4.36 83.34 14.47 9.37 
```

The rotation matrix provides the principal component loadings; each column of pr.out\$rotation contains the corresponding principal component loading vector.2

```txt
> pr.out$rotation
PC1 PC2 PC3 PC4
Murder -0.536 0.418 -0.341 0.649
Assault -0.583 0.188 -0.268 -0.743
UrbanPop -0.278 -0.873 -0.378 0.134
Rape -0.543 -0.167 0.818 0.089 
```

We see that there are four distinct principal components. This is to be expected because there are in general min(n 1, p) informative principal components in a data set with n observations and p variables.

Using the prcomp() function, we do not need to explicitly multiply the data by the principal component loading vectors in order to obtain the principal component score vectors. Rather the 50 4 matrix x has as its columns the principal component score vectors. That is, the kth column is the kth principal component score vector.

```txt
> dim(pr.out$x)
[1] 50 4 
```

We can plot the first two principal components as follows:

```txt
> biplot(pr.out, scale=0) 
```

The scale=0 argument to biplot() ensures that the arrows are scaled to represent the loadings; other values for scale give slightly different biplots with different interpretations.

biplot()

Notice that this figure is a mirror image of Figure 10.1. Recall that the principal components are only unique up to a sign change, so we can reproduce Figure 10.1 by making a few small changes:

```txt
> pr.out$rotation=-pr.out$rotation
> pr.out$x=-pr.out$x
> biplot(pr.out, scale=0) 
```

The prcomp() function also outputs the standard deviation of each principal component. For instance, on the USArrests data set, we can access these standard deviations as follows:

```txt
> pr.out$sdev
[1] 1.575 0.995 0.597 0.416 
```

The variance explained by each principal component is obtained by squaring these:

```txt
> pr.var=pr.out$sdev^2
> pr.var
[1] 2.480 0.990 0.357 0.173 
```

To compute the proportion of variance explained by each principal component, we simply divide the variance explained by each principal component by the total variance explained by all four principal components:

```txt
> pve=pr.var/sum(pr.var)
> pve
[1] 0.6201 0.2474 0.0891 0.0434 
```

We see that the first principal component explains 62.0 % of the variance in the data, the next principal component explains 24.7 % of the variance, and so forth. We can plot the PVE explained by each component, as well as the cumulative PVE, as follows:

```txt
> plot(pve, xlab="Principal Component", ylab="Proportion of Variance Explained", ylim=c(0,1), type='b')
> plot(cumsum(pve), xlab="Principal Component", ylab="Cumulative Proportion of Variance Explained", ylim=c(0,1), type='b') 
```

The result is shown in Figure 10.4. Note that the function cumsum() computes the cumulative sum of the elements of a numeric vector. For instance:

cumsum()

```txt
> a=c(1,2,8,-3)
> cumsum(a)
[1] 1 3 11 8 
```

# 10.5 Lab 2: Clustering

# 10.5.1 K-Means Clustering

The function kmeans() performs K-means clustering in R. We begin with a simple simulated example in which there truly are two clusters in the data: the first 25 observations have a mean shift relative to the next 25 observations.

kmeans()

```txt
> set.seed(2)
> x=matrix(rnorm(50*2), ncol=2)
> x[1:25,1]=x[1:25,1]+3
> x[1:25,2]=x[1:25,2]-4 
```

We now perform K-means clustering with K = 2.

```txt
> km.out=kmeans(x,2,nstart=20) 
```

The cluster assignments of the 50 observations are contained in km.out\$cluster.

```txt
> km.out$cluster
[1] 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1
[30] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
```

The K-means clustering perfectly separated the observations into two clusters even though we did not supply any group information to kmeans(). We can plot the data, with each observation colored according to its cluster assignment.

```txt
> plot(x, col=(km.out$cluster+1), main="K-Means Clustering Results with K=2", xlab="", ylab="", pch=20, cex=2) 
```

Here the observations can be easily plotted because they are two-dimensional. If there were more than two variables then we could instead perform PCA and plot the first two principal components score vectors.

In this example, we knew that there really were two clusters because we generated the data. However, for real data, in general we do not know the true number of clusters. We could instead have performed K-means clustering on this example with K = 3.

```txt
> set.seed(4)
> km.out = kmeans(x, 3, nstart = 20)
> km.out
K-means clustering with 3 clusters of sizes 10, 23, 17 
```

```txt
Cluster means:
    [,1]    [,2]
1 2.3001545 -2.69622023
2 -0.3820397 -0.08740753
3 3.7789567 -4.56200798

Clustering vector:
[1] 3 1 3 1 3 3 3 1 3 1 3 1 3 1 3 1 3 3 3 3 3 1 3 3 3 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 2 2 2

Within cluster sum of squares by cluster:
[1] 19.56137 52.67700 25.74089
(between_SS / total_SS = 79.3 %)

Available components:
[1] "cluster" "centers" "totss" "withinss"
    "tot.withinss" "betweenss" "size"
> plot(x, col=(km.out$cluster+1), main="K-Means Clustering Results with K=3", xlab="", ylab="", pch=20, cex=2) 
```

When K = 3, K-means clustering splits up the two clusters.

To run the kmeans() function in R with multiple initial cluster assignments, we use the nstart argument. If a value of nstart greater than one is used, then K-means clustering will be performed using multiple random assignments in Step 1 of Algorithm 10.1, and the kmeans() function will report only the best results. Here we compare using nstart=1 to nstart=20.

```diff
> set.seed(3)
> km.out=kmeans(x,3,nstart=1)
> km.out$tot.withinss
[1] 104.3319
> km.out=kmeans(x,3,nstart=20)
> km.out$tot.withinss
[1] 97.9793 
```

Note that km.out\$tot.withinss is the total within-cluster sum of squares, which we seek to minimize by performing K-means clustering (Equation 10.11). The individual within-cluster sum-of-squares are contained in the vector km.out\$withinss.

We strongly recommend always running K-means clustering with a large value of nstart, such as 20 or 50, since otherwise an undesirable local optimum may be obtained.

When performing K-means clustering, in addition to using multiple initial cluster assignments, it is also important to set a random seed using the set.seed() function. This way, the initial cluster assignments in Step 1 can be replicated, and the K-means output will be fully reproducible.

# 10.5.2 Hierarchical Clustering

The hclust() function implements hierarchical clustering in R. In the following example we use the data from Section 10.5.1 to plot the hierarchical clustering dendrogram using complete, single, and average linkage clustering, with Euclidean distance as the dissimilarity measure. We begin by clustering observations using complete linkage. The dist() function is used to compute the 50 50 inter-observation Euclidean distance matrix.

```txt
> hc.complete=hclust(dist(x), method="complete") 
```

We could just as easily perform hierarchical clustering with average or single linkage instead:

```txt
> hc.average=hclust(dist(x), method="average")
> hc.single=hclust(dist(x), method="single") 
```

We can now plot the dendrograms obtained using the usual plot() function. The numbers at the bottom of the plot identify each observation.

```txt
> par(mfrow=c(1,3))
> plot(hc.complete, main="Complete Linkage", xlab="", sub="", cex=.9)
> plot(hc.average, main="Average Linkage", xlab="", sub="", cex=.9)
> plot(hc.single, main="Single Linkage", xlab="", sub="", cex=.9) 
```

To determine the cluster labels for each observation associated with a given cut of the dendrogram, we can use the cutree() function:

```txt
> cutree(hc.complete, 2)
[1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
[30] 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
> cutree(hc.average, 2)
[1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
[30] 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2
> cutree(hc.single, 2)
[1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
[30] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
[30] 
```

For this data, complete and average linkage generally separate the observations into their correct groups. However, single linkage identifies one point as belonging to its own cluster. A more sensible answer is obtained when four clusters are selected, although there are still two singletons.

```txt
> cutree(hc.single, 4)
[1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 3 3 3 3
[30] 3 3 3 3 3 3 3 3 3 3 3 4 3 3 3 3 3 3 3 
```

To scale the variables before performing hierarchical clustering of the observations, we use the scale() function:

```txt
> xsc=scale(x)
> plot(hclust(dist(xsc), method="complete"), main="Hierarchical Clustering with Scaled Features") 
```

Correlation-based distance can be computed using the as.dist() function, which converts an arbitrary square symmetric matrix into a form that the hclust() function recognizes as a distance matrix. However, this only makes sense for data with at least three features since the absolute correlation between any two observations with measurements on two features is always 1. Hence, we will cluster a three-dimensional data set.

```txt
> x=matrix(rnorm(30*3), ncol=3)
> dd=as.dist(1-cor(t(x)))
> plot(hclust(dd, method="complete"), main="Complete Linkage with Correlation-Based Distance", xlab="", sub="") 
```

as.dist()

# 10.6 Lab 3: NCI60 Data Example

Unsupervised techniques are often used in the analysis of genomic data. In particular, PCA and hierarchical clustering are popular tools. We illustrate these techniques on the NCI60 cancer cell line microarray data, which consists of 6,830 gene expression measurements on 64 cancer cell lines.

```txt
> library(ISLR)
> nci.labs=NCI60$labs
> nci.data=NCI60$data 
```

Each cell line is labeled with a cancer type. We do not make use of the cancer types in performing PCA and clustering, as these are unsupervised techniques. But after performing PCA and clustering, we will check to see the extent to which these cancer types agree with the results of these unsupervised techniques.

The data has 64 rows and 6,830 columns.

```txt
> dim(nci.data)
[1] 64 6830 
```

We begin by examining the cancer types for the cell lines.

```txt
> nci.labs [1:4]
[1] "CNS" "CNS" "CNS" "RENAL"
> table(nci.labs)
nci.labs
BREAST CNS COLON K562A-repro K562B-repro
7 5 7 1 1
LEUKEMIA MCF7A-repro MCF7D-repro MELANOMA NSCLC
6 1 1 8 9
OVARIAN PROSTATE RENAL UNKNOWN
6 2 9 1 
```

# 10.6.1 PCA on the NCI60 Data

We first perform PCA on the data after scaling the variables (genes) to have standard deviation one, although one could reasonably argue that it is better not to scale the genes.

```txt
> pr.out=prcomp(nci.data, scale=TRUE) 
```

We now plot the first few principal component score vectors, in order to visualize the data. The observations (cell lines) corresponding to a given cancer type will be plotted in the same color, so that we can see to what extent the observations within a cancer type are similar to each other. We first create a simple function that assigns a distinct color to each element of a numeric vector. The function will be used to assign a color to each of the 64 cell lines, based on the cancer type to which it corresponds.

```diff
Cols=function(vec){
+    cols=rainbow(length(unique(vec)))
+    return(cols[as.numeric(as.factor(vec))])
+ } 
```

Note that the rainbow() function takes as its argument a positive integer, and returns a vector containing that number of distinct colors. We now can plot the principal component score vectors.

rainbow()

```txt
> par(mfrow=c(1,2))
> plot(pr.out$x[,1:2], col=Cols(nci.labs), pch=19, xlab="Z1", ylab="Z2")
> plot(pr.out$x[,c(1,3)], col=Cols(nci.labs), pch=19, xlab="Z1", ylab="Z3") 
```

The resulting plots are shown in Figure 10.15. On the whole, cell lines corresponding to a single cancer type do tend to have similar values on the first few principal component score vectors. This indicates that cell lines from the same cancer type tend to have pretty similar gene expression levels.

We can obtain a summary of the proportion of variance explained (PVE) of the first few principal components using the summary() method for a prcomp object (we have truncated the printout):

```txt
> summary (pr.out)
Importance of components:
PC1 PC2 PC3 PC4 PC5
Standard deviation 27.853 21.4814 19.8205 17.0326 15.9718
Proportion of Variance 0.114 0.0676 0.0575 0.0425 0.0374
Cumulative Proportion 0.114 0.1812 0.2387 0.2812 0.3185 
```

Using the plot() function, we can also plot the variance explained by the first few principal components.

```elixir
> plot(pr.out) 
```

Note that the height of each bar in the bar plot is given by squaring the corresponding element of pr.out\$sdev. However, it is more informative to plot the PVE of each principal component (i.e. a scree plot) and the cumulative PVE of each principal component. This can be done with just a little work.

![](images/0535b91a94e2b15e4fa035ab6f0871528a6fcc17699667eab9d851868292599d.jpg)

<details>
<summary>scatter</summary>

| Z1    | Z2    |
|-------|-------|
| -45   | -10   |
| -35   | 10    |
| -25   | 15    |
| -15   | 20    |
| -5    | 10    |
| 0     | 5     |
| 5     | 0     |
| 10    | -5    |
| 15    | -10   |
| 20    | -15   |
| 25    | -20   |
| 30    | -25   |
| 35    | -30   |
| 40    | -35   |
| 45    | -40   |
| 50    | -45   |
| 55    | -50   |
| 60    | -55   |
| 65    | -60   |
</details>

![](images/c4d1befc49583da6f6293a92eae16b593286e4ff91c3d97986b14955de2d1086.jpg)

<details>
<summary>scatter</summary>

| Z1  | Z3  |
| --- | --- |
| -40 | -20 |
| -30 | 0   |
| -20 | 10  |
| -10 | 5   |
| 0   | 0   |
| 10  | 10  |
| 20  | 20  |
| 30  | 30  |
| 40  | 40  |
| 50  | -30 |
| 60  | -40 |
| 70  | -30 |
</details>

FIGURE 10.15. Projections of the NCI60 cancer cell lines onto the first three principal components (in other words, the scores for the first three principal components). On the whole, observations belonging to a single cancer type tend to lie near each other in this low-dimensional space. It would not have been possible to visualize the data without using a dimension reduction method such as PCA, since based on the full data set there are $\binom { 6 , 8 3 0 } { 2 }$  possible scatterplots, none of which would have been particularly informative.

```txt
> pve=100*pr.out$sdev^2/sum(pr.out$sdev^2)
> par(mfrow=c(1,2))
> plot(pve, type="o", ylab="PVE", xlab="Principal Component", col="blue")
> plot(cumsum(pve), type="o", ylab="Cumulative PVE", xlab="Principal Component", col="brown3") 
```

(Note that the elements of pve can also be computed directly from the summary, summary(pr.out)\$importance[2,], and the elements of cumsum(pve) are given by summary(pr.out)\$importance[3,].) The resulting plots are shown in Figure 10.16. We see that together, the first seven principal components explain around 40 % of the variance in the data. This is not a huge amount of the variance. However, looking at the scree plot, we see that while each of the first seven principal components explain a substantial amount of variance, there is a marked decrease in the variance explained by further principal components. That is, there is an elbow in the plot after approximately the seventh principal component. This suggests that there may be little benefit to examining more than seven or so principal components (though even examining seven principal components may be difficult).

![](images/ec81bb74cd529320c7e03f4938479260555990af49aaf966348198fc1372e2cf.jpg)

<details>
<summary>line</summary>

| Principal Component | PVE  |
| ------------------- | ---- |
| 0                   | 11.0 |
| 5                   | 6.8  |
| 10                  | 3.8  |
| 15                  | 2.8  |
| 20                  | 2.2  |
| 25                  | 1.8  |
| 30                  | 1.5  |
| 35                  | 1.3  |
| 40                  | 1.1  |
| 45                  | 0.9  |
| 50                  | 0.7  |
| 55                  | 0.5  |
| 60                  | 0.3  |
| 65                  | 0.1  |
</details>

![](images/e725f6f6174527c4c2be24b904356de26e2d73c7487400e22de67e65e63ca832.jpg)

<details>
<summary>line</summary>

| Principal Component | Cumulative PVE |
| ------------------- | -------------- |
| 0                   | 10             |
| 5                   | 30             |
| 10                  | 45             |
| 15                  | 55             |
| 20                  | 65             |
| 25                  | 75             |
| 30                  | 80             |
| 35                  | 85             |
| 40                  | 90             |
| 45                  | 95             |
| 50                  | 98             |
| 55                  | 99             |
| 60                  | 100            |
</details>

FIGURE 10.16. The PVE of the principal components of the NCI60 cancer cell line microarray data set. Left: the PVE of each principal component is shown. Right: the cumulative PVE of the principal components is shown. Together, all principal components explain 100 % of the variance.

# 10.6.2 Clustering the Observations of the NCI60 Data

We now proceed to hierarchically cluster the cell lines in the NCI60 data, with the goal of finding out whether or not the observations cluster into distinct types of cancer. To begin, we standardize the variables to have mean zero and standard deviation one. As mentioned earlier, this step is optional and should be performed only if we want each gene to be on the same scale.

```javascript
> sd.data=scale(nci.data) 
```

We now perform hierarchical clustering of the observations using complete, single, and average linkage. Euclidean distance is used as the dissimilarity measure.

```txt
> par(mfrow=c(1,3))
> data.dist=dist(sd.data)
> plot(hclust(data.dist), labels=nci.labs, main="Complete Linkage", xlab="", sub="", ylab="")
> plot(hclust(data.dist, method="average"), labels=nci.labs, main="Average Linkage", xlab="", sub="", ylab="")
> plot(hclust(data.dist, method="single"), labels=nci.labs, main="Single Linkage", xlab="", sub="", ylab="") 
```

The results are shown in Figure 10.17. We see that the choice of linkage certainly does affect the results obtained. Typically, single linkage will tend to yield trailing clusters: very large clusters onto which individual observations attach one-by-one. On the other hand, complete and average linkage tend to yield more balanced, attractive clusters. For this reason, complete and average linkage are generally preferred to single linkage. Clearly cell lines within a single cancer type do tend to cluster together, although the

![](images/e1543a674c8d50e48d628f9e0ae842769a5121a8f56e9c97570043df2c8ec5bc.jpg)

<details>
<summary>tree</summary>

Complete Linkage
| Gene | Complete Linkage |
|---|---|
| BREAST | 10 |
| BREAST | 12 |
| CNS | 14 |
| CNS | 16 |
| CREAL | 18 |
| BREAST | 20 |
| NSCLC | 22 |
| CREAL | 24 |
| MELANOMA | 26 |
| OVARIAN | 28 |
| NSCLC | 30 |
| OVARIAN | 32 |
| COLON | 34 |
| COLON | 36 |
| PROSTATE | 38 |
| NSCLC | 40 |
| PROSTATE | 42 |
| NSCLC | 44 |
| CREAL | 46 |
| CREAL | 48 |
| VIVARIAN | 50 |
| Unknown | 52 |
| OVARIAN | 54 |
| NSCLC | 56 |
| CNS | 58 |
| CNS | 60 |
| NSCLC | 62 |
| CREAL | 64 |
| CREAL | 66 |
| NSCLC | 68 |
| CREAL | 70 |
| PRELKEMIA | 72 |
| PRELKEMIA | 74 |
| K562B-repro | 76 |
| K562A-repro | 78 |
| LEUKEMIA | 80 |
| LEUKEMIA | 82 |
| LEUKEMIA | 84 |
| LEUKEMIA | 86 |
| LEUKEMIA | 88 |
| LEUKEMIA | 90 |
| LEUKEMIA | 92 |
| LEUKEMIA | 94 |
| LEUKEMIA | 96 |
| LEUKEMIA | 98 |
| LEUKEMIA | 100 |
| LEUKEMIA | 102 |
| LEUKEMIA | 104 |
| LEUKEMIA | 106 |
| LEUKEMIA | 108 |
| LEUKEMIA | 110 |
| LEUKEMIA | 112 |
| LEUKEMIA | 114 |
| LEUKEMIA | 116 |
| LEUKEMIA | 118 |
| LEUKEMIA | 120 |
| LEUKEMIA | 122 |
| LEUKEMIA | 124 |
| LEUKEMIA | 126 |
| LEUKEMIA | 128 |
| LEUKEMIA | 130 |
| LEUKEMIA | 132 |
| LEUKEMIA | 134 |
| LEUKEMIA | 136 |
| LEUKEMIA | 138 |
| LEUKEMIA | 140 |
| LEUKEMIA | 142 |
| LEUKEMIA | 144 |
| LEUKEMIA | 146 |
| LEUKEMIA | 148 |
| LEUKEMIA | 150 |
| LEUKEMIA | 152 |
| LEUKEMIA | 154 |
| LEUKEMIA | 156 |
| LEUKEMIA | 158 |
| LEUKEMIA | 160 |
| LEUKEMIA | 162 |
| LEUKEMIA | 164 |
| LEUKEMIA | 166 |
| LEUKEMIA | 168 |
| LEUKEMIA | 170 |
| LEUKEMIA | 172 |
| LEUKEMIA | 174 |
| LEUKEMIA | 176 |
| LEUKEMIA | 178 |
| LEUKEMIA | 180 |
| LEUKEMIA | 182 |
| LEUKEMIA | 184 |
| LEUKEMIA | 186 |
| LEUKEMIA | 188 |
| LEUKEMIA | 190 |
| LEUKEMIA | 192 |
| LEUKEMIA | 194 |
| LEUKEMIA | 196 |
| LEUKEMIA | 198 |
| LEUKEMIA | 200 |
| LEUKEMIA | 202 |
| LEUKEMIA | 204 |
| LEUKEMIA | 206 |
| LEUKEMIA | 208 |
| LEUKEMIA | 210 |
| LEUKEMIA | 212 |
| LEUKEMIA | 214 |
| LEUKEMIA | 216 |
| LEUKEMIA | 218 |
| LEUKEMIA | 220 |
| LEUKEMIA | 222 |
| LEUKEMIA | 224 |
| LEUKEMIA | 226 |
| LEUKEMIA | 228 |
| LEUKEMIA | 230 |
| LEUKEMIA | 232 |
| LEUKEMIA | 234 |
| LEUKEMIA | 236 |
| LEUKEMIA | 238 |
| LEUKEMIA | 240 |
| LEUKEMIA | 242 |
| LEUKEMIA | 244 |
| LEUKEMIA | 246 |
| LEUKEMIA | 248 |
| LEUKEMIA | 250 |
| LEUKEMIA | 252 |
| LEUKEMIA | 254 |
| LEUKEMIA | 256 |
| LEUKEMIA | 258 |
| LEUKEMIA | 260 |
| LEUKEMIA | 262 |
| LEUKEMIA | 264 |
| LEUKEMIA | 266 |
| LEUKEMIA | 268 |
| LEUKEMIA | 270 |
| LEUKEMIA | 272 |
| LEUKEMIA | 274 |
| LEUKEMIA | 276 |
| LEUKEMIA | 278 |
| LEUKEMIA | 280 |
| LEUKEMIA | 282 |
| LEUKEMIA | 284 |
| LEUKEMIA | 286 |
| LEUKEMIA | 288 |
| LEUKEMIA | 290 |
| LEUKEMIA | 292 |
| LEUKEMIA | 294 |
| LEUKEMIA | 296 |
| LEUKEMIA | 298 |
| LEUKEMIA | 300 |
| LEUKEMIA | 302 |
| LEUKEMIA | 304 |
| LEUKEMIA | 306 |
| LEUKEMIA | 308 |
| LEUKEMIA | 310 |
| LEUKEMIA | 312 |
| LEUKEMIA | 314 |
| LEUKEMIA | 316 |
| LEUKEMIA | 318 |
| LEUKEMIA | 320 |
| LEUKEMIA | 322 |
| LEUKEMIA | 324 |
| LEUKEMIA | 326 |
| LEUKEMIA | 328 |
| LEUKEMIA | 330 |
| LEUKEMIA | 332 |
| LEUKEMIA | 334 |
| LEUKEMIA | 336 |
| LEUKEMIA | 338 |
| LEUKEMIA | 340 |
| LEUKEMIA | 342 |
| LEUKEMIA | 344 |
| LEUKEMIA | 346 |
| LEUKEMIA | 348 |
| LEUKEMIA | 350 |
| LEUKEMIA | 352 |
| LEUKEMIA | 354 |
| LEUKEMIA | 356 |
| LEUKEMIA | 358 |
| LEUKEMIA | 360 |
| LEUKEMIA | 362 |
| LEUKEMIA | 364 |
| LEUKEMIA | 366 |
| LEUKEMIA | 368 |
| LEUKEMIA | 370 |
| LEUKEMIA | 372 |
| LEUKEMIA | 374 |
| LEUKEMIA | 376 |
| LEUKEMIA | 378 |
| LEUKEMIA | 380 |
| LEUKEMIA | 382 |
| LEUKEMIA | 384 |
| LEUKEMIA | 386 |
| LEUKEMIA | 388 |
| LEUKEMIA | 390 |
| LEUKEMIA | 392 |
| LEUKEMIA | 394 |
| LEUKEMIA | 396 |
| LEUKEMIA | 398 |
| LEUKEMIA | 400
</details>

![](images/e9a8464c95c1308556eec7e7b8419a82abe26a5282916eb1d002aa87b500c323.jpg)

<details>
<summary>tree</summary>

Average Linkage
| Cancer Type | Average Linkage |
|---|---|
| LEUKEMIA | 120 |
| LEUKEMIA | 100 |
| LEUKEMIA | 80 |
| LEUKEMIA | 60 |
| K562B-repro | 40 |
| K562A-repro | 20 |
| RENAL | 10 |
| NSCLC | 5 |
| BREAST | 3 |
| NSCLC | 2 |
| BREAST | 1 |
| MCF7A-repro | 0 |
| BREAST | -1 |
| MCF7D-repro | -2 |
| COLON | -3 |
| COLON | -4 |
| COLON | -5 |
| RENAL | -6 |
| MELANOMA | -7 |
| MELANOMA | -8 |
| BREAST | -9 |
| MELANOMA | -10 |
| MELANOMA | -11 |
| MELANOMA | -12 |
| MELANOMA | -13 |
| MELANOMA | -14 |
| MELANOMA | -15 |
| MELANOMA | -16 |
| MELANOMA | -17 |
| MELANOMA | -18 |
| MELANOMA | -19 |
| MELANOMA | -20 |
| MELANOMA | -21 |
| MELANOMA | -22 |
| MELANOMA | -23 |
| MELANOMA | -24 |
| MELANOMA | -25 |
| MELANOMA | -26 |
| MELANOMA | -27 |
| MELANOMA | -28 |
| MELANOMA | -29 |
| MELANOMA | -30 |
| MELANOMA | -31 |
| MELANOMA | -32 |
| MELANOMA | -33 |
| MELANOMA | -34 |
| MELANOMA | -35 |
| MELANOMA | -36 |
| MELANOMA | -37 |
| MELANOMA | -38 |
| MELANOMA | -39 |
| MELANOMA | -40 |
| MELANOMA | -41 |
| MELANOMA | -42 |
| MELANOMA | -43 |
| MELANOMA | -44 |
| MELANOMA | -45 |
| MELANOMA | -46 |
| MELANOMA | -47 |
| MELANOMA | -48 |
| MELANOMA | -49 |
| MELANOMA | -50 |
| MELANOMA | -51 |
| MELANOMA | -52 |
| MELANOMA | -53 |
| MELANOMA | -54 |
| MELANOMA | -55 |
| MELANOMA | -56 |
| MELANOMA | -57 |
| MELANOMA | -58 |
| MELANOMA | -59 |
| MELANOMA | -60 |
| MELANOMA | -61 |
| MELANOMA | -62 |
| MELANOMA | -63 |
| MELANOMA | -64 |
| MELANOMA | -65 |
| MELANOMA | -66 |
| MELANOMA | -67 |
| MELANOMA | -68 |
| MELANOMA | -69 |
| MELANOMA | -70 |
| MELANOMA | -71 |
| MELANOMA | -72 |
| MELANOMA | -73 |
| MELANOMA | -74 |
| MELANOMA | -75 |
| MELANOMA | -76 |
| MELANOMA | -77 |
| MELANOMA | -78 |
| MELANOMA | -79 |
| MELANOMA | -80 |
| MELANOMA | -81 |
| MELANOMA | -82 |
| MELANOMA | -83 |
| MELANOMA | -84 |
| MELANOMA | -85 |
| MELANOMA | -86 |
| MELANOMA | -87 |
| MELANOMA | -88 |
| MELANOMA | -89 |
| MELANOMA | -90 |
| MELANOMA | -91 |
| MELANOMA | -92 |
| MELANOMA | -93 |
| MELANOMA | -94 |
| MELANOMA | -95 |
| MELANOMA | -96 |
| MELANOMA | -97 |
| MELANOMA | -98 |
| MELANOMA | -99 |
| MELANOMA | -100 |
| NSCLC | 100 |
| NSCLC | 110 |
| NSCLC | 120 |
| NSCLC | 130 |
| NSCLC | 140 |
| NSCLC | 150 |
| NSCLC | 160 |
| NSCLC | 170 |
| NSCLC | 180 |
| NSCLC | 190 |
| NSCLC | 200 |
| NSCLC | 210 |
| NSCLC | 220 |
| NSCLC | 230 |
| NSCLC | 240 |
| NSCLC | 250 |
| NSCLC | 260 |
| NSCLC | 270 |
| NSCLC | 280 |
| NSCLC | 290 |
| NSCLC | 300 |
| NSCLC | 310 |
| NSCLC | 320 |
| NSCLC | 330 |
| NSCLC | 340 |
| NSCLC | 350 |
| NSCLC | 360 |
| NSCLC | 370 |
| NSCLC | 380 |
| NSCLC | 390 |
| NSCLC | 400 |
| NSCLC | 410 |
| NSCLC | 420 |
| NSCLC | 430 |
| NSCLC | 440 |
| NSCLC | 450 |
| NSCLC | 460 |
| NSCLC | 470 |
| NSCLC | 480 |
| NSCLC | 490 |
| NSCLC | 500 |
| NSCLC | 510 |
| NSCLC | 520 |
| NSCLC | 530 |
| NSCLC | 540 |
| NSCLC | 550 |
| NSCLC | 560 |
| NSCLC | 570 |
| NSCLC | 580 |
| NSCLC | 590 |
| NSCLC | 600 |
| NSCLC | 610 |
| NSCLC | 620 |
| NSCLC | 630 |
| NSCLC | 640 |
| NSCLC | 650 |
| NSCLC | 660 |
| NSCLC | 670 |
| NSCLC | 680 |
| NSCLC | 690 |
| NSCLC | 700 |
| NSCLC | 710 |
| NSCLC | 720 |
| NSCLC | 730 |
| NSCLC | 740 |
| NSCLC | 750 |
| NSCLC | 760 |
| NSCLC | 770 |
| NSCLC | 780 |
| NSCLC | 790 |
| NSCLC | 800 |
| NSCLC | 810 |
| NSCLC | 820 |
| NSCLC | 830 |
| NSCLC | 840 |
| NSCLC | 850 |
| NSCLC | 860 |
| NSCLC | 870 |
| NSCLC | 880 |
| NSCLC | 890 |
| NSCLC | 900 |
| NSCLC | 910 |
| NSCLC | 920 |
| NSCLC | 930 |
| NSCLC | 940 |
| NSCLC | 950 |
| NSCLC | 960 |
| NSCLC | 970 |
| NSCLC | 980 |
| NSCLC | 990 |
| NSCLC | 1000 |

The chart displays the average linkage values for each cancer type. The average linkage values are estimated based on the numerical scale (e.g., “Linkages” or “Average”) in a hierarchical format. The labels above the bars represent the cancer types.
</details>

![](images/0bd148a40b6eff8e306e721bbe6131cf41218218dc82dbb4f7c6986e2cec7253.jpg)  
FIGURE 10.17. The NCI60 cancer cell line microarray data, clustered with average, complete, and single linkage, and using Euclidean distance as the dissimilarity measure. Complete and average linkage tend to yield evenly sized clusters whereas single linkage tends to yield extended clusters to which single leaves are fused one by one.

clustering is not perfect. We will use complete linkage hierarchical clustering for the analysis that follows.

We can cut the dendrogram at the height that will yield a particular number of clusters, say four:

```txt
> hc.out=hclust(dist(sd.data))
> hc.clusters=cutree(hc.out,4)
> table(hc.clusters,nci.labs) 
```

There are some clear patterns. All the leukemia cell lines fall in cluster 3, while the breast cancer cell lines are spread out over three different clusters. We can plot the cut on the dendrogram that produces these four clusters:

```txt
> par(mfrow=c(1,1))
> plot(hc.out, labels=nci.labs)
> abline(h=139, col="red") 
```

The abline() function draws a straight line on top of any existing plot in R. The argument h=139 plots a horizontal line at height 139 on the dendrogram; this is the height that results in four distinct clusters. It is easy to verify that the resulting clusters are the same as the ones we obtained using cutree(hc.out,4).

Printing the output of hclust gives a useful brief summary of the object:

```txt
> hc.out
Call:
hclust(d = dist(dat))
Cluster method : complete
Distance : euclidean
Number of objects: 64 
```

We claimed earlier in Section 10.3.2 that K-means clustering and hierarchical clustering with the dendrogram cut to obtain the same number of clusters can yield very different results. How do these NCI60 hierarchical clustering results compare to what we get if we perform K-means clustering with K = 4?

```txt
> set.seed(2)
> km.out=kmeans(sd.data, 4, nstart=20)
> km.clusters=km.out$cluster
> table(km.clusters,hc.clusters)
hc.clusters
km.clusters 1 2 3 4
1 11 0 0 9
2 0 0 8 0
3 9 0 0 0
4 20 7 0 0 
```

We see that the four clusters obtained using hierarchical clustering and Kmeans clustering are somewhat different. Cluster 2 in K-means clustering is identical to cluster 3 in hierarchical clustering. However, the other clusters differ: for instance, cluster 4 in K-means clustering contains a portion of the observations assigned to cluster 1 by hierarchical clustering, as well as all of the observations assigned to cluster 2 by hierarchical clustering.

Rather than performing hierarchical clustering on the entire data matrix, we can simply perform hierarchical clustering on the first few principal component score vectors, as follows:

```txt
> hc.out = hclust(dist(pr.out$x[,1:5]))
> plot(hc.out, labels=nci.labs, main="Hier. Clust. on First Five Score Vectors")
> table(cutree(hc.out,4), nci.labs) 
```

Not surprisingly, these results are different from the ones that we obtained when we performed hierarchical clustering on the full data set. Sometimes performing clustering on the first few principal component score vectors can give better results than performing clustering on the full data. In this situation, we might view the principal component step as one of denoising the data. We could also perform K-means clustering on the first few principal component score vectors rather than the full data set.

# 10.7 Exercises

# Conceptual

1. This problem involves the K-means clustering algorithm.

(a) Prove (10.12).

(b) On the basis of this identity, argue that the K-means clustering algorithm (Algorithm 10.1) decreases the objective (10.11) at each iteration.

2. Suppose that we have four observations, for which we compute a dissimilarity matrix, given by

$$
\left[ \begin{array}{c c c c} & 0. 3 & 0. 4 & 0. 7 \\ 0. 3 & & 0. 5 & 0. 8 \\ 0. 4 & 0. 5 & & 0. 4 5 \\ 0. 7 & 0. 8 & 0. 4 5 \end{array} \right].
$$

For instance, the dissimilarity between the first and second observations is 0.3, and the dissimilarity between the second and fourth observations is 0.8.

(a) On the basis of this dissimilarity matrix, sketch the dendrogram that results from hierarchically clustering these four observations using complete linkage. Be sure to indicate on the plot the height at which each fusion occurs, as well as the observations corresponding to each leaf in the dendrogram.

![](images/9fb828fc309d15807b3fb0761a8e8ce78426d1e0405d0cf317e820772f6dcca7.jpg)

(b) Repeat (a), this time using single linkage clustering. (c) Suppose that we cut the dendogram obtained in (a) such that two clusters result. Which observations are in each cluster?

(d) Suppose that we cut the dendogram obtained in (b) such that two clusters result. Which observations are in each cluster?

(e) It is mentioned in the chapter that at each fusion in the dendrogram, the position of the two clusters being fused can be swapped without changing the meaning of the dendrogram. Draw a dendrogram that is equivalent to the dendrogram in (a), for which two or more of the leaves are repositioned, but for which the meaning of the dendrogram is the same.

3. In this problem, you will perform K-means clustering manually, with K = 2, on a small example with n = 6 observations and p = 2 features. The observations are as follows.

<table><tr><td>Obs.</td><td> $X_1$ </td><td> $X_2$ </td></tr><tr><td>1</td><td>1</td><td>4</td></tr><tr><td>2</td><td>1</td><td>3</td></tr><tr><td>3</td><td>0</td><td>4</td></tr><tr><td>4</td><td>5</td><td>1</td></tr><tr><td>5</td><td>6</td><td>2</td></tr><tr><td>6</td><td>4</td><td>0</td></tr></table>

(a) Plot the observations.   
(b) Randomly assign a cluster label to each observation. You can use the sample() command in R to do this. Report the cluster labels for each observation.   
(c) Compute the centroid for each cluster.   
(d) Assign each observation to the centroid to which it is closest, in terms of Euclidean distance. Report the cluster labels for each observation.   
(e) Repeat (c) and (d) until the answers obtained stop changing.   
(f) In your plot from (a), color the observations according to the cluster labels obtained.

4. Suppose that for a particular data set, we perform hierarchical clustering using single linkage and using complete linkage. We obtain two dendrograms.

(a) At a certain point on the single linkage dendrogram, the clusters 1, 2, 3 and 4, 5 fuse. On the complete linkage dendrogram, the clusters 1, 2, 3 and 4, 5 also fuse at a certain point. Which fusion will occur higher on the tree, or will they fuse at the same height, or is there not enough information to tell?

(b) At a certain point on the single linkage dendrogram, the clusters 5 and 6 fuse. On the complete linkage dendrogram, the clusters 5 and 6 also fuse at a certain point. Which fusion will occur higher on the tree, or will they fuse at the same height, or is there not enough information to tell?

5. In words, describe the results that you would expect if you performed K-means clustering of the eight shoppers in Figure 10.14, on the basis of their sock and computer purchases, with K = 2. Give three answers, one for each of the variable scalings displayed. Explain.

6. A researcher collects expression measurements for 1,000 genes in 100 tissue samples. The data can be written as a $1 , 0 0 0 \times 1 0 0$ matrix, which we call X, in which each row represents a gene and each column a tissue sample. Each tissue sample was processed on a different day, and the columns of X are ordered so that the samples that were processed earliest are on the left, and the samples that were processed later are on the right. The tissue samples belong to two groups: control (C) and treatment (T). The C and T samples were processed in a random order across the days. The researcher wishes to determine whether each gene’s expression measurements differ between the treatment and control groups.

As a pre-analysis (before comparing T versus C), the researcher performs a principal component analysis of the data, and finds that the first principal component (a vector of length 100) has a strong linear trend from left to right, and explains 10 % of the variation. The researcher now remembers that each patient sample was run on one of two machines, A and B, and machine A was used more often in the earlier times while B was used more often later. The researcher has a record of which sample was run on which machine.

(a) Explain what it means that the first principal component “explains 10 % of the variation”.

(b) The researcher decides to replace the (i, j)th element of X with

$$
x _ {i j} - z _ {i 1} \phi_ {j 1}
$$

where $z _ { i 1 }$ is the ith score, and $\phi _ { j 1 }$ is the jth loading, for the first principal component. He will then perform a two-sample t-test on each gene in this new data set in order to determine whether its expression differs between the two conditions. Critique this idea, and suggest a better approach.

(c) Design and run a small simulation experiment to demonstrate the superiority of your idea.

![](images/7e50c7144e613b3df8fae4dec70ced1a923da8c67f35193b53bda3be2039ada3.jpg)

# Applied

7. In the chapter, we mentioned the use of correlation-based distance and Euclidean distance as dissimilarity measures for hierarchical clustering. It turns out that these two measures are almost equivalent: if each observation has been centered to have mean zero and standard deviation one, and if we let $r _ { i j }$ denote the correlation between the ith and jth observations, then the quantity $1 - r _ { i j }$ is proportional to the squared Euclidean distance between the ith and jth observations.

On the USArrests data, show that this proportionality holds.

Hint: The Euclidean distance can be calculated using the dist() function, and correlations can be calculated using the cor() function.

8. In Section 10.2.3, a formula for calculating PVE was given in Equation 10.8. We also saw that the PVE can be obtained using the sdev output of the prcomp() function.

On the USArrests data, calculate PVE in two ways:

(a) Using the sdev output of the prcomp() function, as was done in Section 10.2.3.

(b) By applying Equation 10.8 directly. That is, use the prcomp() function to compute the principal component loadings. Then, use those loadings in Equation 10.8 to obtain the PVE.

These two approaches should give the same results.

Hint: You will only obtain the same results in (a) and (b) if the same data is used in both cases. For instance, if in (a) you performed prcomp() using centered and scaled variables, then you must center and scale the variables before applying Equation 10.3 in (b).

9. Consider the USArrests data. We will now perform hierarchical clustering on the states.

(a) Using hierarchical clustering with complete linkage and Euclidean distance, cluster the states.

(b) Cut the dendrogram at a height that results in three distinct clusters. Which states belong to which clusters?

(c) Hierarchically cluster the states using complete linkage and Euclidean distance, after scaling the variables to have standard deviation one.

(d) What effect does scaling the variables have on the hierarchical clustering obtained? In your opinion, should the variables be scaled before the inter-observation dissimilarities are computed? Provide a justification for your answer.

10. In this problem, you will generate simulated data, and then perform PCA and K-means clustering on the data.

(a) Generate a simulated data set with 20 observations in each of three classes (i.e. 60 observations total), and 50 variables.

Hint: There are a number of functions in R that you can use to generate data. One example is the rnorm() function; runif() is another option. Be sure to add a mean shift to the observations in each class so that there are three distinct classes.

(b) Perform PCA on the 60 observations and plot the first two principal component score vectors. Use a different color to indicate the observations in each of the three classes. If the three classes appear separated in this plot, then continue on to part (c). If not, then return to part (a) and modify the simulation so that there is greater separation between the three classes. Do not continue to part (c) until the three classes show at least some separation in the first two principal component score vectors.

(c) Perform K-means clustering of the observations with K = 3. How well do the clusters that you obtained in K-means clustering compare to the true class labels?

Hint: You can use the table() function in R to compare the true class labels to the class labels obtained by clustering. Be careful how you interpret the results: K-means clustering will arbitrarily number the clusters, so you cannot simply check whether the true class labels and clustering labels are the same.

(d) Perform K-means clustering with K = 2. Describe your results.

(e) Now perform K-means clustering with K = 4, and describe your results.

(f) Now perform K-means clustering with K = 3 on the first two principal component score vectors, rather than on the raw data. That is, perform K-means clustering on the 60 2 matrix of which the first column is the first principal component score vector, and the second column is the second principal component score vector. Comment on the results.

(g) Using the scale() function, perform K-means clustering with K = 3 on the data after scaling each variable to have standard deviation one. How do these results compare to those obtained in (b)? Explain.

11. On the book website, www.StatLearning.com, there is a gene expression data set (Ch10Ex11.csv) that consists of 40 tissue samples with measurements on 1,000 genes. The first 20 samples are from healthy patients, while the second 20 are from a diseased group.

(a) Load in the data using read.csv(). You will need to select header=F.

(b) Apply hierarchical clustering to the samples using correlationbased distance, and plot the dendrogram. Do the genes separate the samples into the two groups? Do your results depend on the type of linkage used?

(c) Your collaborator wants to know which genes differ the most across the two groups. Suggest a way to answer this question, and apply it here.

# Index

Cp , 78, 205, 206, 210–213

R2, 68–71, 79–80, 103, 212

$\ell _ { 2 }$ norm, 216

$\ell _ { 1 }$ norm, 219

additive, 12, 86–90, 104

additivity, 282, 283

adjusted R2, 78, 205, 206, 210–213

Advertising data set, 15, 16, 20, 59, 61–63, 68, 69, 71–76, 79, 81, 82, 87, 88, 102–104

agglomerative clustering, 390

Akaike information criterion, 78, 205, 206, 210–213

alternative hypothesis, 67

analysis of variance, 290

area under the curve, 147

argument, 42

AUC, 147

Auto data set, 14, 48, 49, 56, 90–93, 121, 122, 171, 176–178, 180, 182, 191, 193–195, 299, 371

backfitting, 284, 300

backward stepwise selection, 79, 208–209, 247

bagging, 12, 26, 303, 316–319, 328–330

baseline, 86

basis function, 270, 273

Bayes

classifier, 37–40, 139

decision boundary, 140

error, 37–40

Bayes’ theorem, 138, 139, 226

Bayesian, 226–227

Bayesian information criterion, 78, 205, 206, 210–213

best subset selection, 205, 221, 244–247

bias, 33–36, 65, 82

bias-variance

decomposition, 34

trade-off, 33–37, 42, 105, 149, 217, 230, 239, 243, 278, 307, 347, 357

binary, 28, 130

biplot, 377, 378

Boolean, 159

boosting, 12, 25, 26, 303, 316, 321–324, 330–331

bootstrap, 12, 175, 187–190, 316

Boston data set, 14, 56, 110, 113, 126, 173, 201, 264, 299, 327, 328, 330, 333

bottom-up clustering, 390

boxplot, 50

branch, 305

Caravan data set, 14, 165, 335

Carseats data set, 14, 117, 123, 324, 333

categorical, 3, 28

classification, 3, 12, 28–29, 37–42, 127–173, 337–353

error rate, 311

tree, 311–314, 324–327

classifier, 127

cluster analysis, 26–28

clustering, 4, 26–28, 385–401

K-means, 12, 386–389

agglomerative, 390

bottom-up, 390

hierarchical, 386, 390–401

coefficient, 61

College data set, 14, 54, 263, 300

collinearity, 99–103

conditional probability, 37

confidence interval, 66–67, 81, 82, 103, 268

confounding, 136

confusion matrix, 145, 158

continuous, 3

contour plot, 46

contrast, 86

correlation, 70, 74, 396

Credit data set, 83, 84, 86, 89, 90, 99–102

cross-entropy, 311–312, 332

cross-validation, 12, 33, 36, 175–186, 205, 227, 248–251

k-fold, 181–184

leave-one-out, 178–181

curse of dimensionality, 108, 168, 242–243

data frame, 48

Data sets

Advertising, 15, 16, 20, 59, 61–63, 68, 69, 71–76, 79, 81, 82, 87, 88, 102–104

Auto, 14, 48, 49, 56, 90–93, 121, 122, 171, 176–178, 180, 182, 191, 193–195, 299, 371

Boston, 14, 56, 110, 113, 126, 173, 201, 264, 299, 327, 328, 330, 333

Caravan, 14, 165, 335

Carseats, 14, 117, 123, 324, 333

College, 14, 54, 263, 300

Credit, 83, 84, 86, 89, 90,99–102

Default, 14, 128–137, 144–148, 198, 199

Heart, 312, 313, 317–320, 354, 355

Hitters, 14, 244, 251, 255, 256, 304, 305, 310, 311, 334

Income, 16–18, 22–24

Khan, 14, 366

NCI60, 4, 5, 14, 407, 409–412

OJ, 14, 334, 371

Portfolio, 14, 194

Smarket, 3, 14, 154, 161, 163, 171

USArrests, 14, 377, 378, 381–383

Wage, 1, 2, 9, 10, 14, 267, 269, 271, 272, 274–277, 280, 281, 283, 284, 286, 287, 299

Weekly, 14, 171, 200

decision tree, 12, 303–316

Default data set, 14, 128–137, 144–148, 198, 199

degrees of freedom, 32, 241, 271, 272, 278

dendrogram, 386, 390–396

density function, 138

dependent variable, 15

derivative, 272, 278

deviance, 206

dimension reduction, 204, 228–238

discriminant function, 141

dissimilarity, 396–398

distance

correlation-based, 396–398, 416

Euclidean, 379, 387, 388, 394, 396–398

double-exponential distribution, 227

dummy variable, 82–86, 130, 134, 269

effective degrees of freedom, 278

elbow, 409

error

irreducible, 18, 32

rate, 37

reducible, 18

term, 16

Euclidean distance, 379, 387, 388, 394, 396–398, 416

expected value, 19

exploratory data analysis, 374

F-statistic, 75

factor, 84

false discovery proportion, 147

false negative, 147

false positive, 147

false positive rate, 147, 149, 354

feature, 15

feature selection, 204

Fisher’s linear discriminant, 141

fit, 21

fitted value, 93

flexible, 22

for loop, 193

forward stepwise selection, 78, 207–208, 247

function, 42

Gaussian (normal) distribution, 138, 139, 142–143

generalized additive model, 6, 26, 265, 266, 282–287, 294

generalized linear model, 6, 156, 192

Gini index, 311–312, 319, 332

Heart data set, 312, 313, 317–320, 354, 35

heatmap, 47

heteroscedasticity, 95–96

hierarchical clustering, 390–396

dendrogram, 390–394

inversion, 395

linkage, 394–396

hierarchical principle, 89

high-dimensional, 78, 208, 239

hinge loss, 357

histogram, 50

Hitters data set, 14, 244, 251, 255, 256, 304, 305, 310, 311, 334

hold-out set, 176

hyperplane, 338–343

hypothesis test, 67–68, 75, 95

Income data set, 16–18, 22–24

independent variable, 15

indicator function, 268

inference, 17, 19

inner product, 351

input variable, 15

integral, 278

interaction, 60, 81, 87–90, 104, 286

intercept, 61, 63

interpretability, 203

inversion, 395

irreducible error, 18, 39, 82, 103

K-means clustering, 12, 386–389

K-nearest neighbors classifier, 12, 38–40, 127 regression, 104–109

kernel, 350–353, 356, 367

linear, 352

non-linear, 349–353

polynomial, 352, 354

radial, 352–354, 363

kernel trick, 351

Khan data set, 14, 366

knot, 266, 271, 273–275

Laplace distribution, 227

lasso, 12, 25, 219–227, 241–242, 309, 357

leaf, 305, 391

least squares, 6, 21, 61–63, 133, 203

line, 63

weighted, 96

level, 84

leverage, 97–99

likelihood function, 133

linear, 2, 86

linear combination, 121, 204, 229, 375

linear discriminant analysis, 6, 12, 127, 130, 138–147, 348, 354

linear kernel, 352

linear model, 20, 21, 59

linear regression, 6, 12

multiple, 71–82

simple, 61–71

linkage, 394–396, 410

average, 394–396

centroid, 394–396

complete, 391, 394–396

single, 394–396

local regression, 266, 294

logistic

function, 132

logistic regression, 6, 12, 26, 127, 131–137, 286–287, 349, 356–357

multiple, 135–137

logit, 132, 286, 291

loss function, 277, 357

low-dimensional, 238

main effects, 88, 89

majority vote, 317

Mallow’s Cp, 78, 205, 206, 210–213

margin, 341, 357

matrix multiplication, 12

maximal margin classifier, 337–343 hyperplane, 341

maximum likelihood, 132–133, 135

mean squared error, 29

misclassification error, 37

missing data, 49

mixed selection, 79

model assessment, 175

model selection, 175

multicollinearity, 243

multivariate Gaussian, 142–143

multivariate normal, 142–143

natural spline, 274, 278, 293

NCI60 data set, 4, 5, 14, 407, 409–412

negative predictive value, 147, 149

node

internal, 305

purity, 311–312

terminal, 305

noise, 22, 228

non-linear, 2, 12, 265–301

decision boundary, 349–353

kernel, 349–353

non-parametric, 21, 23–24, 104–109, 168

normal (Gaussian) distribution, 138, 139, 142–143

null, 145

hypothesis, 67

model, 78, 205, 220

odds, 132, 170

OJ data set, 14, 334, 371

one-standard-error rule, 214

one-versus-all, 356

one-versus-one, 355

optimal separating hyperplane,341

optimism of training error, 32

ordered categorical variable, 292

orthogonal, 233, 377

basis, 288

out-of-bag, 317–318

outlier, 96–97

output variable, 15

overfitting, 22, 24, 26, 32, 80, 144, 207, 341

p-value, 67–68, 73

parameter, 61

parametric, 21–23, 104–109

partial least squares, 12, 230, 237–238, 258, 259

path algorithm, 224

perpendicular, 233

polynomial

kernel, 352, 354

regression, 90–92, 265–268, 271

population regression line, 63

Portfolio data set, 14, 194

positive predictive value, 147, 149

posterior

distribution, 226

mode, 226

probability, 139

power, 101, 147

precision, 147

prediction, 17

interval, 82, 103

predictor, 15

principal components, 375

analysis, 12, 230–236, 374–385

loading vector, 375, 376

proportion of variance explained, 382–384, 408

regression, 12, 230–236, 256–257, 374–375, 385

score vector, 376

scree plot, 383–384

prior

distribution, 226

probability, 138

projection, 204

pruning, 307–309

cost complexity, 307–309

weakest link, 307–309

quadratic, 91

quadratic discriminant analysis, 4, 149–150

qualitative, 3, 28, 127, 176

variable, 82–86

quantitative, 3, 28, 127, 176

R functions

x2, 125 2

abline(), 112, 122, 301, 412

anova(), 116, 290, 291

apply(), 250, 401

as.dist(), 407

as.factor(), 50

attach(), 50

biplot(), 403

boot(), 194–196, 199

bs(), 293, 300

c(), 43

cbind(), 164, 289

coef(), 111, 157, 247, 251

confint(), 111

contour(), 46

contrasts(), 118, 157

cor(), 44, 122, 155, 416

cumsum(), 404

cut(), 292

cutree(), 406

cv.glm(), 192, 193, 199

cv.glmnet(), 254

cv.tree(), 326, 328, 334

data.frame(), 171, 201, 262, 324

dev.off(), 46

dim(), 48, 49

dist(), 406, 416

fix(), 48, 54

for(), 193

gam(), 284, 294, 296

gbm(), 330

glm(), 156, 161, 192, 199, 291

glmnet(), 251, 253–255

hatvalues(), 113

hclust(), 406, 407

hist(), 50, 55

I(), 115, 289, 291, 296

identify(), 50

ifelse(), 324

image(), 46

importance(), 330, 333, 334

is.na(), 244

jitter(), 292

jpeg(), 46

kmeans(), 404, 405

knn(), 163, 164

lda(), 161, 163

legend(), 125

length(), 43

library(), 109, 110

lines(), 112

lm(), 110, 112, 113, 115, 116, 121, 122, 156, 161, 191, 192, 254, 256, 288, 294, 324

lo(), 296

loadhistory(), 51

loess(), 294

ls(), 43

matrix(), 44

mean(), 45, 158, 191, 401

median(), 171

model.matrix(), 251

na.omit(), 49, 244

names(), 49, 111

ns(), 293

pairs(), 50, 55

par(), 112, 289

pcr(), 256, 258

pdf(), 46

persp(), 47

plot(), 45, 46, 49, 55, 112, 122, 246, 295, 325, 360, 371, 406, 408

plot.gam(), 295

plot.svm(), 360

plsr(), 258

points(), 246

poly(), 116, 191, 288–290, 299

prcomp(), 402, 403, 416

predict(), 111, 157, 161–163, 191, 249, 250, 252, 253, 289, 291, 292, 296, 325, 327, 361, 364, 365

print(), 172

prune.misclass(), 327

prune.tree(), 328

q(), 51

qda(), 163

quantile(), 201

rainbow(), 408

randomForest(), 329

range(), 56

read.csv(), 49, 54, 418

read.table(), 48, 49

regsubsets(), 244–249, 262

residuals(), 112

return(), 172

rm(), 43

rnorm(), 44, 45, 124, 262, 417

rstudent(), 112

runif(), 417

s(), 294

sample(), 191, 194, 414

savehistory(), 51

scale(), 165, 406, 417

sd(), 45

seq(), 46

set.seed(), 45, 191, 405

smooth.spline(), 293, 294

sqrt(), 44, 45

sum(), 244

summary(), 51, 55, 113, 121, 122, 157, 196, 199, 244, 245, 256, 257, 295, 324, 325, 328, 330, 334, 360, 361, 363, 372, 408

svm(), 359–363, 365, 366

table(), 158, 417

text(), 325

title(), 289

tree(), 304, 324

tune(), 361, 364, 372

update(), 114

var(), 45

varImpPlot(), 330

vif(), 114

which.max(), 113, 246

which.min(), 246

write.table(), 48

radial kernel, 352–354, 363

random forest, 12, 303, 316, 320–321, 328–330

recall, 147

receiver operating characteristic (ROC), 147, 354–355

recursive binary splitting, 306, 309, 311

reducible error, 18, 81

regression, 3, 12, 28–29

local, 265, 266, 280–282

piecewise polynomial, 271

polynomial, 265–268, 276–277

spline, 266, 270, 293

tree, 304–311, 327–328

regularization, 204, 215

replacement, 189

resampling, 175–190

residual, 62, 72

plot, 92

standard error, 66, 68–69, 79–80, 102

studentized, 97

sum of squares, 62, 70, 72

residuals, 239, 322

response, 15

ridge regression, 12, 215–219, 357

robust, 345, 348, 400

ROC curve, 147, 354–355

rug plot, 292

scale equivariant, 217

scatterplot, 49

scatterplot matrix, 50

scree plot, 383–384, 409

elbow, 384

seed, 191

semi-supervised learning, 28

sensitivity, 145, 147

separating hyperplane, 338–343

shrinkage, 204, 215

penalty, 215

signal, 228

slack variable, 346

slope, 61, 63

Smarket data set, 3, 14, 154, 161, 163, 171

smoother, 286

smoothing spline, 266, 277–280, 293

soft margin classifier, 343–345

soft-thresholding, 225

sparse, 219, 228

sparsity, 219

specificity, 145, 147, 148

spline, 265, 271–280

cubic, 273

linear, 273

natural, 274, 278

regression, 266, 271–277

smoothing, 31, 266, 277–280

thin-plate, 23

standard error, 65, 93

standardize, 165

statistical model, 1

step function, 105, 265, 268–270

stepwise model selection, 12, 205, 207

stump, 323

subset selection, 204–214

subtree, 308

supervised learning, 26–28, 237

support vector, 342, 347, 357

classifier, 337, 343–349

machine, 12, 26, 349–359

regression, 358

synergy, 60, 81, 87–90, 104

systematic, 16

t-distribution, 67, 153

t-statistic, 67

test

error, 37, 40, 158

MSE, 29–34

observations, 30

set, 32

time series, 94

total sum of squares, 70

tracking, 94

train, 21

training

data, 21

error, 37, 40, 158

MSE, 29–33

tree, 303–316

tree-based method, 303

true negative, 147

true positive, 147

true positive rate, 147, 149, 354

truncated power basis, 273

tuning parameter, 215

Type I error, 147

Type II error, 147

unsupervised learning, 26–28, 230, 237, 373–413

USArrests data set, 14, 377, 378, 381–383

validation set, 176

approach, 176–178

variable, 15

dependent, 15

dummy, 82–86, 89–90

importance, 319, 330

independent, 15

indicator, 37

input, 15

output, 15

qualitative, 82–86, 89–90

selection, 78, 204, 219

variance, 19, 33–36

inflation factor, 101–103, 114

varying coefficient model, 282

vector, 43

Wage data set, 1, 2, 9, 10, 14,

267, 269, 271, 272,

274–277, 280, 281, 283,

284, 286, 287, 299

weakest link pruning, 308

Weekly data set, 14, 171, 200

weighted least squares, 96, 282

within class covariance, 143

workspace, 51

wrapper, 289