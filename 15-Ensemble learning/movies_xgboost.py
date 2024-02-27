import pandas as pd

df = pd.read_csv('C:/2-Dataset/movies_classification.csv')

#Dummy variables
df.head()
df.info()
df = pd.get_dummies(df,columns=['3D_available','Genre'],drop_first=True)
df.head()

#input and output split
predictors = df.loc[:,df.columns !='Start_Tech_Oscar']
type(predictors)
target = df['Start_Tech_Oscar']
type(target)
#splitting testing and training dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(predictors,target,test_size=0.2,random_state=0)

#model building
import xgboost as xgb
xgb_clf = xgb.XGBClassifier(max_depth = 5,learning_rate=0.3,n_estimators=10000,n_jobs = 1)
xgb_clf.fit(X_train,Y_train)

#evalution on testing data
from sklearn.metrics import accuracy_score, confusion_matrix
confusion_matrix(Y_test,xgb_clf.predict(X_test))
accuracy_score(Y_test,xgb_clf.predict(X_test))

#evalution on training data
confusion_matrix(Y_train,xgb_clf.predict(X_train))
accuracy_score(Y_train,xgb_clf.predict(X_train))

#hyperparameter tunning
xgb_clf = xgb.XGBClassifier(n_estimators=500,learning_rate=0.1,random_state=42)

param_test1 = {'max_depth': range(3,10,2), 'gamma': ([0.1,0.2,0.3]),
               'subsample': [0.8,0.9], 'colsample_bytree': [0.8,0.9],
               'rag_alpha':[1e-2,0.1,1]}


#grid search
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(xgb_clf, param_test1,n_jobs=1,cv=5,scoring='accuracy')
grid_search.fit(X_train,Y_train)
cv_xg_clf = grid_search.best_estimator_


#evaluation on testing data with model with hyperparameter
accuracy_score(Y_test, cv_xg_clf.predict(X_test))
grid_search.best_params_