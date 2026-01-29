# Pandas Cheat Sheet

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
