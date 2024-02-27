import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:/2-Dataset/forestfires.csv')

df.dtypes

###############################################################################
"""EDA"""

df.shape
#(517, 31)

df.describe()

df.info()
#no null values present in the data


plt.figure(1,figsize=(16,10))
sns.countplot(df.month)
#August and September has highest value
sns.countplot(df.day)
#Friday, Saturday and Sunday has greater value

sns.distplot(df.FFMC)
#data isnormal and slight left skewed 
sns.boxplot(df.FFMC)
#There are several outliers

sns.distplot(df.DMC)
#data isnormal and slight right skewed 
sns.boxplot(df.DMC)
#There are several outliers 

sns.distplot(df.DC)
#data isnormal and slight left skewed 
sns.boxplot(df.DC)
#There are outliers

sns.distplot(df.ISI)
#data isnormal 
sns.boxplot(df.ISI)
#There are outliers 

sns.distplot(df.temp)
#data isnormal 
sns.boxplot(df.temp)
#there are outliers 

sns.distplot(df.RH)
#data isnormal and slightly right skewed
sns.boxplot(df.RH)
#there are outliers

sns.distplot(df.wind)
#data isnormal 
sns.boxplot(df.wind)
#there are outliers

sns.distplot(df.rain)
#data isnormal 
sns.boxplot(df.rain)
#there are outliers

sns.distplot(df.area)
#data isnormal 
sns.boxplot(df.area)
#there are outliers


df.sort_values(by='area',ascending=False).head()

highest_fire_area = df.sort_values(by='area',ascending=True)

plt.figure(figsize=(8,6))
plt.title('Temperature vs area of fire')
plt.bar(highest_fire_area['temp'],highest_fire_area['area'])
plt.xlabel('Temperature')
plt.ylabel('Area per km-sq')
plt.show()
"""once the fire starts in almost 1000+ sq-km area themn the temperature goes 
beyond the 25 and around 750 sq-km it hits the 30"""

#now let us check the highest rain in  the forest
highest_rain = df.sort_values(by='rain',ascending=False)[['month','day','rain']].head(5)
highest_rain

highest_temp = df.sort_values(by='temp',ascending=False)[['month','day','temp']].head(5)
highest_temp
#highest temp is observed in august

lowest_temp = df.sort_values(by='temp',ascending=True)[['month','day','temp']].head(5)
lowest_temp
#lowest temp is observed in december

###############################################################################

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df.month = le.fit_transform(df.month)
df.day = le.fit_transform(df.day)
df.size_category = le.fit_transform(df.size_category)

###############################################################################

#now rewmove the outliers using winsorizer
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['month'])
df_t = winsor.fit_transform(df[['month']])
sns.boxplot(df_t.month)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['day'])
df_t = winsor.fit_transform(df[['day']])
sns.boxplot(df_t.day)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['FFMC'])
df_t = winsor.fit_transform(df[['FFMC']])
sns.boxplot(df_t.FFMC)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['DMC'])
df_t = winsor.fit_transform(df[['DMC']])
sns.boxplot(df_t.DMC)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['DC'])
df_t = winsor.fit_transform(df[['DC']])
sns.boxplot(df_t.DC)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['ISI'])
df_t = winsor.fit_transform(df[['ISI']])
sns.boxplot(df_t.ISI)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['temp'])
df_t = winsor.fit_transform(df[['temp']])
sns.boxplot(df_t.temp)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['RH'])
df_t = winsor.fit_transform(df[['RH']])
sns.boxplot(df_t.RH)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['wind'])
df_t = winsor.fit_transform(df[['wind']])
sns.boxplot(df_t.wind)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['rain'])
df_t = winsor.fit_transform(df[['rain']])
sns.boxplot(df_t.rain)

winsor = Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['area'])
df_t = winsor.fit_transform(df[['area']])
sns.boxplot(df_t.area)

###############################################################################
tc=df.corr()
tc
fig,ax=plt.subplots()
fig.set_size_inches(200,10)
sns.heatmap(tc,annot=True, cmap='YlGnBu')
# all the varibles are moderaterly correlated with the size_category

###############################################################################
#model

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
train,test=train_test_split(df, test_size=0.3)
train_x=train.iloc[:,:30]
train_y=train.iloc[:,30]
test_x=test.iloc[:,:30]
test_y=test.iloc[:,30]

#kernel linear
model_linear = SVC(kernel='linear')
model_linear.fit(train_x,train_y)
pred_test_linear = model_linear.predict(test_x)
np.mean(pred_test_linear==test_y)

#RBF
model_rbf = SVC(kernel='rbf')
model_rbf.fit(train_x,train_y)
pred_test_rbf = model_linear.predict(test_x)
np.mean(pred_test_rbf==test_y)