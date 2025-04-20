from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load Model
model = pickle.load(open("isb_house_price_pred.pkl", "rb"))

# Load Data
housing = pd.read_csv("isb_data.csv")

# Extract Unique Locations for Dropdown
locations = sorted(housing["location"].unique())

@app.route("/")
def home():
    return render_template("index.html", house_image="static/house.jpg", locations=locations)

@app.route("/display", methods=["POST"])
def predict():
    location = request.form["location"]
    marla = float(request.form["marla"])
    bathrooms = int(request.form["bathrooms"])
    bedrooms = int(request.form["bedrooms"])
    
    # Convert Marla to Square Feet (1 Marla = 225 sq ft)
    total_area = marla * 225

    # Prepare Data for Prediction
    input_data = pd.DataFrame([[location, bathrooms, bedrooms, total_area]], 
                              columns=["location", "baths", "bedrooms", "Total_Area"])
    
    # Make Prediction
    price_pred = model.predict(input_data)[0]

    return render_template("display.html", 
                           house_image="static/house.jpg", 
                           price=f"{price_pred:.2f}", 
                           marla_entered_by_user=marla, 
                           location=location, 
                           bedrooms_entered_by_user=bedrooms, 
                           bathrooms_entered_by_user=bathrooms)

if __name__ == "__main__":
    app.run(debug=True)
