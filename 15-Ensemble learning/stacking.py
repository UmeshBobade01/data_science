from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import model_selection
from mlxtend.classifier import StackingClassifier
import warnings
warnings.filterwarnings('ignore')
from sklearn import datasets

#splitting dataset
iris = datasets.load_iris()
X_train , Y_train = iris.data[:,1:3],iris.target

#weak learners modelbuilding
weak_l1 = KNeighborsClassifier(n_neighbors=1)
weak_l2 = RandomForestClassifier(random_state=1)
weak_l3 = GaussianNB()

#meta model bulding
meta_l = LogisticRegression()
stacking_clf = StackingClassifier(classifiers=[weak_l1,weak_l2,weak_l3],meta_classifier=meta_l)

#Three fold cross validation
print("After three fold cross validation")
for iterclf, iterlabel in zip([weak_l1, weak_l2, weak_l3, stacking_clf],['K-nearest Neighbours','Random Forest','Naive Bayes','Stacking Classifier']):
    scores = model_selection.cross_val_score(iterclf, X_train,Y_train,cv=3,scoring='accuracy')
    print('Accuracy:',scores.mean(),'for ',iterlabel)