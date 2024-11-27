# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:21:34 2024

@author: punit
"""

import os
import pickle
import streamlit as st
import joblib
import numpy as np

from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('C:/Users/om/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/om/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/om/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))
kidney_model = joblib.load('C:/Users/om/Desktop/Multiple Disease Prediction System/saved models/kidney.sav')

lung_cancer_model = joblib.load('C:/Users/om/Desktop/Multiple Disease Prediction System/saved models/lung_cancer_model.sav')



# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            "Parkinson's Prediction",
                            'Kidney Disease Prediction',
                            "Lung Cancer Prediction"],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'kidney','Lung'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Prediction code
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Prediction code
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Prediction code
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)

# Kidney Disease Prediction Page
if selected == 'Kidney Disease Prediction':
    st.title('Kidney Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Blood pressure')
    with col3:
        cp = st.text_input('specific gravity')
    with col1:
        trestbps = st.text_input('albumin')
    with col2:
        chol = st.text_input('sugar')
    with col3:
        fbs = st.text_input('red blood cell')
    with col1:
        restecg = st.text_input('pus cell')
    with col2:
        thalach = st.text_input('blood glucose random')
    with col3:
        exang = st.text_input('blood urea')
    with col1:
        oldpeak = st.text_input('syrum')
    with col2:
        slope = st.text_input('sodium')
    with col3:
        ca = st.text_input('potassium')
    with col1:
        thal = st.text_input('Himoglobin')

    # Prediction code
    kidney_diagnosis = ''
    if st.button('Kidney Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        kidney_prediction = kidney_model.predict([user_input])
        if kidney_prediction[0] == 1:
            kidney_diagnosis = 'The person is having kidney disease'
        else:
            kidney_diagnosis = 'The person does not have any kidney disease'
    st.success(kidney_diagnosis)
    




# Lung Cancer Prediction Page
if selected == 'Lung Cancer Prediction':
    st.title('Lung Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0)
    with col2:
        gender = st.selectbox('Gender', ['Male', 'Female'])
    with col3:
        smoking = st.selectbox('Smoking Status', ['Yes', 'No'])
    
    with col1:
        yellow_fingers = st.selectbox('Yellow Fingers', ['Yes', 'No'])
    with col2:
        anxiety = st.selectbox('Anxiety', ['Yes', 'No'])
    with col3:
        peer_pressure = st.selectbox('Peer Pressure', ['Yes', 'No'])
    
    with col1:
        chronic_disease = st.selectbox('Chronic Disease', ['Yes', 'No'])
    with col2:
        fatigue = st.selectbox('Fatigue', ['Yes', 'No'])
    with col3:
        allergy = st.selectbox('Allergy', ['Yes', 'No'])
    
    with col1:
        wheezing = st.selectbox('Wheezing', ['Yes', 'No'])
    with col2:
        alcohol_consuming = st.selectbox('Alcohol Consumption', ['Yes', 'No'])
    with col3:
        coughing = st.selectbox('Coughing', ['Yes', 'No'])
    
    with col1:
        shortness_of_breath = st.selectbox('Shortness of Breath', ['Yes', 'No'])
    with col2:
        swallowing_difficulty = st.selectbox('Swallowing Difficulty', ['Yes', 'No'])
    with col3:
        chest_pain = st.selectbox('Chest Pain', ['Yes', 'No'])

    # Prediction code
    lung_cancer_diagnosis = ''
    if st.button('Lung Cancer Test Result'):
        user_input = [
            age,
            1 if gender == 'Male' else 0,  # Convert gender to binary
            1 if smoking == 'Yes' else 0,  # Convert smoking to binary
            1 if yellow_fingers == 'Yes' else 0,
            1 if anxiety == 'Yes' else 0,
            1 if peer_pressure == 'Yes' else 0,
            1 if chronic_disease == 'Yes' else 0,
            1 if fatigue == 'Yes' else 0,
            1 if allergy == 'Yes' else 0,
            1 if wheezing == 'Yes' else 0,
            1 if alcohol_consuming == 'Yes' else 0,
            1 if coughing == 'Yes' else 0,
            1 if shortness_of_breath == 'Yes' else 0,
            1 if swallowing_difficulty == 'Yes' else 0,
            1 if chest_pain == 'Yes' else 0
        ]
        
        # Make prediction
        prediction = lung_cancer_model.predict([user_input])
        
        if prediction[0] == 0:
            lung_cancer_diagnosis = 'The model predicts that you have lung cancer.'
        else:
            lung_cancer_diagnosis = 'The model predicts that you do not have lung cancer.'
        
        st.success(lung_cancer_diagnosis)
