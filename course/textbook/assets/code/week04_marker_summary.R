# Week 04: R 基础语法、数据框操作与 AI 代码核验
# Teaching source code. It reads a small course dataset and prints a compact check.

data <- read.csv("../datasets/week04_marker_table.csv", stringsAsFactors = FALSE)
print(head(data))
print(summary(data))
