#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

def clean_missing_values(df, num_strategy="median", cat_strategy="mode"):
    """
    
    :param df: 输入DataFrame
    :param num_strategy: 数值型缺失值处理方式（median/mean/drop）
    :param cat_strategy: 分类型缺失值处理方式（mode/drop）
    :return: 清洗后的DataFrame
    """
    
    num_cols = df.select_dtypes(include=[np.number]).columns
    if num_strategy == "median":
        df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    elif num_strategy == "mean":
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    elif num_strategy == "drop":
        df = df.dropna(subset=num_cols)
    
    
    cat_cols = df.select_dtypes(include=[object, "category"]).columns
    if cat_strategy == "mode":
        df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode()[0])
    elif cat_strategy == "drop":
        df = df.dropna(subset=cat_cols)
    
    return df

# 示例调用
# df = pd.DataFrame({"age": [25, np.nan, 30], "gender": ["M", np.nan, "F"]})
# cleaned_df = clean_missing_values(df)
# print(cleaned_df)


# In[ ]:




