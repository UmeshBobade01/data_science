import pandas as pd
import numpy as np
import seaborn as sns

cars = pd.read_csv('C:/2-Dataset/Cars.csv')

#######################################################################

#Exploratory Data Analysis
#1. Measure the central tendency
#2. Measure the dispersion
#3. Third moment Business Decision
#4. Fourth moment Business Decision
#5. Probability Distribution
#6. 

cars.describe()

######################################################################

#Graphical representation
import matplotlib.pyplot as plt
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)
#data is right Skewed
plt.boxplot(cars.HP)
#There are several outliers in HP column
#similar operations are expected for the remaining columns

sns.distplot(cars.MPG)
#data is slightly left Skewed
plt.boxplot(cars.MPG)
#no outliers

sns.distplot(cars.VOL)
#data is right Skewed
plt.boxplot(cars.VOL)
#there are some outliers

sns.distplot(cars.SP)
#data is right Skewed
plt.boxplot(cars.SP)
#there are some outliers

sns.distplot(cars.WT)
#data is right Skewed
plt.boxplot(cars.WT)
#there are some outliers


sns.jointplot(x=cars['HP'],y=cars['MPG'])

#now let us plot count plot
plt.figure


#QQplot
from scipy import stats
import pylab
stats.probplot(cars.MPG,dist='norm',plot=pylab)
plt.show()
#MPG data is normally distributed

stats.probplot(cars.VOL,dist='norm',plot=pylab)
plt.show()
#

stats.probplot(cars.SP,dist='norm',plot=pylab)
plt.show()
#

stats.probplot(cars.WT,dist='norm',plot=pylab)
plt.show()
#

sns.pairplot(cars.iloc[:,:])

cars.corr()
#correlation between WT and VOL is 0.99
#correlation between SP and HP is 0.97

import statsmodels.formula.api as smf
m1 = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()
m1.summary()
#R-squared value is observed as 0.771 which is less than 0.85
#p-value of WT and VOL is greater than 0.05 thus need to ignore or delete these columns


import statsmodels.api as sm
sm.graphics.influence_plot(m1)
#76 is the value which got outliers so go to dataframe and check 76th entry
#let us delete this entry
cars_new = cars.drop(cars.index[[76]])

#again apply regression to cars_new
m1_new = smf.ols('MPG~WT+VOL+SP+HP',data=cars_new).fit()
m1_new.summary()
#R-squared value is 0.819 but p-value are same

rsq_hp = smf.ols('HP~WT+VOL+SP',data=cars).fit().rsquared
vif_hp = 1/(1-rsq_hp)
vif_hp
#19.92658897499852

rsq_wt = smf.ols('WT~HP+VOL+SP',data=cars).fit().rsquared
vif_wt = 1/(1-rsq_wt)
vif_wt
#639.5338175572624

rsq_vol = smf.ols('VOL~WT+HP+SP',data=cars).fit().rsquared
vif_vol = 1/(1-rsq_vol)
vif_vol
#638.8060836592878

rsq_sp = smf.ols('SP~WT+VOL+HP',data=cars).fit().rsquared
vif_sp = 1/(1-rsq_sp)
vif_sp
#20.00763878305008

#vif_wt is greater,therefore the WT column should be deleted

final_ml = smf.ols('MPG~VOL+HP+SP',data=cars).fit()
final_ml.summary()
#R-squared value is 0.770<0.85 and p-values are less than 0.05

pred = final_ml.predict(cars)

#QQplot
res = final_ml.resid
sm.qqplot(res)
plt.show()
#
stats.probplot(res,dist='norm',plot=pylab)
plt.show()

#let us plot the residual plot, which takes the residuals and data
sns.residplot(x=pred,y=cars.MPG,lowess=True)
plt.xlabel('Fitted')
plt.ylabel('Residual')
plt


from sklearn.model_selection import train_test_split
train, test = train_test_split(cars,test_size=0.2)

model_train = smf.ols('MPG~VOL+HP+SP',data=cars).fit()




