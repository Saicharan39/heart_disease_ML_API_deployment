import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn import svm 
import pickle

dataset=pd.read_csv('heart_disease_data.csv')
print(dataset.head())

print(dataset.groupby('target').mean())

x=dataset.drop('target',axis=1)
y=dataset['target']


scaler=StandardScaler()
scaler.fit(x)
tf_data=scaler.transform(x)
print(tf_data)

x_train,x_test,y_train,y_test=train_test_split(x,y,stratify=y,random_state=2)
classifier=svm.SVC(kernel='linear')
classifier.fit(x_train,y_train)
print("training accuracy")
y_pred=classifier.predict(x_train)
x_train_accuracy=accuracy_score(y_pred,y_train)
print(x_train_accuracy)
print("testing accuracy")
y_pred_test=classifier.predict(x_test)
x_test_accuracy=accuracy_score(y_pred_test,y_test)
print(x_test_accuracy)


#pickling file
"""
filename='heart_disease_data.sav'
pickle.dump(classifier,open(filename,'wb'))

loaded_model=pickle.load(open('heart_disease_data.sav','rb'))
            
patient_details=(54,0,2,135,304,1,1,170,0,0,2,0,2)
patient_list=np.asarray(patient_details)

reshaped=patient_list.reshape(1,-1)

std_data=scaler.transform(reshaped)

print(std_data)

result=classifier.predict(std_data)
print(result)


if result[0]==0:
    print("no problem")
else:
    print("heart problem")"""
"""   
for columns in dataset:
 
 print(columns,dataset[columns].dtype)
print(dataset.shape)"""


# ...

# Pickling file

# ...

# Importing warnings module
import warnings

# Suppressing the specific warning
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Loading the model
loaded_model = pickle.load(open('heart_disease_data.sav', 'rb'))

# Patient details for prediction
patient_details = (54, 0, 2, 135, 304, 1, 1, 170, 0, 0, 2, 0, 2)
patient_list = np.asarray(patient_details)

reshaped = patient_list.reshape(1, -1)

std_data = scaler.transform(reshaped)

# Making predictions
result = loaded_model.predict(std_data)
print(result)

if result[0] == 0:
    print("no problem")
else:
    print("heart problem")
