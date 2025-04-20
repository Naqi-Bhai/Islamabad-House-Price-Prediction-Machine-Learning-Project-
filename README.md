# 🏡 Islamabad House Price Prediction using Machine Learning

This project predicts house prices in Islamabad, Pakistan using machine learning models. It includes data preprocessing, model training, evaluation, and a Flask-based web app for real-time predictions.

---

## 🔍 Project Overview

- **Objective**: Predict the price of a house based on features like location, bedrooms, bathrooms, and area.
- **Data Source**: Real estate dataset for Pakistani cities.
- **Tech Stack**: Python, Pandas, Scikit-learn, Flask, HTML/CSS

---

## 🧠 Machine Learning Workflow

1. **Data Filtering**:
   - Focused on houses in *Islamabad* listed *For Sale*
   - Removed outliers and irrelevant columns
   - Converted price to Lakhs (1 Lakh = 100,000 PKR)

2. **Feature Engineering**:
   - One-Hot Encoding for locations
   - Scaling for numerical features (baths, bedrooms, total area)
   - Replaced infrequent locations with `'other'`

3. **Model Selection**:
   - Trained and compared:
     - Linear Regression
     - Lasso
     - Ridge
     - Random Forest
   - Best model selected using R² Score

4. **Pipeline**:
   - Combined preprocessing and model into a single pipeline
   - Saved the best model using `pickle`

---

## 🌐 Flask Web Application

The Flask app allows users to:

- Select a location
- Enter house area in marlas
- Choose number of bedrooms and bathrooms
- View the predicted house price

---

## 📁 🚀 How to Run Locally

Clone the repo:
git clone [https://github.com/yourusername/isb-house-price-prediction.git](https://github.com/Naqi-Bhai/Islamabad-House-Price-Prediction-Machine-Learning-Project-.git)

Install dependencies:
pip install flask pandas numpy scikit-learn

Run the Flask app:
python app.py

Open your browser and go to http://127.0.0.1:5000/

📊 Sample Output
![image](https://github.com/user-attachments/assets/2b5ed853-0496-4b22-ab78-bc3224a458fa)
