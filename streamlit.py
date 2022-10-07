#Creating a Streamlit App
import streamlit as st
import pandas as pd
import numpy as np
import pickle


#Creating a Title and Subtitle
st.title("Weather Prediction App")
st.subheader("This app predicts the temperature of a city")

#Creating a Sidebar
st.sidebar.header("User Input Features")

#Loading the Model
load_model = pickle.load(open('model.pkl', 'rb'))

#Creating a Function that will get the user input features into the variable

percipitation = st.slider('percipitation', 0.0, 10.0, 5.0)
temp_max = st.slider('temp_max', 0.0, 100.0, 50.0)
temp_min = st.slider('temp_min', 0.0, 100.0, 50.0)
wind = st.slider('wind', 0.0, 100.0, 50.0)

#Creating a Dictionary that will store the user input features

user_data = {'percipitation': percipitation,
                'temp_max': temp_max,
                'temp_min': temp_min,
                'wind': wind}

#Transforming the data into a data frame

features = pd.DataFrame(user_data, index=[0])

#Displaying the user input features

#Create a button to predict the temperature

if st.button("Predict"):
    prediction = load_model.predict(features)
    st.subheader('Temperature')
    if prediction == 0:
        st.write('Cold')
    elif prediction == 1:
        st.write('Mild')
    else:
        st.write('Hot')

#Creating a Footer

st.subheader("By: Nithesh Kumar Manimaran")
