# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/2/17
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    sep=',')

df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
df.dropna(how="all",inplace=True)

print df.head()