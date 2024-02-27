""" SVD """

import numpy as np
from numpy import array
from scipy.linalg import svd

A =  array([[1,0,0,0,2],[0,0,3,0,0],[0,0,0,0,0],[0,4,0,0,0]])
print(A)

#SVD
u,d,vt = svd(A)
print(u)
print(d)
print(vt)
print(np.diag(d))

#applying SVD to a dataset
import pandas as pd
df = pd.read_excel("C:/2-Dataset/University_Clustering.xlsx")
df.head()
df = df.iloc[:,2:]
df

from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=3)
svd.fit(df)

result = pd.DataFrame(svd.transform(df))
result.head()
result.columns = "pc0","pc1","pc2"
result.head()

#scatter diagram
import matplotlib.pylab as plt

plt.scatter(x=result.pc0,y=result.pc1)
