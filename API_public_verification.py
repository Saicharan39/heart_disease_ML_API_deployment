# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:48:13 2024

@author: saicharan
"""
from fastapi import FastAPI 
from pydantic import BaseModel 
import pickle 
import json 
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#formant in which api considers data
class model_input(BaseModel):
    

    age :int
    sex:int
    trestbps :int
    cp :int
    chol :int
    fbs :int
    restecg :int
    thalach :int
    exang :int
    oldpeak :float
    slope :int
    ca :int
    thal :int
    
model=pickle.load(open('heart_disease_data.sav','rb'))
#file for data consideration

@app.post('/heart_disease_prediction')

def prediction(input_parameters : model_input):
    input_data=input_parameters.json() #api considers data in form of json
    input_dict=json.loads(input_data) #convert it into dictonary
    
    Age=input_dict['age']
    Sex=input_dict['sex']
    Trestbps=input_dict['trestbps']
    Cp=input_dict['cp']
    Chol = input_dict['chol']
    Fbs=input_dict['fbs']
    Restecg=input_dict['restecg']
    Thalach=input_dict['thalach']
    Exang=input_dict['exang']
    Oldpeak=input_dict['oldpeak']
    Slope=input_dict['slope']
    Ca=input_dict['ca']
    Thal=input_dict['thal']
    
    input_list=[Age,Sex,Trestbps,Cp,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]
    prediction=model.predict([input_list])
    if prediction[0]==0:
      return "no problem"
    else:
      return "heart problem"

