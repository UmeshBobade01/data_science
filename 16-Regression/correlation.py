import pandas as pd
import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt

#import the data
data = pd.read_csv('C:/2-Dataset/SampleSuperstore.csv')
data

#calculating correelation using numpy
np.corrcoef(data['Profit'],data['Sales'])
"""array
([[1.        , 0.47906435],
  [0.47906435, 1.        ]])"""


#calculating coefficient using Scipy
st.pearsonr(data['Profit'],data['Sales'])
""" PearsonRResult(statistic=0.4790643497377062, pvalue=0.0) """


#understanding the correlation using scatterplot
sns.scatterplot(data['Sales'],data['Profit'])


#
sns.pairplot(data)

#
data.corr()
"""
Postal Code     Sales  Quantity  Discount    Profit
Postal Code     1.000000 -0.023854  0.012761  0.058443 -0.029961
Sales          -0.023854  1.000000  0.200795 -0.028190  0.479064
Quantity        0.012761  0.200795  1.000000  0.008623  0.066253
Discount        0.058443 -0.028190  0.008623  1.000000 -0.219487
Profit         -0.029961  0.479064  0.066253 -0.219487  1.000000"""


#
sns.heatmap(data.corr())


#
plt.figure(figsize=(15,8))
plt.subplot(231)
sns.scatterplot(data['Sales'],data['Profit'])
plt.subplot(232)
sns.scatterplot(data['Discount'],data['Profit'])
plt.subplot(233)
sns.scatterplot(data['Quantity'],data['Profit'])
plt.subplot(234)
sns.scatterplot(data['Discount'],data['Sales'])
plt.subplot(235)
sns.scatterplot(data['Discount'],data['Quantity'])


#
st.spearmanr(data['Sales'],data['Profit'])
""" SignificanceResult(statistic=0.5184066611400607, pvalue=0.0) """



















