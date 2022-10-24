import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import sklearn as sklearn
import pickle

#image = Image.open("img.jpg")
#st.image(image,width=100)
st.title('Churn Prediction')

mlmodel = st.sidebar.selectbox('Please select the maschine learning model',['GradBoost','KNN','KMeans','RandomForest'])

if mlmodel=="KNN":
    st.header("KNN Information")
    st.text ("Sadece dinle")
    st.sidebar.number_input("TV:",value=230, step=10)

    satisfaction_level = st.sidebar.slider('Select satisfaction_level',0,100,1,1)/100

    last_evaluation = st.sidebar.slider('Select last_evaluation',0,100,1,1)/100

    time_spend_company = st.sidebar.slider('Select time_spend_company',1,15,1,1)

    number_project = st.sidebar.slider('Select number_project',1,10,1,1)

    average_montly_hours=st.sidebar.slider('Select average_montly_hours',50,400,1,1)

    my_dict = {
        "satisfaction_level": satisfaction_level,
        "last_evaluation": last_evaluation,
        "number_project": number_project,
        "average_montly_hours": average_montly_hours,
        "time_spend_company": time_spend_company
    }

    my_dict = pd.DataFrame([my_dict])


    columns=['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company']

    my_dict_dummy = pd.get_dummies(my_dict).reindex(columns=columns, fill_value=0)
    final_scaler = pickle.load(open('scaler_knn.pkl', "rb"))
    my_dict_scaled = final_scaler.transform(my_dict_dummy)
    filename = "final_model_knn.pkl"
    model = pickle.load(open(filename, "rb"))
    pred = model.predict(my_dict_scaled)
    x=pred[0]
    x=x.astype(int)
    st.success(x)

elif mlmodel=="RandomForest":
    st.header("Random Forest Information")
    st.text ("Random dinle")

    satisfaction_level = st.sidebar.slider('Select satisfaction_level',0,100,1,1)/100

    last_evaluation = st.sidebar.slider('Select last_evaluation',0,100,1,1)/100

    time_spend_company = st.sidebar.slider('Select time_spend_company',1,15,1,1)

    number_project = st.sidebar.slider('Select number_project',1,10,1,1)

    average_montly_hours=st.sidebar.slider('Select average_montly_hours',50,400,1,1)

    my_dict = {
        "satisfaction_level": satisfaction_level,
        "last_evaluation": last_evaluation,
        "number_project": number_project,
        "average_montly_hours": average_montly_hours,
        "time_spend_company": time_spend_company
    }

    my_dict = pd.DataFrame([my_dict])


    columns=['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company']

    my_dict_dummy = pd.get_dummies(my_dict).reindex(columns=columns, fill_value=0)
    final_scaler = pickle.load(open('scaler_rf.pkl', "rb"))
    my_dict_scaled = final_scaler.transform(my_dict_dummy)
    filename = "final_model_rf.pkl"
    model = pickle.load(open(filename, "rb"))
    pred = model.predict(my_dict_scaled)
    x=pred[0]
    x=x.astype(int)
    st.success(x)

elif mlmodel=="GradBoost":
    st.header("Gradient Boosting Information")
    st.text("Deneme")

    satisfaction_level = st.sidebar.slider('Select satisfaction_level',0,100,1,1)/100

    last_evaluation = st.sidebar.slider('Select last_evaluation',0,100,1,1)/100

    time_spend_company = st.sidebar.slider('Select time_spend_company',1,15,1,1)

    number_project = st.sidebar.slider('Select number_project',1,10,1,1)

    average_montly_hours=st.sidebar.slider('Select average_montly_hours',50,400,1,1)

    my_dict = {
        "satisfaction_level": satisfaction_level,
        "last_evaluation": last_evaluation,
        "number_project": number_project,
        "average_montly_hours": average_montly_hours,
        "time_spend_company": time_spend_company
    }

    my_dict = pd.DataFrame([my_dict])


    columns=['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company']

    my_dict_dummy = pd.get_dummies(my_dict).reindex(columns=columns, fill_value=0)
    final_scaler = pickle.load(open('scaler_grad.pkl', "rb"))
    my_dict_scaled = final_scaler.transform(my_dict_dummy)
    filename = "final_model_grad.pkl"
    model = pickle.load(open(filename, "rb"))
    pred = model.predict(my_dict_scaled)
    x=pred[0]
    x=x.astype(int)
    st.success(x)
elif mlmodel=="KMeans":
    st.header("KMeans Information")
    st.text("Deneme")

    satisfaction_level = st.sidebar.slider('Select satisfaction_level',0,100,1,1)/100

    last_evaluation = st.sidebar.slider('Select last_evaluation',0,100,1,1)/100

    time_spend_company = st.sidebar.slider('Select time_spend_company',1,15,1,1)

    number_project = st.sidebar.slider('Select number_project',1,10,1,1)

    average_montly_hours=st.sidebar.slider('Select average_montly_hours',50,400,1,1)

    my_dict = {
        "satisfaction_level": satisfaction_level,
        "last_evaluation": last_evaluation,
        "number_project": number_project,
        "average_montly_hours": average_montly_hours,
        "time_spend_company": time_spend_company
    }

    my_dict = pd.DataFrame([my_dict])


    columns=['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company']

    my_dict_dummy = pd.get_dummies(my_dict).reindex(columns=columns, fill_value=0)
    final_scaler = pickle.load(open('scaler_grad.pkl', "rb"))
    my_dict_scaled = final_scaler.transform(my_dict_dummy)
    filename = "final_model_grad.pkl"
    model = pickle.load(open(filename, "rb"))
    pred = model.predict(my_dict_scaled)
    x=pred[0]
    x=x.astype(int)
    st.success(x)










