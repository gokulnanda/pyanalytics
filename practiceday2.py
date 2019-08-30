# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:32:36 2019

@author: Gokul Nanda
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/duanalytics/datasets/master/csv/mtcars.csv')
df.columns
df.shape
df.describe
df.head()
catcolumns1 = ['cyl', 'vs', 'am', 'gear', 'carb'] #list
df[catcolumns1]=df[catcolumns1].astype('category')
df.dtypes
df[df['cyl']==8]
df[df['am']==0]
len(df.loc[df['am']==0])
df.head(2) #first two rows
df.iloc[0:2]
df.iloc[-1, 0:5]
df.iloc[0:3,0:5]
df.iloc[0::2, 0::2] #alternate rows
pip install pydataset
