import pandas as pd 
import numpy as np 

wcat = pd.read_csv("C:/2-Dataset/wc-at.csv")
wcat.head

#EDA
#1 Measure the central tendancy 
#2 Measures of dispersion 
#3 Third moment business decision 
#4 Fourth moment bussiness decision 
wcat.info()
wcat.describe()

#Graphical Representation 
import matplotlib.pyplot as plt
import seaborn as sns
plt.bar(height=wcat.AT, x=np.arange(1,110,1))
plt.hist(wcat.AT)
sns.distplot(wcat.AT)
#data is right skewed 

#scatter plot 
plt.scatter(x=wcat['Waist'],y=wcat['AT'],color='green')
#direction :postive, linearity : Moderate, Strength : poor 

#Now let us calculate correlation coeficient 
np.corrcoef(wcat.Waist, wcat.AT)

#let us check the direction using covar factor 
cov_output = np.cov(wcat.Waist, wcat.AT)[0,1]
cov_output
'''if value is ''' 

#Now let us apply to linear regression model 
import statsmodels.formula.api as smf 
'''all machine learning algo are implemented using sklearn; but for this statsmodel
Package is being used because it gives you backend calculation of bita-0 and bita-1'''

###############################################################################

#First Model
model =smf.ols('AT~Waist', data = wcat).fit()
model.summary()
'''OLS helps to find best fit model, which causes least square error. 
first you check R squared valued =0.670,
if R square = 0.8 means that model is strong corelation fit,
if R-square = 0.8 to 0.6 modetate fit.'''
#Next you chack P>|t|=0, it means less than alpha, 
#alpha is 0.0, Hence the model is accepted 

pred1 = model.predict(pd.DataFrame(wcat['Waist']))

#regeression line and scatter diagram 
plt.scatter(wcat.Waist, wcat.AT)
plt.plot(wcat.Waist, pred1, "r")
plt.show()

#error calculations 
res1 = wcat.AT-pred1
np.mean(res1)
#-6.779490322848662e-14
#it must be zero and here it is 10^-14=~0
res_sqr1 = res1*res1
mse1 = np.mean(res_sqr1)
rmse1 = np.sqrt(mse1)
rmse1 
#RMSE is 32.760177495755144
#lesser the value better the model

###############################################################################

#Second model
#How to improve this model 
plt.scatter(x=np.log(wcat['Waist']), y=wcat['AT'], color='brown')
np.corrcoef(np.log(wcat.Waist),wcat.AT)
# R value is 0.82 < 0.85 hence moderate linearity 
model2 =smf.ols('AT~np.log(Waist)', data = wcat).fit()
model2.summary()
#Again check the R - square value = 0.67 which is less than 0.8 
#p value is 0 less than 0.05

pred2 = model2.predict(pd.DataFrame(wcat['Waist']))
 
#regeression line and scatter diagram 
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist), pred2,"r")
plt.legend(['observed data', 'predicated line'])

#error calculations
res2 = wcat.AT-pred2
res_sqr2 = res2*res2
mse2 = np.mean(res_sqr2)
rmse2 = np.sqrt(mse2)
rmse2
#RMSE is 32.49688490932126
#there no considerable changes 
#Now let us change y value instead of x

###############################################################################

#Third Model
plt.scatter(x=wcat['Waist'],y=np.log(wcat['AT']),color='green')
np.corrcoef(wcat.Waist,np.log(wcat.AT))
#r value is 0.8409006 < 0.85 hence moderate linearity
model3 =  smf.ols('np.log(AT)~Waist', data=wcat).fit()
model3.summary()
#R-Square value = 0.707 which is less than 0.8 
#p value is 0.02 less than 0.05

pred3 = model3.predict(pd.DataFrame(wcat['Waist']))
pred3_at=np.exp(pred3)

#regeression line and scatter diagram 
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist, pred3, "r")
plt.legend(['observed data', 'predicated line'])
plt.show()

#error calculations
res3 = wcat.AT-pred3_at
res_sqr3 = res3*res3
mse3 = np.mean(res_sqr3)
rmse3 = np.sqrt(mse3)
rmse3
# RMSE is 38.52900175807141

###############################################################################

#Polynomial transformation 
model4 = smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
model4.summary()
#R-Square value = 0.779 which is less than 0.8 hence moderate linearity

pred4 = model4.predict(pd.DataFrame(wcat.Waist))
pred4
pred4_at = np.exp(pred4)
pred4_at

#regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred4,'r')
plt.legend(['Observed data','Predicted line'])
plt.show()

#error calculations
res4 = wcat.AT-pred4_at
res_sqr4 = res4*res4
mse4 = np.mean(res_sqr4)
rmse4 = np.sqrt(mse4)
rmse4
#RMSE is 32.244447827762265
#model4 has less RMSE than other models

###############################################################################

data = {'model':pd.Series(['SLR','Log_model','Poly_model'])}
data
table_rmse = pd.DataFrame(data)
table_rmse


from sklearn.model_selection import train_test_split
train, test = train_test_split(wcat,test_size=0.2)
plt.scatter(train.Waist,np.log(train.AT))
plt.scatter(test.Waist,np.log(test.AT))
final_model = smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
final_model.summary()
#R-squared error is 0.779 which is less than 0.85

#predict the result for testing data
test_pred = final_model.predict(pd.DataFrame(test))
test_pred_at = np.exp(test_pred)
test_pred_at

#predict the result for training data
train_pred = final_model.predict(pd.DataFrame(train))
train_pred_at = np.exp(train_pred)
train_pred_at

#evaluation for test data
test_err = test.AT-test_pred_at
test_sqr = test_err*test_err
test_mse = np.mean(test_sqr)
test_rsme =np.sqrt(test_mse)
test_rsme

#evaluation for train data
train_err = train.AT-train_pred_at
train_sqr = train_err*train_err
train_mse = np.mean(train_sqr)
train_rsme =np.sqrt(train_mse)
train_rsme

'''test_rmse < train_rmse'''