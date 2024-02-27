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
from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier(learning_rate=0.02,n_estimators=1000,max_depth=1)
gbc.fit(X_train,Y_train)

#evalution on testing data
from sklearn.metrics import accuracy_score, confusion_matrix
confusion_matrix(Y_test,gbc.predict(X_test))
accuracy_score(Y_test,gbc.predict(X_test))

#evalution on training data
from sklearn.metrics import accuracy_score, confusion_matrix
confusion_matrix(Y_train,gbc.predict(X_train))
accuracy_score(Y_train,gbc.predict(X_train))









































