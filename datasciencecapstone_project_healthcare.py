# -*- coding: utf-8 -*-
"""DataScienceCapstone_Project_HealthCare

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DcFYMCs7_rgeb9zl_DN65nTBj70wtJJ0
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# %matplotlib inline

data = pd.read_csv('/content/health care diabetes.csv')

data.head(5)   #Printing First Five Rows

data.isnull().any() #Finding Null Values

data.info()   #Information of Dataset

Positive = data[data['Outcome']==1]    #selecting only positive Outcome Only
Positive.head(5)

data['Glucose'].value_counts().head()   #Getting count for Glucose Only

plt.hist(data['Glucose'])   # Histogram for Glucose

data['BloodPressure'].value_counts().head()  #Getting count for BloodPressure Only

plt.hist(data['BloodPressure'])         # Histogram for BloodPressure

data['SkinThickness'].value_counts().head()    #Getting count for SkinThickness Only

plt.hist(data['SkinThickness'])        # Histogram for SkinThickness

data['Insulin'].value_counts().head()     #Getting count for Insulin Only

plt.hist(data['Insulin'])         # Histogram for Insulin

data['BMI'].value_counts().head()     #Getting count for BMI Only

plt.hist(data['BMI'])       # Histogram for BMI

values = data.dtypes     #Assigning datatype tp values

sns.countplot(x = values , data = data, palette = "Set2")      #a count  plot describing the data types and the count of variables.

BloodPressure = Positive['BloodPressure']    #Selecting all Positive
Glucose = Positive['Glucose']
SkinThickness = Positive['SkinThickness']
Insulin = Positive['Insulin']
BMI = Positive['BMI']

plt.scatter(BloodPressure, Glucose, color=['b'])    #Scatter PLot for BloodPressure and glucose for Positive
plt.xlabel('BloodPressure')
plt.ylabel('Glucose')
plt.title('BloodPressure & Glucose')
plt.show()

"""======================================================================="""

g =sns.scatterplot(x= "Glucose" ,y= "BloodPressure",hue="Outcome",data=data);        #Scatter PLot for BloodPressure and glucose

"""=======================================================================

=======================================================================

=======================================================================

=======================================================================
"""

g =sns.scatterplot(x= "BMI" ,y= "Insulin",hue="Outcome",data=data);     #Scatter PLot for Insulin and BMI

"""=======================================================================

=======================================================================

=======================================================================
"""

g =sns.scatterplot(x= "SkinThickness" ,y= "Insulin",hue="Outcome",data=data);      #Scatter PLot for SkinThickness and Insulin

"""======================================================================="""

data.corr()     #Finding Correlation

"""======================================================================="""

sns.heatmap(data.corr())      #HeatMap for Correlation

"""=======================================================================

