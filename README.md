# Groundnut_yield_prediction
Machine Learning project on Groundnut Yield Prediction

- **Introduction**:

  Groundnut (Arachis hypogea) holds immense economic significance in Gujarat, with the state contributing substantially to India's overall production. During the Kharif season, Gujarat accounts for approximately 50% of India's groundnut output and cultivates around 42% of the total groundnut area in the country. Spread over roughly 2 million hectares, groundnut cultivation in Gujarat yields approximately 2.6 million tonnes annually.

- **Objectives:**
  1) To develop different ML models for yield prediction of Groundnut Crop.
  2) To evaluate the performance of the models for yield prediction.
  3) To develop a web-based dashboard for feature visualisation.  
  4) To deploy the best model for yield prediction in the web platform.

- **Research Questions:**
  
1) What are the Parameters used for Groundnut yield Prediction, and how can they be measured?
2) Which machine learning techniques work best for estimating Groundnut Yield?
3) What effect does the selection of features have on the yield estimating model's performance?
4) How precise crop yield estimation benefits various stakeholders, such as farmers and policymakers?
   
- **Study Area:**
  
  The study area comprises five districts of Gujarat state, focusing on crop-masked based analysis 

- **Data:**
  
  The dataset comprises 22 years of data for five distinct districts, resulting in 13 columns representing each district's name, eight indices (Mean of four months jun-oct), production, and yield. With a total of 110 rows collected from GEE.

  - Independent Variables / Features:
    1) Normalized Difference Vegetation Index (NDVI) -  MODIS 
    2) Enhanced Vegetation Index (EVI) - MODIS
    3) Gross Primary Product (GPP)  - MODIS
    4) Leaf Area Index (LAI) – MODIS
    5) Land Surface Temperature (LST) -  MODIS
    6) Fraction of Photosynthetically Active Radiation (FPAR) - MODIS
    7) Rainfall - CHIRPS
    8) Soil Moisture index (SMI) – NASA (GEE)
    9) Area - Production – Directorate of Agriculture, Gujarat
    10) Production - Directorate of Agriculture, Gujarat

  - Dependent Variable / Target:
    
    Yield – Directorate of Agriculture, Gujarat

- **Methodology:**
  1) Step 1: Understand The Problem Statement
  2) Step 2: Data Collection (GEE)
  3) Step 3: Data Preparation
  4) Step 4: Hyperparameters Tunning
  5) Step 5: Evaluation of Model
  6) Step 6: Training The Model
  7) Step 5: Model Deploy (Stream lit)
  8) Step 6: Dashboard Creation (looker studio)
 
- **Algorithm Used:**
  1) Linear Regression
  2) Ridge Regressor
  3) Lasso Regressor
  4) Decision Tree Regression
  5) Gradient Boosting Regression
  6) Random Forest Regression
  7) XGBoost Regressor
  8) Support Vector Regression (SVR)
 
- **Dashboard By Google Looker Studio:**
  ![image](https://github.com/Drashti16N/Groundnut_yield_prediction/assets/142567844/554e5f61-9994-4362-a1d6-93f3fd9b1824)

  
  https://lookerstudio.google.com/reporting/ec76b4e8-2a47-4e96-95e1-a543a5ad3852

- **Conclusion:**
  1) Accurate Yield Prediction: Crucial for optimizing agricultural practices and boosting local economy.
  2) Data Inputs for Yield Prediction: Combine vegetation indicators and meteorological variables for accurate Predictions.
  3) Regression Model Evaluation: XGBoost yields highest accuracy and R2 Score among nine models.
  4) Enhancing Model Accuracy: Hyperparameter Tunning is used for enhancing accuracy of model’s predictions.
  5) Promoting Sustainable Agriculture: Accurate yield estimation fosters sustainable practices and boosts productivity.













	

	



	
		

	











