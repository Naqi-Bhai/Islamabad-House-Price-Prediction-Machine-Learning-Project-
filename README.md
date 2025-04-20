# Islamabad-House-Price-Prediction-Machine-Learning-Project-
🏡 Islamabad House Price Prediction using Machine Learning
This project aims to predict the prices of houses in Islamabad, Pakistan, using machine learning models. The project includes complete data preprocessing, model training and evaluation, and a Flask-based web application where users can input house details and get real-time price predictions.

🔍 Project Overview
Objective: Build a machine learning model to predict house prices in Islamabad based on features like location, number of bedrooms, bathrooms, and total area (in marlas).
Data Source: Real estate listing dataset containing house details for various cities in Pakistan.
Tech Stack: Python, Pandas, Scikit-learn, Flask, HTML/CSS

🧠 Machine Learning Workflow
  Data Filtering:


Focused on houses in Islamabad listed for sale.

Removed outliers and unnecessary columns.

Normalized prices (in lakhs) for readability.




  Feature Engineering:

Converted categorical location data using One-Hot Encoding.

Scaled numerical features like area, number of bedrooms, and bathrooms.

Replaced low-frequency locations with 'other' to reduce dimensionality.




  Model Selection:

Trained multiple models: Linear Regression, Lasso, Ridge, and Random Forest.

Selected the best model based on the highest R² score on the test set.



  Pipeline:

Used ColumnTransformer and Pipeline to ensure reproducible and clean preprocessing + modeling workflow.

Saved the trained model as isb_house_price_pred.pkl using pickle.



🌐     Flask Web App
The Flask application allows users to:

Select location from a dropdown

Enter house details: area (in marlas), number of bedrooms, and bathrooms

View the predicted price on a result page

The app uses the trained model to make real-time predictions.

🚀 How to Run Locally
Clone the repo:
git clone [https://github.com/yourusername/isb-house-price-prediction.git](https://github.com/Naqi-Bhai/Islamabad-House-Price-Prediction-Machine-Learning-Project-.git)

cd isb-house-price-predictio

Install dependencies:
pip install flask pandas numpy scikit-learn

Run the Flask app:
python app.py

Open your browser and go to http://127.0.0.1:5000/

📊 Sample Output
![image](https://github.com/user-attachments/assets/2b5ed853-0496-4b22-ab78-bc3224a458fa)
