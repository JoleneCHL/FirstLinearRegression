import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sklearn
# Define the name of your Streamlit app
st.title("My 1st Linear Regression Deployment")

# Load model
loaded_model = joblib.load('LGBMRegressor-joblib.pkl')

# Define function to make predictions and display results
def predict_charges(age, sex, bmi, children, smoker, region):
    input_data = pd.DataFrame({'age': [age],
                               'sex': [sex],
                               'bmi': [bmi],
                               'children': [children],
                               'smoker': [smoker],
                               'region': [region]})
    prediction = loaded_model.predict(input_data)
    return prediction

# Create Streamlit app
st.title("How much will be the predicted individual medical cost?")
age = st.slider("age", min_value=1, max_value=99, value=1)
sex_options = ['male', 'female']
sex = st.selectbox("sex", sex_options, index=0)
bmi = st.slider("bmi", min_value=0.00000, max_value=35.00000, value=0.00001 , format="%.5f")
children = st.slider("children", min_value=0, max_value=6, value=1)
smoker_options = ['yes', 'no']
smoker = st.selectbox("smoker", smoker_options, index=0)
region_options = ['southeast', 'southwest', 'northwest', 'northeast']
region = st.selectbox("region", region_options, index=0)

# Map the selected sex mode to a numerical value
sex_mapping = {'male': 1, 'female': 0}
sex_mode = sex_mapping[sex]

# Map the selected smoker mode to a numerical value
smoker_mapping = {'yes': 1, 'no': 0}
smoker_mode = smoker_mapping[smoker]

# Map the selected region mode to a numerical value
region_mapping = {'southeast': 2, 'southwest': 1, 'northwest': 0, 'northeast': 3}
region_mode = region_mapping[region]

# Make prediction
prediction = predict_charges(age, sex_mode, bmi, children, smoker_mode, region_mode).round(2)

# Display prediction
st.write("Predicted medical cost:", prediction)
