import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the XGBoost model from the pickle file
with open("C:/Users/DIVYA/Desktop/PROJECT IIRS ISRO/groundnut yield prediction/Groundnut_xgb.pkl", 'rb') as f:
    xgboost_model = pickle.load(f)

st.title('YIELD PREDICTION')

# Input fields for features
Year = st.selectbox('Select Year', [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019, 2020, 2021])  # Assuming the years in your dataset
District = st.selectbox('Select District', ['Jamnagar', 'Junagadh', 'Rajkot','Amreli','Bhavnagar'])  # Assuming the districts in your dataset
Area = st.number_input('Area', value=0.0)
Production = st.number_input('Production', value=0.0)
NDVI = st.number_input('NDVI', value=0.0)
EVI = st.number_input('EVI', value=0.0)
LAI = st.number_input('LAI', value=0.0)
FAPAR = st.number_input('FAPAR', value=0.0)
GPP = st.number_input('GPP', value=0.0)
Rainfall = st.number_input('Rainfall', value=0.0)
Temperature = st.number_input('Temperature', value=0.0)
SMI = st.number_input('SMI', value=0.0)

# Prepare input features
input_features = pd.DataFrame({
    'Year': [Year],
    'District': [District],
    'Area': [Area],
    'Production': [Production],
    'NDVI': [NDVI],
    'EVI': [EVI],
    'LAI': [LAI],
    'FAPAR': [FAPAR],
    'GPP': [GPP],
    'Rainfall': [Rainfall],
    'Temperature': [Temperature],
    'SMI': [SMI]
})

# Encoding categorical variables
label_encoder = LabelEncoder()
input_features['District'] = label_encoder.fit_transform(input_features['District'])

# Predict button
if st.button('Predict'):
    # Predict using the loaded model
    prediction = xgboost_model.predict(input_features)
    st.success(f'Predicted Yield: {prediction[0]} tonnes/ha')