=======================================================================
"""

plt.subplots(figsize=(8,8))
sns.heatmap(data.corr(),annot=True,cmap='viridis')            #HeatMap using viridis

plt.subplots(figsize=(8,8))
sns.heatmap(data.corr(),annot=True)     #HeatMaps With Values

data.head(5)

features = data.iloc[:,[0,1,2,3,4,5,6,7]].values       #defining Features and Label
label = data.iloc[:,8].values

from sklearn.model_selection import train_test_split     #Splitting data into Training and testing
X_train , X_test , y_train , y_test =  train_test_split(features, label,test_size = 0.2 , random_state = 42)

from sklearn.linear_model import LogisticRegression    #Fitting LogisticRegression on Training Dataset
model = LogisticRegression()
model.fit(X_train, y_train)

print('The values for training data set is : ',model.score(X_train,y_train))
print('The values for testing data set is : ',model.score(X_test, y_test))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(label,model.predict(features))     #Using features for Confusion Matrix for prediction
f'The Confusion Matrix is : {cm}'

from sklearn.metrics import classification_report
print(classification_report(label,model.predict(features)))     #Using features for Classification Report  for prediction

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

probs = model.predict_proba(features)     #predicting probabilities
probs = probs[:, 1]   #for positive Outcome

auc = roc_auc_score(label, probs) #calculating AUC
print('AUC: %.3f' % auc)

fpr, tpr, thresholds = roc_curve(label, probs)  #calculating ROC

plt.plot([0, 1], [0, 1], linestyle='--')   #[0,1] Plot on graph using --
plt.plot(fpr, tpr, marker='.')   # ROC Curve

from sklearn.neighbors import KNeighborsClassifier   #Using KNeighbour Classifier
model2 = KNeighborsClassifier(n_neighbors=7,metric='minkowski',p = 2)
Ktrain = model2.fit(X_train,y_train)
Ktest = model2.fit(X_test , y_test)
f'Value using KNeighbour Classifier Classifer For Training is : {Ktrain} and For Testing is : {Ktest}'

from sklearn.tree import DecisionTreeClassifier   #Using DecisionTree Classifier
model3 = DecisionTreeClassifier(max_depth=5)
model3.fit(X_train,y_train)
Dtrain = model3.score(X_train,y_train)
Dtest = model3.score(X_test,y_test)
f'Value using DecisionTree Classifer For Training is : {Dtrain} and For Testing is : {Dtest}'

from sklearn.ensemble import RandomForestClassifier   #Using RandomForest Classifier
model4 = RandomForestClassifier(n_estimators=11)
model4.fit(X_train,y_train)
Rtrain = model4.score(X_train,y_train)
Rtest = model4.score(X_test,y_test)
f'Value using RandomForest Classifer For Training is : {Rtrain} and For Testing is : {Rtest}'

from sklearn.svm import SVC    #Using Support Vector Classifier
model5 = SVC(kernel='rbf',gamma='auto')
model5.fit(X_train,y_train)
Strain = model5.score(X_train,y_train)
Stest = model5.score(X_test,y_test)
f'Value using Support Vector Classifer For Training is : {Strain} and For Testing is : {Stest}'

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

probs = model2.predict_proba(features)
probs = probs[:, 1]

auc = roc_auc_score(label, probs)  # calculate AUC
print('AUC: %.3f' % auc)

fpr, tpr, thresholds = roc_curve(label, probs)# calculate roc curve
print("True Positive Rate - {}, False Positive Rate - {} Thresholds - {}".format(tpr,fpr,thresholds))

plt.plot([0, 1], [0, 1], linestyle='--')
plt.plot(fpr, tpr, marker='.')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

from sklearn.metrics import precision_recall_curve , f1_score , auc , average_precision_score  #For Logistic Regression

probs = model.predict_proba(features)
probs = probs[:, 1]
yhat = model.predict(features)
precision, recall, thresholds = precision_recall_curve(label, probs)
f1 = f1_score(label, yhat)
auc = auc(recall, precision)
ap = average_precision_score(label, probs)
print('f1=%.3f auc=%.3f ap=%.3f' % (f1, auc, ap))

plt.plot([0, 1], [0.5, 0.5], linestyle='--')
plt.plot(recall, precision, marker='.')

from sklearn.metrics import precision_recall_curve , f1_score , auc , average_precision_score
probs = model2.predict_proba(features)
probs = probs[:,1]
yhat = model2.predict(features)
precision, recall , thresholds = precision_recall_curve(label,probs)
f1 = f1_score(label,yhat)
auc = auc(recall, precision)
ap = average_precision_score(label,probs)
print('f1 = {} , AUC = {} , Average Precision = {}'.format(f1,auc,ap))

plt.plot([0,1],[0.5,0.5],linestyle = '--')
plt.plot(recall,precision , marker='.')

from sklearn.metrics import precision_recall_curve , f1_score , auc , average_precision_score  #For Logistic Regression
# Random Forest
probs = model4.predict_proba(features)
probs = probs[:, 1]
yhat = model4.predict(features)
precision, recall, thresholds = precision_recall_curve(label, probs)
f1 = f1_score(label, yhat)
auc = auc(recall, precision)
ap = average_precision_score(label, probs)
print('f1=%.3f auc=%.3f ap=%.3f' % (f1, auc, ap))

plt.plot([0, 1], [0.5, 0.5], linestyle='--')
plt.plot(recall, precision, marker='.')