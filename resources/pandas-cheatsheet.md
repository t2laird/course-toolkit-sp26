# Pandas Cheat Sheet

This resource summarizes common pandas operations used in data analysis.

## Common Operations
- Reading CSV files
- Selecting columns
- Filtering rows
- Groupby and aggregation

## Why Useful
Pandas is one of the most frequently used libraries in data science.
This cheat sheet helps beginners quickly recall syntax.
This document provides a quick reference for common pandas operations
used in data analysis.


```python
## Import pandas
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Inspect data
df.head()
df.info()
df.describe()

# Select columns
df["column_name"]
df[["col1", "col2"]]

# Filter rows
df[df["age"] > 30]

---
