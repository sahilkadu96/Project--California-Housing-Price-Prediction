import pickle 
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json


st.title('California Housing Prediction')


#opening model
with open(r'C:\Users\Sahil\.spyder-py3\california_housing\model.pkl', 'rb') as f:
    model = pickle.load(f)


#input variables
medinc = st.number_input('Enter MedInc', min_value = 0.0, max_value= 15.0, step=0.5)
houseage = st.number_input('Enter HouseAge', min_value= 1, max_value= 52, step=1)
averooms = st.number_input('Enter AveRooms', min_value=0.0, max_value = 142.0, step = 0.1)
avebdrms = st.number_input('Enter AveBdrms', min_value=0.0, max_value= 34.0, step = 0.1)
population = st.number_input('Enter Population', min_value=3, max_value = 35682, step = 1)
aveoccup = st.number_input('Enter AveOccup', min_value = 0.0, max_value = 1243.0, step = 0.5)
latitude = st.number_input('Enter Latitude', min_value = 32.0, max_value= 42.0, step=0.1)
longitude = st.number_input('Enter longitude', min_value = -124.0, max_value= -119.0, step = 0.1)



#Streamlit
if st.button('Predict price using Streamlit'):
    result = model.predict([[medinc, houseage, averooms, avebdrms, population, aveoccup, latitude, longitude]])
    st.write(f'The predicted price using Streamlit is {result[0]} ')



#Route the call to fastAPI
if st.button('Predict price using FastAPI'):
    inputs = {'medinc': medinc, 'houseage': houseage, 'averooms': averooms, 'avebdrms': avebdrms, 'population': population,
              'aveoccup': aveoccup, 'latitude': latitude, 'longitude': longitude}
    result = requests.post(url = 'http://127.0.0.1:8000/predict', data = json.dumps(inputs))
    st.write(f'The predicted price using FastAPI is {result.text}')


