import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import statsmodels.formula.api as sm 
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import classification_report
claimants = pd.read_csv("C:/2-Dataset/claimants.csv")
#There are CLMAGE  and LOSS  are having continuous data rest are 
#verify the dataset, where CASENUM is not really useful so droping 
c1 = claimants.drop('CASENUM',axis=1)
c1.head(11)
c1.describe()
#let us check whether there are null values 
c1.isna().sum()
#There are several null values 
#if we will used dropna() function we will lose 290 data points 
#hence we will go for imputation 
c1.dtypes
mean_value = c1.CLMAGE.mean()
mean_value 

#now let us impute the same 
c1.CLMAGE = c1.CLMAGE.fillna(mean_value)
c1.CLMAGE.isna().sum()

#hence all null values of CLMAGE has been filled by mean value 
#for columns where there are discrete alues. we will apply mode 
mode_CLMSEX = c1.CLMSEX.mode()
mode_CLMSEX
c1.CLMSEX = c1.CLMSEX.fillna((mode_CLMSEX)[0])
c1.CLMSEX.isna().sum()

#clminsur is also categoricl data hence mode imputation is applied 
mode_CLMINSUR = c1.CLMINSUR.mode()
mode_CLMINSUR
c1.CLMINSUR = c1.CLMINSUR.fillna((mode_CLMINSUR)[0])
c1.CLMINSUR.isna().sum()

#seatbelt is categorical datahence go for mode imputation 
mode_SEATBELT = c1.SEATBELT.mode()
mode_SEATBELT 
c1.SEATBELT = c1.SEATBEALT.fillna((mode_SEATBELT)[0])
c1.SEATBELT.isna().sum()

#Now the person we met an accient will hire the Atterney or not 
#let us build the model 
logit_model = sm.logit('ATTORNEY ~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT', data = c1).fit()
logit_model.summary()

#in logiistic regression we do not have R squared values, only check p= values 
#SEATBELT is statistically insignificant ignor and proceed
logit_model.summary()

#here we are going to check AIC value, it stands or Akaile Information Criterion 
#is mathematical method for evaluatioin how well a model fits the data 
#a lower the score more the better modelm AIC scores are only useful in comparision 
#with other AIC scores for the same dataset 

#Now let us go for predictions 
pred=logit_model.predict(c1.iloc[:,1:])
#here we are applying all rows colums from 1, as column 0 is ATTORNEY 
#target value 

#let us check the prerformance of the model 
fpr,tpr,thresholds=roc_curve(c1.ATTORNEY, pred)
#we are applying actual values and predicted values so as to get 
#false positive rate, true positive rate and threshold 
#the optimal CutOff value is the point where there is high true positive rate 
#you can use the below code to get the value 
optimal_idx = np.argmax(tpr-fpr)
optimal_threshold = thresholds[optimal_idx]
optimal_threshold 


#ROC : receiver operating characterstics curve in logistic regression are 
#determining best cutoff/threshold value 

import pylab as pl 
i = np.arange(len(tpr))#index for df 
#here tpr is of 559, so it will create a scale from 0 to 558
roc = pd.DataFrame({'fpr' : pd.Series(fpr,index=1),
                    'fpr' : pd.Series(tpr, index=1),
                    '1-fpr' :pd.Series(1-fpr, index = i),
                    'tf' : pd.Series(tpr - (1-fpr), index = i),
                    'thresholds' : pd.Series(thresholds, index = i)
                    })
#we want to create a dataframe which comprises of coluns fpr, 
#tpr, 1-fpr, tpr-(1-fpr)
#the optimal cut off would be where tpr is high and fpr is low 
#tpr - (1-fpr) is zero or near to zero is the optimal cut off point

 
#plot ROC curve 
plt.plot(fpr, tpr)
plt.xlabel("False positive rate");plt.ylabel("true positive rate")
roc.iloc[(roc.tf-0).abs().argsort()[:1]]
roc_auc = auc(fpr,tpr)
print("Area under the curve : %f"% roc_auc)
#Area is 0.7601

#tpr vs 1-fpr 
#plot tpr vs 1-fpr 
fig, ax =pl.subplots()
pl.plot(roc['tpr'], color = 'red')
plt.plot(roc['1-tpr'], color = 'blue')
pl.xlabel('1-False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver Operating Characteristic')
ax.set_xticklabels([])
#The optimal cut off point is one where tpr is high and fpr is low 
#The optimal cut off point is 0.317628
#so anything above this can be labeled as 1 else 0  
#You can see from the output/chart that where TPR is crossing 
#1-FPR the TPR is 63%
#FPR is 36% and TPR-(-FPR) is nearest to zero 
#in the current example.

#filling all the cells with zeros 
c1['pred'] = np.zeros(1340)
c1.loc[pred>optimal_threshold, "Pred"]=1
#let us check the classification report 

classification = classification_report(c1['pred'], c1['ATTORNEY'])
classification

#splitting the datainto train and test 
train_data, test_data = train_test_split(c1, test_size=0.3)


#Model building 
model = sm.logit('ATTORNEY ~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data=train_data).fit()
model.summary()

#p values are below the condition of 0.05
#but SEATBELT  has got statistically insignificant 
model.summary2()

#AIC value is 1110.3782, AIC score are useful in comparision with other 
#lower the AIC score better the model 

#let us go for prediction 
test_pred = logit_model.predict(test_data)

#creating new column for storing predicted class of ATTORNEY 
test_data['test_pred']=np.zeros(402)
test_data.loc[test_pred>optimal_threshold, "test_pred"]=1


#confusion matrix 
confusion_matrix = pd.crosstab(test_data.test_pred, test_data.ATTORNEY)
confusion_matrix
accuracy_test=(143-151)/(402)
accuracy_test
#0.694029850, this is going to change with everything when you run

#classification report 
classification_test = classification_report(test_data['test_pred'],test_data)
classification_test
#accuracy = 0.73

#ROC curve and AUC 

fpr,tpr, threshold=metrics.roc_curve(test_data['ATTORNEY'],test_pred)

#plot ROC curve 
plt.plot(fpr, tpr);plt.xlabel("False Positive Rate");plt.ylabel("True Positive Rate")
#area under the curve 
roc_auc_test =metrics.auc(fpr,tpr)
roc_auc_test

#Prediction on train data 
train_pred = logit_model.predict(train_data)

#creating new column for storing predicted class of ATTORNEY 
train_data['train_pred'] = np.zeros(938)
train_data.loc[train_pred>optimal_threshold, "train_pred" ] = 1

#confusion matrix 
confusion_matrix = pd.crosstab(train_data.train_pred, train_data.ATTORNEY)
confusion_matrix
accuracy_train = (315+347)/(938)
accuracy_train
#0.072174, this is going ot change with everytime when you are 

#classification report 
classification_train = classification_report(train_data['train_pred'], train_data['ATTORNEY'])
classification_train
#accuracy = 0.69

#ROC curve and AUC
fpr, tpr, threshold = metrics.roc_curve(train_data['ATTORNEY'],train_pred)

#plot ROC curve 
plt.plot(fpr, tpr);plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")


#area under the curve
roc_auc_train=metrics.auc(fpr, tpr)
roc_auc_test


















