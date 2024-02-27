import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

iris.feature_names
'''
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']'''

iris.target_names
'''['setosa', 'versicolor', 'virginica']'''

df = pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()

df['target'] = iris.target
df.head()

df[df.target==1].head()
df[df.target==2].head()
df[df.target==0].head()

df['flower_name'] = df.target.apply(lambda x:iris.target_names[x])
df.head()

df[45:55]

#serperate the datafframe
df0 = df[:50]
df1 = df[50:100]
df2 = df[100:]


import matplotlib.pyplot as plt

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color='green',marker='+')
plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color='red',marker='.')


plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'],color='green',marker='+')
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color='red',marker='.')


#train using SVM

from sklearn.model_selection import train_test_split
X = df.drop(['target','flower_name'],axis=1)
Y = df.target

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)


from sklearn.svm import SVC
model = SVC()

model.fit(X_train,Y_train)

model.score(X_test,Y_test)

model.predict([[4.8,3.0,1.5,0.3]])


#tunning parameter

#1. regularization (C)
model_C = SVC(C=1)
model_C.fit(X_train,Y_train)
model_C.score(X_test,Y_test)

#2. Gamma
model_g = SVC(gamma=1)
model_g.fit(X_train,Y_train)
model_g.score(X_test,Y_test)

#3. Kernel
model_k = SVC(kernel='linear')
model_k.fit(X_train,Y_train)
model_k.score(X_test,Y_test)