# -*- coding: utf-8 -*-
"""Heart disease prediction2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11F4WzcLUjeqSEt7YARI_Qh4unMVr6ciu
"""

# from google.colab import drive
# drive.mount('/content/drive')

#importing lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Loading the dataset
data=pd.read_csv('/content/drive/MyDrive/heart disease prediction using ml-data.csv')

data.head()

data.shape

data.columns

#Dropping the columns
data.drop(['id'],axis=1,inplace =True)

data.dtypes

data.info()

data.isnull().sum()

data['bmi']=data['bmi'].fillna(data['bmi'].mean())

data.isnull().sum()

#Visualizing the categorical columns
cat_cols=data.select_dtypes(exclude=np.number).columns
cat_cols

for col in cat_cols:
  plt.figure(figsize=(4,3))
  axis=data[col].value_counts().plot(kind='bar')
for i in axis.containers:
  axis.bar_label(i)
  plt.show()

#Numerical columns
num_cols=data.select_dtypes(include=np.number).columns
num_cols

num_cols=['age','avg_glucose_level','bmi']

#Numerical columns-Histogram
for col in num_cols:
  data[col].plot(kind='hist')
  plt.show()

#Numerical columns- Box plot
for col in num_cols:
  data[col].plot(kind='box')
  axis.bar_label(i)
  plt.show()

#Scatterplot -Correlation among numeric variables
plt.figure(figsize=(4,3))
sns.scatterplot(x='age',y='bmi',data=data)
plt.show()

plt.figure(figsize=(4,3))
sns.scatterplot(x='age',y='avg_glucose_level',data=data)
plt.show()

plt.figure(figsize=(4,3))
sns.scatterplot(x='bmi',y='avg_glucose_level',data=data)
plt.show()

#CORRELATION MATRIX
# Only include numerical features for correlation calculation
Cor_matrix = data[data.select_dtypes(include=np.number).columns].corr()
Cor_matrix

sns.heatmap(Cor_matrix,annot=True)

data.head()

#BALANCE THE DATA
#TARGET VARIABLE IS HEART DISEASE

data.shape

data.heart_disease.value_counts()

axis=data.heart_disease.value_counts().plot(kind='bar')
for i in axis.containers:
  axis.bar_label(i)
  plt.show()

heart_diseasedf=data[data.heart_disease==1]
heart_diseasedf.shape

no_heart_diseasedf=data[data.heart_disease==0]
no_heart_diseasedf.shape

#SELECTING THE AROUND 4000 RECORD

no_heart_diseasedf1=no_heart_diseasedf.sample(n=3800)
no_heart_diseasedf1.shape

#CREATING A NEW BALANCED DATASET
Data_new=pd.concat([heart_diseasedf,no_heart_diseasedf1])
Data_new.shape

axis=Data_new.heart_disease.value_counts().plot(kind='bar')
for i in axis.containers:
  axis.bar_label(i)
  plt.show()

#Feature Engineering
#LABEL ENCODING

#converting the categorical columns into numerical columns
cat_cols

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

# Assuming 'Data_new' is a subset or derived from 'data'and you want to apply the same Label Encoding

# Fit LabelEncoder on the 'gender' column of 'Data_new'
Data_new['gender'] = le.fit_transform(Data_new['gender'])

# Create the dictionary mapping for 'Data_new'
le_gender = dict(zip(le.classes_, le.transform(le.classes_)))

le_gender

Data_new['ever_married']=le.fit_transform(Data_new['ever_married'])
le_ever_married=dict(zip(le.classes_,le.transform(le.classes_)))
le_ever_married

Data_new['work_type']=le.fit_transform(Data_new['work_type'])
le_work_type=dict(zip(le.classes_,le.transform(le.classes_)))
le_work_type

Data_new['Residence_type']=le.fit_transform(Data_new['Residence_type'])
le_Residence_type=dict(zip(le.classes_,le.transform(le.classes_)))
le_Residence_type

Data_new['smoking_status']=le.fit_transform(Data_new['smoking_status'])
le_smoking_status=dict(zip(le.classes_,le.transform(le.classes_)))
le_smoking_status

Data_new.head()

#FEATURE SCALING
#bring all numerical variables on the same scale using standardization

num_cols

from sklearn.preprocessing import StandardScaler

std_scaler=StandardScaler()

Data_new['age']=std_scaler.fit_transform(Data_new[['age']])
Data_new['avg_glucose_level']=std_scaler.fit_transform(Data_new[['avg_glucose_level']])
Data_new['bmi']=std_scaler.fit_transform(Data_new[['bmi']])

Data_new.head()

#DEPENDENT (y)AND INDEPENDENT(X) VARIABLES

X=Data_new.drop(['heart_disease'],axis=1)
X.head()

y=Data_new['heart_disease']
y.head()

X,y #(X-independent variable,y-target or dependent variable)

#splitting into training and testing
from sklearn.model_selection import train_test_split

# Correctly assigning the result of train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

x_train.shape, x_test.shape

#model building
from sklearn.linear_model import LogisticRegression

log_reg=LogisticRegression()

#Model training
log_reg.fit(x_train,y_train)

#model prediction
y_pred=log_reg.predict(x_test)

#model evaluation
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

