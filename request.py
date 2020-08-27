# -*- coding: utf-8 -*-
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Pregnancies':10, 'Glucose':115, 'BloodPressure':70,'Insulin':96
                            ,'BMI':34.6,'DiabetesPedigreeFunction':0.526,'Age':60})

print(r.json())