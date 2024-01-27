# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 00:43:46 2024

@author: saicharan
"""

import json 
import requests 


url="http://127.0.0.1:8000/heart_disease_prediction"

# 50	0	2	120	219	0	1	158	0	1.6	1	0	2	



input_data_model={
"age" :50,
"sex":0,
"trestbps" :2,
"cp" :120,
"chol" :219,
"fbs":0,
"restecg" :1,
"thalach":158,
"exang" :0,
"oldpeak" :1.6,
"slope" :1,
"ca" :0,
"thal" :2
 }
    
input_json=json.dumps(input_data_model)
response=requests.post(url,data=input_json)
print(response.text)