#Accuracy of the model
accuracy_score(y_test,y_pred)

#precision
precision_score(y_test,y_pred,zero_division=1)

#recall score
recall_score(y_test,y_pred)

#confusion matrix
conf_mat=confusion_matrix(y_test,y_pred)
conf_mat

sns.heatmap(conf_mat,annot=True)

print(classification_report(y_test,y_pred))



#Building multiple models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

#Buliding object of the model
log_reg_model=LogisticRegression()
Decision_tree_model=DecisionTreeClassifier()
svc_model=SVC()
Random_forest_model=RandomForestClassifier()
KNN_model=KNeighborsClassifier()

model_list=[log_reg_model,Decision_tree_model,svc_model,Random_forest_model,KNN_model]

#Logistic regression
accuracy_list=[]
model_name=[]
for model in model_list:
    model.fit(x_train,y_train)
    y_prediction=model.predict(x_test)
    accuracy=(accuracy_score(y_test,y_prediction))
    accuracy_list.append(accuracy)
    model_name.append(model.__class__.__name__)

model_dataframe=pd.DataFrame({'Model':model_name,'Accuracy':accuracy_list})
model_dataframe

#importing
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV

#parameters
parameters={
    'n_estimators':[50,100],
    'max_features':['sqrt','log2','None']
}

#creating object for grid search
grid_search=GridSearchCV(estimator=Random_forest_model,
                         param_grid=parameters)

#model fit
grid_search.fit(x_train,y_train)

#best parameters
grid_search.best_params_

#Building a new model
Random_forest_new=RandomForestClassifier(max_features='log2',n_estimators=100)

features = x_train
labels = y_train
CV = 5

#CROSS VALIDATION
Accuracy_cv=cross_val_score(Random_forest_new,
                            features,
                            labels,
                            scoring='accuracy',
                            cv=CV
                        )

#list of accuracies
Accuracy_cv

#Mean accuracy of the model
Mean_accuracy= Accuracy_cv.mean()
print(f"Mean Accuracy of the model= {round(Mean_accuracy*100,2)} %")

#Customizing prediction
Random_forest_new.fit(x_train,y_train)

X.head()

print("Enter Your Data to predict the probability:")
gender = int(input("Enter the Gender: "))
age = int(input("Enter the Age: "))
# Fit the scaler first, then transform
Age_scaled = std_scaler.fit_transform([[age]])[0][0]
hypertension = int(input("Enter the Hypertension: "))
Diabetes = int(input("Enter the Diabetes: "))
ever_married = int(input("Enter the Ever_married: "))
work_type = int(input("Enter the Work_type: "))
Residence_type = int(input("Enter the Residence_type: "))
avg_glucose_level = int(input("Enter the Avg_glucose_level: "))
# Fit the scaler first, then transform
avg_glucose_level_scaled = std_scaler.fit_transform([[avg_glucose_level]])[0][0]
bmi = int(input("Enter the BMI: "))
# Fit the scaler first, then transform
bmi_scaled = std_scaler.fit_transform([[bmi]])[0][0]
smoking_status = int(input("Enter the Smoking_status: "))

patients_data=[gender,Age_scaled,hypertension,Diabetes,ever_married,work_type,Residence_type,avg_glucose_level_scaled,bmi_scaled,smoking_status]
prob = Random_forest_new.predict_proba([patients_data])
heart_disease = prob[0][1]*100

print(f"Probability of having heart disease: {round(heart_disease,2)}%")

print("Enter Your Data to predict the probability:")
gender = int(input("Enter the Gender: "))
age = int(input("Enter the Age: "))
# Fit the scaler first, then transform
Age_scaled = std_scaler.fit_transform([[age]])[0][0]
hypertension = int(input("Enter the Hypertension: "))
Diabetes = int(input("Enter the Diabetes: "))
ever_married = int(input("Enter the Ever_married: "))
work_type = int(input("Enter the Work_type: "))
Residence_type = int(input("Enter the Residence_type: "))
avg_glucose_level = int(input("Enter the Avg_glucose_level: "))
# Fit the scaler first, then transform
avg_glucose_level_scaled = std_scaler.fit_transform([[avg_glucose_level]])[0][0]
bmi = int(input("Enter the BMI: "))
# Fit the scaler first, then transform
bmi_scaled = std_scaler.fit_transform([[bmi]])[0][0]
smoking_status = int(input("Enter the Smoking_status: "))

patients_data=[gender,Age_scaled,hypertension,Diabetes,ever_married,work_type,Residence_type,avg_glucose_level_scaled,bmi_scaled,smoking_status]
prob = Random_forest_new.predict_proba([patients_data])
heart_disease = prob[0][1]*100



from flask import Flask, request, jsonify
import joblib  # Or the library you used to save your model
import numpy as np

app = Flask(__name__)

# Load the model (adjust the filename as needed)
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([
        data['gender'], data['age'], data['hypertension'], data['diabetes'],
        data['ever_married'], data['work_type'], data['Residence_type'],
        data['avg_glucose_level'], data['bmi'], data['smoking_status']
    ]).reshape(1, -1)
    
    probability = model.predict_proba(features)[0][1] * 100
    return jsonify({'heart_disease_probability': probability})

if __name__ == '__main__':
    app.run(debug=True)